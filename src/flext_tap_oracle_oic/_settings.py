"""FLEXT Tap Oracle OIC settings — namespaced under ``settings.TapOracleOic``.

Universal fields via MRO; project fields in the ``TapOracleOic`` group with
simple scalar types (env-settable). URL/header/token construction lives in
consumers (tap.py), not in settings.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from flext_core import FlextSettings, m

_DEFAULT_BASE_URL = "https://localhost.integration.ocp.oraclecloud.com"


class FlextTapOracleOicSettings(FlextSettings):
    """Oracle OIC Singer tap settings; fields under ``settings.TapOracleOic.*``."""

    model_config = m.SettingsConfigDict(
        env_prefix="FLEXT_TAP_ORACLE_OIC_",
        env_nested_delimiter="__",
        extra="ignore",
    )

    class _TapOracleOic(m.StrictModel):
        """Namespaced Oracle OIC tap settings."""

        oauth_client_id: Annotated[str, m.Field(description="OAuth client id")] = ""
        oauth_client_secret: Annotated[
            str, m.Field(description="OAuth client secret")
        ] = ""
        oauth_token_url: Annotated[
            str,
            m.Field(
                description="OAuth token URL",
            ),
        ] = f"{_DEFAULT_BASE_URL}/oauth/token"
        oauth_audience: Annotated[str, m.Field(description="OAuth audience")] = ""
        base_url: Annotated[str, m.Field(description="OIC base URL")] = (
            _DEFAULT_BASE_URL
        )
        timeout: Annotated[int, m.Field(ge=1, description="HTTP timeout (s)")] = 30
        max_retries: Annotated[int, m.Field(ge=0, description="Max retries")] = 3
        page_size: Annotated[int, m.Field(ge=1, description="Page size")] = 10
        include_extended: Annotated[
            bool, m.Field(description="Extended metadata streams")
        ] = False
        include_monitoring: Annotated[
            bool, m.Field(description="Monitoring streams")
        ] = False
        include_logs: Annotated[bool, m.Field(description="Log streams")] = False
        include_artifacts: Annotated[bool, m.Field(description="Artifact streams")] = (
            False
        )

    if TYPE_CHECKING:
        TapOracleOic: _TapOracleOic
    else:
        TapOracleOic: _TapOracleOic = m.Field(
            default_factory=_TapOracleOic,
            description="Namespaced Oracle OIC tap settings.",
        )


settings: FlextTapOracleOicSettings = FlextTapOracleOicSettings.fetch_global()
"""Pre-instantiated settings — ``from flext_tap_oracle_oic import settings``."""

__all__: list[str] = ["FlextTapOracleOicSettings", "settings"]
