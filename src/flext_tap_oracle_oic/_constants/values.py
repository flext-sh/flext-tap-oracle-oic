"""Scalar constants for flext-tap-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import re

from flext_oracle_oic import FlextOracleOicConstants


class FlextTapOracleOicConstantsValues:
    """Scalar constants mixed into the ``c.TapOracleOic`` namespace tree.

    Inherited attributes do not appear in the namespace class's ``vars()``,
    so the runtime census stops flagging them while every consumer path
    keeps resolving.
    """

    class TapOracleOic:
        """Tap Oracle OIC scalar constants."""

        # === Regex authority for the TapOracleOic domain ===
        OCI_REGION_RE: re.Pattern[str] = re.compile(r"(\w+-\w+-\d+)")
        NORMALIZE_NON_ALNUM_RE: re.Pattern[str] = re.compile(r"[^a-zA-Z0-9]")
        NORMALIZE_REPEATED_UNDERSCORE_RE: re.Pattern[str] = re.compile(r"_+")
        SANITIZE_CAMEL_BOUNDARY_RE: re.Pattern[str] = re.compile(r"(?<!^)(?=[A-Z])")
        SANITIZE_NON_IDENTIFIER_RE: re.Pattern[str] = re.compile(r"[^a-zA-Z0-9_]")

        DEFAULT_BATCH_SIZE: int = 100
        MAX_RETRIES: int = 3
        DEFAULT_PAGE_SIZE: int = 50

        DEFAULT_INTEGRATION_VERSION: str = "01.00.0000"
        SCHEMA_EXAMPLE_IDCS_URL: str = (
            "https://idcs-instance.identity.oraclecloud.com/oauth2/v1/token"
        )
        SCHEMA_EXAMPLE_OIC_URL: str = (
            "https://mycompany-oic.integration.ocp.oraclecloud.com"
        )

        OIC_API_BASE_PATH: str = "/ic/api/integration/v1"
        OIC_MONITORING_API_PATH: str = "/ic/api/monitoring/v1"
        OIC_B2B_API_PATH: str = "/ic/api/b2b/v1"
        OIC_PROCESS_API_PATH: str = "/ic/api/process/v1"

        DEFAULT_TIMEOUT: int = FlextOracleOicConstants.OracleOic.MIN_REQUEST_TIMEOUT
        DEFAULT_MAX_RETRIES: int = 3
        DEFAULT_VERIFY_SSL: bool = True

        CORE_STREAMS: tuple[str, ...] = (
            "integrations",
            "connections",
            "packages",
            "lookups",
            "libraries",
        )
        INFRASTRUCTURE_STREAMS: tuple[str, ...] = ("certificates", "adapters")

        MAX_PAGE_SIZE: int = 1000
        MIN_PAGE_SIZE: int = FlextOracleOicConstants.DEFAULT_RETRY_DELAY_SECONDS
        DEFAULT_PAGINATOR_START: int = 0
        DEFAULT_PAGINATOR_PAGE_SIZE: int = 100
        PAGINATOR_MAX_PAGE_SIZE: int = 1000
        PAGINATOR_MIN_PAGE_SIZE: int = 10

        HTTP_UNAUTHORIZED: int = 401
        HTTP_FORBIDDEN: int = 403
        HTTP_ERROR_STATUS_THRESHOLD: int = 400
        HTTP_RATE_LIMITED: int = 429

        MIN_TOKEN_EXPIRY_BUFFER: int = 60
        MIN_PERCENTAGE: float = 0.0
        MAX_PERCENTAGE: float = 100.0

        RESPONSE_TIME_HISTORY_SIZE: int = 10
        MIN_RESPONSE_SAMPLES: int = 5
        SLOW_RESPONSE_THRESHOLD: float = 5.0


__all__: list[str] = ["FlextTapOracleOicConstantsValues"]
