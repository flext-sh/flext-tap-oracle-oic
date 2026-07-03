"""Module skeleton for TestsFlextTapOracleOicProtocols.

Test protocols for flext-tap-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_tap_oracle_oic import FlextTapOracleOicProtocols


class TestsFlextTapOracleOicProtocols(FlextTestsProtocols, FlextTapOracleOicProtocols):
    """Test protocols for flext-tap-oracle-oic."""


p = TestsFlextTapOracleOicProtocols
__all__: list[str] = ["TestsFlextTapOracleOicProtocols", "p"]
