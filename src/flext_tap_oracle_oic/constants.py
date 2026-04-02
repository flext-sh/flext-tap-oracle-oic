"""FLEXT Oracle OIC TAP Constants extending flext-core platform constants.

FLEXT Oracle OIC TAP specific constants that extend flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from enum import StrEnum, unique
from typing import TYPE_CHECKING, Final

from flext_meltano import FlextMeltanoConstants
from flext_oracle_oic import FlextOracleOicConstants

if TYPE_CHECKING:
    from flext_tap_oracle_oic import t


class FlextTapOracleOicConstants(FlextMeltanoConstants, FlextOracleOicConstants):
    """FLEXT Oracle OIC TAP constants extending flext-core platform constants.

    Composes with FlextOracleOicConstants to avoid duplication and ensure consistency.
    """

    OIC_API_BASE_PATH: Final[str] = "/ic/api/integration/v1"
    OIC_MONITORING_API_PATH: Final[str] = "/ic/api/monitoring/v1"
    OIC_B2B_API_PATH: Final[str] = "/ic/api/b2b/v1"
    OIC_PROCESS_API_PATH: Final[str] = "/ic/api/process/v1"

    class TapOracleOic:
        """OIC connection configuration."""

        DEFAULT_TIMEOUT: Final[int] = (
            FlextOracleOicConstants.OracleOic.MIN_REQUEST_TIMEOUT
        )
        DEFAULT_MAX_RETRIES: Final[int] = 3
        DEFAULT_VERIFY_SSL: Final[bool] = True

        CORE_STREAMS: Final[list[str]] = [
            "integrations",
            "connections",
            "packages",
            "lookups",
            "libraries",
        ]
        INFRASTRUCTURE_STREAMS: Final[list[str]] = ["certificates", "adapters"]
        EXTENDED_STREAMS: Final[list[str]] = ["projects"]
        MONITORING_STREAMS: Final[list[str]] = ["executions", "metrics"]

        class TapOicProcessing:
            """OIC tap processing configuration.

            Note: Does not override parent Processing class to avoid inheritance conflicts.
            """

            DEFAULT_PAGE_SIZE: Final[int] = (
                FlextOracleOicConstants.OracleOic.DEFAULT_PAGE_SIZE
            )
            MAX_PAGE_SIZE: Final[int] = 1000
            MIN_PAGE_SIZE: Final[int] = (
                FlextOracleOicConstants.DEFAULT_RETRY_DELAY_SECONDS
            )
            DEFAULT_PAGINATOR_START: Final[int] = 0
            DEFAULT_PAGINATOR_PAGE_SIZE: Final[int] = 100
            PAGINATOR_MAX_PAGE_SIZE: Final[int] = 1000
            PAGINATOR_MIN_PAGE_SIZE: Final[int] = 10

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

            MIN_TOKEN_EXPIRY_BUFFER: Final[int] = 60
            MIN_PERCENTAGE: Final[float] = 0.0
            MAX_PERCENTAGE: Final[float] = 100.0

        class TapOicPerformance:
            """OIC tap performance and monitoring constants."""

            RESPONSE_TIME_HISTORY_SIZE: Final[int] = 10
            MIN_RESPONSE_SAMPLES: Final[int] = 5
            SLOW_RESPONSE_THRESHOLD: Final[float] = 5.0
            MIN_PERCENTAGE: Final[float] = 0.0
            MAX_PERCENTAGE: Final[float] = 100.0

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
            QUEUED = "QUEUED"

        @unique
        class OicIntegrationType(StrEnum):
            """OIC integration/package type."""

            APP_DRIVEN = "APP_DRIVEN"
            SCHEDULED = "SCHEDULED"
            INTEGRATION = "INTEGRATION"
            BASIC = "BASIC"
            PUBLISH = "PUBLISH"
            SUBSCRIBE = "SUBSCRIBE"

        @unique
        class OicAgentType(StrEnum):
            """OIC connectivity agent type."""

            CONNECTIVITY_AGENT = "CONNECTIVITY_AGENT"
            EXECUTION_AGENT = "EXECUTION_AGENT"

        @unique
        class OicAgentStatus(StrEnum):
            """OIC agent operational status."""

            ONLINE = "ONLINE"
            OFFLINE = "OFFLINE"
            ERROR = "ERROR"

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
        class OicErrorType(StrEnum):
            """Error type constants using StrEnum for type safety."""

            AUTHENTICATION = "AUTHENTICATION"
            AUTHORIZATION = "AUTHORIZATION"
            RATE_LIMIT = "RATE_LIMIT"
            SERVER_ERROR = "SERVER_ERROR"
            NETWORK = "NETWORK"
            VALIDATION = "VALIDATION"


c = FlextTapOracleOicConstants
__all__: t.StrSequence = ["FlextTapOracleOicConstants", "c"]
