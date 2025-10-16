"""FLEXT Tap Oracle OIC Types - Domain-specific Singer Oracle OIC tap type definitions.

This module provides Singer Oracle OIC tap-specific type definitions extending FlextTypes.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends FlextTypes properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextTypes

# =============================================================================
# TAP ORACLE OIC-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for Singer Oracle OIC operations
# =============================================================================


# Singer Oracle OIC tap domain TypeVars
class FlextMeltanoTapOracleOicTypes(FlextTypes):
    """Singer Oracle OIC tap-specific type definitions extending FlextTypes.

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
            str, str | int | bool | dict[str, FlextTypes.ConfigValue]
        ]
        type StreamConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.JsonValue]
        ]
        type CatalogDefinition = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        type SchemaDefinition = dict[str, str | dict[str, FlextTypes.JsonValue] | bool]
        type MessageOutput = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type StateManagement = dict[str, str | int | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # ORACLE OIC INTEGRATION TYPES - Complex Oracle OIC integration types
    # =========================================================================

    class OicIntegration:
        """Oracle OIC integration complex types."""

        type IntegrationConfiguration = dict[
            str, str | int | bool | dict[str, FlextTypes.ConfigValue]
        ]
        type IntegrationDefinition = dict[
            str, str | FlextTypes.StringList | dict[str, FlextTypes.JsonValue]
        ]
        type IntegrationFlow = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type IntegrationMapping = dict[str, str | FlextTypes.Dict]
        type IntegrationMetadata = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type IntegrationStatus = dict[str, str | bool | FlextTypes.Dict]

    # =========================================================================
    # OIC CONNECTION TYPES - Complex Oracle OIC connection types
    # =========================================================================

    class OicConnection:
        """Oracle OIC connection complex types."""

        type ConnectionConfiguration = dict[
            str, str | int | bool | dict[str, FlextTypes.ConfigValue]
        ]
        type ConnectionCredentials = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type ConnectionSecurity = dict[
            str, str | bool | dict[str, FlextTypes.ConfigValue]
        ]
        type ConnectionValidation = dict[str, bool | str | FlextTypes.Dict]
        type ConnectionMetadata = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type ConnectionPool = dict[str, int | bool | FlextTypes.Dict]

    # =========================================================================
    # OIC AUTHENTICATION TYPES - Complex OAuth2/IDCS authentication types
    # =========================================================================

    class OicAuthentication:
        """Oracle OIC authentication complex types."""

        type OAuth2Configuration = dict[
            str, str | int | dict[str, FlextTypes.ConfigValue]
        ]
        type IdcsConfiguration = dict[str, str | bool | dict[str, FlextTypes.JsonValue]]
        type TokenManagement = dict[str, str | int | FlextTypes.Dict]
        type AuthenticationFlow = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type SecuritySettings = dict[
            str, bool | str | dict[str, FlextTypes.ConfigValue]
        ]
        type AuthenticationCache = dict[str, str | int | FlextTypes.Dict]

    # =========================================================================
    # OIC MONITORING TYPES - Complex Oracle OIC monitoring and activity types
    # =========================================================================

    class OicMonitoring:
        """Oracle OIC monitoring complex types."""

        type ActivityConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.ConfigValue]
        ]
        type MetricsCollection = dict[
            str, int | float | dict[str, FlextTypes.JsonValue]
        ]
        type TrackingData = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type AlertConfiguration = dict[str, bool | str | FlextTypes.Dict]
        type MonitoringMetrics = dict[
            str, int | float | dict[str, FlextTypes.JsonValue]
        ]
        type AuditTrail = dict[str, str | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # DATA EXTRACTION TYPES - Complex data extraction types
    # =========================================================================

    class DataExtraction:
        """Data extraction complex types."""

        type ExtractionConfiguration = dict[
            str, str | bool | dict[str, FlextTypes.ConfigValue]
        ]
        type ExtractionFilter = dict[str, str | FlextTypes.StringList | FlextTypes.Dict]
        type ExtractionMapping = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type ExtractionResult = dict[str, bool | list[FlextTypes.Dict]]
        type ExtractionMetrics = dict[
            str, int | float | dict[str, FlextTypes.JsonValue]
        ]
        type ExtractionState = dict[str, str | int | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # STREAM PROCESSING TYPES - Complex stream handling types
    # =========================================================================

    class StreamProcessing:
        """Stream processing complex types."""

        type StreamConfiguration = dict[
            str, str | bool | int | dict[str, FlextTypes.ConfigValue]
        ]
        type StreamMetadata = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type StreamRecord = dict[str, FlextTypes.JsonValue | FlextTypes.Dict]
        type StreamState = dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        type StreamBookmark = dict[str, str | int | FlextTypes.Dict]
        type StreamSchema = dict[str, str | dict[str, FlextTypes.JsonValue] | bool]

    # =========================================================================
    # ERROR HANDLING TYPES - Complex error management types
    # =========================================================================

    class ErrorHandling:
        """Error handling complex types."""

        type ErrorConfiguration = dict[
            str, bool | str | int | dict[str, FlextTypes.ConfigValue]
        ]
        type ErrorRecovery = dict[str, str | bool | FlextTypes.Dict]
        type ErrorReporting = dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        type ErrorClassification = dict[str, str | int | FlextTypes.Dict]
        type ErrorMetrics = dict[str, int | float | dict[str, FlextTypes.JsonValue]]
        type ErrorTracking = list[
            dict[str, str | int | dict[str, FlextTypes.JsonValue]]
        ]

    # =========================================================================
    # SINGER TAP ORACLE OIC PROJECT TYPES - Domain-specific project types extending FlextTypes
    # =========================================================================

    class Project(FlextTypes.Project):
        """Singer Tap Oracle OIC-specific project types extending FlextTypes.Project.

        Adds Singer tap Oracle OIC-specific project types while inheriting
        generic types from FlextTypes. Follows domain separation principle:
        Singer tap Oracle OIC domain owns OIC extraction and Singer protocol-specific types.
        """

        # Singer tap Oracle OIC-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextTypes.Project
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
        type SingerTapOracleOicProjectConfig = dict[
            str, FlextTypes.ConfigValue | object
        ]
        type OicExtractorConfig = dict[str, str | int | bool | FlextTypes.StringList]
        type SingerProtocolConfig = dict[str, bool | str | FlextTypes.Dict]
        type TapOracleOicPipelineConfig = dict[str, FlextTypes.ConfigValue | object]


# =============================================================================
# PUBLIC API EXPORTS - Singer Oracle OIC tap TypeVars and types
# =============================================================================

__all__: FlextTypes.StringList = [
    "FlextMeltanoTapOracleOicTypes",
]
