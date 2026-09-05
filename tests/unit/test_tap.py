"""Observable behavior of the public Oracle OIC tap facade.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_tap_oracle_oic import FlextTapOracleOicSettings, c
from flext_tests import tm
from tests import u

if TYPE_CHECKING:
    from flext_tap_oracle_oic import FlextTapOracleOic, m


class TestsFlextTapOracleOic:
    """Public tap construction and Singer discovery contracts."""

    def test_default_tap_exposes_typed_public_settings(
        self,
        tap_oracle_oic: FlextTapOracleOic,
        tap_instance: m.Meltano.TapInstance,
    ) -> None:
        """The public facade exposes typed settings and its request identity."""
        tm.that(tap_oracle_oic.oic_settings, is_=FlextTapOracleOicSettings)
        tm.that(tap_instance.tap_type, eq=tap_oracle_oic.name)

    def test_discovery_returns_the_canonical_public_stream_catalog(
        self,
        tap_oracle_oic: FlextTapOracleOic,
        tap_instance: m.Meltano.TapInstance,
    ) -> None:
        """Discovery returns exactly the streams owned by the public constants."""
        names = u.TapOracleOic.Tests.discover_stream_names(
            tap_oracle_oic, tap_instance
        )

        tm.that(names, eq=tuple(c.TapOracleOic.CORE_STREAMS))
