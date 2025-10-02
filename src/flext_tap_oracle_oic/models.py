"""Oracle Integration Cloud Models using standardized [Project]Models pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Literal, Self

from flext_core import FlextModels
from pydantic import (
    ConfigDict,
    Field,
    FieldSerializationInfo,
    computed_field,
    field_serializer,
    model_validator,
)

# Oracle Integration Cloud status constants
ACTIVE = "ACTIVE"
INACTIVE = "INACTIVE"
DRAFT = "DRAFT"
ERROR = "ERROR"
TESTING = "TESTING"
DEPRECATED = "DEPRECATED"

# Status constants
RUNNING = "RUNNING"
COMPLETED = "COMPLETED"
FAILED = "FAILED"
ABORTED = "ABORTED"
SUSPENDED = "SUSPENDED"

# Integration constants
INTEGRATION = "INTEGRATION"
LIBRARY = "LIBRARY"
TEMPLATE = "TEMPLATE"
RECIPE = "RECIPE"
CONNECTIVITY_AGENT = "CONNECTIVITY_AGENT"

# Agent type constants
ON_PREMISES_AGENT = "ON_PREMISES_AGENT"
FILE_AGENT = "FILE_AGENT"

# Status constants
ONLINE = "ONLINE"
OFFLINE = "OFFLINE"
MAINTENANCE = "MAINTENANCE"

# Replication method constants
FULL_TABLE = "FULL_TABLE"
INCREMENTAL = "INCREMENTAL"

# Error type constants
AUTHENTICATION = "AUTHENTICATION"
AUTHORIZATION = "AUTHORIZATION"
RATE_LIMIT = "RATE_LIMIT"


class FlextTapOracleOicModels(FlextModels):
    """Oracle Integration Cloud tap models extending flext-core FlextModels.

    Provides comprehensive models for OIC entity extraction, authentication,
    monitoring, and Singer protocol compliance following standardized patterns.
    """

    # Pydantic 2.11 Configuration - Enterprise Singer Oracle OIC Tap Features
    model_config = ConfigDict(
        validate_assignment=True,
        use_enum_values=True,
        arbitrary_types_allowed=True,
        extra="forbid",
        frozen=False,
        validate_return=True,
        ser_json_timedelta="iso8601",
        ser_json_bytes="base64",
        hide_input_in_errors=True,
        json_schema_extra={
            "title": "FLEXT Singer Oracle OIC Tap Models",
            "description": "Enterprise Oracle Integration Cloud API extraction models with Singer protocol compliance",
            "examples": [
                {
                    "tap_name": "tap-oracle-oic",
                    "extraction_mode": "api_incremental_replication",
                    "oic_instance": "https://mycompany-oic.integration.ocp.oraclecloud.com",
                }
            ],
            "tags": ["singer", "oracle-oic", "tap", "extraction", "integration-cloud"],
            "version": "2.11.0",
        },
    )

    # Advanced Pydantic 2.11 Features - Singer Oracle OIC Tap Domain

    @computed_field
    @property
    def active_oic_tap_models_count(self) -> int:
        """Count of active Oracle OIC tap models with API extraction capabilities."""
        count = 0
        # Count core Singer Oracle OIC tap models
        if hasattr(self, "OicAuthenticationConfig"):
            count += 1
        if hasattr(self, "OicIntegrationEntity"):
            count += 1
        if hasattr(self, "OicConnectionEntity"):
            count += 1
        if hasattr(self, "OicActivityRecord"):
            count += 1
        if hasattr(self, "OicPackageEntity"):
            count += 1
        if hasattr(self, "OicMetricsRecord"):
            count += 1
        if hasattr(self, "OicAgentEntity"):
            count += 1
        if hasattr(self, "OicStreamConfiguration"):
            count += 1
        if hasattr(self, "OicApiResponse"):
            count += 1
        if hasattr(self, "OicErrorContext"):
            count += 1
        return count

    @computed_field
    @property
    def oic_tap_system_summary(self) -> dict[str, object]:
        """Comprehensive Singer Oracle OIC tap system summary with API extraction capabilities."""
        return {
            "total_models": self.active_oic_tap_models_count,
            "tap_type": "singer_oracle_oic_api_extractor",
            "extraction_features": [
                "oic_integration_monitoring",
                "connection_metadata_extraction",
                "activity_incremental_replication",
                "package_management_tracking",
                "performance_metrics_collection",
                "agent_health_monitoring",
            ],
            "singer_compliance": {
                "protocol_version": "singer_v1",
                "stream_discovery": True,
                "catalog_generation": True,
                "state_management": True,
                "incremental_bookmarking": True,
            },
            "oic_capabilities": {
                "oauth2_authentication": True,
                "api_pagination": True,
                "data_sanitization": True,
                "error_recovery": True,
                "rate_limit_handling": True,
            },
        }

    @model_validator(mode="after")
    def validate_oic_tap_system_consistency(self) -> Self:
        """Validate Singer Oracle OIC tap system consistency and configuration."""
        # Singer OIC tap authentication validation
        if hasattr(self, "_oic_authentication") and self._oic_authentication:
            if not hasattr(self, "OicAuthenticationConfig"):
                msg = "OicAuthenticationConfig required when OIC authentication configured"
                raise ValueError(msg)

        # Stream configuration validation
        if hasattr(self, "_stream_configurations") and self._stream_configurations:
            if not hasattr(self, "OicStreamConfiguration"):
                msg = "OicStreamConfiguration required for stream configurations"
                raise ValueError(msg)

        # Singer protocol compliance validation
        if hasattr(self, "_singer_mode") and self._singer_mode:
            required_models = ["OicApiResponse", "OicErrorContext"]
            for model in required_models:
                if not hasattr(self, model):
                    msg = f"{model} required for Singer protocol compliance"
                    raise ValueError(msg)

        return self

    @field_serializer("*", when_used="json")
    def serialize_with_oic_metadata(
        self, value: object, _info: FieldSerializationInfo
    ) -> object:
        """Add Singer Oracle OIC tap metadata to all serialized fields."""
        if isinstance(value, dict):
            return {
                **value,
                "_oic_tap_metadata": {
                    "extraction_timestamp": datetime.now(UTC).isoformat(),
                    "tap_type": "oracle_oic_api_extractor",
                    "singer_protocol": "v1.0",
                    "data_source": "oracle_integration_cloud",
                },
            }
        if isinstance(value, (str, int, float, bool)) and hasattr(
            self, "_include_oic_metadata"
        ):
            return {
                "value": value,
                "_oic_context": {
                    "extracted_at": datetime.now(UTC).isoformat(),
                    "tap_name": "flext-tap-oracle-oic",
                },
            }
        return value

    class OicAuthenticationConfig(FlextModels.BaseConfig):
        """OAuth2/IDCS authentication configuration for OIC API access."""

        # Pydantic 2.11 Configuration - Authentication Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "OAuth2/IDCS authentication for Oracle OIC API",
                "examples": [
                    {
                        "oauth_client_id": "my-client-id",
                        "oauth_token_url": "https://idcs-instance.identity.oraclecloud.com/oauth2/v1/token",
                        "base_url": "https://mycompany-oic.integration.ocp.oraclecloud.com",
                    }
                ],
            },
        )

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

        @computed_field
        @property
        def auth_config_summary(self) -> dict[str, object]:
            """OAuth2 authentication configuration summary."""
            return {
                "oauth_setup": {
                    "client_id": self.oauth_client_id[:8] + "..."
                    if len(self.oauth_client_id) > 8
                    else self.oauth_client_id,
                    "token_endpoint": self.oauth_token_url,
                    "audience": self.oauth_client_aud,
                },
                "oic_instance": {
                    "base_url": self.base_url,
                    "domain": self.base_url.split("//")[-1].split("/")[0]
                    if "//" in self.base_url
                    else self.base_url,
                },
                "security_settings": {
                    "token_buffer_seconds": self.token_expiry_buffer,
                    "max_retry_attempts": self.max_retry_attempts,
                    "timeout_seconds": self.timeout_seconds,
                },
            }

        @model_validator(mode="after")
        def validate_auth_config(self) -> Self:
            """Validate OAuth2 authentication configuration."""
            if not self.oauth_token_url.startswith("https://"):
                msg = "OAuth token URL must use HTTPS"
                raise ValueError(msg)
            if not self.base_url.startswith("https://"):
                msg = "OIC base URL must use HTTPS"
                raise ValueError(msg)
            if self.token_expiry_buffer < 60:
                msg = "Token expiry buffer must be at least 60 seconds"
                raise ValueError(msg)
            return self

    class OicIntegrationEntity(FlextModels.Entity):
        """OIC Integration entity with comprehensive metadata."""

        # Pydantic 2.11 Configuration - Integration Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "Oracle OIC integration with comprehensive metadata",
                "examples": [
                    {
                        "integration_id": "CUSTOMER_SYNC_01.00.0000",
                        "name": "Customer Synchronization",
                        "status": "ACTIVE",
                        "version": "01.00.0000",
                    }
                ],
            },
        )

        integration_id: str = Field(..., description="Unique integration identifier")
        name: str = Field(..., description="Integration name")
        description: str | None = Field(None, description="Integration description")
        version: str = Field(..., description="Integration version")
        status: Literal[ACTIVE, INACTIVE, DRAFT, ERROR] = Field(
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

        @computed_field
        @property
        def integration_health_summary(self) -> dict[str, object]:
            """OIC integration health and performance summary."""
            error_rate = 0.0
            if self.execution_count and self.execution_count > 0:
                error_rate = (self.error_count or 0) / self.execution_count

            return {
                "integration_identity": {
                    "id": self.integration_id,
                    "name": self.name,
                    "version": self.version,
                    "status": self.status,
                },
                "health_metrics": {
                    "total_executions": self.execution_count or 0,
                    "total_errors": self.error_count or 0,
                    "error_rate": error_rate,
                    "health_status": "healthy" if error_rate < 0.05 else "degraded",
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

        @model_validator(mode="after")
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

    class OicConnectionEntity(FlextModels.Entity):
        """OIC Connection entity with security sanitization."""

        # Pydantic 2.11 Configuration - Connection Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "Oracle OIC connection with security sanitization",
                "examples": [
                    {
                        "connection_id": "SALESFORCE_CONN_01",
                        "name": "Salesforce Production",
                        "connection_type": "SALESFORCE_ADAPTER",
                        "status": "ACTIVE",
                    }
                ],
            },
        )

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
        status: Literal[ACTIVE, INACTIVE, ERROR, TESTING] = Field(
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

        @computed_field
        @property
        def connection_security_summary(self) -> dict[str, object]:
            """OIC connection security and health summary."""
            return {
                "connection_identity": {
                    "id": self.connection_id,
                    "name": self.name,
                    "type": self.connection_type,
                    "status": self.status,
                },
                "connectivity": {
                    "host": self.host,
                    "port": self.port,
                    "last_tested": self.last_tested.isoformat()
                    if self.last_tested
                    else None,
                    "test_result": self.test_result,
                },
                "security": {
                    "auth_type": self.authentication_type,
                    "security_policy": self.security_policy,
                    "certificate_alias": self.certificate_alias,
                    "data_sanitized": self.data_sanitized,
                    "sanitization_timestamp": self.sanitization_timestamp.isoformat()
                    if self.sanitization_timestamp
                    else None,
                },
            }

        @model_validator(mode="after")
        def validate_connection_entity(self) -> Self:
            """Validate OIC connection entity."""
            if not self.connection_id:
                msg = "Connection ID is required"
                raise ValueError(msg)
            if not self.name:
                msg = "Connection name is required"
                raise ValueError(msg)
            if self.port is not None and not (1 <= self.port <= 65535):
                msg = "Port must be between 1 and 65535"
                raise ValueError(msg)
            return self

    class OicActivityRecord(FlextModels.Entity):
        """OIC Activity monitoring record for incremental replication."""

        # Pydantic 2.11 Configuration - Activity Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
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
            },
        )

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
        status: Literal[RUNNING, COMPLETED, FAILED, ABORTED, SUSPENDED] = Field(
            ..., description="Activity status"
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

        @computed_field
        @property
        def activity_performance_summary(self) -> dict[str, object]:
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
                    "success": self.status == "COMPLETED",
                },
                "volume": {
                    "bytes_processed": self.bytes_processed or 0,
                    "mb_processed": (self.bytes_processed or 0) / (1024 * 1024),
                },
            }

        @model_validator(mode="after")
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

    class OicPackageEntity(FlextModels.Entity):
        """OIC Package entity for integration packages."""

        # Pydantic 2.11 Configuration - Package Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "Oracle OIC package with dependency tracking",
                "examples": [
                    {
                        "package_id": "CUSTOMER_SUITE_V1",
                        "name": "Customer Management Suite",
                        "package_type": "INTEGRATION",
                        "status": "ACTIVE",
                    }
                ],
            },
        )

        package_id: str = Field(..., description="Unique package identifier")
        name: str = Field(..., description="Package name")
        description: str | None = Field(None, description="Package description")
        version: str = Field(..., description="Package version")

        # Package metadata
        package_type: Literal[INTEGRATION, LIBRARY, TEMPLATE, RECIPE] = Field(
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
        status: Literal[ACTIVE, INACTIVE, DEPRECATED] = Field(
            ..., description="Package status"
        )
        download_count: int | None = Field(None, description="Package download count")

        @computed_field
        @property
        def package_composition_summary(self) -> dict[str, object]:
            """OIC package composition and usage summary."""
            return {
                "package_identity": {
                    "id": self.package_id,
                    "name": self.name,
                    "version": self.version,
                    "type": self.package_type,
                    "status": self.status,
                },
                "composition": {
                    "integration_count": self.integration_count or 0,
                    "dependency_count": len(self.dependencies),
                    "has_dependencies": bool(self.dependencies),
                    "dependencies": self.dependencies,
                },
                "usage": {
                    "download_count": self.download_count or 0,
                    "created_by": self.created_by,
                    "created_date": self.created_date.isoformat()
                    if self.created_date
                    else None,
                },
            }

        @model_validator(mode="after")
        def validate_package_entity(self) -> Self:
            """Validate OIC package entity."""
            if not self.package_id:
                msg = "Package ID is required"
                raise ValueError(msg)
            if not self.name:
                msg = "Package name is required"
                raise ValueError(msg)
            if self.integration_count is not None and self.integration_count < 0:
                msg = "Integration count cannot be negative"
                raise ValueError(msg)
            return self

    class OicMetricsRecord(FlextModels.Entity):
        """OIC Metrics record for performance monitoring."""

        # Pydantic 2.11 Configuration - Metrics Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "Oracle OIC performance metrics with resource monitoring",
                "examples": [
                    {
                        "metric_id": "METRIC_20230101_001",
                        "integration_id": "CUSTOMER_SYNC_01.00.0000",
                        "throughput_mps": 125.5,
                        "cpu_usage_percent": 45.2,
                    }
                ],
            },
        )

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

        @computed_field
        @property
        def metrics_analysis_summary(self) -> dict[str, object]:
            """OIC metrics comprehensive analysis summary."""
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

        @model_validator(mode="after")
        def validate_metrics_record(self) -> Self:
            """Validate OIC metrics record."""
            if not self.metric_id:
                msg = "Metric ID is required"
                raise ValueError(msg)
            if not self.integration_id:
                msg = "Integration ID is required"
                raise ValueError(msg)
            if self.cpu_usage_percent is not None and not (
                0 <= self.cpu_usage_percent <= 100
            ):
                msg = "CPU usage must be between 0 and 100 percent"
                raise ValueError(msg)
            return self

    class OicAgentEntity(FlextModels.Entity):
        """OIC Agent entity for connectivity agents."""

        # Pydantic 2.11 Configuration - Agent Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "Oracle OIC connectivity agent with health monitoring",
                "examples": [
                    {
                        "agent_id": "AGENT_ONPREM_01",
                        "agent_name": "On-Premises Agent 01",
                        "agent_type": "CONNECTIVITY_AGENT",
                        "status": "ONLINE",
                    }
                ],
            },
        )

        agent_id: str = Field(..., description="Unique agent identifier")
        agent_name: str = Field(..., description="Agent display name")
        agent_type: Literal[CONNECTIVITY_AGENT, ON_PREMISES_AGENT, FILE_AGENT] = Field(
            ..., description="Agent type"
        )

        # Agent status and health
        status: Literal[ONLINE, OFFLINE, ERROR, MAINTENANCE] = Field(
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

        @computed_field
        @property
        def agent_health_summary(self) -> dict[str, object]:
            """OIC agent health and connectivity summary."""
            health_status = "healthy"
            if self.status in {"ERROR", "OFFLINE"}:
                health_status = "unhealthy"
            elif self.last_error:
                health_status = "degraded"

            return {
                "agent_identity": {
                    "id": self.agent_id,
                    "name": self.agent_name,
                    "type": self.agent_type,
                    "version": self.version,
                    "status": self.status,
                },
                "connectivity": {
                    "host_machine": self.host_machine,
                    "port": self.port,
                    "last_heartbeat": self.last_heartbeat.isoformat()
                    if self.last_heartbeat
                    else None,
                    "connection_count": self.connection_count or 0,
                },
                "health": {
                    "health_status": health_status,
                    "uptime_hours": self.uptime_hours or 0.0,
                    "has_error": bool(self.last_error),
                    "last_error": self.last_error,
                },
                "configuration": {"installation_path": self.installation_path},
            }

        @model_validator(mode="after")
        def validate_agent_entity(self) -> Self:
            """Validate OIC agent entity."""
            if not self.agent_id:
                msg = "Agent ID is required"
                raise ValueError(msg)
            if not self.agent_name:
                msg = "Agent name is required"
                raise ValueError(msg)
            if self.port is not None and not (1 <= self.port <= 65535):
                msg = "Port must be between 1 and 65535"
                raise ValueError(msg)
            return self

    class OicStreamConfiguration(FlextModels.BaseConfig):
        """Configuration for OIC tap streams."""

        # Pydantic 2.11 Configuration - Stream Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "Oracle OIC tap stream configuration with filtering",
                "examples": [
                    {
                        "stream_name": "integrations",
                        "replication_method": "INCREMENTAL",
                        "replication_key": "last_updated",
                        "page_size": 100,
                    }
                ],
            },
        )

        stream_name: str = Field(..., description="Singer stream name")
        replication_method: Literal[FULL_TABLE, INCREMENTAL] = Field(
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

        @computed_field
        @property
        def stream_config_summary(self) -> dict[str, object]:
            """OIC stream configuration summary."""
            return {
                "stream_identity": {
                    "name": self.stream_name,
                    "replication_method": self.replication_method,
                    "replication_key": self.replication_key,
                    "is_incremental": self.replication_method == "INCREMENTAL",
                },
                "performance": {
                    "page_size": self.page_size,
                    "include_extended": self.include_extended,
                },
                "filtering": {
                    "status_filters": len(self.status_filter)
                    if self.status_filter
                    else 0,
                    "date_range_filter": bool(self.date_range_filter),
                    "exclude_test_entities": self.exclude_test_entities,
                },
                "security": {"sanitize_sensitive_data": self.sanitize_sensitive_data},
            }

        @model_validator(mode="after")
        def validate_stream_config(self) -> Self:
            """Validate OIC stream configuration."""
            if not self.stream_name:
                msg = "Stream name is required"
                raise ValueError(msg)
            if self.replication_method == "INCREMENTAL" and not self.replication_key:
                msg = "Incremental replication requires a replication key"
                raise ValueError(msg)
            if self.page_size <= 0 or self.page_size > 1000:
                msg = "Page size must be between 1 and 1000"
                raise ValueError(msg)
            return self

    class OicApiResponse(FlextModels.BaseModel):
        """Standardized OIC API response wrapper."""

        # Pydantic 2.11 Configuration - API Response Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "Oracle OIC API response with pagination and error handling",
                "examples": [
                    {
                        "success": True,
                        "total_count": 150,
                        "page_size": 50,
                        "page_number": 1,
                    }
                ],
            },
        )

        success: bool = Field(..., description="Response success indicator")
        data: object | None = Field(None, description="Response data payload")
        total_count: int | None = Field(
            None, description="Total entity count (for pagination)"
        )
        page_size: int | None = Field(None, description="Current page size")
        page_number: int | None = Field(None, description="Current page number")

        # Error information
        error_code: str | None = Field(None, description="Error code if failed")
        error_message: str | None = Field(None, description="Error message if failed")
        error_details: dict[str, object] | None = Field(
            None, description="Detailed error information"
        )

        # Metadata
        timestamp: datetime = Field(
            default_factory=datetime.utcnow, description="Response timestamp"
        )
        api_version: str | None = Field(None, description="OIC API version")
        request_id: str | None = Field(None, description="Request correlation ID")

        @computed_field
        @property
        def api_response_summary(self) -> dict[str, object]:
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
                    "has_more": bool(
                        self.total_count
                        and self.page_size
                        and (self.page_number or 1) * self.page_size < self.total_count
                    ),
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

        @model_validator(mode="after")
        def validate_api_response(self) -> Self:
            """Validate OIC API response."""
            if not self.success and not self.error_message:
                msg = "Failed responses must have an error message"
                raise ValueError(msg)
            if self.page_number is not None and self.page_number < 1:
                msg = "Page number must be positive"
                raise ValueError(msg)
            return self

    class OicErrorContext(FlextModels.BaseModel):
        """Error context for OIC API error handling."""

        # Pydantic 2.11 Configuration - Error Context Features
        model_config = ConfigDict(
            validate_assignment=True,
            extra="forbid",
            frozen=False,
            json_schema_extra={
                "description": "Oracle OIC API error context with recovery guidance",
                "examples": [
                    {
                        "error_type": "RATE_LIMIT",
                        "http_status_code": 429,
                        "retry_after_seconds": 60,
                        "is_retryable": True,
                    }
                ],
            },
        )

        error_type: Literal[
            AUTHENTICATION,
            AUTHORIZATION,
            RATE_LIMIT,
            SERVER_ERROR,
            NETWORK,
            VALIDATION,
        ] = Field(..., description="Error category")
        http_status_code: int | None = Field(None, description="HTTP status code")
        retry_after_seconds: int | None = Field(
            None, description="Retry after duration"
        )

        # Context information
        endpoint: str | None = Field(None, description="API endpoint that failed")
        request_method: str | None = Field(None, description="HTTP method used")
        request_params: dict[str, object] | None = Field(
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

        @computed_field
        @property
        def error_context_summary(self) -> dict[str, object]:
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

        def _determine_severity(self) -> str:
            """Determine error severity based on type and status code."""
            if self.error_type in {"AUTHENTICATION", "AUTHORIZATION"}:
                return "critical"
            if self.error_type == "RATE_LIMIT":
                return "warning"
            if self.error_type == "SERVER_ERROR":
                return "error"
            if self.error_type in {"NETWORK", "VALIDATION"}:
                return "warning"
            return "unknown"

        @model_validator(mode="after")
        def validate_error_context(self) -> Self:
            """Validate OIC error context."""
            if self.http_status_code is not None and not (
                100 <= self.http_status_code <= 599
            ):
                msg = "HTTP status code must be between 100 and 599"
                raise ValueError(msg)
            if self.retry_after_seconds is not None and self.retry_after_seconds < 0:
                msg = "Retry after seconds cannot be negative"
                raise ValueError(msg)
            return self


__all__ = [
    "FlextTapOracleOicModels",
]
