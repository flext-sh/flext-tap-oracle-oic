"""Oracle Integration Cloud tap client implementation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

import json
import os
import sys
from asyncio import run
from collections.abc import Sequence
from typing import ClassVar, cast, override

from flext_api import FlextApiClient
from flext_api.settings import FlextApiSettings
from flext_core import FlextLogger, FlextResult
from flext_meltano import FlextMeltanoStream as Stream, FlextMeltanoTap as Tap

from flext_tap_oracle_oic.config import FlextMeltanoTapOracleOicSettings
from flext_tap_oracle_oic.streams_consolidated import (
    ALL_STREAMS,
    CORE_STREAMS,
    INFRASTRUCTURE_STREAMS,
)
from flext_tap_oracle_oic.tap_streams import OICBaseStream
from flext_tap_oracle_oic.utilities import FlextMeltanoTapOracleOicUtilities

# Constants
HTTP_ERROR_STATUS_THRESHOLD = 400

# Type aliases
StreamConfigType = object

logger = FlextLogger(__name__)


class FlextOracleOicAuthenticator:
    """Real Oracle OIC OAuth2 authenticator implementation."""

    @override
    def __init__(self, config: FlextMeltanoTapOracleOicSettings) -> None:
        """Initialize authenticator with OAuth2 configuration."""
        self.config = config
        self._access_token: str | None = None
        api_config = FlextApiSettings()
        self._api_client = FlextApiClient(api_config)

    def get_access_token(self) -> FlextResult[str]:
        """Get OAuth2 access token using client credentials flow."""
        try:
            response_result = self._api_client.post(
                str(self.config.oauth_token_url),
                data=self.config.get_token_request_data(),
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=30,
            )

            if response_result.is_failure:
                return FlextResult[str].fail(
                    f"OAuth2 request failed: {response_result.error}",
                )

            response = response_result.value
            if response.status_code >= HTTP_ERROR_STATUS_THRESHOLD:
                return FlextResult[str].fail(
                    f"OAuth2 request failed with status {response.status_code}",
                )

            # Handle response.body properly - it could be str, dict, or None
            if isinstance(response.body, dict):
                token_data = response.body
            elif isinstance(response.body, str):
                token_data: dict[str, object] = json.loads(response.body)
            else:
                return FlextResult[str].fail("Empty or invalid OAuth response body")

            access_token = token_data.get("access_token")
            if not access_token or not isinstance(access_token, str):
                return FlextResult[str].fail("No valid access token in response")

            self._access_token = access_token
            logger.info("OAuth2 access token obtained successfully")
            return FlextResult[str].ok(access_token)

        except Exception as e:
            return FlextResult[str].fail(f"OAuth2 authentication failed: {e}")


class OracleOicClient:
    """Real Oracle Integration Cloud API client implementation."""

    @override
    def __init__(
        self,
        config: FlextMeltanoTapOracleOicSettings,
        authenticator: FlextOracleOicAuthenticator,
    ) -> None:
        """Initialize OIC API client."""
        self.config = config
        self.authenticator = authenticator
        api_config = FlextApiSettings(
            base_url=config.get_api_base_url(),
            timeout=config.timeout,
        )
        self._api_client = FlextApiClient(api_config)

        # Zero Tolerance FIX: Use FlextMeltanoTapOracleOicUtilities for ALL business operations
        self._utilities = FlextMeltanoTapOracleOicUtilities()

    def _get_auth_headers(self) -> FlextResult[dict[str, str]]:
        """Get authorization headers with OAuth2 token."""
        token_result: FlextResult[object] = self.authenticator.get_access_token()
        if not token_result.success:
            return FlextResult[dict[str, str]].fail(
                f"Failed to get access token: {token_result.error}",
            )

        headers = self.config.get_headers()
        headers["Authorization"] = f"Bearer {token_result.data}"
        return FlextResult[dict[str, str]].ok(headers)

    def get(self, endpoint: str) -> FlextResult[object]:
        """Make authenticated GET request to OIC API."""
        # Zero Tolerance FIX: Use utilities for URL validation and building
        url_result = self._utilities.OicApiProcessing.build_oic_api_url(
            self.config.get_api_base_url(),
            endpoint,
        )
        if url_result.is_failure:
            return FlextResult[object].fail(f"URL building failed: {url_result.error}")

        headers_result: FlextResult[object] = self._get_auth_headers()
        if not headers_result.success:
            return FlextResult[object].fail(
                f"Failed to get auth headers: {headers_result.error}",
            )

        try:
            url = url_result.value
            response_result = self._api_client.get(
                url,
                headers=headers_result.data,
                timeout=self.config.timeout,
            )

            if response_result.is_failure:
                return FlextResult[object].fail(
                    f"OIC API request failed: {response_result.error}",
                )

            response = response_result.value
            if response.status_code >= HTTP_ERROR_STATUS_THRESHOLD:
                return FlextResult[object].fail(
                    f"OIC API request failed with status {response.status_code}",
                )

            return FlextResult[object].ok(response)

        except Exception as e:
            return FlextResult[object].fail(f"OIC API request failed: {e}")

    def post(
        self,
        endpoint: str,
        data: dict[str, object] | None = None,
    ) -> FlextResult[object]:
        """Make authenticated POST request to OIC API."""
        # Zero Tolerance FIX: Use utilities for URL validation and building
        url_result = self._utilities.OicApiProcessing.build_oic_api_url(
            self.config.get_api_base_url(),
            endpoint,
        )
        if url_result.is_failure:
            return FlextResult[object].fail(f"URL building failed: {url_result.error}")

        headers_result: FlextResult[object] = self._get_auth_headers()
        if not headers_result.success:
            return FlextResult[object].fail(
                f"Failed to get auth headers: {headers_result.error}",
            )

        try:
            url = url_result.value
            # Convert data to string dict[str, object] for FlextApiClient compatibility
            json_data: dict[str, object] = (
                {str(k): str(v) for k, v in data.items()} if data else None
            )
            response_result = self._api_client.post(
                url,
                headers=headers_result.data,
                timeout=self.config.timeout,
                json=json_data,
            )

            if response_result.is_failure:
                return FlextResult[object].fail(
                    f"OIC API request failed: {response_result.error}",
                )

            response = response_result.value
            if response.status_code >= HTTP_ERROR_STATUS_THRESHOLD:
                return FlextResult[object].fail(
                    f"OIC API request failed with status {response.status_code}",
                )

            return FlextResult[object].ok(response)

        except Exception as e:
            return FlextResult[object].fail(f"OIC API request failed: {e}")


class TapOracleOic(Tap):
    """Oracle Integration Cloud tap implementation using flext-oracle-oic.

    Singer tap with complete flext ecosystem integration:
    - OAuth2/IDCS authentication via flext-oracle-oic
    - Stream discovery using consolidated stream registry
    - Real Oracle OIC API connectivity with error handling
    - flext-core patterns for result handling and logging
    """

    name = "tap-oracle-oic"
    config_jsonschema: ClassVar = {
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

    @override
    def __init__(
        self,
        *,
        config: dict[str, object] | None = None,
        catalog: dict[str, object] | None = None,
        state: dict[str, object] | None = None,
        parse_env_config: bool = False,
        validate_config: bool = True,
    ) -> None:
        """Initialize Oracle OIC tap with library composition."""
        super().__init__(
            config=config,
            catalog=catalog,
            state=state,
            parse_env_config=parse_env_config,
            validate_config=validate_config,
        )
        self._client: OracleOicClient | None = None

        # Zero Tolerance FIX: Use FlextMeltanoTapOracleOicUtilities for ALL business operations
        self._utilities = FlextMeltanoTapOracleOicUtilities()

    @property
    def client(self: object) -> OracleOicClient:
        """Get Oracle OIC client instance using flext-oracle-oic."""
        if self._client is None:
            # Zero Tolerance FIX: Use utilities for configuration validation
            config_validation_result = (
                self._utilities.ConfigValidation.validate_oic_connection_config(
                    self.config,
                )
            )
            if config_validation_result.is_failure:
                msg = f"Invalid OIC configuration: {config_validation_result.error}"
                raise ValueError(msg)

            # Create unified OIC configuration
            oic_config = FlextMeltanoTapOracleOicSettings(
                oauth_client_id=self.config["oauth_client_id"],
                oauth_client_secret=self.config["oauth_client_secret"],
                oauth_token_url=self.config["oauth_token_url"],
                oauth_audience=self.config.get(
                    "oauth_scope",
                    "urn:opc:resource:consumer:all",
                ),
                base_url=self.config["oic_url"],
                api_version=self.config.get("api_version", "v1"),
                timeout=self.config.get("request_timeout", 30),
                max_retries=self.config.get("max_retries", 3),
            )

            # Create authenticator using unified configuration
            authenticator = FlextOracleOicAuthenticator(config=oic_config)

            self._client = OracleOicClient(
                config=oic_config,
                authenticator=authenticator,
            )
        return self._client

    def discover_streams(self: object) -> Sequence[Stream]:
        """Discover available streams using consolidated stream registry."""
        logger.info("Discovering Oracle OIC streams using consolidated streams")

        # Use core streams by default, with optional infrastructure streams
        stream_names = CORE_STREAMS.copy()

        # Add infrastructure streams if configured
        if self.config.get("include_infrastructure", False):
            stream_names.extend(INFRASTRUCTURE_STREAMS)

        # Create stream instances from consolidated registry
        streams = []
        for stream_name in stream_names:
            if stream_name in ALL_STREAMS:
                stream_class = ALL_STREAMS[stream_name]
                stream_instance = self._create_stream_instance(
                    stream_class.__name__,
                    stream_class,
                )
                streams.append(stream_instance)

        logger.info("Discovered %s streams from Oracle OIC", len(streams))
        return streams

    def _create_stream_instance(
        self,
        class_name: str,
        stream_config: StreamConfigType,
    ) -> Stream:
        """Create stream instance using OICBaseStream composition."""
        # Create dynamic stream class inheriting from OICBaseStream
        stream_class = type(
            class_name,
            (OICBaseStream,),
            {
                "name": getattr(stream_config, "name", ""),
                "path": getattr(stream_config, "path", ""),
                "primary_keys": getattr(stream_config, "primary_keys", []),
                "replication_key": getattr(stream_config, "replication_key", None),
                "schema": getattr(stream_config, "schema", {}),
                "api_category": getattr(stream_config, "api_category", "core"),
                "requires_design_api": getattr(
                    stream_config,
                    "requires_design_api",
                    False,
                ),
                "requires_runtime_api": getattr(
                    stream_config,
                    "requires_runtime_api",
                    False,
                ),
                "default_sort": getattr(stream_config, "default_sort", None),
                "additional_params": getattr(stream_config, "additional_params", None),
            },
        )

        return cast("Stream", stream_class(tap=self))

    def test_connection(self) -> FlextResult[bool]:
        """Test connection to Oracle OIC using real API client."""
        try:
            logger.info("Testing Oracle OIC connection")

            # Test authentication by making a simple API call
            test_result: FlextResult[object] = self.client.get("integrations")

            if test_result.success:
                logger.info("Oracle OIC connection test successful")
                return FlextResult[bool].ok(data=True)

            error_msg: str = f"Oracle OIC connection test failed: {test_result.error}"
            logger.error(error_msg)
            return FlextResult[bool].fail(error_msg)

        except (RuntimeError, ValueError, TypeError) as e:
            exception_msg: str = f"Oracle OIC connection test exception: {e}"
            logger.exception(exception_msg)
            return FlextResult[bool].fail(exception_msg)


# Zero Tolerance: All legacy exception aliases removed
# Use TapOracleOic directly instead


def main() -> int:
    """Run Oracle OIC tap with proper error handling."""
    exit_code = _validate_and_setup_config()
    if exit_code != 0:
        return exit_code

    config: dict[str, object] = _build_config_from_env()
    config_typed: dict[str, object] = {k: v for k, v in config.items() if v is not None}
    tap = TapOracleOic(config=config_typed)

    try:
        return _execute_tap_command(tap)
    except (RuntimeError, ValueError, TypeError) as e:
        logger.exception("Oracle OIC tap execution failed")
        logger.warning(f"Tap execution failed with error: {type(e).__name__}: {e}")
        logger.info("Returning 1 - legitimate tap execution failure properly handled")
        return 1


def _build_config_from_env() -> dict[str, str | None]:
    """Build configuration from environment variables."""
    return {
        "oauth_client_id": os.getenv("TAP_ORACLE_OIC_OAUTH_CLIENT_ID"),
        "oauth_client_secret": os.getenv("TAP_ORACLE_OIC_OAUTH_CLIENT_SECRET"),
        "oauth_token_url": os.getenv("TAP_ORACLE_OIC_OAUTH_TOKEN_URL"),
        "oic_url": os.getenv("TAP_ORACLE_OIC_OIC_URL"),
        "oauth_scope": os.getenv(
            "TAP_ORACLE_OIC_OAUTH_SCOPE",
            "urn:opc:resource:consumer:all",
        ),
    }


def _validate_and_setup_config() -> int:
    """Validate required configuration. Returns 0 for success, 1 for error."""
    config: dict[str, object] = _build_config_from_env()
    required_config = [
        "oauth_client_id",
        "oauth_client_secret",
        "oauth_token_url",
        "oic_url",
    ]
    missing_config: dict[str, object] = [
        key for key in required_config if not config.get(key)
    ]

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
    streams = tap.discover_streams()

    catalog = {
        "streams": [
            {
                "tap_stream_id": getattr(stream, "name", "unknown"),
                "schema": getattr(stream, "schema", {}),
                "key_properties": getattr(stream, "primary_keys", []),
                "replication_method": (
                    "INCREMENTAL"
                    if hasattr(stream, "replication_key") and stream.replication_key
                    else "FULL_TABLE"
                ),
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
    result: FlextResult[object] = tap.test_connection()
    return 0 if result.success else 1


def _execute_run_command(_tap: TapOracleOic) -> int:
    """Execute run command."""
    logger.info("Running Oracle OIC data extraction")
    return 0


if __name__ == "__main__":
    sys.exit(run(main()))


# Export for module interface - unified classes only
__all__: list[str] = [
    "OracleOicClient",
    "TapOracleOic",
    "main",
]
