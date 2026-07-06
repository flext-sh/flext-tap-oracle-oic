# AUTO-GENERATED FILE — Regenerate with: make gen
"""Models package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_oracle_oic._models._activity import OicActivityRecord
    from flext_tap_oracle_oic._models._agent import OicAgentEntity
    from flext_tap_oracle_oic._models._api_response import OicApiResponse
    from flext_tap_oracle_oic._models._auth_config import OicAuthenticationConfig
    from flext_tap_oracle_oic._models._connection import OicConnectionEntity
    from flext_tap_oracle_oic._models._envelope import OicEnvelope
    from flext_tap_oracle_oic._models._error_context import OicErrorContext
    from flext_tap_oracle_oic._models._integration import OicIntegrationEntity
    from flext_tap_oracle_oic._models._metrics import OicMetricsRecord
    from flext_tap_oracle_oic._models._oic_connection import FlextTapOracleOicConnection
    from flext_tap_oracle_oic._models._oic_execution_summary import (
        FlextTapOracleOicExecutionSummary,
    )
    from flext_tap_oracle_oic._models._oic_integration import (
        FlextTapOracleOicIntegration,
    )
    from flext_tap_oracle_oic._models._oic_lookup import FlextTapOracleOicLookup
    from flext_tap_oracle_oic._models._oic_monitoring import (
        FlextTapOracleOicMonitoringRecord,
    )
    from flext_tap_oracle_oic._models._oic_project import FlextTapOracleOicProject
    from flext_tap_oracle_oic._models._oic_resource_metadata import (
        FlextTapOracleOicResourceMetadata,
    )
    from flext_tap_oracle_oic._models._package import OicPackageEntity
    from flext_tap_oracle_oic._models._stream_config import OicStreamConfiguration
    from flext_tap_oracle_oic._models.streams import (
        ALL_STREAMS,
        FlextTapOracleOicModelsStreams,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
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
        ".streams": (
            "ALL_STREAMS",
            "FlextTapOracleOicModelsStreams",
            "th",
        ),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
