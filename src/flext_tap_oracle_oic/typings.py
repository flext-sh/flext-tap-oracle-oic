"""FLEXT Tap Oracle OIC Types — MRO composition of parent type namespaces.

All Singer protocol types are in ``m.Meltano.*``.
All Oracle OIC domain types are in ``FlextOracleOicTypes.OracleOic.*``.
This facade composes both via MRO — access as ``t.Meltano.*`` and ``t.OracleOic.*``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from pydantic import ConfigDict, TypeAdapter

from flext_core import t
from flext_meltano import FlextMeltanoTypingsSinger, m
from flext_oracle_oic import FlextOracleOicTypes


class FlextTapOracleOicTypes(m, FlextOracleOicTypes):
    """MRO facade composing Meltano + Oracle OIC type namespaces."""

    class Meltano(m.Meltano, FlextMeltanoTypingsSinger):
        """Extended Meltano namespace with Singer type aliases."""

    CONTAINER_VALUE_MAP_ADAPTER: m.TypeAdapter[t.ContainerValueMapping] = m.TypeAdapter(
        t.ContainerValueMapping
    )

    # ── Strict adapters (from utilities.py) ───────────────────────
    STRICT_LIST_ADAPTER: m.TypeAdapter[t.ContainerValueList] = TypeAdapter(
        t.ContainerValueList,
        config=ConfigDict(strict=True),
    )
    STRICT_MAP_ADAPTER: m.TypeAdapter[t.ContainerValueMapping] = TypeAdapter(
        t.ContainerValueMapping,
        config=ConfigDict(strict=True),
    )
    STRICT_INT_ADAPTER: m.TypeAdapter[int] = TypeAdapter(
        int,
        config=ConfigDict(strict=True),
    )

    # ── General adapters (from models.py) ─────────────────────────
    GENERAL_LIST_ADAPTER: m.TypeAdapter[Sequence[t.ContainerValue]] = TypeAdapter(
        Sequence[t.ContainerValue],
        config=ConfigDict(strict=True),
    )
    GENERAL_MAP_ADAPTER: m.TypeAdapter[Mapping[str, t.ContainerValue]] = TypeAdapter(
        Mapping[str, t.ContainerValue],
        config=ConfigDict(strict=True),
    )
    STRING_LIST_ADAPTER: m.TypeAdapter[t.StrSequence] = TypeAdapter(
        t.StrSequence,
        config=ConfigDict(strict=True),
    )

    # ── Schema adapter (from _models/streams.py) ─────────────────
    SCHEMA_ADAPTER: m.TypeAdapter[t.ContainerValueMapping] = TypeAdapter(
        t.ContainerValueMapping,
    )


t = FlextTapOracleOicTypes

__all__: list[str] = ["FlextTapOracleOicTypes", "t"]
