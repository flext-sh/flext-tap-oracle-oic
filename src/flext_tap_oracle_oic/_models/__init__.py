# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Oracle Oic. Models package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from ._activity import OicActivityRecord
    from ._agent import OicAgentEntity
    from ._api_response import OicApiResponse
    from ._auth_config import OicAuthenticationConfig
    from ._connection import OicConnectionEntity
    from ._envelope import OicEnvelope
    from ._error_context import OicErrorContext
    from ._helpers import (
        require_entity_value,
        validate_entity_identity_and_port,
        validate_optional_port,
    )
    from ._integration import OicIntegrationEntity
    from ._metrics import OicMetricsRecord
    from ._oic_connection import FlextTapOracleOicConnection
    from ._oic_execution_summary import FlextTapOracleOicExecutionSummary
    from ._oic_integration import FlextTapOracleOicIntegration
    from ._oic_lookup import FlextTapOracleOicLookup
    from ._oic_monitoring import FlextTapOracleOicMonitoringRecord
    from ._oic_project import FlextTapOracleOicProject
    from ._oic_resource_metadata import FlextTapOracleOicResourceMetadata
    from ._package import OicPackageEntity
    from ._stream_config import OicStreamConfiguration
    from .streams import ALL_STREAMS, FlextTapOracleOicModelsStreams, th
__all__: tuple[str, ...] = (
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

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
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
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
