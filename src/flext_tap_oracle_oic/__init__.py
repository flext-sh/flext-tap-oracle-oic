# @generated AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Oracle Oic package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import __author__ as __author__
from .__version__ import __author_email__ as __author_email__
from .__version__ import __description__ as __description__
from .__version__ import __license__ as __license__
from .__version__ import __title__ as __title__
from .__version__ import __url__ as __url__
from .__version__ import __version__ as __version__
from .__version__ import __version_info__ as __version_info__

if TYPE_CHECKING:
    from flext_oracle_oic import d as d
    from flext_oracle_oic import e as e
    from flext_oracle_oic import h as h
    from flext_oracle_oic import r as r
    from flext_oracle_oic import s as s
    from flext_oracle_oic import x as x

    from ._config import FlextTapOracleOicConfig as FlextTapOracleOicConfig
    from ._config import config as config
    from ._settings import FlextTapOracleOicSettings as FlextTapOracleOicSettings
    from ._settings import settings as settings
    from .api import FlextTapOracleOicService as FlextTapOracleOicService
    from .api import tap_oracle_oic as tap_oracle_oic
    from .cli import FlextTapOracleOicCli as FlextTapOracleOicCli
    from .cli import main as main
    from .constants import FlextTapOracleOicConstants as FlextTapOracleOicConstants

    c: type[FlextTapOracleOicConstants]
    from .models import FlextTapOracleOicModels as FlextTapOracleOicModels

    m: type[FlextTapOracleOicModels]
    from .protocols import FlextTapOracleOicProtocols as FlextTapOracleOicProtocols

    p: type[FlextTapOracleOicProtocols]
    from .tap import FlextOracleOicAuthenticator as FlextOracleOicAuthenticator
    from .tap import FlextTapOracleOic as FlextTapOracleOic
    from .tap import FlextTapOracleOicClient as FlextTapOracleOicClient
    from .typings import FlextTapOracleOicTypes as FlextTapOracleOicTypes

    t: type[FlextTapOracleOicTypes]
    from .utilities import FlextTapOracleOicUtilities as FlextTapOracleOicUtilities

    u: type[FlextTapOracleOicUtilities]

_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    "._config": ("FlextTapOracleOicConfig", "config"),
    "._settings": ("FlextTapOracleOicSettings", "settings"),
    ".api": ("FlextTapOracleOicService", "tap_oracle_oic"),
    ".cli": ("FlextTapOracleOicCli", "main"),
    ".constants": ("FlextTapOracleOicConstants", "c"),
    ".models": ("FlextTapOracleOicModels", "m"),
    ".protocols": ("FlextTapOracleOicProtocols", "p"),
    ".tap": (
        "FlextOracleOicAuthenticator",
        "FlextTapOracleOic",
        "FlextTapOracleOicClient",
    ),
    ".typings": ("FlextTapOracleOicTypes", "t"),
    ".utilities": ("FlextTapOracleOicUtilities", "u"),
    "flext_oracle_oic": ("d", "e", "h", "r", "s", "x"),
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES, alias_groups=_LAZY_ALIAS_GROUPS, sort_keys=False
)

_PUBLIC_EXPORTS: tuple[str, ...] = (
    "FlextOracleOicAuthenticator",
    "FlextTapOracleOic",
    "FlextTapOracleOicCli",
    "FlextTapOracleOicClient",
    "FlextTapOracleOicConfig",
    "FlextTapOracleOicConstants",
    "FlextTapOracleOicModels",
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

__all__: tuple[str, ...] = tuple(_PUBLIC_EXPORTS)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
