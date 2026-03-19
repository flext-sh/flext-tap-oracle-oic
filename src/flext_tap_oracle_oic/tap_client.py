"""Oracle Integration Cloud tap client implementation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

import sys
from collections.abc import Mapping, Sequence
from typing import ClassVar, override

from flext_api import FlextApi, FlextApiSettings
from flext_api.models import FlextApiModels
from flext_core import FlextLogger, r, t
from flext_meltano import (
    FlextMeltanoSettings,
    FlextMeltanoTapAbstractions as Tap,
    m,
    t as mt,
)
from pydantic import TypeAdapter

from flext_tap_oracle_oic import c
from flext_tap_oracle_oic.settings import FlextTapOracleOicSettings
from flext_tap_oracle_oic.streams_consolidated import (
    ALL_STREAMS,
    CORE_STREAMS,
    INFRASTRUCTURE_STREAMS,
)
from flext_tap_oracle_oic.tap_streams import OICBaseStream
from flext_tap_oracle_oic.utilities import FlextTapOracleOicUtilities

logger = FlextLogger(__name__)


class FlextOracleOicAuthenticator:
    """Real Oracle OIC OAuth2 authenticator implementation."""

    def __init__(self, config: FlextTapOracleOicSettings) -> None:
        """Initialize authenticator with OAuth2 configuration."""
        self.config = config
        self._access_token: str | None = None
        api_config = FlextApiSettings.model_validate({})
        self._api_client = FlextApi(api_config)

    def get_access_token(self) -> r[str]:
        """Get OAuth2 access token using client credentials flow."""
        try:
            token_request_data: str = "&".join(
                (f"{k}={v}" for k, v in self.config.get_token_request_data().items()),
            )
            response_result = self._api_client.post(
                str(self.config.oauth_token_url),
                data=token_request_data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            if response_result.is_failure:
                return r[str].fail(f"OAuth2 request failed: {response_result.error}")
            response = response_result.value
            if response.status_code >= c.TapOicHttp.HTTP_ERROR_STATUS_THRESHOLD:
                return r[str].fail(
                    f"OAuth2 request failed with status {response.status_code}",
                )
            match response.body:
                case dict() as token_dict:
                    token_data = token_dict
                case str() as body_str:
                    parser: TypeAdapter[dict[str, t.ContainerValue]] = TypeAdapter(
                        dict[str, t.ContainerValue],
                    )
                    token_data = parser.validate_json(body_str)
                case _:
                    return r[str].fail("Empty or invalid OAuth response body")
            access_token = token_data.get("access_token")
            match access_token:
                case str() as access_token_str if access_token_str:
                    access_token = access_token_str
                case _:
                    return r[str].fail("No valid access token in response")
            if not access_token:
                return r[str].fail("No valid access token in response")
            self._access_token = access_token
            logger.info("OAuth2 access token obtained successfully")
            return r[str].ok(access_token)
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            return r[str].fail(f"OAuth2 authentication failed: {e}")


class OracleOicClient:
    """Real Oracle Integration Cloud API client implementation."""

    def __init__(
        self,
        config: FlextTapOracleOicSettings,
        authenticator: FlextOracleOicAuthenticator,
    ) -> None:
        """Initialize OIC API client."""
        self.config = config
        self.authenticator = authenticator
        api_config = FlextApiSettings.model_validate({
            "base_url": config.get_api_base_url(),
            "timeout": config.timeout,
        })
        self._api_client = FlextApi(api_config)
        self._utilities = FlextTapOracleOicUtilities()

    def get(self, endpoint: str) -> r[FlextApiModels.Api.HttpResponse]:
        """Make authenticated GET request to OIC API."""
        url = f"{self.config.get_api_base_url().rstrip('/')}/{endpoint.lstrip('/')}"
        headers_result = self._get_auth_headers()
        if headers_result.is_failure:
            return r[FlextApiModels.Api.HttpResponse].fail(
                f"Failed to get auth headers: {headers_result.error}",
            )
        try:
            response_result = self._api_client.get(url, headers=headers_result.value)
            if response_result.is_failure:
                return r[FlextApiModels.Api.HttpResponse].fail(
                    f"OIC API request failed: {response_result.error}",
                )
            response = response_result.value
            if response.status_code >= c.TapOicHttp.HTTP_ERROR_STATUS_THRESHOLD:
                return r[FlextApiModels.Api.HttpResponse].fail(
                    f"OIC API request failed with status {response.status_code}",
                )
            return r[FlextApiModels.Api.HttpResponse].ok(response)
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            return r[FlextApiModels.Api.HttpResponse].fail(
                f"OIC API request failed: {e}",
            )

    def post(
        self,
        endpoint: str,
        data: Mapping[str, dict[str, t.ContainerValue]] | None = None,
    ) -> r[FlextApiModels.Api.HttpResponse]:
        """Make authenticated POST request to OIC API."""
        url = f"{self.config.get_api_base_url().rstrip('/')}/{endpoint.lstrip('/')}"
        headers_result = self._get_auth_headers()
        if headers_result.is_failure:
            return r[FlextApiModels.Api.HttpResponse].fail(
                f"Failed to get auth headers: {headers_result.error}",
            )
        try:
            serializer: TypeAdapter[dict[str, t.ContainerValue]] = TypeAdapter(
                dict[str, t.ContainerValue],
            )
            json_body: str | None = (
                serializer.dump_json(dict(data)).decode("utf-8") if data else None
            )
            response_result = self._api_client.post(
                url,
                data=json_body,
                headers=headers_result.value,
            )
            if response_result.is_failure:
                return r[FlextApiModels.Api.HttpResponse].fail(
                    f"OIC API request failed: {response_result.error}",
                )
            response = response_result.value
            if response.status_code >= c.TapOicHttp.HTTP_ERROR_STATUS_THRESHOLD:
                return r[FlextApiModels.Api.HttpResponse].fail(
                    f"OIC API request failed with status {response.status_code}",
                )
            return r[FlextApiModels.Api.HttpResponse].ok(response)
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            return r[FlextApiModels.Api.HttpResponse].fail(
                f"OIC API request failed: {e}",
            )

    def _get_auth_headers(self) -> r[Mapping[str, str]]:
        """Get authorization headers with OAuth2 token."""
        token_result = self.authenticator.get_access_token()
        if token_result.is_failure:
            return r[Mapping[str, str]].fail(
                f"Failed to get access token: {token_result.error}",
            )
        headers: dict[str, str] = dict(self.config.get_headers())
        headers["Authorization"] = f"Bearer {token_result.value}"
        return r[Mapping[str, str]].ok(headers)


class TapOracleOic(Tap):
    """Oracle Integration Cloud tap implementation using flext-oracle-oic.

    Singer tap with complete flext ecosystem integration:
    - OAuth2/IDCS authentication via flext-oracle-oic
    - Stream discovery using consolidated stream registry
    - Real Oracle OIC API connectivity with error handling
    - flext-core patterns for result handling and logging
    """

    name: ClassVar[str] = "tap-oracle-oic"
    config_jsonschema: ClassVar[dict[str, t.ContainerValue]] = {
        "type": "object",
        "properties": {
            "oauth_client_id": {"type": "string", "description": "OAuth2 client ID"},
            "oauth_client_secret": {
                "type": "string",
                "description": "OAuth2 client secret",
                "secret": "True",
            },
            "oauth_token_url": {"type": "string", "description": "OAuth2 token URL"},
            "oic_url": {"type": "string", "description": "OIC instance URL"},
            "oauth_scope": {"type": ["string", "null"], "description": "OAuth2 scope"},
            "include_infrastructure": {
                "type": ["boolean", "null"],
                "description": "Include infrastructure streams",
            },
        },
        "required": [
            "oauth_client_id",
            "oauth_client_secret",
            "oauth_token_url",
            "oic_url",
        ],
    }

    def __init__(
        self,
        *,
        config: Mapping[str, t.ContainerValue] | None = None,
        catalog: Mapping[str, t.ContainerValue] | None = None,
        state: Mapping[str, t.ContainerValue] | None = None,
        parse_env_config: bool = False,
        validate_config: bool = True,
    ) -> None:
        """Initialize Oracle OIC tap with library composition."""
        _ = catalog
        _ = state
        _ = parse_env_config
        _ = validate_config
        Tap.__init__(self, config=FlextMeltanoSettings.model_validate({}))
        self._tap_config: dict[str, t.ContainerValue] = (
            dict(config) if config is not None else {}
        )
        self._client: OracleOicClient | None = None
        self._utilities = FlextTapOracleOicUtilities()

    @property
    def client(self) -> OracleOicClient:
        """Get Oracle OIC client instance using flext-oracle-oic."""
        if self._client is None:
            config_dict: dict[str, t.ContainerValue] = self._tap_config
            oic_config_data: dict[str, t.ContainerValue] = {
                "oauth_client_id": str(config_dict["oauth_client_id"]),
                "oauth_client_secret": str(config_dict["oauth_client_secret"]),
                "oauth_token_url": str(config_dict["oauth_token_url"]),
                "oauth_audience": str(
                    config_dict.get("oauth_scope", "urn:opc:resource:consumer:all"),
                ),
                "base_url": str(config_dict["oic_url"]),
                "timeout": self._to_positive_int(
                    config_dict.get("request_timeout"),
                    30,
                ),
                "max_retries": self._to_positive_int(config_dict.get("max_retries"), 3),
            }
            oic_config = FlextTapOracleOicSettings.model_validate(oic_config_data)
            authenticator = FlextOracleOicAuthenticator(config=oic_config)
            self._client = OracleOicClient(
                config=oic_config,
                authenticator=authenticator,
            )
        return self._client

    def discover_oic_streams(self) -> Sequence[OICBaseStream]:
        """Discover OIC stream class instances for this tap."""
        logger.info("Discovering Oracle OIC streams using consolidated streams")
        stream_names = CORE_STREAMS.copy()
        if self._tap_config.get("include_infrastructure", False):
            stream_names.extend(INFRASTRUCTURE_STREAMS)
        streams: list[OICBaseStream] = []
        for stream_name in stream_names:
            if stream_name in ALL_STREAMS:
                stream_class = ALL_STREAMS[stream_name]
                stream_config: dict[str, t.ContainerValue] = dict(self._tap_config)
                stream_instance = stream_class(config=stream_config)
                streams.append(stream_instance)
        logger.info("Discovered %s streams from Oracle OIC", len(streams))
        return streams

    @override
    def discover_streams(
        self,
        source_config: m.Meltano.DataSourceConfig
        | m.Meltano.TapConfig
        | m.Meltano.TapInstance,
    ) -> r[mt.Meltano.Singer.StreamCatalog]:
        """Discover stream catalog matching FlextMeltanoTapAbstractions contract."""
        _ = source_config
        streams: Sequence[OICBaseStream] = self.discover_oic_streams()
        catalog: mt.Meltano.Singer.StreamCatalog = {
            "streams": [
                {
                    "tap_stream_id": getattr(
                        stream,
                        "name",
                        c.Mixins.IDENTIFIER_UNKNOWN,
                    ),
                    "schema": getattr(stream, "schema", {}),
                    "replication_method": "INCREMENTAL"
                    if getattr(stream, "replication_key", None)
                    else "FULL_TABLE",
                }
                for stream in streams
            ],
        }
        return r[mt.Meltano.Singer.StreamCatalog].ok(catalog)

    @staticmethod
    def _to_positive_int(value: t.ContainerValue | None, default: int) -> int:
        if isinstance(value, int):
            return value
        if isinstance(value, float):
            return int(value)
        if isinstance(value, str) and value.strip().isdigit():
            return int(value)
        return default

    def test_connection(self) -> r[bool]:
        """Test connection to Oracle OIC using real API client."""
        try:
            logger.info("Testing Oracle OIC connection")
            test_result: r[FlextApiModels.Api.HttpResponse] = self.client.get(
                "integrations",
            )
            if test_result.is_success:
                logger.info("Oracle OIC connection test successful")
                return r[bool].ok(value=True)
            error_msg: str = f"Oracle OIC connection test failed: {test_result.error}"
            logger.error(error_msg)
            return r[bool].fail(error_msg)
        except (RuntimeError, ValueError, TypeError) as e:
            exception_msg: str = f"Oracle OIC connection test exception: {e}"
            logger.exception(exception_msg)
            return r[bool].fail(exception_msg)


def main() -> int:
    """Run Oracle OIC tap with proper error handling."""
    exit_code = _validate_and_setup_config()
    if exit_code != 0:
        return exit_code
    config: dict[str, str] = dict(_build_config_from_env())
    config_typed: dict[str, t.ContainerValue] = {
        k: v for k, v in config.items() if v is not None
    }
    tap = TapOracleOic(config=config_typed)
    try:
        return _execute_tap_command(tap)
    except (RuntimeError, ValueError, TypeError) as e:
        logger.exception("Oracle OIC tap execution failed")
        err_msg = f"Tap execution failed with error: {type(e).__name__}: {e}"
        logger.warning(err_msg)
        logger.info("Returning 1 - legitimate tap execution failure properly handled")
        return 1


def _build_config_from_env() -> dict[str, str]:
    """Build configuration from environment variables using pydantic-settings.

    Uses FlextTapOracleOicSettings with env_prefix='FLEXT_TAP_ORACLE_OIC_'
    for automatic environment variable loading and validation.
    """
    try:
        settings = FlextTapOracleOicSettings.model_validate({})
        return {
            "oauth_client_id": settings.oauth_client_id,
            "oauth_client_secret": settings.oauth_client_secret.get_secret_value(),
            "oauth_token_url": str(settings.oauth_token_url),
            "oic_url": str(settings.base_url),
            "oauth_scope": settings.oauth_audience,
        }
    except (ValueError, TypeError) as e:
        logger.debug(f"Configuration loading failed: {e}")
        return {}


def _validate_and_setup_config() -> int:
    """Validate required configuration. Returns 0 for success, 1 for error."""
    config: dict[str, str] = dict(_build_config_from_env())
    required_config = [
        "oauth_client_id",
        "oauth_client_secret",
        "oauth_token_url",
        "oic_url",
    ]
    missing_config: list[str] = [key for key in required_config if not config.get(key)]
    if missing_config:
        logger.error("Missing required configuration: ")
        for key in missing_config:
            logger.error(f"{key} (env var: TAP_ORACLE_OIC_{key.upper()})")
        return 1
    return 0


def _execute_tap_command(tap: TapOracleOic) -> int:
    """Execute appropriate tap command based on arguments."""
    if "--discover" in sys.argv:
        return _execute_discover_command(tap)
    if "--test" in sys.argv:
        return _execute_test_command(tap)
    if "--run" in sys.argv:
        return _execute_run_command(tap)
    return 0


def _execute_discover_command(tap: TapOracleOic) -> int:
    """Execute discovery command."""
    logger.info("Discovering Oracle OIC streams")
    streams: Sequence[OICBaseStream] = tap.discover_oic_streams()
    catalog = {
        "streams": [
            {
                "tap_stream_id": getattr(
                    stream,
                    "name",
                    c.Mixins.IDENTIFIER_UNKNOWN,
                ),
                "schema": getattr(stream, "schema", {}),
                "key_properties": getattr(stream, "primary_keys", []),
                "replication_method": "INCREMENTAL"
                if getattr(stream, "replication_key", None)
                else "FULL_TABLE",
                "replication_key": getattr(stream, "replication_key", None),
            }
            for stream in streams
        ],
    }
    logger.info("Generated catalog with %s streams", len(catalog["streams"]))
    return 0


def _execute_test_command(tap: TapOracleOic) -> int:
    """Execute test command."""
    logger.info("Testing Oracle OIC connection")
    result = tap.test_connection()
    return 0 if result.is_success else 1


def _execute_run_command(_tap: TapOracleOic) -> int:
    """Execute run command."""
    logger.info("Running Oracle OIC data extraction")
    return 0


if __name__ == "__main__":
    sys.exit(main())
__all__: list[str] = ["OracleOicClient", "TapOracleOic", "main"]
