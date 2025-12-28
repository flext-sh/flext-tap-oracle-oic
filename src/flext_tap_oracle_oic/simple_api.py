"""Simple API for Oracle Integration Cloud tap setup and operations.

SIMPLIFIED FOR PEP8 REORGANIZATION:
Provides basic setup utilities using flext-oracle-oic patterns.
Complex configuration has been moved to flext-oracle-oic library.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import os

from flext_core import FlextResult, FlextTypes as t
from flext_oracle_oic import (
    FlextOracleOicModels,
)
from pydantic import SecretStr


def setup_oic_tap(
    config: object | None = None,
) -> FlextResult[object]:
    """Set up Oracle Integration Cloud tap with basic configuration.

    Args:
    config: Optional configuration override

    Returns:
    FlextResult with basic config dict[str, t.GeneralValueType] or error message.

    """
    try:
        if config is None:
            # Create basic configuration dictionary
            config: dict[str, t.GeneralValueType] = {
                "oauth_client_id": os.getenv("OIC_CLIENT_ID", "your-client-id"),
                "oauth_client_secret": os.getenv("OIC_CLIENT_SECRET", "your-secret"),
                "oauth_token_url": os.getenv(
                    "OIC_TOKEN_URL",
                    "https://idcs/oauth2/v1/token",
                ),
                "oic_url": os.getenv(
                    "OIC_URL",
                    "https://instance.integration.ocp.oraclecloud.com",
                ),
            }

        return FlextResult[object].ok(config)

    except (ValueError, TypeError) as e:
        return FlextResult[object].fail(f"Failed to setup OIC tap: {e}")


def create_oic_auth_config(
    client_id: str,
    client_secret: str,
    token_url: str,
    **kwargs: object,
) -> FlextResult[FlextOracleOicModels.OICAuthConfig]:
    """Create OIC authentication configuration.

    Args:
    client_id: OAuth2 client ID
    client_secret: OAuth2 client secret
    token_url: IDCS token endpoint URL
    **kwargs: Additional configuration parameters

    Returns:
    FlextResult with FlextOracleOicModels.OICAuthConfig or error message.

    """
    try:
        config: dict[str, t.GeneralValueType] = FlextOracleOicModels.OICAuthConfig(
            oauth_client_id=client_id,
            oauth_client_secret=SecretStr(client_secret),
            oauth_token_url=token_url,
            oauth_scope=str(kwargs.get("oauth_scope", "urn:opc:resource:consumer:all")),
        )

        return FlextResult[FlextOracleOicModels.OICAuthConfig].ok(config)

    except (ValueError, TypeError) as e:
        return FlextResult[FlextOracleOicModels.OICAuthConfig].fail(
            f"Failed to create OIC auth config: {e}"
        )


def create_oic_connection_config(
    base_url: str,
    **kwargs: object,
) -> FlextResult[FlextOracleOicModels.OICConnectionConfig]:
    """Create OIC connection configuration.

    Args:
    base_url: OIC instance base URL
    **kwargs: Additional configuration parameters

    Returns:
    FlextResult with FlextOracleOicModels.OICConnectionConfig or error message.

    """
    try:
        config: dict[str, t.GeneralValueType] = (
            FlextOracleOicModels.OICConnectionConfig(
                base_url=base_url,
                api_version=str(kwargs.get("api_version", "v1")),
                request_timeout=int(kwargs.get("request_timeout", 30)),
                max_retries=int(kwargs.get("max_retries", 3)),
            )
        )

        return FlextResult[FlextOracleOicModels.OICConnectionConfig].ok(config)

    except (ValueError, TypeError) as e:
        return FlextResult[FlextOracleOicModels.OICConnectionConfig].fail(
            f"Failed to create OIC connection config: {e}",
        )


def validate_oic_config(config: object) -> FlextResult[bool]:
    """Validate OIC tap configuration.

    Args:
    config: Configuration to validate

    Returns:
    FlextResult with validation success or error message.

    """
    try:
        # Basic validation for dictionary config
        if isinstance(config, dict):
            required_keys = [
                "oauth_client_id",
                "oauth_client_secret",
                "oauth_token_url",
                "oic_url",
            ]
            missing_keys = [key for key in required_keys if not config.get(key)]

            if missing_keys:
                return FlextResult[bool].fail(
                    f"Missing required configuration keys: {missing_keys}",
                )

        return FlextResult[bool].ok(data=True)

    except (ValueError, TypeError) as e:
        return FlextResult[bool].fail(f"Failed to validate OIC config: {e}")


# Export simplified API
__all__: list[str] = [
    "create_oic_auth_config",
    "create_oic_connection_config",
    "setup_oic_tap",
    "validate_oic_config",
]
