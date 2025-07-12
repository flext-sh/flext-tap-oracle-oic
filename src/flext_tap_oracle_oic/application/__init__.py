"""Application layer for FLEXT-TAP-ORACLE-OIC v0.7.0.

REFACTORED:
            Using flext-core application patterns - NO duplication.
"""

from flext_tap_oracle_oic.application.services import (
    OICConnectionService,
    OICIntegrationService,
    OICLookupService,
    OICMonitoringService,
    OICProjectService,
)

__all__ = [
    "OICConnectionService",
    "OICIntegrationService",
    "OICLookupService",
    "OICMonitoringService",
    "OICProjectService",
]
