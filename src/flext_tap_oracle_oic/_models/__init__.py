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
    from flext_tap_oracle_oic._models import streams
    from flext_tap_oracle_oic._models.streams import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "ALL_STREAMS": "flext_tap_oracle_oic._models.streams",
    "CORE_STREAMS": "flext_tap_oracle_oic._models.streams",
    "EXTENDED_STREAMS": "flext_tap_oracle_oic._models.streams",
    "FlextTapOracleOicModelsStreams": "flext_tap_oracle_oic._models.streams",
    "INFRASTRUCTURE_STREAMS": "flext_tap_oracle_oic._models.streams",
    "MONITORING_STREAMS": "flext_tap_oracle_oic._models.streams",
    "streams": "flext_tap_oracle_oic._models.streams",
    "th": "flext_tap_oracle_oic._models.streams",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, sorted(_LAZY_IMPORTS))
