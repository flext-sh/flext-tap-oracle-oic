"""OIC OicAgentEntity model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, ClassVar, Self

from flext_meltano import FlextMeltanoModels
from flext_tap_oracle_oic import c, t, u
from flext_tap_oracle_oic._models._helpers import validate_entity_identity_and_port

if TYPE_CHECKING:
    from datetime import datetime


class OicAgentEntity(FlextMeltanoModels.Entity):
    """OIC Agent entity for connectivity agents."""

    # Pydantic 2.11 Configuration - Agent Features
    model_config: ClassVar[FlextMeltanoModels.ConfigDict] = (
        FlextMeltanoModels.ConfigDict(
            json_schema_extra={
                "description": "Oracle OIC connectivity agent with health monitoring",
                "examples": [
                    {
                        "agent_id": "AGENT_ONPREM_01",
                        "agent_name": "On-Premises Agent 01",
                        "agent_type": "CONNECTIVITY_AGENT",
                        "status": "ONLINE",
                    }
                ],
            }
        )
    )

    agent_id: Annotated[str, u.Field(..., description="Unique agent identifier")]
    agent_name: Annotated[str, u.Field(..., description="Agent display name")]
    agent_type: Annotated[
        c.TapOracleOic.OicAgentType, u.Field(..., description="Agent type")
    ]

    # Agent status and health
    status: Annotated[
        c.TapOracleOic.OicAgentStatus, u.Field(..., description="Agent status")
    ]
    last_heartbeat: Annotated[
        datetime | None, u.Field(None, description="Last heartbeat timestamp")
    ]
    api_version: Annotated[
        str | None, u.Field(None, description="Agent version from OIC API")
    ]

    # Configuration
    host_machine: Annotated[str | None, u.Field(None, description="Host machine name")]
    installation_path: Annotated[
        str | None, u.Field(None, description="Agent installation path")
    ]
    port: Annotated[int | None, u.Field(None, description="Agent communication port")]

    # Health metrics
    uptime_hours: Annotated[
        float | None, u.Field(None, description="Agent uptime in hours")
    ]
    connection_count: Annotated[
        int | None, u.Field(None, description="Active connection count")
    ]
    last_error: Annotated[str | None, u.Field(None, description="Last error message")]

    @u.computed_field
    @property
    def agent_health_summary(self) -> t.TapOracleOic.SectionedSummary:
        """OIC agent health and connectivity summary."""
        health_status = c.TapOracleOic.OicHealthStatus.HEALTHY.value
        if self.status in {"ERROR", "OFFLINE"}:
            health_status = c.TapOracleOic.OicHealthStatus.UNHEALTHY.value
        elif self.last_error:
            health_status = c.TapOracleOic.OicHealthStatus.DEGRADED.value

        return {
            "agent_identity": {
                "id": self.agent_id,
                "name": self.agent_name,
                "type": self.agent_type,
                "version": self.api_version,
                "status": self.status,
            },
            "connectivity": {
                "host_machine": self.host_machine,
                "port": self.port,
                "last_heartbeat": self.last_heartbeat.isoformat()
                if self.last_heartbeat
                else None,
                "connection_count": self.connection_count or 0,
            },
            "health": {
                "health_status": health_status,
                "uptime_hours": self.uptime_hours or 0.0,
                "has_error": bool(self.last_error),
                "last_error": self.last_error,
            },
            "configuration": {"installation_path": self.installation_path},
        }

    @u.model_validator(mode="after")
    def validate_agent_entity(self) -> Self:
        """Validate OIC agent entity."""
        validate_entity_identity_and_port(
            entity_id=self.agent_id,
            entity_name=self.agent_name,
            id_label="Agent ID",
            name_label="Agent name",
            port=self.port,
        )
        return self


__all__: list[str] = ["OicAgentEntity"]
