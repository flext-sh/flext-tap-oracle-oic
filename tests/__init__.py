# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_auth import auth
    from flext_cli import cli
    from flext_infra import docs_main, infra
    from flext_meltano import meltano
    from flext_oracle_oic import oracle_oic
    from flext_tests import (
        active_rules,
        api,
        config,
        discover_repository_root,
        install_local_packages,
        load_infra_report,
        settings,
        split_csv,
        td,
        tf,
        tk,
        tm,
        tv,
    )
    from flext_web import web
    from pydantic_core import from_json, to_json, to_jsonable_python

    from flext_core import core, d, e, h, lazy_attribute, r, x
    from flext_tap_oracle_oic import main, tap_oracle_oic

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
    "active_rules",
    "api",
    "auth",
    "c",
    "cli",
    "config",
    "core",
    "d",
    "discover_repository_root",
    "docs_main",
    "e",
    "from_json",
    "h",
    "infra",
    "install_local_packages",
    "lazy_attribute",
    "load_infra_report",
    "m",
    "main",
    "meltano",
    "oracle_oic",
    "p",
    "r",
    "s",
    "settings",
    "split_csv",
    "t",
    "tap_oracle_oic",
    "td",
    "tf",
    "tk",
    "tm",
    "to_json",
    "to_jsonable_python",
    "tv",
    "u",
    "unit",
    "web",
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
            "flext_auth": ("auth",),
            "flext_cli": ("cli",),
            "flext_core": ("core", "d", "e", "h", "lazy_attribute", "r", "x"),
            "flext_infra": ("docs_main", "infra"),
            "flext_meltano": ("meltano",),
            "flext_oracle_oic": ("oracle_oic",),
            "flext_tap_oracle_oic": ("main", "tap_oracle_oic"),
            "flext_tests": (
                "active_rules",
                "api",
                "config",
                "discover_repository_root",
                "install_local_packages",
                "load_infra_report",
                "settings",
                "split_csv",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
            ),
            "flext_web": ("web",),
            "pydantic_core": ("from_json", "to_json", "to_jsonable_python"),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
