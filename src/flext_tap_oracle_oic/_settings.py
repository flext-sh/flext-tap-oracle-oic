"""FLEXT Tap Oracle OIC settings — namespaced under ``settings.TapOracleOic``.

Universal fields via MRO; project fields in the ``TapOracleOic`` group with
simple scalar types (env-settable). URL/header/token construction lives in
consumers (tap.py), not in settings.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, Field
from pydantic_settings import SettingsConfigDict

from flext_core import FlextSettings

_DEFAULT_BASE_URL = "https://localhost.integration.ocp.oraclecloud.com"


class FlextTapOracleOicSettings(FlextSettings):
    """Oracle OIC Singer tap settings; fields under ``settings.TapOracleOic.*``."""

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_TAP_ORACLE_OIC_",
        env_nested_delimiter="__",
        extra="ignore",
    )

    class _TapOracleOic(BaseModel):
        """Namespaced Oracle OIC tap settings."""

        oauth_client_id: Annotated[
            str, Field(default="", description="OAuth client id")
        ]
        oauth_client_secret: Annotated[
            str, Field(default="", description="OAuth client secret")
        ]
        oauth_token_url: Annotated[
            str,
            Field(
                default=f"{_DEFAULT_BASE_URL}/oauth/token",
                description="OAuth token URL",
            ),
        ]
        oauth_audience: Annotated[str, Field(default="", description="OAuth audience")]
        base_url: Annotated[
            str, Field(default=_DEFAULT_BASE_URL, description="OIC base URL")
        ]
        timeout: Annotated[int, Field(default=30, ge=1, description="HTTP timeout (s)")]
        max_retries: Annotated[int, Field(default=3, ge=0, description="Max retries")]
        page_size: Annotated[int, Field(default=10, ge=1, description="Page size")]
        include_extended: Annotated[
            bool, Field(default=False, description="Extended metadata streams")
        ]
        include_monitoring: Annotated[
            bool, Field(default=False, description="Monitoring streams")
        ]
        include_logs: Annotated[bool, Field(default=False, description="Log streams")]
        include_artifacts: Annotated[
            bool, Field(default=False, description="Artifact streams")
        ]

    if TYPE_CHECKING:
        TapOracleOic: _TapOracleOic
    else:
        TapOracleOic: _TapOracleOic = Field(
            default_factory=_TapOracleOic,
            description="Namespaced Oracle OIC tap settings.",
        )


settings: FlextTapOracleOicSettings = FlextTapOracleOicSettings.fetch_global()
"""Pre-instantiated project settings singleton — ``from flext_tap_oracle_oic import settings``."""

__all__: list[str] = ["FlextTapOracleOicSettings", "settings"]
