"""FLEXT Tap Oracle OIC Types — MRO composition of parent type namespaces.

All Singer protocol types are in ``FlextMeltanoTypes.Meltano.*``.
All Oracle OIC domain types are in ``FlextOracleOicTypes.OracleOic.*``.
This facade composes both via MRO — access as ``t.Meltano.*`` and ``t.OracleOic.*``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import TypeAdapter

from flext_meltano import FlextMeltanoTypes
from flext_oracle_oic import FlextOracleOicTypes


class FlextTapOracleOicTypes(FlextMeltanoTypes, FlextOracleOicTypes):
    """MRO facade composing Meltano + Oracle OIC type namespaces."""

    CONTAINER_VALUE_MAP_ADAPTER: TypeAdapter[
        FlextMeltanoTypes.ContainerValueMapping
    ] = TypeAdapter(FlextMeltanoTypes.ContainerValueMapping)


t = FlextTapOracleOicTypes
__all__ = ["FlextTapOracleOicTypes", "t"]
