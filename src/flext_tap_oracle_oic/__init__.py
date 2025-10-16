"""FLEXT Oracle Integration Cloud (OIC) Tap for Meltano.

Enterprise Oracle Integration Cloud data extraction with FLEXT ecosystem integration.

SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextLogger, FlextModels, FlextResult
from flext_meltano import FlextMeltanoBridge, FlextMeltanoConfig, FlextMeltanoService

from flext_tap_oracle_oic.__version__ import __version__, __version_info__
from flext_tap_oracle_oic.config import (
    FlextMeltanoTapOracleOicConfig,
    create_oracle_oic_tap_config,
)
from flext_tap_oracle_oic.models import FlextMeltanoTapOracleOicModels
from flext_tap_oracle_oic.protocols import FlextMeltanoTapOracleOicProtocols
from flext_tap_oracle_oic.simple_api import setup_oic_tap as create_oic_tap
from flext_tap_oracle_oic.tap_client import OracleOicClient, TapOracleOic
from flext_tap_oracle_oic.tap_exceptions import (
    OICAPIError,
    OICAuthenticationError,
    OICConnectionError,
    OICValidationError,
)
from flext_tap_oracle_oic.tap_streams import OICBaseStream
from flext_tap_oracle_oic.utilities import FlextMeltanoTapOracleOicUtilities

__all__ = [
    "FlextLogger",
    "FlextMeltanoBridge",
    "FlextMeltanoConfig",
    "FlextMeltanoService",
    "FlextMeltanoTapOracleOicConfig",
    "FlextMeltanoTapOracleOicModels",
    "FlextMeltanoTapOracleOicProtocols",
    "FlextMeltanoTapOracleOicUtilities",
    "FlextModels",
    "FlextResult",
    "FlextTypes.Dict",
    "OICAPIError",
    "OICAuthenticationError",
    "OICBaseStream",
    "OICConnectionError",
    "OICValidationError",
    "OracleOicClient",
    "TapOracleOic",
    "__version__",
    "__version_info__",
    "create_oic_tap",
    "create_oracle_oic_tap_config",
]
