# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Oracle Oic package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports
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
from flext_tap_oracle_oic._exports import FLEXT_TAP_ORACLE_OIC_LAZY_IMPORTS

if TYPE_CHECKING:
    from flext_core._root_typing_parts.facades import (
        d as d,
        e as e,
        h as h,
        r as r,
        s as s,
        x as x,
    )
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


_LAZY_IMPORTS = FLEXT_TAP_ORACLE_OIC_LAZY_IMPORTS


_EAGER_EXPORTS = (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)


_PUBLIC_EXPORTS: tuple[str, ...] = (
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
    "tap_oracle_oic",
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
    "u",
    "x",
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
    public_exports=_PUBLIC_EXPORTS,
)
