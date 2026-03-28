# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Models subpackage for flext-tap-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes

    from flext_tap_oracle_oic._models.streams import (
        ALL_STREAMS,
        CORE_STREAMS,
        EXTENDED_STREAMS,
        INFRASTRUCTURE_STREAMS,
        MONITORING_STREAMS,
        FlextTapOracleOicModelsStreams,
        th,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "ALL_STREAMS": ["flext_tap_oracle_oic._models.streams", "ALL_STREAMS"],
    "CORE_STREAMS": ["flext_tap_oracle_oic._models.streams", "CORE_STREAMS"],
    "EXTENDED_STREAMS": ["flext_tap_oracle_oic._models.streams", "EXTENDED_STREAMS"],
    "FlextTapOracleOicModelsStreams": ["flext_tap_oracle_oic._models.streams", "FlextTapOracleOicModelsStreams"],
    "INFRASTRUCTURE_STREAMS": ["flext_tap_oracle_oic._models.streams", "INFRASTRUCTURE_STREAMS"],
    "MONITORING_STREAMS": ["flext_tap_oracle_oic._models.streams", "MONITORING_STREAMS"],
    "th": ["flext_tap_oracle_oic._models.streams", "th"],
}

__all__ = [
    "ALL_STREAMS",
    "CORE_STREAMS",
    "EXTENDED_STREAMS",
    "INFRASTRUCTURE_STREAMS",
    "MONITORING_STREAMS",
    "FlextTapOracleOicModelsStreams",
    "th",
]


_LAZY_CACHE: MutableMapping[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> Sequence[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
