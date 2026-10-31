# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contract.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_tap_oracle_oic/_protocols/generated_models_taporacleoic
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    from collections.abc import Mapping as collections_abc_Mapping

    import pydantic


class FlextTapOracleOicProtocolsGeneratedModelsTapOracleOic:
    """Own the structural model contract declared by this module."""

    @runtime_checkable
    class TapOracleOic(Protocol):
        """Structural data contract projected from the owning model."""

        settings: collections_abc_Mapping[str, pydantic.JsonValue]
        name: str
        replication_key: str | None
        stream_schema: collections_abc_Mapping[str, pydantic.JsonValue]


__all__: list[str] = [
    "FlextTapOracleOicProtocolsGeneratedModelsTapOracleOic",
]
