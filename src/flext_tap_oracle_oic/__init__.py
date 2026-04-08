# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Oracle Oic package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)
from flext_tap_oracle_oic.__version__ import *

if _t.TYPE_CHECKING:
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_tap_oracle_oic._models.streams import FlextTapOracleOicModelsStreams, th
    from flext_tap_oracle_oic.api import (
        FlextTapOracleOicService,
        FlextTapOracleOicService as s,
    )
    from flext_tap_oracle_oic.cli import FlextTapOracleOicCli, main
    from flext_tap_oracle_oic.constants import (
        FlextTapOracleOicConstants,
        FlextTapOracleOicConstants as c,
    )
    from flext_tap_oracle_oic.errors import (
        FlextTapOracleOicApiError,
        FlextTapOracleOicAuthenticationError,
        FlextTapOracleOicConnectionError,
        FlextTapOracleOicExceptionFactory,
        FlextTapOracleOicValidationError,
    )
    from flext_tap_oracle_oic.health import FlextTapOracleOicHealthChecker
    from flext_tap_oracle_oic.models import (
        FlextTapOracleOicModels,
        FlextTapOracleOicModels as m,
    )
    from flext_tap_oracle_oic.protocols import (
        FlextTapOracleOicProtocols,
        FlextTapOracleOicProtocols as p,
    )
    from flext_tap_oracle_oic.settings import FlextTapOracleOicSettings
    from flext_tap_oracle_oic.tap import (
        FlextOracleOicAuthenticator,
        FlextTapOracleOic,
        FlextTapOracleOicClient,
    )
    from flext_tap_oracle_oic.tap_streams import FlextTapOracleOicPaginator
    from flext_tap_oracle_oic.typings import (
        FlextTapOracleOicTypes,
        FlextTapOracleOicTypes as t,
    )
    from flext_tap_oracle_oic.utilities import (
        FlextTapOracleOicUtilities,
        FlextTapOracleOicUtilities as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("._models",),
    build_lazy_import_map(
        {
            ".__version__": (
                "__author__",
                "__author_email__",
                "__description__",
                "__license__",
                "__title__",
                "__url__",
                "__version__",
                "__version_info__",
            ),
            ".api": ("FlextTapOracleOicService",),
            ".cli": (
                "FlextTapOracleOicCli",
                "main",
            ),
            ".constants": ("FlextTapOracleOicConstants",),
            ".errors": (
                "FlextTapOracleOicApiError",
                "FlextTapOracleOicAuthenticationError",
                "FlextTapOracleOicConnectionError",
                "FlextTapOracleOicExceptionFactory",
                "FlextTapOracleOicValidationError",
            ),
            ".health": ("FlextTapOracleOicHealthChecker",),
            ".models": ("FlextTapOracleOicModels",),
            ".protocols": ("FlextTapOracleOicProtocols",),
            ".settings": ("FlextTapOracleOicSettings",),
            ".tap": (
                "FlextOracleOicAuthenticator",
                "FlextTapOracleOic",
                "FlextTapOracleOicClient",
            ),
            ".tap_streams": ("FlextTapOracleOicPaginator",),
            ".typings": ("FlextTapOracleOicTypes",),
            ".utilities": ("FlextTapOracleOicUtilities",),
        },
        alias_groups={
            ".api": (("s", "FlextTapOracleOicService"),),
            ".constants": (("c", "FlextTapOracleOicConstants"),),
            ".models": (("m", "FlextTapOracleOicModels"),),
            ".protocols": (("p", "FlextTapOracleOicProtocols"),),
            ".typings": (("t", "FlextTapOracleOicTypes"),),
            ".utilities": (("u", "FlextTapOracleOicUtilities"),),
            "flext_core.decorators": (("d", "FlextDecorators"),),
            "flext_core.exceptions": (("e", "FlextExceptions"),),
            "flext_core.handlers": (("h", "FlextHandlers"),),
            "flext_core.mixins": (("x", "FlextMixins"),),
            "flext_core.result": (("r", "FlextResult"),),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
    ),
    module_name=__name__,
)

__all__ = [
    "FlextOracleOicAuthenticator",
    "FlextTapOracleOic",
    "FlextTapOracleOicApiError",
    "FlextTapOracleOicAuthenticationError",
    "FlextTapOracleOicCli",
    "FlextTapOracleOicClient",
    "FlextTapOracleOicConnectionError",
    "FlextTapOracleOicConstants",
    "FlextTapOracleOicExceptionFactory",
    "FlextTapOracleOicHealthChecker",
    "FlextTapOracleOicModels",
    "FlextTapOracleOicModelsStreams",
    "FlextTapOracleOicPaginator",
    "FlextTapOracleOicProtocols",
    "FlextTapOracleOicService",
    "FlextTapOracleOicSettings",
    "FlextTapOracleOicTypes",
    "FlextTapOracleOicUtilities",
    "FlextTapOracleOicValidationError",
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
    "th",
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
