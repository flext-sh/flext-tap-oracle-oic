"""OracleOic.FlextTapOracleOicExecutionSummary entity model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from flext_oracle_oic import m
from flext_tap_oracle_oic import t, u

if TYPE_CHECKING:
    from datetime import datetime


class FlextTapOracleOicExecutionSummary(m):
    """OIC execution summary value object."""

    integration_id: Annotated[str, u.Field(..., description="Integration ID")]
    total_executions: Annotated[
        t.NonNegativeInt,
        u.Field(description="Total number of executions"),
    ] = 0
    successful_executions: Annotated[
        t.NonNegativeInt,
        u.Field(description="Successful executions"),
    ] = 0
    failed_executions: Annotated[
        t.NonNegativeInt,
        u.Field(description="Failed executions"),
    ] = 0
    average_duration_ms: Annotated[
        t.NonNegativeFloat | None,
        u.Field(None, description="Average execution duration"),
    ]
    last_execution_at: Annotated[
        datetime | None,
        u.Field(None, description="Last execution timestamp"),
    ]

    @property
    def failure_rate(self) -> float:
        """Calculate failure rate percentage."""
        return 100.0 - self.success_rate

    @property
    def success_rate(self) -> float:
        """Calculate success rate percentage."""
        if self.total_executions == 0:
            return 0.0
        success_rate: float = self.successful_executions / self.total_executions * 100.0
        return success_rate


__all__: list[str] = ["FlextTapOracleOicExecutionSummary"]
