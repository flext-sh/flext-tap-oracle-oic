"""Observable behavior of the public Oracle OIC tap validation utilities.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tests import tm

from flext_tap_oracle_oic import c
from tests import u


class TestsFlextTapOracleOicUtilities:
    """Endpoint and stream-configuration validation contracts."""

    @staticmethod
    def test_validate_oic_endpoint_accepts_oic_host() -> None:
        """Test validate oic endpoint accepts oic host."""
        endpoint = "https://tenant.integration.oic.example.com"
        tm.ok(u.TapOracleOic.validate_oic_endpoint(endpoint), eq=endpoint)

    @staticmethod
    def test_validate_oic_endpoint_rejects_empty_and_foreign_hosts() -> None:
        """Test validate oic endpoint rejects empty and foreign hosts."""
        tm.fail(u.TapOracleOic.validate_oic_endpoint(""))
        tm.fail(u.TapOracleOic.validate_oic_endpoint("not-a-url"))
        tm.fail(u.TapOracleOic.validate_oic_endpoint("https://example.com"))

    @staticmethod
    def test_validate_stream_config_accepts_page_size_within_bound() -> None:
        """Test validate stream config accepts page size within bound."""
        tm.ok(
            u.TapOracleOic.validate_stream_config({
                "streams": {
                    "integrations": {"selected": True, "page_size": c.MAX_PAGE_SIZE},
                },
            }),
        )

    @staticmethod
    def test_validate_stream_config_rejects_invalid_streams() -> None:
        """Test validate stream config rejects invalid streams."""
        tm.fail(u.TapOracleOic.validate_stream_config({}))
        tm.fail(
            u.TapOracleOic.validate_stream_config({
                "streams": {"integrations": {"page_size": 1}},
            }),
        )
        tm.fail(
            u.TapOracleOic.validate_stream_config({
                "streams": {
                    "integrations": {
                        "selected": True,
                        "page_size": c.MAX_PAGE_SIZE + 1,
                    },
                },
            }),
        )
