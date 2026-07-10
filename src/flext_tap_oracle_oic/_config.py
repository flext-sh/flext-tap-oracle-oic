"""FlextTapOracleOicConfig — frozen config singleton for flext-tap-oracle-oic (ADR-005 §7).

Model-less: business rules live in ``config/*.yaml`` under the ``TapOracleOic:`` key and
are exposed through the open ``config.TapOracleOic`` namespace (``extra="allow"``), with
no per-domain model. Access is ``config.TapOracleOic.<domain>[<key>...]``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from flext_meltano import FlextMeltanoConfig


class _TapOracleOicNamespace(BaseModel):
    """Open, frozen namespace exposing every ``config/*.yaml`` domain model-less."""

    model_config = ConfigDict(extra="allow", frozen=True)


class FlextTapOracleOicConfig(FlextMeltanoConfig):
    """TapOracleOic config auto-loaded model-less from ``config/*.yaml``."""

    TapOracleOic: _TapOracleOicNamespace = _TapOracleOicNamespace()


config: FlextTapOracleOicConfig = FlextTapOracleOicConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_tap_oracle_oic import config``."""

__all__: list[str] = ["FlextTapOracleOicConfig", "config"]
