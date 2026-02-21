"""Utilities for flext-tap-oracle-oic tests - uses composition with FlextTestsUtilities.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tap_oracle_oic import t
from flext_tests import FlextTestsUtilities


class TestsFlextMeltanoTapOracleOicUtilities(FlextTestsUtilities):
    """Utilities for flext-tap-oracle-oic tests - uses composition with FlextTestsUtilities.

    Architecture: Uses composition (not inheritance) with FlextTestsUtilities and FlextMeltanoTapOracleOicUtilities
    for flext-tap-oracle-oic-specific utility definitions.

    Access patterns:
    - TestsFlextMeltanoTapOracleOicUtilities.Tests.* = flext_tests test utilities (via composition)
    - TestsFlextMeltanoTapOracleOicUtilities.TapOracleOic.* = flext-tap-oracle-oic-specific test utilities
    - TestsFlextMeltanoTapOracleOicUtilities.* = FlextTestsUtilities methods (via composition)

    Rules:
    - Use composition, not inheritance (FlextTestsUtilities deprecates subclassing)
    - flext-tap-oracle-oic-specific utilities go in TapOracleOic namespace
    - Generic utilities accessed via Tests namespace
    """

    # Composition: expose FlextTestsUtilities namespaces
    Tests = FlextTestsUtilities.Tests

    # TapOracleOic-specific test utilities namespace
    class TapOracleOic:
        """Tap Oracle OIC test utilities - domain-specific for Oracle OIC tap testing.

        Contains test utilities specific to Oracle OIC tap functionality including:
        - Oracle OIC connection test helpers
        - Oracle OIC API test helpers
        - Oracle OIC data generation helpers
        """

        @staticmethod
        def create_test_oracle_oic_config(
            base_url: str = "https://test.oraclecloud.com",
            username: str = "test_user",
            password: str = "test_pass",
            client_id: str | None = None,
            **kwargs: t.GeneralValueType,
        ) -> dict[str, t.GeneralValueType]:
            """Create test Oracle OIC configuration."""
            config = {
                "base_url": base_url,
                "username": username,
                "password": password,
            }
            if client_id:
                config["client_id"] = client_id
            config.update(kwargs)
            return config

        @staticmethod
        def create_test_oracle_oic_api_response(
            data: list[dict[str, t.GeneralValueType]],
            *,
            has_more: bool = False,
            next_page_url: str | None = None,
            **kwargs: t.GeneralValueType,
        ) -> dict[str, t.GeneralValueType]:
            """Create test Oracle OIC API response."""
            response = {
                "items": data,
                "hasMore": has_more,
            }
            if next_page_url:
                response["nextPageUrl"] = next_page_url
            response.update(kwargs)
            return response

        @staticmethod
        def generate_mock_oracle_oic_records(
            count: int = 5,
            base_id: int = 1000,
            **kwargs: t.GeneralValueType,
        ) -> list[dict[str, t.GeneralValueType]]:
            """Generate mock Oracle OIC records for testing."""
            records = []
            for i in range(count):
                record = {
                    "id": base_id + i,
                    "name": f"Test Record {i + 1}",
                    "created_date": "2023-01-01T00:00:00Z",
                    "modified_date": "2023-01-01T00:00:00Z",
                }
                # Add custom fields
                record.update(dict(kwargs.items()))
                records.append(record)
            return records

        @staticmethod
        def validate_oracle_oic_config(config: dict[str, t.GeneralValueType]) -> bool:
            """Validate Oracle OIC configuration for testing."""
            required_fields = ["base_url", "username"]
            return all(field in config and config[field] for field in required_fields)


# Alias for simplified usage
tu = TestsFlextMeltanoTapOracleOicUtilities

__all__ = [
    "TestsFlextMeltanoTapOracleOicUtilities",
    "tu",
]
