"""Types for flext-tap-oracle-oic tests - uses composition with FlextTestsTypes.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_tests import FlextTestsTypes

from flext_tap_oracle_oic import t


class TestsFlextMeltanoTapOracleOicTypes(FlextTestsTypes):
    """Types for flext-tap-oracle-oic tests - uses composition with FlextTestsTypes.

    Architecture: Uses composition (not inheritance) with FlextTestsTypes and FlextMeltanoTapOracleOicTypes
    for flext-tap-oracle-oic-specific type definitions.

    Access patterns:
    - TestsFlextMeltanoTapOracleOicTypes.Tests.* = flext_tests test types (via composition)
    - TestsFlextMeltanoTapOracleOicTypes.TapOracleOic.* = flext-tap-oracle-oic-specific test types
    - TestsFlextMeltanoTapOracleOicTypes.* = FlextTestsTypes types (via composition)

    Rules:
    - Use composition, not inheritance (FlextTestsTypes deprecates subclassing)
    - flext-tap-oracle-oic-specific types go in TapOracleOic namespace
    - Generic types accessed via Tests namespace
    """

    # Composition: expose FlextTestsTypes
    Tests = FlextTestsTypes

    # TapOracleOic-specific test types namespace
    class TapOracleOic:
        """Tap Oracle OIC test types - domain-specific for Oracle OIC tap testing.

        Contains test types specific to Oracle OIC tap functionality including:
        - Test configuration types
        - Mock Oracle OIC data types
        - Test scenario types
        """

        # Test configuration literals
        type TestOracleOicBaseUrl = Literal[
            "https://test.oraclecloud.com",
            "https://staging.oraclecloud.com",
        ]
        type TestOracleOicUsername = Literal[
            "test_user", "REDACTED_LDAP_BIND_PASSWORD_user"
        ]
        type TestOracleOicMethod = Literal["GET", "POST", "PUT", "DELETE"]

        # Test data types
        type MockOracleOicRecord = dict[str, str | int | float | bool]
        type MockOracleOicResponse = dict[
            str,
            list[MockOracleOicRecord] | bool | str | None,
        ]
        type TestOracleOicScenario = dict[str, t.GeneralValueType]

        # Test result types
        type TestOracleOicValidationResult = dict[str, bool | str | list[str]]
        type TestOracleOicApiResult = dict[str, t.GeneralValueType]


# Alias for simplified usage
tt = TestsFlextMeltanoTapOracleOicTypes

__all__ = [
    "TestsFlextMeltanoTapOracleOicTypes",
    "tt",
]
