"""Oracle Integration Cloud tap implementation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import sys
from collections.abc import (
    Mapping,
)
from typing import ClassVar, override

from flext_api import FlextApi, FlextApiModels, FlextApiSettings

from flext_meltano import FlextMeltanoAbstractions
from flext_tap_oracle_oic import (
    ALL_STREAMS,
    FlextTapOracleOicSettings,
    c,
    m,
    p,
    r,
    t,
    u,
)

logger = u.fetch_logger(__name__)


class FlextOracleOicAuthenticator:
    """Real Oracle OIC OAuth2 authenticator implementation."""

    def __init__(self, settings: FlextTapOracleOicSettings) -> None:
        """Initialize authenticator with OAuth2 configuration."""
        self.settings = settings
        self._access_token: str | None = None
        api_config = FlextApiSettings.model_validate({})
        self._api_client = FlextApi(settings=api_config)

    def get_access_token(self) -> p.Result[str]:
        """Get OAuth2 access token using client credentials flow."""
        try:
            token_request_data = "&".join(
                f"{key}={value}"
                for key, value in self.settings.get_token_request_data().items()
            )
            response_result = self._api_client.post(
                self.settings.oauth_token_url,
                data=token_request_data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            if response_result.failure:
                return r[str].fail_op("OAuth2 request", response_result.error)
            response = response_result.value
            if response.status_code >= c.TapOracleOic.HTTP_ERROR_STATUS_THRESHOLD:
                return r[str].fail(
                    f"OAuth2 request failed with status {response.status_code}",
                )
            token_data: t.JsonMapping
            match response.body:
                case dict() as token_dict:
                    token_data = token_dict
                case str() as body_str:
                    token_data = (
                        t.TapOracleOic.CONTAINER_VALUE_MAP_ADAPTER.validate_json(
                            body_str
                        )
                    )
                case _:
                    return r[str].fail("Empty or invalid OAuth response body")
            access_token = token_data.get("access_token")
            match access_token:
                case str() as access_token_str if access_token_str:
                    self._access_token = access_token_str
                    logger.info("OAuth2 access token obtained successfully")
                    return r[str].ok(access_token_str)
                case _:
                    return r[str].fail("No valid access token in response")
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            return r[str].fail_op("OAuth2 authentication", e)


class FlextTapOracleOicClient:
    """Real Oracle Integration Cloud API client implementation."""

    def __init__(
        self,
        settings: FlextTapOracleOicSettings,
        authenticator: FlextOracleOicAuthenticator,
    ) -> None:
        """Initialize OIC API client."""
        self.settings = settings
        self.authenticator = authenticator
        api_config = FlextApiSettings.model_validate({
            "base_url": settings.get_api_base_url(),
            "timeout": settings.timeout,
        })
        self._api_client = FlextApi(settings=api_config)
        self._utilities = u()

    def get(self, endpoint: str) -> p.Result[FlextApiModels.Api.HttpResponse]:
        """Make authenticated GET request to OIC API."""
        url = f"{self.settings.get_api_base_url().rstrip('/')}/{endpoint.lstrip('/')}"
        headers_result = self._get_auth_headers()
        if headers_result.failure:
            return r[FlextApiModels.Api.HttpResponse].fail(
                f"Failed to get auth headers: {headers_result.error}",
            )
        try:
            response_result = self._api_client.get(url, headers=headers_result.value)
            if response_result.failure:
                return r[FlextApiModels.Api.HttpResponse].fail_op("OIC API request", response_result.error)
            response = response_result.value
            if response.status_code >= c.TapOracleOic.HTTP_ERROR_STATUS_THRESHOLD:
                return r[FlextApiModels.Api.HttpResponse].fail(
                    f"OIC API request failed with status {response.status_code}",
                )
            return r[FlextApiModels.Api.HttpResponse].ok(response)
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            return r[FlextApiModels.Api.HttpResponse].fail_op("OIC API request", e)

    def post(
        self,
        endpoint: str,
        data: t.MappingKV[str, t.JsonMapping] | None = None,
    ) -> p.Result[FlextApiModels.Api.HttpResponse]:
        """Make authenticated POST request to OIC API."""
        url = f"{self.settings.get_api_base_url().rstrip('/')}/{endpoint.lstrip('/')}"
        headers_result = self._get_auth_headers()
        if headers_result.failure:
            return r[FlextApiModels.Api.HttpResponse].fail(
                f"Failed to get auth headers: {headers_result.error}",
            )
        try:
            json_body = (
                t.TapOracleOic.CONTAINER_VALUE_MAP_ADAPTER.dump_json(
                    t.TapOracleOic.CONTAINER_VALUE_MAP_ADAPTER.validate_python(data),
                ).decode(c.DEFAULT_ENCODING)
                if data
                else None
            )
            response_result = self._api_client.post(
                url,
                data=json_body,
                headers=headers_result.value,
            )
            if response_result.failure:
                return r[FlextApiModels.Api.HttpResponse].fail(
                    f"OIC API request failed: {response_result.error}",
                )
            response = response_result.value
            if response.status_code >= c.TapOracleOic.HTTP_ERROR_STATUS_THRESHOLD:
                return r[FlextApiModels.Api.HttpResponse].fail(
                    f"OIC API request failed with status {response.status_code}",
                )
            return r[FlextApiModels.Api.HttpResponse].ok(response)
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            return r[FlextApiModels.Api.HttpResponse].fail(
                f"OIC API request failed: {e}",
            )

    def _get_auth_headers(self) -> p.Result[t.StrMapping]:
        """Get authorization headers with OAuth2 token."""
        token_result = self.authenticator.get_access_token()
        if token_result.failure:
            return r[t.StrMapping].fail(
                f"Failed to get access token: {token_result.error}",
            )
        headers: t.MutableStrMapping = dict(self.settings.get_headers())
        headers["Authorization"] = f"Bearer {token_result.value}"
        return r[t.StrMapping].ok(headers)


class FlextTapOracleOic(FlextMeltanoAbstractions):
    """Oracle Integration Cloud tap implementation using flext-oracle-oic."""

    name: ClassVar[str] = "tap-oracle-oic"
    capabilities: ClassVar[t.StrSequence] = ["catalog", "state", "discover"]
    config_jsonschema: ClassVar[t.JsonMapping] = {
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
        settings: t.JsonMapping | None = None,
        validate_config: bool = True,
    ) -> None:
        """Initialize Oracle OIC tap with library composition."""
        super().__init__()
        self._tap_config: t.JsonMapping = dict(settings) if settings is not None else {}
        self._oic_settings = FlextTapOracleOicSettings.model_validate(
            self._tap_config,
            strict=validate_config,
        )
        self._client: FlextTapOracleOicClient | None = None
        self._utilities = u()

    @property
    def oic_settings(self) -> FlextTapOracleOicSettings:
        """Return typed OIC settings."""
        return self._oic_settings

    @property
    def client(self) -> FlextTapOracleOicClient:
        """Get Oracle OIC client instance using flext-oracle-oic."""
        if self._client is None:
            config_dict = self._tap_config
            oic_config_data: t.JsonMapping = {
                "oauth_client_id": str(config_dict["oauth_client_id"]),
                "oauth_client_secret": str(config_dict["oauth_client_secret"]),
                "oauth_token_url": str(config_dict["oauth_token_url"]),
                "oauth_audience": str(
                    config_dict.get("oauth_scope", "urn:opc:resource:consumer:all"),
                ),
                "base_url": str(config_dict["oic_url"]),
                "timeout": u.to_positive_int(
                    config_dict.get("request_timeout"),
                    default=30,
                ),
                "max_retries": u.to_positive_int(
                    config_dict.get("max_retries"),
                    default=3,
                ),
            }
            oic_config = FlextTapOracleOicSettings.model_validate(oic_config_data)
            authenticator = FlextOracleOicAuthenticator(settings=oic_config)
            self._client = FlextTapOracleOicClient(
                settings=oic_config,
                authenticator=authenticator,
            )
        return self._client

    def discover_oic_streams(self) -> t.SequenceOf[m.TapOracleOic.OICBaseStream]:
        """Discover OIC stream class instances for this tap."""
        logger.info("Discovering Oracle OIC streams using consolidated streams")
        stream_names = list(c.TapOracleOic.CORE_STREAMS)
        if self._tap_config.get("include_infrastructure", False):
            stream_names.extend(c.TapOracleOic.INFRASTRUCTURE_STREAMS)
        streams = [
            ALL_STREAMS[stream_name].model_validate({"settings": self._tap_config})
            for stream_name in stream_names
            if stream_name in ALL_STREAMS
        ]
        logger.info("Discovered %s streams from Oracle OIC", len(streams))
        return streams

    @override
    def discover_streams(
        self,
        tap_instance: m.Meltano.TapInstance,
    ) -> p.Result[t.JsonMapping]:
        """Discover stream catalog matching FlextMeltanoAbstractions contract."""
        _ = tap_instance
        streams = self.discover_oic_streams()
        catalog_entries: list[m.Meltano.SingerCatalogEntry] = []
        for stream in streams:
            stream_name = str(getattr(stream, "name", c.IDENTIFIER_UNKNOWN))
            stream_schema_raw: object = getattr(stream, "stream_schema", {})
            stream_schema: t.JsonMapping = (
                t.TapOracleOic.CONTAINER_VALUE_MAP_ADAPTER.validate_python(
                    stream_schema_raw,
                )
                if isinstance(stream_schema_raw, Mapping)
                else {}
            )
            entry_result = u.Meltano.build_catalog_entry(
                stream_name=stream_name,
                schema=stream_schema,
                key_properties=(),
                replication_key=(
                    str(replication_key)
                    if (replication_key := getattr(stream, "replication_key", None))
                    is not None
                    else None
                ),
            )
            if entry_result.failure:
                return r[t.JsonMapping].fail(
                    entry_result.error
                    or f"Failed to build Singer catalog entry for {stream_name}",
                )
            if entry_result.value is not None:
                catalog_entries.append(entry_result.value)
        catalog: t.JsonMapping = (
            t.TapOracleOic.CONTAINER_VALUE_MAP_ADAPTER.validate_python(
                m.Meltano.SingerCatalog(streams=catalog_entries).model_dump(
                    by_alias=True,
                    exclude_defaults=True,
                    exclude_none=True,
                    mode="json",
                )
            )
        )
        return r[t.JsonMapping].ok(
            t.TapOracleOic.CONTAINER_VALUE_MAP_ADAPTER.validate_python({
                "streams": catalog.get("streams", []),
            }),
        )

    def test_connection(self) -> p.Result[bool]:
        """Test connection to Oracle OIC using real API client."""
        try:
            logger.info("Testing Oracle OIC connection")
            test_result = self.client.get("integrations")
            if test_result.success:
                logger.info("Oracle OIC connection test successful")
                return r[bool].ok(value=True)
            error_msg = f"Oracle OIC connection test failed: {test_result.error}"
            logger.error(error_msg)
            return r[bool].fail(error_msg)
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            exception_msg = f"Oracle OIC connection test exception: {e}"
            logger.exception(exception_msg)
            return r[bool].fail(exception_msg)


def main() -> int:
    """Run Oracle OIC tap with proper error handling."""
    exit_code = _validate_and_setup_config()
    if exit_code != 0:
        return exit_code
    settings = dict(_build_config_from_env())
    config_typed: t.JsonMapping = dict(settings)
    tap = FlextTapOracleOic(settings=config_typed)
    try:
        return _execute_tap_command(tap)
    except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
        logger.exception("Oracle OIC tap execution failed")
        err_msg = f"Tap execution failed with error: {type(e).__name__}: {e}"
        logger.warning(err_msg)
        logger.info("Returning 1 - legitimate tap execution failure properly handled")
        return 1


def _build_config_from_env() -> t.StrMapping:
    """Build configuration from environment variables using pydantic-settings."""
    try:
        settings = FlextTapOracleOicSettings.model_validate({})
        return {
            "oauth_client_id": settings.oauth_client_id,
            "oauth_client_secret": settings.oauth_client_secret.get_secret_value(),
            "oauth_token_url": settings.oauth_token_url,
            "oic_url": settings.base_url,
            "oauth_scope": settings.oauth_audience,
        }
    except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
        logger.debug(f"Configuration loading failed: {e}")
        return {}


def _validate_and_setup_config() -> int:
    """Validate required configuration. Returns 0 for success, 1 for error."""
    settings = dict(_build_config_from_env())
    required_config = [
        "oauth_client_id",
        "oauth_client_secret",
        "oauth_token_url",
        "oic_url",
    ]
    missing_config = [key for key in required_config if not settings.get(key)]
    if missing_config:
        logger.error("Missing required configuration: ")
        for key in missing_config:
            logger.error(f"{key} (env var: TAP_ORACLE_OIC_{key.upper()})")
        return 1
    return 0


def _execute_tap_command(tap: FlextTapOracleOic) -> int:
    """Execute appropriate tap command based on arguments."""
    if "--discover" in sys.argv:
        return _execute_discover_command(tap)
    if "--test" in sys.argv:
        return _execute_test_command(tap)
    if "--run" in sys.argv:
        return _execute_run_command(tap)
    return 0


def _execute_discover_command(tap: FlextTapOracleOic) -> int:
    """Execute discovery command."""
    logger.info("Discovering Oracle OIC streams")
    streams = tap.discover_oic_streams()
    catalog = {
        "streams": [
            {
                "tap_stream_id": getattr(
                    stream,
                    "name",
                    c.IDENTIFIER_UNKNOWN,
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


def _execute_test_command(tap: FlextTapOracleOic) -> int:
    """Execute test command."""
    logger.info("Testing Oracle OIC connection")
    result = tap.test_connection()
    return 0 if result.success else 1


def _execute_run_command(_tap: FlextTapOracleOic) -> int:
    """Execute run command."""
    logger.info("Running Oracle OIC data extraction")
    return 0


if __name__ == "__main__":
    sys.exit(main())

__all__: list[str] = [
    "FlextOracleOicAuthenticator",
    "FlextTapOracleOic",
    "FlextTapOracleOicClient",
    "logger",
    "main",
]
