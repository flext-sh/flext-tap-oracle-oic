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
        "c": ("flext_tap_oracle_oic.constants", "FlextTapOracleOicConstants"),
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("flext_tap_oracle_oic.models", "FlextTapOracleOicModels"),
        "p": ("flext_tap_oracle_oic.protocols", "FlextTapOracleOicProtocols"),
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_tap_oracle_oic.api", "FlextTapOracleOicService"),
        "t": ("flext_tap_oracle_oic.typings", "FlextTapOracleOicTypes"),
        "u": ("flext_tap_oracle_oic.utilities", "FlextTapOracleOicUtilities"),
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
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "th",
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
