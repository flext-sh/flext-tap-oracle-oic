"""Domain layer for FLEXT-TAP-ORACLE-OIC v0.7.0.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

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

__all__: list[str] = [
    "OICConnection",
    "OICIntegration",
    "OICLookup",
    "OICMonitoringRecord",
    "OICProject",
    "OICResourceMetadata",
    "OICResourceType",
]
