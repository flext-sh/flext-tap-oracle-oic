"""Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from flext_core import FlextTypes

"""Enterprise Singer Tap for Oracle Integration Cloud data extraction.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""


import importlib.metadata

from flext_core import FlextLogger, FlextModels, FlextResult
from flext_meltano import (
    FlextMeltanoBridge,
    FlextMeltanoConfig,
    FlextPropertiesList as PropertiesList,
    FlextTapAbstract as Tap,
    FlextTapStream as Stream,
)

from flext_tap_oracle_oic.tap_client import OracleOICClient, TapOracleOIC
from flext_tap_oracle_oic.tap_config import OICAuthConfig, OICConnectionConfig
from flext_tap_oracle_oic.tap_streams import OICBaseStream

# Aliases for backward compatibility
TapOIC = TapOracleOIC
OICClient = OracleOICClient


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
from flext_tap_oracle_oic.simple_api import setup_oic_tap as create_oic_tap
from flext_tap_oracle_oic.tap_exceptions import (
    OICAPIError,
    OICAuthenticationError,
    OICConnectionError,
    OICValidationError,
)

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
    "FlextLogger",
    "FlextMeltanoBaseService",
    "FlextMeltanoBridge",
    "FlextMeltanoConfig",
    "FlextMeltanoEvent",
    "FlextMeltanoTapService",
    "FlextModels",
    # === FLEXT-CORE RE-EXPORTS ===
    "FlextResult",
    "OAuthAuthenticator",
    "OICAPIError",
    # Configuration classes
    "OICAuthConfig",
    # Exception classes
    "OICAuthenticationError",
    # Stream classes
    "OICBaseStream",
    # === BACKWARD COMPATIBILITY EXPORTS ===
    "OICClient",
    "OICConnectionConfig",
    "OICConnectionError",
    # Model classes
    "OICIntegration",
    "OICPaginator",
    "OICValidationError",
    "OracleOICClient",
    "PropertiesList",
    "Property",
    "SQLSink",
    "Sink",
    "Stream",
    "Tap",
    "TapOIC",
    # === PEP8 REORGANIZED PRIMARY EXPORTS ===
    # Main tap classes
    "TapOracleOIC",
    "Target",
    # === METADATA ===
    "__version__",
    "__version_info__",
    "create_meltano_tap_service",
    # === SIMPLE API ===
    "create_oic_tap",
    "get_tap_test_class",
    "singer_typing",
]

# from . import infrastructure  # Module doesn't exist, commented out
