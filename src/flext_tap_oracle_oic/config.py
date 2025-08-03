"""Configuration schema for Oracle Integration Cloud TAP v0.7.0.

MIGRATED TO FLEXT-CORE:
Uses flext-core FlextValueObject and configuration patterns.
"""

from __future__ import annotations

from typing import Any

# Import from flext-core for foundational patterns (standardized)
from pydantic import BaseModel, Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class OICAuthConfig(BaseModel):
    """OAuth2 authentication configuration for Oracle IDCS using flext-core patterns."""

    oauth_client_id: str = Field(
        ...,
        description="OAuth2 client ID from IDCS application",
    )
    oauth_client_secret: str = Field(
        ...,
        description="OAuth2 client secret from IDCS application",
        json_schema_extra={"secret": True},
    )
    oauth_token_url: str = Field(..., description="IDCS token endpoint URL")
    oauth_client_aud: str | None = Field(
        None,
        description="IDCS client audience URL for scope building",
    )
    oauth_scope: str | None = Field(None, description="OAuth2 scope for authentication")


class OICConnectionConfig(BaseModel):
    """Connection configuration for Oracle Integration Cloud."""

    base_url: str = Field(
        ...,
        description="OIC instance base URL (e.g., https://myinstance-region.integration.ocp.oraclecloud.com)",
    )
    auth_method: str = Field(
        default="oauth2",
        description="Authentication method: 'oauth2' (OIC only supports OAuth2)",
    )

    # Performance settings
    timeout: int = Field(default=300, description="Request timeout in seconds", gt=0)
    retry_count: int = Field(
        default=3,
        description="Number of retry attempts for failed requests",
        ge=0,
    )
    retry_delay: float = Field(
        default=1.0,
        description="Delay between retry attempts in seconds",
        gt=0,
    )
    page_size: int = Field(
        default=100,
        description="Page size for paginated results",
        gt=0,
        le=500,
    )
    max_concurrent_requests: int = Field(
        default=5,
        description="Maximum concurrent API requests",
        gt=0,
        le=20,
    )


class StreamSelectionConfig(BaseModel):
    """Configuration for stream selection and filtering using flext-core patterns."""

    stream_maps: dict[str, object] | None = Field(
        None,
        description="Stream maps for transforming data",
    )
    stream_map_config: dict[str, object] | None = Field(
        None,
        description="Configuration for stream maps",
    )
    include_integrations: list[str] | None = Field(
        None,
        description="List of integration identifiers to include",
    )
    exclude_integrations: list[str] | None = Field(
        None,
        description="List of integration identifiers to exclude",
    )
    include_lookups: list[str] | None = Field(
        None,
        description="List of lookup identifiers to include",
    )
    exclude_lookups: list[str] | None = Field(
        None,
        description="List of lookup identifiers to exclude",
    )
    include_patterns: list[str] | None = Field(
        None,
        description="Regex patterns for including integrations/lookups",
    )
    exclude_patterns: list[str] | None = Field(
        None,
        description="Regex patterns for excluding integrations/lookups",
    )


class DiscoveryConfig(BaseModel):
    """Configuration for catalog discovery using flext-core patterns."""

    discover_integrations: bool = Field(
        default=True,
        description="Discover integration flows",
    )
    discover_connections: bool = Field(
        default=True,
        description="Discover connection configurations",
    )
    discover_lookups: bool = Field(default=True, description="Discover lookup tables")
    discover_libraries: bool = Field(
        default=False,
        description="Discover JavaScript libraries",
    )
    discover_agents: bool = Field(
        default=False,
        description="Discover connectivity agents",
    )
    discover_certificates: bool = Field(
        default=False,
        description="Discover certificates",
    )

    # Discovery optimization
    discovery_batch_size: int = Field(
        default=50,
        description="Batch size for discovery operations",
        gt=0,
    )
    discovery_timeout: int = Field(
        default=600,
        description="Timeout for discovery operations in seconds",
        gt=0,
    )


class DataExtractionConfig(BaseModel):
    """Configuration for data extraction behavior using flext-core patterns."""

    extract_integration_metadata: bool = Field(
        default=True,
        description="Extract detailed integration metadata",
    )
    extract_connection_properties: bool = Field(
        default=True,
        description="Extract connection property details",
    )
    extract_lookup_data: bool = Field(
        default=False,
        description="Extract actual lookup table data (can be large)",
    )
    extract_monitoring_data: bool = Field(
        default=False,
        description="Extract monitoring and metrics data",
    )
    extract_audit_logs: bool = Field(
        default=False,
        description="Extract audit log entries",
    )

    # Data filtering
    created_after: str | None = Field(
        None,
        description="Only extract items created after this date (ISO 8601)",
    )
    modified_after: str | None = Field(
        None,
        description="Only extract items modified after this date (ISO 8601)",
    )


class TapOracleOICConfig(BaseSettings):
    """Complete configuration for tap-oracle-oic v0.7.0 using flext-core patterns.

    Combines all configuration aspects with environment variable support.
    """

    model_config = SettingsConfigDict(
        env_prefix="TAP_ORACLE_OIC_",
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="allow",
        validate_assignment=True,
        str_strip_whitespace=True,
        use_enum_values=True,
    )

    # Core configurations as embedded value objects
    auth: OICAuthConfig = Field(..., description="OAuth2 authentication configuration")
    connection: OICConnectionConfig = Field(
        ...,
        description="OIC connection configuration",
    )
    stream_selection: StreamSelectionConfig = Field(
        default_factory=lambda: StreamSelectionConfig(
            stream_maps=None,
            stream_map_config=None,
            include_integrations=None,
            exclude_integrations=None,
            include_lookups=None,
            exclude_lookups=None,
            include_patterns=None,
            exclude_patterns=None,
        ),
        description="Stream selection and filtering configuration",
    )
    discovery: DiscoveryConfig = Field(
        default_factory=DiscoveryConfig,
        description="Catalog discovery configuration",
    )
    data_extraction: DataExtractionConfig = Field(
        default_factory=lambda: DataExtractionConfig(
            created_after=None,
            modified_after=None,
        ),
        description="Data extraction behavior configuration",
    )

    # Project identification
    project_name: str = Field(
        default="flext-data.taps.flext-data.taps.flext-tap-oracle-oic",
        description="Project name",
    )
    project_version: str = Field(default="0.9.0", description="Project version")

    @field_validator("auth")
    @classmethod
    def validate_auth_config(cls, v: OICAuthConfig) -> OICAuthConfig:
        """Validate authentication configuration."""
        if not v.oauth_token_url.startswith(("http://", "https://")):
            msg = "OAuth token URL must start with http:// or https://"
            raise ValueError(msg)
        return v

    @field_validator("connection")
    @classmethod
    def validate_connection_config(cls, v: OICConnectionConfig) -> OICConnectionConfig:
        """Validate connection configuration."""
        if not v.base_url.startswith(("http://", "https://")):
            msg = "Base URL must start with http:// or https://"
            raise ValueError(msg)
        # Remove trailing slash for consistency - create new object with corrected value
        return v.model_copy(update={"base_url": v.base_url.rstrip("/")})

    @model_validator(mode="after")
    def validate_stream_filters(self) -> TapOracleOICConfig:
        """Validate stream filter configurations."""
        selection = self.stream_selection

        if selection.include_integrations and selection.exclude_integrations:
            overlap = set(selection.include_integrations) & set(
                selection.exclude_integrations,
            )
            if overlap:
                msg = f"Include and exclude integrations overlap: {overlap}"
                raise ValueError(msg)

        if selection.include_lookups and selection.exclude_lookups:
            overlap = set(selection.include_lookups) & set(selection.exclude_lookups)
            if overlap:
                msg = f"Include and exclude lookups overlap: {overlap}"
                raise ValueError(msg)

        return self

    def get_oauth_headers(self) -> dict[str, str]:
        """Get OAuth headers (implemented by client using flext-api.auth.flext-auth)."""
        return {}

    def should_include_integration(self, integration_id: str) -> bool:
        """Check if integration should be included based on filters."""
        selection = self.stream_selection

        if selection.include_integrations:
            return integration_id in selection.include_integrations
        if selection.exclude_integrations:
            return integration_id not in selection.exclude_integrations
        return True

    def should_include_lookup(self, lookup_id: str) -> bool:
        """Check if lookup should be included based on filters."""
        selection = self.stream_selection

        if selection.include_lookups:
            return lookup_id in selection.include_lookups
        if selection.exclude_lookups:
            return lookup_id not in selection.exclude_lookups
        return True

    @classmethod
    def create_with_defaults(cls, **overrides: object) -> TapOracleOICConfig:
        """Create configuration with intelligent defaults."""
        defaults = {
            "auth": OICAuthConfig(
                oauth_client_id="your-client-id",
                oauth_client_secret="your-client-secret",
                oauth_token_url="https://idcs-url/oauth2/v1/token",
                oauth_client_aud=None,
                oauth_scope=None,
            ),
            "connection": OICConnectionConfig(
                base_url="https://your-instance.integration.ocp.oraclecloud.com",
            ),
            "stream_selection": StreamSelectionConfig(
                stream_maps=None,
                stream_map_config=None,
                include_integrations=None,
                exclude_integrations=None,
                include_lookups=None,
                exclude_lookups=None,
                include_patterns=None,
                exclude_patterns=None,
            ),
            "discovery": DiscoveryConfig(),
            "data_extraction": DataExtractionConfig(
                created_after=None,
                modified_after=None,
            ),
            "project_name": "flext-data.taps.flext-data.taps.flext-tap-oracle-oic",
            "project_version": "0.9.0",
        }
        defaults.update(overrides)
        return cls.model_validate(defaults)


# Export main configuration classes
__all__ = [
    "DataExtractionConfig",
    "DiscoveryConfig",
    "OICAuthConfig",
    "OICConnectionConfig",
    "StreamSelectionConfig",
    "TapOracleOICConfig",
]
