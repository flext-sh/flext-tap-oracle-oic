"""OIC API response envelope model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated

from flext_meltano import FlextMeltanoModels

from flext_tap_oracle_oic import t, u


class FlextTapOracleOicEnvelope(FlextMeltanoModels.Entity):
    """OIC API response envelope for paginated list endpoints.

    Parses the outer wrapper that Oracle OIC returns for list responses,
    normalizing between 'items', 'data', 'count', and 'totalSize' fields.
    """

    items: Annotated[
        t.SequenceOf[t.JsonMapping] | None,
        u.Field(None, description="Records in the returned page"),
    ] = None
    data: Annotated[
        t.SequenceOf[t.JsonMapping] | None,
        u.Field(None, description="Alternative records payload returned by OIC"),
    ] = None
    total_size: Annotated[
        int | None,
        u.Field(
            None,
            alias="totalSize",
            description="Total number of records available server-side",
        ),
    ] = None
    count: Annotated[
        int | None,
        u.Field(None, description="Number of records present in this response"),
    ] = None


__all__: list[str] = ["FlextTapOracleOicEnvelope"]
