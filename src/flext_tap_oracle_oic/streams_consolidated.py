"""Oracle Integration Cloud - Consolidated Streams.

Consolidated stream implementations removing duplications between core, extended,
infrastructure, and monitoring modules. Follows DRY principles and FLEXT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
"""

from __future__ import annotations

from typing import ClassVar, Protocol

from flext_core.typings import t
from flext_meltano import FlextMeltanoTypes
from pydantic import TypeAdapter

from flext_tap_oracle_oic.tap_streams import OICBaseStream

th = FlextMeltanoTypes()
_SCHEMA_ADAPTER: TypeAdapter[dict[str, t.ContainerValue]] = TypeAdapter(
    dict[str, t.ContainerValue]
)


class _PropertiesListLike(Protocol):
    def to_dict(self) -> dict[str, t.ContainerValue]: ...


def _properties_to_dict(
    properties: _PropertiesListLike,
) -> dict[str, t.ContainerValue]:
    return _SCHEMA_ADAPTER.validate_python(dict(properties.to_dict()))


class IntegrationsStream(OICBaseStream):
    """Oracle Integration Cloud Integrations Stream.

    Extracts complete integration metadata including configurations,
    endpoints, triggers, connections, and execution statistics.
    """

    name: str = "integrations"
    path: str = "/integrations"
    primary_keys: ClassVar[list[str]] = ["id"]
    replication_key: str | None = "lastUpdated"
    api_category: ClassVar[str] = "core"
    requires_design_api: ClassVar[bool] = True
    default_sort: ClassVar[str | None] = "lastUpdated:desc"
    default_expand: ClassVar[str] = "connections,endpoints"
    stream_schema: dict[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Singer.Typing.PropertiesList(
                th.Singer.Typing.Property(
                    "id",
                    th.Singer.Typing.StringType(),
                    description="Integration ID",
                ),
                th.Singer.Typing.Property(
                    "name",
                    th.Singer.Typing.StringType(),
                    description="Integration name",
                ),
                th.Singer.Typing.Property(
                    "version",
                    th.Singer.Typing.StringType(),
                    description="Integration version",
                ),
                th.Singer.Typing.Property(
                    "description",
                    th.Singer.Typing.StringType(),
                    description="Integration description",
                ),
                th.Singer.Typing.Property(
                    "status",
                    th.Singer.Typing.StringType(),
                    description="Integration status",
                ),
                th.Singer.Typing.Property(
                    "pattern",
                    th.Singer.Typing.StringType(),
                    description="Integration pattern",
                ),
                th.Singer.Typing.Property(
                    "style",
                    th.Singer.Typing.StringType(),
                    description="Integration style",
                ),
                th.Singer.Typing.Property(
                    "created",
                    th.Singer.Typing.DateTimeType(),
                    description="Creation timestamp",
                ),
                th.Singer.Typing.Property(
                    "lastUpdated",
                    th.Singer.Typing.DateTimeType(),
                    description="Last update timestamp",
                ),
                th.Singer.Typing.Property(
                    "createdBy",
                    th.Singer.Typing.StringType(),
                    description="Created by user",
                ),
                th.Singer.Typing.Property(
                    "lastUpdatedBy",
                    th.Singer.Typing.StringType(),
                    description="Last updated by user",
                ),
                th.Singer.Typing.Property(
                    "connections",
                    th.Singer.Typing.ArrayType(th.Singer.Typing.ObjectType()),
                    description="Used connections",
                ),
                th.Singer.Typing.Property(
                    "endpoints",
                    th.Singer.Typing.ArrayType(th.Singer.Typing.ObjectType()),
                    description="Integration endpoints",
                ),
                th.Singer.Typing.Property(
                    "trackingFields",
                    th.Singer.Typing.ArrayType(th.Singer.Typing.StringType()),
                    description="Tracking fields",
                ),
                th.Singer.Typing.Property(
                    "payloadTracking",
                    th.Singer.Typing.BooleanType(),
                    description="Payload tracking enabled",
                ),
                th.Singer.Typing.Property(
                    "tracing",
                    th.Singer.Typing.BooleanType(),
                    description="Tracing enabled",
                ),
                th.Singer.Typing.Property(
                    "lockedBy",
                    th.Singer.Typing.StringType(),
                    description="Locked by user",
                ),
                th.Singer.Typing.Property(
                    "lockedFlag",
                    th.Singer.Typing.BooleanType(),
                    description="Is locked",
                ),
                th.Singer.Typing.Property(
                    "projectId",
                    th.Singer.Typing.StringType(),
                    description="Project ID",
                ),
                th.Singer.Typing.Property(
                    "folderId",
                    th.Singer.Typing.StringType(),
                    description="Folder ID",
                ),
            ),
        ),
    )


class ConnectionsStream(OICBaseStream):
    """Oracle Integration Cloud Connections Stream.

    Extracts adapter connection configurations, security policies,
    and connection properties for integrations.
    """

    name: str = "connections"
    path: str = "/connections"
    primary_keys: ClassVar[list[str]] = ["id"]
    replication_key: str | None = "lastUpdated"
    api_category: ClassVar[str] = "core"
    requires_design_api: ClassVar[bool] = True
    default_sort: ClassVar[str | None] = "name:asc"
    stream_schema: dict[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Singer.Typing.PropertiesList(
                th.Singer.Typing.Property(
                    "id",
                    th.Singer.Typing.StringType(),
                    description="Connection ID",
                ),
                th.Singer.Typing.Property(
                    "name",
                    th.Singer.Typing.StringType(),
                    description="Connection name",
                ),
                th.Singer.Typing.Property(
                    "description",
                    th.Singer.Typing.StringType(),
                    description="Connection description",
                ),
                th.Singer.Typing.Property(
                    "adapterType",
                    th.Singer.Typing.StringType(),
                    description="Adapter type",
                ),
                th.Singer.Typing.Property(
                    "adapterDisplayName",
                    th.Singer.Typing.StringType(),
                    description="Adapter display name",
                ),
                th.Singer.Typing.Property(
                    "adapterVersion",
                    th.Singer.Typing.StringType(),
                    description="Adapter version",
                ),
                th.Singer.Typing.Property(
                    "status",
                    th.Singer.Typing.StringType(),
                    description="Connection status",
                ),
                th.Singer.Typing.Property(
                    "created",
                    th.Singer.Typing.DateTimeType(),
                    description="Creation timestamp",
                ),
                th.Singer.Typing.Property(
                    "lastUpdated",
                    th.Singer.Typing.DateTimeType(),
                    description="Last update timestamp",
                ),
                th.Singer.Typing.Property(
                    "createdBy",
                    th.Singer.Typing.StringType(),
                    description="Created by user",
                ),
                th.Singer.Typing.Property(
                    "lastUpdatedBy",
                    th.Singer.Typing.StringType(),
                    description="Last updated by user",
                ),
                th.Singer.Typing.Property(
                    "connectionUrl",
                    th.Singer.Typing.StringType(),
                    description="Connection URL",
                ),
                th.Singer.Typing.Property(
                    "securityPolicy",
                    th.Singer.Typing.StringType(),
                    description="Security policy",
                ),
                th.Singer.Typing.Property(
                    "connectionProperties",
                    th.Singer.Typing.ObjectType(),
                    description="Connection properties",
                ),
                th.Singer.Typing.Property(
                    "isValid",
                    th.Singer.Typing.BooleanType(),
                    description="Connection validity",
                ),
                th.Singer.Typing.Property(
                    "usageCount",
                    th.Singer.Typing.IntegerType(),
                    description="Usage count",
                ),
                th.Singer.Typing.Property(
                    "lockedBy",
                    th.Singer.Typing.StringType(),
                    description="Locked by user",
                ),
                th.Singer.Typing.Property(
                    "lockedFlag",
                    th.Singer.Typing.BooleanType(),
                    description="Is locked",
                ),
            ),
        ),
    )


class PackagesStream(OICBaseStream):
    """Oracle Integration Cloud Packages Stream.

    Extracts integration packages for deployment and versioning,
    including package metadata and content information.
    """

    name: str = "packages"
    path: str = "/packages"
    primary_keys: ClassVar[list[str]] = ["id"]
    replication_key: str | None = "lastUpdated"
    api_category: ClassVar[str] = "core"
    default_sort: ClassVar[str | None] = "lastUpdated:desc"
    stream_schema: dict[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Singer.Typing.PropertiesList(
                th.Singer.Typing.Property(
                    "id",
                    th.Singer.Typing.StringType(),
                    description="Package ID",
                ),
                th.Singer.Typing.Property(
                    "name",
                    th.Singer.Typing.StringType(),
                    description="Package name",
                ),
                th.Singer.Typing.Property(
                    "description",
                    th.Singer.Typing.StringType(),
                    description="Package description",
                ),
                th.Singer.Typing.Property(
                    "version",
                    th.Singer.Typing.StringType(),
                    description="Package version",
                ),
                th.Singer.Typing.Property(
                    "status",
                    th.Singer.Typing.StringType(),
                    description="Package status",
                ),
                th.Singer.Typing.Property(
                    "created",
                    th.Singer.Typing.DateTimeType(),
                    description="Creation timestamp",
                ),
                th.Singer.Typing.Property(
                    "lastUpdated",
                    th.Singer.Typing.DateTimeType(),
                    description="Last update timestamp",
                ),
                th.Singer.Typing.Property(
                    "createdBy",
                    th.Singer.Typing.StringType(),
                    description="Created by user",
                ),
                th.Singer.Typing.Property(
                    "lastUpdatedBy",
                    th.Singer.Typing.StringType(),
                    description="Last updated by user",
                ),
                th.Singer.Typing.Property(
                    "integrations",
                    th.Singer.Typing.ArrayType(th.Singer.Typing.ObjectType()),
                    description="Included integrations",
                ),
                th.Singer.Typing.Property(
                    "connections",
                    th.Singer.Typing.ArrayType(th.Singer.Typing.ObjectType()),
                    description="Included connections",
                ),
                th.Singer.Typing.Property(
                    "size",
                    th.Singer.Typing.IntegerType(),
                    description="Package size",
                ),
                th.Singer.Typing.Property(
                    "projectId",
                    th.Singer.Typing.StringType(),
                    description="Project ID",
                ),
            ),
        ),
    )


class LookupsStream(OICBaseStream):
    """Oracle Integration Cloud Lookups Stream.

    Extracts data transformation lookup tables used in mappings
    and transformations across integrations.
    """

    name: str = "lookups"
    path: str = "/lookups"
    primary_keys: ClassVar[list[str]] = ["name"]
    replication_key: str | None = "lastUpdated"
    api_category: ClassVar[str] = "core"
    stream_schema: dict[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Singer.Typing.PropertiesList(
                th.Singer.Typing.Property(
                    "name",
                    th.Singer.Typing.StringType(),
                    description="Lookup name",
                ),
                th.Singer.Typing.Property(
                    "description",
                    th.Singer.Typing.StringType(),
                    description="Lookup description",
                ),
                th.Singer.Typing.Property(
                    "type",
                    th.Singer.Typing.StringType(),
                    description="Lookup type",
                ),
                th.Singer.Typing.Property(
                    "status",
                    th.Singer.Typing.StringType(),
                    description="Lookup status",
                ),
                th.Singer.Typing.Property(
                    "created",
                    th.Singer.Typing.DateTimeType(),
                    description="Creation timestamp",
                ),
                th.Singer.Typing.Property(
                    "lastUpdated",
                    th.Singer.Typing.DateTimeType(),
                    description="Last update timestamp",
                ),
                th.Singer.Typing.Property(
                    "createdBy",
                    th.Singer.Typing.StringType(),
                    description="Created by user",
                ),
                th.Singer.Typing.Property(
                    "lastUpdatedBy",
                    th.Singer.Typing.StringType(),
                    description="Last updated by user",
                ),
                th.Singer.Typing.Property(
                    "valueCount",
                    th.Singer.Typing.IntegerType(),
                    description="Number of lookup values",
                ),
                th.Singer.Typing.Property(
                    "defaultValue",
                    th.Singer.Typing.StringType(),
                    description="Default lookup value",
                ),
                th.Singer.Typing.Property(
                    "isReadOnly",
                    th.Singer.Typing.BooleanType(),
                    description="Is read-only",
                ),
                th.Singer.Typing.Property(
                    "usageCount",
                    th.Singer.Typing.IntegerType(),
                    description="Usage count",
                ),
            ),
        ),
    )


class LibrariesStream(OICBaseStream):
    """Oracle Integration Cloud Libraries Stream.

    Extracts reusable libraries including JavaScript libraries,
    XSLT stylesheets, and custom functions.
    """

    name: str = "libraries"
    path: str = "/libraries"
    primary_keys: ClassVar[list[str]] = ["id"]
    replication_key: str | None = "lastUpdated"
    api_category: ClassVar[str] = "infrastructure"
    stream_schema: dict[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Singer.Typing.PropertiesList(
                th.Singer.Typing.Property(
                    "id",
                    th.Singer.Typing.StringType(),
                    description="Library ID",
                ),
                th.Singer.Typing.Property(
                    "name",
                    th.Singer.Typing.StringType(),
                    description="Library name",
                ),
                th.Singer.Typing.Property(
                    "description",
                    th.Singer.Typing.StringType(),
                    description="Library description",
                ),
                th.Singer.Typing.Property(
                    "type",
                    th.Singer.Typing.StringType(),
                    description="Library type",
                ),
                th.Singer.Typing.Property(
                    "status",
                    th.Singer.Typing.StringType(),
                    description="Library status",
                ),
                th.Singer.Typing.Property(
                    "created",
                    th.Singer.Typing.DateTimeType(),
                    description="Creation timestamp",
                ),
                th.Singer.Typing.Property(
                    "lastUpdated",
                    th.Singer.Typing.DateTimeType(),
                    description="Last update timestamp",
                ),
                th.Singer.Typing.Property(
                    "createdBy",
                    th.Singer.Typing.StringType(),
                    description="Created by user",
                ),
                th.Singer.Typing.Property(
                    "lastUpdatedBy",
                    th.Singer.Typing.StringType(),
                    description="Last updated by user",
                ),
                th.Singer.Typing.Property(
                    "version",
                    th.Singer.Typing.StringType(),
                    description="Library version",
                ),
                th.Singer.Typing.Property(
                    "size",
                    th.Singer.Typing.IntegerType(),
                    description="Library size",
                ),
                th.Singer.Typing.Property(
                    "usageCount",
                    th.Singer.Typing.IntegerType(),
                    description="Usage count",
                ),
                th.Singer.Typing.Property(
                    "functions",
                    th.Singer.Typing.ArrayType(th.Singer.Typing.StringType()),
                    description="Available functions",
                ),
            ),
        ),
    )


class CertificatesStream(OICBaseStream):
    """Oracle Integration Cloud Certificates Stream.

    Extracts security certificates used for SSL/TLS connections,
    message encryption, and digital signatures.
    """

    name: str = "certificates"
    path: str = "/certificates"
    primary_keys: ClassVar[list[str]] = ["name"]
    replication_key: str | None = "lastUpdated"
    api_category: ClassVar[str] = "security"
    stream_schema: dict[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Singer.Typing.PropertiesList(
                th.Singer.Typing.Property(
                    "name",
                    th.Singer.Typing.StringType(),
                    description="Certificate name",
                ),
                th.Singer.Typing.Property(
                    "description",
                    th.Singer.Typing.StringType(),
                    description="Certificate description",
                ),
                th.Singer.Typing.Property(
                    "type",
                    th.Singer.Typing.StringType(),
                    description="Certificate type",
                ),
                th.Singer.Typing.Property(
                    "status",
                    th.Singer.Typing.StringType(),
                    description="Certificate status",
                ),
                th.Singer.Typing.Property(
                    "created",
                    th.Singer.Typing.DateTimeType(),
                    description="Creation timestamp",
                ),
                th.Singer.Typing.Property(
                    "lastUpdated",
                    th.Singer.Typing.DateTimeType(),
                    description="Last update timestamp",
                ),
                th.Singer.Typing.Property(
                    "createdBy",
                    th.Singer.Typing.StringType(),
                    description="Created by user",
                ),
                th.Singer.Typing.Property(
                    "expirationDate",
                    th.Singer.Typing.DateTimeType(),
                    description="Expiration date",
                ),
                th.Singer.Typing.Property(
                    "issuer",
                    th.Singer.Typing.StringType(),
                    description="Certificate issuer",
                ),
                th.Singer.Typing.Property(
                    "subject",
                    th.Singer.Typing.StringType(),
                    description="Certificate subject",
                ),
                th.Singer.Typing.Property(
                    "serialNumber",
                    th.Singer.Typing.StringType(),
                    description="Serial number",
                ),
                th.Singer.Typing.Property(
                    "fingerprint",
                    th.Singer.Typing.StringType(),
                    description="Certificate fingerprint",
                ),
                th.Singer.Typing.Property(
                    "usageCount",
                    th.Singer.Typing.IntegerType(),
                    description="Usage count",
                ),
            ),
        ),
    )


class AdaptersStream(OICBaseStream):
    """Oracle Integration Cloud Adapters Stream.

    Extracts available adapter information including versions,
    capabilities, and configuration options.
    """

    name: str = "adapters"
    path: str = "/adapters"
    primary_keys: ClassVar[list[str]] = ["id"]
    replication_key: str | None = None
    api_category: ClassVar[str] = "infrastructure"
    stream_schema: dict[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Singer.Typing.PropertiesList(
                th.Singer.Typing.Property(
                    "id",
                    th.Singer.Typing.StringType(),
                    description="Adapter ID",
                ),
                th.Singer.Typing.Property(
                    "name",
                    th.Singer.Typing.StringType(),
                    description="Adapter name",
                ),
                th.Singer.Typing.Property(
                    "displayName",
                    th.Singer.Typing.StringType(),
                    description="Adapter display name",
                ),
                th.Singer.Typing.Property(
                    "description",
                    th.Singer.Typing.StringType(),
                    description="Adapter description",
                ),
                th.Singer.Typing.Property(
                    "version",
                    th.Singer.Typing.StringType(),
                    description="Adapter version",
                ),
                th.Singer.Typing.Property(
                    "vendor",
                    th.Singer.Typing.StringType(),
                    description="Adapter vendor",
                ),
                th.Singer.Typing.Property(
                    "category",
                    th.Singer.Typing.StringType(),
                    description="Adapter category",
                ),
                th.Singer.Typing.Property(
                    "capabilities",
                    th.Singer.Typing.ArrayType(th.Singer.Typing.StringType()),
                    description="Adapter capabilities",
                ),
                th.Singer.Typing.Property(
                    "connectionTypes",
                    th.Singer.Typing.ArrayType(th.Singer.Typing.StringType()),
                    description="Connection types",
                ),
                th.Singer.Typing.Property(
                    "isCustom",
                    th.Singer.Typing.BooleanType(),
                    description="Is custom adapter",
                ),
                th.Singer.Typing.Property(
                    "isDeprecated",
                    th.Singer.Typing.BooleanType(),
                    description="Is deprecated",
                ),
                th.Singer.Typing.Property(
                    "documentationUrl",
                    th.Singer.Typing.StringType(),
                    description="Documentation URL",
                ),
            ),
        ),
    )


class ProjectsStream(OICBaseStream):
    """Oracle Integration Cloud Projects Stream.

    Extracts project organization data including folder structure,
    permissions, and resource grouping.
    """

    name: str = "projects"
    path: str = "/projects"
    primary_keys: ClassVar[list[str]] = ["id"]
    replication_key: str | None = "lastUpdated"
    api_category: ClassVar[str] = "extended"
    requires_design_api: ClassVar[bool] = True
    stream_schema: dict[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Singer.Typing.PropertiesList(
                th.Singer.Typing.Property(
                    "id",
                    th.Singer.Typing.StringType(),
                    description="Project ID",
                ),
                th.Singer.Typing.Property(
                    "name",
                    th.Singer.Typing.StringType(),
                    description="Project name",
                ),
                th.Singer.Typing.Property(
                    "description",
                    th.Singer.Typing.StringType(),
                    description="Project description",
                ),
                th.Singer.Typing.Property(
                    "status",
                    th.Singer.Typing.StringType(),
                    description="Project status",
                ),
                th.Singer.Typing.Property(
                    "created",
                    th.Singer.Typing.DateTimeType(),
                    description="Creation timestamp",
                ),
                th.Singer.Typing.Property(
                    "lastUpdated",
                    th.Singer.Typing.DateTimeType(),
                    description="Last update timestamp",
                ),
                th.Singer.Typing.Property(
                    "createdBy",
                    th.Singer.Typing.StringType(),
                    description="Created by user",
                ),
                th.Singer.Typing.Property(
                    "lastUpdatedBy",
                    th.Singer.Typing.StringType(),
                    description="Last updated by user",
                ),
                th.Singer.Typing.Property(
                    "folders",
                    th.Singer.Typing.ArrayType(th.Singer.Typing.ObjectType()),
                    description="Project folders",
                ),
                th.Singer.Typing.Property(
                    "integrationCount",
                    th.Singer.Typing.IntegerType(),
                    description="Number of integrations",
                ),
                th.Singer.Typing.Property(
                    "connectionCount",
                    th.Singer.Typing.IntegerType(),
                    description="Number of connections",
                ),
                th.Singer.Typing.Property(
                    "permissions",
                    th.Singer.Typing.ArrayType(th.Singer.Typing.ObjectType()),
                    description="Project permissions",
                ),
            ),
        ),
    )


class ExecutionsStream(OICBaseStream):
    """Oracle Integration Cloud Executions Stream.

    Extracts integration execution data including status,
    performance metrics, and error information.
    """

    name: str = "executions"
    path: str = "/monitoring/v1/integrations"
    primary_keys: ClassVar[list[str]] = ["instanceId"]
    replication_key: str | None = "startTime"
    api_category: ClassVar[str] = "monitoring"
    requires_monitoring_api: ClassVar[bool] = True
    stream_schema: dict[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Singer.Typing.PropertiesList(
                th.Singer.Typing.Property(
                    "instanceId",
                    th.Singer.Typing.StringType(),
                    description="Execution instance ID",
                ),
                th.Singer.Typing.Property(
                    "integrationName",
                    th.Singer.Typing.StringType(),
                    description="Integration name",
                ),
                th.Singer.Typing.Property(
                    "integrationVersion",
                    th.Singer.Typing.StringType(),
                    description="Integration version",
                ),
                th.Singer.Typing.Property(
                    "status",
                    th.Singer.Typing.StringType(),
                    description="Execution status",
                ),
                th.Singer.Typing.Property(
                    "startTime",
                    th.Singer.Typing.DateTimeType(),
                    description="Execution start time",
                ),
                th.Singer.Typing.Property(
                    "endTime",
                    th.Singer.Typing.DateTimeType(),
                    description="Execution end time",
                ),
                th.Singer.Typing.Property(
                    "duration",
                    th.Singer.Typing.IntegerType(),
                    description="Execution duration (ms)",
                ),
                th.Singer.Typing.Property(
                    "errorCode",
                    th.Singer.Typing.StringType(),
                    description="Error code",
                ),
                th.Singer.Typing.Property(
                    "errorMessage",
                    th.Singer.Typing.StringType(),
                    description="Error message",
                ),
                th.Singer.Typing.Property(
                    "payloadSize",
                    th.Singer.Typing.IntegerType(),
                    description="Payload size",
                ),
                th.Singer.Typing.Property(
                    "processedRecords",
                    th.Singer.Typing.IntegerType(),
                    description="Processed record count",
                ),
            ),
        ),
    )


class MetricsStream(OICBaseStream):
    """Oracle Integration Cloud Metrics Stream.

    Extracts performance and usage metrics for integrations,
    connections, and overall system healFlextMeltanoTypes.Singer.Typing.
    """

    name: str = "metrics"
    path: str = "/monitoring/v1/metrics"
    primary_keys: ClassVar[list[str]] = ["metricId", "timestamp"]
    replication_key: str | None = "timestamp"
    api_category: ClassVar[str] = "monitoring"
    requires_monitoring_api: ClassVar[bool] = True
    stream_schema: dict[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Singer.Typing.PropertiesList(
                th.Singer.Typing.Property(
                    "metricId",
                    th.Singer.Typing.StringType(),
                    description="Metric ID",
                ),
                th.Singer.Typing.Property(
                    "metricName",
                    th.Singer.Typing.StringType(),
                    description="Metric name",
                ),
                th.Singer.Typing.Property(
                    "timestamp",
                    th.Singer.Typing.DateTimeType(),
                    description="Metric timestamp",
                ),
                th.Singer.Typing.Property(
                    "value",
                    th.Singer.Typing.NumberType(),
                    description="Metric value",
                ),
                th.Singer.Typing.Property(
                    "unit",
                    th.Singer.Typing.StringType(),
                    description="Metric unit",
                ),
                th.Singer.Typing.Property(
                    "tags",
                    th.Singer.Typing.ObjectType(),
                    description="Metric tags",
                ),
                th.Singer.Typing.Property(
                    "integrationName",
                    th.Singer.Typing.StringType(),
                    description="Related integration",
                ),
                th.Singer.Typing.Property(
                    "connectionName",
                    th.Singer.Typing.StringType(),
                    description="Related connection",
                ),
            ),
        ),
    )


ALL_STREAMS: dict[str, type[OICBaseStream]] = {
    "integrations": IntegrationsStream,
    "connections": ConnectionsStream,
    "packages": PackagesStream,
    "lookups": LookupsStream,
    "libraries": LibrariesStream,
    "certificates": CertificatesStream,
    "adapters": AdaptersStream,
    "projects": ProjectsStream,
    "executions": ExecutionsStream,
    "metrics": MetricsStream,
}
CORE_STREAMS = ["integrations", "connections", "packages", "lookups", "libraries"]
INFRASTRUCTURE_STREAMS = ["certificates", "adapters"]
EXTENDED_STREAMS = ["projects"]
MONITORING_STREAMS = ["executions", "metrics"]
