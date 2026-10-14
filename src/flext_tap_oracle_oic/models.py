"""Oracle Integration Cloud Models using standardized [Project]Models pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_meltano import FlextMeltanoModels
from flext_oracle_oic import FlextOracleOicModels

from flext_tap_oracle_oic._models._envelope import FlextTapOracleOicEnvelope
from flext_tap_oracle_oic._models.base import FlextTapOracleOicModelsBase
from flext_tap_oracle_oic._models.stream_base import FlextTapOracleOicStreamBase
from flext_tap_oracle_oic._models.streams import FlextTapOracleOicModelsStreams


class FlextTapOracleOicModels(FlextMeltanoModels, FlextOracleOicModels):
    """Oracle Integration Cloud tap models extending flext-core m.

    Provides the OIC stream namespace, envelope, and stream base composed from
    the ``_models`` family; the OIC domain entities live in ``flext-oracle-oic``
    (ADR-006 thin driver), so the tap does not duplicate them.

    """

    class TapOracleOic(
        FlextTapOracleOicEnvelope,
        FlextTapOracleOicModelsBase,
        FlextTapOracleOicStreamBase,
        FlextTapOracleOicModelsStreams,
    ):
        """TapOracleOic domain namespace."""


# Short alias
m = FlextTapOracleOicModels

__all__: list[str] = ["FlextTapOracleOicModels", "m"]
