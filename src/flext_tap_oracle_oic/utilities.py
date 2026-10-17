# AUTO-GENERATED FILE — Regenerate with: make gen
"""Singer tap utilities for Oracle OIC (Oracle Integration Cloud) operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_meltano import FlextMeltanoUtilities
from flext_oracle_oic import FlextOracleOicUtilities

from flext_tap_oracle_oic._utilities import FlextTapOracleOicUtilitiesValidation


class FlextTapOracleOicUtilities(FlextOracleOicUtilities, FlextMeltanoUtilities):
    """Single unified utilities class for Singer tap Oracle OIC operations.

    Follows FLEXT unified class pattern with nested helper classes for
    domain-specific Singer tap functionality with Oracle Integration Cloud.

    """

    class TapOracleOic(FlextTapOracleOicUtilitiesValidation):
        """Tap Oracle OIC-specific utility namespace."""


u = FlextTapOracleOicUtilities

__all__: list[str] = ["FlextTapOracleOicUtilities", "u"]
