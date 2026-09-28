# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from . import unit as unit
    from flext_tap_oracle_oic import FlextTapOracleOicConstants
    from flext_tests import FlextTestsConstants, d, e, h, r, td, tf, tk, tm, tv, x

    from .base import (
        TestsFlextTapOracleOicServiceBase,
        TestsFlextTapOracleOicServiceBase as s,
    )
    from .constants import (
        TestsFlextTapOracleOicConstants,
        TestsFlextTapOracleOicConstants as c,
    )
    from .models import TestsFlextTapOracleOicModels, TestsFlextTapOracleOicModels as m
    from .protocols import (
        TestsFlextTapOracleOicProtocols,
        TestsFlextTapOracleOicProtocols as p,
    )
    from .settings import TestsFlextTapOracleOicSettings
    from .typings import TestsFlextTapOracleOicTypes, TestsFlextTapOracleOicTypes as t
    from .utilities import (
        TestsFlextTapOracleOicUtilities,
        TestsFlextTapOracleOicUtilities as u,
    )
__all__: tuple[str, ...] = (
    "FlextTapOracleOicConstants",
    "FlextTestsConstants",
    "TestsFlextTapOracleOicConstants",
    "TestsFlextTapOracleOicModels",
    "TestsFlextTapOracleOicProtocols",
    "TestsFlextTapOracleOicServiceBase",
    "TestsFlextTapOracleOicSettings",
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
    "tm",
    "tv",
    "u",
    "unit",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("TestsFlextTapOracleOicServiceBase", "s"),
            ".constants": ("TestsFlextTapOracleOicConstants", "c"),
            ".models": ("TestsFlextTapOracleOicModels", "m"),
            ".protocols": ("TestsFlextTapOracleOicProtocols", "p"),
            ".settings": ("TestsFlextTapOracleOicSettings",),
            ".typings": ("TestsFlextTapOracleOicTypes", "t"),
            ".unit": ("unit",),
            ".utilities": ("TestsFlextTapOracleOicUtilities", "u"),
            "flext_tap_oracle_oic": ("FlextTapOracleOicConstants",),
            "flext_tests": (
                "FlextTestsConstants",
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
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
