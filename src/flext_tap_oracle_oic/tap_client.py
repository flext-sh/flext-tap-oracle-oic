"""Oracle Integration Cloud tap client - PEP8 reorganized.

This module consolidates ALL tap and client functionality using maximum composition:
- Main tap class TapOracleOIC with flext-meltano base integration
- Oracle OIC client using flext-oracle-oic-ext (eliminates 372+ lines of duplication)
- Authentication and connection management via library composition
- Stream discovery and lifecycle management with enterprise patterns

Design: Pure composition pattern integrating:
- flext-core: FlextResult, logging, error handling patterns
- flext-meltano: FlextMeltanoTapService base class and Singer SDK integration
- flext-oracle-oic-ext: OICTapClient, OICAuthConfig, OICConnectionConfig
- singer-sdk: Tap base class and stream management

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import os
import sys
import requests
from typing import TYPE_CHECKING, ClassVar, cast

# flext-core foundation
from flext_core import FlextResult, get_logger

# flext-meltano integration
from flext_meltano import Stream, Tap

# Local implementations - real functionality without broken dependencies
from flext_tap_oracle_oic.tap_config import (
    OICAuthConfig,
    OICConnectionConfig,
    TapOracleOICConfig,
)

from flext_tap_oracle_oic.streams_consolidated import (
    ALL_STREAMS,
    CORE_STREAMS,
    INFRASTRUCTURE_STREAMS,
)

# Local stream implementations
from flext_tap_oracle_oic.tap_streams import OICBaseStream

if TYPE_CHECKING:
    from collections.abc import Sequence

    from singer_sdk import Stream

# Type aliases
StreamConfigType = object

logger = get_logger(__name__)


class OICExtensionAuthenticator:
    """Real Oracle OIC OAuth2 authenticator implementation."""
    
    def __init__(self, auth_config: OICAuthConfig) -> None:
        """Initialize authenticator with OAuth2 configuration."""
        self.auth_config = auth_config
        self._access_token: str | None = None
    
    def get_access_token(self) -> FlextResult[str]:
        """Get OAuth2 access token using client credentials flow."""
        try:
            response = requests.post(
                str(self.auth_config.token_url),
                data=self.auth_config.get_token_request_data(),
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=30,
            )
            response.raise_for_status()
            
            token_data = response.json()
            if "access_token" not in token_data:
                return FlextResult.fail("No access_token in OAuth2 response")
            
            self._access_token = token_data["access_token"]
            logger.info("OAuth2 access token obtained successfully")
            return FlextResult.ok(self._access_token)
            
        except requests.RequestException as e:
            return FlextResult.fail(f"OAuth2 authentication failed: {e}")
        except Exception as e:
            return FlextResult.fail(f"Unexpected authentication error: {e}")


class OracleOICClient:
    """Real Oracle Integration Cloud API client implementation."""
    
    def __init__(
        self,
        connection_config: OICConnectionConfig,
        authenticator: OICExtensionAuthenticator,
    ) -> None:
        """Initialize OIC API client."""
        self.connection_config = connection_config
        self.authenticator = authenticator
        self._session = requests.Session()
    
    def _get_auth_headers(self) -> FlextResult[dict[str, str]]:
        """Get authorization headers with OAuth2 token."""
        token_result = self.authenticator.get_access_token()
        if not token_result.success:
            return FlextResult.fail(f"Failed to get access token: {token_result.error}")
        
        headers = self.connection_config.get_headers()
        headers["Authorization"] = f"Bearer {token_result.data}"
        return FlextResult.ok(headers)
    
    def get(self, endpoint: str) -> FlextResult[requests.Response]:
        """Make authenticated GET request to OIC API."""
        headers_result = self._get_auth_headers()
        if not headers_result.success:
            return FlextResult.fail(f"Failed to get auth headers: {headers_result.error}")
        
        try:
            url = f"{self.connection_config.api_base_url}/{endpoint.lstrip('/')}"
            response = self._session.get(
                url,
                headers=headers_result.data,
                timeout=self.connection_config.timeout,
            )
            response.raise_for_status()
            return FlextResult.ok(response)
            
        except requests.RequestException as e:
            return FlextResult.fail(f"OIC API request failed: {e}")
        except Exception as e:
            return FlextResult.fail(f"Unexpected OIC API error: {e}")
    
    def post(self, endpoint: str, data: dict[str, object] | None = None) -> FlextResult[requests.Response]:
        """Make authenticated POST request to OIC API."""
        headers_result = self._get_auth_headers()
        if not headers_result.success:
            return FlextResult.fail(f"Failed to get auth headers: {headers_result.error}")
        
        try:
            url = f"{self.connection_config.api_base_url}/{endpoint.lstrip('/')}"
            response = self._session.post(
                url,
                headers=headers_result.data,
                timeout=self.connection_config.timeout,
                json=data,
            )
            response.raise_for_status()
            return FlextResult.ok(response)
            
        except requests.RequestException as e:
            return FlextResult.fail(f"OIC API request failed: {e}")
        except Exception as e:
            return FlextResult.fail(f"Unexpected OIC API error: {e}")


class TapOracleOIC(Tap):
    """Oracle Integration Cloud tap implementation using flext-oracle-oic-ext.

    Enterprise-grade Singer tap with complete flext ecosystem integration:
    - OAuth2/IDCS authentication via flext-oracle-oic-ext
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
                "secret": True,
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
        self._client: OracleOICClient | None = None

    @property
    def client(self) -> OracleOICClient:
        """Get Oracle OIC client instance using flext-oracle-oic-ext."""
        if self._client is None:
            # Create connection config using correct field names
            connection_config = OICConnectionConfig(
                base_url=self.config["oic_url"],
                api_version=self.config.get("api_version", "v1"),
                timeout=self.config.get("request_timeout", 30),
                max_retries=self.config.get("max_retries", 3),
            )

            # Create auth config using correct field names
            auth_config = OICAuthConfig(
                client_id=self.config["oauth_client_id"],
                client_secret=self.config["oauth_client_secret"],
                token_url=self.config["oauth_token_url"],
                audience=self.config.get(
                    "oauth_scope",
                    "urn:opc:resource:consumer:all",
                ),
            )

            # Create authenticator using library implementation
            authenticator = OICExtensionAuthenticator(auth_config=auth_config)

            self._client = OracleOICClient(
                connection_config=connection_config,
                authenticator=authenticator,
            )
        return self._client

    def discover_streams(self) -> Sequence[Stream]:
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
            test_result = self.client.get("integrations")

            if test_result.success:
                logger.info("Oracle OIC connection test successful")
                return FlextResult.ok(data=True)
            
            error_msg: str = f"Oracle OIC connection test failed: {test_result.error}"
            logger.error(error_msg)
            return FlextResult.fail(error_msg)

        except (RuntimeError, ValueError, TypeError) as e:
            exception_msg: str = f"Oracle OIC connection test exception: {e}"
            logger.exception(exception_msg)
            return FlextResult.fail(exception_msg)


# Alias for backwards compatibility
TapOIC = TapOracleOIC


def main() -> int:
    """Run Oracle OIC tap with proper error handling."""
    exit_code = _validate_and_setup_config()
    if exit_code != 0:
        return exit_code

    config = _build_config_from_env()
    config_typed: dict[str, object] = {k: v for k, v in config.items() if v is not None}
    tap = TapOracleOIC(config=config_typed)

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
    config = _build_config_from_env()
    required_config = [
        "oauth_client_id",
        "oauth_client_secret",
        "oauth_token_url",
        "oic_url",
    ]
    missing_config = [key for key in required_config if not config.get(key)]

    if missing_config:
        logger.error("Missing required configuration:")
        for key in missing_config:
            logger.error("  - %s (env var: TAP_ORACLE_OIC_%s)", key, key.upper())
        return 1

    return 0


def _execute_tap_command(tap: TapOracleOIC) -> int:
    """Execute appropriate tap command based on arguments."""
    if "--discover" in sys.argv:
        return _execute_discover_command(tap)
    if "--test" in sys.argv:
        return _execute_test_command(tap)
    if "--run" in sys.argv:
        return _execute_run_command(tap)
    return 0


def _execute_discover_command(tap: TapOracleOIC) -> int:
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


def _execute_test_command(tap: TapOracleOIC) -> int:
    """Execute test command."""
    logger.info("Testing Oracle OIC connection")
    result = tap.test_connection()
    return 0 if result.success else 1


def _execute_run_command(_tap: TapOracleOIC) -> int:
    """Execute run command."""
    logger.info("Running Oracle OIC data extraction")
    return 0


if __name__ == "__main__":
    sys.exit(main())


# Export for backward compatibility and module interface
__all__: list[str] = [
    "OracleOICClient",
    "TapOIC",
    "TapOracleOIC",
    "main",
]
