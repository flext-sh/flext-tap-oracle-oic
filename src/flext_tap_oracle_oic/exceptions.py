"""Oracle OIC tap exception hierarchy using flext-core patterns.

Copyright (c) 2025 FLEXT Contributors
SPDX-License-Identifier: MIT

Domain-specific exceptions for Oracle OIC tap operations inheriting from flext-core.
"""

from __future__ import annotations

from flext_core.exceptions import (
    FlextAuthenticationError,
    FlextConfigurationError,
    FlextConnectionError,
    FlextError,
    FlextProcessingError,
    FlextTimeoutError,
    FlextValidationError,
)


class FlextTapOracleOicError(FlextError):
    """Base exception for Oracle OIC tap operations."""

    def __init__(
        self,
        message: str = "Oracle OIC tap error",
        integration_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC tap error with context."""
        context = kwargs.copy()
        if integration_name is not None:
            context["integration_name"] = integration_name

        super().__init__(message, error_code="ORACLE_OIC_TAP_ERROR", context=context)


class FlextTapOracleOicConnectionError(FlextConnectionError):
    """Oracle OIC tap connection errors."""

    def __init__(
        self,
        message: str = "Oracle OIC tap connection failed",
        oic_instance: str | None = None,
        endpoint: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC tap connection error with context."""
        context = kwargs.copy()
        if oic_instance is not None:
            context["oic_instance"] = oic_instance
        if endpoint is not None:
            context["endpoint"] = endpoint

        super().__init__(f"Oracle OIC tap connection: {message}", **context)


class FlextTapOracleOicAuthenticationError(FlextAuthenticationError):
    """Oracle OIC tap authentication errors."""

    def __init__(
        self,
        message: str = "Oracle OIC tap authentication failed",
        auth_method: str | None = None,
        username: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC tap authentication error with context."""
        context = kwargs.copy()
        if auth_method is not None:
            context["auth_method"] = auth_method
        if username is not None:
            context["username"] = username

        super().__init__(f"Oracle OIC tap auth: {message}", **context)


class FlextTapOracleOicValidationError(FlextValidationError):
    """Oracle OIC tap validation errors."""

    def __init__(
        self,
        message: str = "Oracle OIC tap validation failed",
        field: str | None = None,
        value: object = None,
        integration_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC tap validation error with context."""
        validation_details = {}
        if field is not None:
            validation_details["field"] = field
        if value is not None:
            validation_details["value"] = str(value)[:100]  # Truncate long values

        context = kwargs.copy()
        if integration_name is not None:
            context["integration_name"] = integration_name

        super().__init__(
            f"Oracle OIC tap validation: {message}",
            validation_details=validation_details,
            context=context,
        )


class FlextTapOracleOicConfigurationError(FlextConfigurationError):
    """Oracle OIC tap configuration errors."""

    def __init__(
        self,
        message: str = "Oracle OIC tap configuration error",
        config_key: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC tap configuration error with context."""
        context = kwargs.copy()
        if config_key is not None:
            context["config_key"] = config_key

        super().__init__(f"Oracle OIC tap config: {message}", **context)


class FlextTapOracleOicProcessingError(FlextProcessingError):
    """Oracle OIC tap processing errors."""

    def __init__(
        self,
        message: str = "Oracle OIC tap processing failed",
        integration_name: str | None = None,
        processing_stage: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC tap processing error with context."""
        context = kwargs.copy()
        if integration_name is not None:
            context["integration_name"] = integration_name
        if processing_stage is not None:
            context["processing_stage"] = processing_stage

        super().__init__(f"Oracle OIC tap processing: {message}", **context)


class FlextTapOracleOicAPIError(FlextTapOracleOicError):
    """Oracle OIC tap API errors."""

    def __init__(
        self,
        message: str = "Oracle OIC tap API error",
        status_code: int | None = None,
        endpoint: str | None = None,
        response_body: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC tap API error with context."""
        context = kwargs.copy()
        if status_code is not None:
            context["status_code"] = status_code
        if endpoint is not None:
            context["endpoint"] = endpoint
        if response_body is not None:
            context["response_body"] = response_body[:300]  # Truncate long responses

        integration_name_obj = context.get("integration_name")
        integration_name_typed = (
            integration_name_obj if isinstance(integration_name_obj, str) else None
        )
        super().__init__(
            f"Oracle OIC tap API: {message}",
            integration_name=integration_name_typed,
            **{k: v for k, v in context.items() if k != "integration_name"},
        )


class FlextTapOracleOicTimeoutError(FlextTimeoutError):
    """Oracle OIC tap timeout errors."""

    def __init__(
        self,
        message: str = "Oracle OIC tap operation timed out",
        operation: str | None = None,
        timeout_seconds: float | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC tap timeout error with context."""
        context = kwargs.copy()
        if operation is not None:
            context["operation"] = operation
        if timeout_seconds is not None:
            context["timeout_seconds"] = timeout_seconds

        super().__init__(f"Oracle OIC tap timeout: {message}", **context)


class FlextTapOracleOicStreamError(FlextTapOracleOicError):
    """Oracle OIC tap stream processing errors."""

    def __init__(
        self,
        message: str = "Oracle OIC tap stream error",
        stream_name: str | None = None,
        integration_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle OIC tap stream error with context."""
        context = kwargs.copy()
        if stream_name is not None:
            context["stream_name"] = stream_name
        if integration_name is not None:
            context["integration_name"] = integration_name

        integration_name_obj = context.get("integration_name")
        integration_name_typed = (
            integration_name_obj if isinstance(integration_name_obj, str) else None
        )
        super().__init__(
            f"Oracle OIC tap stream: {message}",
            integration_name=integration_name_typed,
            **{k: v for k, v in context.items() if k != "integration_name"},
        )


__all__: list[str] = [
    "FlextTapOracleOicAPIError",
    "FlextTapOracleOicAuthenticationError",
    "FlextTapOracleOicConfigurationError",
    "FlextTapOracleOicConnectionError",
    "FlextTapOracleOicError",
    "FlextTapOracleOicProcessingError",
    "FlextTapOracleOicStreamError",
    "FlextTapOracleOicTimeoutError",
    "FlextTapOracleOicValidationError",
]
