"""FLEXT Tap Oracle OIC - Oracle Integration Cloud Data Extraction with simplified imports.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Version 0.7.0 - Tap Oracle OIC with simplified public API:
- All common imports available from root: from flext_tap_oracle_oic import TapOIC
- Built on flext-core foundation for robust Oracle OIC data extraction
- Deprecation warnings for internal imports
"""

from __future__ import annotations

import contextlib
import importlib.metadata
import warnings

# Foundation patterns - ALWAYS from flext-core
# 🚨 ARCHITECTURAL COMPLIANCE
from flext_tap_oracle_oic.infrastructure.di_container import get_service_result, get_domain_entity, get_field
ServiceResult = get_service_result()
DomainEntity = get_domain_entity()
Field = get_field()
    BaseConfig as OICBaseConfig,  # Configuration base
    DomainBaseModel as BaseModel,  # Base for OIC models
    DomainError as OICError,  # OIC-specific errors
    ServiceResult,  # OIC operation results
    ValidationError,  # Validation errors
)

try:
    __version__ = importlib.metadata.version("flext-tap-oracle-oic")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.7.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())


class FlextTapOracleOicDeprecationWarning(DeprecationWarning):
    """Custom deprecation warning for FLEXT TAP ORACLE OIC import changes."""


def _show_deprecation_warning(old_import: str, new_import: str) -> None:
    """Show deprecation warning for import paths."""
    message_parts = [
        f"⚠️  DEPRECATED IMPORT: {old_import}",
        f"✅ USE INSTEAD: {new_import}",
        "🔗 This will be removed in version 1.0.0",
        "📖 See FLEXT TAP ORACLE OIC docs for migration guide",
    ]
    warnings.warn(
        "\n".join(message_parts),
        FlextTapOracleOicDeprecationWarning,
        stacklevel=3,
    )


# ================================
# SIMPLIFIED PUBLIC API EXPORTS
# ================================

# Foundation patterns - imported at top of file

# Singer Tap exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_tap_oracle_oic.tap import TapOIC

# OIC Client exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_tap_oracle_oic.client import (
        OICAuthenticator,
        OICClient,
    )

# OIC Streams exports - simplified imports
with contextlib.suppress(ImportError):
    from flext_tap_oracle_oic.streams import (
        ConnectionsStream,
        IntegrationsStream,
        LookupsStream,
        PackagesStream,
    )

# ================================
# PUBLIC API EXPORTS
# ================================

__all__ = [
    "BaseModel",  # from flext_tap_oracle_oic import BaseModel
    # OIC Streams (simplified access)
    "ConnectionsStream",  # from flext_tap_oracle_oic import ConnectionsStream
    # Deprecation utilities
    "FlextTapOracleOicDeprecationWarning",
    # OIC Streams (simplified access)
    "IntegrationsStream",  # from flext_tap_oracle_oic import IntegrationsStream
    "LookupsStream",  # from flext_tap_oracle_oic import LookupsStream
    # OIC Authentication (simplified access)
    "OICAuthenticator",  # from flext_tap_oracle_oic import OICAuthenticator
    # Core Patterns (from flext-core)
    "OICBaseConfig",  # from flext_tap_oracle_oic import OICBaseConfig
    # OIC Client (simplified access)
    "OICClient",  # from flext_tap_oracle_oic import OICClient
    "OICError",  # from flext_tap_oracle_oic import OICError
    "PackagesStream",  # from flext_tap_oracle_oic import PackagesStream
    "ServiceResult",  # from flext_tap_oracle_oic import ServiceResult
    # Main Singer Tap (simplified access)
    "TapOIC",  # from flext_tap_oracle_oic import TapOIC
    "ValidationError",  # from flext_tap_oracle_oic import ValidationError
    # Version
    "__version__",
    "__version_info__",
]
