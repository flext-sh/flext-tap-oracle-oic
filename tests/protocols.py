"""Test protocol definitions for flext-tap-oracle-oic.

Provides TestsFlextTapOracleOicProtocols, combining FlextTestsProtocols with
FlextMeltanoTapOracleOicProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tap_oracle_oic.protocols import FlextMeltanoTapOracleOicProtocols
from flext_tests.protocols import FlextTestsProtocols


class TestsFlextTapOracleOicProtocols(
    FlextTestsProtocols,
    FlextMeltanoTapOracleOicProtocols,
):
    """Test protocols combining FlextTestsProtocols and FlextMeltanoTapOracleOicProtocols.

    Provides access to:
    - tp.Tests.Docker.* (from FlextTestsProtocols)
    - tp.Tests.Factory.* (from FlextTestsProtocols)
    - tp.TapOracleOic.* (from FlextMeltanoTapOracleOicProtocols)
    """

    class Tests:
        """Project-specific test protocols.

        Extends FlextTestsProtocols.Tests with TapOracleOic-specific protocols.
        """

        class TapOracleOic:
            """TapOracleOic-specific test protocols."""


# Runtime aliases
p = TestsFlextTapOracleOicProtocols
tp = TestsFlextTapOracleOicProtocols

__all__ = ["TestsFlextTapOracleOicProtocols", "p", "tp"]
