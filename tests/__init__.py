# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if TYPE_CHECKING:
    from flext_tests import (
        d as d,
        e as e,
        h as h,
        r as r,
        td as td,
        tf as tf,
        tk as tk,
        tm as tm,
        tv as tv,
        x as x,
    )

    from flext_tap_oracle_oic.tests.base import (
        TestsFlextTapOracleOicServiceBase as TestsFlextTapOracleOicServiceBase,
        s as s,
    )
    from flext_tap_oracle_oic.tests.constants import (
        TestsFlextTapOracleOicConstants as TestsFlextTapOracleOicConstants,
        c as c,
    )
    from flext_tap_oracle_oic.tests.models import (
        TestsFlextTapOracleOicModels as TestsFlextTapOracleOicModels,
        m as m,
    )
    from flext_tap_oracle_oic.tests.protocols import (
        TestsFlextTapOracleOicProtocols as TestsFlextTapOracleOicProtocols,
        p as p,
    )
    from flext_tap_oracle_oic.tests.settings import (
        TestsFlextTapOracleOicSettings as TestsFlextTapOracleOicSettings,
    )
    from flext_tap_oracle_oic.tests.typings import (
        TestsFlextTapOracleOicTypes as TestsFlextTapOracleOicTypes,
        t as t,
    )
    from flext_tap_oracle_oic.tests.unit.test_auth import (
        TestsFlextTapOracleOicAuth as TestsFlextTapOracleOicAuth,
    )
    from flext_tap_oracle_oic.tests.unit.test_tap import (
        TestsFlextTapOracleOicTap as TestsFlextTapOracleOicTap,
    )
    from flext_tap_oracle_oic.tests.unit.test_tap_core import (
        TestsFlextTapOracleOicTapCore as TestsFlextTapOracleOicTapCore,
    )
    from flext_tap_oracle_oic.tests.utilities import (
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
            ".conftest": ("conftest",),
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
            ".unit": ("unit",),
            ".unit.test_auth": ("TestsFlextTapOracleOicAuth",),
            ".unit.test_tap": ("TestsFlextTapOracleOicTap",),
            ".unit.test_tap_core": ("TestsFlextTapOracleOicTapCore",),
            ".utilities": (
                "TestsFlextTapOracleOicUtilities",
                "u",
            ),
            "flext_tests": (
                "d",
                "e",
                "h",
                "r",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "x",
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


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
