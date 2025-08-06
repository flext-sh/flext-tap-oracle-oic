"""Oracle Integration Cloud - Infrastructure Streams.

Copyright (c) 2025 FLEXT Team. All rights reserved.

Professional infrastructure streams providing comprehensive information about
adapters, libraries, agents, and system components.
"""

from __future__ import annotations

from typing import ClassVar

from flext_meltano import singer_typing as th

from flext_tap_oracle_oic.streams import OICBaseStream


class AdaptersStream(OICBaseStream):
    """OIC Adapters Stream.

    Provides comprehensive information about available adapters, their
    capabilities, versions, and configuration options.

    Features:
        - Complete adapter catalog
        - Version and capability information
        - Configuration templates
        - Compatibility information
    """

    name = "adapters"
    path = "/adapters"
    primary_keys: ClassVar = ["id"]
    replication_key = "lastUpdated"

    schema = th.PropertiesList(
        th.Property("id", th.StringType, description="Adapter ID"),
        th.Property("name", th.StringType, description="Adapter name"),
        th.Property("version", th.StringType, description="Adapter version"),
        th.Property("type", th.StringType, description="Adapter type"),
        th.Property("description", th.StringType, description="Adapter description"),
        th.Property(
            "lastUpdated",
            th.DateTimeType,
            description="Last update timestamp",
        ),
        th.Property(
            "_tap_extracted_at",
            th.DateTimeType,
            description="Extraction timestamp",
        ),
        th.Property(
            "_tap_stream_name",
            th.StringType,
            description="Source stream name",
        ),
    ).to_dict()

    def additional_params(
        self,
        _context: dict[str, object] | None,
    ) -> dict[str, object]:
        """Additional parameters for the request."""
        params: dict[str, object] = {}

        # Adapter type filtering
        adapter_types = self.config.get("adapter_types")
        if adapter_types:
            params["adapterType"] = (
                ",".join(adapter_types)
                if isinstance(adapter_types, list)
                else adapter_types
            )

        return params


class LibrariesStream(OICBaseStream):
    """OIC Libraries Stream.

    Provides information about reusable libraries, their versions,
    and dependencies.

    Features:
        - Library catalog
        - Dependency information
        - Version management
        - Usage statistics
    """

    name = "libraries"
    path = "/libraries"
    primary_keys: ClassVar = ["id"]
    replication_key = "lastUpdated"

    schema = th.PropertiesList(
        th.Property("id", th.StringType, description="Library ID"),
        th.Property("name", th.StringType, description="Library name"),
        th.Property("version", th.StringType, description="Library version"),
        th.Property("type", th.StringType, description="Library type"),
        th.Property("description", th.StringType, description="Library description"),
        th.Property(
            "lastUpdated",
            th.DateTimeType,
            description="Last update timestamp",
        ),
        th.Property(
            "_tap_extracted_at",
            th.DateTimeType,
            description="Extraction timestamp",
        ),
        th.Property(
            "_tap_stream_name",
            th.StringType,
            description="Source stream name",
        ),
    ).to_dict()

    def additional_params(
        self,
        _context: dict[str, object] | None,
    ) -> dict[str, object]:
        """Additional parameters for the request."""
        params: dict[str, object] = {}
        return params


class AgentsStream(OICBaseStream):
    """OIC Agents Stream.

    Provides information about connectivity agents, their status,
    and configuration.

    Features:
        - Agent catalog
        - Status monitoring
        - Configuration details
        - Health information
    """

    name = "agents"
    path = "/agents"
    primary_keys: ClassVar = ["id"]
    replication_key = "lastUpdated"

    schema = th.PropertiesList(
        th.Property("id", th.StringType, description="Agent ID"),
        th.Property("name", th.StringType, description="Agent name"),
        th.Property("status", th.StringType, description="Agent status"),
        th.Property("type", th.StringType, description="Agent type"),
        th.Property("lastHeartbeat", th.DateTimeType, description="Last heartbeat"),
        th.Property(
            "lastUpdated",
            th.DateTimeType,
            description="Last update timestamp",
        ),
        th.Property(
            "_tap_extracted_at",
            th.DateTimeType,
            description="Extraction timestamp",
        ),
        th.Property(
            "_tap_stream_name",
            th.StringType,
            description="Source stream name",
        ),
    ).to_dict()

    def additional_params(
        self,
        _context: dict[str, object] | None,
    ) -> dict[str, object]:
        """Additional parameters for the request."""
        params: dict[str, object] = {}
        return params
