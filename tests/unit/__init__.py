# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_oracle_oic.tests.unit.test_auth import (
        TestsFlextTapOracleOicAuth as TestsFlextTapOracleOicAuth,
    )
    from flext_tap_oracle_oic.tests.unit.test_tap import (
        TestsFlextTapOracleOicTap as TestsFlextTapOracleOicTap,
    )
    from flext_tap_oracle_oic.tests.unit.test_tap_core import (
        TestsFlextTapOracleOicTapCore as TestsFlextTapOracleOicTapCore,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_auth": ("TestsFlextTapOracleOicAuth",),
        ".test_tap": ("TestsFlextTapOracleOicTap",),
        ".test_tap_core": ("TestsFlextTapOracleOicTapCore",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
