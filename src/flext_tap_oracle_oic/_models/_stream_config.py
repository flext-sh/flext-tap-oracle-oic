"""OIC OicStreamConfiguration model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, ClassVar, Self

from flext_meltano import FlextMeltanoModels
from flext_tap_oracle_oic import c, t, u


class OicStreamConfiguration(FlextMeltanoModels.ArbitraryTypesModel):
    """Configuration for OIC tap streams."""

    # Pydantic 2.11 Configuration - Stream Features
    model_config: ClassVar[FlextMeltanoModels.ConfigDict] = (
        FlextMeltanoModels.ConfigDict(
            json_schema_extra={
                "description": "Oracle OIC tap stream configuration with filtering",
                "examples": [
                    {
                        "stream_name": "integrations",
                        "replication_method": "INCREMENTAL",
                        "replication_key": "last_updated",
                        "page_size": 100,
                    }
                ],
            }
        )
    )

    stream_name: Annotated[str, u.Field(..., description="Singer stream name")]
    replication_method: Annotated[
        c.TapOracleOic.OicReplicationMethod, u.Field(description="Replication method")
    ] = c.TapOracleOic.OicReplicationMethod.FULL_TABLE
    replication_key: Annotated[
        str | None, u.Field(None, description="Replication key field name")
    ]

    # Pagination and performance
    page_size: Annotated[
        int, u.Field(ge=1, le=1000, description="API pagination size")
    ] = 100
    include_extended: Annotated[
        bool, u.Field(description="Include extended entity metadata")
    ] = False

    # Filtering
    status_filter: Annotated[
        t.StrSequence | None,
        u.Field(None, description="Filter by entity status values"),
    ]
    date_range_filter: Annotated[
        str | None,
        u.Field(None, description="Date range filter for incremental streams"),
    ]

    # Security
    sanitize_sensitive_data: Annotated[
        bool, u.Field(description="Enable data sanitization")
    ] = True
    exclude_test_entities: Annotated[
        bool, u.Field(description="Exclude test/demo entities")
    ] = True

    @u.computed_field()
    @property
    def stream_config_summary(self) -> t.TapOracleOic.SectionedSummary:
        """OIC stream configuration summary."""
        return {
            "stream_identity": {
                "name": self.stream_name,
                "replication_method": self.replication_method,
                "replication_key": self.replication_key,
                "is_incremental": self.replication_method == "INCREMENTAL",
            },
            "performance": {
                "page_size": self.page_size,
                "include_extended": self.include_extended,
            },
            "filtering": {
                "status_filters": len(self.status_filter) if self.status_filter else 0,
                "date_range_filter": bool(self.date_range_filter),
                "exclude_test_entities": self.exclude_test_entities,
            },
            "security": {"sanitize_sensitive_data": self.sanitize_sensitive_data},
        }

    @u.model_validator(mode="after")
    def validate_stream_config(self) -> Self:
        """Validate OIC stream configuration."""
        if not self.stream_name:
            msg = "Stream name is required"
            raise ValueError(msg)
        if self.replication_method == "INCREMENTAL" and not self.replication_key:
            msg = "Incremental replication requires a replication key"
            raise ValueError(msg)
        if self.page_size <= 0 or self.page_size > c.MAX_ITEMS:
            msg = "Page size must be between 1 and 1000"
            raise ValueError(msg)
        return self


__all__: list[str] = ["OicStreamConfiguration"]
