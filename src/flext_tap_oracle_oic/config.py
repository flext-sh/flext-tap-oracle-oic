"""FLEXT Tap Oracle OIC Configuration - Enhanced FlextConfig Implementation.

Single unified configuration class for Oracle Integration Cloud Singer tap
operations following FLEXT 1.0.0 patterns with enhanced singleton, SecretStr,
and Pydantic 2.11+ features.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import re
from typing import Self

from flext_core import FlextConfig, FlextConstants, FlextResult
from pydantic import Field, HttpUrl, SecretStr, field_validator, model_validator
from pydantic_settings import SettingsConfigDict


class FlextMeltanoTapOracleOicConfig(FlextConfig):
    """Oracle Integration Cloud Tap Configuration using enhanced FlextConfig patterns.

    This class extends FlextConfig and includes all the configuration fields
    needed for Oracle Integration Cloud tap operations. Uses the enhanced singleton pattern
    with get_or_create_shared_instance for thread-safe configuration management.

    Follows standardized pattern:
    - Extends FlextConfig from flext-core
    - Uses SecretStr for sensitive data (oauth_client_secret)
    - All defaults from FlextConstants where possible
    - Uses enhanced singleton pattern with inverse dependency injection
    - Uses Pydantic 2.11+ features (field_validator, model_validator)
    """

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_TAP_ORACLE_OIC_",
        case_sensitive=False,
        extra="ignore",
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        use_enum_values=True,
        validate_assignment=True,
        validate_default=True,
        frozen=False,
        str_strip_whitespace=True,
        # Enhanced Pydantic 2.11+ features
        validate_return=True,
        json_schema_extra={
            "title": "FLEXT Tap Oracle OIC Configuration",
            "description": "Oracle Integration Cloud Singer tap configuration extending FlextConfig",
        },
    )

    # OAuth2/IDCS Authentication Configuration using SecretStr
    oauth_client_id: str = Field(
        ...,
        min_length=1,
        description="OAuth2 client ID for IDCS authentication",
    )

    oauth_client_secret: SecretStr = Field(
        ...,
        description="OAuth2 client secret for IDCS authentication (sensitive)",
    )

    oauth_token_url: HttpUrl = Field(
        default="https://idcs-tenant.identity.oraclecloud.com/oauth2/v1/token",
        description="OAuth2 token endpoint URL",
    )

    oauth_audience: str = Field(
        ...,
        min_length=1,
        description="OAuth2 audience/scope for OIC API access",
    )

    # OIC Connection Configuration
    base_url: HttpUrl = Field(
        default="https://instance.integration.ocp.oraclecloud.com",
        description="OIC instance base URL",
    )

    api_version: str = Field(
        default="v1",
        min_length=1,
        description="OIC API version",
    )

    timeout: int = Field(
        default=FlextConstants.Network.DEFAULT_TIMEOUT,
        ge=1,
        le=300,
        description="Request timeout in seconds",
    )

    max_retries: int = Field(
        default=FlextConstants.Network.DEFAULT_MAX_RETRIES,
        ge=0,
        le=10,
        description="Maximum retry attempts",
    )

    page_size: int = Field(
        default=FlextConstants.Performance.DEFAULT_BATCH_SIZE,
        ge=1,
        le=1000,
        description="API pagination size",
    )

    # Tap-specific Configuration using FlextConstants where applicable
    stream_prefix: str = Field(
        default="oic",
        min_length=1,
        description="Prefix for Singer stream names",
    )

    include_extended: bool = Field(
        default=False,
        description="Include extended/monitoring streams",
    )

    start_date: str | None = Field(
        default=None,
        description="Start date for incremental extraction (YYYY-MM-DD or ISO 8601)",
    )

    batch_size: int = Field(
        default=FlextConstants.Performance.DEFAULT_BATCH_SIZE,
        ge=1,
        le=FlextConstants.Performance.MAX_BATCH_SIZE_VALIDATION,
        description="Batch size for data extraction",
    )

    max_parallel_streams: int = Field(
        default=FlextConstants.Reliability.MAX_RETRY_ATTEMPTS,
        ge=1,
        le=FlextConstants.Container.MAX_WORKERS,
        description="Maximum parallel streams for extraction",
    )

    # Project identification
    project_name: str = Field(
        default="flext-tap-oracle-oic",
        description="Project name",
    )

    project_version: str = Field(
        default="0.9.0",
        description="Project version",
    )

    # Pydantic 2.11+ field validators
    @field_validator("stream_prefix")
    @classmethod
    def validate_stream_prefix(cls, v: str) -> str:
        """Validate stream prefix follows naming conventions."""
        # Valid identifier: start with letter, contain letters/digits/underscore
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$", v):
            msg = f"Invalid stream prefix: {v}. Must start with letter and contain only letters, digits, and underscores"
            raise ValueError(msg)

        if len(v) > FlextConstants.Limits.MAX_STRING_LENGTH:
            msg = f"Stream prefix too long: {len(v)} > {FlextConstants.Limits.MAX_STRING_LENGTH}"
            raise ValueError(msg)

        return v.lower()

    @field_validator("api_version")
    @classmethod
    def validate_api_version(cls, v: str) -> str:
        """Validate API version format."""
        # API version should be like v1, v2, etc.
        if not re.match(r"^v\d+(\.\d+)*$", v):
            msg = (
                f"Invalid API version format: {v}. Expected format: v1, v2, v1.2, etc."
            )
            raise ValueError(msg)

        return v.strip()

    @field_validator("start_date")
    @classmethod
    def validate_start_date(cls, v: str | None) -> str | None:
        """Validate start date format if provided."""
        if v is None:
            return v

        v = v.strip()
        if not v:
            return None

        # Minimum length check for YYYY-MM-DD format
        if len(v) < FlextConstants.Configuration.MIN_DATE_LENGTH:
            msg = "Start date must be in YYYY-MM-DD format or ISO 8601"
            raise ValueError(msg)

        # Check for reasonable date format (must contain - or T)
        if not any(char in v for char in ["-", "T"]):
            msg = "Start date must be in ISO date format"
            raise ValueError(msg)

        return v

    @model_validator(mode="after")
    def validate_oauth_configuration(self) -> Self:
        """Validate OAuth configuration completeness."""
        # Check that all OAuth fields are provided together
        oauth_fields = [
            self.oauth_client_id,
            self.oauth_client_secret.get_secret_value(),
            str(self.oauth_token_url),
            self.oauth_audience,
        ]

        if any(oauth_fields) and not all(oauth_fields):
            msg = "All OAuth fields (client_id, client_secret, token_url, audience) must be provided together"
            raise ValueError(msg)

        return self

    @model_validator(mode="after")
    def validate_url_consistency(self) -> Self:
        """Validate URL consistency between token URL and base URL."""
        try:
            token_host = str(self.oauth_token_url).split("//")[1].split("/")[0]
            base_host = str(self.base_url).split("//")[1].split("/")[0]

            # Basic validation that hosts are properly formatted
            if not token_host or not base_host:
                msg = "OAuth token URL and base URL must be valid URLs"
                raise ValueError(msg)

        except (IndexError, AttributeError) as e:
            msg = f"URL validation failed: {e}"
            raise ValueError(msg) from e

        return self

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate Oracle Integration Cloud tap configuration business rules."""
        try:
            # Validate OAuth configuration
            if not self.oauth_client_id:
                return FlextResult[None].fail("OAuth client ID is required")

            if not self.oauth_client_secret.get_secret_value():
                return FlextResult[None].fail("OAuth client secret is required")

            if not self.oauth_audience:
                return FlextResult[None].fail("OAuth audience is required")

            # Validate connection parameters
            if self.timeout <= 0:
                return FlextResult[None].fail("Timeout must be positive")

            if self.max_retries < 0:
                return FlextResult[None].fail("Max retries cannot be negative")

            if self.page_size <= 0:
                return FlextResult[None].fail("Page size must be positive")

            # Validate performance settings
            max_safe_parallel = FlextConstants.Container.MAX_WORKERS
            max_safe_batch = FlextConstants.Performance.BatchProcessing.MAX_ITEMS // 2
            if (
                self.max_parallel_streams > max_safe_parallel
                and self.batch_size > max_safe_batch
            ):
                return FlextResult[None].fail(
                    "High parallelism with large batch sizes may cause memory issues",
                )

            return FlextResult[None].ok(None)

        except Exception as e:
            return FlextResult[None].fail(f"Business rules validation failed: {e}")

    # Configuration helper methods
    def get_api_base_url(self) -> str:
        """Get full API base URL with version."""
        return f"{str(self.base_url).rstrip('/')}/ic/api/integration/{self.api_version}"

    def get_auth_config(self) -> dict[str, object]:
        """Get authentication configuration dictionary."""
        return {
            "client_id": self.oauth_client_id,
            "client_secret": self.oauth_client_secret.get_secret_value(),
            "token_url": str(self.oauth_token_url),
            "audience": self.oauth_audience,
        }

    def get_connection_config(self) -> dict[str, object]:
        """Get connection configuration dictionary."""
        return {
            "base_url": str(self.base_url),
            "api_version": self.api_version,
            "timeout": self.timeout,
            "max_retries": self.max_retries,
            "page_size": self.page_size,
        }

    def get_tap_config(self) -> dict[str, object]:
        """Get tap-specific configuration dictionary."""
        return {
            "stream_prefix": self.stream_prefix,
            "include_extended": self.include_extended,
            "start_date": self.start_date,
            "batch_size": self.batch_size,
            "max_parallel_streams": self.max_parallel_streams,
        }

    def get_performance_config(self) -> dict[str, object]:
        """Get performance configuration dictionary."""
        return {
            "batch_size": self.batch_size,
            "max_parallel_streams": self.max_parallel_streams,
            "page_size": self.page_size,
            "timeout": self.timeout,
            "max_retries": self.max_retries,
        }

    def get_token_request_data(self) -> dict[str, str]:
        """Get OAuth2 token request data for client credentials flow."""
        return {
            "grant_type": "client_credentials",
            "client_id": self.oauth_client_id,
            "client_secret": self.oauth_client_secret.get_secret_value(),
            "audience": self.oauth_audience,
        }

    def get_headers(self) -> dict[str, str]:
        """Get default headers for OIC API requests."""
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": f"flext-tap-oracle-oic/{self.project_version}",
        }

    @classmethod
    def create_for_environment(
        cls,
        environment: str,
        **overrides: object,
    ) -> FlextMeltanoTapOracleOicConfig:
        """Create configuration for specific environment using enhanced singleton pattern."""
        env_overrides: dict[str, object] = {}

        if environment == "production":
            env_overrides.update({
                "timeout": FlextConstants.Network.DEFAULT_TIMEOUT,
                "max_retries": FlextConstants.Reliability.MAX_RETRY_ATTEMPTS,
                "page_size": FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE
                // 10,
                "include_extended": False,
                "max_parallel_streams": FlextConstants.Reliability.MAX_RETRY_ATTEMPTS,
            })
        elif environment == "development":
            env_overrides.update({
                "timeout": FlextConstants.Network.DEFAULT_TIMEOUT * 2,
                "max_retries": 1,
                "page_size": FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE
                // 20,
                "include_extended": True,
                "max_parallel_streams": 1,
            })
        elif environment == "staging":
            env_overrides.update({
                "timeout": FlextConstants.Network.DEFAULT_TIMEOUT + 15,
                "max_retries": 2,
                "page_size": FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE
                // 13,
                "include_extended": False,
                "max_parallel_streams": 2,
            })

        all_overrides = {**env_overrides, **overrides}
        return cls.get_or_create_shared_instance(
            project_name="flext-tap-oracle-oic",
            environment=environment,
            **all_overrides,
        )

    @classmethod
    def get_global_instance(cls) -> Self:
        """Get the global singleton instance using enhanced FlextConfig pattern."""
        return cls.get_or_create_shared_instance(project_name="flext-tap-oracle-oic")

    @classmethod
    def create_for_development(cls, **overrides: object) -> Self:
        """Create configuration for development environment."""
        dev_overrides: dict[str, object] = {
            "timeout": FlextConstants.Network.DEFAULT_TIMEOUT * 2,
            "max_retries": 1,
            "page_size": FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE // 20,
            "include_extended": True,
            "max_parallel_streams": 1,
            **overrides,
        }
        return cls.get_or_create_shared_instance(
            project_name="flext-tap-oracle-oic",
            **dev_overrides,
        )

    @classmethod
    def create_for_production(cls, **overrides: object) -> Self:
        """Create configuration for production environment."""
        prod_overrides: dict[str, object] = {
            "timeout": FlextConstants.Network.DEFAULT_TIMEOUT,
            "max_retries": FlextConstants.Reliability.MAX_RETRY_ATTEMPTS,
            "page_size": FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE // 10,
            "include_extended": False,
            "max_parallel_streams": FlextConstants.Reliability.MAX_RETRY_ATTEMPTS,
            **overrides,
        }
        return cls.get_or_create_shared_instance(
            project_name="flext-tap-oracle-oic",
            **prod_overrides,
        )

    @classmethod
    def create_for_testing(cls, **overrides: object) -> Self:
        """Create configuration for testing environment."""
        test_overrides: dict[str, object] = {
            "timeout": FlextConstants.Network.DEFAULT_TIMEOUT // 3,
            "max_retries": 1,
            "page_size": FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE // 100,
            "include_extended": True,
            "max_parallel_streams": 1,
            **overrides,
        }
        return cls.get_or_create_shared_instance(
            project_name="flext-tap-oracle-oic",
            **test_overrides,
        )

    @classmethod
    def reset_global_instance(cls) -> None:
        """Reset the global FlextMeltanoTapOracleOicConfig instance (mainly for testing)."""
        cls.reset_shared_instance()


# Factory function for backward compatibility (will be removed in future versions)
def create_oracle_oic_tap_config(
    oauth_params: dict[str, object],
    connection_params: dict[str, object],
    tap_params: dict[str, object] | None = None,
) -> FlextResult[FlextMeltanoTapOracleOicConfig]:
    """Create Oracle Integration Cloud tap configuration using grouped parameters.

    Args:
    oauth_params: OAuth2/IDCS authentication parameters
    connection_params: OIC connection parameters
    tap_params: Optional tap-specific parameters

    Returns:
    FlextResult containing validated Oracle OIC tap configuration

    """
    try:
        # Apply defaults
        tap_config = tap_params or {}

        # Set default values using semantic constants
        tap_config.setdefault(
            "batch_size",
            FlextConstants.Performance.DEFAULT_BATCH_SIZE,
        )
        tap_config.setdefault("stream_prefix", "oic")

        # Merge OAuth, connection, and tap parameters
        config_data = {
            **oauth_params,
            **connection_params,
            **tap_config,
        }

        config_instance = (
            FlextMeltanoTapOracleOicConfig.get_global_instance().model_validate(
                config_data,
            )
        )
        return FlextResult[FlextMeltanoTapOracleOicConfig].ok(config_instance)

    except Exception as e:
        return FlextResult[FlextMeltanoTapOracleOicConfig].fail(
            f"Oracle OIC tap configuration creation failed: {e}",
        )


def validate_oracle_oic_tap_configuration(
    config: FlextMeltanoTapOracleOicConfig,
) -> FlextResult[None]:
    """Validate Oracle Integration Cloud tap configuration using FlextConfig patterns - ZERO DUPLICATION."""
    # Required string fields validation
    required_fields = [
        (config.oauth_client_id, "OAuth client ID is required"),
        (
            config.oauth_client_secret.get_secret_value(),
            "OAuth client secret is required",
        ),
        (config.oauth_audience, "OAuth audience is required"),
    ]

    # Validate required string fields
    for field_value, error_message in required_fields:
        if not (field_value and str(field_value).strip()):
            return FlextResult[None].fail(error_message)

    # Validate timeout constraints
    if config.timeout <= 0:
        return FlextResult[None].fail("Timeout must be positive")

    # Validate retry constraints
    if config.max_retries < 0:
        return FlextResult[None].fail("Max retries cannot be negative")

    # Validate page size constraints
    if config.page_size <= 0:
        return FlextResult[None].fail("Page size must be positive")

    return FlextResult[None].ok(None)


__all__: list[str] = [
    "FlextMeltanoTapOracleOicConfig",
    "create_oracle_oic_tap_config",
    "validate_oracle_oic_tap_configuration",
]
