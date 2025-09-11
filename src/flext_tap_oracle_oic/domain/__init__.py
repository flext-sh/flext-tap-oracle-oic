"""Domain layer for FLEXT-TAP-ORACLE-OIC v0.7.0.

REFACTORED:
          Domain entities and value objects.


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextTypes

"""
Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""


from flext_tap_oracle_oic.domain.entities import (
    OICConnection,
    OICIntegration,
    OICLookup,
    OICMonitoringRecord,
    OICProject,
    OICResourceMetadata,
    OICResourceType,
)

__all__: FlextTypes.Core.StringList = [
    "OICConnection",
    "OICIntegration",
    "OICLookup",
    "OICMonitoringRecord",
    "OICProject",
    "OICResourceMetadata",
    "OICResourceType",
]
