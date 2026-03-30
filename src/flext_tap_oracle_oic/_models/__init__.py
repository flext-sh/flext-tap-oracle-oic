# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Models subpackage for flext-tap-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tap_oracle_oic._models import streams as streams
    from flext_tap_oracle_oic._models.streams import (
        ALL_STREAMS as ALL_STREAMS,
        CORE_STREAMS as CORE_STREAMS,
        EXTENDED_STREAMS as EXTENDED_STREAMS,
        INFRASTRUCTURE_STREAMS as INFRASTRUCTURE_STREAMS,
        MONITORING_STREAMS as MONITORING_STREAMS,
        FlextTapOracleOicModelsStreams as FlextTapOracleOicModelsStreams,
        th as th,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "ALL_STREAMS": ["flext_tap_oracle_oic._models.streams", "ALL_STREAMS"],
    "CORE_STREAMS": ["flext_tap_oracle_oic._models.streams", "CORE_STREAMS"],
    "EXTENDED_STREAMS": ["flext_tap_oracle_oic._models.streams", "EXTENDED_STREAMS"],
    "FlextTapOracleOicModelsStreams": [
        "flext_tap_oracle_oic._models.streams",
        "FlextTapOracleOicModelsStreams",
    ],
    "INFRASTRUCTURE_STREAMS": [
        "flext_tap_oracle_oic._models.streams",
        "INFRASTRUCTURE_STREAMS",
    ],
    "MONITORING_STREAMS": [
        "flext_tap_oracle_oic._models.streams",
        "MONITORING_STREAMS",
    ],
    "streams": ["flext_tap_oracle_oic._models.streams", ""],
    "th": ["flext_tap_oracle_oic._models.streams", "th"],
}

_EXPORTS: Sequence[str] = [
    "ALL_STREAMS",
    "CORE_STREAMS",
    "EXTENDED_STREAMS",
    "FlextTapOracleOicModelsStreams",
    "INFRASTRUCTURE_STREAMS",
    "MONITORING_STREAMS",
    "streams",
    "th",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
