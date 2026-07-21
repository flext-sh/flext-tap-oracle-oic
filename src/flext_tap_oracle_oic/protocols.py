"""Singer Oracle OIC tap protocols for FLEXT ecosystem.

Of the 5 inner ``TapOracleOic.*`` Protocol classes that previously lived
here, 3 had **zero workspace consumers** (per AGENTS.md §3.5 + STRICT YAGNI
they were deleted). Only ``TapOracleOic.Paginator`` (consumed by
``models.py``) and ``TapOracleOic.PropertiesListLike`` (consumed by
``_models/streams.py``) remain.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import p
from flext_oracle_oic import FlextOracleOicProtocols

if TYPE_CHECKING:
    from flext_api import FlextApiModels
    from flext_tap_oracle_oic import t


class FlextTapOracleOicProtocols(p, FlextOracleOicProtocols):
    """Singer Oracle OIC tap protocols facade — composes Meltano + OracleOic."""

    class TapOracleOic:
        """Singer Tap Oracle OIC structural protocols (consumer surface)."""

        @runtime_checkable
        class Paginator(Protocol):
            """Structural paginator contract used by stream models."""

            current_value: int

            def get_next(
                self,
                response: FlextApiModels.Api.HttpResponse,
            ) -> int | None:
                """Return the next pagination token for a response."""
                ...

        @runtime_checkable
        class PropertiesListLike(Protocol):
            """Structural protocol for singer PropertiesList-compatible objects."""

            def to_dict(self) -> t.JsonMapping:
                """Convert properties list to dictionary representation."""
                ...


p = FlextTapOracleOicProtocols
__all__: list[str] = ["FlextTapOracleOicProtocols", "p"]
