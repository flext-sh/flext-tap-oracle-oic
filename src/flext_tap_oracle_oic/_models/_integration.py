"""OIC OicIntegrationEntity model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, ClassVar, Self

from flext_meltano import FlextMeltanoModels
from flext_tap_oracle_oic import c, t, u

if TYPE_CHECKING:
    from datetime import datetime


class OicIntegrationEntity(FlextMeltanoModels.Entity):
    """OIC Integration entity with complete metadata."""

    # Pydantic 2.11 Configuration - Integration Features
    model_config: ClassVar[FlextMeltanoModels.ConfigDict] = (
        FlextMeltanoModels.ConfigDict(
            json_schema_extra={
                "description": "Oracle OIC integration with complete metadata",
                "examples": [
                    {
                        "integration_id": "CUSTOMER_SYNC_01.00.0000",
                        "name": "Customer Synchronization",
                        "status": "ACTIVE",
                        "version": "01.00.0000",
                    }
                ],
            }
        )
    )

    integration_id: Annotated[str, u.Field(description="Unique integration identifier")]
    name: Annotated[str, u.Field(..., description="Integration name")]
    description: Annotated[
        str | None, u.Field(None, description="Integration description")
    ]
    api_version: Annotated[
        str, u.Field(..., description="Integration version from OIC API")
    ]
    status: Annotated[
        c.TapOracleOic.OicIntegrationStatus,
        u.Field(..., description="Integration status"),
    ]

    # Temporal information
    created_date: Annotated[
        datetime | None, u.Field(None, description="Integration creation date")
    ]
    last_updated: Annotated[
        datetime | None, u.Field(None, description="Last update timestamp")
    ]
    last_activated: Annotated[
        datetime | None, u.Field(None, description="Last activation timestamp")
    ]

    # Metadata
    package_id: Annotated[
        str | None, u.Field(None, description="Associated package ID")
    ]
    pattern: Annotated[
        str | None, u.Field(None, description="Integration pattern type")
    ]
    style: Annotated[str | None, u.Field(None, description="Integration style")]

    # Runtime information
    execution_count: Annotated[
        int | None, u.Field(None, description="Total execution count")
    ]
    error_count: Annotated[int | None, u.Field(None, description="Total error count")]
    last_execution_time: Annotated[
        datetime | None, u.Field(None, description="Last execution timestamp")
    ]

    @u.computed_field()
    @property
    def integration_health_summary(self) -> t.TapOracleOic.SectionedSummary:
        """OIC integration health and performance summary."""
        error_rate = 0.0
        if self.execution_count and self.execution_count > 0:
            error_rate = (self.error_count or 0) / self.execution_count

        return {
            "integration_identity": {
                "id": self.integration_id,
                "name": self.name,
                "version": self.api_version,
                "status": self.status,
            },
            "health_metrics": {
                "total_executions": self.execution_count or 0,
                "total_errors": self.error_count or 0,
                "error_rate": error_rate,
                "health_status": c.TapOracleOic.OicHealthStatus.HEALTHY.value
                if error_rate < c.TapOracleOic.MAX_PERCENTAGE / 20
                else c.TapOracleOic.OicHealthStatus.DEGRADED.value,
            },
            "metadata": {
                "pattern": self.pattern,
                "style": self.style,
                "package_id": self.package_id,
                "last_execution": self.last_execution_time.isoformat()
                if self.last_execution_time
                else None,
            },
        }

    @u.model_validator(mode="after")
    def validate_integration_entity(self) -> Self:
        """Validate OIC integration entity."""
        if not self.integration_id:
            msg = "Integration ID is required"
            raise ValueError(msg)
        if not self.name:
            msg = "Integration name is required"
            raise ValueError(msg)
        if self.execution_count is not None and self.execution_count < 0:
            msg = "Execution count cannot be negative"
            raise ValueError(msg)
        return self


__all__: list[str] = ["OicIntegrationEntity"]
