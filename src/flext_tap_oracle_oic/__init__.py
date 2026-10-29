# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Oracle Oic package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_meltano import (
        build_lazy_import_map,
        cleanup_submodule_namespace,
        cli,
        core,
        d,
        e,
        h,
        install_lazy_exports,
        lazy,
        lazy_getattr,
        lazy_member,
        meltano,
        merge_lazy_imports,
        normalize_lazy_imports,
        r,
        resolve_lazy_members,
        s,
        x,
    )
    from flext_oracle_oic import api, auth, oracle_oic, web

    from flext_tap_oracle_oic.__version__ import (
        FlextTapOracleOicVersion,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
    )
    from flext_tap_oracle_oic._config import FlextTapOracleOicConfig, config
    from flext_tap_oracle_oic._settings import FlextTapOracleOicSettings, settings
    from flext_tap_oracle_oic.api import FlextTapOracleOicService, tap_oracle_oic
    from flext_tap_oracle_oic.authenticator import FlextTapOracleOicAuthenticator
    from flext_tap_oracle_oic.cli import FlextTapOracleOicCli, main
    from flext_tap_oracle_oic.client import FlextTapOracleOicClient
    from flext_tap_oracle_oic.constants import FlextTapOracleOicConstants, c
    from flext_tap_oracle_oic.models import FlextTapOracleOicModels, m
    from flext_tap_oracle_oic.protocols import FlextTapOracleOicProtocols, p
    from flext_tap_oracle_oic.tap import FlextTapOracleOic
    from flext_tap_oracle_oic.tap_streams import FlextTapOracleOicPaginator
    from flext_tap_oracle_oic.typings import FlextTapOracleOicTypes, t
    from flext_tap_oracle_oic.utilities import FlextTapOracleOicUtilities, u


__all__: tuple[str, ...] = (
    "FlextTapOracleOic",
    "FlextTapOracleOicAuthenticator",
    "FlextTapOracleOicCli",
    "FlextTapOracleOicClient",
    "FlextTapOracleOicConfig",
    "FlextTapOracleOicConstants",
    "FlextTapOracleOicModels",
    "FlextTapOracleOicPaginator",
    "FlextTapOracleOicProtocols",
    "FlextTapOracleOicService",
    "FlextTapOracleOicSettings",
    "FlextTapOracleOicTypes",
    "FlextTapOracleOicUtilities",
    "FlextTapOracleOicVersion",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "api",
    "auth",
    "build_lazy_import_map",
    "c",
    "cleanup_submodule_namespace",
    "cli",
    "config",
    "core",
    "d",
    "e",
    "h",
    "install_lazy_exports",
    "lazy",
    "lazy_getattr",
    "lazy_member",
    "m",
    "main",
    "meltano",
    "merge_lazy_imports",
    "normalize_lazy_imports",
    "oracle_oic",
    "p",
    "r",
    "resolve_lazy_members",
    "s",
    "settings",
    "t",
    "tap_oracle_oic",
    "u",
    "web",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextTapOracleOic": ".tap",
        "FlextTapOracleOicAuthenticator": ".authenticator",
        "FlextTapOracleOicCli": ".cli",
        "FlextTapOracleOicClient": ".client",
        "FlextTapOracleOicConfig": "._config",
        "FlextTapOracleOicConstants": ".constants",
        "FlextTapOracleOicModels": ".models",
        "FlextTapOracleOicPaginator": ".tap_streams",
        "FlextTapOracleOicProtocols": ".protocols",
        "FlextTapOracleOicService": ".api",
        "FlextTapOracleOicSettings": "._settings",
        "FlextTapOracleOicTypes": ".typings",
        "FlextTapOracleOicUtilities": ".utilities",
        "FlextTapOracleOicVersion": ".__version__",
        "__author__": ".__version__",
        "__author_email__": ".__version__",
        "__description__": ".__version__",
        "__license__": ".__version__",
        "__title__": ".__version__",
        "__url__": ".__version__",
        "__version_info__": ".__version__",
        "api": "flext_oracle_oic",
        "auth": "flext_oracle_oic",
        "build_lazy_import_map": "flext_meltano",
        "c": ".constants",
        "cleanup_submodule_namespace": "flext_meltano",
        "cli": "flext_meltano",
        "config": "._config",
        "core": "flext_meltano",
        "d": "flext_meltano",
        "e": "flext_meltano",
        "h": "flext_meltano",
        "install_lazy_exports": "flext_meltano",
        "lazy": "flext_meltano",
        "lazy_getattr": "flext_meltano",
        "lazy_member": "flext_meltano",
        "m": ".models",
        "main": ".cli",
        "meltano": "flext_meltano",
        "merge_lazy_imports": "flext_meltano",
        "normalize_lazy_imports": "flext_meltano",
        "oracle_oic": "flext_oracle_oic",
        "p": ".protocols",
        "r": "flext_meltano",
        "resolve_lazy_members": "flext_meltano",
        "s": "flext_meltano",
        "settings": "._settings",
        "t": ".typings",
        "tap_oracle_oic": ".api",
        "u": ".utilities",
        "web": "flext_oracle_oic",
        "x": "flext_meltano",
    }),
    public_exports=__all__,
)

if not TYPE_CHECKING:
    from flext_tap_oracle_oic.__version__ import __version__
