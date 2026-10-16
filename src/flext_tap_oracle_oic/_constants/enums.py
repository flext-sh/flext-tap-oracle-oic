"""OIC tap domain enumerations.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from enum import StrEnum, unique


class FlextTapOracleOicConstantsEnums:
    """OIC tap domain enumerations composed into ``c.TapOracleOic``."""

    @unique
    class OicIntegrationStatus(StrEnum):
        """OIC integration lifecycle status."""

        CONFIGURED = "CONFIGURED"
        ACTIVATED = "ACTIVATED"
        DEACTIVATED = "DEACTIVATED"
        DRAFT = "DRAFT"
        ERROR = "ERROR"
        FAILED = "FAILED"
        LOCKED = "LOCKED"

    @unique
    class OicJobStatus(StrEnum):
        """OIC job/activity execution status."""

        COMPLETED = "COMPLETED"
        FAILED = "FAILED"
        RUNNING = "RUNNING"
        PENDING = "PENDING"
        ABORTED = "ABORTED"

    @unique
    class OicIntegrationType(StrEnum):
        """OIC integration/package type."""

        APP_DRIVEN = "APP_DRIVEN"
        SCHEDULED = "SCHEDULED"
        INTEGRATION = "INTEGRATION"
        BASIC = "BASIC"
        PUBLISH = "PUBLISH"

    @unique
    class OicAgentType(StrEnum):
        """OIC connectivity agent type."""

        CONNECTIVITY_AGENT = "CONNECTIVITY_AGENT"

    @unique
    class OicAgentStatus(StrEnum):
        """OIC agent operational status."""

        ONLINE = "ONLINE"
        OFFLINE = "OFFLINE"
        ERROR = "ERROR"

    @unique
    class OicHealthStatus(StrEnum):
        """OIC health status values for operational summaries."""

        HEALTHY = "healthy"
        UNHEALTHY = "unhealthy"
        WARNING = "warning"
        UNKNOWN = "unknown"
        DEGRADED = "degraded"

    @unique
    class OicErrorSeverity(StrEnum):
        """OIC error severity values for classification."""

        CRITICAL = "critical"
        WARNING = "warning"
        ERROR = "error"
        UNKNOWN = "unknown"

    @unique
    class OicConnectionTestStatus(StrEnum):
        """Connection test status values."""

        SUCCESS = "success"
        FAILED = "failed"
        ERROR = "error"

    @unique
    class OicReplicationMethod(StrEnum):
        """Singer replication method for OIC streams."""

        FULL_TABLE = "FULL_TABLE"
        INCREMENTAL = "INCREMENTAL"
        LOG_BASED = "LOG_BASED"

    @unique
    class OICResourceType(StrEnum):
        """Oracle Integration Cloud resource types.

        DRY Pattern:
            StrEnum is the single source of truth. Use
            OICResourceType.INTEGRATION.value or OICResourceType.INTEGRATION
            directly - no base strings needed.

        """

        INTEGRATION = "integration"
        CONNECTION = "connection"
        CERTIFICATE = "certificate"
        PACKAGE = "package"
        PROJECT = "project"

    @unique
    class IntegrationStatus(StrEnum):
        """Integration lifecycle status.

        DRY Pattern:
            StrEnum is the single source of truth. Use
            IntegrationStatus.ACTIVATED.value or IntegrationStatus.ACTIVATED
            directly - no base strings needed.

        """

        CONFIGURED = "configured"
        ACTIVATED = "activated"
        DEACTIVATED = "deactivated"
        FAILED = "failed"
        LOCKED = "locked"

    @unique
    class ConnectionStatus(StrEnum):
        """Connection status.

        DRY Pattern:
            StrEnum is the single source of truth. Use ConnectionStatus.TESTED.value
            or ConnectionStatus.TESTED directly - no base strings needed.

        """

        CONFIGURED = "configured"
        TESTED = "tested"
        FAILED = "failed"

    @unique
    class OicErrorType(StrEnum):
        """Error type constants using StrEnum for type safety."""

        AUTHENTICATION = "AUTHENTICATION"
        AUTHORIZATION = "AUTHORIZATION"
        RATE_LIMIT = "RATE_LIMIT"
        SERVER_ERROR = "SERVER_ERROR"
        NETWORK = "NETWORK"
        VALIDATION = "VALIDATION"


__all__: list[str] = [
    "ConnectionStatus",
    "FlextTapOracleOicConstantsEnums",
    "IntegrationStatus",
    "OICResourceType",
    "OicAgentStatus",
    "OicAgentType",
    "OicConnectionTestStatus",
    "OicErrorSeverity",
    "OicErrorType",
    "OicHealthStatus",
    "OicIntegrationStatus",
    "OicIntegrationType",
    "OicJobStatus",
    "OicReplicationMethod",
]
