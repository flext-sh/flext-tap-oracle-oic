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

if TYPE_CHECKING:
    from flext_core import p

    from flext_tap_oracle_oic import t


class FlextTapOracleOicProtocolsEnvelope:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class Envelope(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def domain_events(self) -> Sequence[p.DomainEvent]:
            """List of uncommitted domain events for event sourcing."""
            ...

        items: Sequence[t.JsonMapping] | None
        data: Sequence[t.JsonMapping] | None
        total_size: int | None
        count: int | None


__all__: list[str] = [
    "FlextTapOracleOicProtocolsEnvelope",
]
