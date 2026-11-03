# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_tap_oracle_oic/_protocols/envelope
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols

from flext_tap_oracle_oic import t

if TYPE_CHECKING:
    from flext_core import p


class FlextTapOracleOicProtocolsEnvelope:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class Envelope(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def domain_events(self) -> Sequence[p.DomainEvent]:
            """List of uncommitted domain events for event sourcing."""
            ...

        @property
        def items(self) -> Sequence[t.JsonMapping] | None:
            """Records in the returned page."""
            ...

        @property
        def data(self) -> Sequence[t.JsonMapping] | None:
            """Alternative records payload returned by OIC."""
            ...

        @property
        def total_size(self) -> int | None:
            """Total number of records available server-side."""
            ...

        @property
        def count(self) -> int | None:
            """Number of records present in this response."""
            ...


__all__: list[str] = [
    "FlextTapOracleOicProtocolsEnvelope",
]
