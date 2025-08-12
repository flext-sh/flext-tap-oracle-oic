"""Configuration patterns for Oracle Integration Cloud tap - PEP8 reorganized.

This module consolidates ALL configuration-related functionality using flext-core patterns:
- OAuth2/IDCS authentication configuration with flext-oracle-oic-ext integration
- Connection parameters and performance tuning with flext-core validation
- Stream selection and filtering using value object patterns
- Discovery and extraction configuration with enterprise patterns

Design: Uses composition over inheritance, integrating:
- flext-core: FlextSettings, FlextValueObject for configuration patterns
- flext-oracle-oic-ext: OICAuthConfig, OICConnectionConfig for Oracle specifics
- Standard Python: Pydantic for validation and environment integration

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

# flext-core foundation
from flext_core import FlextSettings, get_logger

# flext-oracle-oic-ext integration (avoid duplication)
from flext_oracle_oic_ext import (
    OICAuthConfig,
    OICConnectionConfig,
)

# Re-export for backward compatibility
__all__: list[str] = [
    "FlextSettings",
    "OICAuthConfig",
    "OICConnectionConfig",
    "get_logger",
]
