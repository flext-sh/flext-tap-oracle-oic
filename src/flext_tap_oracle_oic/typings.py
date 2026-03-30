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

from collections.abc import Mapping, Sequence

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

        type TapConfiguration = Mapping[
            str,
            FlextMeltanoTypes.Scalar
            | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type StreamConfiguration = Mapping[
            str,
            str | bool | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type CatalogDefinition = Mapping[
            str,
            str | Sequence[Mapping[str, FlextMeltanoTypes.ContainerValue | None]],
        ]
        type SchemaDefinition = Mapping[
            str,
            str | Mapping[str, FlextMeltanoTypes.ContainerValue | None] | bool,
        ]
        type MessageOutput = Mapping[
            str,
            str | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
        ]
        type StateManagement = Mapping[
            str,
            str | int | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
        ]

        class OicIntegration:
            """Oracle OIC integration complex types."""

            type IntegrationConfiguration = Mapping[
                str,
                FlextMeltanoTypes.Scalar
                | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type IntegrationDefinition = Mapping[
                str,
                str
                | FlextMeltanoTypes.StrSequence
                | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type IntegrationFlow = Mapping[
                str,
                str | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type IntegrationMapping = Mapping[
                str,
                str | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type IntegrationMetadata = Mapping[
                str,
                str | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type IntegrationStatus = Mapping[
                str,
                str | bool | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]

        class OicConnection:
            """Oracle OIC connection complex types."""

            type ConnectionConfiguration = Mapping[
                str,
                FlextMeltanoTypes.Scalar
                | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type ConnectionCredentials = Mapping[
                str,
                str | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type ConnectionSecurity = Mapping[
                str,
                str | bool | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type ConnectionValidation = Mapping[
                str,
                bool | str | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type ConnectionMetadata = Mapping[
                str,
                str | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type ConnectionPool = Mapping[
                str,
                int | bool | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]

        class OicAuthentication:
            """Oracle OIC authentication complex types."""

            type OAuth2Configuration = Mapping[
                str,
                str | int | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type IdcsConfiguration = Mapping[
                str,
                str | bool | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type TokenManagement = Mapping[
                str,
                str | int | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type AuthenticationFlow = Mapping[
                str,
                str | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type SecuritySettings = Mapping[
                str,
                bool | str | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type AuthenticationCache = Mapping[
                str,
                str | int | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]

        class OicMonitoring:
            """Oracle OIC monitoring complex types."""

            type ActivityConfiguration = Mapping[
                str,
                str | bool | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type MetricsCollection = Mapping[
                str,
                int | float | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type TrackingData = Mapping[
                str,
                str | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type AlertConfiguration = Mapping[
                str,
                bool | str | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type MonitoringMetrics = Mapping[
                str,
                int | float | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type AuditTrail = Mapping[
                str,
                str | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]

        class DataExtraction:
            """Data extraction complex types."""

            type ExtractionConfiguration = Mapping[
                str,
                str | bool | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type ExtractionFilter = Mapping[
                str,
                str
                | FlextMeltanoTypes.StrSequence
                | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type ExtractionMapping = Mapping[
                str,
                str | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type ExtractionResult = Mapping[
                str,
                bool | Sequence[Mapping[str, FlextMeltanoTypes.ContainerValue | None]],
            ]
            type ExtractionMetrics = Mapping[
                str,
                int | float | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type ExtractionState = Mapping[
                str,
                str | int | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]

        class StreamProcessing:
            """Stream processing complex types."""

            type StreamConfiguration = Mapping[
                str,
                str
                | bool
                | int
                | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type StreamMetadata = Mapping[
                str,
                str | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type StreamRecord = Mapping[
                str,
                FlextMeltanoTypes.ContainerValue
                | None
                | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type StreamState = Mapping[
                str,
                str | int | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type StreamBookmark = Mapping[
                str,
                str | int | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type StreamSchema = Mapping[
                str,
                str | Mapping[str, FlextMeltanoTypes.ContainerValue | None] | bool,
            ]

        class ErrorHandling:
            """Error handling complex types."""

            type ErrorConfiguration = Mapping[
                str,
                bool
                | str
                | int
                | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type ErrorRecovery = Mapping[
                str,
                str | bool | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type ErrorReporting = Mapping[
                str,
                str | int | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type ErrorClassification = Mapping[
                str,
                str | int | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type ErrorMetrics = Mapping[
                str,
                int | float | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type ErrorTracking = Sequence[
                Mapping[
                    str,
                    str | int | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
                ]
            ]

        class ProjectTypes:
            """Singer Tap Oracle OIC-specific project types.

            Adds Singer tap Oracle OIC-specific project types.
            Follows domain separation principle:
            Singer tap Oracle OIC domain owns OIC extraction and Singer protocol-specific types.
            """

            type ProjectType = c.ProjectType
            type SingerTapOracleOicProjectConfig = Mapping[
                str,
                FlextMeltanoTypes.ContainerValue | None,
            ]
            type OicExtractorConfig = Mapping[
                str,
                FlextMeltanoTypes.Scalar | FlextMeltanoTypes.StrSequence,
            ]
            type SingerProtocolConfig = Mapping[
                str,
                bool | str | Mapping[str, FlextMeltanoTypes.ContainerValue | None],
            ]
            type TapOracleOicPipelineConfig = Mapping[
                str,
                FlextMeltanoTypes.ContainerValue | None,
            ]
            type OicIntegrationStatusLiteral = (
                c.TapOracleOic.OicIntegrationStatusLiteral
            )
            type OicJobStatusLiteral = c.TapOracleOic.OicJobStatusLiteral
            type OicIntegrationTypeLiteral = c.TapOracleOic.OicIntegrationTypeLiteral
            type OicAgentTypeLiteral = c.TapOracleOic.OicAgentTypeLiteral
            type OicAgentStatusLiteral = c.TapOracleOic.OicAgentStatusLiteral
            type OicReplicationMethodLiteral = (
                c.TapOracleOic.OicReplicationMethodLiteral
            )
            type OicErrorTypeLiteral = c.TapOracleOic.OicErrorTypeLiteral


t = FlextTapOracleOicTypes
__all__ = ["FlextTapOracleOicTypes", "t"]
