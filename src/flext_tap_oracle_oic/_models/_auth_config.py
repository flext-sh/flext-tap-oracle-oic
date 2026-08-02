"""OIC OicAuthenticationConfig model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, ClassVar, Self

from flext_meltano import FlextMeltanoModels
from flext_tap_oracle_oic import c, t, u


class OicAuthenticationConfig(FlextMeltanoModels.ArbitraryTypesModel):
    """OAuth2/IDCS authentication configuration for OIC API access."""

    # Pydantic 2.11 Configuration - Authentication Features
    model_config: ClassVar[FlextMeltanoModels.ConfigDict] = (
        FlextMeltanoModels.ConfigDict(
            json_schema_extra={
                "description": "OAuth2/IDCS authentication for Oracle OIC API",
                "examples": [
                    {
                        "oauth_client_id": "my-client-id",
                        "oauth_token_url": "https://idcs-instance.identity.oraclecloud.com/oauth2/v1/token",
                        "base_url": "https://mycompany-oic.integration.ocp.oraclecloud.com",
                    }
                ],
            }
        )
    )

    oauth_client_id: Annotated[
        str, u.Field(..., description="OAuth2 client ID for OIC API")
    ]
    oauth_client_secret: Annotated[
        str, u.Field(..., description="OAuth2 client secret")
    ]
    oauth_token_url: Annotated[
        str, u.Field(..., description="IDCS OAuth2 token endpoint URL")
    ]
    oauth_client_aud: Annotated[
        str, u.Field(..., description="OAuth2 audience parameter")
    ]
    base_url: Annotated[str, u.Field(..., description="OIC instance base URL")]

    # Optional authentication settings
    token_expiry_buffer: Annotated[
        int, u.Field(description="Token refresh buffer in seconds")
    ] = 300
    max_retry_attempts: Annotated[
        int, u.Field(description="Maximum authentication retry attempts")
    ] = 3
    timeout_seconds: Annotated[int, u.Field(description="Authentication timeout")] = 30

    @u.computed_field
    @property
    def auth_config_summary(self) -> t.TapOracleOic.SectionedSummary:
        """OAuth2 authentication configuration summary."""
        min_name_length: int = 2
        return {
            "oauth_setup": {
                "client_id": self.oauth_client_id[:min_name_length] + "..."
                if len(self.oauth_client_id) > min_name_length
                else self.oauth_client_id,
                "token_endpoint": self.oauth_token_url,
                "audience": self.oauth_client_aud,
            },
            "oic_instance": {
                "base_url": self.base_url,
                "domain": self.base_url.split("//")[-1].split("/")[0]
                if "//" in self.base_url
                else self.base_url,
            },
            "security_settings": {
                "token_buffer_seconds": self.token_expiry_buffer,
                "max_retry_attempts": self.max_retry_attempts,
                "timeout_seconds": self.timeout_seconds,
            },
        }

    @u.model_validator(mode="after")
    def validate_auth_config(self) -> Self:
        """Validate OAuth2 authentication configuration."""
        if not self.oauth_token_url.startswith("https://"):
            msg = "OAuth token URL must use HTTPS"
            raise ValueError(msg)
        if not self.base_url.startswith("https://"):
            msg = "OIC base URL must use HTTPS"
            raise ValueError(msg)
        if self.token_expiry_buffer < c.TapOracleOic.MIN_TOKEN_EXPIRY_BUFFER:
            msg = "Token expiry buffer must be at least 60 seconds"
            raise ValueError(msg)
        return self


__all__: list[str] = ["OicAuthenticationConfig"]
