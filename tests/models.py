"""Module skeleton for TestsFlextTapOracleOicModels.

Test models for flext-tap-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from tests import FlextTapOracleOicModels


class TestsFlextTapOracleOicModels(FlextTestsModels, FlextTapOracleOicModels):
    """Test models for flext-tap-oracle-oic."""

    class Tests(FlextTestsModels.Tests):
        """Internal tests declarations."""


m = TestsFlextTapOracleOicModels

__all__: list[str] = ["TestsFlextTapOracleOicModels", "m"]
