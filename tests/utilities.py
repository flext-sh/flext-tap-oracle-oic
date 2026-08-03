"""Module skeleton for TestsFlextTapOracleOicUtilities.

Test utilities for flext-tap-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tap_oracle_oic import FlextTapOracleOicUtilities
from flext_tests import FlextTestsUtilities


class TestsFlextTapOracleOicUtilities(FlextTestsUtilities, FlextTapOracleOicUtilities):
    """Test utilities for flext-tap-oracle-oic."""

    class TapOracleOic(FlextTapOracleOicUtilities.TapOracleOic):
        """TapOracleOic test utilities namespace."""

        class Tests:
            """Internal tests declarations."""


u = TestsFlextTapOracleOicUtilities
__all__: list[str] = ["TestsFlextTapOracleOicUtilities", "u"]
