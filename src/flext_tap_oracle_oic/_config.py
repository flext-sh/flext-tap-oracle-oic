"""FlextTapOracleOicConfig — frozen config singleton for flext-tap-oracle-oic.

See ADR-005 §7.

Model-less: business rules live in ``config/*.yaml`` under the ``TapOracleOic:`` key and
are exposed through the open ``config.TapOracleOic`` namespace (``extra="allow"``), with
no per-domain model. Access is ``config.TapOracleOic.<domain>[<key>...]``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated

from flext_meltano import FlextMeltanoConfig, m

from flext_tap_oracle_oic._models.base import FlextTapOracleOicModelsBase


class FlextTapOracleOicConfig(FlextMeltanoConfig):
    """TapOracleOic config auto-loaded model-less from ``config/*.yaml``.

    MRO carries ``FlextSettings`` FIRST (ENFORCE-042); the class stays a frozen,
    YAML-validated config singleton.

    """

    TapOracleOic: Annotated[
        FlextTapOracleOicModelsBase.ConfigNamespace,
        m.Field(
            description=(
                "Open namespace exposing ``config/*.yaml`` under ``TapOracleOic``."
            ),
        ),
    ] = FlextTapOracleOicModelsBase.ConfigNamespace()


config: FlextTapOracleOicConfig = FlextTapOracleOicConfig.fetch_global()
"""Pre-instantiated frozen config singleton.

Exposed as ``from flext_tap_oracle_oic import config``.
"""

__all__: list[str] = ["FlextTapOracleOicConfig", "config"]
