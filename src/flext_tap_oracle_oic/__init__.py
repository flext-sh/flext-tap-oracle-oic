# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext tap oracle oic package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_tap_oracle_oic.__version__ import (
    __all__,
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
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
        streams,
        tap,
        tap_streams,
        typings,
        utilities,
    )
    from flext_tap_oracle_oic._models import FlextTapOracleOicModelsStreams, th
    from flext_tap_oracle_oic.api import FlextTapOracleOicService
    from flext_tap_oracle_oic.cli import main
    from flext_tap_oracle_oic.constants import (
        FlextTapOracleOicConstants,
        FlextTapOracleOicConstants as c,
    )
    from flext_tap_oracle_oic.errors import FlextTapOracleOicExceptionFactory
    from flext_tap_oracle_oic.health import FlextTapOracleOicHealthChecker
    from flext_tap_oracle_oic.models import (
        FlextTapOracleOicModels,
        FlextTapOracleOicModels as m,
    )
    from flext_tap_oracle_oic.protocols import (
        FlextTapOracleOicProtocols,
        FlextTapOracleOicProtocols as p,
    )
    from flext_tap_oracle_oic.settings import (
        FlextTapOracleOicSettings,
        config_data,
        config_instance,
        required_fields,
        tap_config,
        validate_configuration,
    )
    from flext_tap_oracle_oic.tap import FlextOracleOicAuthenticator, logger
    from flext_tap_oracle_oic.tap_streams import FlextTapOracleOicPaginator
    from flext_tap_oracle_oic.typings import (
        FlextTapOracleOicTypes,
        FlextTapOracleOicTypes as t,
    )
    from flext_tap_oracle_oic.utilities import (
        FlextTapOracleOicUtilities,
        FlextTapOracleOicUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
    ("flext_tap_oracle_oic._models",),
    {
        "FlextOracleOicAuthenticator": "flext_tap_oracle_oic.tap",
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
        "_models": "flext_tap_oracle_oic._models",
        "api": "flext_tap_oracle_oic.api",
        "c": ("flext_tap_oracle_oic.constants", "FlextTapOracleOicConstants"),
        "cli": "flext_tap_oracle_oic.cli",
        "config_data": "flext_tap_oracle_oic.settings",
        "config_instance": "flext_tap_oracle_oic.settings",
        "constants": "flext_tap_oracle_oic.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "errors": "flext_tap_oracle_oic.errors",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "health": "flext_tap_oracle_oic.health",
        "logger": "flext_tap_oracle_oic.tap",
        "m": ("flext_tap_oracle_oic.models", "FlextTapOracleOicModels"),
        "main": "flext_tap_oracle_oic.cli",
        "models": "flext_tap_oracle_oic.models",
        "p": ("flext_tap_oracle_oic.protocols", "FlextTapOracleOicProtocols"),
        "protocols": "flext_tap_oracle_oic.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "required_fields": "flext_tap_oracle_oic.settings",
        "s": ("flext_core.service", "FlextService"),
        "settings": "flext_tap_oracle_oic.settings",
        "streams": "flext_tap_oracle_oic.streams",
        "t": ("flext_tap_oracle_oic.typings", "FlextTapOracleOicTypes"),
        "tap": "flext_tap_oracle_oic.tap",
        "tap_config": "flext_tap_oracle_oic.settings",
        "tap_streams": "flext_tap_oracle_oic.tap_streams",
        "typings": "flext_tap_oracle_oic.typings",
        "u": ("flext_tap_oracle_oic.utilities", "FlextTapOracleOicUtilities"),
        "utilities": "flext_tap_oracle_oic.utilities",
        "validate_configuration": "flext_tap_oracle_oic.settings",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "__all__",
        "__author__",
        "__author_email__",
        "__description__",
        "__license__",
        "__title__",
        "__url__",
        "__version__",
        "__version_info__",
    ],
)
