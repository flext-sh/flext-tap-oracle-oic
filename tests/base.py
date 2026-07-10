"""Service base for flext-tap-oracle-oic tests."""

from __future__ import annotations

from typing import override

from flext_tests import s as tests_s

from flext_tap_oracle_oic import m
from tests.settings import TestsFlextTapOracleOicSettings


class TestsFlextTapOracleOicServiceBase(tests_s):
    """Tap Oracle OIC test service base with source and test settings namespaces."""

    @classmethod
    @override
    def fetch_settings(cls) -> TestsFlextTapOracleOicSettings:
        """Return the typed Tap Oracle OIC+Tests settings singleton."""

    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(settings_type=TestsFlextTapOracleOicSettings)


s = TestsFlextTapOracleOicServiceBase

__all__: list[str] = ["TestsFlextTapOracleOicServiceBase", "s"]
