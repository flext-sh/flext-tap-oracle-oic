"""Module skeleton for FlextTapOracleOicTestConstants.

Test constants for flext-tap-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsConstants

from flext_tap_oracle_oic import FlextTapOracleOicConstants


class FlextTapOracleOicTestConstants(FlextTestsConstants, FlextTapOracleOicConstants):
    """Test constants for flext-tap-oracle-oic."""


c = FlextTapOracleOicTestConstants
__all__ = ["FlextTapOracleOicTestConstants", "c"]
