"""Singer Oracle OIC tap protocols for FLEXT ecosystem.

Only ``TapOracleOic.Paginator`` (consumed by ``models.py``) remains; every
other inner protocol lost its last consumer and was deleted (STRICT YAGNI).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols
from flext_oracle_oic import FlextOracleOicProtocols

if TYPE_CHECKING:
    from flext_api import FlextApiModels


class FlextTapOracleOicProtocols(FlextMeltanoProtocols, FlextOracleOicProtocols):
    """Singer Oracle OIC tap protocols facade — composes Meltano + OracleOic."""

    class TapOracleOic:
        """Singer Tap Oracle OIC structural protocols (consumer surface)."""

        @runtime_checkable
        class Paginator(Protocol):
            """Structural paginator contract used by stream models."""

            current_value: int

            def fetch_next(
                self,
                response: FlextApiModels.Api.HttpResponse,
            ) -> int | None:
                """Fetch the next pagination token for a response."""
                ...

        class SingerProperty(Protocol):
            """Structural contract for one upstream Singer SDK property helper.

            ``singer_sdk`` exposes the property class through a class-body alias
            that the static checkers reject in type position; this pins the
            runtime shape (a named property helper) at the single declaration
            site instead of leaking the partially-unknown member type.
            """

            name: str


p = FlextTapOracleOicProtocols
__all__: list[str] = ["FlextTapOracleOicProtocols", "p"]
