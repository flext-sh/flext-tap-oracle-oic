"""OracleOic.FlextTapOracleOicIntegration entity model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from datetime import datetime
from typing import Annotated

from flext_oracle_oic import m
from flext_tap_oracle_oic import c, t, u


class FlextTapOracleOicIntegration(m):
    """OIC integration domain entity using flext-core patterns."""

    integration_id: Annotated[
        str,
        u.Field(..., min_length=1, description="OIC integration identifier"),
    ]
    integration_code: Annotated[
        str,
        u.Field(..., min_length=1, description="Integration code"),
    ]
    name: Annotated[
        str,
        u.Field(..., min_length=1, description="Integration name"),
    ]
    package_name: Annotated[str | None, u.Field(None, description="Package name")]
    project_name: Annotated[str | None, u.Field(None, description="Project name")]
    integration_type: Annotated[
        str,
        u.Field(
            ...,
            description="Integration type (e.g., APP_DRIVEN, SCHEDULED)",
        ),
    ]
    pattern: Annotated[
        str | None,
        u.Field(None, description="Integration pattern"),
    ]
    style: Annotated[str | None, u.Field(None, description="Integration style")]
    endpoint_url: Annotated[
        str | None,
        u.Field(None, description="Integration endpoint URL"),
    ]
    tracking_level: Annotated[
        str | None,
        u.Field(None, description="Tracking level"),
    ]
    payload_tracking: Annotated[
        bool, u.Field(description="Enable payload tracking")
    ] = False
    integration_status: Annotated[
        c.TapOracleOic.IntegrationStatus,
        u.Field(
            description="Integration status",
        ),
    ] = c.TapOracleOic.IntegrationStatus.CONFIGURED
    activated_at: Annotated[
        datetime | None,
        u.Field(None, description="Activation timestamp"),
    ]
    deactivated_at: Annotated[
        datetime | None,
        u.Field(None, description="Deactivation timestamp"),
    ]
    version: Annotated[str, u.Field(description="Integration version")] = "01.00.0000"
    locked_by: Annotated[
        str | None,
        u.Field(None, description="User who locked the integration"),
    ]
    locked_at: Annotated[
        datetime | None,
        u.Field(None, description="Lock timestamp"),
    ]
    connection_ids: Annotated[
        t.StrSequence,
        u.Field(description="Associated connection IDs"),
    ] = u.Field(default_factory=tuple)
    created_at: Annotated[
        datetime | None,
        u.Field(None, description="Creation timestamp"),
    ]
    updated_at: Annotated[
        datetime | None,
        u.Field(None, description="Last update timestamp"),
    ]

    @property
    def is_active(self) -> bool:
        """Check if integration is active."""
        is_active: bool = (
            self.integration_status == c.TapOracleOic.IntegrationStatus.ACTIVATED
        )
        return is_active

    def activate(self) -> None:
        """Activate the integration."""
        self.integration_status = c.TapOracleOic.IntegrationStatus.ACTIVATED
        self.activated_at = u.now()

    def deactivate(self) -> None:
        """Deactivate the integration."""
        self.integration_status = c.TapOracleOic.IntegrationStatus.DEACTIVATED
        self.deactivated_at = u.now()

    def lock(self, user: str) -> None:
        """Lock the integration for a specific user."""
        self.locked_by = user
        self.locked_at = u.now()
        self.integration_status = c.TapOracleOic.IntegrationStatus.LOCKED

    def unlock(self) -> None:
        """Unlock the integration."""
        self.locked_by = None
        self.locked_at = None


__all__: list[str] = ["FlextTapOracleOicIntegration"]
