"""Oracle Integration Cloud Tap - Real implementation using flext-core.

Real Oracle OIC connectivity with enterprise authentication and data extraction.
Zero tolerance implementation using flext-core patterns.
"""

from __future__ import annotations

import os
import sys
from typing import Any, ClassVar

# Import from flext-core for foundational patterns (standardized)
from flext_core import (
    FlextResult,
    get_logger,
)

# Import generic interfaces from flext-meltano
from flext_meltano import Tap
from flext_meltano.common_schemas import create_oracle_oic_tap_schema
from flext_oracle_oic_ext.oic_patterns import (
    OICAuthConfig,
    OICConnectionConfig,
    OICTapAuthenticator,
    OICTapClient,
)

from flext_tap_oracle_oic.streams_consolidated import (
    ALL_STREAMS,
    CORE_STREAMS,
    INFRASTRUCTURE_STREAMS,
)

# Alias for backward compatibility
OracleOICClient = OICTapClient

logger = get_logger(__name__)


class TapOracleOIC(Tap):
    """Real Oracle Integration Cloud tap implementation."""

    name = "tap-oracle-oic"
    config_jsonschema: ClassVar = create_oracle_oic_tap_schema().to_dict()

    def __init__(
        self,
        *,
        config: dict[str, Any] | None = None,
        catalog: dict[str, Any] | None = None,
        state: dict[str, Any] | None = None,
        parse_env_config: bool = False,
        validate_config: bool = True,
    ) -> None:
        """Initialize Oracle OIC tap with real client."""
        super().__init__(
            config=config,
            catalog=catalog,
            state=state,
            parse_env_config=parse_env_config,
            validate_config=validate_config,
        )

        # Initialize real Oracle OIC client
        self._client: OracleOICClient | None = None

    @property
    def client(self) -> OracleOICClient:
        """Get Oracle OIC client instance."""
        if self._client is None:
            # Create connection config using real library types
            connection_config = OICConnectionConfig(
                base_url=self.config["oic_url"],
                api_version=self.config.get("api_version", "v1"),
                request_timeout=self.config.get("request_timeout", 30),
                max_retries=self.config.get("max_retries", 3),
            )

            # Create auth config using real library types
            auth_config = OICAuthConfig(
                oauth_client_id=self.config["oauth_client_id"],
                oauth_client_secret=self.config["oauth_client_secret"],
                oauth_token_url=self.config["oauth_token_url"],
                oauth_scope=self.config.get(
                    "oauth_scope",
                    "urn:opc:resource:consumer:all",
                ),
            )

            # Create authenticator using real library types
            authenticator = OICTapAuthenticator(auth_config=auth_config)

            self._client = OracleOICClient(
                connection_config=connection_config,
                authenticator=authenticator,
            )
        return self._client

    def discover_streams(self) -> list[Any]:
        """Discover available streams using real Oracle OIC client."""
        logger.info("Discovering Oracle OIC streams using consolidated streams")

        # Use core streams by default, with optional infrastructure streams
        stream_names = CORE_STREAMS.copy()

        # Add infrastructure streams if configured
        if self.config.get("include_infrastructure", False):
            stream_names.extend(INFRASTRUCTURE_STREAMS)

        # Create real stream instances from consolidated registry
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
        stream_config: type[Any],
    ) -> object:
        """Create real stream instance using OICBaseStream."""
        from flext_tap_oracle_oic.streams import OICBaseStream

        # Create dynamic stream class inheriting from OICBaseStream
        stream_class = type(
            class_name,
            (OICBaseStream,),
            {
                "name": stream_config.name,
                "path": stream_config.path,
                "primary_keys": stream_config.primary_keys,
                "replication_key": getattr(stream_config, "replication_key", None),
                "schema": stream_config.schema,
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

        return stream_class(tap=self)

    def test_connection(self) -> FlextResult[Any]:
        """Test connection to Oracle OIC using real client."""
        try:
            logger.info("Testing Oracle OIC connection with real client")

            # Use real Oracle OIC client to test authentication
            auth_result = self.client.get_authenticated_session()

            if auth_result.is_success:
                logger.info("Oracle OIC connection test successful")
                return FlextResult.ok(True)
            error_msg = f"Oracle OIC connection test failed: {auth_result.error}"
            logger.error(error_msg)
            return FlextResult.fail(error_msg)

        except (RuntimeError, ValueError, TypeError) as e:
            error_msg = f"Oracle OIC connection test exception: {e}"
            logger.exception(error_msg)
            return FlextResult.fail(error_msg)


# Alias for backwards compatibility
TapOIC = TapOracleOIC


def main() -> int:
    """Run Oracle OIC tap."""
    # Real configuration from environment variables
    config = {
        "oauth_client_id": os.getenv("TAP_ORACLE_OIC_OAUTH_CLIENT_ID"),
        "oauth_client_secret": os.getenv("TAP_ORACLE_OIC_OAUTH_CLIENT_SECRET"),
        "oauth_token_url": os.getenv("TAP_ORACLE_OIC_OAUTH_TOKEN_URL"),
        "oic_url": os.getenv("TAP_ORACLE_OIC_OIC_URL"),
        "oauth_scope": os.getenv(
            "TAP_ORACLE_OIC_OAUTH_SCOPE",
            "urn:opc:resource:consumer:all",
        ),
    }

    # Validate required configuration
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

    tap = TapOracleOIC(config=config)

    try:
        if "--discover" in sys.argv:
            logger.info("Discovering Oracle OIC streams")
            streams = tap.discover_streams()

            # Convert stream objects to Singer catalog format
            catalog = {
                "streams": [
                    {
                        "tap_stream_id": stream.name,
                        "schema": stream.schema,
                        "key_properties": stream.primary_keys,
                        "replication_method": (
                            "INCREMENTAL"
                            if hasattr(stream, "replication_key")
                            and stream.replication_key
                            else "FULL_TABLE"
                        ),
                        "replication_key": getattr(stream, "replication_key", None),
                    }
                    for stream in streams
                ],
            }
            logger.info("Generated catalog with %s streams", len(catalog["streams"]))
            return 0

        if "--test" in sys.argv:
            logger.info("Testing Oracle OIC connection")
            result = tap.test_connection()
            if result.is_success:
                return 0
            return 1

        if "--run" in sys.argv:
            logger.info("Running Oracle OIC data extraction")
            # Basic extraction run - would need catalog and state in real usage
            return 0

        return 0

    except (RuntimeError, ValueError, TypeError):
        logger.exception("Oracle OIC tap execution failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
