# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext tap oracle oic package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

from flext_tap_oracle_oic.__version__ import (
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
    from flext_meltano import d, e, h, r, s, x

    from flext_tap_oracle_oic import (
        _models as _models,
        cli as cli,
        constants as constants,
        errors as errors,
        health as health,
        models as models,
        protocols as protocols,
        settings as settings,
        tap as tap,
        tap_streams as tap_streams,
        typings as typings,
        utilities as utilities,
    )
    from flext_tap_oracle_oic._models import streams as streams
    from flext_tap_oracle_oic._models.streams import (
        ALL_STREAMS as ALL_STREAMS,
        CORE_STREAMS as CORE_STREAMS,
        EXTENDED_STREAMS as EXTENDED_STREAMS,
        INFRASTRUCTURE_STREAMS as INFRASTRUCTURE_STREAMS,
        MONITORING_STREAMS as MONITORING_STREAMS,
        FlextTapOracleOicModelsStreams as FlextTapOracleOicModelsStreams,
        th as th,
    )
    from flext_tap_oracle_oic.cli import main as main
    from flext_tap_oracle_oic.constants import (
        FlextTapOracleOicConstants as FlextTapOracleOicConstants,
        FlextTapOracleOicConstants as c,
    )
    from flext_tap_oracle_oic.errors import (
        FlextTapOracleOicApiError as FlextTapOracleOicApiError,
        FlextTapOracleOicAuthenticationError as FlextTapOracleOicAuthenticationError,
        FlextTapOracleOicConnectionError as FlextTapOracleOicConnectionError,
        FlextTapOracleOicExceptionFactory as FlextTapOracleOicExceptionFactory,
        FlextTapOracleOicValidationError as FlextTapOracleOicValidationError,
    )
    from flext_tap_oracle_oic.health import (
        FlextTapOracleOicHealthChecker as FlextTapOracleOicHealthChecker,
    )
    from flext_tap_oracle_oic.models import (
        FlextTapOracleOicModels as FlextTapOracleOicModels,
        FlextTapOracleOicModels as m,
    )
    from flext_tap_oracle_oic.protocols import (
        FlextTapOracleOicProtocols as FlextTapOracleOicProtocols,
        FlextTapOracleOicProtocols as p,
    )
    from flext_tap_oracle_oic.settings import (
        FlextTapOracleOicSettings as FlextTapOracleOicSettings,
        flext_tap_oracle_oic_create_config as flext_tap_oracle_oic_create_config,
        validate_configuration as validate_configuration,
    )
    from flext_tap_oracle_oic.tap import (
        FlextOracleOicAuthenticator as FlextOracleOicAuthenticator,
        FlextTapOracleOic as FlextTapOracleOic,
        FlextTapOracleOicClient as FlextTapOracleOicClient,
        logger as logger,
    )
    from flext_tap_oracle_oic.tap_streams import (
        FlextTapOracleOicPaginator as FlextTapOracleOicPaginator,
    )
    from flext_tap_oracle_oic.typings import (
        FlextTapOracleOicTypes as FlextTapOracleOicTypes,
        FlextTapOracleOicTypes as t,
    )
    from flext_tap_oracle_oic.utilities import (
        FlextTapOracleOicUtilities as FlextTapOracleOicUtilities,
        FlextTapOracleOicUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "ALL_STREAMS": ["flext_tap_oracle_oic._models.streams", "ALL_STREAMS"],
    "CORE_STREAMS": ["flext_tap_oracle_oic._models.streams", "CORE_STREAMS"],
    "EXTENDED_STREAMS": ["flext_tap_oracle_oic._models.streams", "EXTENDED_STREAMS"],
    "FlextOracleOicAuthenticator": ["flext_tap_oracle_oic.tap", "FlextOracleOicAuthenticator"],
    "FlextTapOracleOic": ["flext_tap_oracle_oic.tap", "FlextTapOracleOic"],
    "FlextTapOracleOicApiError": ["flext_tap_oracle_oic.errors", "FlextTapOracleOicApiError"],
    "FlextTapOracleOicAuthenticationError": ["flext_tap_oracle_oic.errors", "FlextTapOracleOicAuthenticationError"],
    "FlextTapOracleOicClient": ["flext_tap_oracle_oic.tap", "FlextTapOracleOicClient"],
    "FlextTapOracleOicConnectionError": ["flext_tap_oracle_oic.errors", "FlextTapOracleOicConnectionError"],
    "FlextTapOracleOicConstants": ["flext_tap_oracle_oic.constants", "FlextTapOracleOicConstants"],
    "FlextTapOracleOicExceptionFactory": ["flext_tap_oracle_oic.errors", "FlextTapOracleOicExceptionFactory"],
    "FlextTapOracleOicHealthChecker": ["flext_tap_oracle_oic.health", "FlextTapOracleOicHealthChecker"],
    "FlextTapOracleOicModels": ["flext_tap_oracle_oic.models", "FlextTapOracleOicModels"],
    "FlextTapOracleOicModelsStreams": ["flext_tap_oracle_oic._models.streams", "FlextTapOracleOicModelsStreams"],
    "FlextTapOracleOicPaginator": ["flext_tap_oracle_oic.tap_streams", "FlextTapOracleOicPaginator"],
    "FlextTapOracleOicProtocols": ["flext_tap_oracle_oic.protocols", "FlextTapOracleOicProtocols"],
    "FlextTapOracleOicSettings": ["flext_tap_oracle_oic.settings", "FlextTapOracleOicSettings"],
    "FlextTapOracleOicTypes": ["flext_tap_oracle_oic.typings", "FlextTapOracleOicTypes"],
    "FlextTapOracleOicUtilities": ["flext_tap_oracle_oic.utilities", "FlextTapOracleOicUtilities"],
    "FlextTapOracleOicValidationError": ["flext_tap_oracle_oic.errors", "FlextTapOracleOicValidationError"],
    "INFRASTRUCTURE_STREAMS": ["flext_tap_oracle_oic._models.streams", "INFRASTRUCTURE_STREAMS"],
    "MONITORING_STREAMS": ["flext_tap_oracle_oic._models.streams", "MONITORING_STREAMS"],
    "_models": ["flext_tap_oracle_oic._models", ""],
    "c": ["flext_tap_oracle_oic.constants", "FlextTapOracleOicConstants"],
    "cli": ["flext_tap_oracle_oic.cli", ""],
    "constants": ["flext_tap_oracle_oic.constants", ""],
    "d": ["flext_meltano", "d"],
    "e": ["flext_meltano", "e"],
    "errors": ["flext_tap_oracle_oic.errors", ""],
    "flext_tap_oracle_oic_create_config": ["flext_tap_oracle_oic.settings", "flext_tap_oracle_oic_create_config"],
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
    "validate_configuration": ["flext_tap_oracle_oic.settings", "validate_configuration"],
    "x": ["flext_meltano", "x"],
}

_EXPORTS: Sequence[str] = [
    "ALL_STREAMS",
    "CORE_STREAMS",
    "EXTENDED_STREAMS",
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
    "INFRASTRUCTURE_STREAMS",
    "MONITORING_STREAMS",
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
