"""FLEXT Oracle OIC TAP Constants extending flext-core platform constants.

FLEXT Oracle OIC TAP specific constants that extend flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from enum import StrEnum
from typing import Final

from flext_core import FlextConstants
from flext_oracle_oic.constants import FlextOracleOicConstants as ParentOicConstants


class FlextTapOracleOicConstants(FlextConstants):
    """FLEXT Oracle OIC TAP constants extending flext-core platform constants.

    Composes with FlextOracleOicConstants to avoid duplication and ensure consistency.
    """

    # Oracle OIC API Constants using composition
    OIC_API_BASE_PATH: Final[str] = (
        ParentOicConstants.API.ENDPOINT_INTEGRATIONS.replace("/integrations", "")
    )
    OIC_MONITORING_API_PATH: Final[str] = "/ic/api/integration/v1/monitoring"
    OIC_DESIGNTIME_API_PATH: Final[str] = "/ic/api/integration/v1/designtime"
    OIC_PROCESS_API_PATH: Final[str] = "/ic/api/integration/v1/processes"
    OIC_B2B_API_PATH: Final[str] = "/ic/api/integration/v1/b2b"
    OIC_ENVIRONMENT_API_PATH: Final[str] = "/ic/api/integration/v1/environments"

    # Official OIC REST API Endpoints using composition where appropriate
    OIC_ENDPOINTS: Final[dict[str, str]] = {
        # Core Integration APIs
        "integrations": "/integrations",
        "integrations_detail": "/integrations/{id}",
        "integrations_status": "/integrations/{id}/status",
        "integrations_archive": "/integrations/{id}/archive",
        # Connection APIs
        "connections": "/connections",
        "connections_detail": "/connections/{id}",
        "connections_test": "/connections/{id}/test",
        # Package APIs
        "packages": "/packages",
        "packages_detail": "/packages/{id}",
        "packages_export": "/packages/export",
        "packages_import": "/packages/import",
        # Monitoring APIs (v1) - correct paths according to Oracle docs
        "monitoring_instances": "/monitoring/instances",
        "monitoring_instances_detail": "/monitoring/instances/{id}",
        "monitoring_messages": "/monitoring/messages",
        "monitoring_errors": "/monitoring/errors",
        "monitoring_activity": "/monitoring/activity",
        "audit_records": "/audit/events",
        "usage_analytics": "/monitoring/usage",
        # Lookup APIs
        "lookups": "/lookups",
        "lookup_values": "/lookups/{name}/values",
        # Library APIs
        "libraries": "/libraries",
        "libraries_detail": "/libraries/{id}",
        # Agent Group APIs
        "agent_groups": "/agentGroups",
        "agent_groups_detail": "/agentGroups/{id}",
        # Certificate APIs
        "certificates": "/certificates",
        "certificates_detail": "/certificates/{alias}",
        # Adapter APIs
        "adapters": "/adapters",
        "adapters_detail": "/adapters/{id}",
        # Process Management APIs
        "process_definitions": "/process-definitions",
        "process_definitions_detail": "/process-definitions/{id}",
        "processes": "/processes",
        "processes_detail": "/processes/{id}",
        "process_instances": "/processes/{id}/instances",
        "tasks": "/tasks",
        "tasks_detail": "/tasks/{id}",
        "spaces": "/spaces",
        "spaces_detail": "/spaces/{id}",
        # B2B Trading Partner APIs
        "trading_partners": "/tpm/partners",
        "trading_partners_detail": "/tpm/partners/{id}",
        "document_types": "/tpm/documents",
        "document_types_detail": "/tpm/documents/{id}",
        "business_messages": "/monitoring/business-messages",
        "wire_messages": "/monitoring/wire-messages",
        # Environment APIs
        "cors_domains": "/cors-domains",
        # System APIs
        "health": "/health",
        "metadata": "/metadata",
        # Execution logs
        "execution_logs": "/monitoring/logs",
        "execution_logs_detail": "/monitoring/logs/{id}",
        # Lookup details
        "lookup_usage": "/lookups/{name}/usage",
    }

    class TapOracleOic:
        """OIC connection configuration."""

        DEFAULT_TIMEOUT: Final[int] = ParentOicConstants.OracleOic.DEFAULT_TIMEOUT
        DEFAULT_MAX_RETRIES: Final[int] = (
            ParentOicConstants.OracleOic.DEFAULT_MAX_RETRIES
        )
        DEFAULT_VERIFY_SSL: Final[bool] = (
            ParentOicConstants.OracleOic.DEFAULT_VERIFY_SSL
        )

    class TapOicProcessing:
        """OIC tap processing configuration.

        Note: Does not override parent Processing class to avoid inheritance conflicts.
        """

        DEFAULT_PAGE_SIZE: Final[int] = ParentOicConstants.OracleOic.DEFAULT_PAGE_SIZE
        MAX_PAGE_SIZE: Final[int] = ParentOicConstants.OracleOic.MAX_PAGE_SIZE
        MIN_PAGE_SIZE: Final[int] = ParentOicConstants.OracleOic.MIN_PAGE_SIZE

    class TapOicAuth:
        """OIC authentication configuration.

        Note: Does not override parent Auth class to avoid inheritance conflicts.
        """

        DEFAULT_OAUTH_CLIENT_ID: Final[str] = (
            ParentOicConstants.Auth.DEFAULT_OAUTH_CLIENT_ID
        )
        DEFAULT_OAUTH_TOKEN_URL: Final[str] = (
            ParentOicConstants.Auth.DEFAULT_OAUTH_TOKEN_URL
        )
        DEFAULT_TOKEN_EXPIRY_SECONDS: Final[int] = (
            ParentOicConstants.Auth.DEFAULT_TOKEN_EXPIRY_SECONDS
        )

    class TapOicValidation:
        """OIC tap validation constants."""

        MAX_STREAM_PREFIX_LENGTH: Final[int] = 255
        MIN_DATE_LENGTH: Final[int] = 10  # YYYY-MM-DD format

    # =========================================================================
    # STRENUM CLASSES - Single source of truth for string enumerations
    # =========================================================================

    class OICResourceType(StrEnum):
        """Oracle Integration Cloud resource types.

        DRY Pattern:
            StrEnum is the single source of truth. Use OICResourceType.INTEGRATION.value
            or OICResourceType.INTEGRATION directly - no base strings needed.
        """

        INTEGRATION = "integration"
        CONNECTION = "connection"
        LOOKUP = "lookup"
        LIBRARY = "library"
        AGENT = "agent"
        CERTIFICATE = "certificate"
        PACKAGE = "package"
        PROJECT = "project"

    class IntegrationStatus(StrEnum):
        """Integration lifecycle status.

        DRY Pattern:
            StrEnum is the single source of truth. Use IntegrationStatus.ACTIVATED.value
            or IntegrationStatus.ACTIVATED directly - no base strings needed.
        """

        CONFIGURED = "configured"
        ACTIVATED = "activated"
        DEACTIVATED = "deactivated"
        FAILED = "failed"
        LOCKED = "locked"

    class ConnectionStatus(StrEnum):
        """Connection status.

        DRY Pattern:
            StrEnum is the single source of truth. Use ConnectionStatus.TESTED.value
            or ConnectionStatus.TESTED directly - no base strings needed.
        """

        CONFIGURED = "configured"
        TESTED = "tested"
        FAILED = "failed"

    class OicIntegrationStatus(StrEnum):
        """OIC integration lifecycle status using StrEnum for type safety."""

        ACTIVE = "ACTIVE"
        INACTIVE = "INACTIVE"
        DRAFT = "DRAFT"
        ERROR = "ERROR"
        TESTING = "TESTING"
        DEPRECATED = "DEPRECATED"

    class OicJobStatus(StrEnum):
        """OIC job execution status using StrEnum for type safety."""

        RUNNING = "RUNNING"
        COMPLETED = "COMPLETED"
        FAILED = "FAILED"
        ABORTED = "ABORTED"
        SUSPENDED = "SUSPENDED"

    class OicIntegrationType(StrEnum):
        """OIC integration type using StrEnum for type safety."""

        INTEGRATION = "INTEGRATION"
        LIBRARY = "LIBRARY"
        TEMPLATE = "TEMPLATE"
        RECIPE = "RECIPE"
        CONNECTIVITY_AGENT = "CONNECTIVITY_AGENT"

    class OicAgentType(StrEnum):
        """OIC agent type using StrEnum for type safety."""

        ON_PREMISES_AGENT = "ON_PREMISES_AGENT"
        FILE_AGENT = "FILE_AGENT"

    class OicAgentStatus(StrEnum):
        """OIC agent operational status using StrEnum for type safety."""

        ONLINE = "ONLINE"
        OFFLINE = "OFFLINE"
        MAINTENANCE = "MAINTENANCE"

    class OicReplicationMethod(StrEnum):
        """Replication method types using StrEnum for type safety."""

        FULL_TABLE = "FULL_TABLE"
        INCREMENTAL = "INCREMENTAL"

    class OicErrorType(StrEnum):
        """Error type constants using StrEnum for type safety."""

        AUTHENTICATION = "AUTHENTICATION"
        AUTHORIZATION = "AUTHORIZATION"
        RATE_LIMIT = "RATE_LIMIT"
        SERVER_ERROR = "SERVER_ERROR"
        NETWORK = "NETWORK"
        VALIDATION = "VALIDATION"


c = FlextTapOracleOicConstants

__all__: list[str] = [
    "FlextTapOracleOicConstants",
    "c",
]
