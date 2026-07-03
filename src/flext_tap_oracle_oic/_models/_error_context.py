"""OIC OicErrorContext model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, ClassVar, Self

from flext_meltano import FlextMeltanoModels
from flext_tap_oracle_oic import c, t, u


class OicErrorContext(FlextMeltanoModels.Entity):
    """Error context for OIC API error handling."""

    # Pydantic 2.11 Configuration - Error Context Features
    model_config: ClassVar[FlextMeltanoModels.ConfigDict] = (
        FlextMeltanoModels.ConfigDict(
            json_schema_extra={
                "description": "Oracle OIC API error context with recovery guidance",
                "examples": [
                    {
                        "error_type": "RATE_LIMIT",
                        "http_status_code": 429,
                        "retry_after_seconds": 60,
                        "is_retryable": True,
                    },
                ],
            },
        )
    )

    error_type: Annotated[
        c.TapOracleOic.OicErrorType,
        u.Field(..., description="Error category"),
    ]
    http_status_code: Annotated[
        int | None,
        u.Field(None, description="HTTP status code"),
    ]
    retry_after_seconds: Annotated[
        int | None,
        u.Field(
            None,
            description="Retry after duration",
        ),
    ]

    # Context information
    endpoint: Annotated[
        str | None,
        u.Field(None, description="API endpoint that failed"),
    ]
    request_method: Annotated[
        str | None,
        u.Field(None, description="HTTP method used"),
    ]
    request_params: Annotated[
        t.MappingKV[str, t.JsonMapping] | None,
        u.Field(
            None,
            description="Request parameters",
        ),
    ]

    # Recovery information
    is_retryable: Annotated[
        bool,
        u.Field(
            description="Whether error is retryable",
        ),
    ] = False
    suggested_action: Annotated[
        str | None,
        u.Field(
            None,
            description="Suggested recovery action",
        ),
    ]
    max_retry_attempts: Annotated[
        int | None,
        u.Field(
            None,
            description="Maximum retry attempts for this error",
        ),
    ]

    @u.computed_field()
    @property
    def error_context_summary(
        self,
    ) -> t.TapOracleOic.SectionedSummary:
        """OIC error context summary."""
        return {
            "error_classification": {
                "type": self.error_type,
                "http_status": self.http_status_code,
                "is_retryable": self.is_retryable,
                "severity": self._determine_severity(),
            },
            "request_context": {
                "endpoint": self.endpoint,
                "method": self.request_method,
                "has_params": bool(self.request_params),
            },
            "recovery_guidance": {
                "suggested_action": self.suggested_action,
                "retry_after_seconds": self.retry_after_seconds,
                "max_retry_attempts": self.max_retry_attempts,
                "auto_recoverable": self.is_retryable
                and bool(self.retry_after_seconds),
            },
        }

    @u.model_validator(mode="after")
    def validate_error_context(self) -> Self:
        """Validate OIC error context."""
        if self.http_status_code is not None and not (
            c.HTTP_STATUS_MIN <= self.http_status_code <= c.HTTP_STATUS_MAX
        ):
            msg = "HTTP status code must be between 100 and 599"
            raise ValueError(msg)
        if self.retry_after_seconds is not None and self.retry_after_seconds < 0:
            msg = "Retry after seconds cannot be negative"
            raise ValueError(msg)
        return self

    def _determine_severity(self) -> str:
        """Determine error severity based on type and status code."""
        if self.error_type in {
            c.TapOracleOic.OicErrorType.AUTHENTICATION,
            c.TapOracleOic.OicErrorType.AUTHORIZATION,
        }:
            return str(c.TapOracleOic.OicErrorSeverity.CRITICAL.value)
        if self.error_type == c.TapOracleOic.OicErrorType.RATE_LIMIT:
            return str(c.TapOracleOic.OicErrorSeverity.WARNING.value)
        if self.error_type == c.TapOracleOic.OicErrorType.SERVER_ERROR:
            return str(c.TapOracleOic.OicErrorSeverity.ERROR.value)
        if self.error_type in {
            c.TapOracleOic.OicErrorType.NETWORK,
            c.TapOracleOic.OicErrorType.VALIDATION,
        }:
            return str(c.TapOracleOic.OicErrorSeverity.WARNING.value)
        return str(c.TapOracleOic.OicErrorSeverity.UNKNOWN.value)


__all__: list[str] = ["OicErrorContext"]
