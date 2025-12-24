"""Domain entities for FLEXT-TAP-ORACLE-OIC v0.7.0 using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from datetime import UTC, datetime

from flext_core import FlextModels, FlextResult
from pydantic import ConfigDict, Field

from flext_tap_oracle_oic.constants import c

# Aliases from constants.py (single source of truth)
OICResourceType = c.OICResourceType
IntegrationStatus = c.IntegrationStatus
ConnectionStatus = c.ConnectionStatus


class OICConnection(FlextModels):
    """OIC connection domain entity using flext-core patterns."""

    model_config: dict[str, object] = ConfigDict(frozen=False)

    connection_id: str = Field(
        ...,
        min_length=1,
        description="OIC connection identifier",
    )
    adapter_type: str = Field(
        ...,
        min_length=1,
        description="Adapter type (e.g., REST, SOAP, DB)",
    )
    name: str = Field(..., min_length=1, description="Connection name")

    # Connection properties
    connection_url: str | None = Field(None, description="Connection endpoint URL")
    connection_properties: dict[str, object] = Field(
        default_factory=dict,
        description="Connection properties",
    )
    security_policy: str | None = Field(None, description="Security policy name")

    # Connection state
    connection_status: ConnectionStatus = Field(
        default=ConnectionStatus.CONFIGURED,
        description="Connection status",
    )
    last_tested: datetime | None = Field(None, description="Last test timestamp")
    test_result: dict[str, object] | None = Field(
        None,
        description="Last test result",
    )

    # Metadata
    version: str | None = Field(None, description="Connection version")
    locked_by: str | None = Field(None, description="User who locked the connection")
    locked_at: datetime | None = Field(None, description="Lock timestamp")
    created_at: datetime | None = Field(None, description="Creation timestamp")
    updated_at: datetime | None = Field(None, description="Last update timestamp")

    def test_connection(self: object) -> None:
        """Mark connection as tested."""
        self.last_tested = datetime.now(UTC)
        self.connection_status = ConnectionStatus.TESTED

    def mark_failed(self, _error: str) -> None:
        """Mark connection as failed with error details."""
        self.connection_status = ConnectionStatus.FAILED
        self.test_result: FlextResult[object] = {
            "error": "error",
            "timestamp": datetime.now(UTC).isoformat(),
        }


class OICIntegration(FlextModels):
    """OIC integration domain entity using flext-core patterns."""

    model_config: dict[str, object] = ConfigDict(frozen=False)

    integration_id: str = Field(
        ...,
        min_length=1,
        description="OIC integration identifier",
    )
    integration_code: str = Field(..., min_length=1, description="Integration code")
    name: str = Field(..., min_length=1, description="Integration name")
    package_name: str | None = Field(None, description="Package name")
    project_name: str | None = Field(None, description="Project name")

    # Integration details
    integration_type: str = Field(
        ...,
        description="Integration type (e.g., APP_DRIVEN, SCHEDULED)",
    )
    pattern: str | None = Field(None, description="Integration pattern")
    style: str | None = Field(None, description="Integration style")

    # Configuration
    endpoint_url: str | None = Field(None, description="Integration endpoint URL")
    tracking_level: str | None = Field(None, description="Tracking level")
    payload_tracking: bool = Field(default=False, description="Enable payload tracking")

    # State
    integration_status: IntegrationStatus = Field(
        default=IntegrationStatus.CONFIGURED,
        description="Integration status",
    )
    activated_at: datetime | None = Field(None, description="Activation timestamp")
    deactivated_at: datetime | None = Field(None, description="Deactivation timestamp")

    # Version control
    version: str = Field(default="01.00.0000", description="Integration version")
    locked_by: str | None = Field(None, description="User who locked the integration")
    locked_at: datetime | None = Field(None, description="Lock timestamp")

    # Connections
    connection_ids: list[str] = Field(
        default_factory=list,
        description="Associated connection IDs",
    )

    # Metadata
    created_at: datetime | None = Field(None, description="Creation timestamp")
    updated_at: datetime | None = Field(None, description="Last update timestamp")

    def activate(self: object) -> None:
        """Activate the integration."""
        self.integration_status = IntegrationStatus.ACTIVATED
        self.activated_at = datetime.now(UTC)

    def deactivate(self: object) -> None:
        """Deactivate the integration."""
        self.integration_status = IntegrationStatus.DEACTIVATED
        self.deactivated_at = datetime.now(UTC)

    def lock(self, user: str) -> None:
        """Lock the integration for a specific user."""
        self.locked_by = user
        self.locked_at = datetime.now(UTC)
        self.integration_status = IntegrationStatus.LOCKED

    def unlock(self: object) -> None:
        """Unlock the integration."""
        self.locked_by = None
        self.locked_at = None

    @property
    def is_active(self: object) -> bool:
        """Check if integration is active."""
        return self.integration_status == IntegrationStatus.ACTIVATED


class OICLookup(FlextModels):
    """OIC lookup table domain entity using flext-core patterns."""

    model_config: dict[str, object] = ConfigDict(frozen=False)

    lookup_id: str = Field(..., min_length=1, description="OIC lookup identifier")
    lookup_name: str = Field(..., min_length=1, description="Lookup table name")
    domain_name: str | None = Field(None, description="Domain name")

    # Lookup structure
    columns: list[dict[str, object]] = Field(
        default_factory=list,
        description="Column definitions",
    )
    key_columns: list[str] = Field(
        default_factory=list,
        description="Key column names",
    )
    value_columns: list[str] = Field(
        default_factory=list,
        description="Value column names",
    )

    # Data
    row_count: int = Field(default=0, ge=0, description="Number of rows")
    data_size_bytes: int | None = Field(None, ge=0, description="Data size in bytes")

    # State
    locked_by: str | None = Field(None, description="User who locked the lookup")
    locked_at: datetime | None = Field(None, description="Lock timestamp")
    last_imported: datetime | None = Field(None, description="Last import timestamp")

    # Metadata
    created_at: datetime | None = Field(None, description="Creation timestamp")
    updated_at: datetime | None = Field(None, description="Last update timestamp")

    def update_statistics(self, row_count: int, data_size: int | None = None) -> None:
        """Update lookup statistics."""
        self.row_count = row_count
        self.data_size_bytes = data_size

    def record_import(self: object) -> None:
        """Record successful import."""
        self.last_imported = datetime.now(UTC)

    @property
    def is_empty(self: object) -> bool:
        """Check if lookup is empty."""
        return self.row_count == 0


class OICMonitoringRecord(FlextModels):
    """OIC monitoring record domain entity using flext-core patterns."""

    instance_id: str = Field(..., min_length=1, description="Flow instance ID")
    integration_id: str = Field(..., description="Associated integration ID")

    # Execution details
    flow_id: str | None = Field(None, description="Flow ID")
    tracking_level: str | None = Field(None, description="Tracking level")

    # Timing
    started_at: datetime = Field(..., description="Execution start time")
    completed_at: datetime | None = Field(None, description="Execution completion time")
    duration_ms: int | None = Field(None, ge=0, description="Duration in milliseconds")

    # Status
    execution_status: str = Field(..., description="Execution status")
    error_code: str | None = Field(None, description="Error code if failed")
    error_message: str | None = Field(None, description="Error message if failed")

    # Metrics
    message_count: int = Field(
        default=0,
        ge=0,
        description="Number of messages processed",
    )
    error_count: int = Field(default=0, ge=0, description="Number of errors")

    # Tracking
    business_identifiers: dict[str, object] = Field(
        default_factory=dict,
        description="Business tracking identifiers",
    )

    @property
    def successful(self: object) -> bool:
        """Check if execution was successful."""
        return self.execution_status.lower() in {"completed", "succeeded"}

    @property
    def is_failed(self: object) -> bool:
        """Check if execution failed."""
        return self.execution_status.lower() in {"failed", "faulted", "aborted"}

    @property
    def duration_seconds(self: object) -> float | None:
        """Get duration in seconds."""
        return self.duration_ms / 1000.0 if self.duration_ms is not None else None


class OICProject(FlextModels):
    """OIC project domain entity using flext-core patterns."""

    model_config: dict[str, object] = ConfigDict(frozen=False)

    project_id: str = Field(..., min_length=1, description="OIC project identifier")
    project_code: str = Field(..., min_length=1, description="Project code")
    name: str = Field(..., min_length=1, description="Project name")

    # Project resources
    integration_ids: list[str] = Field(
        default_factory=list,
        description="Integration IDs in project",
    )
    connection_ids: list[str] = Field(
        default_factory=list,
        description="Connection IDs in project",
    )
    lookup_ids: list[str] = Field(
        default_factory=list,
        description="Lookup IDs in project",
    )

    # Deployment
    deployment_status: str | None = Field(None, description="Deployment status")
    deployed_at: datetime | None = Field(None, description="Deployment timestamp")
    deployed_by: str | None = Field(None, description="User who deployed")

    # Metadata
    created_at: datetime | None = Field(None, description="Creation timestamp")
    updated_at: datetime | None = Field(None, description="Last update timestamp")

    def add_integration(self, integration_id: str) -> None:
        """Add integration to project."""
        if integration_id not in self.integration_ids:
            self.integration_ids.append(integration_id)

    def remove_integration(self, integration_id: str) -> None:
        """Remove integration from project."""
        if integration_id in self.integration_ids:
            self.integration_ids.remove(integration_id)

    def deploy(self, user: str) -> None:
        """Deploy the project."""
        self.deployment_status = "deployed"
        self.deployed_at = datetime.now(UTC)
        self.deployed_by = user

    @property
    def total_resources(self: object) -> int:
        """Get total number of resources in project."""
        return (
            len(self.integration_ids) + len(self.connection_ids) + len(self.lookup_ids)
        )


# Value Objects for configuration and metadata
class OICResourceMetadata(FlextModels):
    """OIC resource metadata value object."""

    resource_type: OICResourceType = Field(..., description="Resource type")
    resource_id: str = Field(..., min_length=1, description="Resource identifier")
    name: str = Field(..., min_length=1, description="Resource name")
    version: str | None = Field(None, description="Resource version")
    created_at: datetime | None = Field(None, description="Creation timestamp")
    updated_at: datetime | None = Field(None, description="Last update timestamp")


class OICExecutionSummary(FlextModels):
    """OIC execution summary value object."""

    integration_id: str = Field(..., description="Integration ID")
    total_executions: int = Field(
        default=0,
        ge=0,
        description="Total number of executions",
    )
    successful_executions: int = Field(
        default=0,
        ge=0,
        description="Successful executions",
    )
    failed_executions: int = Field(default=0, ge=0, description="Failed executions")
    average_duration_ms: float | None = Field(
        None,
        ge=0,
        description="Average execution duration",
    )
    last_execution_at: datetime | None = Field(
        None,
        description="Last execution timestamp",
    )

    @property
    def success_rate(self: object) -> float:
        """Calculate success rate percentage."""
        if self.total_executions == 0:
            return 0.0
        return (self.successful_executions / self.total_executions) * 100.0

    @property
    def failure_rate(self: object) -> float:
        """Calculate failure rate percentage."""
        return 100.0 - self.success_rate


# Export main entities and value objects
__all__: list[str] = [
    "ConnectionStatus",
    "IntegrationStatus",
    "OICConnection",
    "OICExecutionSummary",
    "OICIntegration",
    "OICLookup",
    "OICMonitoringRecord",
    "OICProject",
    "OICResourceMetadata",
    "OICResourceType",
]
