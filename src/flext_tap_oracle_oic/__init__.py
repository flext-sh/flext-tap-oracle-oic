"""FLEXT Oracle Integration Cloud (OIC) Tap for Meltano.

Enterprise Oracle Integration Cloud data extraction with FLEXT ecosystem integration.

SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import importlib.metadata
from typing import Final

from flext_core import FlextLogger, FlextModels, FlextResult, FlextTypes
from flext_meltano import FlextMeltanoBridge, FlextMeltanoConfig, FlextMeltanoService
from flext_tap_oracle_oic.config import (
    FlextTapOracleOicConfig,
    create_oracle_oic_tap_config,
)
from flext_tap_oracle_oic.models import FlextTapOracleOicModels
from flext_tap_oracle_oic.protocols import FlextTapOracleOicProtocols
from flext_tap_oracle_oic.simple_api import setup_oic_tap as create_oic_tap
from flext_tap_oracle_oic.tap_client import OracleOICClient, TapOracleOIC
from flext_tap_oracle_oic.tap_exceptions import (
    OICAPIError,
    OICAuthenticationError,
    OICConnectionError,
    OICValidationError,
)
from flext_tap_oracle_oic.tap_streams import OICBaseStream
from flext_tap_oracle_oic.version import VERSION, FlextTapOracleOicVersion

try:
    from flext_tap_oracle_oic.utilities import FlextTapOracleOicUtilities

    __version__ = importlib.metadata.version("flext-tap-oracle-oic")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

PROJECT_VERSION: Final[FlextTapOracleOicVersion] = VERSION

__version__: str = VERSION.version
__version_info__: tuple[int | str, ...] = VERSION.version_info

__all__ = [
    "PROJECT_VERSION",
    "VERSION",
    "FlextLogger",
    "FlextMeltanoBridge",
    "FlextMeltanoConfig",
    "FlextMeltanoService",
    "FlextModels",
    "FlextResult",
    "FlextTapOracleOicConfig",
    "FlextTapOracleOicModels",
    "FlextTapOracleOicProtocols",
    "FlextTapOracleOicUtilities",
    "FlextTapOracleOicVersion",
    "FlextTypes",
    "OICAPIError",
    "OICAuthenticationError",
    "OICBaseStream",
    "OICConnectionError",
    "OICValidationError",
    "OracleOICClient",
    "TapOracleOIC",
    "__version__",
    "__version_info__",
    "create_oic_tap",
    "create_oracle_oic_tap_config",
]
