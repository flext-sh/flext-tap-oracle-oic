"""FLEXT Tap Oracle OIC Types — MRO composition of parent type namespaces.

All Singer protocol types are in ``m.Meltano.*``.
All Oracle OIC domain types are in ``t.OracleOic.*``.
This facade composes both via MRO — access as ``t.Meltano.*`` and ``t.OracleOic.*``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import t as meltano_t
from flext_oracle_oic import t


class FlextTapOracleOicTypes(meltano_t, t):
    """MRO facade composing Meltano + Oracle OIC type namespaces."""

    class TapOracleOic:
        """Tap Oracle OIC-specific adapter namespace."""

        type SectionedSummary = t.MappingKV[str, t.MappingKV[str, t.JsonValue | None]]
        """Two-level summary mapping (section -> field -> value-or-None)."""


t = FlextTapOracleOicTypes

__all__: list[str] = ["FlextTapOracleOicTypes", "t"]
