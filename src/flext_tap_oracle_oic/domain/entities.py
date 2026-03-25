"""Domain entities for FLEXT-TAP-ORACLE-OIC — re-exported from models.py.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

MRO policy: all FlextModels subclasses live under FlextTapOracleOicModels.OracleOic.
Use m.OracleOic.* directly from flext_tap_oracle_oic.models.
"""

from __future__ import annotations

from flext_tap_oracle_oic.constants import FlextTapOracleOicConstants as _c
from flext_tap_oracle_oic.models import FlextTapOracleOicModels as _m

ConnectionStatus = _c.TapOracleOic.ConnectionStatus
IntegrationStatus = _c.TapOracleOic.IntegrationStatus
OICConnection = _m.TapOracleOic.OracleOic.OICConnection
OICExecutionSummary = _m.TapOracleOic.OracleOic.OICExecutionSummary
OICIntegration = _m.TapOracleOic.OracleOic.OICIntegration
OICLookup = _m.TapOracleOic.OracleOic.OICLookup
OICMonitoringRecord = _m.TapOracleOic.OracleOic.OICMonitoringRecord
OICProject = _m.TapOracleOic.OracleOic.OICProject
OICResourceMetadata = _m.TapOracleOic.OracleOic.OICResourceMetadata
OICResourceType = _c.TapOracleOic.OICResourceType

__all__: list[str] = [
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
