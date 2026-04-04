"""FLEXT Tap Oracle OIC Types — MRO composition of parent type namespaces.

All Singer protocol types are in ``FlextMeltanoTypes.Meltano.*``.
All Oracle OIC domain types are in ``FlextOracleOicTypes.OracleOic.*``.
This facade composes both via MRO — access as ``t.Meltano.*`` and ``t.OracleOic.*``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence

from pydantic import ConfigDict, TypeAdapter

from flext_core import FlextTypes
from flext_meltano import FlextMeltanoTypes
from flext_oracle_oic import FlextOracleOicTypes


class FlextTapOracleOicTypes(FlextMeltanoTypes, FlextOracleOicTypes):
    """MRO facade composing Meltano + Oracle OIC type namespaces."""

    CONTAINER_VALUE_MAP_ADAPTER: TypeAdapter[
        FlextMeltanoTypes.ContainerValueMapping
    ] = TypeAdapter(FlextMeltanoTypes.ContainerValueMapping)

    # ── Strict adapters (from utilities.py) ───────────────────────
    STRICT_LIST_ADAPTER: TypeAdapter[FlextTypes.ContainerValueList] = TypeAdapter(
        FlextTypes.ContainerValueList,
        config=ConfigDict(strict=True),
    )
    STRICT_MAP_ADAPTER: TypeAdapter[FlextTypes.ContainerValueMapping] = TypeAdapter(
        FlextTypes.ContainerValueMapping,
        config=ConfigDict(strict=True),
    )
    STRICT_INT_ADAPTER: TypeAdapter[int] = TypeAdapter(
        int,
        config=ConfigDict(strict=True),
    )

    # ── General adapters (from models.py) ─────────────────────────
    GENERAL_LIST_ADAPTER: TypeAdapter[Sequence[FlextTypes.ContainerValue]] = (
        TypeAdapter(
            Sequence[FlextTypes.ContainerValue],
            config=ConfigDict(strict=True),
        )
    )
    GENERAL_MAP_ADAPTER: TypeAdapter[Mapping[str, FlextTypes.ContainerValue]] = (
        TypeAdapter(
            Mapping[str, FlextTypes.ContainerValue],
            config=ConfigDict(strict=True),
        )
    )
    STRING_LIST_ADAPTER: TypeAdapter[FlextTypes.StrSequence] = TypeAdapter(
        FlextTypes.StrSequence,
        config=ConfigDict(strict=True),
    )

    # ── Schema adapter (from _models/streams.py) ─────────────────
    SCHEMA_ADAPTER: TypeAdapter[FlextTypes.ContainerValueMapping] = TypeAdapter(
        FlextTypes.ContainerValueMapping,
    )


t = FlextTapOracleOicTypes
__all__ = ["FlextTapOracleOicTypes", "t"]
