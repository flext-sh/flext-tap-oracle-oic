"""Oracle Integration Cloud - Consolidated Stream models.

Consolidated stream implementations following FLEXT namespace patterns.
All stream classes are inner classes of FlextTapOracleOicModelsStreams,
wired into m.TapOracleOic via MRO.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import ClassVar

from flext_tap_oracle_oic import m, p, t

th = t()


def _properties_to_dict(
    properties: p.TapOracleOic.TapOracleOicPrivate.PropertiesListLike,
) -> t.ContainerValueMapping:
    return t.SCHEMA_ADAPTER.validate_python(dict(properties.to_dict()))


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
        stream_schema: t.ContainerValueMapping = t.SCHEMA_ADAPTER.validate_python(
            _properties_to_dict(
                th.Meltano.SingerPropertiesList(
                    th.Meltano.SingerProperty(
                        "id",
                        th.Meltano.SingerStringType(),
                        description="Integration ID",
                    ),
                    th.Meltano.SingerProperty(
                        "name",
                        th.Meltano.SingerStringType(),
                        description="Integration name",
                    ),
                    th.Meltano.SingerProperty(
                        "version",
                        th.Meltano.SingerStringType(),
                        description="Integration version",
                    ),
                    th.Meltano.SingerProperty(
                        "description",
                        th.Meltano.SingerStringType(),
                        description="Integration description",
                    ),
                    th.Meltano.SingerProperty(
                        "status",
                        th.Meltano.SingerStringType(),
                        description="Integration status",
                    ),
                    th.Meltano.SingerProperty(
                        "pattern",
                        th.Meltano.SingerStringType(),
                        description="Integration pattern",
                    ),
                    th.Meltano.SingerProperty(
                        "style",
                        th.Meltano.SingerStringType(),
                        description="Integration style",
                    ),
                    th.Meltano.SingerProperty(
                        "created",
                        th.Meltano.SingerDateTimeType(),
                        description="Creation timestamp",
                    ),
                    th.Meltano.SingerProperty(
                        "lastUpdated",
                        th.Meltano.SingerDateTimeType(),
                        description="Last update timestamp",
                    ),
                    th.Meltano.SingerProperty(
                        "createdBy",
                        th.Meltano.SingerStringType(),
                        description="Created by user",
                    ),
                    th.Meltano.SingerProperty(
                        "lastUpdatedBy",
                        th.Meltano.SingerStringType(),
                        description="Last updated by user",
                    ),
                    th.Meltano.SingerProperty(
                        "connections",
                        th.Meltano.SingerArrayType(
                            th.Meltano.SingerObjectType(),
                        ),
                        description="Used connections",
                    ),
                    th.Meltano.SingerProperty(
                        "endpoints",
                        th.Meltano.SingerArrayType(
                            th.Meltano.SingerObjectType(),
                        ),
                        description="Integration endpoints",
                    ),
                    th.Meltano.SingerProperty(
                        "trackingFields",
                        th.Meltano.SingerArrayType(
                            th.Meltano.SingerStringType(),
                        ),
                        description="Tracking fields",
                    ),
                    th.Meltano.SingerProperty(
                        "payloadTracking",
                        th.Meltano.SingerBooleanType(),
                        description="Payload tracking enabled",
                    ),
                    th.Meltano.SingerProperty(
                        "tracing",
                        th.Meltano.SingerBooleanType(),
                        description="Tracing enabled",
                    ),
                    th.Meltano.SingerProperty(
                        "lockedBy",
                        th.Meltano.SingerStringType(),
                        description="Locked by user",
                    ),
                    th.Meltano.SingerProperty(
                        "lockedFlag",
                        th.Meltano.SingerBooleanType(),
                        description="Is locked",
                    ),
                    th.Meltano.SingerProperty(
                        "projectId",
                        th.Meltano.SingerStringType(),
                        description="Project ID",
                    ),
                    th.Meltano.SingerProperty(
                        "folderId",
                        th.Meltano.SingerStringType(),
                        description="Folder ID",
                    ),
                ),
            ),
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
        stream_schema: t.ContainerValueMapping = t.SCHEMA_ADAPTER.validate_python(
            _properties_to_dict(
                th.Meltano.SingerPropertiesList(
                    th.Meltano.SingerProperty(
                        "id",
                        th.Meltano.SingerStringType(),
                        description="Connection ID",
                    ),
                    th.Meltano.SingerProperty(
                        "name",
                        th.Meltano.SingerStringType(),
                        description="Connection name",
                    ),
                    th.Meltano.SingerProperty(
                        "description",
                        th.Meltano.SingerStringType(),
                        description="Connection description",
                    ),
                    th.Meltano.SingerProperty(
                        "adapterType",
                        th.Meltano.SingerStringType(),
                        description="Adapter type",
                    ),
                    th.Meltano.SingerProperty(
                        "adapterDisplayName",
                        th.Meltano.SingerStringType(),
                        description="Adapter display name",
                    ),
                    th.Meltano.SingerProperty(
                        "adapterVersion",
                        th.Meltano.SingerStringType(),
                        description="Adapter version",
                    ),
                    th.Meltano.SingerProperty(
                        "status",
                        th.Meltano.SingerStringType(),
                        description="Connection status",
                    ),
                    th.Meltano.SingerProperty(
                        "created",
                        th.Meltano.SingerDateTimeType(),
                        description="Creation timestamp",
                    ),
                    th.Meltano.SingerProperty(
                        "lastUpdated",
                        th.Meltano.SingerDateTimeType(),
                        description="Last update timestamp",
                    ),
                    th.Meltano.SingerProperty(
                        "createdBy",
                        th.Meltano.SingerStringType(),
                        description="Created by user",
                    ),
                    th.Meltano.SingerProperty(
                        "lastUpdatedBy",
                        th.Meltano.SingerStringType(),
                        description="Last updated by user",
                    ),
                    th.Meltano.SingerProperty(
                        "connectionUrl",
                        th.Meltano.SingerStringType(),
                        description="Connection URL",
                    ),
                    th.Meltano.SingerProperty(
                        "securityPolicy",
                        th.Meltano.SingerStringType(),
                        description="Security policy",
                    ),
                    th.Meltano.SingerProperty(
                        "connectionProperties",
                        th.Meltano.SingerObjectType(),
                        description="Connection properties",
                    ),
                    th.Meltano.SingerProperty(
                        "isValid",
                        th.Meltano.SingerBooleanType(),
                        description="Connection validity",
                    ),
                    th.Meltano.SingerProperty(
                        "usageCount",
                        th.Meltano.SingerIntegerType(),
                        description="Usage count",
                    ),
                    th.Meltano.SingerProperty(
                        "lockedBy",
                        th.Meltano.SingerStringType(),
                        description="Locked by user",
                    ),
                    th.Meltano.SingerProperty(
                        "lockedFlag",
                        th.Meltano.SingerBooleanType(),
                        description="Is locked",
                    ),
                ),
            ),
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
        stream_schema: t.ContainerValueMapping = t.SCHEMA_ADAPTER.validate_python(
            _properties_to_dict(
                th.Meltano.SingerPropertiesList(
                    th.Meltano.SingerProperty(
                        "id",
                        th.Meltano.SingerStringType(),
                        description="Package ID",
                    ),
                    th.Meltano.SingerProperty(
                        "name",
                        th.Meltano.SingerStringType(),
                        description="Package name",
                    ),
                    th.Meltano.SingerProperty(
                        "description",
                        th.Meltano.SingerStringType(),
                        description="Package description",
                    ),
                    th.Meltano.SingerProperty(
                        "version",
                        th.Meltano.SingerStringType(),
                        description="Package version",
                    ),
                    th.Meltano.SingerProperty(
                        "status",
                        th.Meltano.SingerStringType(),
                        description="Package status",
                    ),
                    th.Meltano.SingerProperty(
                        "created",
                        th.Meltano.SingerDateTimeType(),
                        description="Creation timestamp",
                    ),
                    th.Meltano.SingerProperty(
                        "lastUpdated",
                        th.Meltano.SingerDateTimeType(),
                        description="Last update timestamp",
                    ),
                    th.Meltano.SingerProperty(
                        "createdBy",
                        th.Meltano.SingerStringType(),
                        description="Created by user",
                    ),
                    th.Meltano.SingerProperty(
                        "lastUpdatedBy",
                        th.Meltano.SingerStringType(),
                        description="Last updated by user",
                    ),
                    th.Meltano.SingerProperty(
                        "integrations",
                        th.Meltano.SingerArrayType(
                            th.Meltano.SingerObjectType(),
                        ),
                        description="Included integrations",
                    ),
                    th.Meltano.SingerProperty(
                        "connections",
                        th.Meltano.SingerArrayType(
                            th.Meltano.SingerObjectType(),
                        ),
                        description="Included connections",
                    ),
                    th.Meltano.SingerProperty(
                        "size",
                        th.Meltano.SingerIntegerType(),
                        description="Package size",
                    ),
                    th.Meltano.SingerProperty(
                        "projectId",
                        th.Meltano.SingerStringType(),
                        description="Project ID",
                    ),
                ),
            ),
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
        stream_schema: t.ContainerValueMapping = t.SCHEMA_ADAPTER.validate_python(
            _properties_to_dict(
                th.Meltano.SingerPropertiesList(
                    th.Meltano.SingerProperty(
                        "name",
                        th.Meltano.SingerStringType(),
                        description="Lookup name",
                    ),
                    th.Meltano.SingerProperty(
                        "description",
                        th.Meltano.SingerStringType(),
                        description="Lookup description",
                    ),
                    th.Meltano.SingerProperty(
                        "type",
                        th.Meltano.SingerStringType(),
                        description="Lookup type",
                    ),
                    th.Meltano.SingerProperty(
                        "status",
                        th.Meltano.SingerStringType(),
                        description="Lookup status",
                    ),
                    th.Meltano.SingerProperty(
                        "created",
                        th.Meltano.SingerDateTimeType(),
                        description="Creation timestamp",
                    ),
                    th.Meltano.SingerProperty(
                        "lastUpdated",
                        th.Meltano.SingerDateTimeType(),
                        description="Last update timestamp",
                    ),
                    th.Meltano.SingerProperty(
                        "createdBy",
                        th.Meltano.SingerStringType(),
                        description="Created by user",
                    ),
                    th.Meltano.SingerProperty(
                        "lastUpdatedBy",
                        th.Meltano.SingerStringType(),
                        description="Last updated by user",
                    ),
                    th.Meltano.SingerProperty(
                        "valueCount",
                        th.Meltano.SingerIntegerType(),
                        description="Number of lookup values",
                    ),
                    th.Meltano.SingerProperty(
                        "defaultValue",
                        th.Meltano.SingerStringType(),
                        description="Default lookup value",
                    ),
                    th.Meltano.SingerProperty(
                        "isReadOnly",
                        th.Meltano.SingerBooleanType(),
                        description="Is read-only",
                    ),
                    th.Meltano.SingerProperty(
                        "usageCount",
                        th.Meltano.SingerIntegerType(),
                        description="Usage count",
                    ),
                ),
            ),
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
        stream_schema: t.ContainerValueMapping = t.SCHEMA_ADAPTER.validate_python(
            _properties_to_dict(
                th.Meltano.SingerPropertiesList(
                    th.Meltano.SingerProperty(
                        "id",
                        th.Meltano.SingerStringType(),
                        description="Library ID",
                    ),
                    th.Meltano.SingerProperty(
                        "name",
                        th.Meltano.SingerStringType(),
                        description="Library name",
                    ),
                    th.Meltano.SingerProperty(
                        "description",
                        th.Meltano.SingerStringType(),
                        description="Library description",
                    ),
                    th.Meltano.SingerProperty(
                        "type",
                        th.Meltano.SingerStringType(),
                        description="Library type",
                    ),
                    th.Meltano.SingerProperty(
                        "status",
                        th.Meltano.SingerStringType(),
                        description="Library status",
                    ),
                    th.Meltano.SingerProperty(
                        "created",
                        th.Meltano.SingerDateTimeType(),
                        description="Creation timestamp",
                    ),
                    th.Meltano.SingerProperty(
                        "lastUpdated",
                        th.Meltano.SingerDateTimeType(),
                        description="Last update timestamp",
                    ),
                    th.Meltano.SingerProperty(
                        "createdBy",
                        th.Meltano.SingerStringType(),
                        description="Created by user",
                    ),
                    th.Meltano.SingerProperty(
                        "lastUpdatedBy",
                        th.Meltano.SingerStringType(),
                        description="Last updated by user",
                    ),
                    th.Meltano.SingerProperty(
                        "version",
                        th.Meltano.SingerStringType(),
                        description="Library version",
                    ),
                    th.Meltano.SingerProperty(
                        "size",
                        th.Meltano.SingerIntegerType(),
                        description="Library size",
                    ),
                    th.Meltano.SingerProperty(
                        "usageCount",
                        th.Meltano.SingerIntegerType(),
                        description="Usage count",
                    ),
                    th.Meltano.SingerProperty(
                        "functions",
                        th.Meltano.SingerArrayType(
                            th.Meltano.SingerStringType(),
                        ),
                        description="Available functions",
                    ),
                ),
            ),
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
        stream_schema: t.ContainerValueMapping = t.SCHEMA_ADAPTER.validate_python(
            _properties_to_dict(
                th.Meltano.SingerPropertiesList(
                    th.Meltano.SingerProperty(
                        "name",
                        th.Meltano.SingerStringType(),
                        description="Certificate name",
                    ),
                    th.Meltano.SingerProperty(
                        "description",
                        th.Meltano.SingerStringType(),
                        description="Certificate description",
                    ),
                    th.Meltano.SingerProperty(
                        "type",
                        th.Meltano.SingerStringType(),
                        description="Certificate type",
                    ),
                    th.Meltano.SingerProperty(
                        "status",
                        th.Meltano.SingerStringType(),
                        description="Certificate status",
                    ),
                    th.Meltano.SingerProperty(
                        "created",
                        th.Meltano.SingerDateTimeType(),
                        description="Creation timestamp",
                    ),
                    th.Meltano.SingerProperty(
                        "lastUpdated",
                        th.Meltano.SingerDateTimeType(),
                        description="Last update timestamp",
                    ),
                    th.Meltano.SingerProperty(
                        "createdBy",
                        th.Meltano.SingerStringType(),
                        description="Created by user",
                    ),
                    th.Meltano.SingerProperty(
                        "expirationDate",
                        th.Meltano.SingerDateTimeType(),
                        description="Expiration date",
                    ),
                    th.Meltano.SingerProperty(
                        "issuer",
                        th.Meltano.SingerStringType(),
                        description="Certificate issuer",
                    ),
                    th.Meltano.SingerProperty(
                        "subject",
                        th.Meltano.SingerStringType(),
                        description="Certificate subject",
                    ),
                    th.Meltano.SingerProperty(
                        "serialNumber",
                        th.Meltano.SingerStringType(),
                        description="Serial number",
                    ),
                    th.Meltano.SingerProperty(
                        "fingerprint",
                        th.Meltano.SingerStringType(),
                        description="Certificate fingerprint",
                    ),
                    th.Meltano.SingerProperty(
                        "usageCount",
                        th.Meltano.SingerIntegerType(),
                        description="Usage count",
                    ),
                ),
            ),
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
        stream_schema: t.ContainerValueMapping = t.SCHEMA_ADAPTER.validate_python(
            _properties_to_dict(
                th.Meltano.SingerPropertiesList(
                    th.Meltano.SingerProperty(
                        "id",
                        th.Meltano.SingerStringType(),
                        description="Adapter ID",
                    ),
                    th.Meltano.SingerProperty(
                        "name",
                        th.Meltano.SingerStringType(),
                        description="Adapter name",
                    ),
                    th.Meltano.SingerProperty(
                        "displayName",
                        th.Meltano.SingerStringType(),
                        description="Adapter display name",
                    ),
                    th.Meltano.SingerProperty(
                        "description",
                        th.Meltano.SingerStringType(),
                        description="Adapter description",
                    ),
                    th.Meltano.SingerProperty(
                        "version",
                        th.Meltano.SingerStringType(),
                        description="Adapter version",
                    ),
                    th.Meltano.SingerProperty(
                        "vendor",
                        th.Meltano.SingerStringType(),
                        description="Adapter vendor",
                    ),
                    th.Meltano.SingerProperty(
                        "category",
                        th.Meltano.SingerStringType(),
                        description="Adapter category",
                    ),
                    th.Meltano.SingerProperty(
                        "capabilities",
                        th.Meltano.SingerArrayType(
                            th.Meltano.SingerStringType(),
                        ),
                        description="Adapter capabilities",
                    ),
                    th.Meltano.SingerProperty(
                        "connectionTypes",
                        th.Meltano.SingerArrayType(
                            th.Meltano.SingerStringType(),
                        ),
                        description="Connection types",
                    ),
                    th.Meltano.SingerProperty(
                        "isCustom",
                        th.Meltano.SingerBooleanType(),
                        description="Is custom adapter",
                    ),
                    th.Meltano.SingerProperty(
                        "isDeprecated",
                        th.Meltano.SingerBooleanType(),
                        description="Is deprecated",
                    ),
                    th.Meltano.SingerProperty(
                        "documentationUrl",
                        th.Meltano.SingerStringType(),
                        description="Documentation URL",
                    ),
                ),
            ),
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
        stream_schema: t.ContainerValueMapping = t.SCHEMA_ADAPTER.validate_python(
            _properties_to_dict(
                th.Meltano.SingerPropertiesList(
                    th.Meltano.SingerProperty(
                        "id",
                        th.Meltano.SingerStringType(),
                        description="Project ID",
                    ),
                    th.Meltano.SingerProperty(
                        "name",
                        th.Meltano.SingerStringType(),
                        description="Project name",
                    ),
                    th.Meltano.SingerProperty(
                        "description",
                        th.Meltano.SingerStringType(),
                        description="Project description",
                    ),
                    th.Meltano.SingerProperty(
                        "status",
                        th.Meltano.SingerStringType(),
                        description="Project status",
                    ),
                    th.Meltano.SingerProperty(
                        "created",
                        th.Meltano.SingerDateTimeType(),
                        description="Creation timestamp",
                    ),
                    th.Meltano.SingerProperty(
                        "lastUpdated",
                        th.Meltano.SingerDateTimeType(),
                        description="Last update timestamp",
                    ),
                    th.Meltano.SingerProperty(
                        "createdBy",
                        th.Meltano.SingerStringType(),
                        description="Created by user",
                    ),
                    th.Meltano.SingerProperty(
                        "lastUpdatedBy",
                        th.Meltano.SingerStringType(),
                        description="Last updated by user",
                    ),
                    th.Meltano.SingerProperty(
                        "folders",
                        th.Meltano.SingerArrayType(
                            th.Meltano.SingerObjectType(),
                        ),
                        description="Project folders",
                    ),
                    th.Meltano.SingerProperty(
                        "integrationCount",
                        th.Meltano.SingerIntegerType(),
                        description="Number of integrations",
                    ),
                    th.Meltano.SingerProperty(
                        "connectionCount",
                        th.Meltano.SingerIntegerType(),
                        description="Number of connections",
                    ),
                    th.Meltano.SingerProperty(
                        "permissions",
                        th.Meltano.SingerArrayType(
                            th.Meltano.SingerObjectType(),
                        ),
                        description="Project permissions",
                    ),
                ),
            ),
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
        stream_schema: t.ContainerValueMapping = t.SCHEMA_ADAPTER.validate_python(
            _properties_to_dict(
                th.Meltano.SingerPropertiesList(
                    th.Meltano.SingerProperty(
                        "instanceId",
                        th.Meltano.SingerStringType(),
                        description="Execution instance ID",
                    ),
                    th.Meltano.SingerProperty(
                        "integrationName",
                        th.Meltano.SingerStringType(),
                        description="Integration name",
                    ),
                    th.Meltano.SingerProperty(
                        "integrationVersion",
                        th.Meltano.SingerStringType(),
                        description="Integration version",
                    ),
                    th.Meltano.SingerProperty(
                        "status",
                        th.Meltano.SingerStringType(),
                        description="Execution status",
                    ),
                    th.Meltano.SingerProperty(
                        "startTime",
                        th.Meltano.SingerDateTimeType(),
                        description="Execution start time",
                    ),
                    th.Meltano.SingerProperty(
                        "endTime",
                        th.Meltano.SingerDateTimeType(),
                        description="Execution end time",
                    ),
                    th.Meltano.SingerProperty(
                        "duration",
                        th.Meltano.SingerIntegerType(),
                        description="Execution duration (ms)",
                    ),
                    th.Meltano.SingerProperty(
                        "errorCode",
                        th.Meltano.SingerStringType(),
                        description="Error code",
                    ),
                    th.Meltano.SingerProperty(
                        "errorMessage",
                        th.Meltano.SingerStringType(),
                        description="Error message",
                    ),
                    th.Meltano.SingerProperty(
                        "payloadSize",
                        th.Meltano.SingerIntegerType(),
                        description="Payload size",
                    ),
                    th.Meltano.SingerProperty(
                        "processedRecords",
                        th.Meltano.SingerIntegerType(),
                        description="Processed record count",
                    ),
                ),
            ),
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
        stream_schema: t.ContainerValueMapping = t.SCHEMA_ADAPTER.validate_python(
            _properties_to_dict(
                th.Meltano.SingerPropertiesList(
                    th.Meltano.SingerProperty(
                        "metricId",
                        th.Meltano.SingerStringType(),
                        description="Metric ID",
                    ),
                    th.Meltano.SingerProperty(
                        "metricName",
                        th.Meltano.SingerStringType(),
                        description="Metric name",
                    ),
                    th.Meltano.SingerProperty(
                        "timestamp",
                        th.Meltano.SingerDateTimeType(),
                        description="Metric timestamp",
                    ),
                    th.Meltano.SingerProperty(
                        "value",
                        th.Meltano.SingerNumberType(),
                        description="Metric value",
                    ),
                    th.Meltano.SingerProperty(
                        "unit",
                        th.Meltano.SingerStringType(),
                        description="Metric unit",
                    ),
                    th.Meltano.SingerProperty(
                        "tags",
                        th.Meltano.SingerObjectType(),
                        description="Metric tags",
                    ),
                    th.Meltano.SingerProperty(
                        "integrationName",
                        th.Meltano.SingerStringType(),
                        description="Related integration",
                    ),
                    th.Meltano.SingerProperty(
                        "connectionName",
                        th.Meltano.SingerStringType(),
                        description="Related connection",
                    ),
                ),
            ),
        )


# Stream registry - maps stream names to their classes
ALL_STREAMS: Mapping[str, type[m.TapOracleOic.OICBaseStream]] = {
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

__all__ = [
    "ALL_STREAMS",
    "FlextTapOracleOicModelsStreams",
    "th",
]
