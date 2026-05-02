"""OracleOic.OICProject entity model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Annotated

from flext_oracle_oic import m
from flext_tap_oracle_oic import t, u


class OICProject(m):
    """OIC project domain entity using flext-core patterns."""

    project_id: Annotated[
        t.NonEmptyStr,
        u.Field(..., description="OIC project identifier"),
    ]
    project_code: Annotated[
        t.NonEmptyStr,
        u.Field(..., description="Project code"),
    ]
    name: Annotated[t.NonEmptyStr, u.Field(..., description="Project name")]
    integration_ids: Annotated[
        MutableSequence[str],
        u.Field(description="Integration IDs in project"),
    ] = u.Field(default_factory=list)
    connection_ids: Annotated[
        t.StrSequence,
        u.Field(description="Connection IDs in project"),
    ] = u.Field(default_factory=tuple)
    lookup_ids: Annotated[
        t.StrSequence,
        u.Field(description="Lookup IDs in project"),
    ] = u.Field(default_factory=tuple)
    deployment_status: Annotated[
        str | None,
        u.Field(None, description="Deployment status"),
    ]
    deployed_at: Annotated[
        datetime | None,
        u.Field(None, description="Deployment timestamp"),
    ]
    deployed_by: Annotated[
        str | None,
        u.Field(None, description="User who deployed"),
    ]
    created_at: Annotated[
        datetime | None,
        u.Field(None, description="Creation timestamp"),
    ]
    updated_at: Annotated[
        datetime | None,
        u.Field(None, description="Last update timestamp"),
    ]

    @property
    def total_resources(self) -> int:
        """Get total number of resources in project."""
        return (
            len(self.integration_ids) + len(self.connection_ids) + len(self.lookup_ids)
        )

    def add_integration(self, integration_id: str) -> None:
        """Add integration to project."""
        if integration_id not in self.integration_ids:
            self.integration_ids.append(integration_id)

    def deploy(self, user: str) -> None:
        """Deploy the project."""
        self.deployment_status = "deployed"
        self.deployed_at = datetime.now(UTC)
        self.deployed_by = user

    def remove_integration(self, integration_id: str) -> None:
        """Remove integration from project."""
        if integration_id in self.integration_ids:
            self.integration_ids.remove(integration_id)


__all__: list[str] = ["OICProject"]
