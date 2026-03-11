"""FLEXT Oracle Integration Cloud (OIC) Tap for Meltano.

Enterprise Oracle Integration Cloud data extraction with FLEXT ecosystem integration.

SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextLogger, FlextModels, r
    from flext_meltano import (
        FlextMeltanoBridge,
        FlextMeltanoService,
        FlextMeltanoSettings,
    )

    from flext_tap_oracle_oic.__version__ import __version__, __version_info__
    from flext_tap_oracle_oic.constants import (
        FlextTapOracleOicConstants,
        FlextTapOracleOicConstants as c,
    )
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
        create_oracle_oic_tap_config,
    )
    from flext_tap_oracle_oic.tap_client import OracleOicClient, TapOracleOic
    from flext_tap_oracle_oic.tap_exceptions import (
        OICAPIError,
        OICAuthenticationError,
        OICConnectionError,
        OICValidationError,
    )
    from flext_tap_oracle_oic.tap_streams import OICBaseStream
    from flext_tap_oracle_oic.typings import (
        FlextTapOracleOicTypes,
        FlextTapOracleOicTypes as t,
    )
    from flext_tap_oracle_oic.utilities import (
        FlextTapOracleOicUtilities,
        FlextTapOracleOicUtilities as u,
    )

# Lazy import mapping: export_name -> (module_path, attr_name)
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextLogger": ("flext_core", "FlextLogger"),
    "FlextMeltanoBridge": ("flext_meltano", "FlextMeltanoBridge"),
    "FlextMeltanoService": ("flext_meltano", "FlextMeltanoService"),
    "FlextMeltanoSettings": ("flext_meltano", "FlextMeltanoSettings"),
    "FlextModels": ("flext_core", "FlextModels"),
    "r": ("flext_core", "r"),
    "FlextTapOracleOicConstants": (
        "flext_tap_oracle_oic.constants",
        "FlextTapOracleOicConstants",
    ),
    "FlextTapOracleOicModels": (
        "flext_tap_oracle_oic.models",
        "FlextTapOracleOicModels",
    ),
    "FlextTapOracleOicProtocols": (
        "flext_tap_oracle_oic.protocols",
        "FlextTapOracleOicProtocols",
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
    "OICAPIError": ("flext_tap_oracle_oic.tap_exceptions", "OICAPIError"),
    "OICAuthenticationError": (
        "flext_tap_oracle_oic.tap_exceptions",
        "OICAuthenticationError",
    ),
    "OICBaseStream": ("flext_tap_oracle_oic.tap_streams", "OICBaseStream"),
    "OICConnectionError": ("flext_tap_oracle_oic.tap_exceptions", "OICConnectionError"),
    "OICValidationError": ("flext_tap_oracle_oic.tap_exceptions", "OICValidationError"),
    "OracleOicClient": ("flext_tap_oracle_oic.tap_client", "OracleOicClient"),
    "TapOracleOic": ("flext_tap_oracle_oic.tap_client", "TapOracleOic"),
    "__version__": ("flext_tap_oracle_oic.__version__", "__version__"),
    "__version_info__": ("flext_tap_oracle_oic.__version__", "__version_info__"),
    "c": ("flext_tap_oracle_oic.constants", "FlextTapOracleOicConstants"),
    "create_oracle_oic_tap_config": (
        "flext_tap_oracle_oic.settings",
        "create_oracle_oic_tap_config",
    ),
    "m": ("flext_tap_oracle_oic.models", "FlextTapOracleOicModels"),
    "p": ("flext_tap_oracle_oic.protocols", "FlextTapOracleOicProtocols"),
    "t": ("flext_tap_oracle_oic.typings", "FlextTapOracleOicTypes"),
    "u": ("flext_tap_oracle_oic.utilities", "FlextTapOracleOicUtilities"),
}

__all__ = [
    "FlextLogger",
    "FlextMeltanoBridge",
    "FlextMeltanoService",
    "FlextMeltanoSettings",
    "FlextModels",
    "FlextTapOracleOicConstants",
    "FlextTapOracleOicModels",
    "FlextTapOracleOicProtocols",
    "FlextTapOracleOicSettings",
    "FlextTapOracleOicTypes",
    "FlextTapOracleOicUtilities",
    "OICAPIError",
    "OICAuthenticationError",
    "OICBaseStream",
    "OICConnectionError",
    "OICValidationError",
    "OracleOicClient",
    "TapOracleOic",
    "__version__",
    "__version_info__",
    "c",
    "create_oracle_oic_tap_config",
    "m",
    "p",
    "r",
    "t",
    "u",
]


def __getattr__(
    name: str,
) -> Any:  # JUSTIFIED: Ruff (any-type) with PEP 562 dynamic module exports — https://docs.astral.sh/ruff/rules/any-type/
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
