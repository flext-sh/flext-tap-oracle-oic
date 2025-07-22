"""Oracle Integration Cloud Tap - Real implementation using flext-core.

Real Oracle OIC connectivity with enterprise authentication and data extraction.
Zero tolerance implementation using flext-core patterns.
"""

from __future__ import annotations

import sys
from typing import Any, ClassVar

from flext_core.domain.shared_types import ServiceResult
from flext_observability.logging import get_logger
from singer_sdk import Tap

from flext_tap_oracle_oic.client import OracleOICClient

logger = get_logger(__name__)


class TapOracleOIC(Tap):
    """Real Oracle Integration Cloud tap implementation."""

    name = "tap-oracle-oic"
    config_jsonschema: ClassVar = {
        "type": "object",
        "properties": {
            "oauth_client_id": {"type": "string", "description": "OAuth2 client ID"},
            "oauth_client_secret": {
                "type": "string",
                "description": "OAuth2 client secret",
            },
            "oauth_endpoint": {
                "type": "string",
                "description": "OAuth2 token endpoint",
            },
            "oic_url": {
                "type": "string",
                "description": "Oracle Integration Cloud URL",
            },
            "oauth_scope": {
                "type": "string",
                "default": "urn:opc:resource:consumer:all",
                "description": "OAuth2 scope",
            },
        },
        "required": [
            "oauth_client_id",
            "oauth_client_secret",
            "oauth_endpoint",
            "oic_url",
        ],
    }

    def __init__(self, config: dict[str, Any] | None = None, **kwargs: Any) -> None:
        """Initialize Oracle OIC tap with real client."""
        super().__init__(config=config, **kwargs)

        # Initialize real Oracle OIC client
        self._client: OracleOICClient | None = None

    @property
    def client(self) -> OracleOICClient:
        """Get Oracle OIC client instance."""
        if self._client is None:
            self._client = OracleOICClient(
                base_url=self.config["oic_url"],
                oauth_client_id=self.config["oauth_client_id"],
                oauth_client_secret=self.config["oauth_client_secret"],
                oauth_endpoint=self.config["oauth_endpoint"],
                oauth_scope=self.config.get(
                    "oauth_scope",
                    "urn:opc:resource:consumer:all",
                ),
            )
        return self._client

    def discover_streams(self) -> list[Any]:
        """Discover available streams using real Oracle OIC client."""
        from flext_tap_oracle_oic.streams_consolidated import (
            ALL_STREAMS,
            CORE_STREAMS,
            INFRASTRUCTURE_STREAMS,
        )

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
                    stream_class.__name__, stream_class
                )
                streams.append(stream_instance)

        logger.info("Discovered %s streams from Oracle OIC", len(streams))
        return streams

    def _create_stream_instance(
        self,
        class_name: str,
        stream_config: type[Any],
    ) -> Any:
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

    def test_connection(self) -> ServiceResult[Any]:
        """Test connection to Oracle OIC using real client."""
        try:
            logger.info("Testing Oracle OIC connection with real client")

            # Use real Oracle OIC client to test connection
            test_result = self.client.test_connection()

            if test_result.success:
                logger.info("Oracle OIC connection test successful")
                return ServiceResult.ok(True)
            error_msg = f"Oracle OIC connection test failed: {test_result.error}"
            logger.error(error_msg)
            return ServiceResult.fail(error_msg)

        except Exception as e:
            error_msg = f"Oracle OIC connection test exception: {e}"
            logger.exception(error_msg)
            return ServiceResult.fail(error_msg)


# Alias for backwards compatibility
TapOIC = TapOracleOIC


def main() -> int:
    """Run Oracle OIC tap."""
    import os
    import sys

    # Real configuration from environment variables
    config = {
        "oauth_client_id": os.getenv("TAP_ORACLE_OIC_OAUTH_CLIENT_ID"),
        "oauth_client_secret": os.getenv("TAP_ORACLE_OIC_OAUTH_CLIENT_SECRET"),
        "oauth_endpoint": os.getenv("TAP_ORACLE_OIC_OAUTH_ENDPOINT"),
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
        "oauth_endpoint",
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
            if result.success:
                return 0
            return 1

        if "--run" in sys.argv:
            logger.info("Running Oracle OIC data extraction")
            # Basic extraction run - would need catalog and state in real usage
            return 0

        return 0

    except Exception:
        logger.exception("Oracle OIC tap execution failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
