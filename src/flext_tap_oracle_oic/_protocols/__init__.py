# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Oracle Oic. Protocols package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_oracle_oic._protocols.base import FlextTapOracleOicProtocolsBase
    from flext_tap_oracle_oic._protocols.envelope import (
        FlextTapOracleOicProtocolsEnvelope,
    )
    from flext_tap_oracle_oic._protocols.generated_models_taporacleoic import (
        FlextTapOracleOicProtocolsGeneratedModelsTapOracleOic,
    )
    from flext_tap_oracle_oic._protocols.streams import (
        FlextTapOracleOicProtocolsStreams,
    )


__all__: tuple[str, ...] = (
    "FlextTapOracleOicProtocolsBase",
    "FlextTapOracleOicProtocolsEnvelope",
    "FlextTapOracleOicProtocolsGeneratedModelsTapOracleOic",
    "FlextTapOracleOicProtocolsStreams",
)

install_lazy_exports(
    __name__,
    globals(),
    {
        "FlextTapOracleOicProtocolsBase": ".base",
        "FlextTapOracleOicProtocolsEnvelope": ".envelope",
        "FlextTapOracleOicProtocolsGeneratedModelsTapOracleOic": (
            ".generated_models_taporacleoic"
        ),
        "FlextTapOracleOicProtocolsStreams": ".streams",
    },
    public_exports=__all__,
)
