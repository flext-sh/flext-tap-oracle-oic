# AUTO-GENERATED FILE — Regenerate with: make gen
"""FLEXT Tap Oracle OIC Types — MRO composition of parent type namespaces.

All Singer protocol types are in ``m.Meltano.*``.
All Oracle OIC domain types are in ``t.OracleOic.*``.
This facade composes both via MRO — access as ``t.Meltano.*`` and ``t.OracleOic.*``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_meltano import FlextMeltanoTypes
from flext_oracle_oic import FlextOracleOicTypes

from flext_tap_oracle_oic._typings import FlextTapOracleOicTypingsBase


class FlextTapOracleOicTypes(FlextMeltanoTypes, FlextOracleOicTypes):
    """MRO facade composing Meltano + Oracle OIC type namespaces."""

    class TapOracleOic(FlextTapOracleOicTypingsBase):
        """Tap Oracle OIC namespace composing the ``_typings`` family base."""


t = FlextTapOracleOicTypes

__all__: list[str] = ["FlextTapOracleOicTypes", "t"]
