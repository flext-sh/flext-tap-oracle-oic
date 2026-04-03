# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Models package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import flext_tap_oracle_oic._models.streams as _flext_tap_oracle_oic__models_streams

    streams = _flext_tap_oracle_oic__models_streams

    _ = (
        ALL_STREAMS,
        FlextTapOracleOicModelsStreams,
        streams,
        th,
    )
_LAZY_IMPORTS = {
    "ALL_STREAMS": "flext_tap_oracle_oic._models.streams",
    "FlextTapOracleOicModelsStreams": "flext_tap_oracle_oic._models.streams",
    "streams": "flext_tap_oracle_oic._models.streams",
    "th": "flext_tap_oracle_oic._models.streams",
}

__all__ = [
    "ALL_STREAMS",
    "FlextTapOracleOicModelsStreams",
    "streams",
    "th",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
