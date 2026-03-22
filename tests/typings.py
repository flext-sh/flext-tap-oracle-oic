"""Module skeleton for FlextTapOracleOicTestTypes.

Test type aliases for flext-tap-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_tap_oracle_oic import FlextTapOracleOicTypes


class FlextTapOracleOicTestTypes(FlextTestsTypes, FlextTapOracleOicTypes):
    """Test type aliases for flext-tap-oracle-oic."""

    class TapOracleOic(FlextTapOracleOicTypes.TapOracleOic):
        """TapOracleOic test types namespace."""

        class Tests:
            """Internal tests declarations."""


t = FlextTapOracleOicTestTypes
__all__ = ["FlextTapOracleOicTestTypes", "t"]
