"""OIC OicMetricsRecord model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from datetime import datetime
from typing import Annotated, ClassVar, Self

from flext_meltano import FlextMeltanoModels
from flext_tap_oracle_oic import c, t, u


class OicMetricsRecord(FlextMeltanoModels.Entity):
    """OIC Metrics record for performance monitoring."""

    # Pydantic 2.11 Configuration - Metrics Features
    model_config: ClassVar[FlextMeltanoModels.ConfigDict] = (
        FlextMeltanoModels.ConfigDict(
            json_schema_extra={
                "description": "Oracle OIC performance metrics with resource monitoring",
                "examples": [
                    {
                        "metric_id": "METRIC_20230101_001",
                        "integration_id": "CUSTOMER_SYNC_01.00.0000",
                        "throughput_mps": 125.5,
                        "cpu_usage_percent": 45.2,
                    },
                ],
            },
        )
    )

    metric_id: Annotated[
        str,
        u.Field(..., description="Unique metrics record identifier"),
    ]
    integration_id: Annotated[
        str,
        u.Field(..., description="Associated integration ID"),
    ]
    timestamp: Annotated[datetime, u.Field(..., description="Metrics timestamp")]

    # Performance metrics
    cpu_usage_percent: Annotated[
        float | None,
        u.Field(
            None,
            description="CPU usage percentage",
        ),
    ]
    memory_usage_mb: Annotated[
        float | None,
        u.Field(
            None,
            description="Memory usage in MB",
        ),
    ]
    throughput_mps: Annotated[
        float | None,
        u.Field(
            None,
            description="Messages per second",
        ),
    ]
    latency_ms: Annotated[
        float | None,
        u.Field(
            None,
            description="Average latency in milliseconds",
        ),
    ]

    # Business metrics
    success_count: Annotated[
        int | None,
        u.Field(
            None,
            description="Successful message count",
        ),
    ]
    error_count: Annotated[
        int | None,
        u.Field(None, description="Error message count"),
    ]
    retry_count: Annotated[
        int | None,
        u.Field(None, description="Retry attempt count"),
    ]

    # Resource utilization
    database_connections: Annotated[
        int | None,
        u.Field(
            None,
            description="Active database connections",
        ),
    ]
    thread_count: Annotated[
        int | None,
        u.Field(None, description="Active thread count"),
    ]
    queue_depth: Annotated[
        int | None,
        u.Field(None, description="Message queue depth"),
    ]

    @u.computed_field()
    @property
    def metrics_analysis_summary(
        self,
    ) -> t.TapOracleOic.SectionedSummary:
        """OIC metrics complete analysis summary."""
        total_messages = (self.success_count or 0) + (self.error_count or 0)
        error_rate = 0.0
        if total_messages > 0:
            error_rate = (self.error_count or 0) / total_messages

        return {
            "metrics_identity": {
                "id": self.metric_id,
                "integration_id": self.integration_id,
                "timestamp": self.timestamp.isoformat(),
            },
            "performance": {
                "cpu_usage_percent": self.cpu_usage_percent or 0.0,
                "memory_usage_mb": self.memory_usage_mb or 0.0,
                "throughput_mps": self.throughput_mps or 0.0,
                "latency_ms": self.latency_ms or 0.0,
            },
            "business_metrics": {
                "total_messages": total_messages,
                "success_count": self.success_count or 0,
                "error_count": self.error_count or 0,
                "retry_count": self.retry_count or 0,
                "error_rate": error_rate,
            },
            "resource_utilization": {
                "database_connections": self.database_connections or 0,
                "thread_count": self.thread_count or 0,
                "queue_depth": self.queue_depth or 0,
            },
        }

    @u.model_validator(mode="after")
    def validate_metrics_record(self) -> Self:
        """Validate OIC metrics record."""
        if not self.metric_id:
            msg = "Metric ID is required"
            raise ValueError(msg)
        if not self.integration_id:
            msg = "Integration ID is required"
            raise ValueError(msg)
        if self.cpu_usage_percent is not None and not (
            c.TapOracleOic.MIN_PERCENTAGE
            <= self.cpu_usage_percent
            <= c.TapOracleOic.MAX_PERCENTAGE
        ):
            msg = "CPU usage must be between 0 and 100 percent"
            raise ValueError(msg)
        return self


__all__: list[str] = ["OicMetricsRecord"]
