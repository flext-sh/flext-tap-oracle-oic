"""Domain entities for FLEXT-TAP-ORACLE-OIC — re-exported from models.py.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

MRO policy: all FlextModels subclasses live under FlextTapOracleOicModels.OracleOic.
This module re-exports them for backwards compatibility with existing callers.

"""

from __future__ import annotations

from flext_tap_oracle_oic import t
from flext_tap_oracle_oic.constants import c
from flext_tap_oracle_oic.models import FlextTapOracleOicModels as _m

OICResourceType = c.OICResourceType
IntegrationStatus = c.IntegrationStatus
ConnectionStatus = c.ConnectionStatus

OICConnection = _m.OracleOic.OICConnection
OICIntegration = _m.OracleOic.OICIntegration
OICLookup = _m.OracleOic.OICLookup
OICMonitoringRecord = _m.OracleOic.OICMonitoringRecord
OICProject = _m.OracleOic.OICProject
OICResourceMetadata = _m.OracleOic.OICResourceMetadata
OICExecutionSummary = _m.OracleOic.OICExecutionSummary

__all__: t.StrSequence = [
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
