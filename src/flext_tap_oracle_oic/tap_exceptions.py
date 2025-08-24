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
    FlextAuthenticationError,
    FlextConnectionError,
    FlextError,
    FlextValidationError,
)


# Oracle OIC exception factory using standard pattern
class OICExceptionFactory:
    """Factory for Oracle OIC specific exceptions."""

    @staticmethod
    def create_authentication_error(message: str) -> FlextAuthenticationError:
        """Create OIC authentication error."""
        return OICAuthenticationError(message)

    @staticmethod
    def create_connection_error(message: str) -> FlextConnectionError:
        """Create OIC connection error."""
        return OICConnectionError(message)

    @staticmethod
    def create_validation_error(message: str) -> FlextValidationError:
        """Create OIC validation error."""
        return OICValidationError(message)

    @staticmethod
    def create_api_error(message: str) -> FlextError:
        """Create OIC API error."""
        return OICAPIError(message)


# Specific Oracle OIC exceptions
class OICAuthenticationError(FlextAuthenticationError):
    """Oracle OIC authentication error."""


class OICConnectionError(FlextConnectionError):
    """Oracle OIC connection error."""


class OICValidationError(FlextValidationError):
    """Oracle OIC validation error."""


class OICAPIError(FlextError):
    """Oracle OIC API error."""


# Export for backward compatibility and module interface
__all__: list[str] = [
    "FlextAuthenticationError",
    "FlextConnectionError",
    "FlextError",
    "FlextValidationError",
    "OICAPIError",
    "OICAuthenticationError",
    "OICConnectionError",
    "OICExceptionFactory",
    "OICValidationError",
]
