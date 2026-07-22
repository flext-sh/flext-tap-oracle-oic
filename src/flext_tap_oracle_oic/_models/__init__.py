# AUTO-GENERATED FILE — Regenerate with: make gen
"""Models package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_oracle_oic._models._activity import (
        OicActivityRecord as OicActivityRecord,
    )
    from flext_tap_oracle_oic._models._agent import OicAgentEntity as OicAgentEntity
    from flext_tap_oracle_oic._models._api_response import (
        OicApiResponse as OicApiResponse,
    )
    from flext_tap_oracle_oic._models._auth_config import (
        OicAuthenticationConfig as OicAuthenticationConfig,
    )
    from flext_tap_oracle_oic._models._connection import (
        OicConnectionEntity as OicConnectionEntity,
    )
    from flext_tap_oracle_oic._models._envelope import OicEnvelope as OicEnvelope
    from flext_tap_oracle_oic._models._error_context import (
        OicErrorContext as OicErrorContext,
    )
    from flext_tap_oracle_oic._models._helpers import (
        require_entity_value as require_entity_value,
        validate_entity_identity_and_port as validate_entity_identity_and_port,
        validate_optional_port as validate_optional_port,
    )
    from flext_tap_oracle_oic._models._integration import (
        OicIntegrationEntity as OicIntegrationEntity,
    )
    from flext_tap_oracle_oic._models._metrics import (
        OicMetricsRecord as OicMetricsRecord,
    )
    from flext_tap_oracle_oic._models._oic_connection import (
        FlextTapOracleOicConnection as FlextTapOracleOicConnection,
    )
    from flext_tap_oracle_oic._models._oic_execution_summary import (
        FlextTapOracleOicExecutionSummary as FlextTapOracleOicExecutionSummary,
    )
    from flext_tap_oracle_oic._models._oic_integration import (
        FlextTapOracleOicIntegration as FlextTapOracleOicIntegration,
    )
    from flext_tap_oracle_oic._models._oic_lookup import (
        FlextTapOracleOicLookup as FlextTapOracleOicLookup,
    )
    from flext_tap_oracle_oic._models._oic_monitoring import (
        FlextTapOracleOicMonitoringRecord as FlextTapOracleOicMonitoringRecord,
    )
    from flext_tap_oracle_oic._models._oic_project import (
        FlextTapOracleOicProject as FlextTapOracleOicProject,
    )
    from flext_tap_oracle_oic._models._oic_resource_metadata import (
        FlextTapOracleOicResourceMetadata as FlextTapOracleOicResourceMetadata,
    )
    from flext_tap_oracle_oic._models._package import (
        OicPackageEntity as OicPackageEntity,
    )
    from flext_tap_oracle_oic._models._stream_config import (
        OicStreamConfiguration as OicStreamConfiguration,
    )
    from flext_tap_oracle_oic._models.streams import (
        ALL_STREAMS as ALL_STREAMS,
        FlextTapOracleOicModelsStreams as FlextTapOracleOicModelsStreams,
        th as th,
    )
_LAZY_IMPORTS = build_lazy_import_map({
    "._activity": ("OicActivityRecord",),
    "._agent": ("OicAgentEntity",),
    "._api_response": ("OicApiResponse",),
    "._auth_config": ("OicAuthenticationConfig",),
    "._connection": ("OicConnectionEntity",),
    "._envelope": ("OicEnvelope",),
    "._error_context": ("OicErrorContext",),
    "._helpers": (
        "require_entity_value",
        "validate_entity_identity_and_port",
        "validate_optional_port",
    ),
    "._integration": ("OicIntegrationEntity",),
    "._metrics": ("OicMetricsRecord",),
    "._oic_connection": ("FlextTapOracleOicConnection",),
    "._oic_execution_summary": ("FlextTapOracleOicExecutionSummary",),
    "._oic_integration": ("FlextTapOracleOicIntegration",),
    "._oic_lookup": ("FlextTapOracleOicLookup",),
    "._oic_monitoring": ("FlextTapOracleOicMonitoringRecord",),
    "._oic_project": ("FlextTapOracleOicProject",),
    "._oic_resource_metadata": ("FlextTapOracleOicResourceMetadata",),
    "._package": ("OicPackageEntity",),
    "._stream_config": ("OicStreamConfiguration",),
    ".streams": ("ALL_STREAMS", "FlextTapOracleOicModelsStreams", "th"),
})


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
