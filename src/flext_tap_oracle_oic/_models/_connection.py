"""OIC OicConnectionEntity model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Annotated, ClassVar, Self

from flext_meltano import FlextMeltanoModels
from flext_tap_oracle_oic import c, t, u
from flext_tap_oracle_oic._models._helpers import validate_entity_identity_and_port


class OicConnectionEntity(FlextMeltanoModels.Entity):
    """OIC Connection entity with security sanitization."""

    # Pydantic 2.11 Configuration - Connection Features
    model_config: ClassVar[FlextMeltanoModels.ConfigDict] = (
        FlextMeltanoModels.ConfigDict(
            json_schema_extra={
                "description": "Oracle OIC connection with security sanitization",
                "examples": [
                    {
                        "connection_id": "SALESFORCE_CONN_01",
                        "name": "Salesforce Production",
                        "connection_type": "SALESFORCE_ADAPTER",
                        "status": "ACTIVE",
                    },
                ],
            },
        )
    )

    connection_id: Annotated[
        str,
        u.Field(..., description="Unique connection identifier"),
    ]
    name: Annotated[str, u.Field(..., description="Connection name")]
    description: Annotated[
        str | None,
        u.Field(None, description="Connection description"),
    ]
    connection_type: Annotated[
        str,
        u.Field(..., description="Connection adapter type"),
    ]

    host: Annotated[
        str | None,
        u.Field(
            None,
            description="Connection host (if applicable)",
        ),
    ]
    port: Annotated[
        int | None,
        u.Field(
            None,
            description="Connection port (if applicable)",
        ),
    ]

    # Security metadata (credentials removed)
    authentication_type: Annotated[
        str | None,
        u.Field(
            None,
            description="Authentication method used",
        ),
    ]
    security_policy: Annotated[
        str | None,
        u.Field(
            None,
            description="Security policy name",
        ),
    ]
    certificate_alias: Annotated[
        str | None,
        u.Field(
            None,
            description="Certificate alias (if used)",
        ),
    ]

    # Status and health
    status: Annotated[
        c.TapOracleOic.OicIntegrationStatus,
        u.Field(
            ...,
            description="Connection status",
        ),
    ]
    last_tested: Annotated[
        datetime | None,
        u.Field(
            None,
            description="Last connection test timestamp",
        ),
    ]
    test_result: Annotated[
        str | None,
        u.Field(None, description="Last test result"),
    ]

    # Sanitization markers
    data_sanitized: Annotated[
        bool,
        u.Field(
            description="Indicates if sensitive data was removed",
        ),
    ] = True
    sanitization_timestamp: Annotated[
        datetime | None,
        u.Field(
            description="When sanitization occurred",
        ),
    ] = u.Field(default_factory=lambda: datetime.now(UTC))

    @u.computed_field()
    @property
    def connection_security_summary(
        self,
    ) -> t.TapOracleOic.SectionedSummary:
        """OIC connection security and health summary."""
        return {
            "connection_identity": {
                "id": self.connection_id,
                "name": self.name,
                "type": self.connection_type,
                "status": self.status,
            },
            "connectivity": {
                "host": self.host,
                "port": self.port,
                "last_tested": self.last_tested.isoformat()
                if self.last_tested
                else None,
                "test_result": self.test_result,
            },
            "security": {
                "auth_type": self.authentication_type,
                "security_policy": self.security_policy,
                "certificate_alias": self.certificate_alias,
                "data_sanitized": self.data_sanitized,
                "sanitization_timestamp": self.sanitization_timestamp.isoformat()
                if self.sanitization_timestamp
                else None,
            },
        }

    @u.model_validator(mode="after")
    def validate_connection_entity(self) -> Self:
        """Validate OIC connection entity."""
        validate_entity_identity_and_port(
            entity_id=self.connection_id,
            entity_name=self.name,
            id_label="Connection ID",
            name_label="Connection name",
            port=self.port,
        )
        return self


__all__: list[str] = ["OicConnectionEntity"]
