"""FLEXT Oracle OIC TAP Constants extending flext-core platform constants.

FLEXT Oracle OIC TAP specific constants that extend flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from enum import StrEnum, unique
from typing import Final

from flext_core.constants import (
    PROJECT_KIND_APPLICATION,
    PROJECT_KIND_LIBRARY,
    PROJECT_KIND_SERVICE,
)
from flext_meltano import FlextMeltanoConstants
from flext_oracle_oic import FlextOracleOicConstants
from flext_oracle_oic.constants import FlextOracleOicConstants as ParentOicConstants


class FlextTapOracleOicConstants(FlextMeltanoConstants, FlextOracleOicConstants):
    """FLEXT Oracle OIC TAP constants extending flext-core platform constants.

    Composes with FlextOracleOicConstants to avoid duplication and ensure consistency.
    """

    OIC_API_BASE_PATH: Final[str] = (
        ParentOicConstants.API.ENDPOINT_INTEGRATIONS.replace("/integrations", "")
    )
    OIC_MONITORING_API_PATH: Final[str] = "/ic/api/integration/v1/monitoring"
    OIC_DESIGNTIME_API_PATH: Final[str] = "/ic/api/integration/v1/designtime"
    OIC_PROCESS_API_PATH: Final[str] = "/ic/api/integration/v1/processes"
    OIC_B2B_API_PATH: Final[str] = "/ic/api/integration/v1/b2b"
    OIC_ENVIRONMENT_API_PATH: Final[str] = "/ic/api/integration/v1/environments"
    OIC_ENDPOINTS: Final[dict[str, str]] = {
        "integrations": "/integrations",
        "integrations_detail": "/integrations/{id}",
        "integrations_status": "/integrations/{id}/status",
        "integrations_archive": "/integrations/{id}/archive",
        "connections": "/connections",
        "connections_detail": "/connections/{id}",
        "connections_test": "/connections/{id}/test",
        "packages": "/packages",
        "packages_detail": "/packages/{id}",
        "packages_export": "/packages/export",
        "packages_import": "/packages/import",
        "monitoring_instances": "/monitoring/instances",
        "monitoring_instances_detail": "/monitoring/instances/{id}",
        "monitoring_messages": "/monitoring/messages",
        "monitoring_errors": "/monitoring/errors",
        "monitoring_activity": "/monitoring/activity",
        "audit_records": "/audit/events",
        "usage_analytics": "/monitoring/usage",
        "lookups": "/lookups",
        "lookup_values": "/lookups/{name}/values",
        "libraries": "/libraries",
        "libraries_detail": "/libraries/{id}",
        "agent_groups": "/agentGroups",
        "agent_groups_detail": "/agentGroups/{id}",
        "certificates": "/certificates",
        "certificates_detail": "/certificates/{alias}",
        "adapters": "/adapters",
        "adapters_detail": "/adapters/{id}",
        "process_definitions": "/process-definitions",
        "process_definitions_detail": "/process-definitions/{id}",
        "processes": "/processes",
        "processes_detail": "/processes/{id}",
        "process_instances": "/processes/{id}/instances",
        "tasks": "/tasks",
        "tasks_detail": "/tasks/{id}",
        "spaces": "/spaces",
        "spaces_detail": "/spaces/{id}",
        "trading_partners": "/tpm/partners",
        "trading_partners_detail": "/tpm/partners/{id}",
        "document_types": "/tpm/documents",
        "document_types_detail": "/tpm/documents/{id}",
        "business_messages": "/monitoring/business-messages",
        "wire_messages": "/monitoring/wire-messages",
        "cors_domains": "/cors-domains",
        "health": "/health",
        "metadata": "/metadata",
        "execution_logs": "/monitoring/logs",
        "execution_logs_detail": "/monitoring/logs/{id}",
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
        DEFAULT_PAGINATOR_START: Final[int] = 0
        DEFAULT_PAGINATOR_PAGE_SIZE: Final[int] = 100
        PAGINATOR_MAX_PAGE_SIZE: Final[int] = 1000
        PAGINATOR_MIN_PAGE_SIZE: Final[int] = 10

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

    class TapOicHttp:
        """HTTP status codes and MIME types for OIC API communication."""

        HTTP_OK: Final[int] = 200
        HTTP_UNAUTHORIZED: Final[int] = 401
        HTTP_FORBIDDEN: Final[int] = 403
        HTTP_ERROR_STATUS_THRESHOLD: Final[int] = 400
        HTTP_RATE_LIMITED: Final[int] = 429
        JSON_MIME: Final[str] = "application/json"

    class TapOicValidation:
        """OIC tap validation constants."""

        MAX_STREAM_PREFIX_LENGTH: Final[int] = 255
        MIN_DATE_LENGTH: Final[int] = 10
        MIN_TOKEN_EXPIRY_BUFFER: Final[int] = 60
        MIN_PERCENTAGE: Final[float] = 0.0
        MAX_PERCENTAGE: Final[float] = 100.0

    class TapOicPerformance:
        """OIC tap performance and monitoring constants."""

        RESPONSE_TIME_HISTORY_SIZE: Final[int] = 10
        MIN_RESPONSE_SAMPLES: Final[int] = 5
        SLOW_RESPONSE_THRESHOLD: Final[float] = 5.0
        MAX_SAFE_PARALLEL_STREAMS: Final[int] = 4
        MIN_PERCENTAGE: Final[float] = 0.0
        MAX_PERCENTAGE: Final[float] = 100.0

    @unique
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

    @unique
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
    class OicIntegrationStatus(StrEnum):
        """OIC integration lifecycle status using StrEnum for type safety."""

        ACTIVE = "ACTIVE"
        INACTIVE = "INACTIVE"
        DRAFT = "DRAFT"
        ERROR = "ERROR"
        TESTING = "TESTING"
        DEPRECATED = "DEPRECATED"

    @unique
    class OicJobStatus(StrEnum):
        """OIC job execution status using StrEnum for type safety."""

        RUNNING = "RUNNING"
        COMPLETED = "COMPLETED"
        FAILED = "FAILED"
        ABORTED = "ABORTED"
        SUSPENDED = "SUSPENDED"

    @unique
    class OicIntegrationType(StrEnum):
        """OIC integration type using StrEnum for type safety."""

        INTEGRATION = "INTEGRATION"
        LIBRARY = "LIBRARY"
        TEMPLATE = "TEMPLATE"
        RECIPE = "RECIPE"
        CONNECTIVITY_AGENT = "CONNECTIVITY_AGENT"

    @unique
    class OicAgentType(StrEnum):
        """OIC agent type using StrEnum for type safety."""

        ON_PREMISES_AGENT = "ON_PREMISES_AGENT"
        FILE_AGENT = "FILE_AGENT"

    @unique
    class OicAgentStatus(StrEnum):
        """OIC agent operational status using StrEnum for type safety."""

        ONLINE = "ONLINE"
        OFFLINE = "OFFLINE"
        MAINTENANCE = "MAINTENANCE"

    @unique
    class OicReplicationMethod(StrEnum):
        """Replication method types using StrEnum for type safety."""

        FULL_TABLE = "FULL_TABLE"
        INCREMENTAL = "INCREMENTAL"

    @unique
    class OicErrorType(StrEnum):
        """Error type constants using StrEnum for type safety."""

        AUTHENTICATION = "AUTHENTICATION"
        AUTHORIZATION = "AUTHORIZATION"
        RATE_LIMIT = "RATE_LIMIT"
        SERVER_ERROR = "SERVER_ERROR"
        NETWORK = "NETWORK"
        VALIDATION = "VALIDATION"

    @unique
    class TapOracleOicProjectType(StrEnum):
        """Project type literals for tap package metadata."""

        LIBRARY = PROJECT_KIND_LIBRARY
        APPLICATION = PROJECT_KIND_APPLICATION
        SERVICE = PROJECT_KIND_SERVICE
        SINGER_TAP = "singer-tap"
        OIC_EXTRACTOR = "oic-extractor"
        INTEGRATION_EXTRACTOR = "integration-extractor"
        SINGER_TAP_ORACLE_OIC = "singer-tap-oracle-oic"
        TAP_ORACLE_OIC = "tap-oracle-oic"
        OIC_CONNECTOR = "oic-connector"
        INTEGRATION_CONNECTOR = "integration-connector"
        SINGER_PROTOCOL = "singer-protocol"
        OIC_INTEGRATION = "oic-integration"
        ORACLE_OIC = "oracle-oic"
        CLOUD_INTEGRATION = "cloud-integration"
        SINGER_STREAM = "singer-stream"
        ETL_TAP = "etl-tap"
        DATA_PIPELINE = "data-pipeline"
        OIC_TAP = "oic-tap"
        SINGER_INTEGRATION = "singer-integration"

    @unique
    class OicIntegrationStatusLiteral(StrEnum):
        """Oracle OIC integration status literals."""

        ACTIVE = "ACTIVE"
        INACTIVE = "INACTIVE"
        DRAFT = "DRAFT"
        ERROR = "ERROR"
        TESTING = "TESTING"
        DEPRECATED = "DEPRECATED"

    @unique
    class OicJobStatusLiteral(StrEnum):
        """Oracle OIC job status literals."""

        RUNNING = "RUNNING"
        COMPLETED = "COMPLETED"
        FAILED = "FAILED"
        ABORTED = "ABORTED"
        SUSPENDED = "SUSPENDED"

    @unique
    class OicIntegrationTypeLiteral(StrEnum):
        """Oracle OIC integration type literals."""

        INTEGRATION = "INTEGRATION"
        LIBRARY = "LIBRARY"
        TEMPLATE = "TEMPLATE"
        RECIPE = "RECIPE"
        CONNECTIVITY_AGENT = "CONNECTIVITY_AGENT"

    @unique
    class OicAgentTypeLiteral(StrEnum):
        """Oracle OIC agent type literals."""

        ON_PREMISES_AGENT = "ON_PREMISES_AGENT"
        FILE_AGENT = "FILE_AGENT"

    @unique
    class OicAgentStatusLiteral(StrEnum):
        """Oracle OIC agent status literals."""

        ONLINE = "ONLINE"
        OFFLINE = "OFFLINE"
        MAINTENANCE = "MAINTENANCE"

    @unique
    class OicReplicationMethodLiteral(StrEnum):
        """Replication strategy literals for OIC extraction."""

        FULL_TABLE = "FULL_TABLE"
        INCREMENTAL = "INCREMENTAL"

    @unique
    class OicErrorTypeLiteral(StrEnum):
        """Error category literals for OIC operations."""

        AUTHENTICATION = "AUTHENTICATION"
        AUTHORIZATION = "AUTHORIZATION"
        RATE_LIMIT = "RATE_LIMIT"
        SERVER_ERROR = "SERVER_ERROR"
        NETWORK = "NETWORK"
        VALIDATION = "VALIDATION"


c = FlextTapOracleOicConstants
__all__: list[str] = ["FlextTapOracleOicConstants", "c"]
