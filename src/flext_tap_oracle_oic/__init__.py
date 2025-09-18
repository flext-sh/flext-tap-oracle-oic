"""FLEXT Oracle Integration Cloud (OIC) Tap for Meltano.

Enterprise Oracle Integration Cloud data extraction with FLEXT ecosystem integration.

SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import importlib.metadata

from flext_core import FlextLogger, FlextModels, FlextResult, FlextTypes
from flext_meltano import FlextMeltanoBridge, FlextMeltanoConfig, FlextMeltanoService
from flext_tap_oracle_oic.models import OICIntegration
from flext_tap_oracle_oic.simple_api import setup_oic_tap as create_oic_tap
from flext_tap_oracle_oic.tap_client import OracleOICClient, TapOracleOIC
from flext_tap_oracle_oic.tap_config import OICAuthConfig, OICConnectionConfig
from flext_tap_oracle_oic.tap_exceptions import (
    OICAPIError,
    OICAuthenticationError,
    OICConnectionError,
    OICValidationError,
)
from flext_tap_oracle_oic.tap_streams import OICBaseStream

try:
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
    "FlextTypes",
    # Exceptions
    "OICAPIError",
    # Configuration
    "OICAuthConfig",
    "OICAuthenticationError",
    "OICBaseStream",
    "OICConnectionConfig",
    "OICConnectionError",
    # Models
    "OICIntegration",
    "OICValidationError",
    "OracleOICClient",
    # Core tap functionality
    "TapOracleOIC",
    # Version info
    "__version__",
    "__version_info__",
    # API functions
    "create_oic_tap",
]
