# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Oracle Oic. Models package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_oracle_oic._models._envelope import FlextTapOracleOicEnvelope
    from flext_tap_oracle_oic._models.base import FlextTapOracleOicModelsBase
    from flext_tap_oracle_oic._models.stream_base import FlextTapOracleOicStreamBase
    from flext_tap_oracle_oic._models.streams import FlextTapOracleOicModelsStreams


__all__: tuple[str, ...] = (
    "FlextTapOracleOicEnvelope",
    "FlextTapOracleOicModelsBase",
    "FlextTapOracleOicModelsStreams",
    "FlextTapOracleOicStreamBase",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextTapOracleOicEnvelope": "._envelope",
        "FlextTapOracleOicModelsBase": ".base",
        "FlextTapOracleOicModelsStreams": ".streams",
        "FlextTapOracleOicStreamBase": ".stream_base",
    }),
    public_exports=__all__,
)
