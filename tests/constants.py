"""Module skeleton for TestsFlextTapOracleOic.

Test constants for flext-tap-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsConstants

from flext_tap_oracle_oic import FlextTapOracleOicConstants


class TestsFlextTapOracleOicConstants(
    FlextTestsConstants,
    FlextTapOracleOicConstants,
):
    """Test constants for flext-tap-oracle-oic."""


c = TestsFlextTapOracleOicConstants
__all__: list[str] = ["TestsFlextTapOracleOicConstants", "c"]
