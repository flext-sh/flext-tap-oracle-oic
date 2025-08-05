"""FLEXT Tap Oracle OIC - Oracle Integration Cloud Data Extraction.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Version 0.9.0 - Tap Oracle OIC with simplified public API:
- All common imports available from root: from flext_tap_oracle_oic import TapOIC
- Built on flext-core foundation for robust Oracle OIC data extraction
- Modern namespace imports from flext-core
"""

from __future__ import annotations

import contextlib
import importlib.metadata

# Import from flext-core for foundational patterns (standardized)
from flext_core import (
    FlextBaseSettings as BaseConfig,
    FlextEntity as DomainEntity,
    FlextFields as Field,
    FlextResult,
    FlextValueObject,
    FlextValueObject as BaseModel,
    FlextValueObject as FlextDomainBaseModel,
)

try:
    __version__ = importlib.metadata.version("flext-tap-oracle-oic")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())


# ================================
# SIMPLIFIED PUBLIC API EXPORTS
# ================================

# Singer Tap exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_tap_oracle_oic.tap import TapOracleOIC

# OIC Client exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_tap_oracle_oic.client import OracleOICClient as OICClient

# OIC Auth exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_tap_oracle_oic.auth import OICOAuth2Authenticator as OICAuthenticator

# OIC Streams exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_tap_oracle_oic.streams import OICBaseStream
    # Stream classes will be implemented as needed for specific OIC integrations
    # ConnectionsStream, IntegrationsStream, LookupsStream, PackagesStream

# Domain entities
with contextlib.suppress(ImportError):
    from flext_tap_oracle_oic.domain.entities import OICIntegration

# Simple API
with contextlib.suppress(ImportError):
    from flext_tap_oracle_oic.simple_api import setup_oic_tap as create_oic_tap

# ================================
# PUBLIC API EXPORTS
# ================================

__all__: list[str] = [
    # Core patterns from flext-core
    "BaseConfig",
    "BaseModel",
    # OIC Streams
    "ConnectionsStream",
    "DomainEntity",
    "Field",
    "FlextDomainBaseModel",
    "FlextResult",
    "FlextValueObject",
    "IntegrationsStream",
    "LookupsStream",
    # OIC Authentication
    "OICAuthenticator",
    "OICBaseStream",
    # OIC Client
    "OICClient",
    # Domain entities
    "OICIntegration",
    "PackagesStream",
    # Main Singer Tap
    "TapOracleOIC",
    # Metadata
    "__version__",
    "__version_info__",
    # Simple API
    "create_oic_tap",
]
