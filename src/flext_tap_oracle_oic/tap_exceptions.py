"""Oracle Integration Cloud tap exceptions - PEP8 reorganized.

This module consolidates ALL exception handling using flext-core factory patterns:
- Standard exception hierarchy using flext-core.exceptions
- Oracle OIC specific exceptions with detailed error context
- Error factory patterns for consistent error handling
- Integration with flext-core logging and error tracking

Design: Uses flext-core exception factory patterns:
- flext-core.exceptions: Base exception classes and factory
- Custom OIC exceptions: Domain-specific error handling
- Error context: Rich error information for debugging
- Logging integration: Automatic error logging and tracking

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import (
    FlextExceptions.AuthenticationError,
    FlextExceptions.ConnectionError,
    FlextExceptions.Error,
    FlextExceptions.ValidationError,
)


# Oracle OIC exception factory using standard pattern
class OICExceptionFactory:
    """Factory for Oracle OIC specific exceptions."""

    @staticmethod
    def create_authentication_error(message: str) -> FlextExceptions.AuthenticationError:
        """Create OIC authentication error."""
        return OICAuthenticationError(message)

    @staticmethod
    def create_connection_error(message: str) -> FlextExceptions.ConnectionError:
        """Create OIC connection error."""
        return OICConnectionError(message)

    @staticmethod
    def create_validation_error(message: str) -> FlextExceptions.ValidationError:
        """Create OIC validation error."""
        return OICValidationError(message)

    @staticmethod
    def create_api_error(message: str) -> FlextExceptions.Error:
        """Create OIC API error."""
        return OICAPIError(message)


# Specific Oracle OIC exceptions
class OICAuthenticationError(FlextExceptions.AuthenticationError):
    """Oracle OIC authentication error."""


class OICConnectionError(FlextExceptions.ConnectionError):
    """Oracle OIC connection error."""


class OICValidationError(FlextExceptions.ValidationError):
    """Oracle OIC validation error."""


class OICAPIError(FlextExceptions.Error):
    """Oracle OIC API error."""


# Export for backward compatibility and module interface
__all__: list[str] = [
    "FlextExceptions.AuthenticationError",
    "FlextExceptions.ConnectionError",
    "FlextExceptions.Error",
    "FlextExceptions.ValidationError",
    "OICAPIError",
    "OICAuthenticationError",
    "OICConnectionError",
    "OICExceptionFactory",
    "OICValidationError",
]
