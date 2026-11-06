# AUTO-GENERATED FILE — Regenerate with: make gen
"""Singer Oracle OIC tap protocols for FLEXT ecosystem.

Only ``TapOracleOic.Paginator`` (consumed by ``models.py``) remains; every
other inner protocol lost its last consumer and was deleted (STRICT YAGNI).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_meltano import p as flext_meltano_p
from flext_oracle_oic import p as flext_oracle_oic_p

from flext_tap_oracle_oic._protocols import (
    FlextTapOracleOicProtocolsBase,
    FlextTapOracleOicProtocolsEnvelope,
    FlextTapOracleOicProtocolsGeneratedModelsTapOracleOic,
    FlextTapOracleOicProtocolsStreams,
)


class FlextTapOracleOicProtocols(
    flext_meltano_p,
    flext_oracle_oic_p,
    FlextTapOracleOicProtocolsBase,
    FlextTapOracleOicProtocolsEnvelope,
    FlextTapOracleOicProtocolsGeneratedModelsTapOracleOic,
    FlextTapOracleOicProtocolsStreams,
):
    """Singer Oracle OIC tap protocols facade — composes Meltano + OracleOic."""

    class TapOracleOic(
        FlextTapOracleOicProtocolsGeneratedModelsTapOracleOic.TapOracleOic,
        FlextTapOracleOicProtocolsBase,
        FlextTapOracleOicProtocolsEnvelope,
        FlextTapOracleOicProtocolsStreams,
    ):
        """Singer Tap Oracle OIC structural protocols (consumer surface)."""


p = FlextTapOracleOicProtocols
__all__: list[str] = ["FlextTapOracleOicProtocols", "p"]
