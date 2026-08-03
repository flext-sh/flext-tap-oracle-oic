"""Oracle Integration Cloud tap exceptions.

This module consolidates ALL exception handling using flext-core factory patterns:
- Standard exception hierarchy using flext-core.exceptions
- Oracle OIC specific exceptions with detailed error context
- Error factory patterns for consistent error handling
- Integration with flext-core logging and error tracking

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from flext_tap_oracle_oic import e, t


class FlextTapOracleOicAuthenticationError(e.AuthenticationError):
    """Oracle OIC authentication error."""


class FlextTapOracleOicConnectionError(e.FlextConnectionError):
    """Oracle OIC connection error."""


class FlextTapOracleOicValidationError(e.ValidationError):
    """Oracle OIC validation error."""


class FlextTapOracleOicApiError(e.OperationError):
    """Oracle OIC API error."""


__all__: t.StrSequence = (
    "FlextTapOracleOicApiError",
    "FlextTapOracleOicAuthenticationError",
    "FlextTapOracleOicConnectionError",
    "FlextTapOracleOicValidationError",
)
