"""FLEXT service orchestrator for tap-oracle-oic.

from flext_tap_oracle_oic import u
Thin facade — all infrastructure from ``FlextMeltanoTapServiceBase`` via MRO.
The tap uses FlextMeltanoAbstractions (CLI dispatch), not singer_sdk.Tap.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, Never, override

from flext_meltano.services.consumer_bases.tap_service_base import (
    FlextMeltanoTapServiceBase,
)
from flext_tap_oracle_oic import p, t, u


class FlextTapOracleOicService(FlextMeltanoTapServiceBase):
    """Orchestrator for tap-oracle-oic. CLI dispatch, not Singer SDK."""

    tap_name: Annotated[
        t.NonEmptyStr,
        u.Field(description="Canonical Singer tap identifier."),
    ] = "tap-oracle-oic"

    @override
    def create_tap_instance(
        self,
        settings: p.Settings | t.JsonMapping | None = None,
    ) -> Never:
        """Not supported — use FlextTapOracleOic directly."""
        msg = "tap-oracle-oic uses CLI dispatch, not singer_sdk.Tap"
        raise TypeError(msg)


tap_oracle_oic = FlextTapOracleOicService

__all__: list[str] = ["FlextTapOracleOicService", "tap_oracle_oic"]
