"""Service base for flext-tap-oracle-oic tests."""

from __future__ import annotations

from typing import override

from flext_tests import s as tests_s

from flext_tap_oracle_oic import m
from tests.settings import TestsFlextTapOracleOicSettings


class TestsFlextTapOracleOicServiceBase(tests_s):
    """Tap Oracle OIC test service base with source and test settings namespaces."""

    # NOTE (multi-agent): flext-tests owns fetch_settings; this project
    # declares only its more-specific bootstrap settings type.
    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> p.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(settings_type=TestsFlextTapOracleOicSettings)


s = TestsFlextTapOracleOicServiceBase

__all__: list[str] = ["TestsFlextTapOracleOicServiceBase", "s"]
