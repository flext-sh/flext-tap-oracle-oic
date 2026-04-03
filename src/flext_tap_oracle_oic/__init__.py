# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext tap oracle oic package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_tap_oracle_oic.__version__ import *

if _t.TYPE_CHECKING:
    import flext_tap_oracle_oic._models as _flext_tap_oracle_oic__models
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

    _models = _flext_tap_oracle_oic__models
    import flext_tap_oracle_oic._models.streams as _flext_tap_oracle_oic__models_streams

    streams = _flext_tap_oracle_oic__models_streams
    import flext_tap_oracle_oic.api as _flext_tap_oracle_oic_api
    from flext_tap_oracle_oic._models.streams import (
        ALL_STREAMS,
        FlextTapOracleOicModelsStreams,
        th,
    )

    api = _flext_tap_oracle_oic_api
    import flext_tap_oracle_oic.cli as _flext_tap_oracle_oic_cli
    from flext_tap_oracle_oic.api import (
        FlextTapOracleOicService,
        FlextTapOracleOicService as s,
    )

    cli = _flext_tap_oracle_oic_cli
    import flext_tap_oracle_oic.constants as _flext_tap_oracle_oic_constants
    from flext_tap_oracle_oic.cli import main

    constants = _flext_tap_oracle_oic_constants
    import flext_tap_oracle_oic.errors as _flext_tap_oracle_oic_errors
    from flext_tap_oracle_oic.constants import (
        FlextTapOracleOicConstants,
        FlextTapOracleOicConstants as c,
    )

    errors = _flext_tap_oracle_oic_errors
    import flext_tap_oracle_oic.health as _flext_tap_oracle_oic_health
    from flext_tap_oracle_oic.errors import (
        FlextTapOracleOicApiError,
        FlextTapOracleOicAuthenticationError,
        FlextTapOracleOicConnectionError,
        FlextTapOracleOicExceptionFactory,
        FlextTapOracleOicValidationError,
    )

    health = _flext_tap_oracle_oic_health
    import flext_tap_oracle_oic.models as _flext_tap_oracle_oic_models
    from flext_tap_oracle_oic.health import FlextTapOracleOicHealthChecker

    models = _flext_tap_oracle_oic_models
    import flext_tap_oracle_oic.protocols as _flext_tap_oracle_oic_protocols
    from flext_tap_oracle_oic.models import (
        FlextTapOracleOicModels,
        FlextTapOracleOicModels as m,
    )

    protocols = _flext_tap_oracle_oic_protocols
    import flext_tap_oracle_oic.settings as _flext_tap_oracle_oic_settings
    from flext_tap_oracle_oic.protocols import (
        FlextTapOracleOicProtocols,
        FlextTapOracleOicProtocols as p,
    )

    settings = _flext_tap_oracle_oic_settings
    import flext_tap_oracle_oic.tap as _flext_tap_oracle_oic_tap
    from flext_tap_oracle_oic.settings import (
        FlextTapOracleOicSettings,
        flext_tap_oracle_oic_create_config,
        validate_configuration,
    )

    tap = _flext_tap_oracle_oic_tap
    import flext_tap_oracle_oic.tap_streams as _flext_tap_oracle_oic_tap_streams
    from flext_tap_oracle_oic.tap import (
        FlextOracleOicAuthenticator,
        FlextTapOracleOic,
        FlextTapOracleOicClient,
        logger,
    )

    tap_streams = _flext_tap_oracle_oic_tap_streams
    import flext_tap_oracle_oic.typings as _flext_tap_oracle_oic_typings
    from flext_tap_oracle_oic.tap_streams import FlextTapOracleOicPaginator

    typings = _flext_tap_oracle_oic_typings
    import flext_tap_oracle_oic.utilities as _flext_tap_oracle_oic_utilities
    from flext_tap_oracle_oic.typings import (
        FlextTapOracleOicTypes,
        FlextTapOracleOicTypes as t,
    )

    utilities = _flext_tap_oracle_oic_utilities
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_tap_oracle_oic.utilities import (
        FlextTapOracleOicUtilities,
        FlextTapOracleOicUtilities as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("flext_tap_oracle_oic._models",),
    {
        "FlextOracleOicAuthenticator": "flext_tap_oracle_oic.tap",
        "FlextTapOracleOic": "flext_tap_oracle_oic.tap",
        "FlextTapOracleOicApiError": "flext_tap_oracle_oic.errors",
        "FlextTapOracleOicAuthenticationError": "flext_tap_oracle_oic.errors",
        "FlextTapOracleOicClient": "flext_tap_oracle_oic.tap",
        "FlextTapOracleOicConnectionError": "flext_tap_oracle_oic.errors",
        "FlextTapOracleOicConstants": "flext_tap_oracle_oic.constants",
        "FlextTapOracleOicExceptionFactory": "flext_tap_oracle_oic.errors",
        "FlextTapOracleOicHealthChecker": "flext_tap_oracle_oic.health",
        "FlextTapOracleOicModels": "flext_tap_oracle_oic.models",
        "FlextTapOracleOicPaginator": "flext_tap_oracle_oic.tap_streams",
        "FlextTapOracleOicProtocols": "flext_tap_oracle_oic.protocols",
        "FlextTapOracleOicService": "flext_tap_oracle_oic.api",
        "FlextTapOracleOicSettings": "flext_tap_oracle_oic.settings",
        "FlextTapOracleOicTypes": "flext_tap_oracle_oic.typings",
        "FlextTapOracleOicUtilities": "flext_tap_oracle_oic.utilities",
        "FlextTapOracleOicValidationError": "flext_tap_oracle_oic.errors",
        "__author__": "flext_tap_oracle_oic.__version__",
        "__author_email__": "flext_tap_oracle_oic.__version__",
        "__description__": "flext_tap_oracle_oic.__version__",
        "__license__": "flext_tap_oracle_oic.__version__",
        "__title__": "flext_tap_oracle_oic.__version__",
        "__url__": "flext_tap_oracle_oic.__version__",
        "__version__": "flext_tap_oracle_oic.__version__",
        "__version_info__": "flext_tap_oracle_oic.__version__",
        "_models": "flext_tap_oracle_oic._models",
        "api": "flext_tap_oracle_oic.api",
        "c": ("flext_tap_oracle_oic.constants", "FlextTapOracleOicConstants"),
        "cli": "flext_tap_oracle_oic.cli",
        "constants": "flext_tap_oracle_oic.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "errors": "flext_tap_oracle_oic.errors",
        "flext_tap_oracle_oic_create_config": "flext_tap_oracle_oic.settings",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "health": "flext_tap_oracle_oic.health",
        "logger": "flext_tap_oracle_oic.tap",
        "m": ("flext_tap_oracle_oic.models", "FlextTapOracleOicModels"),
        "main": "flext_tap_oracle_oic.cli",
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
        "validate_configuration": "flext_tap_oracle_oic.settings",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)

__all__ = [
    "ALL_STREAMS",
    "FlextOracleOicAuthenticator",
    "FlextTapOracleOic",
    "FlextTapOracleOicApiError",
    "FlextTapOracleOicAuthenticationError",
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
    "flext_tap_oracle_oic_create_config",
    "h",
    "health",
    "logger",
    "m",
    "main",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "settings",
    "streams",
    "t",
    "tap",
    "tap_streams",
    "th",
    "typings",
    "u",
    "utilities",
    "validate_configuration",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
