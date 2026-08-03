"""OracleOic.FlextTapOracleOicMonitoringRecord entity model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from flext_oracle_oic import m
from flext_tap_oracle_oic import c, t, u

if TYPE_CHECKING:
    from datetime import datetime


class FlextTapOracleOicMonitoringRecord(m):
    """OIC monitoring record domain entity using flext-core patterns."""

    instance_id: Annotated[
        str, u.Field(..., min_length=1, description="Flow instance ID")
    ]
    integration_id: Annotated[
        str, u.Field(..., description="Associated integration ID")
    ]
    flow_id: Annotated[str | None, u.Field(None, description="Flow ID")]
    tracking_level: Annotated[str | None, u.Field(None, description="Tracking level")]
    started_at: Annotated[datetime, u.Field(..., description="Execution start time")]
    completed_at: Annotated[
        datetime | None, u.Field(None, description="Execution completion time")
    ]
    duration_ms: Annotated[
        int | None, u.Field(None, ge=0, description="Duration in milliseconds")
    ]
    execution_status: Annotated[str, u.Field(..., description="Execution status")]
    error_code: Annotated[str | None, u.Field(None, description="Error code if failed")]
    error_message: Annotated[
        str | None, u.Field(None, description="Error message if failed")
    ]
    message_count: Annotated[
        t.NonNegativeInt, u.Field(description="Number of messages processed")
    ] = 0
    error_count: Annotated[
        t.NonNegativeInt, u.Field(description="Number of errors")
    ] = 0
    business_identifiers: Annotated[
        t.MappingKV[str, t.JsonMapping],
        u.Field(description="Business tracking identifiers"),
    ] = u.Field(default_factory=dict)

    @property
    def duration_seconds(self) -> float | None:
        """The duration in seconds."""
        return self.duration_ms / 1000.0 if self.duration_ms is not None else None

    @property
    def is_failed(self) -> bool:
        """Check if execution failed."""
        return self.execution_status.lower() in {
            c.TapOracleOic.OicJobStatus.FAILED.value.lower(),
            "faulted",
            c.TapOracleOic.OicJobStatus.ABORTED.value.lower(),
        }

    @property
    def successful(self) -> bool:
        """Check if execution was successful."""
        return self.execution_status.lower() in {
            c.TapOracleOic.OicJobStatus.COMPLETED.value.lower(),
            "succeeded",
        }


__all__: list[str] = ["FlextTapOracleOicMonitoringRecord"]
