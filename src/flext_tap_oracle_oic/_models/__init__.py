# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Oracle Oic. Models package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

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
    from flext_tap_oracle_oic._models._tap_oracle_oic_namespace import (
        FlextTapOracleOicModelsTapOracleOicNamespace,
    )
    from flext_tap_oracle_oic._models.streams import (
        FlextTapOracleOicFlextModelsStreams,
        FlextTapOracleOicModelsStreams,
    )


__all__: tuple[str, ...] = (
    "FlextTapOracleOicActivityRecord",
    "FlextTapOracleOicAgentEntity",
    "FlextTapOracleOicApiResponse",
    "FlextTapOracleOicAuthenticationConfig",
    "FlextTapOracleOicConnection",
    "FlextTapOracleOicConnectionEntity",
    "FlextTapOracleOicEnvelope",
    "FlextTapOracleOicErrorContext",
    "FlextTapOracleOicExecutionSummary",
    "FlextTapOracleOicFlextModelsStreams",
    "FlextTapOracleOicIntegration",
    "FlextTapOracleOicIntegrationEntity",
    "FlextTapOracleOicLookup",
    "FlextTapOracleOicMetricsRecord",
    "FlextTapOracleOicModelsHelpers",
    "FlextTapOracleOicModelsStreams",
    "FlextTapOracleOicModelsTapOracleOicNamespace",
    "FlextTapOracleOicMonitoringRecord",
    "FlextTapOracleOicPackageEntity",
    "FlextTapOracleOicProject",
    "FlextTapOracleOicResourceMetadata",
    "FlextTapOracleOicStreamConfiguration",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextTapOracleOicActivityRecord": "._activity",
        "FlextTapOracleOicAgentEntity": "._agent",
        "FlextTapOracleOicApiResponse": "._api_response",
        "FlextTapOracleOicAuthenticationConfig": "._auth_config",
        "FlextTapOracleOicConnection": "._oic_connection",
        "FlextTapOracleOicConnectionEntity": "._connection",
        "FlextTapOracleOicEnvelope": "._envelope",
        "FlextTapOracleOicErrorContext": "._error_context",
        "FlextTapOracleOicExecutionSummary": "._oic_execution_summary",
        "FlextTapOracleOicFlextModelsStreams": ".streams",
        "FlextTapOracleOicIntegration": "._oic_integration",
        "FlextTapOracleOicIntegrationEntity": "._integration",
        "FlextTapOracleOicLookup": "._oic_lookup",
        "FlextTapOracleOicMetricsRecord": "._metrics",
        "FlextTapOracleOicModelsHelpers": "._helpers",
        "FlextTapOracleOicModelsStreams": ".streams",
        "FlextTapOracleOicModelsTapOracleOicNamespace": "._tap_oracle_oic_namespace",
        "FlextTapOracleOicMonitoringRecord": "._oic_monitoring",
        "FlextTapOracleOicPackageEntity": "._package",
        "FlextTapOracleOicProject": "._oic_project",
        "FlextTapOracleOicResourceMetadata": "._oic_resource_metadata",
        "FlextTapOracleOicStreamConfiguration": "._stream_config",
    }),
    public_exports=__all__,
)
