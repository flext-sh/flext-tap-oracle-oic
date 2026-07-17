"""OIC OicApiResponse model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, ClassVar, Self

from flext_meltano import FlextMeltanoModels
from flext_tap_oracle_oic import t, u

if TYPE_CHECKING:
    from datetime import datetime


class OicApiResponse(FlextMeltanoModels.Entity):
    """Standardized OIC API response wrapper."""

    # Pydantic 2.11 Configuration - API Response Features
    model_config: ClassVar[FlextMeltanoModels.ConfigDict] = (
        FlextMeltanoModels.ConfigDict(
            json_schema_extra={
                "description": "Oracle OIC API response with pagination and error handling",
                "examples": [
                    {
                        "success": True,
                        "total_count": 150,
                        "page_size": 50,
                        "page_number": 1,
                    },
                ],
            },
        )
    )

    success: Annotated[
        bool,
        u.Field(..., description="Response success indicator"),
    ]
    data: Annotated[
        t.JsonMapping | None,
        u.Field(
            None,
            description="Response data payload",
        ),
    ]
    total_count: Annotated[
        int | None,
        u.Field(
            None,
            description="Total entity count (for pagination)",
        ),
    ]
    page_size: Annotated[
        int | None,
        u.Field(None, description="Current page size"),
    ]
    page_number: Annotated[
        int | None,
        u.Field(None, description="Current page number"),
    ]

    # Error information
    error_code: Annotated[
        str | None,
        u.Field(None, description="Error code if failed"),
    ]
    error_message: Annotated[
        str | None,
        u.Field(
            None,
            description="Error message if failed",
        ),
    ]
    error_details: Annotated[
        t.MappingKV[str, t.JsonMapping] | None,
        u.Field(
            None,
            description="Detailed error information",
        ),
    ]

    # Metadata
    timestamp: Annotated[
        datetime,
        u.Field(
            description="Response timestamp",
        ),
    ] = u.Field(default_factory=u.now)
    api_version: Annotated[
        str | None,
        u.Field(None, description="OIC API version"),
    ]
    request_id: Annotated[
        str | None,
        u.Field(None, description="Request correlation ID"),
    ]

    @u.computed_field()
    @property
    def api_response_summary(
        self,
    ) -> t.TapOracleOic.SectionedSummary:
        """OIC API response summary."""
        return {
            "response_status": {
                "success": self.success,
                "timestamp": self.timestamp.isoformat(),
                "api_version": self.api_version,
                "request_id": self.request_id,
            },
            "pagination": {
                "total_count": self.total_count,
                "page_size": self.page_size,
                "page_number": self.page_number,
                "has_more": self.total_count
                and self.page_size
                and (self.page_number or 1) * self.page_size < self.total_count,
            },
            "error_info": {
                "has_error": not self.success,
                "error_code": self.error_code,
                "error_message": self.error_message,
                "has_details": bool(self.error_details),
            },
            "data_info": {
                "has_data": self.data is not None,
                "data_type": type(self.data).__name__
                if self.data is not None
                else None,
            },
        }

    @u.model_validator(mode="after")
    def validate_api_response(self) -> Self:
        """Validate OIC API response."""
        if not self.success and not self.error_message:
            msg = "Failed responses must have an error message"
            raise ValueError(msg)
        if self.page_number is not None and self.page_number < 1:
            msg = "Page number must be positive"
            raise ValueError(msg)
        return self


__all__: list[str] = ["OicApiResponse"]
