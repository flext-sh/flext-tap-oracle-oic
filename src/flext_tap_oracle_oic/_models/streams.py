"""Oracle Integration Cloud - Consolidated Stream models.

Consolidated stream implementations following FLEXT namespace patterns.
All stream classes are inner classes of FlextTapOracleOicModelsStreams;
the tap derives its stream registry from this namespace.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_meltano import FlextMeltanoModels, t

from flext_tap_oracle_oic._models import FlextTapOracleOicStreamBase


class FlextTapOracleOicModelsStreams:
    """Stream model definitions for Oracle Integration Cloud.

    Contains all OIC stream classes as inner classes; shared audit-trail
    properties come from ``FlextTapOracleOicStreamBase.oic_common_properties``.
    """

    class IntegrationsStream(FlextTapOracleOicStreamBase):
        """Oracle Integration Cloud Integrations Stream.

        Extracts complete integration metadata including configurations,
        endpoints, triggers, connections, and execution statistics.
        """

        name: str = "integrations"
        path: str = "/integrations"
        primary_keys: ClassVar[t.StrSequence] = ["id"]
        replication_key: str | None = "lastUpdated"
        api_category: ClassVar[str] = "core"
        requires_design_api: ClassVar[bool] = True
        default_sort: ClassVar[str | None] = "lastUpdated:desc"
        default_expand: ClassVar[str] = "connections,endpoints"
        stream_schema: t.JsonMapping = t.json_mapping_adapter().validate_python(
            FlextTapOracleOicStreamBase.schema_mapping(
                FlextMeltanoModels.Meltano.SingerPropertiesList(
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "id",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Integration ID",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "name",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Integration name",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "version",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Integration version",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "description",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Integration description",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "status",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Integration status",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "pattern",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Integration pattern",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "style",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Integration style",
                    ),
                    *FlextTapOracleOicStreamBase.oic_common_properties,
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "connections",
                        FlextMeltanoModels.Meltano.SingerArrayType(
                            FlextMeltanoModels.Meltano.SingerObjectType()
                        ),
                        description="Used connections",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "endpoints",
                        FlextMeltanoModels.Meltano.SingerArrayType(
                            FlextMeltanoModels.Meltano.SingerObjectType()
                        ),
                        description="Integration endpoints",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "trackingu.Fields",
                        FlextMeltanoModels.Meltano.SingerArrayType(
                            FlextMeltanoModels.Meltano.SingerStringType()
                        ),
                        description="Tracking fields",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "payloadTracking",
                        FlextMeltanoModels.Meltano.SingerBooleanType(),
                        description="Payload tracking enabled",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "tracing",
                        FlextMeltanoModels.Meltano.SingerBooleanType(),
                        description="Tracing enabled",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "lockedBy",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Locked by user",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "lockedFlag",
                        FlextMeltanoModels.Meltano.SingerBooleanType(),
                        description="Is locked",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "projectId",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Project ID",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "folderId",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Folder ID",
                    ),
                ),
            ),
        )

    class ConnectionsStream(FlextTapOracleOicStreamBase):
        """Oracle Integration Cloud Connections Stream.

        Extracts adapter connection configurations, security policies,
        and connection properties for integrations.
        """

        name: str = "connections"
        path: str = "/connections"
        primary_keys: ClassVar[t.StrSequence] = ["id"]
        replication_key: str | None = "lastUpdated"
        api_category: ClassVar[str] = "core"
        requires_design_api: ClassVar[bool] = True
        default_sort: ClassVar[str | None] = "name:asc"
        stream_schema: t.JsonMapping = t.json_mapping_adapter().validate_python(
            FlextTapOracleOicStreamBase.schema_mapping(
                FlextMeltanoModels.Meltano.SingerPropertiesList(
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "id",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Connection ID",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "name",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Connection name",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "description",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Connection description",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "adapterType",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Adapter type",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "adapterDisplayName",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Adapter display name",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "adapterVersion",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Adapter version",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "status",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Connection status",
                    ),
                    *FlextTapOracleOicStreamBase.oic_common_properties,
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "connectionUrl",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Connection URL",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "securityPolicy",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Security policy",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "connectionProperties",
                        FlextMeltanoModels.Meltano.SingerObjectType(),
                        description="Connection properties",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "isValid",
                        FlextMeltanoModels.Meltano.SingerBooleanType(),
                        description="Connection validity",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "usageCount",
                        FlextMeltanoModels.Meltano.SingerIntegerType(),
                        description="Usage count",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "lockedBy",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Locked by user",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "lockedFlag",
                        FlextMeltanoModels.Meltano.SingerBooleanType(),
                        description="Is locked",
                    ),
                ),
            ),
        )

    class PackagesStream(FlextTapOracleOicStreamBase):
        """Oracle Integration Cloud Packages Stream.

        Extracts integration packages for deployment and versioning,
        including package metadata and content information.
        """

        name: str = "packages"
        path: str = "/packages"
        primary_keys: ClassVar[t.StrSequence] = ["id"]
        replication_key: str | None = "lastUpdated"
        api_category: ClassVar[str] = "core"
        default_sort: ClassVar[str | None] = "lastUpdated:desc"
        stream_schema: t.JsonMapping = t.json_mapping_adapter().validate_python(
            FlextTapOracleOicStreamBase.schema_mapping(
                FlextMeltanoModels.Meltano.SingerPropertiesList(
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "id",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Package ID",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "name",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Package name",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "description",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Package description",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "version",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Package version",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "status",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Package status",
                    ),
                    *FlextTapOracleOicStreamBase.oic_common_properties,
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "integrations",
                        FlextMeltanoModels.Meltano.SingerArrayType(
                            FlextMeltanoModels.Meltano.SingerObjectType()
                        ),
                        description="Included integrations",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "connections",
                        FlextMeltanoModels.Meltano.SingerArrayType(
                            FlextMeltanoModels.Meltano.SingerObjectType()
                        ),
                        description="Included connections",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "size",
                        FlextMeltanoModels.Meltano.SingerIntegerType(),
                        description="Package size",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "projectId",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Project ID",
                    ),
                ),
            ),
        )

    class LookupsStream(FlextTapOracleOicStreamBase):
        """Oracle Integration Cloud Lookups Stream.

        Extracts data transformation lookup tables used in mappings
        and transformations across integrations.
        """

        name: str = "lookups"
        path: str = "/lookups"
        primary_keys: ClassVar[t.StrSequence] = ["name"]
        replication_key: str | None = "lastUpdated"
        api_category: ClassVar[str] = "core"
        stream_schema: t.JsonMapping = t.json_mapping_adapter().validate_python(
            FlextTapOracleOicStreamBase.schema_mapping(
                FlextMeltanoModels.Meltano.SingerPropertiesList(
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "name",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Lookup name",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "description",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Lookup description",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "type",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Lookup type",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "status",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Lookup status",
                    ),
                    *FlextTapOracleOicStreamBase.oic_common_properties,
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "valueCount",
                        FlextMeltanoModels.Meltano.SingerIntegerType(),
                        description="Number of lookup values",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "defaultValue",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Default lookup value",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "isReadOnly",
                        FlextMeltanoModels.Meltano.SingerBooleanType(),
                        description="Is read-only",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "usageCount",
                        FlextMeltanoModels.Meltano.SingerIntegerType(),
                        description="Usage count",
                    ),
                ),
            ),
        )

    class LibrariesStream(FlextTapOracleOicStreamBase):
        """Oracle Integration Cloud Libraries Stream.

        Extracts reusable libraries including JavaScript libraries,
        XSLT stylesheets, and custom functions.
        """

        name: str = "libraries"
        path: str = "/libraries"
        primary_keys: ClassVar[t.StrSequence] = ["id"]
        replication_key: str | None = "lastUpdated"
        api_category: ClassVar[str] = "infrastructure"
        stream_schema: t.JsonMapping = t.json_mapping_adapter().validate_python(
            FlextTapOracleOicStreamBase.schema_mapping(
                FlextMeltanoModels.Meltano.SingerPropertiesList(
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "id",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Library ID",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "name",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Library name",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "description",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Library description",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "type",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Library type",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "status",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Library status",
                    ),
                    *FlextTapOracleOicStreamBase.oic_common_properties,
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "version",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Library version",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "size",
                        FlextMeltanoModels.Meltano.SingerIntegerType(),
                        description="Library size",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "usageCount",
                        FlextMeltanoModels.Meltano.SingerIntegerType(),
                        description="Usage count",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "functions",
                        FlextMeltanoModels.Meltano.SingerArrayType(
                            FlextMeltanoModels.Meltano.SingerStringType()
                        ),
                        description="Available functions",
                    ),
                ),
            ),
        )

    class CertificatesStream(FlextTapOracleOicStreamBase):
        """Oracle Integration Cloud Certificates Stream.

        Extracts security certificates used for SSL/TLS connections,
        message encryption, and digital signatures.
        """

        name: str = "certificates"
        path: str = "/certificates"
        primary_keys: ClassVar[t.StrSequence] = ["name"]
        replication_key: str | None = "lastUpdated"
        api_category: ClassVar[str] = "security"
        stream_schema: t.JsonMapping = t.json_mapping_adapter().validate_python(
            FlextTapOracleOicStreamBase.schema_mapping(
                FlextMeltanoModels.Meltano.SingerPropertiesList(
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "name",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Certificate name",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "description",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Certificate description",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "type",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Certificate type",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "status",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Certificate status",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "created",
                        FlextMeltanoModels.Meltano.SingerDateTimeType(),
                        description="Creation timestamp",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "lastUpdated",
                        FlextMeltanoModels.Meltano.SingerDateTimeType(),
                        description="Last update timestamp",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "createdBy",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Created by user",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "expirationDate",
                        FlextMeltanoModels.Meltano.SingerDateTimeType(),
                        description="Expiration date",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "issuer",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Certificate issuer",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "subject",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Certificate subject",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "serialNumber",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Serial number",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "fingerprint",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Certificate fingerprint",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "usageCount",
                        FlextMeltanoModels.Meltano.SingerIntegerType(),
                        description="Usage count",
                    ),
                ),
            ),
        )

    class AdaptersStream(FlextTapOracleOicStreamBase):
        """Oracle Integration Cloud Adapters Stream.

        Extracts available adapter information including versions,
        capabilities, and configuration options.
        """

        name: str = "adapters"
        path: str = "/adapters"
        primary_keys: ClassVar[t.StrSequence] = ["id"]
        replication_key: str | None = None
        api_category: ClassVar[str] = "infrastructure"
        stream_schema: t.JsonMapping = t.json_mapping_adapter().validate_python(
            FlextTapOracleOicStreamBase.schema_mapping(
                FlextMeltanoModels.Meltano.SingerPropertiesList(
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "id",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Adapter ID",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "name",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Adapter name",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "displayName",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Adapter display name",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "description",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Adapter description",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "version",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Adapter version",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "vendor",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Adapter vendor",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "category",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Adapter category",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "capabilities",
                        FlextMeltanoModels.Meltano.SingerArrayType(
                            FlextMeltanoModels.Meltano.SingerStringType()
                        ),
                        description="Adapter capabilities",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "connectionTypes",
                        FlextMeltanoModels.Meltano.SingerArrayType(
                            FlextMeltanoModels.Meltano.SingerStringType()
                        ),
                        description="Connection types",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "isCustom",
                        FlextMeltanoModels.Meltano.SingerBooleanType(),
                        description="Is custom adapter",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "isDeprecated",
                        FlextMeltanoModels.Meltano.SingerBooleanType(),
                        description="Is deprecated",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "documentationUrl",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Documentation URL",
                    ),
                ),
            ),
        )

    class ProjectsStream(FlextTapOracleOicStreamBase):
        """Oracle Integration Cloud Projects Stream.

        Extracts project organization data including folder structure,
        permissions, and resource grouping.
        """

        name: str = "projects"
        path: str = "/projects"
        primary_keys: ClassVar[t.StrSequence] = ["id"]
        replication_key: str | None = "lastUpdated"
        api_category: ClassVar[str] = "extended"
        requires_design_api: ClassVar[bool] = True
        stream_schema: t.JsonMapping = t.json_mapping_adapter().validate_python(
            FlextTapOracleOicStreamBase.schema_mapping(
                FlextMeltanoModels.Meltano.SingerPropertiesList(
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "id",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Project ID",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "name",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Project name",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "description",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Project description",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "status",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Project status",
                    ),
                    *FlextTapOracleOicStreamBase.oic_common_properties,
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "folders",
                        FlextMeltanoModels.Meltano.SingerArrayType(
                            FlextMeltanoModels.Meltano.SingerObjectType()
                        ),
                        description="Project folders",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "integrationCount",
                        FlextMeltanoModels.Meltano.SingerIntegerType(),
                        description="Number of integrations",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "connectionCount",
                        FlextMeltanoModels.Meltano.SingerIntegerType(),
                        description="Number of connections",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "permissions",
                        FlextMeltanoModels.Meltano.SingerArrayType(
                            FlextMeltanoModels.Meltano.SingerObjectType()
                        ),
                        description="Project permissions",
                    ),
                ),
            ),
        )

    class ExecutionsStream(FlextTapOracleOicStreamBase):
        """Oracle Integration Cloud Executions Stream.

        Extracts integration execution data including status,
        performance metrics, and error information.
        """

        name: str = "executions"
        path: str = "/monitoring/v1/integrations"
        primary_keys: ClassVar[t.StrSequence] = ["instanceId"]
        replication_key: str | None = "startTime"
        api_category: ClassVar[str] = "monitoring"
        requires_monitoring_api: ClassVar[bool] = True
        stream_schema: t.JsonMapping = t.json_mapping_adapter().validate_python(
            FlextTapOracleOicStreamBase.schema_mapping(
                FlextMeltanoModels.Meltano.SingerPropertiesList(
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "instanceId",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Execution instance ID",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "integrationName",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Integration name",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "integrationVersion",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Integration version",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "status",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Execution status",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "startTime",
                        FlextMeltanoModels.Meltano.SingerDateTimeType(),
                        description="Execution start time",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "endTime",
                        FlextMeltanoModels.Meltano.SingerDateTimeType(),
                        description="Execution end time",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "duration",
                        FlextMeltanoModels.Meltano.SingerIntegerType(),
                        description="Execution duration (ms)",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "errorCode",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Error code",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "errorMessage",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Error message",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "payloadSize",
                        FlextMeltanoModels.Meltano.SingerIntegerType(),
                        description="Payload size",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "processedRecords",
                        FlextMeltanoModels.Meltano.SingerIntegerType(),
                        description="Processed record count",
                    ),
                ),
            ),
        )

    class MetricsStream(FlextTapOracleOicStreamBase):
        """Oracle Integration Cloud Metrics Stream.

        Extracts performance and usage metrics for integrations,
        connections, and overall system health.
        """

        name: str = "metrics"
        path: str = "/monitoring/v1/metrics"
        primary_keys: ClassVar[t.StrSequence] = ["metricId", "timestamp"]
        replication_key: str | None = "timestamp"
        api_category: ClassVar[str] = "monitoring"
        requires_monitoring_api: ClassVar[bool] = True
        stream_schema: t.JsonMapping = t.json_mapping_adapter().validate_python(
            FlextTapOracleOicStreamBase.schema_mapping(
                FlextMeltanoModels.Meltano.SingerPropertiesList(
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "metricId",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Metric ID",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "metricName",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Metric name",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "timestamp",
                        FlextMeltanoModels.Meltano.SingerDateTimeType(),
                        description="Metric timestamp",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "value",
                        FlextMeltanoModels.Meltano.SingerNumberType(),
                        description="Metric value",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "unit",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Metric unit",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "tags",
                        FlextMeltanoModels.Meltano.SingerObjectType(),
                        description="Metric tags",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "integrationName",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Related integration",
                    ),
                    FlextMeltanoModels.Meltano.SingerProperty(
                        "connectionName",
                        FlextMeltanoModels.Meltano.SingerStringType(),
                        description="Related connection",
                    ),
                ),
            ),
        )


__all__: list[str] = ["FlextTapOracleOicModelsStreams"]
