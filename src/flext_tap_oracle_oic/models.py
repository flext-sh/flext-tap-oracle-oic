"""Oracle Integration Cloud Models using standardized [Project]Models pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import Field

from flext_core import FlextModels


class FlextTapOracleOicModels(FlextModels):
    """Oracle Integration Cloud tap models extending flext-core FlextModels.

    Provides comprehensive models for OIC entity extraction, authentication,
    monitoring, and Singer protocol compliance following standardized patterns.
    """

    class OicAuthenticationConfig(FlextModels.BaseConfig):
        """OAuth2/IDCS authentication configuration for OIC API access."""

        oauth_client_id: str = Field(..., description="OAuth2 client ID for OIC API")
        oauth_client_secret: str = Field(..., description="OAuth2 client secret")
        oauth_token_url: str = Field(..., description="IDCS OAuth2 token endpoint URL")
        oauth_client_aud: str = Field(..., description="OAuth2 audience parameter")
        base_url: str = Field(..., description="OIC instance base URL")

        # Optional authentication settings
        token_expiry_buffer: int = Field(
            default=300, description="Token refresh buffer in seconds"
        )
        max_retry_attempts: int = Field(
            default=3, description="Maximum authentication retry attempts"
        )
        timeout_seconds: int = Field(default=30, description="Authentication timeout")

    class OicIntegrationEntity(FlextModels.Entity):
        """OIC Integration entity with comprehensive metadata."""

        integration_id: str = Field(..., description="Unique integration identifier")
        name: str = Field(..., description="Integration name")
        description: str | None = Field(None, description="Integration description")
        version: str = Field(..., description="Integration version")
        status: Literal["ACTIVE", "INACTIVE", "DRAFT", "ERROR"] = Field(
            ..., description="Integration status"
        )

        # Temporal information
        created_date: datetime | None = Field(
            None, description="Integration creation date"
        )
        last_updated: datetime | None = Field(None, description="Last update timestamp")
        last_activated: datetime | None = Field(
            None, description="Last activation timestamp"
        )

        # Metadata
        package_id: str | None = Field(None, description="Associated package ID")
        pattern: str | None = Field(None, description="Integration pattern type")
        style: str | None = Field(None, description="Integration style")

        # Runtime information
        execution_count: int | None = Field(None, description="Total execution count")
        error_count: int | None = Field(None, description="Total error count")
        last_execution_time: datetime | None = Field(
            None, description="Last execution timestamp"
        )

    class OicConnectionEntity(FlextModels.Entity):
        """OIC Connection entity with security sanitization."""

        connection_id: str = Field(..., description="Unique connection identifier")
        name: str = Field(..., description="Connection name")
        description: str | None = Field(None, description="Connection description")
        connection_type: str = Field(..., description="Connection adapter type")

        # Configuration (sanitized)
        host: str | None = Field(None, description="Connection host (if applicable)")
        port: int | None = Field(None, description="Connection port (if applicable)")

        # Security metadata (credentials removed)
        authentication_type: str | None = Field(
            None, description="Authentication method used"
        )
        security_policy: str | None = Field(None, description="Security policy name")
        certificate_alias: str | None = Field(
            None, description="Certificate alias (if used)"
        )

        # Status and health
        status: Literal["ACTIVE", "INACTIVE", "ERROR", "TESTING"] = Field(
            ..., description="Connection status"
        )
        last_tested: datetime | None = Field(
            None, description="Last connection test timestamp"
        )
        test_result: str | None = Field(None, description="Last test result")

        # Sanitization markers
        data_sanitized: bool = Field(
            default=True, description="Indicates if sensitive data was removed"
        )
        sanitization_timestamp: datetime | None = Field(
            default_factory=datetime.utcnow, description="When sanitization occurred"
        )

    class OicActivityRecord(FlextModels.Entity):
        """OIC Activity monitoring record for incremental replication."""

        activity_id: str = Field(..., description="Unique activity record identifier")
        integration_id: str = Field(..., description="Associated integration ID")
        instance_id: str = Field(..., description="Integration instance ID")

        # Temporal information (for incremental replication)
        start_time: datetime = Field(..., description="Activity start timestamp")
        end_time: datetime | None = Field(None, description="Activity end timestamp")
        duration_ms: int | None = Field(
            None, description="Activity duration in milliseconds"
        )

        # Status and results
        status: Literal["RUNNING", "COMPLETED", "FAILED", "ABORTED", "SUSPENDED"] = (
            Field(..., description="Activity status")
        )
        result: str | None = Field(None, description="Activity result")
        error_message: str | None = Field(None, description="Error message if failed")

        # Metrics
        messages_processed: int | None = Field(
            None, description="Number of messages processed"
        )
        bytes_processed: int | None = Field(None, description="Bytes processed")
        throughput_mps: float | None = Field(
            None, description="Messages per second throughput"
        )

    class OicPackageEntity(FlextModels.Entity):
        """OIC Package entity for integration packages."""

        package_id: str = Field(..., description="Unique package identifier")
        name: str = Field(..., description="Package name")
        description: str | None = Field(None, description="Package description")
        version: str = Field(..., description="Package version")

        # Package metadata
        package_type: Literal["INTEGRATION", "LIBRARY", "TEMPLATE", "RECIPE"] = Field(
            ..., description="Package type"
        )
        created_by: str | None = Field(None, description="Package creator")
        created_date: datetime | None = Field(None, description="Package creation date")

        # Dependencies and relationships
        dependencies: list[str] = Field(
            default_factory=list, description="List of dependent package IDs"
        )
        integration_count: int | None = Field(
            None, description="Number of integrations in package"
        )

        # Status
        status: Literal["ACTIVE", "INACTIVE", "DEPRECATED"] = Field(
            ..., description="Package status"
        )
        download_count: int | None = Field(None, description="Package download count")

    class OicMetricsRecord(FlextModels.Entity):
        """OIC Metrics record for performance monitoring."""

        metric_id: str = Field(..., description="Unique metrics record identifier")
        integration_id: str = Field(..., description="Associated integration ID")
        timestamp: datetime = Field(..., description="Metrics timestamp")

        # Performance metrics
        cpu_usage_percent: float | None = Field(
            None, description="CPU usage percentage"
        )
        memory_usage_mb: float | None = Field(None, description="Memory usage in MB")
        throughput_mps: float | None = Field(None, description="Messages per second")
        latency_ms: float | None = Field(
            None, description="Average latency in milliseconds"
        )

        # Business metrics
        success_count: int | None = Field(None, description="Successful message count")
        error_count: int | None = Field(None, description="Error message count")
        retry_count: int | None = Field(None, description="Retry attempt count")

        # Resource utilization
        database_connections: int | None = Field(
            None, description="Active database connections"
        )
        thread_count: int | None = Field(None, description="Active thread count")
        queue_depth: int | None = Field(None, description="Message queue depth")

    class OicAgentEntity(FlextModels.Entity):
        """OIC Agent entity for connectivity agents."""

        agent_id: str = Field(..., description="Unique agent identifier")
        agent_name: str = Field(..., description="Agent display name")
        agent_type: Literal["CONNECTIVITY_AGENT", "ON_PREMISES_AGENT", "FILE_AGENT"] = (
            Field(..., description="Agent type")
        )

        # Agent status and health
        status: Literal["ONLINE", "OFFLINE", "ERROR", "MAINTENANCE"] = Field(
            ..., description="Agent status"
        )
        last_heartbeat: datetime | None = Field(
            None, description="Last heartbeat timestamp"
        )
        version: str | None = Field(None, description="Agent version")

        # Configuration
        host_machine: str | None = Field(None, description="Host machine name")
        installation_path: str | None = Field(
            None, description="Agent installation path"
        )
        port: int | None = Field(None, description="Agent communication port")

        # Health metrics
        uptime_hours: float | None = Field(None, description="Agent uptime in hours")
        connection_count: int | None = Field(
            None, description="Active connection count"
        )
        last_error: str | None = Field(None, description="Last error message")

    class OicStreamConfiguration(FlextModels.BaseConfig):
        """Configuration for OIC tap streams."""

        stream_name: str = Field(..., description="Singer stream name")
        replication_method: Literal["FULL_TABLE", "INCREMENTAL"] = Field(
            default="FULL_TABLE", description="Replication method"
        )
        replication_key: str | None = Field(
            None, description="Replication key field name"
        )

        # Pagination and performance
        page_size: int = Field(
            default=100, ge=1, le=1000, description="API pagination size"
        )
        include_extended: bool = Field(
            default=False, description="Include extended entity metadata"
        )

        # Filtering
        status_filter: list[str] | None = Field(
            None, description="Filter by entity status values"
        )
        date_range_filter: str | None = Field(
            None, description="Date range filter for incremental streams"
        )

        # Security
        sanitize_sensitive_data: bool = Field(
            default=True, description="Enable data sanitization"
        )
        exclude_test_entities: bool = Field(
            default=True, description="Exclude test/demo entities"
        )

    class OicApiResponse(FlextModels.BaseModel):
        """Standardized OIC API response wrapper."""

        success: bool = Field(..., description="Response success indicator")
        data: Any | None = Field(None, description="Response data payload")
        total_count: int | None = Field(
            None, description="Total entity count (for pagination)"
        )
        page_size: int | None = Field(None, description="Current page size")
        page_number: int | None = Field(None, description="Current page number")

        # Error information
        error_code: str | None = Field(None, description="Error code if failed")
        error_message: str | None = Field(None, description="Error message if failed")
        error_details: dict[str, Any] | None = Field(
            None, description="Detailed error information"
        )

        # Metadata
        timestamp: datetime = Field(
            default_factory=datetime.utcnow, description="Response timestamp"
        )
        api_version: str | None = Field(None, description="OIC API version")
        request_id: str | None = Field(None, description="Request correlation ID")

    class OicErrorContext(FlextModels.BaseModel):
        """Error context for OIC API error handling."""

        error_type: Literal[
            "AUTHENTICATION",
            "AUTHORIZATION",
            "RATE_LIMIT",
            "SERVER_ERROR",
            "NETWORK",
            "VALIDATION",
        ] = Field(..., description="Error category")
        http_status_code: int | None = Field(None, description="HTTP status code")
        retry_after_seconds: int | None = Field(
            None, description="Retry after duration"
        )

        # Context information
        endpoint: str | None = Field(None, description="API endpoint that failed")
        request_method: str | None = Field(None, description="HTTP method used")
        request_params: dict[str, Any] | None = Field(
            None, description="Request parameters"
        )

        # Recovery information
        is_retryable: bool = Field(
            default=False, description="Whether error is retryable"
        )
        suggested_action: str | None = Field(
            None, description="Suggested recovery action"
        )
        max_retry_attempts: int | None = Field(
            None, description="Maximum retry attempts for this error"
        )


__all__ = [
    "FlextTapOracleOicModels",
]
