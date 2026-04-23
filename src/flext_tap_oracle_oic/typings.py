"""FLEXT Tap Oracle OIC Types — MRO composition of parent type namespaces.

All Singer protocol types are in ``m.Meltano.*``.
All Oracle OIC domain types are in ``t.OracleOic.*``.
This facade composes both via MRO — access as ``t.Meltano.*`` and ``t.OracleOic.*``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import m, t as meltano_t
from flext_oracle_oic import t


class FlextTapOracleOicTypes(meltano_t, t):
    """MRO facade composing Meltano + Oracle OIC type namespaces."""

    class TapOracleOic:
        """Tap Oracle OIC-specific adapter namespace."""

        CONTAINER_VALUE_MAP_ADAPTER: m.TypeAdapter[t.JsonMapping] = m.TypeAdapter(
            t.JsonMapping
        )

        # ── Strict adapters (from utilities.py) ───────────────────────
        STRICT_LIST_ADAPTER: m.TypeAdapter[t.JsonList] = m.TypeAdapter(
            t.JsonList,
            config=m.ConfigDict(strict=True),
        )
        STRICT_MAP_ADAPTER: m.TypeAdapter[t.JsonMapping] = m.TypeAdapter(
            t.JsonMapping,
            config=m.ConfigDict(strict=True),
        )
        STRICT_INT_ADAPTER: m.TypeAdapter[int] = m.TypeAdapter(
            int,
            config=m.ConfigDict(strict=True),
        )

        # ── General adapters (from models.py) ─────────────────────────
        GENERAL_LIST_ADAPTER: m.TypeAdapter[t.JsonList] = m.TypeAdapter(
            t.JsonList,
            config=m.ConfigDict(strict=True),
        )
        GENERAL_MAP_ADAPTER: m.TypeAdapter[t.JsonMapping] = m.TypeAdapter(
            t.JsonMapping,
            config=m.ConfigDict(strict=True),
        )
        STRING_LIST_ADAPTER: m.TypeAdapter[t.StrSequence] = m.TypeAdapter(
            t.StrSequence,
            config=m.ConfigDict(strict=True),
        )

        # ── Schema adapter (from _models/streams.py) ─────────────────
        SCHEMA_ADAPTER: m.TypeAdapter[t.JsonMapping] = m.TypeAdapter(
            t.JsonMapping,
        )


t = FlextTapOracleOicTypes

__all__: list[str] = ["FlextTapOracleOicTypes", "t"]
