# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext tap oracle oic package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_tap_oracle_oic.__version__ import *

if _t.TYPE_CHECKING:
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_tap_oracle_oic import (
        _models,
        api,
        cli,
        constants,
        errors,
        health,
        models,
        protocols,
        settings,
        tap,
        tap_streams,
        typings,
        utilities,
    )
    from flext_tap_oracle_oic._models.streams import FlextTapOracleOicModelsStreams, th
    from flext_tap_oracle_oic.api import (
        FlextTapOracleOicService,
        FlextTapOracleOicService as s,
    )
    from flext_tap_oracle_oic.cli import FlextTapOracleOicCli
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
    ("flext_tap_oracle_oic._models",),
    {
        "FlextOracleOicAuthenticator": (
            "flext_tap_oracle_oic.tap",
            "FlextOracleOicAuthenticator",
        ),
        "FlextTapOracleOic": ("flext_tap_oracle_oic.tap", "FlextTapOracleOic"),
        "FlextTapOracleOicApiError": (
            "flext_tap_oracle_oic.errors",
            "FlextTapOracleOicApiError",
        ),
        "FlextTapOracleOicAuthenticationError": (
            "flext_tap_oracle_oic.errors",
            "FlextTapOracleOicAuthenticationError",
        ),
        "FlextTapOracleOicCli": ("flext_tap_oracle_oic.cli", "FlextTapOracleOicCli"),
        "FlextTapOracleOicClient": (
            "flext_tap_oracle_oic.tap",
            "FlextTapOracleOicClient",
        ),
        "FlextTapOracleOicConnectionError": (
            "flext_tap_oracle_oic.errors",
            "FlextTapOracleOicConnectionError",
        ),
        "FlextTapOracleOicConstants": (
            "flext_tap_oracle_oic.constants",
            "FlextTapOracleOicConstants",
        ),
        "FlextTapOracleOicExceptionFactory": (
            "flext_tap_oracle_oic.errors",
            "FlextTapOracleOicExceptionFactory",
        ),
        "FlextTapOracleOicHealthChecker": (
            "flext_tap_oracle_oic.health",
            "FlextTapOracleOicHealthChecker",
        ),
        "FlextTapOracleOicModels": (
            "flext_tap_oracle_oic.models",
            "FlextTapOracleOicModels",
        ),
        "FlextTapOracleOicPaginator": (
            "flext_tap_oracle_oic.tap_streams",
            "FlextTapOracleOicPaginator",
        ),
        "FlextTapOracleOicProtocols": (
            "flext_tap_oracle_oic.protocols",
            "FlextTapOracleOicProtocols",
        ),
        "FlextTapOracleOicService": (
            "flext_tap_oracle_oic.api",
            "FlextTapOracleOicService",
        ),
        "FlextTapOracleOicSettings": (
            "flext_tap_oracle_oic.settings",
            "FlextTapOracleOicSettings",
        ),
        "FlextTapOracleOicTypes": (
            "flext_tap_oracle_oic.typings",
            "FlextTapOracleOicTypes",
        ),
        "FlextTapOracleOicUtilities": (
            "flext_tap_oracle_oic.utilities",
            "FlextTapOracleOicUtilities",
        ),
        "FlextTapOracleOicValidationError": (
            "flext_tap_oracle_oic.errors",
            "FlextTapOracleOicValidationError",
        ),
        "__author__": ("flext_tap_oracle_oic.__version__", "__author__"),
        "__author_email__": ("flext_tap_oracle_oic.__version__", "__author_email__"),
        "__description__": ("flext_tap_oracle_oic.__version__", "__description__"),
        "__license__": ("flext_tap_oracle_oic.__version__", "__license__"),
        "__title__": ("flext_tap_oracle_oic.__version__", "__title__"),
        "__url__": ("flext_tap_oracle_oic.__version__", "__url__"),
        "__version__": ("flext_tap_oracle_oic.__version__", "__version__"),
        "__version_info__": ("flext_tap_oracle_oic.__version__", "__version_info__"),
        "_models": "flext_tap_oracle_oic._models",
        "api": "flext_tap_oracle_oic.api",
        "c": ("flext_tap_oracle_oic.constants", "FlextTapOracleOicConstants"),
        "cli": "flext_tap_oracle_oic.cli",
        "constants": "flext_tap_oracle_oic.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "errors": "flext_tap_oracle_oic.errors",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "health": "flext_tap_oracle_oic.health",
        "m": ("flext_tap_oracle_oic.models", "FlextTapOracleOicModels"),
        "models": "flext_tap_oracle_oic.models",
        "p": ("flext_tap_oracle_oic.protocols", "FlextTapOracleOicProtocols"),
        "protocols": "flext_tap_oracle_oic.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_tap_oracle_oic.api", "FlextTapOracleOicService"),
        "settings": "flext_tap_oracle_oic.settings",
        "t": ("flext_tap_oracle_oic.typings", "FlextTapOracleOicTypes"),
        "tap": "flext_tap_oracle_oic.tap",
        "tap_streams": "flext_tap_oracle_oic.tap_streams",
        "typings": "flext_tap_oracle_oic.typings",
        "u": ("flext_tap_oracle_oic.utilities", "FlextTapOracleOicUtilities"),
        "utilities": "flext_tap_oracle_oic.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)
_ = _LAZY_IMPORTS.pop("cleanup_submodule_namespace", None)
_ = _LAZY_IMPORTS.pop("install_lazy_exports", None)
_ = _LAZY_IMPORTS.pop("lazy_getattr", None)
_ = _LAZY_IMPORTS.pop("logger", None)
_ = _LAZY_IMPORTS.pop("merge_lazy_imports", None)
_ = _LAZY_IMPORTS.pop("output", None)
_ = _LAZY_IMPORTS.pop("output_reporting", None)

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
    "_models",
    "api",
    "c",
    "cli",
    "constants",
    "d",
    "e",
    "errors",
    "h",
    "health",
    "m",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "settings",
    "t",
    "tap",
    "tap_streams",
    "th",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
