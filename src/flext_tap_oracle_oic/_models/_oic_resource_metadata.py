"""OracleOic.FlextTapOracleOicResourceMetadata entity model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from flext_oracle_oic import m
from flext_tap_oracle_oic import c, t, u

if TYPE_CHECKING:
    from datetime import datetime


class FlextTapOracleOicResourceMetadata(m):
    """OIC resource metadata value object."""

    resource_type: Annotated[
        c.TapOracleOic.OICResourceType, u.Field(..., description="Resource type")
    ]
    resource_id: Annotated[
        t.NonEmptyStr, u.Field(..., description="Resource identifier")
    ]
    name: Annotated[t.NonEmptyStr, u.Field(..., description="Resource name")]
    version: Annotated[str | None, u.Field(None, description="Resource version")]
    created_at: Annotated[
        datetime | None, u.Field(None, description="Creation timestamp")
    ]
    updated_at: Annotated[
        datetime | None, u.Field(None, description="Last update timestamp")
    ]


__all__: list[str] = ["FlextTapOracleOicResourceMetadata"]
