# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Tap Oracle Oic. Protocols package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_oracle_oic._protocols.base import FlextTapOracleOicProtocolsBase


__all__: tuple[str, ...] = ("FlextTapOracleOicProtocolsBase",)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({"FlextTapOracleOicProtocolsBase": ".base"}),
    public_exports=__all__,
)
