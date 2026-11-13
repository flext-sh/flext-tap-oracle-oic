# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import api, d, e, h, r, td, tf, tk, tm, x

    from flext_tap_oracle_oic import (
        FlextTapOracleOic,
        FlextTapOracleOicAuthenticator,
        FlextTapOracleOicCli,
        FlextTapOracleOicClient,
        FlextTapOracleOicConfig,
        FlextTapOracleOicConstants,
        FlextTapOracleOicExtractService,
        FlextTapOracleOicModels,
        FlextTapOracleOicPaginator,
        FlextTapOracleOicProtocols,
        FlextTapOracleOicService,
        FlextTapOracleOicSettings,
        FlextTapOracleOicTypes,
        FlextTapOracleOicUtilities,
        FlextTapOracleOicVersion,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
        config,
        main,
        settings,
        tap_oracle_oic,
    )
    from tests.base import TestsFlextTapOracleOicServiceBase, s
    from tests.constants import TestsFlextTapOracleOicConstants, c
    from tests.models import TestsFlextTapOracleOicModels, m
    from tests.protocols import TestsFlextTapOracleOicProtocols, p
    from tests.settings import TestsFlextTapOracleOicSettings
    from tests.typings import TestsFlextTapOracleOicTypes, t
    from tests.utilities import TestsFlextTapOracleOicUtilities, u


__all__: tuple[str, ...] = (
    "FlextTapOracleOic",
    "FlextTapOracleOicAuthenticator",
    "FlextTapOracleOicCli",
    "FlextTapOracleOicClient",
    "FlextTapOracleOicConfig",
    "FlextTapOracleOicConstants",
    "FlextTapOracleOicExtractService",
    "FlextTapOracleOicModels",
    "FlextTapOracleOicPaginator",
    "FlextTapOracleOicProtocols",
    "FlextTapOracleOicService",
    "FlextTapOracleOicSettings",
    "FlextTapOracleOicTypes",
    "FlextTapOracleOicUtilities",
    "FlextTapOracleOicVersion",
    "TestsFlextTapOracleOicConstants",
    "TestsFlextTapOracleOicModels",
    "TestsFlextTapOracleOicProtocols",
    "TestsFlextTapOracleOicServiceBase",
    "TestsFlextTapOracleOicSettings",
    "TestsFlextTapOracleOicTypes",
    "TestsFlextTapOracleOicUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "api",
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
    "td",
    "tf",
    "tk",
    "tm",
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    {
        "FlextTapOracleOic": "flext_tap_oracle_oic",
        "FlextTapOracleOicAuthenticator": "flext_tap_oracle_oic",
        "FlextTapOracleOicCli": "flext_tap_oracle_oic",
        "FlextTapOracleOicClient": "flext_tap_oracle_oic",
        "FlextTapOracleOicConfig": "flext_tap_oracle_oic",
        "FlextTapOracleOicConstants": "flext_tap_oracle_oic",
        "FlextTapOracleOicExtractService": "flext_tap_oracle_oic",
        "FlextTapOracleOicModels": "flext_tap_oracle_oic",
        "FlextTapOracleOicPaginator": "flext_tap_oracle_oic",
        "FlextTapOracleOicProtocols": "flext_tap_oracle_oic",
        "FlextTapOracleOicService": "flext_tap_oracle_oic",
        "FlextTapOracleOicSettings": "flext_tap_oracle_oic",
        "FlextTapOracleOicTypes": "flext_tap_oracle_oic",
        "FlextTapOracleOicUtilities": "flext_tap_oracle_oic",
        "FlextTapOracleOicVersion": "flext_tap_oracle_oic",
        "TestsFlextTapOracleOicConstants": ".constants",
        "TestsFlextTapOracleOicModels": ".models",
        "TestsFlextTapOracleOicProtocols": ".protocols",
        "TestsFlextTapOracleOicServiceBase": ".base",
        "TestsFlextTapOracleOicSettings": ".settings",
        "TestsFlextTapOracleOicTypes": ".typings",
        "TestsFlextTapOracleOicUtilities": ".utilities",
        "__author__": "flext_tap_oracle_oic",
        "__author_email__": "flext_tap_oracle_oic",
        "__description__": "flext_tap_oracle_oic",
        "__license__": "flext_tap_oracle_oic",
        "__title__": "flext_tap_oracle_oic",
        "__url__": "flext_tap_oracle_oic",
        "__version__": "flext_tap_oracle_oic",
        "__version_info__": "flext_tap_oracle_oic",
        "api": "flext_tests",
        "c": ".constants",
        "config": "flext_tap_oracle_oic",
        "d": "flext_tests",
        "e": "flext_tests",
        "h": "flext_tests",
        "m": ".models",
        "main": "flext_tap_oracle_oic",
        "p": ".protocols",
        "r": "flext_tests",
        "s": ".base",
        "settings": "flext_tap_oracle_oic",
        "t": ".typings",
        "tap_oracle_oic": "flext_tap_oracle_oic",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "x": "flext_tests",
    },
    public_exports=__all__,
)
