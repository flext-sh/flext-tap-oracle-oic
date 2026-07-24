"""FlextTapOracleOicConfig — frozen, validated config singleton for flext-tap-oracle-oic.

Every ``config/*.yaml`` file is auto-discovered and deep-merged at first
``fetch_global`` call (model-less, ``extra="allow"`` at the FlextMeltanoConfig base).
The flat YAML is then validated into the pure-Pydantic ``_models.config``
shapes and exposed as typed domain objects under ``config.TapOracleOic`` — never a
model-less dict subscript.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from functools import cached_property
from pathlib import Path
from typing import ClassVar

from flext_meltano import FlextMeltanoConfig
from flext_tap_oracle_oic._models.config import FlextTapOracleOicConfigModels


class FlextTapOracleOicConfig(FlextMeltanoConfig):
    """TapOracleOic config auto-loaded from ``config/*.yaml`` and validated via models."""

    CONFIG_DIR: ClassVar[str] = str(Path(__file__).resolve().parents[2] / "config")

    @cached_property
    def TapOracleOic(self) -> FlextTapOracleOicConfigModels.TapOracleOic:
        """Validated ``TapOracleOic`` business-rule config namespace."""
        root = FlextTapOracleOicConfigModels.Root.model_validate(
            dict(self.model_extra or {})
        )
        return root.TapOracleOic


config: FlextTapOracleOicConfig = FlextTapOracleOicConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_tap_oracle_oic import config``."""

__all__: list[str] = ["FlextTapOracleOicConfig", "config"]
