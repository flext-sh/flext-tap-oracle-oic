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
    from flext_tap_oracle_oic._models import streams
    from flext_tap_oracle_oic._models.streams import (
        ALL_STREAMS,
        FlextTapOracleOicModelsStreams,
        th,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "ALL_STREAMS": "flext_tap_oracle_oic._models.streams",
    "FlextTapOracleOicModelsStreams": "flext_tap_oracle_oic._models.streams",
    "streams": "flext_tap_oracle_oic._models.streams",
    "th": "flext_tap_oracle_oic._models.streams",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
