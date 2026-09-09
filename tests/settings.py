"""Runtime settings for flext-tap-oracle-oic tests."""

from __future__ import annotations

from flext_tests import FlextTestsSettings

from flext_tap_oracle_oic import FlextTapOracleOicSettings


class TestsFlextTapOracleOicSettings(FlextTapOracleOicSettings, FlextTestsSettings):
    """Tap Oracle OIC settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextTapOracleOicSettings"]
