"""FLEXT Tap Oracle OIC Types - Domain-specific Singer Oracle OIC tap type definitions.

This module provides Singer Oracle OIC tap-specific type definitions extending t.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends t properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_meltano import FlextMeltanoTypes
from flext_oracle_oic import FlextOracleOicTypes


class FlextTapOracleOicTypes(FlextMeltanoTypes, FlextOracleOicTypes):
    """Singer Oracle OIC tap-specific type definitions extending t.

    Domain-specific type system for Singer Oracle OIC tap operations.
    Contains ONLY complex Oracle OIC tap-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    class TapOracleOic:
        """Singer tap protocol complex types."""

        type TapConfiguration = dict[
            str, str | int | bool | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type StreamConfiguration = dict[
            str, str | bool | dict[str, FlextMeltanoTypes.JsonValue]
        ]
        type CatalogDefinition = dict[
            str, str | list[dict[str, FlextMeltanoTypes.JsonValue]]
        ]
        type SchemaDefinition = dict[
            str, str | dict[str, FlextMeltanoTypes.JsonValue] | bool
        ]
        type MessageOutput = dict[str, str | dict[str, FlextMeltanoTypes.JsonValue]]
        type StateManagement = dict[
            str, str | int | dict[str, FlextMeltanoTypes.JsonValue]
        ]

    class OicIntegration:
        """Oracle OIC integration complex types."""

        type IntegrationConfiguration = dict[
            str, str | int | bool | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type IntegrationDefinition = dict[
            str, str | list[str] | dict[str, FlextMeltanoTypes.JsonValue]
        ]
        type IntegrationFlow = dict[str, str | dict[str, FlextMeltanoTypes.JsonValue]]
        type IntegrationMapping = dict[
            str, str | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type IntegrationMetadata = dict[
            str, str | dict[str, FlextMeltanoTypes.JsonValue]
        ]
        type IntegrationStatus = dict[
            str, str | bool | dict[str, FlextMeltanoTypes.ContainerValue]
        ]

    class OicConnection:
        """Oracle OIC connection complex types."""

        type ConnectionConfiguration = dict[
            str, str | int | bool | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type ConnectionCredentials = dict[
            str, str | dict[str, FlextMeltanoTypes.JsonValue]
        ]
        type ConnectionSecurity = dict[
            str, str | bool | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type ConnectionValidation = dict[
            str, bool | str | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type ConnectionMetadata = dict[
            str, str | dict[str, FlextMeltanoTypes.JsonValue]
        ]
        type ConnectionPool = dict[
            str, int | bool | dict[str, FlextMeltanoTypes.ContainerValue]
        ]

    class OicAuthentication:
        """Oracle OIC authentication complex types."""

        type OAuth2Configuration = dict[
            str, str | int | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type IdcsConfiguration = dict[
            str, str | bool | dict[str, FlextMeltanoTypes.JsonValue]
        ]
        type TokenManagement = dict[
            str, str | int | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type AuthenticationFlow = dict[
            str, str | dict[str, FlextMeltanoTypes.JsonValue]
        ]
        type SecuritySettings = dict[
            str, bool | str | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type AuthenticationCache = dict[
            str, str | int | dict[str, FlextMeltanoTypes.ContainerValue]
        ]

    class OicMonitoring:
        """Oracle OIC monitoring complex types."""

        type ActivityConfiguration = dict[
            str, str | bool | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type MetricsCollection = dict[
            str, int | float | dict[str, FlextMeltanoTypes.JsonValue]
        ]
        type TrackingData = dict[str, str | dict[str, FlextMeltanoTypes.JsonValue]]
        type AlertConfiguration = dict[
            str, bool | str | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type MonitoringMetrics = dict[
            str, int | float | dict[str, FlextMeltanoTypes.JsonValue]
        ]
        type AuditTrail = dict[str, str | dict[str, FlextMeltanoTypes.JsonValue]]

    class DataExtraction:
        """Data extraction complex types."""

        type ExtractionConfiguration = dict[
            str, str | bool | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type ExtractionFilter = dict[
            str, str | list[str] | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type ExtractionMapping = dict[str, str | dict[str, FlextMeltanoTypes.JsonValue]]
        type ExtractionResult = dict[
            str, bool | list[dict[str, FlextMeltanoTypes.ContainerValue]]
        ]
        type ExtractionMetrics = dict[
            str, int | float | dict[str, FlextMeltanoTypes.JsonValue]
        ]
        type ExtractionState = dict[
            str, str | int | dict[str, FlextMeltanoTypes.JsonValue]
        ]

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = dict[
            str, str | bool | int | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type StreamMetadata = dict[str, str | dict[str, FlextMeltanoTypes.JsonValue]]
        type StreamRecord = dict[
            str,
            FlextMeltanoTypes.JsonValue | dict[str, FlextMeltanoTypes.ContainerValue],
        ]
        type StreamState = dict[str, str | int | dict[str, FlextMeltanoTypes.JsonValue]]
        type StreamBookmark = dict[
            str, str | int | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type StreamSchema = dict[
            str, str | dict[str, FlextMeltanoTypes.JsonValue] | bool
        ]

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = dict[
            str, bool | str | int | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type ErrorRecovery = dict[
            str, str | bool | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type ErrorReporting = dict[
            str, str | int | dict[str, FlextMeltanoTypes.JsonValue]
        ]
        type ErrorClassification = dict[
            str, str | int | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type ErrorMetrics = dict[
            str, int | float | dict[str, FlextMeltanoTypes.JsonValue]
        ]
        type ErrorTracking = list[
            dict[str, str | int | dict[str, FlextMeltanoTypes.JsonValue]]
        ]

    class Project:
        """Singer Tap Oracle OIC-specific project types.

        Adds Singer tap Oracle OIC-specific project types.
        Follows domain separation principle:
        Singer tap Oracle OIC domain owns OIC extraction and Singer protocol-specific types.
        """

        type ProjectType = Literal[
            "library",
            "application",
            "service",
            "singer-tap",
            "oic-extractor",
            "integration-extractor",
            "singer-tap-oracle-oic",
            "tap-oracle-oic",
            "oic-connector",
            "integration-connector",
            "singer-protocol",
            "oic-integration",
            "oracle-oic",
            "cloud-integration",
            "singer-stream",
            "etl-tap",
            "data-pipeline",
            "oic-tap",
            "singer-integration",
        ]
        type SingerTapOracleOicProjectConfig = dict[
            str, FlextMeltanoTypes.ContainerValue
        ]
        type OicExtractorConfig = dict[str, str | int | bool | list[str]]
        type SingerProtocolConfig = dict[
            str, bool | str | dict[str, FlextMeltanoTypes.ContainerValue]
        ]
        type TapOracleOicPipelineConfig = dict[str, FlextMeltanoTypes.ContainerValue]
        type OicIntegrationStatusLiteral = Literal[
            "ACTIVE", "INACTIVE", "DRAFT", "ERROR", "TESTING", "DEPRECATED"
        ]
        type OicJobStatusLiteral = Literal[
            "RUNNING", "COMPLETED", "FAILED", "ABORTED", "SUSPENDED"
        ]
        type OicIntegrationTypeLiteral = Literal[
            "INTEGRATION", "LIBRARY", "TEMPLATE", "RECIPE", "CONNECTIVITY_AGENT"
        ]
        type OicAgentTypeLiteral = Literal["ON_PREMISES_AGENT", "FILE_AGENT"]
        type OicAgentStatusLiteral = Literal["ONLINE", "OFFLINE", "MAINTENANCE"]
        type OicReplicationMethodLiteral = Literal["FULL_TABLE", "INCREMENTAL"]
        type OicErrorTypeLiteral = Literal[
            "AUTHENTICATION",
            "AUTHORIZATION",
            "RATE_LIMIT",
            "SERVER_ERROR",
            "NETWORK",
            "VALIDATION",
        ]


t = FlextTapOracleOicTypes
__all__ = ["FlextTapOracleOicTypes", "t"]
