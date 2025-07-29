"""Oracle Integration Cloud authentication - Using flext-oracle-oic-ext library.

This module re-exports authentication classes from flext-oracle-oic-ext library
to eliminate code duplication and ensure consistency.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

# Import real implementations from the library
from flext_oracle_oic_ext.oic_patterns import (
    OICAuthConfig,
    OICTapAuthenticator,
)

# Alias for backward compatibility
OICOAuth2Authenticator = OICTapAuthenticator

__all__ = ["OICAuthConfig", "OICOAuth2Authenticator", "OICTapAuthenticator"]
