"""Module skeleton for FlextTapOracleOicTestProtocols.

Test protocols for flext-tap-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_tap_oracle_oic import FlextTapOracleOicProtocols


class FlextTapOracleOicTestProtocols(FlextTestsProtocols, FlextTapOracleOicProtocols):
    """Test protocols for flext-tap-oracle-oic."""

    class TapOracleOic(FlextTapOracleOicProtocols.TapOracleOic):
        """TapOracleOic test protocols namespace."""

        class Tests:
            """Internal tests declarations."""


p = FlextTapOracleOicTestProtocols
__all__ = ["FlextTapOracleOicTestProtocols", "p"]
