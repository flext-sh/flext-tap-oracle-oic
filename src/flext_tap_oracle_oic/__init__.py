"""Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations
from flext_core import FlextTypes


"""Enterprise Singer Tap for Oracle Integration Cloud data extraction.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""


import contextlib
import importlib.metadata

from flext_core import FlextResult, FlextModels, FlextLogger

from flext_meltano import (
    FlextMeltanoBridge,
    FlextMeltanoConfig,
    FlextMeltanoTypeAdapters,
    FlextTapAbstract as Tap,
    FlextTapStream as Stream,
    FlextSingerTypes,
    FlextPropertiesList as PropertiesList,
    create_flext_tap_config,
)

from flext_tap_oracle_oic.tap_client import TapOracleOIC, OracleOICClient
from flext_tap_oracle_oic.tap_streams import OICBaseStream
from flext_tap_oracle_oic.tap_config import OICAuthConfig, OICConnectionConfig

# Aliases for backward compatibility
TapOIC = TapOracleOIC
OICClient = OracleOICClient  # Alias for OICClient export


# Create a stub OICPaginator if needed by other modules
class OICPaginator:
    """Paginator for OIC API responses."""

    def __init__(self, page_size: int = 100) -> None:
        """Init function.

        Args:
            page_size (int): Description.

        Returns:
            object: Description of return value.

        """
        self.page_size = page_size


from flext_tap_oracle_oic.models import OICIntegration
from flext_tap_oracle_oic.tap_exceptions import (
    OICAuthenticationError,
    OICConnectionError,
    OICValidationError,
    OICAPIError,
)
from flext_tap_oracle_oic.simple_api import setup_oic_tap as create_oic_tap

# === VERSION AND METADATA ===
try:
    __version__ = importlib.metadata.version("flext-tap-oracle-oic")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0-enterprise-pep8-reorganized"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())

# === COMPLETE PUBLIC API EXPORTS ===
__all__: FlextTypes.Core.StringList = [
    # === FLEXT-MELTANO COMPLETE RE-EXPORTS ===
    "BatchSink",
    "FlextMeltanoBaseService",
    "FlextMeltanoBridge",
    "FlextMeltanoConfig",
    "FlextMeltanoEvent",
    "FlextMeltanoTapService",
    "OAuthAuthenticator",
    "PropertiesList",
    "Property",
    "SQLSink",
    "Sink",
    "Stream",
    "Tap",
    "Target",
    "create_meltano_tap_service",
    "get_tap_test_class",
    "singer_typing",
    # === FLEXT-CORE RE-EXPORTS ===
    "FlextResult",
    "FlextModels",
    "FlextLogger",
    # === PEP8 REORGANIZED PRIMARY EXPORTS ===
    # Main tap classes
    "TapOracleOIC",
    "TapOIC",
    "OracleOICClient",
    # Stream classes
    "OICBaseStream",
    "OICPaginator",
    # Configuration classes
    "OICAuthConfig",
    "OICConnectionConfig",
    # Model classes
    "OICIntegration",
    # Exception classes
    "OICAuthenticationError",
    "OICConnectionError",
    "OICValidationError",
    "OICAPIError",
    # === BACKWARD COMPATIBILITY EXPORTS ===
    "OICClient",  # Alias for OracleOICClient
    # === SIMPLE API ===
    "create_oic_tap",
    # === METADATA ===
    "__version__",
    "__version_info__",
]

# from . import infrastructure  # Module doesn't exist, commented out
