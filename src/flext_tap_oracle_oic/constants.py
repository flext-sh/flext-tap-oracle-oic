"""FLEXT Oracle OIC TAP Constants extending flext-core platform constants.

FLEXT Oracle OIC TAP specific constants that extend flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_meltano import FlextMeltanoConstants
from flext_oracle_oic import FlextOracleOicConstants

from flext_tap_oracle_oic._constants import (
    FlextTapOracleOicConstantsBase,
    FlextTapOracleOicConstantsValues,
)
from flext_tap_oracle_oic._constants.enums import FlextTapOracleOicConstantsEnums


class FlextTapOracleOicConstants(FlextMeltanoConstants, FlextOracleOicConstants):
    """FLEXT Oracle OIC TAP constants extending flext-core platform constants.

    Composes with FlextOracleOicConstants to avoid duplication and ensure consistency.
    Scalar constants inherit from ``FlextTapOracleOicConstantsValues`` (the
    ``_constants`` SSOT); this class declares only the domain enums.

    """

    class TapOracleOic(
        FlextTapOracleOicConstantsValues.TapOracleOic,
        FlextTapOracleOicConstantsValues,
        FlextTapOracleOicConstantsBase,
    ):
        """OIC connection configuration and domain enumerations."""

        OicIntegrationStatus = FlextTapOracleOicConstantsEnums.OicIntegrationStatus
        OicJobStatus = FlextTapOracleOicConstantsEnums.OicJobStatus
        OicIntegrationType = FlextTapOracleOicConstantsEnums.OicIntegrationType
        OicAgentType = FlextTapOracleOicConstantsEnums.OicAgentType
        OicAgentStatus = FlextTapOracleOicConstantsEnums.OicAgentStatus
        OicHealthStatus = FlextTapOracleOicConstantsEnums.OicHealthStatus
        OicErrorSeverity = FlextTapOracleOicConstantsEnums.OicErrorSeverity
        OicConnectionTestStatus = (
            FlextTapOracleOicConstantsEnums.OicConnectionTestStatus
        )
        OicReplicationMethod = FlextTapOracleOicConstantsEnums.OicReplicationMethod
        OICResourceType = FlextTapOracleOicConstantsEnums.OICResourceType
        IntegrationStatus = FlextTapOracleOicConstantsEnums.IntegrationStatus
        ConnectionStatus = FlextTapOracleOicConstantsEnums.ConnectionStatus
        OicErrorType = FlextTapOracleOicConstantsEnums.OicErrorType


c = FlextTapOracleOicConstants

__all__: tuple[str, ...] = ("FlextTapOracleOicConstants", "c")
