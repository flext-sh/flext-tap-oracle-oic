# @generated AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Oracle Oic. Models package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from ._activity import OicActivityRecord as OicActivityRecord
    from ._agent import OicAgentEntity as OicAgentEntity
    from ._api_response import OicApiResponse as OicApiResponse
    from ._auth_config import OicAuthenticationConfig as OicAuthenticationConfig
    from ._connection import OicConnectionEntity as OicConnectionEntity
    from ._envelope import OicEnvelope as OicEnvelope
    from ._error_context import OicErrorContext as OicErrorContext
    from ._helpers import require_entity_value as require_entity_value
    from ._helpers import (
        validate_entity_identity_and_port as validate_entity_identity_and_port,
    )
    from ._helpers import validate_optional_port as validate_optional_port
    from ._integration import OicIntegrationEntity as OicIntegrationEntity
    from ._metrics import OicMetricsRecord as OicMetricsRecord
    from ._oic_connection import (
        FlextTapOracleOicConnection as FlextTapOracleOicConnection,
    )
    from ._oic_execution_summary import (
        FlextTapOracleOicExecutionSummary as FlextTapOracleOicExecutionSummary,
    )
    from ._oic_integration import (
        FlextTapOracleOicIntegration as FlextTapOracleOicIntegration,
    )
    from ._oic_lookup import FlextTapOracleOicLookup as FlextTapOracleOicLookup
    from ._oic_monitoring import (
        FlextTapOracleOicMonitoringRecord as FlextTapOracleOicMonitoringRecord,
    )
    from ._oic_project import FlextTapOracleOicProject as FlextTapOracleOicProject
    from ._oic_resource_metadata import (
        FlextTapOracleOicResourceMetadata as FlextTapOracleOicResourceMetadata,
    )
    from ._package import OicPackageEntity as OicPackageEntity
    from ._stream_config import OicStreamConfiguration as OicStreamConfiguration
    from .streams import ALL_STREAMS as ALL_STREAMS
    from .streams import (
        FlextTapOracleOicModelsStreams as FlextTapOracleOicModelsStreams,
    )
    from .streams import th as th

_LAZY_MODULES: dict[str, tuple[str, ...]] = {
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
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES, alias_groups=_LAZY_ALIAS_GROUPS, sort_keys=False
)

_PUBLIC_EXPORTS: tuple[str, ...] = (
    "ALL_STREAMS",
    "FlextTapOracleOicConnection",
    "FlextTapOracleOicExecutionSummary",
    "FlextTapOracleOicIntegration",
    "FlextTapOracleOicLookup",
    "FlextTapOracleOicModelsStreams",
    "FlextTapOracleOicMonitoringRecord",
    "FlextTapOracleOicProject",
    "FlextTapOracleOicResourceMetadata",
    "OicActivityRecord",
    "OicAgentEntity",
    "OicApiResponse",
    "OicAuthenticationConfig",
    "OicConnectionEntity",
    "OicEnvelope",
    "OicErrorContext",
    "OicIntegrationEntity",
    "OicMetricsRecord",
    "OicPackageEntity",
    "OicStreamConfiguration",
    "require_entity_value",
    "th",
    "validate_entity_identity_and_port",
    "validate_optional_port",
)

__all__: tuple[str, ...] = tuple(_PUBLIC_EXPORTS)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
