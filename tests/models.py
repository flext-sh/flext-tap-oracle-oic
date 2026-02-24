"""Test models for flext-tap-oracle-oic tests.

Provides TestsFlextTapOracleOicModels, extending FlextTestsModels with
flext-tap-oracle-oic-specific models using COMPOSITION INHERITANCE.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tap_oracle_oic.models import FlextMeltanoTapOracleOicModels
from flext_tests.models import FlextTestsModels


class TestsFlextTapOracleOicModels(FlextTestsModels, FlextMeltanoTapOracleOicModels):
    """Models for flext-tap-oracle-oic tests using COMPOSITION INHERITANCE.

    MANDATORY: Inherits from BOTH:
    1. FlextTestsModels - for test infrastructure (.Tests.*)
    2. FlextMeltanoTapOracleOicModels - for domain models

    Access patterns:
    - tm.Tests.* (generic test models from FlextTestsModels)
    - tm.* (Tap Oracle OIC domain models)
    - m.* (production models via alternative alias)
    """

    class Tests:
        """Project-specific test fixtures namespace."""

        class TapOracleOic:
            """Tap Oracle OIC-specific test fixtures."""


# Short aliases per FLEXT convention
tm = TestsFlextTapOracleOicModels
m = TestsFlextTapOracleOicModels

__all__ = [
    "TestsFlextTapOracleOicModels",
    "m",
    "tm",
]
