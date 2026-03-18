# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Domain layer for FLEXT-TAP-ORACLE-OIC v0.7.0.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

    from flext_tap_oracle_oic.domain.entities import (
        ConnectionStatus,
        IntegrationStatus,
        OICConnection,
        OICExecutionSummary,
        OICIntegration,
        OICLookup,
        OICMonitoringRecord,
        OICProject,
        OICResourceMetadata,
        OICResourceType,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "ConnectionStatus": ("flext_tap_oracle_oic.domain.entities", "ConnectionStatus"),
    "IntegrationStatus": ("flext_tap_oracle_oic.domain.entities", "IntegrationStatus"),
    "OICConnection": ("flext_tap_oracle_oic.domain.entities", "OICConnection"),
    "OICExecutionSummary": ("flext_tap_oracle_oic.domain.entities", "OICExecutionSummary"),
    "OICIntegration": ("flext_tap_oracle_oic.domain.entities", "OICIntegration"),
    "OICLookup": ("flext_tap_oracle_oic.domain.entities", "OICLookup"),
    "OICMonitoringRecord": ("flext_tap_oracle_oic.domain.entities", "OICMonitoringRecord"),
    "OICProject": ("flext_tap_oracle_oic.domain.entities", "OICProject"),
    "OICResourceMetadata": ("flext_tap_oracle_oic.domain.entities", "OICResourceMetadata"),
    "OICResourceType": ("flext_tap_oracle_oic.domain.entities", "OICResourceType"),
}

__all__ = [
    "ConnectionStatus",
    "IntegrationStatus",
    "OICConnection",
    "OICExecutionSummary",
    "OICIntegration",
    "OICLookup",
    "OICMonitoringRecord",
    "OICProject",
    "OICResourceMetadata",
    "OICResourceType",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
