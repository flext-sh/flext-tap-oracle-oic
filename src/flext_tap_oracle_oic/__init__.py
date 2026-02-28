"""FLEXT Oracle Integration Cloud (OIC) Tap for Meltano.

Enterprise Oracle Integration Cloud data extraction with FLEXT ecosystem integration.

SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from flext_core import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextLogger, FlextModels, FlextResult
    from flext_meltano import (
        FlextMeltanoBridge,
        FlextMeltanoService,
        FlextMeltanoSettings,
    )

    from flext_tap_oracle_oic.__version__ import __version__, __version_info__
    from flext_tap_oracle_oic.constants import (
        FlextMeltanoTapOracleOicConstants,
        FlextMeltanoTapOracleOicConstants as c,
    )
    from flext_tap_oracle_oic.models import (
        FlextMeltanoTapOracleOicModels,
        FlextMeltanoTapOracleOicModels as m,
    )
    from flext_tap_oracle_oic.protocols import FlextMeltanoTapOracleOicProtocols
    from flext_tap_oracle_oic.settings import (
        FlextMeltanoTapOracleOicSettings,
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
    from flext_tap_oracle_oic.typings import t
    from flext_tap_oracle_oic.utilities import (
        FlextMeltanoTapOracleOicUtilities,
        FlextMeltanoTapOracleOicUtilities as u,
    )

# Lazy import mapping: export_name -> (module_path, attr_name)
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextLogger": ("flext_core", "FlextLogger"),
    "FlextMeltanoBridge": ("flext_meltano", "FlextMeltanoBridge"),
    "FlextMeltanoService": ("flext_meltano", "FlextMeltanoService"),
    "FlextMeltanoSettings": ("flext_meltano", "FlextMeltanoSettings"),
    "FlextMeltanoTapOracleOicConstants": (
        "flext_tap_oracle_oic.constants",
        "FlextMeltanoTapOracleOicConstants",
    ),
    "FlextMeltanoTapOracleOicModels": (
        "flext_tap_oracle_oic.models",
        "FlextMeltanoTapOracleOicModels",
    ),
    "FlextMeltanoTapOracleOicProtocols": (
        "flext_tap_oracle_oic.protocols",
        "FlextMeltanoTapOracleOicProtocols",
    ),
    "FlextMeltanoTapOracleOicSettings": (
        "flext_tap_oracle_oic.settings",
        "FlextMeltanoTapOracleOicSettings",
    ),
    "FlextMeltanoTapOracleOicUtilities": (
        "flext_tap_oracle_oic.utilities",
        "FlextMeltanoTapOracleOicUtilities",
    ),
    "u": ("flext_tap_oracle_oic.utilities", "u"),
    "FlextModels": ("flext_core", "FlextModels"),
    "FlextResult": ("flext_core", "FlextResult"),
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
    "c": ("flext_tap_oracle_oic.constants", "FlextMeltanoTapOracleOicConstants"),
    "create_oracle_oic_tap_config": (
        "flext_tap_oracle_oic.settings",
        "create_oracle_oic_tap_config",
    ),
    "m": ("flext_tap_oracle_oic.models", "FlextMeltanoTapOracleOicModels"),
    "t": ("flext_tap_oracle_oic.typings", "t"),
}

__all__ = [
    "FlextLogger",
    "FlextMeltanoBridge",
    "FlextMeltanoService",
    "FlextMeltanoSettings",
    "FlextMeltanoTapOracleOicConstants",
    "FlextMeltanoTapOracleOicModels",
    "FlextMeltanoTapOracleOicProtocols",
    "FlextMeltanoTapOracleOicSettings",
    "FlextMeltanoTapOracleOicUtilities",
    "FlextModels",
    "FlextResult",
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
    "t",
    "u",
]


def __getattr__(name: str) -> Any:  # noqa: ANN401
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
