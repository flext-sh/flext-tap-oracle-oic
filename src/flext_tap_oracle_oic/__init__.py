# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext tap oracle oic package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
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

if TYPE_CHECKING:
    from flext_meltano import *

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
    from flext_tap_oracle_oic._models.streams import *
    from flext_tap_oracle_oic.cli import *
    from flext_tap_oracle_oic.constants import *
    from flext_tap_oracle_oic.errors import *
    from flext_tap_oracle_oic.health import *
    from flext_tap_oracle_oic.models import *
    from flext_tap_oracle_oic.protocols import *
    from flext_tap_oracle_oic.settings import *
    from flext_tap_oracle_oic.tap import *
    from flext_tap_oracle_oic.tap_streams import *
    from flext_tap_oracle_oic.typings import *
    from flext_tap_oracle_oic.utilities import *

from flext_tap_oracle_oic._models import _LAZY_IMPORTS as __MODELS_LAZY

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    **__MODELS_LAZY,
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
    "FlextTapOracleOicSettings": "flext_tap_oracle_oic.settings",
    "FlextTapOracleOicTypes": "flext_tap_oracle_oic.typings",
    "FlextTapOracleOicUtilities": "flext_tap_oracle_oic.utilities",
    "FlextTapOracleOicValidationError": "flext_tap_oracle_oic.errors",
    "_models": "flext_tap_oracle_oic._models",
    "c": ["flext_tap_oracle_oic.constants", "FlextTapOracleOicConstants"],
    "cli": "flext_tap_oracle_oic.cli",
    "constants": "flext_tap_oracle_oic.constants",
    "d": "flext_meltano",
    "e": "flext_meltano",
    "errors": "flext_tap_oracle_oic.errors",
    "flext_tap_oracle_oic_create_config": "flext_tap_oracle_oic.settings",
    "h": "flext_meltano",
    "health": "flext_tap_oracle_oic.health",
    "logger": "flext_tap_oracle_oic.tap",
    "m": ["flext_tap_oracle_oic.models", "FlextTapOracleOicModels"],
    "main": "flext_tap_oracle_oic.cli",
    "models": "flext_tap_oracle_oic.models",
    "p": ["flext_tap_oracle_oic.protocols", "FlextTapOracleOicProtocols"],
    "protocols": "flext_tap_oracle_oic.protocols",
    "r": "flext_meltano",
    "s": "flext_meltano",
    "settings": "flext_tap_oracle_oic.settings",
    "t": ["flext_tap_oracle_oic.typings", "FlextTapOracleOicTypes"],
    "tap": "flext_tap_oracle_oic.tap",
    "tap_streams": "flext_tap_oracle_oic.tap_streams",
    "typings": "flext_tap_oracle_oic.typings",
    "u": ["flext_tap_oracle_oic.utilities", "FlextTapOracleOicUtilities"],
    "utilities": "flext_tap_oracle_oic.utilities",
    "validate_configuration": "flext_tap_oracle_oic.settings",
    "x": "flext_meltano",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, sorted(_LAZY_IMPORTS))
