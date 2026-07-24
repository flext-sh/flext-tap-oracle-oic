"""OIC OicActivityRecord model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, ClassVar, Self

from flext_meltano import FlextMeltanoModels
from flext_tap_oracle_oic import c, t, u

if TYPE_CHECKING:
    from datetime import datetime


class OicActivityRecord(FlextMeltanoModels.Entity):
    """OIC Activity monitoring record for incremental replication."""

    # Pydantic 2.11 Configuration - Activity Features
    model_config: ClassVar[FlextMeltanoModels.ConfigDict] = (
        FlextMeltanoModels.ConfigDict(
            json_schema_extra={
                "description": "Oracle OIC activity record with performance tracking",
                "examples": [
                    {
                        "activity_id": "ACT_20230101_001",
                        "integration_id": "CUSTOMER_SYNC_01.00.0000",
                        "status": "COMPLETED",
                        "messages_processed": 1500,
                    }
                ],
            }
        )
    )

    activity_id: Annotated[
        str, u.Field(..., description="Unique activity record identifier")
    ]
    integration_id: Annotated[
        str, u.Field(..., description="Associated integration ID")
    ]
    instance_id: Annotated[str, u.Field(..., description="Integration instance ID")]

    # Temporal information (for incremental replication)
    start_time: Annotated[
        datetime, u.Field(..., description="Activity start timestamp")
    ]
    end_time: Annotated[
        datetime | None, u.Field(None, description="Activity end timestamp")
    ]
    duration_ms: Annotated[
        int | None, u.Field(None, description="Activity duration in milliseconds")
    ]

    # Status and results
    status: Annotated[
        c.TapOracleOic.OicJobStatus, u.Field(..., description="Activity status")
    ]
    result: Annotated[str | None, u.Field(None, description="Activity result")]
    error_message: Annotated[
        str | None, u.Field(None, description="Error message if failed")
    ]

    # Metrics
    messages_processed: Annotated[
        int | None, u.Field(None, description="Number of messages processed")
    ]
    bytes_processed: Annotated[int | None, u.Field(None, description="Bytes processed")]
    throughput_mps: Annotated[
        float | None, u.Field(None, description="Messages per second throughput")
    ]

    @u.computed_field()
    @property
    def activity_performance_summary(self) -> t.TapOracleOic.SectionedSummary:
        """OIC activity performance summary."""
        duration_seconds = 0.0
        if self.duration_ms:
            duration_seconds = self.duration_ms / 1000

        return {
            "activity_identity": {
                "id": self.activity_id,
                "integration_id": self.integration_id,
                "instance_id": self.instance_id,
                "status": self.status,
            },
            "performance": {
                "start_time": self.start_time.isoformat(),
                "end_time": self.end_time.isoformat() if self.end_time else None,
                "duration_seconds": duration_seconds,
                "messages_processed": self.messages_processed or 0,
                "throughput_mps": self.throughput_mps or 0.0,
            },
            "quality": {
                "result": self.result,
                "has_error": bool(self.error_message),
                "error_message": self.error_message,
                "success": self.status == c.TapOracleOic.OicJobStatus.COMPLETED.value,
            },
            "volume": {
                "bytes_processed": self.bytes_processed or 0,
                "mb_processed": (self.bytes_processed or 0) / (1024 * 1024),
            },
        }

    @u.model_validator(mode="after")
    def validate_activity_record(self) -> Self:
        """Validate OIC activity record."""
        if not self.activity_id:
            msg = "Activity ID is required"
            raise ValueError(msg)
        if not self.integration_id:
            msg = "Integration ID is required"
            raise ValueError(msg)
        if self.duration_ms is not None and self.duration_ms < 0:
            msg = "Duration cannot be negative"
            raise ValueError(msg)
        return self


__all__: list[str] = ["OicActivityRecord"]
