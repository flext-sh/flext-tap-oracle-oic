"""Singer Oracle OIC tap protocol contracts.

Only ``TapOracleOic.Paginator`` (consumed by ``models.py``) remains alongside
its Singer SDK helper contracts; every other inner protocol lost its last
consumer and was deleted (STRICT YAGNI).

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_tap_oracle_oic import t

if TYPE_CHECKING:
    from flext_api import FlextApiModels


class FlextTapOracleOicProtocolsBase:
    """Singer Tap Oracle OIC structural protocol contracts for ``p.TapOracleOic``."""

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

    @runtime_checkable
    class SingerProperty(Protocol):
        """Structural contract for one upstream Singer SDK property helper.

        ``singer_sdk`` exposes the property class through a class-body alias
        that the static checkers reject in type position; this pins the
        runtime shape (a named property helper) at the single declaration
        site instead of leaking the partially-unknown member type.

        """

        name: str

    @runtime_checkable
    class SchemaSource(Protocol):
        """Structural contract for Singer SDK schema carriers dumped to JSON."""

        def to_dict(self) -> t.JsonMapping:
            """Dump the carrier to a JSON Schema mapping."""
            ...


__all__: list[str] = [
    "FlextTapOracleOicProtocolsBase",
    "Paginator",
    "SchemaSource",
    "SingerProperty",
]
