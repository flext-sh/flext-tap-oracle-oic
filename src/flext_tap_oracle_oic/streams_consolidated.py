"""Oracle Integration Cloud - Consolidated Streams.

Consolidated stream implementations removing duplications between core, extended,
infrastructure, and monitoring modules. Follows DRY principles and FLEXT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
"""

from __future__ import annotations

from typing import ClassVar, cast

from singer_sdk import typing as th

from flext_meltano import FlextSingerTypes
from flext_tap_oracle_oic.tap_streams import OICBaseStream

# Initialize FlextSingerTypes for compatibility
flext_singer_types = FlextSingerTypes()


class IntegrationsStream(OICBaseStream):
    """Oracle Integration Cloud Integrations Stream.

    Extracts comprehensive integration metadata including configurations,
    endpoints, triggers, connections, and execution statistics.
    """

    name = "integrations"
    path = "/integrations"
    primary_keys: ClassVar = ["id"]
    replication_key = "lastUpdated"
    api_category = "core"
    requires_design_api = True
    default_sort = "lastUpdated:desc"
    default_expand = "connections,endpoints"

    schema: dict[str, object] = cast(
        "dict[str, object]",
        th.PropertiesList(
            th.Property("id", th.StringType(), description="Integration ID"),
            th.Property("name", th.StringType(), description="Integration name"),
            th.Property("version", th.StringType(), description="Integration version"),
            th.Property(
                "description",
                th.StringType(),
                description="Integration description",
            ),
            th.Property("status", th.StringType(), description="Integration status"),
            th.Property("pattern", th.StringType(), description="Integration pattern"),
            th.Property("style", th.StringType(), description="Integration style"),
            th.Property("created", th.DateTimeType(), description="Creation timestamp"),
            th.Property(
                "lastUpdated",
                th.DateTimeType(),
                description="Last update timestamp",
            ),
            th.Property("createdBy", th.StringType(), description="Created by user"),
            th.Property(
                "lastUpdatedBy",
                th.StringType(),
                description="Last updated by user",
            ),
            th.Property(
                "connections",
                th.ArrayType(th.ObjectType()),
                description="Used connections",
            ),
            th.Property(
                "endpoints",
                th.ArrayType(th.ObjectType()),
                description="Integration endpoints",
            ),
            th.Property(
                "trackingFields",
                th.ArrayType(th.StringType()),
                description="Tracking fields",
            ),
            th.Property(
                "payloadTracking",
                th.BooleanType(),
                description="Payload tracking enabled",
            ),
            th.Property("tracing", th.BooleanType(), description="Tracing enabled"),
            th.Property("lockedBy", th.StringType(), description="Locked by user"),
            th.Property("lockedFlag", th.BooleanType(), description="Is locked"),
            th.Property("projectId", th.StringType(), description="Project ID"),
            th.Property("folderId", th.StringType(), description="Folder ID"),
        ).to_dict(),
    )


class ConnectionsStream(OICBaseStream):
    """Oracle Integration Cloud Connections Stream.

    Extracts adapter connection configurations, security policies,
    and connection properties for integrations.
    """

    name = "connections"
    path = "/connections"
    primary_keys: ClassVar = ["id"]
    replication_key = "lastUpdated"
    api_category = "core"
    requires_design_api = True
    default_sort = "name:asc"

    schema: dict[str, object] = cast(
        "dict[str, object]",
        th.PropertiesList(
            th.Property("id", th.StringType(), description="Connection ID"),
            th.Property("name", th.StringType(), description="Connection name"),
            th.Property(
                "description",
                th.StringType(),
                description="Connection description",
            ),
            th.Property("adapterType", th.StringType(), description="Adapter type"),
            th.Property(
                "adapterDisplayName",
                th.StringType(),
                description="Adapter display name",
            ),
            th.Property(
                "adapterVersion", th.StringType(), description="Adapter version"
            ),
            th.Property("status", th.StringType(), description="Connection status"),
            th.Property("created", th.DateTimeType(), description="Creation timestamp"),
            th.Property(
                "lastUpdated",
                th.DateTimeType(),
                description="Last update timestamp",
            ),
            th.Property("createdBy", th.StringType(), description="Created by user"),
            th.Property(
                "lastUpdatedBy",
                th.StringType(),
                description="Last updated by user",
            ),
            th.Property("connectionUrl", th.StringType(), description="Connection URL"),
            th.Property(
                "securityPolicy", th.StringType(), description="Security policy"
            ),
            th.Property(
                "connectionProperties",
                th.ObjectType(),
                description="Connection properties",
            ),
            th.Property("isValid", th.BooleanType(), description="Connection validity"),
            th.Property("usageCount", th.IntegerType(), description="Usage count"),
            th.Property("lockedBy", th.StringType(), description="Locked by user"),
            th.Property("lockedFlag", th.BooleanType(), description="Is locked"),
        ).to_dict(),
    )


class PackagesStream(OICBaseStream):
    """Oracle Integration Cloud Packages Stream.

    Extracts integration packages for deployment and versioning,
    including package metadata and content information.
    """

    name = "packages"
    path = "/packages"
    primary_keys: ClassVar = ["id"]
    replication_key = "lastUpdated"
    api_category = "core"
    default_sort = "lastUpdated:desc"

    schema: dict[str, object] = cast(
        "dict[str, object]",
        th.PropertiesList(
            th.Property("id", th.StringType(), description="Package ID"),
            th.Property("name", th.StringType(), description="Package name"),
            th.Property(
                "description", th.StringType(), description="Package description"
            ),
            th.Property("version", th.StringType(), description="Package version"),
            th.Property("status", th.StringType(), description="Package status"),
            th.Property("created", th.DateTimeType(), description="Creation timestamp"),
            th.Property(
                "lastUpdated",
                th.DateTimeType(),
                description="Last update timestamp",
            ),
            th.Property("createdBy", th.StringType(), description="Created by user"),
            th.Property(
                "lastUpdatedBy",
                th.StringType(),
                description="Last updated by user",
            ),
            th.Property(
                "integrations",
                th.ArrayType(th.ObjectType()),
                description="Included integrations",
            ),
            th.Property(
                "connections",
                th.ArrayType(th.ObjectType()),
                description="Included connections",
            ),
            th.Property("size", th.IntegerType(), description="Package size"),
            th.Property("projectId", th.StringType(), description="Project ID"),
        ).to_dict(),
    )


class LookupsStream(OICBaseStream):
    """Oracle Integration Cloud Lookups Stream.

    Extracts data transformation lookup tables used in mappings
    and transformations across integrations.
    """

    name = "lookups"
    path = "/lookups"
    primary_keys: ClassVar = ["name"]
    replication_key = "lastUpdated"
    api_category = "core"

    schema: dict[str, object] = cast(
        "dict[str, object]",
        th.PropertiesList(
            th.Property("name", th.StringType(), description="Lookup name"),
            th.Property(
                "description", th.StringType(), description="Lookup description"
            ),
            th.Property("type", th.StringType(), description="Lookup type"),
            th.Property("status", th.StringType(), description="Lookup status"),
            th.Property("created", th.DateTimeType(), description="Creation timestamp"),
            th.Property(
                "lastUpdated",
                th.DateTimeType(),
                description="Last update timestamp",
            ),
            th.Property("createdBy", th.StringType(), description="Created by user"),
            th.Property(
                "lastUpdatedBy",
                th.StringType(),
                description="Last updated by user",
            ),
            th.Property(
                "valueCount",
                th.IntegerType(),
                description="Number of lookup values",
            ),
            th.Property(
                "defaultValue",
                th.StringType(),
                description="Default lookup value",
            ),
            th.Property("isReadOnly", th.BooleanType(), description="Is read-only"),
            th.Property("usageCount", th.IntegerType(), description="Usage count"),
        ).to_dict(),
    )


# INFRASTRUCTURE STREAMS


class LibrariesStream(OICBaseStream):
    """Oracle Integration Cloud Libraries Stream.

    Extracts reusable libraries including JavaScript libraries,
    XSLT stylesheets, and custom functions.
    """

    name = "libraries"
    path = "/libraries"
    primary_keys: ClassVar = ["id"]
    replication_key = "lastUpdated"
    api_category = "infrastructure"

    schema: dict[str, object] = cast(
        "dict[str, object]",
        th.PropertiesList(
            th.Property("id", th.StringType(), description="Library ID"),
            th.Property("name", th.StringType(), description="Library name"),
            th.Property(
                "description", th.StringType(), description="Library description"
            ),
            th.Property("type", th.StringType(), description="Library type"),
            th.Property("status", th.StringType(), description="Library status"),
            th.Property("created", th.DateTimeType(), description="Creation timestamp"),
            th.Property(
                "lastUpdated",
                th.DateTimeType(),
                description="Last update timestamp",
            ),
            th.Property("createdBy", th.StringType(), description="Created by user"),
            th.Property(
                "lastUpdatedBy",
                th.StringType(),
                description="Last updated by user",
            ),
            th.Property("version", th.StringType(), description="Library version"),
            th.Property("size", th.IntegerType(), description="Library size"),
            th.Property("usageCount", th.IntegerType(), description="Usage count"),
            th.Property(
                "functions",
                th.ArrayType(th.StringType()),
                description="Available functions",
            ),
        ).to_dict(),
    )


class CertificatesStream(OICBaseStream):
    """Oracle Integration Cloud Certificates Stream.

    Extracts security certificates used for SSL/TLS connections,
    message encryption, and digital signatures.
    """

    name = "certificates"
    path = "/certificates"
    primary_keys: ClassVar = ["name"]
    replication_key = "lastUpdated"
    api_category = "security"

    schema: dict[str, object] = cast(
        "dict[str, object]",
        th.PropertiesList(
            th.Property("name", th.StringType(), description="Certificate name"),
            th.Property(
                "description",
                th.StringType(),
                description="Certificate description",
            ),
            th.Property("type", th.StringType(), description="Certificate type"),
            th.Property("status", th.StringType(), description="Certificate status"),
            th.Property("created", th.DateTimeType(), description="Creation timestamp"),
            th.Property(
                "lastUpdated",
                th.DateTimeType(),
                description="Last update timestamp",
            ),
            th.Property("createdBy", th.StringType(), description="Created by user"),
            th.Property(
                "expirationDate", th.DateTimeType(), description="Expiration date"
            ),
            th.Property("issuer", th.StringType(), description="Certificate issuer"),
            th.Property("subject", th.StringType(), description="Certificate subject"),
            th.Property("serialNumber", th.StringType(), description="Serial number"),
            th.Property(
                "fingerprint",
                th.StringType(),
                description="Certificate fingerprint",
            ),
            th.Property("usageCount", th.IntegerType(), description="Usage count"),
        ).to_dict(),
    )


class AdaptersStream(OICBaseStream):
    """Oracle Integration Cloud Adapters Stream.

    Extracts available adapter information including versions,
    capabilities, and configuration options.
    """

    name = "adapters"
    path = "/adapters"
    primary_keys: ClassVar = ["id"]
    replication_key = None  # Static metadata
    api_category = "infrastructure"

    schema: dict[str, object] = cast(
        "dict[str, object]",
        th.PropertiesList(
            th.Property("id", th.StringType(), description="Adapter ID"),
            th.Property("name", th.StringType(), description="Adapter name"),
            th.Property(
                "displayName", th.StringType(), description="Adapter display name"
            ),
            th.Property(
                "description", th.StringType(), description="Adapter description"
            ),
            th.Property("version", th.StringType(), description="Adapter version"),
            th.Property("vendor", th.StringType(), description="Adapter vendor"),
            th.Property("category", th.StringType(), description="Adapter category"),
            th.Property(
                "capabilities",
                th.ArrayType(th.StringType()),
                description="Adapter capabilities",
            ),
            th.Property(
                "connectionTypes",
                th.ArrayType(th.StringType()),
                description="Connection types",
            ),
            th.Property("isCustom", th.BooleanType(), description="Is custom adapter"),
            th.Property("isDeprecated", th.BooleanType(), description="Is deprecated"),
            th.Property(
                "documentationUrl",
                th.StringType(),
                description="Documentation URL",
            ),
        ).to_dict(),
    )


# EXTENDED BUSINESS STREAMS


class ProjectsStream(OICBaseStream):
    """Oracle Integration Cloud Projects Stream.

    Extracts project organization data including folder structure,
    permissions, and resource grouping.
    """

    name = "projects"
    path = "/projects"
    primary_keys: ClassVar = ["id"]
    replication_key = "lastUpdated"
    api_category = "extended"
    requires_design_api = True

    schema: dict[str, object] = cast(
        "dict[str, object]",
        th.PropertiesList(
            th.Property("id", th.StringType(), description="Project ID"),
            th.Property("name", th.StringType(), description="Project name"),
            th.Property(
                "description", th.StringType(), description="Project description"
            ),
            th.Property("status", th.StringType(), description="Project status"),
            th.Property("created", th.DateTimeType(), description="Creation timestamp"),
            th.Property(
                "lastUpdated",
                th.DateTimeType(),
                description="Last update timestamp",
            ),
            th.Property("createdBy", th.StringType(), description="Created by user"),
            th.Property(
                "lastUpdatedBy",
                th.StringType(),
                description="Last updated by user",
            ),
            th.Property(
                "folders",
                th.ArrayType(th.ObjectType()),
                description="Project folders",
            ),
            th.Property(
                "integrationCount",
                th.IntegerType(),
                description="Number of integrations",
            ),
            th.Property(
                "connectionCount",
                th.IntegerType(),
                description="Number of connections",
            ),
            th.Property(
                "permissions",
                th.ArrayType(th.ObjectType()),
                description="Project permissions",
            ),
        ).to_dict(),
    )


# MONITORING STREAMS


class ExecutionsStream(OICBaseStream):
    """Oracle Integration Cloud Executions Stream.

    Extracts integration execution data including status,
    performance metrics, and error information.
    """

    name = "executions"
    path = "/monitoring/v1/integrations"
    primary_keys: ClassVar = ["instanceId"]
    replication_key = "startTime"
    api_category = "monitoring"
    requires_monitoring_api = True

    schema: dict[str, object] = cast(
        "dict[str, object]",
        th.PropertiesList(
            th.Property(
                "instanceId", th.StringType(), description="Execution instance ID"
            ),
            th.Property(
                "integrationName", th.StringType(), description="Integration name"
            ),
            th.Property(
                "integrationVersion",
                th.StringType(),
                description="Integration version",
            ),
            th.Property("status", th.StringType(), description="Execution status"),
            th.Property(
                "startTime", th.DateTimeType(), description="Execution start time"
            ),
            th.Property("endTime", th.DateTimeType(), description="Execution end time"),
            th.Property(
                "duration",
                th.IntegerType(),
                description="Execution duration (ms)",
            ),
            th.Property("errorCode", th.StringType(), description="Error code"),
            th.Property("errorMessage", th.StringType(), description="Error message"),
            th.Property("payloadSize", th.IntegerType(), description="Payload size"),
            th.Property(
                "processedRecords",
                th.IntegerType(),
                description="Processed record count",
            ),
        ).to_dict(),
    )


class MetricsStream(OICBaseStream):
    """Oracle Integration Cloud Metrics Stream.

    Extracts performance and usage metrics for integrations,
    connections, and overall system health.
    """

    name = "metrics"
    path = "/monitoring/v1/metrics"
    primary_keys: ClassVar = ["metricId", "timestamp"]
    replication_key = "timestamp"
    api_category = "monitoring"
    requires_monitoring_api = True

    schema: dict[str, object] = cast(
        "dict[str, object]",
        th.PropertiesList(
            th.Property("metricId", th.StringType(), description="Metric ID"),
            th.Property("metricName", th.StringType(), description="Metric name"),
            th.Property("timestamp", th.DateTimeType(), description="Metric timestamp"),
            th.Property("value", th.NumberType(), description="Metric value"),
            th.Property("unit", th.StringType(), description="Metric unit"),
            th.Property("tags", th.ObjectType(), description="Metric tags"),
            th.Property(
                "integrationName",
                th.StringType(),
                description="Related integration",
            ),
            th.Property(
                "connectionName",
                th.StringType(),
                description="Related connection",
            ),
        ).to_dict(),
    )


# CONSOLIDATED STREAM REGISTRY

ALL_STREAMS = {
    # Core business streams
    "integrations": IntegrationsStream,
    "connections": ConnectionsStream,
    "packages": PackagesStream,
    "lookups": LookupsStream,
    # Infrastructure streams
    "libraries": LibrariesStream,
    "certificates": CertificatesStream,
    "adapters": AdaptersStream,
    # Extended business streams
    "projects": ProjectsStream,
    # Monitoring streams
    "executions": ExecutionsStream,
    "metrics": MetricsStream,
}

CORE_STREAMS = ["integrations", "connections", "packages", "lookups", "libraries"]
INFRASTRUCTURE_STREAMS = ["certificates", "adapters"]
EXTENDED_STREAMS = ["projects"]
MONITORING_STREAMS = ["executions", "metrics"]
