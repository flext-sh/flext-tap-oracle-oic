# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Oracle Oic package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports
from flext_tap_oracle_oic.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if TYPE_CHECKING:
    from flext_meltano import d, e, h, r, s, x

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
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "config",
    "d",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "tap_oracle_oic",
    "u",
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
        "c": ".constants",
        "config": "._config",
        "d": "flext_meltano",
        "e": "flext_meltano",
        "h": "flext_meltano",
        "m": ".models",
        "main": ".cli",
        "p": ".protocols",
        "r": "flext_meltano",
        "s": "flext_meltano",
        "settings": "._settings",
        "t": ".typings",
        "tap_oracle_oic": ".api",
        "u": ".utilities",
        "x": "flext_meltano",
    }),
    public_exports=__all__,
)
