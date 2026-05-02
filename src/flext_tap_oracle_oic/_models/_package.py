"""OIC OicPackageEntity model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from datetime import datetime
from typing import Annotated, ClassVar, Self

from flext_meltano import FlextMeltanoModels
from flext_tap_oracle_oic import c, t, u


class OicPackageEntity(FlextMeltanoModels.Entity):
    """OIC Package entity for integration packages."""

    # Pydantic 2.11 Configuration - Package Features
    model_config: ClassVar[FlextMeltanoModels.ConfigDict] = (
        FlextMeltanoModels.ConfigDict(
            json_schema_extra={
                "description": "Oracle OIC package with dependency tracking",
                "examples": [
                    {
                        "package_id": "CUSTOMER_SUITE_V1",
                        "name": "Customer Management Suite",
                        "package_type": "INTEGRATION",
                        "status": "ACTIVE",
                    },
                ],
            },
        )
    )

    package_id: Annotated[
        str,
        u.Field(..., description="Unique package identifier"),
    ]
    name: Annotated[str, u.Field(..., description="Package name")]
    description: Annotated[
        str | None,
        u.Field(None, description="Package description"),
    ]
    api_version: Annotated[
        str,
        u.Field(..., description="Package version from OIC API"),
    ]

    # Package metadata
    package_type: Annotated[
        c.TapOracleOic.OicIntegrationType,
        u.Field(
            ...,
            description="Package type",
        ),
    ]
    created_by: Annotated[
        str | None,
        u.Field(None, description="Package creator"),
    ]
    created_date: Annotated[
        datetime | None,
        u.Field(
            None,
            description="Package creation date",
        ),
    ]

    # Dependencies and relationships
    dependencies: Annotated[
        t.StrSequence,
        u.Field(
            description="List of dependent package IDs",
        ),
    ] = u.Field(default_factory=tuple)
    integration_count: Annotated[
        int | None,
        u.Field(
            None,
            description="Number of integrations in package",
        ),
    ]

    # Status
    status: Annotated[
        c.TapOracleOic.OicIntegrationStatus,
        u.Field(
            ...,
            description="Package status",
        ),
    ]
    download_count: Annotated[
        int | None,
        u.Field(
            None,
            description="Package download count",
        ),
    ]

    @u.computed_field()
    @property
    def package_composition_summary(
        self,
    ) -> t.TapOracleOic.SectionedSummary:
        """OIC package composition and usage summary."""
        dependencies_payload: list[t.JsonValue] = list(self.dependencies)
        composition: dict[str, t.JsonValue | None] = {
            "integration_count": self.integration_count or 0,
            "dependency_count": len(self.dependencies),
            "has_dependencies": bool(self.dependencies),
            "dependencies": dependencies_payload,
        }
        return {
            "package_identity": {
                "id": self.package_id,
                "name": self.name,
                "version": self.api_version,
                "type": self.package_type,
                "status": self.status,
            },
            "composition": composition,
            "usage": {
                "download_count": self.download_count or 0,
                "created_by": self.created_by,
                "created_date": self.created_date.isoformat()
                if self.created_date
                else None,
            },
        }

    @u.model_validator(mode="after")
    def validate_package_entity(self) -> Self:
        """Validate OIC package entity."""
        if not self.package_id:
            msg = "Package ID is required"
            raise ValueError(msg)
        if not self.name:
            msg = "Package name is required"
            raise ValueError(msg)
        if self.integration_count is not None and self.integration_count < 0:
            msg = "Integration count cannot be negative"
            raise ValueError(msg)
        return self


__all__: list[str] = ["OicPackageEntity"]
