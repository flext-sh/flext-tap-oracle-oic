"""FLEXT Oracle Integration Cloud (OIC) Tap for Meltano.

Enterprise Oracle Integration Cloud data extraction with FLEXT ecosystem integration.

SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import importlib.metadata

from flext_core import FlextLogger, FlextModels, FlextResult, FlextTypes
from flext_meltano import FlextMeltanoBridge, FlextMeltanoConfig, FlextMeltanoService
from flext_tap_oracle_oic.config import (
    FlextTapOracleOicConfig,
    create_oracle_oic_tap_config,
)

# Standardized [Project]Models pattern
from flext_tap_oracle_oic.models import FlextTapOracleOicModels
from flext_tap_oracle_oic.simple_api import setup_oic_tap as create_oic_tap
from flext_tap_oracle_oic.tap_client import OracleOICClient, TapOracleOIC
from flext_tap_oracle_oic.tap_exceptions import (
    OICAPIError,
    OICAuthenticationError,
    OICConnectionError,
    OICValidationError,
)
from flext_tap_oracle_oic.tap_streams import OICBaseStream

try:
    # Standardized [Project]Utilities pattern
    from flext_tap_oracle_oic.utilities import FlextTapOracleOicUtilities

    __version__ = importlib.metadata.version("flext-tap-oracle-oic")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())

__all__: FlextTypes.Core.StringList = [
    # FLEXT ecosystem integration
    "FlextLogger",
    # Meltano integration
    "FlextMeltanoBridge",
    "FlextMeltanoConfig",
    "FlextMeltanoService",
    "FlextModels",
    "FlextResult",
    # Configuration
    "FlextTapOracleOicConfig",
    # Standardized [Project]Models pattern
    "FlextTapOracleOicModels",
    "FlextTapOracleOicUtilities",
    "FlextTypes",
    # Exceptions
    "OICAPIError",
    "OICAuthenticationError",
    "OICBaseStream",
    "OICConnectionError",
    "OICValidationError",
    "OracleOICClient",
    # Core tap functionality
    "TapOracleOIC",
    # Version info
    "__version__",
    # API functions
    "create_oic_tap",
    "create_oracle_oic_tap_config",
]
