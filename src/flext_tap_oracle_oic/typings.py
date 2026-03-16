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

from flext_meltano import FlextMeltanoTypes
from flext_oracle_oic import FlextOracleOicTypes

from flext_tap_oracle_oic import c


class FlextTapOracleOicTypes(FlextMeltanoTypes, FlextOracleOicTypes):
    """Singer Oracle OIC tap-specific type definitions extending t.

    Domain-specific type system for Singer Oracle OIC tap operations.
    Contains ONLY complex Oracle OIC tap-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    class TapOracleOic:
        """Singer tap protocol complex types."""

        type TapConfiguration = dict[
            str,
            str | int | bool | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type StreamConfiguration = dict[
            str,
            str | bool | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type CatalogDefinition = dict[
            str,
            str | list[dict[str, FlextMeltanoTypes.ContainerValue | None]],
        ]
        type SchemaDefinition = dict[
            str,
            str | dict[str, FlextMeltanoTypes.ContainerValue | None] | bool,
        ]
        type MessageOutput = dict[
            str,
            str | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type StateManagement = dict[
            str,
            str | int | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]

    class OicIntegration:
        """Oracle OIC integration complex types."""

        type IntegrationConfiguration = dict[
            str,
            str | int | bool | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type IntegrationDefinition = dict[
            str,
            str | list[str] | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type IntegrationFlow = dict[
            str,
            str | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type IntegrationMapping = dict[
            str,
            str | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type IntegrationMetadata = dict[
            str,
            str | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type IntegrationStatus = dict[
            str,
            str | bool | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]

    class OicConnection:
        """Oracle OIC connection complex types."""

        type ConnectionConfiguration = dict[
            str,
            str | int | bool | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type ConnectionCredentials = dict[
            str,
            str | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type ConnectionSecurity = dict[
            str,
            str | bool | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type ConnectionValidation = dict[
            str,
            bool | str | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type ConnectionMetadata = dict[
            str,
            str | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type ConnectionPool = dict[
            str,
            int | bool | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]

    class OicAuthentication:
        """Oracle OIC authentication complex types."""

        type OAuth2Configuration = dict[
            str,
            str | int | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type IdcsConfiguration = dict[
            str,
            str | bool | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type TokenManagement = dict[
            str,
            str | int | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type AuthenticationFlow = dict[
            str,
            str | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type SecuritySettings = dict[
            str,
            bool | str | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type AuthenticationCache = dict[
            str,
            str | int | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]

    class OicMonitoring:
        """Oracle OIC monitoring complex types."""

        type ActivityConfiguration = dict[
            str,
            str | bool | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type MetricsCollection = dict[
            str,
            int | float | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type TrackingData = dict[
            str,
            str | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type AlertConfiguration = dict[
            str,
            bool | str | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type MonitoringMetrics = dict[
            str,
            int | float | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type AuditTrail = dict[
            str,
            str | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]

    class DataExtraction:
        """Data extraction complex types."""

        type ExtractionConfiguration = dict[
            str,
            str | bool | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type ExtractionFilter = dict[
            str,
            str | list[str] | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type ExtractionMapping = dict[
            str,
            str | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type ExtractionResult = dict[
            str,
            bool | list[dict[str, FlextMeltanoTypes.ContainerValue | None]],
        ]
        type ExtractionMetrics = dict[
            str,
            int | float | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type ExtractionState = dict[
            str,
            str | int | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = dict[
            str,
            str | bool | int | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type StreamMetadata = dict[
            str,
            str | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type StreamRecord = dict[
            str,
            FlextMeltanoTypes.ContainerValue
            | None
            | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type StreamState = dict[
            str,
            str | int | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type StreamBookmark = dict[
            str,
            str | int | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type StreamSchema = dict[
            str,
            str | dict[str, FlextMeltanoTypes.ContainerValue | None] | bool,
        ]

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = dict[
            str,
            bool | str | int | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type ErrorRecovery = dict[
            str,
            str | bool | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type ErrorReporting = dict[
            str,
            str | int | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type ErrorClassification = dict[
            str,
            str | int | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type ErrorMetrics = dict[
            str,
            int | float | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type ErrorTracking = list[
            dict[
                str,
                str | int | dict[str, FlextMeltanoTypes.ContainerValue | None],
            ]
        ]

    class ProjectTypes:
        """Singer Tap Oracle OIC-specific project types.

        Adds Singer tap Oracle OIC-specific project types.
        Follows domain separation principle:
        Singer tap Oracle OIC domain owns OIC extraction and Singer protocol-specific types.
        """

        type ProjectType = c.ProjectType
        type SingerTapOracleOicProjectConfig = dict[
            str,
            FlextMeltanoTypes.ContainerValue | None,
        ]
        type OicExtractorConfig = dict[str, str | int | bool | list[str]]
        type SingerProtocolConfig = dict[
            str,
            bool | str | dict[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type TapOracleOicPipelineConfig = dict[
            str,
            FlextMeltanoTypes.ContainerValue | None,
        ]
        type OicIntegrationStatusLiteral = c.OicIntegrationStatusLiteral
        type OicJobStatusLiteral = c.OicJobStatusLiteral
        type OicIntegrationTypeLiteral = c.OicIntegrationTypeLiteral
        type OicAgentTypeLiteral = c.OicAgentTypeLiteral
        type OicAgentStatusLiteral = c.OicAgentStatusLiteral
        type OicReplicationMethodLiteral = c.OicReplicationMethodLiteral
        type OicErrorTypeLiteral = c.OicErrorTypeLiteral


t = FlextTapOracleOicTypes
__all__ = ["FlextTapOracleOicTypes", "t"]
