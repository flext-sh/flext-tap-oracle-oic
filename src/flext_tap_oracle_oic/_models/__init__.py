# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Oracle Oic. Models package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_oracle_oic._models._activity import FlextTapOracleOicActivityRecord
    from flext_tap_oracle_oic._models._agent import FlextTapOracleOicAgentEntity
    from flext_tap_oracle_oic._models._api_response import FlextTapOracleOicApiResponse
    from flext_tap_oracle_oic._models._auth_config import (
        FlextTapOracleOicAuthenticationConfig,
    )
    from flext_tap_oracle_oic._models._connection import (
        FlextTapOracleOicConnectionEntity,
    )
    from flext_tap_oracle_oic._models._envelope import FlextTapOracleOicEnvelope
    from flext_tap_oracle_oic._models._error_context import (
        FlextTapOracleOicErrorContext,
    )
    from flext_tap_oracle_oic._models._helpers import FlextTapOracleOicModelsHelpers
    from flext_tap_oracle_oic._models._integration import (
        FlextTapOracleOicIntegrationEntity,
    )
    from flext_tap_oracle_oic._models._metrics import FlextTapOracleOicMetricsRecord
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
    from flext_tap_oracle_oic._models._package import FlextTapOracleOicPackageEntity
    from flext_tap_oracle_oic._models._stream_config import (
        FlextTapOracleOicStreamConfiguration,
    )
    from flext_tap_oracle_oic._models.streams import (
        ALL_STREAMS,
        FlextTapOracleOicModelsStreams,
    )


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
    "FlextTapOracleOicModelsHelpers",
    "FlextTapOracleOicModelsStreams",
    "FlextTapOracleOicMonitoringRecord",
    "FlextTapOracleOicPackageEntity",
    "FlextTapOracleOicProject",
    "FlextTapOracleOicResourceMetadata",
    "FlextTapOracleOicStreamConfiguration",
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
            "._helpers": ("FlextTapOracleOicModelsHelpers",),
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
    ),
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
