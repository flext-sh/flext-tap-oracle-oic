# AUTO-GENERATED FILE — Regenerate with: make gen
"""Oracle Integration Cloud Models using standardized [Project]Models pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_meltano import FlextMeltanoModels
from flext_oracle_oic import FlextOracleOicModels

from flext_tap_oracle_oic._models import (
    FlextTapOracleOicEnvelope,
    FlextTapOracleOicModelsBase,
    FlextTapOracleOicModelsStreams,
    FlextTapOracleOicStreamBase,
)


class FlextTapOracleOicModels(FlextMeltanoModels, FlextOracleOicModels):
    """Oracle Integration Cloud tap models extending flext-core m.

    Provides the OIC stream namespace, envelope, and stream base composed from
    the ``_models`` family; the OIC domain entities live in ``flext-oracle-oic``
    (ADR-006 thin driver), so the tap does not duplicate them.

    """

    class TapOracleOic(
        FlextTapOracleOicModelsBase,
        FlextTapOracleOicModelsStreams,
        FlextTapOracleOicEnvelope,
        FlextTapOracleOicStreamBase,
    ):
        """TapOracleOic domain namespace."""


# Short alias
m = FlextTapOracleOicModels

__all__: list[str] = ["FlextTapOracleOicModels", "m"]
