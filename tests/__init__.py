# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import api, d, e, h, r, td, tf, tk, tm, tv, x

    from . import unit
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
    "TestsFlextTapOracleOicConstants",
    "TestsFlextTapOracleOicModels",
    "TestsFlextTapOracleOicProtocols",
    "TestsFlextTapOracleOicServiceBase",
    "TestsFlextTapOracleOicSettings",
    "TestsFlextTapOracleOicTypes",
    "TestsFlextTapOracleOicUtilities",
    "api",
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
            "flext_tests": (
                "api",
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
