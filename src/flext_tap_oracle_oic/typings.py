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

from flext_core import FlextTypes as _t

# =============================================================================
# TAP ORACLE OIC-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for Singer Oracle OIC operations
# =============================================================================


# Singer Oracle OIC tap domain TypeVars
class FlextMeltanoTapOracleOicTypes(_t):
    """Singer Oracle OIC tap-specific type definitions extending t.

    Domain-specific type system for Singer Oracle OIC tap operations.
    Contains ONLY complex Oracle OIC tap-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # SINGER TAP TYPES - Complex Singer protocol types
    # =========================================================================

    class SingerTap:
        """Singer tap protocol complex types."""

        type TapConfiguration = dict[
            str, str | int | bool | dict[str, _t.GeneralValueType]
        ]
        type StreamConfiguration = dict[
            str,
            str | bool | dict[str, _t.JsonValue],
        ]
        type CatalogDefinition = dict[str, str | list[dict[str, _t.JsonValue]]]
        type SchemaDefinition = dict[str, str | dict[str, _t.JsonValue] | bool]
        type MessageOutput = dict[str, str | dict[str, _t.JsonValue]]
        type StateManagement = dict[str, str | int | dict[str, _t.JsonValue]]

    # =========================================================================
    # ORACLE OIC INTEGRATION TYPES - Complex Oracle OIC integration types
    # =========================================================================

    class OicIntegration:
        """Oracle OIC integration complex types."""

        type IntegrationConfiguration = dict[
            str, str | int | bool | dict[str, _t.GeneralValueType]
        ]
        type IntegrationDefinition = dict[
            str,
            str | list[str] | dict[str, _t.JsonValue],
        ]
        type IntegrationFlow = dict[str, str | dict[str, _t.JsonValue]]
        type IntegrationMapping = dict[str, str | dict[str, _t.GeneralValueType]]
        type IntegrationMetadata = dict[str, str | dict[str, _t.JsonValue]]
        type IntegrationStatus = dict[str, str | bool | dict[str, _t.GeneralValueType]]

    # =========================================================================
    # OIC CONNECTION TYPES - Complex Oracle OIC connection types
    # =========================================================================

    class OicConnection:
        """Oracle OIC connection complex types."""

        type ConnectionConfiguration = dict[
            str, str | int | bool | dict[str, _t.GeneralValueType]
        ]
        type ConnectionCredentials = dict[str, str | dict[str, _t.JsonValue]]
        type ConnectionSecurity = dict[str, str | bool | dict[str, _t.GeneralValueType]]
        type ConnectionValidation = dict[
            str, bool | str | dict[str, _t.GeneralValueType]
        ]
        type ConnectionMetadata = dict[str, str | dict[str, _t.JsonValue]]
        type ConnectionPool = dict[str, int | bool | dict[str, _t.GeneralValueType]]

    # =========================================================================
    # OIC AUTHENTICATION TYPES - Complex OAuth2/IDCS authentication types
    # =========================================================================

    class OicAuthentication:
        """Oracle OIC authentication complex types."""

        type OAuth2Configuration = dict[str, str | int | dict[str, _t.GeneralValueType]]
        type IdcsConfiguration = dict[str, str | bool | dict[str, _t.JsonValue]]
        type TokenManagement = dict[str, str | int | dict[str, _t.GeneralValueType]]
        type AuthenticationFlow = dict[str, str | dict[str, _t.JsonValue]]
        type SecuritySettings = dict[str, bool | str | dict[str, _t.GeneralValueType]]
        type AuthenticationCache = dict[str, str | int | dict[str, _t.GeneralValueType]]

    # =========================================================================
    # OIC MONITORING TYPES - Complex Oracle OIC monitoring and activity types
    # =========================================================================

    class OicMonitoring:
        """Oracle OIC monitoring complex types."""

        type ActivityConfiguration = dict[
            str, str | bool | dict[str, _t.GeneralValueType]
        ]
        type MetricsCollection = dict[
            str,
            int | float | dict[str, _t.JsonValue],
        ]
        type TrackingData = dict[str, str | dict[str, _t.JsonValue]]
        type AlertConfiguration = dict[str, bool | str | dict[str, _t.GeneralValueType]]
        type MonitoringMetrics = dict[
            str,
            int | float | dict[str, _t.JsonValue],
        ]
        type AuditTrail = dict[str, str | dict[str, _t.JsonValue]]

    # =========================================================================
    # DATA EXTRACTION TYPES - Complex data extraction types
    # =========================================================================

    class DataExtraction:
        """Data extraction complex types."""

        type ExtractionConfiguration = dict[
            str, str | bool | dict[str, _t.GeneralValueType]
        ]
        type ExtractionFilter = dict[
            str, str | list[str] | dict[str, _t.GeneralValueType]
        ]
        type ExtractionMapping = dict[str, str | dict[str, _t.JsonValue]]
        type ExtractionResult = dict[str, bool | list[dict[str, _t.GeneralValueType]]]
        type ExtractionMetrics = dict[
            str,
            int | float | dict[str, _t.JsonValue],
        ]
        type ExtractionState = dict[str, str | int | dict[str, _t.JsonValue]]

    # =========================================================================
    # STREAM PROCESSING TYPES - Complex stream handling types
    # =========================================================================

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = dict[
            str, str | bool | int | dict[str, _t.GeneralValueType]
        ]
        type StreamMetadata = dict[str, str | dict[str, _t.JsonValue]]
        type StreamRecord = dict[str, _t.JsonValue | dict[str, _t.GeneralValueType]]
        type StreamState = dict[str, str | int | dict[str, _t.JsonValue]]
        type StreamBookmark = dict[str, str | int | dict[str, _t.GeneralValueType]]
        type StreamSchema = dict[str, str | dict[str, _t.JsonValue] | bool]

    # =========================================================================
    # ERROR HANDLING TYPES - Complex error management types
    # =========================================================================

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = dict[
            str, bool | str | int | dict[str, _t.GeneralValueType]
        ]
        type ErrorRecovery = dict[str, str | bool | dict[str, _t.GeneralValueType]]
        type ErrorReporting = dict[str, str | int | dict[str, _t.JsonValue]]
        type ErrorClassification = dict[str, str | int | dict[str, _t.GeneralValueType]]
        type ErrorMetrics = dict[str, int | float | dict[str, _t.JsonValue]]
        type ErrorTracking = list[dict[str, str | int | dict[str, _t.JsonValue]]]

    # =========================================================================
    # SINGER TAP ORACLE OIC PROJECT TYPES - Domain-specific project types extending t
    # =========================================================================

    class Project:
        """Singer Tap Oracle OIC-specific project types.

        Adds Singer tap Oracle OIC-specific project types.
        Follows domain separation principle:
        Singer tap Oracle OIC domain owns OIC extraction and Singer protocol-specific types.
        """

        # Singer tap Oracle OIC-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from t
            "library",
            "application",
            "service",
            # Singer tap Oracle OIC-specific types
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

        # Singer tap Oracle OIC-specific project configurations
        type SingerTapOracleOicProjectConfig = dict[str, _t.GeneralValueType]
        type OicExtractorConfig = dict[str, str | int | bool | list[str]]
        type SingerProtocolConfig = dict[
            str, bool | str | dict[str, _t.GeneralValueType]
        ]
        type TapOracleOicPipelineConfig = dict[str, _t.GeneralValueType]

        # Singer tap Oracle OIC-specific Literal type aliases (referencing constants.py StrEnums)
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

    class TapOracleOic:
        """Tap Oracle OIC types namespace for cross-project access.

        Provides organized access to all Tap Oracle OIC types for other FLEXT projects.
        Usage: Other projects can reference `t.TapOracleOic.OracleOicIntegration.*`, `t.TapOracleOic.Project.*`, etc.
        This enables consistent namespace patterns for cross-project type access.

        Examples:
            from flext_tap_oracle_oic.typings import t
            config: t.TapOracleOic.Project.SingerTapOracleOicProjectConfig = ...
            integration: t.TapOracleOic.OracleOicIntegration.IntegrationDefinition = ...

        Note: Namespace composition via inheritance - no aliases needed.
        Access parent namespaces directly through inheritance.

        """


# Alias for simplified usage
t = FlextMeltanoTapOracleOicTypes

# Namespace composition via class inheritance
# TapOracleOic namespace provides access to nested classes through inheritance
# Access patterns:
# - t.TapOracleOic.* for Tap Oracle OIC-specific types
# - t.Project.* for project types
# - t.Core.* for core types (inherited from parent)

# =============================================================================
# PUBLIC API EXPORTS - Singer Oracle OIC tap TypeVars and types
# =============================================================================

__all__ = [
    "FlextMeltanoTapOracleOicTypes",
    "t",
]
