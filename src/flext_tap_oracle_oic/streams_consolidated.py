"""Oracle Integration Cloud - Consolidated Streams.

Consolidated stream implementations removing duplications between core, extended,
infrastructure, and monitoring modules. Follows DRY principles and FLEXT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import ClassVar

from pydantic import TypeAdapter

from flext_tap_oracle_oic import OICBaseStream, TapOracleOicPrivate, t

th = t()
_SCHEMA_ADAPTER: TypeAdapter[Mapping[str, t.ContainerValue]] = TypeAdapter(
    Mapping[str, t.ContainerValue]
)


def _properties_to_dict(
    properties: TapOracleOicPrivate.PropertiesListLike,
) -> Mapping[str, t.ContainerValue]:
    return _SCHEMA_ADAPTER.validate_python(dict(properties.to_dict()))


class IntegrationsStream(OICBaseStream):
    """Oracle Integration Cloud Integrations Stream.

    Extracts complete integration metadata including configurations,
    endpoints, triggers, connections, and execution statistics.
    """

    name: str = "integrations"
    path: str = "/integrations"
    primary_keys: ClassVar[Sequence[str]] = ["id"]
    replication_key: str | None = "lastUpdated"
    api_category: ClassVar[str] = "core"
    requires_design_api: ClassVar[bool] = True
    default_sort: ClassVar[str | None] = "lastUpdated:desc"
    default_expand: ClassVar[str] = "connections,endpoints"
    stream_schema: Mapping[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Meltano.Singer.Typing.PropertiesList(
                th.Meltano.Singer.Typing.Property(
                    "id",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Integration ID",
                ),
                th.Meltano.Singer.Typing.Property(
                    "name",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Integration name",
                ),
                th.Meltano.Singer.Typing.Property(
                    "version",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Integration version",
                ),
                th.Meltano.Singer.Typing.Property(
                    "description",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Integration description",
                ),
                th.Meltano.Singer.Typing.Property(
                    "status",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Integration status",
                ),
                th.Meltano.Singer.Typing.Property(
                    "pattern",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Integration pattern",
                ),
                th.Meltano.Singer.Typing.Property(
                    "style",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Integration style",
                ),
                th.Meltano.Singer.Typing.Property(
                    "created",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Creation timestamp",
                ),
                th.Meltano.Singer.Typing.Property(
                    "lastUpdated",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Last update timestamp",
                ),
                th.Meltano.Singer.Typing.Property(
                    "createdBy",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Created by user",
                ),
                th.Meltano.Singer.Typing.Property(
                    "lastUpdatedBy",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Last updated by user",
                ),
                th.Meltano.Singer.Typing.Property(
                    "connections",
                    th.Meltano.Singer.Typing.ArrayType(
                        th.Meltano.Singer.Typing.ObjectType()
                    ),
                    description="Used connections",
                ),
                th.Meltano.Singer.Typing.Property(
                    "endpoints",
                    th.Meltano.Singer.Typing.ArrayType(
                        th.Meltano.Singer.Typing.ObjectType()
                    ),
                    description="Integration endpoints",
                ),
                th.Meltano.Singer.Typing.Property(
                    "trackingFields",
                    th.Meltano.Singer.Typing.ArrayType(
                        th.Meltano.Singer.Typing.StringType()
                    ),
                    description="Tracking fields",
                ),
                th.Meltano.Singer.Typing.Property(
                    "payloadTracking",
                    th.Meltano.Singer.Typing.BooleanType(),
                    description="Payload tracking enabled",
                ),
                th.Meltano.Singer.Typing.Property(
                    "tracing",
                    th.Meltano.Singer.Typing.BooleanType(),
                    description="Tracing enabled",
                ),
                th.Meltano.Singer.Typing.Property(
                    "lockedBy",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Locked by user",
                ),
                th.Meltano.Singer.Typing.Property(
                    "lockedFlag",
                    th.Meltano.Singer.Typing.BooleanType(),
                    description="Is locked",
                ),
                th.Meltano.Singer.Typing.Property(
                    "projectId",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Project ID",
                ),
                th.Meltano.Singer.Typing.Property(
                    "folderId",
                    th.Meltano.Singer.Typing.StringType(),
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
    primary_keys: ClassVar[Sequence[str]] = ["id"]
    replication_key: str | None = "lastUpdated"
    api_category: ClassVar[str] = "core"
    requires_design_api: ClassVar[bool] = True
    default_sort: ClassVar[str | None] = "name:asc"
    stream_schema: Mapping[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Meltano.Singer.Typing.PropertiesList(
                th.Meltano.Singer.Typing.Property(
                    "id",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Connection ID",
                ),
                th.Meltano.Singer.Typing.Property(
                    "name",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Connection name",
                ),
                th.Meltano.Singer.Typing.Property(
                    "description",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Connection description",
                ),
                th.Meltano.Singer.Typing.Property(
                    "adapterType",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Adapter type",
                ),
                th.Meltano.Singer.Typing.Property(
                    "adapterDisplayName",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Adapter display name",
                ),
                th.Meltano.Singer.Typing.Property(
                    "adapterVersion",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Adapter version",
                ),
                th.Meltano.Singer.Typing.Property(
                    "status",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Connection status",
                ),
                th.Meltano.Singer.Typing.Property(
                    "created",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Creation timestamp",
                ),
                th.Meltano.Singer.Typing.Property(
                    "lastUpdated",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Last update timestamp",
                ),
                th.Meltano.Singer.Typing.Property(
                    "createdBy",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Created by user",
                ),
                th.Meltano.Singer.Typing.Property(
                    "lastUpdatedBy",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Last updated by user",
                ),
                th.Meltano.Singer.Typing.Property(
                    "connectionUrl",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Connection URL",
                ),
                th.Meltano.Singer.Typing.Property(
                    "securityPolicy",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Security policy",
                ),
                th.Meltano.Singer.Typing.Property(
                    "connectionProperties",
                    th.Meltano.Singer.Typing.ObjectType(),
                    description="Connection properties",
                ),
                th.Meltano.Singer.Typing.Property(
                    "isValid",
                    th.Meltano.Singer.Typing.BooleanType(),
                    description="Connection validity",
                ),
                th.Meltano.Singer.Typing.Property(
                    "usageCount",
                    th.Meltano.Singer.Typing.IntegerType(),
                    description="Usage count",
                ),
                th.Meltano.Singer.Typing.Property(
                    "lockedBy",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Locked by user",
                ),
                th.Meltano.Singer.Typing.Property(
                    "lockedFlag",
                    th.Meltano.Singer.Typing.BooleanType(),
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
    primary_keys: ClassVar[Sequence[str]] = ["id"]
    replication_key: str | None = "lastUpdated"
    api_category: ClassVar[str] = "core"
    default_sort: ClassVar[str | None] = "lastUpdated:desc"
    stream_schema: Mapping[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Meltano.Singer.Typing.PropertiesList(
                th.Meltano.Singer.Typing.Property(
                    "id",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Package ID",
                ),
                th.Meltano.Singer.Typing.Property(
                    "name",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Package name",
                ),
                th.Meltano.Singer.Typing.Property(
                    "description",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Package description",
                ),
                th.Meltano.Singer.Typing.Property(
                    "version",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Package version",
                ),
                th.Meltano.Singer.Typing.Property(
                    "status",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Package status",
                ),
                th.Meltano.Singer.Typing.Property(
                    "created",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Creation timestamp",
                ),
                th.Meltano.Singer.Typing.Property(
                    "lastUpdated",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Last update timestamp",
                ),
                th.Meltano.Singer.Typing.Property(
                    "createdBy",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Created by user",
                ),
                th.Meltano.Singer.Typing.Property(
                    "lastUpdatedBy",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Last updated by user",
                ),
                th.Meltano.Singer.Typing.Property(
                    "integrations",
                    th.Meltano.Singer.Typing.ArrayType(
                        th.Meltano.Singer.Typing.ObjectType()
                    ),
                    description="Included integrations",
                ),
                th.Meltano.Singer.Typing.Property(
                    "connections",
                    th.Meltano.Singer.Typing.ArrayType(
                        th.Meltano.Singer.Typing.ObjectType()
                    ),
                    description="Included connections",
                ),
                th.Meltano.Singer.Typing.Property(
                    "size",
                    th.Meltano.Singer.Typing.IntegerType(),
                    description="Package size",
                ),
                th.Meltano.Singer.Typing.Property(
                    "projectId",
                    th.Meltano.Singer.Typing.StringType(),
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
    primary_keys: ClassVar[Sequence[str]] = ["name"]
    replication_key: str | None = "lastUpdated"
    api_category: ClassVar[str] = "core"
    stream_schema: Mapping[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Meltano.Singer.Typing.PropertiesList(
                th.Meltano.Singer.Typing.Property(
                    "name",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Lookup name",
                ),
                th.Meltano.Singer.Typing.Property(
                    "description",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Lookup description",
                ),
                th.Meltano.Singer.Typing.Property(
                    "type",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Lookup type",
                ),
                th.Meltano.Singer.Typing.Property(
                    "status",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Lookup status",
                ),
                th.Meltano.Singer.Typing.Property(
                    "created",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Creation timestamp",
                ),
                th.Meltano.Singer.Typing.Property(
                    "lastUpdated",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Last update timestamp",
                ),
                th.Meltano.Singer.Typing.Property(
                    "createdBy",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Created by user",
                ),
                th.Meltano.Singer.Typing.Property(
                    "lastUpdatedBy",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Last updated by user",
                ),
                th.Meltano.Singer.Typing.Property(
                    "valueCount",
                    th.Meltano.Singer.Typing.IntegerType(),
                    description="Number of lookup values",
                ),
                th.Meltano.Singer.Typing.Property(
                    "defaultValue",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Default lookup value",
                ),
                th.Meltano.Singer.Typing.Property(
                    "isReadOnly",
                    th.Meltano.Singer.Typing.BooleanType(),
                    description="Is read-only",
                ),
                th.Meltano.Singer.Typing.Property(
                    "usageCount",
                    th.Meltano.Singer.Typing.IntegerType(),
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
    primary_keys: ClassVar[Sequence[str]] = ["id"]
    replication_key: str | None = "lastUpdated"
    api_category: ClassVar[str] = "infrastructure"
    stream_schema: Mapping[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Meltano.Singer.Typing.PropertiesList(
                th.Meltano.Singer.Typing.Property(
                    "id",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Library ID",
                ),
                th.Meltano.Singer.Typing.Property(
                    "name",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Library name",
                ),
                th.Meltano.Singer.Typing.Property(
                    "description",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Library description",
                ),
                th.Meltano.Singer.Typing.Property(
                    "type",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Library type",
                ),
                th.Meltano.Singer.Typing.Property(
                    "status",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Library status",
                ),
                th.Meltano.Singer.Typing.Property(
                    "created",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Creation timestamp",
                ),
                th.Meltano.Singer.Typing.Property(
                    "lastUpdated",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Last update timestamp",
                ),
                th.Meltano.Singer.Typing.Property(
                    "createdBy",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Created by user",
                ),
                th.Meltano.Singer.Typing.Property(
                    "lastUpdatedBy",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Last updated by user",
                ),
                th.Meltano.Singer.Typing.Property(
                    "version",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Library version",
                ),
                th.Meltano.Singer.Typing.Property(
                    "size",
                    th.Meltano.Singer.Typing.IntegerType(),
                    description="Library size",
                ),
                th.Meltano.Singer.Typing.Property(
                    "usageCount",
                    th.Meltano.Singer.Typing.IntegerType(),
                    description="Usage count",
                ),
                th.Meltano.Singer.Typing.Property(
                    "functions",
                    th.Meltano.Singer.Typing.ArrayType(
                        th.Meltano.Singer.Typing.StringType()
                    ),
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
    primary_keys: ClassVar[Sequence[str]] = ["name"]
    replication_key: str | None = "lastUpdated"
    api_category: ClassVar[str] = "security"
    stream_schema: Mapping[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Meltano.Singer.Typing.PropertiesList(
                th.Meltano.Singer.Typing.Property(
                    "name",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Certificate name",
                ),
                th.Meltano.Singer.Typing.Property(
                    "description",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Certificate description",
                ),
                th.Meltano.Singer.Typing.Property(
                    "type",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Certificate type",
                ),
                th.Meltano.Singer.Typing.Property(
                    "status",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Certificate status",
                ),
                th.Meltano.Singer.Typing.Property(
                    "created",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Creation timestamp",
                ),
                th.Meltano.Singer.Typing.Property(
                    "lastUpdated",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Last update timestamp",
                ),
                th.Meltano.Singer.Typing.Property(
                    "createdBy",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Created by user",
                ),
                th.Meltano.Singer.Typing.Property(
                    "expirationDate",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Expiration date",
                ),
                th.Meltano.Singer.Typing.Property(
                    "issuer",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Certificate issuer",
                ),
                th.Meltano.Singer.Typing.Property(
                    "subject",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Certificate subject",
                ),
                th.Meltano.Singer.Typing.Property(
                    "serialNumber",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Serial number",
                ),
                th.Meltano.Singer.Typing.Property(
                    "fingerprint",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Certificate fingerprint",
                ),
                th.Meltano.Singer.Typing.Property(
                    "usageCount",
                    th.Meltano.Singer.Typing.IntegerType(),
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
    primary_keys: ClassVar[Sequence[str]] = ["id"]
    replication_key: str | None = None
    api_category: ClassVar[str] = "infrastructure"
    stream_schema: Mapping[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Meltano.Singer.Typing.PropertiesList(
                th.Meltano.Singer.Typing.Property(
                    "id",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Adapter ID",
                ),
                th.Meltano.Singer.Typing.Property(
                    "name",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Adapter name",
                ),
                th.Meltano.Singer.Typing.Property(
                    "displayName",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Adapter display name",
                ),
                th.Meltano.Singer.Typing.Property(
                    "description",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Adapter description",
                ),
                th.Meltano.Singer.Typing.Property(
                    "version",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Adapter version",
                ),
                th.Meltano.Singer.Typing.Property(
                    "vendor",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Adapter vendor",
                ),
                th.Meltano.Singer.Typing.Property(
                    "category",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Adapter category",
                ),
                th.Meltano.Singer.Typing.Property(
                    "capabilities",
                    th.Meltano.Singer.Typing.ArrayType(
                        th.Meltano.Singer.Typing.StringType()
                    ),
                    description="Adapter capabilities",
                ),
                th.Meltano.Singer.Typing.Property(
                    "connectionTypes",
                    th.Meltano.Singer.Typing.ArrayType(
                        th.Meltano.Singer.Typing.StringType()
                    ),
                    description="Connection types",
                ),
                th.Meltano.Singer.Typing.Property(
                    "isCustom",
                    th.Meltano.Singer.Typing.BooleanType(),
                    description="Is custom adapter",
                ),
                th.Meltano.Singer.Typing.Property(
                    "isDeprecated",
                    th.Meltano.Singer.Typing.BooleanType(),
                    description="Is deprecated",
                ),
                th.Meltano.Singer.Typing.Property(
                    "documentationUrl",
                    th.Meltano.Singer.Typing.StringType(),
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
    primary_keys: ClassVar[Sequence[str]] = ["id"]
    replication_key: str | None = "lastUpdated"
    api_category: ClassVar[str] = "extended"
    requires_design_api: ClassVar[bool] = True
    stream_schema: Mapping[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Meltano.Singer.Typing.PropertiesList(
                th.Meltano.Singer.Typing.Property(
                    "id",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Project ID",
                ),
                th.Meltano.Singer.Typing.Property(
                    "name",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Project name",
                ),
                th.Meltano.Singer.Typing.Property(
                    "description",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Project description",
                ),
                th.Meltano.Singer.Typing.Property(
                    "status",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Project status",
                ),
                th.Meltano.Singer.Typing.Property(
                    "created",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Creation timestamp",
                ),
                th.Meltano.Singer.Typing.Property(
                    "lastUpdated",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Last update timestamp",
                ),
                th.Meltano.Singer.Typing.Property(
                    "createdBy",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Created by user",
                ),
                th.Meltano.Singer.Typing.Property(
                    "lastUpdatedBy",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Last updated by user",
                ),
                th.Meltano.Singer.Typing.Property(
                    "folders",
                    th.Meltano.Singer.Typing.ArrayType(
                        th.Meltano.Singer.Typing.ObjectType()
                    ),
                    description="Project folders",
                ),
                th.Meltano.Singer.Typing.Property(
                    "integrationCount",
                    th.Meltano.Singer.Typing.IntegerType(),
                    description="Number of integrations",
                ),
                th.Meltano.Singer.Typing.Property(
                    "connectionCount",
                    th.Meltano.Singer.Typing.IntegerType(),
                    description="Number of connections",
                ),
                th.Meltano.Singer.Typing.Property(
                    "permissions",
                    th.Meltano.Singer.Typing.ArrayType(
                        th.Meltano.Singer.Typing.ObjectType()
                    ),
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
    primary_keys: ClassVar[Sequence[str]] = ["instanceId"]
    replication_key: str | None = "startTime"
    api_category: ClassVar[str] = "monitoring"
    requires_monitoring_api: ClassVar[bool] = True
    stream_schema: Mapping[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Meltano.Singer.Typing.PropertiesList(
                th.Meltano.Singer.Typing.Property(
                    "instanceId",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Execution instance ID",
                ),
                th.Meltano.Singer.Typing.Property(
                    "integrationName",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Integration name",
                ),
                th.Meltano.Singer.Typing.Property(
                    "integrationVersion",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Integration version",
                ),
                th.Meltano.Singer.Typing.Property(
                    "status",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Execution status",
                ),
                th.Meltano.Singer.Typing.Property(
                    "startTime",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Execution start time",
                ),
                th.Meltano.Singer.Typing.Property(
                    "endTime",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Execution end time",
                ),
                th.Meltano.Singer.Typing.Property(
                    "duration",
                    th.Meltano.Singer.Typing.IntegerType(),
                    description="Execution duration (ms)",
                ),
                th.Meltano.Singer.Typing.Property(
                    "errorCode",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Error code",
                ),
                th.Meltano.Singer.Typing.Property(
                    "errorMessage",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Error message",
                ),
                th.Meltano.Singer.Typing.Property(
                    "payloadSize",
                    th.Meltano.Singer.Typing.IntegerType(),
                    description="Payload size",
                ),
                th.Meltano.Singer.Typing.Property(
                    "processedRecords",
                    th.Meltano.Singer.Typing.IntegerType(),
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
    primary_keys: ClassVar[Sequence[str]] = ["metricId", "timestamp"]
    replication_key: str | None = "timestamp"
    api_category: ClassVar[str] = "monitoring"
    requires_monitoring_api: ClassVar[bool] = True
    stream_schema: Mapping[str, t.ContainerValue] = _SCHEMA_ADAPTER.validate_python(
        _properties_to_dict(
            th.Meltano.Singer.Typing.PropertiesList(
                th.Meltano.Singer.Typing.Property(
                    "metricId",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Metric ID",
                ),
                th.Meltano.Singer.Typing.Property(
                    "metricName",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Metric name",
                ),
                th.Meltano.Singer.Typing.Property(
                    "timestamp",
                    th.Meltano.Singer.Typing.DateTimeType(),
                    description="Metric timestamp",
                ),
                th.Meltano.Singer.Typing.Property(
                    "value",
                    th.Meltano.Singer.Typing.NumberType(),
                    description="Metric value",
                ),
                th.Meltano.Singer.Typing.Property(
                    "unit",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Metric unit",
                ),
                th.Meltano.Singer.Typing.Property(
                    "tags",
                    th.Meltano.Singer.Typing.ObjectType(),
                    description="Metric tags",
                ),
                th.Meltano.Singer.Typing.Property(
                    "integrationName",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Related integration",
                ),
                th.Meltano.Singer.Typing.Property(
                    "connectionName",
                    th.Meltano.Singer.Typing.StringType(),
                    description="Related connection",
                ),
            ),
        ),
    )


ALL_STREAMS: Mapping[str, type[OICBaseStream]] = {
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
