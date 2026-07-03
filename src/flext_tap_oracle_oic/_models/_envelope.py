"""OIC API response envelope model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated

from flext_meltano import FlextMeltanoModels
from flext_tap_oracle_oic import t, u


class OicEnvelope(FlextMeltanoModels.BaseModel):
    """OIC API response envelope for paginated list endpoints.

    Parses the outer wrapper that Oracle OIC returns for list responses,
    normalizing between 'items', 'data', 'count', and 'totalSize' fields.
    """

    items: t.SequenceOf[t.JsonMapping] | None = None
    data: t.SequenceOf[t.JsonMapping] | None = None
    total_size: Annotated[int | None, u.Field(alias="totalSize")] = None
    count: int | None = None


__all__: list[str] = ["OicEnvelope"]
