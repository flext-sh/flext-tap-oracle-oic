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

from flext_core import FlextExceptions

from flext_tap_oracle_oic import t


class FlextTapOracleOicExceptionFactory:
    """Factory for Oracle OIC specific exceptions."""

    @staticmethod
    def create_api_error(message: str) -> FlextTapOracleOicApiError:
        """Create OIC API error."""
        return FlextTapOracleOicApiError(message)

    @staticmethod
    def create_authentication_error(
        message: str,
    ) -> FlextTapOracleOicAuthenticationError:
        """Create OIC authentication error."""
        return FlextTapOracleOicAuthenticationError(message)

    @staticmethod
    def create_connection_error(message: str) -> FlextTapOracleOicConnectionError:
        """Create OIC connection error."""
        return FlextTapOracleOicConnectionError(message)

    @staticmethod
    def create_validation_error(message: str) -> FlextTapOracleOicValidationError:
        """Create OIC validation error."""
        return FlextTapOracleOicValidationError(message)


class FlextTapOracleOicAuthenticationError(FlextExceptions.AuthenticationError):
    """Oracle OIC authentication error."""


class FlextTapOracleOicConnectionError(FlextExceptions.ConnectionError):
    """Oracle OIC connection error."""


class FlextTapOracleOicValidationError(FlextExceptions.ValidationError):
    """Oracle OIC validation error."""


class FlextTapOracleOicApiError(FlextExceptions.OperationError):
    """Oracle OIC API error."""


__all__: t.StrSequence = [
    "FlextTapOracleOicApiError",
    "FlextTapOracleOicAuthenticationError",
    "FlextTapOracleOicConnectionError",
    "FlextTapOracleOicExceptionFactory",
    "FlextTapOracleOicValidationError",
]
