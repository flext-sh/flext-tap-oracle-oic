"""Domain layer for FLEXT-TAP-ORACLE-OIC v0.7.0.

REFACTORED:
            Domain entities and value objects.
"""

from __future__ import annotations

from flext_tap_oracle_oic.domain.entities import (
    OICConnection,
    OICIntegration,
    OICLookup,
    OICMonitoringRecord,
    OICProject,
    OICResourceMetadata,
    OICResourceType,
)

__all__ = [
    "OICConnection",
    "OICIntegration",
    "OICLookup",
    "OICMonitoringRecord",
    "OICProject",
    "OICResourceMetadata",
    "OICResourceType",
]
