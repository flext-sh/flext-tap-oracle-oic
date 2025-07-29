"""Oracle Integration Cloud - Monitoring Streams.

Copyright (c) 2025 FLEXT Team. All rights reserved.

Professional monitoring streams providing comprehensive visibility into
integration execution, performance metrics, errors, and operational health.
"""

from __future__ import annotations

from typing import Any, ClassVar

# MIGRATED: Singer SDK imports centralized via flext-meltano
from flext_meltano import singer_typing as th

from flext_tap_oracle_oic.streams import OICBaseStream


class ExecutionsStream(OICBaseStream):
    """Integration Executions Stream.

    Provides comprehensive execution history with performance metrics,
    status tracking, and detailed runtime information.

    Features:
        - Complete execution history with filtering
        - Performance metrics and timing data
        - Error details and recovery information
        - Business data tracking and correlation
        - Incremental extraction based on execution time
    """

    name = "executions"
    path = "/monitoring/executions"
    primary_keys: ClassVar = ["executionId"]
    replication_key = "timestamp"

    schema = th.PropertiesList(
        th.Property("executionId", th.StringType, description="Execution ID"),
        th.Property("integrationId", th.StringType, description="Integration ID"),
        th.Property("timestamp", th.DateTimeType, description="Execution timestamp"),
        th.Property("status", th.StringType, description="Execution status"),
        th.Property("duration", th.IntegerType, description="Duration in milliseconds"),
        th.Property(
            "errorMessage",
            th.StringType,
            description="Error message if failed",
        ),
        th.Property(
            "_tap_extracted_at",
            th.DateTimeType,
            description="Extraction timestamp",
        ),
        th.Property(
            "_tap_stream_name",
            th.StringType,
            description="Source stream name",
        ),
    ).to_dict()

    def additional_params(self, _context: dict[str, Any] | None) -> dict[str, Any]:
        """Additional parameters for the request."""
        params: dict[str, Any] = {}

        # Time range filtering
        time_range = self.config.get("execution_time_range", "24h")
        params["timeRange"] = time_range

        # Status filtering
        status_filter = self.config.get("execution_status_filter")
        if status_filter:
            params["status"] = (
                ",".join(status_filter)
                if isinstance(status_filter, list)
                else status_filter
            )

        return params


class MetricsStream(OICBaseStream):
    """Integration Metrics Stream.

    Provides aggregated performance metrics, KPIs, and statistical data
    for integrations, including success rates, throughput, and latency.

    Features:
        - Real-time and historical metrics
        - Aggregated KPIs and statistics
        - Performance trending data
        - Resource utilization metrics
        - SLA compliance tracking
    """

    name = "metrics"
    path = "/monitoring/metrics"
    primary_keys: ClassVar = ["metricId", "timestamp"]
    replication_key = "timestamp"

    schema = th.PropertiesList(
        th.Property("metricId", th.StringType, description="Metric ID"),
        th.Property("timestamp", th.DateTimeType, description="Metric timestamp"),
        th.Property("metricType", th.StringType, description="Type of metric"),
        th.Property("value", th.NumberType, description="Metric value"),
        th.Property("unit", th.StringType, description="Metric unit"),
        th.Property(
            "_tap_extracted_at",
            th.DateTimeType,
            description="Extraction timestamp",
        ),
        th.Property(
            "_tap_stream_name",
            th.StringType,
            description="Source stream name",
        ),
    ).to_dict()

    def additional_params(self, _context: dict[str, Any] | None) -> dict[str, Any]:
        """Additional parameters for the request."""
        params: dict[str, Any] = {}

        # Time range
        time_range = self.config.get("metrics_time_range", "1h")
        params["timeRange"] = time_range

        return params


class ErrorsStream(OICBaseStream):
    """Integration Errors Stream.

    Provides detailed error tracking, analysis, and recovery information
    for failed integrations and system errors.

    Features:
        - Comprehensive error details
        - Error categorization and analysis
        - Recovery and retry information
        - Root cause analysis data
        - Error trends and patterns
    """

    name = "errors"
    path = "/monitoring/errors"
    primary_keys: ClassVar = ["errorId"]
    replication_key = "timestamp"

    schema = th.PropertiesList(
        th.Property("errorId", th.StringType, description="Error ID"),
        th.Property("timestamp", th.DateTimeType, description="Error timestamp"),
        th.Property("errorCode", th.StringType, description="Error code"),
        th.Property("errorMessage", th.StringType, description="Error message"),
        th.Property("severity", th.StringType, description="Error severity"),
        th.Property(
            "integrationId",
            th.StringType,
            description="Related integration ID",
        ),
        th.Property(
            "_tap_extracted_at",
            th.DateTimeType,
            description="Extraction timestamp",
        ),
        th.Property(
            "_tap_stream_name",
            th.StringType,
            description="Source stream name",
        ),
    ).to_dict()

    def additional_params(self, _context: dict[str, Any] | None) -> dict[str, Any]:
        """Additional parameters for the request."""
        params: dict[str, Any] = {}

        # Time range
        time_range = self.config.get("error_time_range", "24h")
        params["timeRange"] = time_range

        return params
