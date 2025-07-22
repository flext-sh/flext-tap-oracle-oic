"""Simple API for Oracle Integration Cloud tap setup and operations using flext-core patterns.

MIGRATED TO FLEXT-CORE:
Provides enterprise-ready setup utilities with ServiceResult pattern support.
"""

from __future__ import annotations

from typing import Any

import requests

# Use centralized ServiceResult from flext-core - ELIMINATE DUPLICATION
from flext_core import ServiceResult
from pydantic import ValidationError

from flext_tap_oracle_oic.config import (
    DataExtractionConfig,
    DiscoveryConfig,
    OICAuthConfig,
    OICConnectionConfig,
    StreamSelectionConfig,
    TapOracleOICConfig,
)


def setup_oic_tap(
    config: TapOracleOICConfig | None = None,
) -> ServiceResult[Any]:
    """Set up Oracle Integration Cloud tap with configuration.

    Args:
        config: Optional configuration. If None, creates defaults.

    Returns:
        ServiceResult with TapOracleOICConfig or error message.

    """
    try:
        if config is None:
            # Create with intelligent defaults
            config = TapOracleOICConfig.create_with_defaults()

        # Validate configuration
        config.model_validate(config.model_dump())

        return ServiceResult.ok(config)

    except (ValueError, ValidationError, TypeError) as e:
        return ServiceResult.ok(error=f"Failed to setup OIC tap: {e}")


def create_oic_auth_config(
    client_id: str,
    client_secret: str,
    token_url: str,
    **kwargs: Any,
) -> ServiceResult[Any]:
    """Create OIC authentication configuration.

    Args:
        client_id: OAuth2 client ID
        client_secret: OAuth2 client secret
        token_url: IDCS token endpoint URL
        **kwargs: Additional configuration parameters

    Returns:
        ServiceResult with OICAuthConfig or error message.

    """
    try:
        config = OICAuthConfig(
            oauth_client_id=client_id,
            oauth_client_secret=client_secret,
            oauth_token_url=token_url,
            **kwargs,
        )

        return ServiceResult.ok(config)

    except (ValueError, ValidationError, TypeError) as e:
        return ServiceResult.ok(error=f"Failed to create OIC auth config: {e}")


def create_oic_connection_config(
    base_url: str,
    **kwargs: Any,
) -> ServiceResult[Any]:
    """Create OIC connection configuration.

    Args:
        base_url: OIC instance base URL
        **kwargs: Additional configuration parameters

    Returns:
        ServiceResult with OICConnectionConfig or error message.

    """
    try:
        config = OICConnectionConfig(
            base_url=base_url,
            **kwargs,
        )

        return ServiceResult.ok(config)

    except (ValueError, ValidationError, TypeError) as e:
        return ServiceResult.ok(error=f"Failed to create OIC connection config: {e}")


def validate_oic_config(config: TapOracleOICConfig) -> ServiceResult[Any]:
    """Validate OIC tap configuration.

    Args:
        config: Configuration to validate

    Returns:
        ServiceResult with validation success or error message.

    """
    try:
        # Validate using Pydantic model validation
        config.model_validate(config.model_dump())

        # Additional business rule validations
        if not config.connection.base_url:
            return ServiceResult.fail("Base URL is required")

        if not config.auth.oauth_client_id:
            return ServiceResult.fail("OAuth client ID is required")

        if not config.auth.oauth_client_secret:
            return ServiceResult.fail("OAuth client secret is required")

        if not config.auth.oauth_token_url:
            return ServiceResult.fail("OAuth token URL is required")

        return ServiceResult.ok(True)

    except (ValueError, ValidationError, AttributeError) as e:
        return ServiceResult.ok(error=f"Configuration validation failed: {e}")


def create_development_oic_config(
    **overrides: Any,
) -> ServiceResult[Any]:
    """Create development OIC configuration with defaults.

    Args:
        **overrides: Configuration overrides

    Returns:
        ServiceResult with TapOracleOICConfig for development use.

    """
    try:
        auth_config = OICAuthConfig(
            oauth_client_id="dev-client-id",
            oauth_client_secret="dev-client-secret",
            oauth_token_url="https://identity.oraclecloud.com/oauth2/v1/token",
            oauth_client_aud=None,
            oauth_scope=None,
        )

        connection_config = OICConnectionConfig(
            base_url="https://dev-instance.integration.ocp.oraclecloud.com",
            timeout=120,
            retry_count=3,
            retry_delay=2.0,
            page_size=50,
            max_concurrent_requests=3,
        )

        discovery_config = DiscoveryConfig(
            discover_integrations=True,
            discover_connections=True,
            discover_lookups=False,
            discover_libraries=False,
        )

        data_extraction_config = DataExtractionConfig(
            extract_integration_metadata=True,
            extract_connection_properties=True,
            extract_lookup_data=False,
            created_after=None,
            modified_after=None,
        )

        config = TapOracleOICConfig(
            auth=auth_config,
            connection=connection_config,
            stream_selection=StreamSelectionConfig(
                stream_maps=None,
                stream_map_config=None,
                include_integrations=None,
                exclude_integrations=None,
                include_lookups=None,
                exclude_lookups=None,
                include_patterns=None,
                exclude_patterns=None,
            ),
            discovery=discovery_config,
            data_extraction=data_extraction_config,
            project_name="flext-data.taps.flext-data.taps.flext-tap-oracle-oic",
            project_version="0.7.0",
        )

        # Apply overrides
        if overrides:
            config_dict = config.model_dump()
            config_dict.update(overrides)
            config = TapOracleOICConfig(**config_dict)

        return ServiceResult.ok(config)

    except (ValueError, ValidationError, TypeError, requests.RequestException) as e:
        return ServiceResult.ok(error=f"Failed to create development config: {e}")


def create_production_oic_config(**overrides: Any) -> ServiceResult[Any]:
    """Create production OIC configuration with security defaults.

    Args:
        **overrides: Configuration overrides

    Returns:
        ServiceResult with TapOracleOICConfig for production use.

    """
    try:
        auth_config = OICAuthConfig(
            oauth_client_id="prod-client-id",
            oauth_client_secret="prod-client-secret",
            oauth_token_url="https://identity.oraclecloud.com/oauth2/v1/token",
            oauth_client_aud=None,
            oauth_scope=None,
        )

        connection_config = OICConnectionConfig(
            base_url="https://prod-instance.integration.ocp.oraclecloud.com",
            timeout=300,
            retry_count=5,
            retry_delay=1.0,
            page_size=100,
            max_concurrent_requests=5,
        )

        discovery_config = DiscoveryConfig(
            discover_integrations=True,
            discover_connections=True,
            discover_lookups=True,
            discover_libraries=False,
            discover_agents=False,
            discovery_timeout=900,
        )

        data_extraction_config = DataExtractionConfig(
            extract_integration_metadata=True,
            extract_connection_properties=True,
            extract_lookup_data=True,
            created_after=None,
            modified_after=None,
        )

        config = TapOracleOICConfig(
            auth=auth_config,
            connection=connection_config,
            stream_selection=StreamSelectionConfig(
                stream_maps=None,
                stream_map_config=None,
                include_integrations=None,
                exclude_integrations=None,
                include_lookups=None,
                exclude_lookups=None,
                include_patterns=None,
                exclude_patterns=None,
            ),
            discovery=discovery_config,
            data_extraction=data_extraction_config,
            project_name="flext-data.taps.flext-data.taps.flext-tap-oracle-oic",
            project_version="0.7.0",
        )

        # Apply overrides
        if overrides:
            config_dict = config.model_dump()
            config_dict.update(overrides)
            config = TapOracleOICConfig(**config_dict)

        return ServiceResult.ok(config)

    except (ValueError, ValidationError, TypeError, requests.RequestException) as e:
        return ServiceResult.ok(error=f"Failed to create production config: {e}")


def create_discovery_only_config(**overrides: Any) -> ServiceResult[Any]:
    """Create OIC configuration optimized for catalog discovery only.

    Args:
        **overrides: Configuration overrides

    Returns:
        ServiceResult with TapOracleOICConfig optimized for discovery.

    """
    try:
        auth_config = OICAuthConfig(
            oauth_client_id="discovery-client-id",
            oauth_client_secret="discovery-client-secret",
            oauth_token_url="https://identity.oraclecloud.com/oauth2/v1/token",
            oauth_client_aud=None,
            oauth_scope=None,
        )

        connection_config = OICConnectionConfig(
            base_url="https://your-instance.integration.ocp.oraclecloud.com",
            timeout=600,
            retry_count=3,
            page_size=200,
            max_concurrent_requests=10,
        )

        discovery_config = DiscoveryConfig(
            discover_integrations=True,
            discover_connections=True,
            discover_lookups=True,
            discover_libraries=True,
            discover_agents=True,
            discover_certificates=True,
            discovery_batch_size=100,
            discovery_timeout=1200,
        )

        data_extraction_config = DataExtractionConfig(
            extract_integration_metadata=False,
            extract_connection_properties=False,
            extract_lookup_data=False,
            extract_monitoring_data=False,
            extract_audit_logs=False,
            created_after=None,
            modified_after=None,
        )

        config = TapOracleOICConfig(
            auth=auth_config,
            connection=connection_config,
            stream_selection=StreamSelectionConfig(
                stream_maps=None,
                stream_map_config=None,
                include_integrations=None,
                exclude_integrations=None,
                include_lookups=None,
                exclude_lookups=None,
                include_patterns=None,
                exclude_patterns=None,
            ),
            discovery=discovery_config,
            data_extraction=data_extraction_config,
            project_name="flext-data.taps.flext-data.taps.flext-tap-oracle-oic",
            project_version="0.7.0",
        )

        # Apply overrides
        if overrides:
            config_dict = config.model_dump()
            config_dict.update(overrides)
            config = TapOracleOICConfig(**config_dict)

        return ServiceResult.ok(config)

    except (ValueError, ValidationError, TypeError, requests.RequestException) as e:
        return ServiceResult.ok(error=f"Failed to create discovery config: {e}")


def create_monitoring_config(**overrides: Any) -> ServiceResult[Any]:
    """Create OIC configuration optimized for monitoring data extraction.

    Args:
        **overrides: Configuration overrides

    Returns:
        ServiceResult with TapOracleOICConfig optimized for monitoring.

    """
    try:
        auth_config = OICAuthConfig(
            oauth_client_id="monitoring-client-id",
            oauth_client_secret="monitoring-client-secret",
            oauth_token_url="https://identity.oraclecloud.com/oauth2/v1/token",
            oauth_client_aud=None,
            oauth_scope=None,
        )

        connection_config = OICConnectionConfig(
            base_url="https://your-instance.integration.ocp.oraclecloud.com",
            timeout=300,
            retry_count=5,
            page_size=500,
            max_concurrent_requests=8,
        )

        discovery_config = DiscoveryConfig(
            discover_integrations=False,
            discover_connections=False,
            discover_lookups=False,
        )

        data_extraction_config = DataExtractionConfig(
            extract_integration_metadata=False,
            extract_connection_properties=False,
            extract_lookup_data=False,
            extract_monitoring_data=True,
            extract_audit_logs=True,
            created_after=None,
            modified_after=None,
        )

        config = TapOracleOICConfig(
            auth=auth_config,
            connection=connection_config,
            stream_selection=StreamSelectionConfig(
                stream_maps=None,
                stream_map_config=None,
                include_integrations=None,
                exclude_integrations=None,
                include_lookups=None,
                exclude_lookups=None,
                include_patterns=None,
                exclude_patterns=None,
            ),
            discovery=discovery_config,
            data_extraction=data_extraction_config,
            project_name="flext-data.taps.flext-data.taps.flext-tap-oracle-oic",
            project_version="0.7.0",
        )

        # Apply overrides
        if overrides:
            config_dict = config.model_dump()
            config_dict.update(overrides)
            config = TapOracleOICConfig(**config_dict)

        return ServiceResult.ok(config)

    except (ValueError, ValidationError, TypeError, requests.RequestException) as e:
        return ServiceResult.ok(error=f"Failed to create monitoring config: {e}")


# Export main API functions
__all__ = [
    "ServiceResult",
    "create_development_oic_config",
    "create_discovery_only_config",
    "create_monitoring_config",
    "create_oic_auth_config",
    "create_oic_connection_config",
    "create_production_oic_config",
    "setup_oic_tap",
    "validate_oic_config",
]
