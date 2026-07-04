"""OracleOic.FlextTapOracleOicLookup entity model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from flext_oracle_oic import m
from flext_tap_oracle_oic import t, u

if TYPE_CHECKING:
    from datetime import datetime


class FlextTapOracleOicLookup(m):
    """OIC lookup table domain entity using flext-core patterns."""

    lookup_id: Annotated[
        str,
        u.Field(..., min_length=1, description="OIC lookup identifier"),
    ]
    lookup_name: Annotated[
        str,
        u.Field(..., min_length=1, description="Lookup table name"),
    ]
    domain_name: Annotated[str | None, u.Field(None, description="Domain name")]
    columns: Annotated[
        t.SequenceOf[t.JsonMapping],
        u.Field(
            description="Column definitions",
        ),
    ] = u.Field(default_factory=list[t.JsonMapping])
    key_columns: Annotated[
        t.StrSequence,
        u.Field(description="Key column names"),
    ] = u.Field(default_factory=tuple)
    value_columns: Annotated[
        t.StrSequence,
        u.Field(description="Value column names"),
    ] = u.Field(default_factory=tuple)
    row_count: Annotated[t.NonNegativeInt, u.Field(description="Number of rows")] = 0
    data_size_bytes: Annotated[
        t.NonNegativeInt | None,
        u.Field(None, description="Data size in bytes"),
    ]
    locked_by: Annotated[
        str | None,
        u.Field(None, description="User who locked the lookup"),
    ]
    locked_at: Annotated[
        datetime | None,
        u.Field(None, description="Lock timestamp"),
    ]
    last_imported: Annotated[
        datetime | None,
        u.Field(None, description="Last import timestamp"),
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
    def is_empty(self) -> bool:
        """Check if lookup is empty."""
        is_empty: bool = self.row_count == 0
        return is_empty

    def record_import(self) -> None:
        """Record successful import."""
        self.last_imported = u.now()

    def update_statistics(
        self,
        row_count: int,
        data_size: int | None = None,
    ) -> None:
        """Update lookup statistics."""
        self.row_count = row_count
        self.data_size_bytes = data_size


__all__: list[str] = ["FlextTapOracleOicLookup"]
