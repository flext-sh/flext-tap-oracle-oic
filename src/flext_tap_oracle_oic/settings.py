"""FLEXT Tap Oracle OIC Configuration - Enhanced FlextSettings Implementation.

Single unified configuration class for Oracle Integration Cloud Singer tap
operations following FLEXT 1.0.0 patterns with enhanced singleton, SecretStr,
and Pydantic 2.11+ features.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated, ClassVar, Self

from pydantic import Field, SecretStr
from pydantic_settings import SettingsConfigDict

from flext_core import FlextSettings
from flext_oracle_oic import FlextOracleOicSettings
from flext_tap_oracle_oic import c, p, r, t


@FlextSettings.auto_register("tap-oracle-oic")
class FlextTapOracleOicSettings(FlextOracleOicSettings):
    """Tap-specific OIC settings contract."""

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_prefix="FLEXT_TAP_ORACLE_OIC_", extra="ignore"
    )

    oauth_client_id: Annotated[str, Field(default="")]
    oauth_client_secret: Annotated[SecretStr, Field(default=SecretStr(""))]
    oauth_token_url: Annotated[
        str, Field(default=f"{c.OracleOic.DEFAULT_BASE_URL}/oauth/token")
    ]
    oauth_audience: Annotated[str, Field(default="")]
    base_url: Annotated[str, Field(default=c.OracleOic.DEFAULT_BASE_URL)]
    timeout: Annotated[t.PositiveInt, Field(default=c.DEFAULT_TIMEOUT_SECONDS)]
    max_retries: Annotated[
        t.NonNegativeInt, Field(default=c.TapOracleOic.DEFAULT_MAX_RETRIES)
    ]
    page_size: Annotated[
        t.PositiveInt, Field(default=c.TapOracleOic.TapOicProcessing.DEFAULT_PAGE_SIZE)
    ]

    def get_api_base_url(self) -> str:
        """Return base URL without trailing slash."""
        return self.base_url.rstrip("/")

    def get_headers(self) -> t.StrMapping:
        """Return default headers for OIC requests."""
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def get_token_request_data(self) -> t.StrMapping:
        """Return OAuth2 client credentials payload."""
        return {
            "grant_type": "client_credentials",
            "client_id": self.oauth_client_id,
            "client_secret": self.oauth_client_secret.get_secret_value(),
            "audience": self.oauth_audience,
        }

    @classmethod
    def create_config(
        cls,
        oauth_params: t.ContainerValueMapping,
        connection_params: t.ContainerValueMapping,
        tap_params: t.ContainerValueMapping | None = None,
    ) -> p.Result[Self]:
        """Create a validated tap configuration from grouped parameter blocks."""
        try:
            tap_config: t.MutableContainerValueMapping = (
                dict(tap_params) if tap_params is not None else {}
            )
            tap_config.setdefault(
                "batch_size",
                c.DEFAULT_SIZE,
            )
            tap_config.setdefault("stream_prefix", "oic")
            config_data = {**oauth_params, **connection_params, **tap_config}
            config_instance = cls.model_validate(config_data)
            return r[Self].ok(config_instance)
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as exc:
            return r[Self].fail(
                f"Oracle OIC tap configuration creation failed: {exc}",
            )

    def validate_configuration(self) -> p.Result[bool]:
        """Validate the current settings instance."""
        required_fields = [
            (self.oauth_client_id, "OAuth client ID is required"),
            (
                self.oauth_client_secret.get_secret_value(),
                "OAuth client secret is required",
            ),
            (self.oauth_audience, "OAuth audience is required"),
        ]
        for field_value, error_message in required_fields:
            if not (field_value and str(field_value).strip()):
                return r[bool].fail(error_message)
        if self.timeout <= 0:
            return r[bool].fail("Timeout must be positive")
        if self.max_retries < 0:
            return r[bool].fail("Max retries cannot be negative")
        if self.page_size <= 0:
            return r[bool].fail("Page size must be positive")
        return r[bool].ok(value=True)
