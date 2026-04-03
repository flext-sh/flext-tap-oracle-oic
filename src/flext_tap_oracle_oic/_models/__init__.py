# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Models package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_tap_oracle_oic import streams
    from flext_tap_oracle_oic.streams import FlextTapOracleOicModelsStreams, th

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextTapOracleOicModelsStreams": "flext_tap_oracle_oic.streams",
    "streams": "flext_tap_oracle_oic.streams",
    "th": "flext_tap_oracle_oic.streams",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
