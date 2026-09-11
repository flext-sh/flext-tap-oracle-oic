"""Oracle Integration Cloud - Consolidated Stream models.

Consolidated stream implementations following FLEXT namespace patterns.
All stream classes are inner classes of FlextTapOracleOicModelsStreams,
wired into m.TapOracleOic via MRO.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_tap_oracle_oic import m, p, t


def _properties_to_dict(properties: p.TapOracleOic.PropertiesListLike) -> t.JsonMapping:
    return t.json_mapping_adapter().validate_python(properties.to_dict())


def _oic_common_properties() -> tuple[m.Meltano.SingerProperty[str], ...]:
    """Return the audit trail properties shared by every OIC stream.

    ``created``, ``lastUpdated``, ``createdBy`` and ``lastUpdatedBy`` carry the
    same SingerProperty definition across all streams, so they are factored out
    here and spread via ``*_oic_common_properties()`` to eliminate the
    per-stream jscpd clone.
    """
    return (
        m.Meltano.SingerProperty(
            "created", m.Meltano.SingerDateTimeType(), description="Creation timestamp"
        ),
        m.Meltano.SingerProperty(
            "lastUpdated",
            m.Meltano.SingerDateTimeType(),
            description="Last update timestamp",
        ),
        m.Meltano.SingerProperty(
            "createdBy", m.Meltano.SingerStringType(), description="Created by user"
        ),
        m.Meltano.SingerProperty(
            "lastUpdatedBy",
            m.Meltano.SingerStringType(),
            description="Last updated by user",
        ),
    )


class FlextTapOracleOicModelsStreams:
    """Stream model definitions for Oracle Integration Cloud.

    Contains all OIC stream classes as inner classes, wired into
    m.TapOracleOic via MRO composition.
    """

    class IntegrationsStream(m.TapOracleOic.OICBaseStream):
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
            _properties_to_dict(
                m.Meltano.SingerPropertiesList(
                    m.Meltano.SingerProperty(
                        "id", m.Meltano.SingerStringType(), description="Integration ID"
                    ),
                    m.Meltano.SingerProperty(
                        "name",
                        m.Meltano.SingerStringType(),
                        description="Integration name",
                    ),
                    m.Meltano.SingerProperty(
                        "version",
                        m.Meltano.SingerStringType(),
                        description="Integration version",
                    ),
                    m.Meltano.SingerProperty(
                        "description",
                        m.Meltano.SingerStringType(),
                        description="Integration description",
                    ),
                    m.Meltano.SingerProperty(
                        "status",
                        m.Meltano.SingerStringType(),
                        description="Integration status",
                    ),
                    m.Meltano.SingerProperty(
                        "pattern",
                        m.Meltano.SingerStringType(),
                        description="Integration pattern",
                    ),
                    m.Meltano.SingerProperty(
                        "style",
                        m.Meltano.SingerStringType(),
                        description="Integration style",
                    ),
                    *_oic_common_properties(),
                    m.Meltano.SingerProperty(
                        "connections",
                        m.Meltano.SingerArrayType(m.Meltano.SingerObjectType()),
                        description="Used connections",
                    ),
                    m.Meltano.SingerProperty(
                        "endpoints",
                        m.Meltano.SingerArrayType(m.Meltano.SingerObjectType()),
                        description="Integration endpoints",
                    ),
                    m.Meltano.SingerProperty(
                        "trackingu.Fields",
                        m.Meltano.SingerArrayType(m.Meltano.SingerStringType()),
                        description="Tracking fields",
                    ),
                    m.Meltano.SingerProperty(
                        "payloadTracking",
                        m.Meltano.SingerBooleanType(),
                        description="Payload tracking enabled",
                    ),
                    m.Meltano.SingerProperty(
                        "tracing",
                        m.Meltano.SingerBooleanType(),
                        description="Tracing enabled",
                    ),
                    m.Meltano.SingerProperty(
                        "lockedBy",
                        m.Meltano.SingerStringType(),
                        description="Locked by user",
                    ),
                    m.Meltano.SingerProperty(
                        "lockedFlag",
                        m.Meltano.SingerBooleanType(),
                        description="Is locked",
                    ),
                    m.Meltano.SingerProperty(
                        "projectId",
                        m.Meltano.SingerStringType(),
                        description="Project ID",
                    ),
                    m.Meltano.SingerProperty(
                        "folderId",
                        m.Meltano.SingerStringType(),
                        description="Folder ID",
                    ),
                )
            )
        )

    class ConnectionsStream(m.TapOracleOic.OICBaseStream):
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
            _properties_to_dict(
                m.Meltano.SingerPropertiesList(
                    m.Meltano.SingerProperty(
                        "id", m.Meltano.SingerStringType(), description="Connection ID"
                    ),
                    m.Meltano.SingerProperty(
                        "name",
                        m.Meltano.SingerStringType(),
                        description="Connection name",
                    ),
                    m.Meltano.SingerProperty(
                        "description",
                        m.Meltano.SingerStringType(),
                        description="Connection description",
                    ),
                    m.Meltano.SingerProperty(
                        "adapterType",
                        m.Meltano.SingerStringType(),
                        description="Adapter type",
                    ),
                    m.Meltano.SingerProperty(
                        "adapterDisplayName",
                        m.Meltano.SingerStringType(),
                        description="Adapter display name",
                    ),
                    m.Meltano.SingerProperty(
                        "adapterVersion",
                        m.Meltano.SingerStringType(),
                        description="Adapter version",
                    ),
                    m.Meltano.SingerProperty(
                        "status",
                        m.Meltano.SingerStringType(),
                        description="Connection status",
                    ),
                    *_oic_common_properties(),
                    m.Meltano.SingerProperty(
                        "connectionUrl",
                        m.Meltano.SingerStringType(),
                        description="Connection URL",
                    ),
                    m.Meltano.SingerProperty(
                        "securityPolicy",
                        m.Meltano.SingerStringType(),
                        description="Security policy",
                    ),
                    m.Meltano.SingerProperty(
                        "connectionProperties",
                        m.Meltano.SingerObjectType(),
                        description="Connection properties",
                    ),
                    m.Meltano.SingerProperty(
                        "isValid",
                        m.Meltano.SingerBooleanType(),
                        description="Connection validity",
                    ),
                    m.Meltano.SingerProperty(
                        "usageCount",
                        m.Meltano.SingerIntegerType(),
                        description="Usage count",
                    ),
                    m.Meltano.SingerProperty(
                        "lockedBy",
                        m.Meltano.SingerStringType(),
                        description="Locked by user",
                    ),
                    m.Meltano.SingerProperty(
                        "lockedFlag",
                        m.Meltano.SingerBooleanType(),
                        description="Is locked",
                    ),
                )
            )
        )

    class PackagesStream(m.TapOracleOic.OICBaseStream):
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
            _properties_to_dict(
                m.Meltano.SingerPropertiesList(
                    m.Meltano.SingerProperty(
                        "id", m.Meltano.SingerStringType(), description="Package ID"
                    ),
                    m.Meltano.SingerProperty(
                        "name", m.Meltano.SingerStringType(), description="Package name"
                    ),
                    m.Meltano.SingerProperty(
                        "description",
                        m.Meltano.SingerStringType(),
                        description="Package description",
                    ),
                    m.Meltano.SingerProperty(
                        "version",
                        m.Meltano.SingerStringType(),
                        description="Package version",
                    ),
                    m.Meltano.SingerProperty(
                        "status",
                        m.Meltano.SingerStringType(),
                        description="Package status",
                    ),
                    *_oic_common_properties(),
                    m.Meltano.SingerProperty(
                        "integrations",
                        m.Meltano.SingerArrayType(m.Meltano.SingerObjectType()),
                        description="Included integrations",
                    ),
                    m.Meltano.SingerProperty(
                        "connections",
                        m.Meltano.SingerArrayType(m.Meltano.SingerObjectType()),
                        description="Included connections",
                    ),
                    m.Meltano.SingerProperty(
                        "size",
                        m.Meltano.SingerIntegerType(),
                        description="Package size",
                    ),
                    m.Meltano.SingerProperty(
                        "projectId",
                        m.Meltano.SingerStringType(),
                        description="Project ID",
                    ),
                )
            )
        )

    class LookupsStream(m.TapOracleOic.OICBaseStream):
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
            _properties_to_dict(
                m.Meltano.SingerPropertiesList(
                    m.Meltano.SingerProperty(
                        "name", m.Meltano.SingerStringType(), description="Lookup name"
                    ),
                    m.Meltano.SingerProperty(
                        "description",
                        m.Meltano.SingerStringType(),
                        description="Lookup description",
                    ),
                    m.Meltano.SingerProperty(
                        "type", m.Meltano.SingerStringType(), description="Lookup type"
                    ),
                    m.Meltano.SingerProperty(
                        "status",
                        m.Meltano.SingerStringType(),
                        description="Lookup status",
                    ),
                    *_oic_common_properties(),
                    m.Meltano.SingerProperty(
                        "valueCount",
                        m.Meltano.SingerIntegerType(),
                        description="Number of lookup values",
                    ),
                    m.Meltano.SingerProperty(
                        "defaultValue",
                        m.Meltano.SingerStringType(),
                        description="Default lookup value",
                    ),
                    m.Meltano.SingerProperty(
                        "isReadOnly",
                        m.Meltano.SingerBooleanType(),
                        description="Is read-only",
                    ),
                    m.Meltano.SingerProperty(
                        "usageCount",
                        m.Meltano.SingerIntegerType(),
                        description="Usage count",
                    ),
                )
            )
        )

    class LibrariesStream(m.TapOracleOic.OICBaseStream):
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
            _properties_to_dict(
                m.Meltano.SingerPropertiesList(
                    m.Meltano.SingerProperty(
                        "id", m.Meltano.SingerStringType(), description="Library ID"
                    ),
                    m.Meltano.SingerProperty(
                        "name", m.Meltano.SingerStringType(), description="Library name"
                    ),
                    m.Meltano.SingerProperty(
                        "description",
                        m.Meltano.SingerStringType(),
                        description="Library description",
                    ),
                    m.Meltano.SingerProperty(
                        "type", m.Meltano.SingerStringType(), description="Library type"
                    ),
                    m.Meltano.SingerProperty(
                        "status",
                        m.Meltano.SingerStringType(),
                        description="Library status",
                    ),
                    *_oic_common_properties(),
                    m.Meltano.SingerProperty(
                        "version",
                        m.Meltano.SingerStringType(),
                        description="Library version",
                    ),
                    m.Meltano.SingerProperty(
                        "size",
                        m.Meltano.SingerIntegerType(),
                        description="Library size",
                    ),
                    m.Meltano.SingerProperty(
                        "usageCount",
                        m.Meltano.SingerIntegerType(),
                        description="Usage count",
                    ),
                    m.Meltano.SingerProperty(
                        "functions",
                        m.Meltano.SingerArrayType(m.Meltano.SingerStringType()),
                        description="Available functions",
                    ),
                )
            )
        )

    class CertificatesStream(m.TapOracleOic.OICBaseStream):
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
            _properties_to_dict(
                m.Meltano.SingerPropertiesList(
                    m.Meltano.SingerProperty(
                        "name",
                        m.Meltano.SingerStringType(),
                        description="Certificate name",
                    ),
                    m.Meltano.SingerProperty(
                        "description",
                        m.Meltano.SingerStringType(),
                        description="Certificate description",
                    ),
                    m.Meltano.SingerProperty(
                        "type",
                        m.Meltano.SingerStringType(),
                        description="Certificate type",
                    ),
                    m.Meltano.SingerProperty(
                        "status",
                        m.Meltano.SingerStringType(),
                        description="Certificate status",
                    ),
                    m.Meltano.SingerProperty(
                        "created",
                        m.Meltano.SingerDateTimeType(),
                        description="Creation timestamp",
                    ),
                    m.Meltano.SingerProperty(
                        "lastUpdated",
                        m.Meltano.SingerDateTimeType(),
                        description="Last update timestamp",
                    ),
                    m.Meltano.SingerProperty(
                        "createdBy",
                        m.Meltano.SingerStringType(),
                        description="Created by user",
                    ),
                    m.Meltano.SingerProperty(
                        "expirationDate",
                        m.Meltano.SingerDateTimeType(),
                        description="Expiration date",
                    ),
                    m.Meltano.SingerProperty(
                        "issuer",
                        m.Meltano.SingerStringType(),
                        description="Certificate issuer",
                    ),
                    m.Meltano.SingerProperty(
                        "subject",
                        m.Meltano.SingerStringType(),
                        description="Certificate subject",
                    ),
                    m.Meltano.SingerProperty(
                        "serialNumber",
                        m.Meltano.SingerStringType(),
                        description="Serial number",
                    ),
                    m.Meltano.SingerProperty(
                        "fingerprint",
                        m.Meltano.SingerStringType(),
                        description="Certificate fingerprint",
                    ),
                    m.Meltano.SingerProperty(
                        "usageCount",
                        m.Meltano.SingerIntegerType(),
                        description="Usage count",
                    ),
                )
            )
        )

    class AdaptersStream(m.TapOracleOic.OICBaseStream):
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
            _properties_to_dict(
                m.Meltano.SingerPropertiesList(
                    m.Meltano.SingerProperty(
                        "id", m.Meltano.SingerStringType(), description="Adapter ID"
                    ),
                    m.Meltano.SingerProperty(
                        "name", m.Meltano.SingerStringType(), description="Adapter name"
                    ),
                    m.Meltano.SingerProperty(
                        "displayName",
                        m.Meltano.SingerStringType(),
                        description="Adapter display name",
                    ),
                    m.Meltano.SingerProperty(
                        "description",
                        m.Meltano.SingerStringType(),
                        description="Adapter description",
                    ),
                    m.Meltano.SingerProperty(
                        "version",
                        m.Meltano.SingerStringType(),
                        description="Adapter version",
                    ),
                    m.Meltano.SingerProperty(
                        "vendor",
                        m.Meltano.SingerStringType(),
                        description="Adapter vendor",
                    ),
                    m.Meltano.SingerProperty(
                        "category",
                        m.Meltano.SingerStringType(),
                        description="Adapter category",
                    ),
                    m.Meltano.SingerProperty(
                        "capabilities",
                        m.Meltano.SingerArrayType(m.Meltano.SingerStringType()),
                        description="Adapter capabilities",
                    ),
                    m.Meltano.SingerProperty(
                        "connectionTypes",
                        m.Meltano.SingerArrayType(m.Meltano.SingerStringType()),
                        description="Connection types",
                    ),
                    m.Meltano.SingerProperty(
                        "isCustom",
                        m.Meltano.SingerBooleanType(),
                        description="Is custom adapter",
                    ),
                    m.Meltano.SingerProperty(
                        "isDeprecated",
                        m.Meltano.SingerBooleanType(),
                        description="Is deprecated",
                    ),
                    m.Meltano.SingerProperty(
                        "documentationUrl",
                        m.Meltano.SingerStringType(),
                        description="Documentation URL",
                    ),
                )
            )
        )

    class ProjectsStream(m.TapOracleOic.OICBaseStream):
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
            _properties_to_dict(
                m.Meltano.SingerPropertiesList(
                    m.Meltano.SingerProperty(
                        "id", m.Meltano.SingerStringType(), description="Project ID"
                    ),
                    m.Meltano.SingerProperty(
                        "name", m.Meltano.SingerStringType(), description="Project name"
                    ),
                    m.Meltano.SingerProperty(
                        "description",
                        m.Meltano.SingerStringType(),
                        description="Project description",
                    ),
                    m.Meltano.SingerProperty(
                        "status",
                        m.Meltano.SingerStringType(),
                        description="Project status",
                    ),
                    *_oic_common_properties(),
                    m.Meltano.SingerProperty(
                        "folders",
                        m.Meltano.SingerArrayType(m.Meltano.SingerObjectType()),
                        description="Project folders",
                    ),
                    m.Meltano.SingerProperty(
                        "integrationCount",
                        m.Meltano.SingerIntegerType(),
                        description="Number of integrations",
                    ),
                    m.Meltano.SingerProperty(
                        "connectionCount",
                        m.Meltano.SingerIntegerType(),
                        description="Number of connections",
                    ),
                    m.Meltano.SingerProperty(
                        "permissions",
                        m.Meltano.SingerArrayType(m.Meltano.SingerObjectType()),
                        description="Project permissions",
                    ),
                )
            )
        )

    class ExecutionsStream(m.TapOracleOic.OICBaseStream):
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
            _properties_to_dict(
                m.Meltano.SingerPropertiesList(
                    m.Meltano.SingerProperty(
                        "instanceId",
                        m.Meltano.SingerStringType(),
                        description="Execution instance ID",
                    ),
                    m.Meltano.SingerProperty(
                        "integrationName",
                        m.Meltano.SingerStringType(),
                        description="Integration name",
                    ),
                    m.Meltano.SingerProperty(
                        "integrationVersion",
                        m.Meltano.SingerStringType(),
                        description="Integration version",
                    ),
                    m.Meltano.SingerProperty(
                        "status",
                        m.Meltano.SingerStringType(),
                        description="Execution status",
                    ),
                    m.Meltano.SingerProperty(
                        "startTime",
                        m.Meltano.SingerDateTimeType(),
                        description="Execution start time",
                    ),
                    m.Meltano.SingerProperty(
                        "endTime",
                        m.Meltano.SingerDateTimeType(),
                        description="Execution end time",
                    ),
                    m.Meltano.SingerProperty(
                        "duration",
                        m.Meltano.SingerIntegerType(),
                        description="Execution duration (ms)",
                    ),
                    m.Meltano.SingerProperty(
                        "errorCode",
                        m.Meltano.SingerStringType(),
                        description="Error code",
                    ),
                    m.Meltano.SingerProperty(
                        "errorMessage",
                        m.Meltano.SingerStringType(),
                        description="Error message",
                    ),
                    m.Meltano.SingerProperty(
                        "payloadSize",
                        m.Meltano.SingerIntegerType(),
                        description="Payload size",
                    ),
                    m.Meltano.SingerProperty(
                        "processedRecords",
                        m.Meltano.SingerIntegerType(),
                        description="Processed record count",
                    ),
                )
            )
        )

    class MetricsStream(m.TapOracleOic.OICBaseStream):
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
            _properties_to_dict(
                m.Meltano.SingerPropertiesList(
                    m.Meltano.SingerProperty(
                        "metricId",
                        m.Meltano.SingerStringType(),
                        description="Metric ID",
                    ),
                    m.Meltano.SingerProperty(
                        "metricName",
                        m.Meltano.SingerStringType(),
                        description="Metric name",
                    ),
                    m.Meltano.SingerProperty(
                        "timestamp",
                        m.Meltano.SingerDateTimeType(),
                        description="Metric timestamp",
                    ),
                    m.Meltano.SingerProperty(
                        "value",
                        m.Meltano.SingerNumberType(),
                        description="Metric value",
                    ),
                    m.Meltano.SingerProperty(
                        "unit", m.Meltano.SingerStringType(), description="Metric unit"
                    ),
                    m.Meltano.SingerProperty(
                        "tags", m.Meltano.SingerObjectType(), description="Metric tags"
                    ),
                    m.Meltano.SingerProperty(
                        "integrationName",
                        m.Meltano.SingerStringType(),
                        description="Related integration",
                    ),
                    m.Meltano.SingerProperty(
                        "connectionName",
                        m.Meltano.SingerStringType(),
                        description="Related connection",
                    ),
                )
            )
        )


# Stream registry - maps stream names to their classes
ALL_STREAMS: t.MappingKV[str, type[m.TapOracleOic.OICBaseStream]] = {
    "integrations": FlextTapOracleOicModelsStreams.IntegrationsStream,
    "connections": FlextTapOracleOicModelsStreams.ConnectionsStream,
    "packages": FlextTapOracleOicModelsStreams.PackagesStream,
    "lookups": FlextTapOracleOicModelsStreams.LookupsStream,
    "libraries": FlextTapOracleOicModelsStreams.LibrariesStream,
    "certificates": FlextTapOracleOicModelsStreams.CertificatesStream,
    "adapters": FlextTapOracleOicModelsStreams.AdaptersStream,
    "projects": FlextTapOracleOicModelsStreams.ProjectsStream,
    "executions": FlextTapOracleOicModelsStreams.ExecutionsStream,
    "metrics": FlextTapOracleOicModelsStreams.MetricsStream,
}

__all__: list[str] = ["ALL_STREAMS", "FlextTapOracleOicModelsStreams"]
