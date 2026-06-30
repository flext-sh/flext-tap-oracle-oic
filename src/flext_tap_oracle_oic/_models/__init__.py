# AUTO-GENERATED FILE — Regenerate with: make gen
"""Models package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_oracle_oic._models.streams import (
        ALL_STREAMS as ALL_STREAMS,
        FlextTapOracleOicModelsStreams as FlextTapOracleOicModelsStreams,
        th as th,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".streams": (
            "ALL_STREAMS",
            "FlextTapOracleOicModelsStreams",
            "th",
        ),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
