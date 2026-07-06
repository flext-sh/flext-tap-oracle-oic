# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Oracle Oic package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports
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
    from flext_oracle_oic import d as d, e as e, h as h, r as r, s as s, x as x
    from flext_tap_oracle_oic.api import (
        FlextTapOracleOicService as FlextTapOracleOicService,
        tap_oracle_oic as tap_oracle_oic,
    )
    from flext_tap_oracle_oic.cli import (
        FlextTapOracleOicCli as FlextTapOracleOicCli,
        main as main,
    )
    from flext_tap_oracle_oic.constants import (
        FlextTapOracleOicConstants as FlextTapOracleOicConstants,
        c as c,
    )
    from flext_tap_oracle_oic.models import (
        FlextTapOracleOicModels as FlextTapOracleOicModels,
        m as m,
    )
    from flext_tap_oracle_oic.protocols import (
        FlextTapOracleOicProtocols as FlextTapOracleOicProtocols,
        p as p,
    )
    from flext_tap_oracle_oic.settings import (
        FlextTapOracleOicSettings as FlextTapOracleOicSettings,
    )
    from flext_tap_oracle_oic.tap import (
        FlextOracleOicAuthenticator as FlextOracleOicAuthenticator,
        FlextTapOracleOic as FlextTapOracleOic,
        FlextTapOracleOicClient as FlextTapOracleOicClient,
    )
    from flext_tap_oracle_oic.typings import (
        FlextTapOracleOicTypes as FlextTapOracleOicTypes,
        t as t,
    )
    from flext_tap_oracle_oic.utilities import (
        FlextTapOracleOicUtilities as FlextTapOracleOicUtilities,
        u as u,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".api": (
            "FlextTapOracleOicService",
            "tap_oracle_oic",
        ),
        ".cli": (
            "FlextTapOracleOicCli",
            "main",
        ),
        ".constants": (
            "FlextTapOracleOicConstants",
            "c",
        ),
        ".models": (
            "FlextTapOracleOicModels",
            "m",
        ),
        ".protocols": (
            "FlextTapOracleOicProtocols",
            "p",
        ),
        ".settings": ("FlextTapOracleOicSettings",),
        ".tap": (
            "FlextOracleOicAuthenticator",
            "FlextTapOracleOic",
            "FlextTapOracleOicClient",
        ),
        ".typings": (
            "FlextTapOracleOicTypes",
            "t",
        ),
        ".utilities": (
            "FlextTapOracleOicUtilities",
            "u",
        ),
        "flext_oracle_oic": (
            "d",
            "e",
            "h",
            "r",
            "s",
            "x",
        ),
    },
)


__all__: tuple[str, ...] = (
    "FlextOracleOicAuthenticator",
    "FlextTapOracleOic",
    "FlextTapOracleOicCli",
    "FlextTapOracleOicClient",
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
    "d",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "t",
    "tap_oracle_oic",
    "u",
    "x",
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    public_exports=__all__,
)
