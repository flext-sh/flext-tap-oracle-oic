# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Oracle Oic package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import (
    __author__ as __author__,
    __author_email__ as __author_email__,
    __description__ as __description__,
    __license__ as __license__,
    __title__ as __title__,
    __url__ as __url__,
    __version__ as __version__,
    __version_info__ as __version_info__,
)

if TYPE_CHECKING:
    from enum import StrEnum, unique
    from typing import TYPE_CHECKING, ClassVar, Final

    from flext_oracle_oic import FlextOracleOicConstants, d, e, h, r, s, x

    from ._config import FlextTapOracleOicConfig, config
    from ._settings import FlextTapOracleOicSettings, settings
    from .api import FlextTapOracleOicService, tap_oracle_oic
    from .cli import FlextTapOracleOicCli, main
    from .constants import FlextTapOracleOicConstants, FlextTapOracleOicConstants as c
    from .errors import (
        FlextTapOracleOicApiError,
        FlextTapOracleOicAuthenticationError,
        FlextTapOracleOicConnectionError,
        FlextTapOracleOicValidationError,
    )
    from .models import FlextTapOracleOicModels, FlextTapOracleOicModels as m
    from .protocols import FlextTapOracleOicProtocols, FlextTapOracleOicProtocols as p
    from .tap import (
        FlextOracleOicAuthenticator,
        FlextTapOracleOic,
        FlextTapOracleOicClient,
    )
    from .tap_streams import FlextTapOracleOicPaginator
    from .typings import FlextTapOracleOicTypes, FlextTapOracleOicTypes as t
    from .utilities import FlextTapOracleOicUtilities, FlextTapOracleOicUtilities as u
__all__: tuple[str, ...] = (
    "TYPE_CHECKING",
    "ClassVar",
    "Final",
    "FlextOracleOicAuthenticator",
    "FlextOracleOicConstants",
    "FlextTapOracleOic",
    "FlextTapOracleOicApiError",
    "FlextTapOracleOicAuthenticationError",
    "FlextTapOracleOicCli",
    "FlextTapOracleOicClient",
    "FlextTapOracleOicConfig",
    "FlextTapOracleOicConnectionError",
    "FlextTapOracleOicConstants",
    "FlextTapOracleOicModels",
    "FlextTapOracleOicPaginator",
    "FlextTapOracleOicProtocols",
    "FlextTapOracleOicService",
    "FlextTapOracleOicSettings",
    "FlextTapOracleOicTypes",
    "FlextTapOracleOicUtilities",
    "FlextTapOracleOicValidationError",
    "StrEnum",
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
    "unique",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            "._config": ("FlextTapOracleOicConfig", "config"),
            "._settings": ("FlextTapOracleOicSettings", "settings"),
            ".api": ("FlextTapOracleOicService", "tap_oracle_oic"),
            ".cli": ("FlextTapOracleOicCli", "main"),
            ".constants": ("FlextTapOracleOicConstants", "c"),
            ".errors": (
                "FlextTapOracleOicApiError",
                "FlextTapOracleOicAuthenticationError",
                "FlextTapOracleOicConnectionError",
                "FlextTapOracleOicValidationError",
            ),
            ".models": ("FlextTapOracleOicModels", "m"),
            ".protocols": ("FlextTapOracleOicProtocols", "p"),
            ".tap": (
                "FlextOracleOicAuthenticator",
                "FlextTapOracleOic",
                "FlextTapOracleOicClient",
            ),
            ".tap_streams": ("FlextTapOracleOicPaginator",),
            ".typings": ("FlextTapOracleOicTypes", "t"),
            ".utilities": ("FlextTapOracleOicUtilities", "u"),
            "enum": ("StrEnum", "unique"),
            "flext_oracle_oic": (
                "FlextOracleOicConstants",
                "d",
                "e",
                "h",
                "r",
                "s",
                "x",
            ),
            "typing": ("ClassVar", "Final", "TYPE_CHECKING"),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
