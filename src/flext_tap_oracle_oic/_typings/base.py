"""Tap Oracle OIC type alias declarations.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_oracle_oic import FlextOracleOicTypes


class FlextTapOracleOicTypingsBase:
    """Tap Oracle OIC adapter type aliases composed into ``t.TapOracleOic``."""

    type SectionedSummary = FlextOracleOicTypes.MappingKV[
        str,
        FlextOracleOicTypes.MappingKV[str, FlextOracleOicTypes.JsonValue | None],
    ]
    """Two-level summary mapping (section -> field -> value-or-None)."""


__all__: list[str] = [
    "FlextTapOracleOicTypingsBase",
    "SectionedSummary",
]
