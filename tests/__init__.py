# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if _t.TYPE_CHECKING:
    from flext_tests import td as td, tf as tf, tk as tk, tv as tv

    from flext_tap_oracle_oic import d as d, e as e, h as h, r as r, x as x
    from tests.base import (
        TestsFlextTapOracleOicServiceBase as TestsFlextTapOracleOicServiceBase,
        s as s,
    )
    from tests.constants import (
        TestsFlextTapOracleOicConstants as TestsFlextTapOracleOicConstants,
        c as c,
    )
    from tests.models import (
        TestsFlextTapOracleOicModels as TestsFlextTapOracleOicModels,
        m as m,
    )
    from tests.protocols import (
        TestsFlextTapOracleOicProtocols as TestsFlextTapOracleOicProtocols,
        p as p,
    )
    from tests.settings import (
        TestsFlextTapOracleOicSettings as TestsFlextTapOracleOicSettings,
    )
    from tests.typings import (
        TestsFlextTapOracleOicTypes as TestsFlextTapOracleOicTypes,
        t as t,
    )
    from tests.unit.test_auth import (
        TestsFlextTapOracleOicAuth as TestsFlextTapOracleOicAuth,
    )
    from tests.unit.test_tap import (
        TestsFlextTapOracleOicTap as TestsFlextTapOracleOicTap,
    )
    from tests.unit.test_tap_core import (
        TestsFlextTapOracleOicTapCore as TestsFlextTapOracleOicTapCore,
    )
    from tests.utilities import (
        TestsFlextTapOracleOicUtilities as TestsFlextTapOracleOicUtilities,
        u as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    (".unit",),
    build_lazy_import_map(
        {
            ".base": (
                "TestsFlextTapOracleOicServiceBase",
                "s",
            ),
            ".constants": (
                "TestsFlextTapOracleOicConstants",
                "c",
            ),
            ".models": (
                "TestsFlextTapOracleOicModels",
                "m",
            ),
            ".protocols": (
                "TestsFlextTapOracleOicProtocols",
                "p",
            ),
            ".settings": ("TestsFlextTapOracleOicSettings",),
            ".typings": (
                "TestsFlextTapOracleOicTypes",
                "t",
            ),
            ".unit.test_auth": ("TestsFlextTapOracleOicAuth",),
            ".unit.test_tap": ("TestsFlextTapOracleOicTap",),
            ".unit.test_tap_core": ("TestsFlextTapOracleOicTapCore",),
            ".utilities": (
                "TestsFlextTapOracleOicUtilities",
                "u",
            ),
            "flext_tap_oracle_oic": (
                "d",
                "e",
                "h",
                "r",
                "x",
            ),
            "flext_tests": (
                "td",
                "tf",
                "tk",
                "tv",
            ),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
        "pytest_addoption",
        "pytest_collect_file",
        "pytest_collection_modifyitems",
        "pytest_configure",
        "pytest_runtest_setup",
        "pytest_runtest_teardown",
        "pytest_sessionfinish",
        "pytest_sessionstart",
        "pytest_terminal_summary",
        "pytest_warning_recorded",
    ),
    module_name=__name__,
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "TestsFlextTapOracleOicAuth",
    "TestsFlextTapOracleOicConstants",
    "TestsFlextTapOracleOicModels",
    "TestsFlextTapOracleOicProtocols",
    "TestsFlextTapOracleOicServiceBase",
    "TestsFlextTapOracleOicSettings",
    "TestsFlextTapOracleOicTap",
    "TestsFlextTapOracleOicTapCore",
    "TestsFlextTapOracleOicTypes",
    "TestsFlextTapOracleOicUtilities",
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "td",
    "tf",
    "tk",
    "tv",
    "u",
    "x",
]
