"""Module skeleton for TestsFlextTapOracleOicModels.

Test models for flext-tap-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_tap_oracle_oic import FlextTapOracleOicModels


class TestsFlextTapOracleOicModels(FlextTestsModels, FlextTapOracleOicModels):
    """Test models for flext-tap-oracle-oic."""

    class TapOracleOic(FlextTapOracleOicModels.TapOracleOic):
        """TapOracleOic domain models extending project models."""

        class Tests:
            """Internal tests declarations."""


m = TestsFlextTapOracleOicModels

__all__: list[str] = ["TestsFlextTapOracleOicModels", "m"]
