"""Oracle Integration Cloud - Consolidated Streams.

Consolidated stream implementations removing duplications between core, extended,
infrastructure, and monitoring modules. Follows DRY principles and FLEXT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
"""

from __future__ import annotations

from typing import ClassVar, cast

from flext_meltano import FlextMeltanoTypes

from flext_tap_oracle_oic.tap_streams import OICBaseStream

# Initialize FlextMeltanoTypes for compatibility
th = FlextMeltanoTypes()


class IntegrationsStream(OICBaseStream):
    """Oracle Integration Cloud Integrations Stream.

    Extracts complete integration metadata including configurations,
    endpoints, triggers, connections, and execution statistics.
    """

    name: ClassVar[str] = "integrations"
    path: ClassVar[str] = "/integrations"
    primary_keys: ClassVar[list[str]] = ["id"]
    replication_key: ClassVar[str] = "lastUpdated"
    api_category: ClassVar[str] = "core"
    requires_design_api: ClassVar[bool] = True
    default_sort: ClassVar[str] = "lastUpdated:desc"
    default_expand: ClassVar[str] = "connections,endpoints"

    schema: dict[str, object] = cast(
        "dict[str, object]",
        FlextMeltanoTypes.Singer.Typing.PropertiesList(
            FlextMeltanoTypes.Singer.Typing.Property(
                "id",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Integration ID",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "name",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Integration name",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "version",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Integration version",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "description",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Integration description",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "status",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Integration status",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "pattern",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Integration pattern",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "style",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Integration style",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "created",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Creation timestamp",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "lastUpdated",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Last update timestamp",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "createdBy",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Created by user",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "lastUpdatedBy",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Last updated by user",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "connections",
                FlextMeltanoTypes.Singer.Typing.ArrayType(
                    FlextMeltanoTypes.Singer.Typing.ObjectType()
                ),
                description="Used connections",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "endpoints",
                FlextMeltanoTypes.Singer.Typing.ArrayType(
                    FlextMeltanoTypes.Singer.Typing.ObjectType()
                ),
                description="Integration endpoints",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "trackingFields",
                FlextMeltanoTypes.Singer.Typing.ArrayType(
                    FlextMeltanoTypes.Singer.Typing.StringType()
                ),
                description="Tracking fields",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "payloadTracking",
                FlextMeltanoTypes.Singer.Typing.BooleanType(),
                description="Payload tracking enabled",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "tracing",
                FlextMeltanoTypes.Singer.Typing.BooleanType(),
                description="Tracing enabled",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "lockedBy",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Locked by user",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "lockedFlag",
                FlextMeltanoTypes.Singer.Typing.BooleanType(),
                description="Is locked",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "projectId",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Project ID",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "folderId",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Folder ID",
            ),
        ).to_dict(),
    )


class ConnectionsStream(OICBaseStream):
    """Oracle Integration Cloud Connections Stream.

    Extracts adapter connection configurations, security policies,
    and connection properties for integrations.
    """

    name: ClassVar[str] = "connections"
    path: ClassVar[str] = "/connections"
    primary_keys: ClassVar[list[str]] = ["id"]
    replication_key: ClassVar[str] = "lastUpdated"
    api_category: ClassVar[str] = "core"
    requires_design_api: ClassVar[bool] = True
    default_sort: ClassVar[str] = "name:asc"

    schema: dict[str, object] = cast(
        "dict[str, object]",
        FlextMeltanoTypes.Singer.Typing.PropertiesList(
            FlextMeltanoTypes.Singer.Typing.Property(
                "id",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Connection ID",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "name",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Connection name",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "description",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Connection description",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "adapterType",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Adapter type",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "adapterDisplayName",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Adapter display name",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "adapterVersion",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Adapter version",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "status",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Connection status",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "created",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Creation timestamp",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "lastUpdated",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Last update timestamp",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "createdBy",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Created by user",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "lastUpdatedBy",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Last updated by user",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "connectionUrl",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Connection URL",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "securityPolicy",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Security policy",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "connectionProperties",
                FlextMeltanoTypes.Singer.Typing.ObjectType(),
                description="Connection properties",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "isValid",
                FlextMeltanoTypes.Singer.Typing.BooleanType(),
                description="Connection validity",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "usageCount",
                FlextMeltanoTypes.Singer.Typing.IntegerType(),
                description="Usage count",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "lockedBy",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Locked by user",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "lockedFlag",
                FlextMeltanoTypes.Singer.Typing.BooleanType(),
                description="Is locked",
            ),
        ).to_dict(),
    )


class PackagesStream(OICBaseStream):
    """Oracle Integration Cloud Packages Stream.

    Extracts integration packages for deployment and versioning,
    including package metadata and content information.
    """

    name: ClassVar[str] = "packages"
    path: ClassVar[str] = "/packages"
    primary_keys: ClassVar[list[str]] = ["id"]
    replication_key: ClassVar[str] = "lastUpdated"
    api_category: ClassVar[str] = "core"
    default_sort: ClassVar[str] = "lastUpdated:desc"

    schema: dict[str, object] = cast(
        "dict[str, object]",
        FlextMeltanoTypes.Singer.Typing.PropertiesList(
            FlextMeltanoTypes.Singer.Typing.Property(
                "id",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Package ID",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "name",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Package name",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "description",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Package description",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "version",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Package version",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "status",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Package status",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "created",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Creation timestamp",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "lastUpdated",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Last update timestamp",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "createdBy",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Created by user",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "lastUpdatedBy",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Last updated by user",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "integrations",
                FlextMeltanoTypes.Singer.Typing.ArrayType(
                    FlextMeltanoTypes.Singer.Typing.ObjectType()
                ),
                description="Included integrations",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "connections",
                FlextMeltanoTypes.Singer.Typing.ArrayType(
                    FlextMeltanoTypes.Singer.Typing.ObjectType()
                ),
                description="Included connections",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "size",
                FlextMeltanoTypes.Singer.Typing.IntegerType(),
                description="Package size",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "projectId",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Project ID",
            ),
        ).to_dict(),
    )


class LookupsStream(OICBaseStream):
    """Oracle Integration Cloud Lookups Stream.

    Extracts data transformation lookup tables used in mappings
    and transformations across integrations.
    """

    name: ClassVar[str] = "lookups"
    path: ClassVar[str] = "/lookups"
    primary_keys: ClassVar[list[str]] = ["name"]
    replication_key: ClassVar[str] = "lastUpdated"
    api_category: ClassVar[str] = "core"

    schema: dict[str, object] = cast(
        "dict[str, object]",
        FlextMeltanoTypes.Singer.Typing.PropertiesList(
            FlextMeltanoTypes.Singer.Typing.Property(
                "name",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Lookup name",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "description",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Lookup description",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "type",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Lookup type",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "status",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Lookup status",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "created",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Creation timestamp",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "lastUpdated",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Last update timestamp",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "createdBy",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Created by user",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "lastUpdatedBy",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Last updated by user",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "valueCount",
                FlextMeltanoTypes.Singer.Typing.IntegerType(),
                description="Number of lookup values",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "defaultValue",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Default lookup value",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "isReadOnly",
                FlextMeltanoTypes.Singer.Typing.BooleanType(),
                description="Is read-only",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "usageCount",
                FlextMeltanoTypes.Singer.Typing.IntegerType(),
                description="Usage count",
            ),
        ).to_dict(),
    )


# INFRASTRUCTURE STREAMS


class LibrariesStream(OICBaseStream):
    """Oracle Integration Cloud Libraries Stream.

    Extracts reusable libraries including JavaScript libraries,
    XSLT stylesheets, and custom functions.
    """

    name: ClassVar[str] = "libraries"
    path: ClassVar[str] = "/libraries"
    primary_keys: ClassVar[list[str]] = ["id"]
    replication_key: ClassVar[str] = "lastUpdated"
    api_category: ClassVar[str] = "infrastructure"

    schema: dict[str, object] = cast(
        "dict[str, object]",
        FlextMeltanoTypes.Singer.Typing.PropertiesList(
            FlextMeltanoTypes.Singer.Typing.Property(
                "id",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Library ID",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "name",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Library name",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "description",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Library description",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "type",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Library type",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "status",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Library status",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "created",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Creation timestamp",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "lastUpdated",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Last update timestamp",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "createdBy",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Created by user",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "lastUpdatedBy",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Last updated by user",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "version",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Library version",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "size",
                FlextMeltanoTypes.Singer.Typing.IntegerType(),
                description="Library size",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "usageCount",
                FlextMeltanoTypes.Singer.Typing.IntegerType(),
                description="Usage count",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "functions",
                FlextMeltanoTypes.Singer.Typing.ArrayType(
                    FlextMeltanoTypes.Singer.Typing.StringType()
                ),
                description="Available functions",
            ),
        ).to_dict(),
    )


class CertificatesStream(OICBaseStream):
    """Oracle Integration Cloud Certificates Stream.

    Extracts security certificates used for SSL/TLS connections,
    message encryption, and digital signatures.
    """

    name: ClassVar[str] = "certificates"
    path: ClassVar[str] = "/certificates"
    primary_keys: ClassVar[list[str]] = ["name"]
    replication_key: ClassVar[str] = "lastUpdated"
    api_category: ClassVar[str] = "security"

    schema: dict[str, object] = cast(
        "dict[str, object]",
        FlextMeltanoTypes.Singer.Typing.PropertiesList(
            FlextMeltanoTypes.Singer.Typing.Property(
                "name",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Certificate name",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "description",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Certificate description",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "type",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Certificate type",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "status",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Certificate status",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "created",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Creation timestamp",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "lastUpdated",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Last update timestamp",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "createdBy",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Created by user",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "expirationDate",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Expiration date",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "issuer",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Certificate issuer",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "subject",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Certificate subject",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "serialNumber",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Serial number",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "fingerprint",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Certificate fingerprint",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "usageCount",
                FlextMeltanoTypes.Singer.Typing.IntegerType(),
                description="Usage count",
            ),
        ).to_dict(),
    )


class AdaptersStream(OICBaseStream):
    """Oracle Integration Cloud Adapters Stream.

    Extracts available adapter information including versions,
    capabilities, and configuration options.
    """

    name: ClassVar[str] = "adapters"
    path: ClassVar[str] = "/adapters"
    primary_keys: ClassVar[list[str]] = ["id"]
    replication_key: ClassVar[str | None] = None  # Static metadata
    api_category: ClassVar[str] = "infrastructure"

    schema: dict[str, object] = cast(
        "dict[str, object]",
        FlextMeltanoTypes.Singer.Typing.PropertiesList(
            FlextMeltanoTypes.Singer.Typing.Property(
                "id",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Adapter ID",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "name",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Adapter name",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "displayName",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Adapter display name",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "description",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Adapter description",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "version",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Adapter version",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "vendor",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Adapter vendor",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "category",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Adapter category",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "capabilities",
                FlextMeltanoTypes.Singer.Typing.ArrayType(
                    FlextMeltanoTypes.Singer.Typing.StringType()
                ),
                description="Adapter capabilities",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "connectionTypes",
                FlextMeltanoTypes.Singer.Typing.ArrayType(
                    FlextMeltanoTypes.Singer.Typing.StringType()
                ),
                description="Connection types",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "isCustom",
                FlextMeltanoTypes.Singer.Typing.BooleanType(),
                description="Is custom adapter",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "isDeprecated",
                FlextMeltanoTypes.Singer.Typing.BooleanType(),
                description="Is deprecated",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "documentationUrl",
                FlextMeltanoTypes.Singer.Typing.StringType(),
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

    name: ClassVar[str] = "projects"
    path: ClassVar[str] = "/projects"
    primary_keys: ClassVar[list[str]] = ["id"]
    replication_key: ClassVar[str] = "lastUpdated"
    api_category: ClassVar[str] = "extended"
    requires_design_api: ClassVar[bool] = True

    schema: dict[str, object] = cast(
        "dict[str, object]",
        FlextMeltanoTypes.Singer.Typing.PropertiesList(
            FlextMeltanoTypes.Singer.Typing.Property(
                "id",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Project ID",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "name",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Project name",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "description",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Project description",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "status",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Project status",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "created",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Creation timestamp",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "lastUpdated",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Last update timestamp",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "createdBy",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Created by user",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "lastUpdatedBy",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Last updated by user",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "folders",
                FlextMeltanoTypes.Singer.Typing.ArrayType(
                    FlextMeltanoTypes.Singer.Typing.ObjectType()
                ),
                description="Project folders",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "integrationCount",
                FlextMeltanoTypes.Singer.Typing.IntegerType(),
                description="Number of integrations",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "connectionCount",
                FlextMeltanoTypes.Singer.Typing.IntegerType(),
                description="Number of connections",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "permissions",
                FlextMeltanoTypes.Singer.Typing.ArrayType(
                    FlextMeltanoTypes.Singer.Typing.ObjectType()
                ),
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

    name: ClassVar[str] = "executions"
    path: ClassVar[str] = "/monitoring/v1/integrations"
    primary_keys: ClassVar[list[str]] = ["instanceId"]
    replication_key: ClassVar[str] = "startTime"
    api_category: ClassVar[str] = "monitoring"
    requires_monitoring_api: ClassVar[bool] = True

    schema: dict[str, object] = cast(
        "dict[str, object]",
        FlextMeltanoTypes.Singer.Typing.PropertiesList(
            FlextMeltanoTypes.Singer.Typing.Property(
                "instanceId",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Execution instance ID",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "integrationName",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Integration name",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "integrationVersion",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Integration version",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "status",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Execution status",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "startTime",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Execution start time",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "endTime",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Execution end time",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "duration",
                FlextMeltanoTypes.Singer.Typing.IntegerType(),
                description="Execution duration (ms)",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "errorCode",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Error code",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "errorMessage",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Error message",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "payloadSize",
                FlextMeltanoTypes.Singer.Typing.IntegerType(),
                description="Payload size",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "processedRecords",
                FlextMeltanoTypes.Singer.Typing.IntegerType(),
                description="Processed record count",
            ),
        ).to_dict(),
    )


class MetricsStream(OICBaseStream):
    """Oracle Integration Cloud Metrics Stream.

    Extracts performance and usage metrics for integrations,
    connections, and overall system healFlextMeltanoTypes.Singer.Typing.
    """

    name: ClassVar[str] = "metrics"
    path: ClassVar[str] = "/monitoring/v1/metrics"
    primary_keys: ClassVar[list[str]] = ["metricId", "timestamp"]
    replication_key: ClassVar[str] = "timestamp"
    api_category: ClassVar[str] = "monitoring"
    requires_monitoring_api: ClassVar[bool] = True

    schema: dict[str, object] = cast(
        "dict[str, object]",
        FlextMeltanoTypes.Singer.Typing.PropertiesList(
            FlextMeltanoTypes.Singer.Typing.Property(
                "metricId",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Metric ID",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "metricName",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Metric name",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "timestamp",
                FlextMeltanoTypes.Singer.Typing.DateTimeType(),
                description="Metric timestamp",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "value",
                FlextMeltanoTypes.Singer.Typing.NumberType(),
                description="Metric value",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "unit",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Metric unit",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "tags",
                FlextMeltanoTypes.Singer.Typing.ObjectType(),
                description="Metric tags",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "integrationName",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Related integration",
            ),
            FlextMeltanoTypes.Singer.Typing.Property(
                "connectionName",
                FlextMeltanoTypes.Singer.Typing.StringType(),
                description="Related connection",
            ),
        ).to_dict(),
    )


# CONSOLIDATED STREAM REGISTRY


ALL_STREAMS = {
    # Core business streams
    "integrations": "IntegrationsStream",
    "connections": "ConnectionsStream",
    "packages": "PackagesStream",
    "lookups": "LookupsStream",
    # Infrastructure streams
    "libraries": "LibrariesStream",
    "certificates": "CertificatesStream",
    "adapters": "AdaptersStream",
    # Extended business streams
    "projects": "ProjectsStream",
    # Monitoring streams
    "executions": "ExecutionsStream",
    "metrics": "MetricsStream",
}

CORE_STREAMS = ["integrations", "connections", "packages", "lookups", "libraries"]
INFRASTRUCTURE_STREAMS = ["certificates", "adapters"]
EXTENDED_STREAMS = ["projects"]
MONITORING_STREAMS = ["executions", "metrics"]
