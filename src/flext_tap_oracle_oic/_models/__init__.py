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
    from flext_tap_oracle_oic._models.base import FlextTapOracleOicModelsBase
    from flext_tap_oracle_oic._models.envelope import FlextTapOracleOicModelsEnvelope
    from flext_tap_oracle_oic._models.streams import FlextTapOracleOicModelsStreams


__all__: tuple[str, ...] = (
    "FlextTapOracleOicModelsBase",
    "FlextTapOracleOicModelsEnvelope",
    "FlextTapOracleOicModelsStreams",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextTapOracleOicModelsBase": ".base",
        "FlextTapOracleOicModelsEnvelope": ".envelope",
        "FlextTapOracleOicModelsStreams": ".streams",
    }),
    public_exports=__all__,
)
