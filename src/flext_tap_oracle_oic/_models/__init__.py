# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Oracle Oic. Models package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from ._activity import FlextTapOracleOicActivityRecord
    from ._agent import FlextTapOracleOicAgentEntity
    from ._api_response import FlextTapOracleOicApiResponse
    from ._auth_config import FlextTapOracleOicAuthenticationConfig
    from ._connection import FlextTapOracleOicConnectionEntity
    from ._envelope import FlextTapOracleOicEnvelope
    from ._error_context import FlextTapOracleOicErrorContext
    from ._helpers import (
        require_entity_value,
        validate_entity_identity_and_port,
        validate_optional_port,
    )
    from ._integration import FlextTapOracleOicIntegrationEntity
    from ._metrics import FlextTapOracleOicMetricsRecord
    from ._oic_connection import FlextTapOracleOicConnection
    from ._oic_execution_summary import FlextTapOracleOicExecutionSummary
    from ._oic_integration import FlextTapOracleOicIntegration
    from ._oic_lookup import FlextTapOracleOicLookup
    from ._oic_monitoring import FlextTapOracleOicMonitoringRecord
    from ._oic_project import FlextTapOracleOicProject
    from ._oic_resource_metadata import FlextTapOracleOicResourceMetadata
    from ._package import FlextTapOracleOicPackageEntity
    from ._stream_config import FlextTapOracleOicStreamConfiguration
    from .streams import ALL_STREAMS, FlextTapOracleOicModelsStreams


__all__: tuple[str, ...] = (
    "ALL_STREAMS",
    "FlextTapOracleOicActivityRecord",
    "FlextTapOracleOicAgentEntity",
    "FlextTapOracleOicApiResponse",
    "FlextTapOracleOicAuthenticationConfig",
    "FlextTapOracleOicConnection",
    "FlextTapOracleOicConnectionEntity",
    "FlextTapOracleOicEnvelope",
    "FlextTapOracleOicErrorContext",
    "FlextTapOracleOicExecutionSummary",
    "FlextTapOracleOicIntegration",
    "FlextTapOracleOicIntegrationEntity",
    "FlextTapOracleOicLookup",
    "FlextTapOracleOicMetricsRecord",
    "FlextTapOracleOicModelsStreams",
    "FlextTapOracleOicMonitoringRecord",
    "FlextTapOracleOicPackageEntity",
    "FlextTapOracleOicProject",
    "FlextTapOracleOicResourceMetadata",
    "FlextTapOracleOicStreamConfiguration",
    "require_entity_value",
    "validate_entity_identity_and_port",
    "validate_optional_port",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            "._activity": ("FlextTapOracleOicActivityRecord",),
            "._agent": ("FlextTapOracleOicAgentEntity",),
            "._api_response": ("FlextTapOracleOicApiResponse",),
            "._auth_config": ("FlextTapOracleOicAuthenticationConfig",),
            "._connection": ("FlextTapOracleOicConnectionEntity",),
            "._envelope": ("FlextTapOracleOicEnvelope",),
            "._error_context": ("FlextTapOracleOicErrorContext",),
            "._helpers": (
                "require_entity_value",
                "validate_entity_identity_and_port",
                "validate_optional_port",
            ),
            "._integration": ("FlextTapOracleOicIntegrationEntity",),
            "._metrics": ("FlextTapOracleOicMetricsRecord",),
            "._oic_connection": ("FlextTapOracleOicConnection",),
            "._oic_execution_summary": ("FlextTapOracleOicExecutionSummary",),
            "._oic_integration": ("FlextTapOracleOicIntegration",),
            "._oic_lookup": ("FlextTapOracleOicLookup",),
            "._oic_monitoring": ("FlextTapOracleOicMonitoringRecord",),
            "._oic_project": ("FlextTapOracleOicProject",),
            "._oic_resource_metadata": ("FlextTapOracleOicResourceMetadata",),
            "._package": ("FlextTapOracleOicPackageEntity",),
            "._stream_config": ("FlextTapOracleOicStreamConfiguration",),
            ".streams": ("ALL_STREAMS", "FlextTapOracleOicModelsStreams"),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
