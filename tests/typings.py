"""Test types for flext-tap-oracle-oic — MRO composition with test infrastructure.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_tap_oracle_oic import FlextTapOracleOicTypes


class TestsFlextTapOracleOicTypes(FlextTestsTypes, FlextTapOracleOicTypes):
    """Test type aliases for flext-tap-oracle-oic."""


t = TestsFlextTapOracleOicTypes
__all__ = ["TestsFlextTapOracleOicTypes", "t"]
