# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext tap oracle oic package."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

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
    from flext_core import FlextTypes
    from flext_meltano import d, e, h, r, s, x

    from flext_tap_oracle_oic import (
        _models,
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
    from flext_tap_oracle_oic._models import streams
    from flext_tap_oracle_oic._models.streams import (
        ALL_STREAMS,
        CORE_STREAMS,
        EXTENDED_STREAMS,
        INFRASTRUCTURE_STREAMS,
        MONITORING_STREAMS,
        FlextTapOracleOicModelsStreams,
        th,
    )
    from flext_tap_oracle_oic.cli import main
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
    from flext_tap_oracle_oic.settings import (
        FlextTapOracleOicSettings,
        flext_tap_oracle_oic_create_config,
        validate_configuration,
    )
    from flext_tap_oracle_oic.tap import (
        FlextOracleOicAuthenticator,
        FlextTapOracleOic,
        FlextTapOracleOicClient,
        logger,
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

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "ALL_STREAMS": ["flext_tap_oracle_oic._models.streams", "ALL_STREAMS"],
    "CORE_STREAMS": ["flext_tap_oracle_oic._models.streams", "CORE_STREAMS"],
    "EXTENDED_STREAMS": ["flext_tap_oracle_oic._models.streams", "EXTENDED_STREAMS"],
    "FlextOracleOicAuthenticator": [
        "flext_tap_oracle_oic.tap",
        "FlextOracleOicAuthenticator",
    ],
    "FlextTapOracleOic": ["flext_tap_oracle_oic.tap", "FlextTapOracleOic"],
    "FlextTapOracleOicApiError": [
        "flext_tap_oracle_oic.errors",
        "FlextTapOracleOicApiError",
    ],
    "FlextTapOracleOicAuthenticationError": [
        "flext_tap_oracle_oic.errors",
        "FlextTapOracleOicAuthenticationError",
    ],
    "FlextTapOracleOicClient": ["flext_tap_oracle_oic.tap", "FlextTapOracleOicClient"],
    "FlextTapOracleOicConnectionError": [
        "flext_tap_oracle_oic.errors",
        "FlextTapOracleOicConnectionError",
    ],
    "FlextTapOracleOicConstants": [
        "flext_tap_oracle_oic.constants",
        "FlextTapOracleOicConstants",
    ],
    "FlextTapOracleOicExceptionFactory": [
        "flext_tap_oracle_oic.errors",
        "FlextTapOracleOicExceptionFactory",
    ],
    "FlextTapOracleOicHealthChecker": [
        "flext_tap_oracle_oic.health",
        "FlextTapOracleOicHealthChecker",
    ],
    "FlextTapOracleOicModels": [
        "flext_tap_oracle_oic.models",
        "FlextTapOracleOicModels",
    ],
    "FlextTapOracleOicModelsStreams": [
        "flext_tap_oracle_oic._models.streams",
        "FlextTapOracleOicModelsStreams",
    ],
    "FlextTapOracleOicPaginator": [
        "flext_tap_oracle_oic.tap_streams",
        "FlextTapOracleOicPaginator",
    ],
    "FlextTapOracleOicProtocols": [
        "flext_tap_oracle_oic.protocols",
        "FlextTapOracleOicProtocols",
    ],
    "FlextTapOracleOicSettings": [
        "flext_tap_oracle_oic.settings",
        "FlextTapOracleOicSettings",
    ],
    "FlextTapOracleOicTypes": [
        "flext_tap_oracle_oic.typings",
        "FlextTapOracleOicTypes",
    ],
    "FlextTapOracleOicUtilities": [
        "flext_tap_oracle_oic.utilities",
        "FlextTapOracleOicUtilities",
    ],
    "FlextTapOracleOicValidationError": [
        "flext_tap_oracle_oic.errors",
        "FlextTapOracleOicValidationError",
    ],
    "INFRASTRUCTURE_STREAMS": [
        "flext_tap_oracle_oic._models.streams",
        "INFRASTRUCTURE_STREAMS",
    ],
    "MONITORING_STREAMS": [
        "flext_tap_oracle_oic._models.streams",
        "MONITORING_STREAMS",
    ],
    "_models": ["flext_tap_oracle_oic._models", ""],
    "c": ["flext_tap_oracle_oic.constants", "FlextTapOracleOicConstants"],
    "cli": ["flext_tap_oracle_oic.cli", ""],
    "constants": ["flext_tap_oracle_oic.constants", ""],
    "d": ["flext_meltano", "d"],
    "e": ["flext_meltano", "e"],
    "errors": ["flext_tap_oracle_oic.errors", ""],
    "flext_tap_oracle_oic_create_config": [
        "flext_tap_oracle_oic.settings",
        "flext_tap_oracle_oic_create_config",
    ],
    "h": ["flext_meltano", "h"],
    "health": ["flext_tap_oracle_oic.health", ""],
    "logger": ["flext_tap_oracle_oic.tap", "logger"],
    "m": ["flext_tap_oracle_oic.models", "FlextTapOracleOicModels"],
    "main": ["flext_tap_oracle_oic.cli", "main"],
    "models": ["flext_tap_oracle_oic.models", ""],
    "p": ["flext_tap_oracle_oic.protocols", "FlextTapOracleOicProtocols"],
    "protocols": ["flext_tap_oracle_oic.protocols", ""],
    "r": ["flext_meltano", "r"],
    "s": ["flext_meltano", "s"],
    "settings": ["flext_tap_oracle_oic.settings", ""],
    "streams": ["flext_tap_oracle_oic._models.streams", ""],
    "t": ["flext_tap_oracle_oic.typings", "FlextTapOracleOicTypes"],
    "tap": ["flext_tap_oracle_oic.tap", ""],
    "tap_streams": ["flext_tap_oracle_oic.tap_streams", ""],
    "th": ["flext_tap_oracle_oic._models.streams", "th"],
    "typings": ["flext_tap_oracle_oic.typings", ""],
    "u": ["flext_tap_oracle_oic.utilities", "FlextTapOracleOicUtilities"],
    "utilities": ["flext_tap_oracle_oic.utilities", ""],
    "validate_configuration": [
        "flext_tap_oracle_oic.settings",
        "validate_configuration",
    ],
    "x": ["flext_meltano", "x"],
}

__all__ = [
    "ALL_STREAMS",
    "CORE_STREAMS",
    "EXTENDED_STREAMS",
    "INFRASTRUCTURE_STREAMS",
    "MONITORING_STREAMS",
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


_LAZY_CACHE: MutableMapping[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> Sequence[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
