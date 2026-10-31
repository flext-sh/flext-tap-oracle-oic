# AUTO-GENERATED FILE — Regenerate with: make gen
"""FLEXT Oracle OIC TAP Constants extending flext-core platform constants.

FLEXT Oracle OIC TAP specific constants that extend flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_meltano import c as flext_meltano_c
from flext_oracle_oic import c as flext_oracle_oic_c

from flext_tap_oracle_oic._constants import (
    FlextTapOracleOicConstantsBase,
    FlextTapOracleOicConstantsEnums,
    FlextTapOracleOicConstantsValues,
)


class FlextTapOracleOicConstants(flext_meltano_c, flext_oracle_oic_c):
    """FLEXT Oracle OIC TAP constants extending flext-core platform constants.

    Composes with FlextOracleOicConstants to avoid duplication and ensure consistency.
    Scalar constants inherit from ``FlextTapOracleOicConstantsValues`` (the
    ``_constants`` SSOT); this class declares only the domain enums.

    """

    class TapOracleOic(
        FlextTapOracleOicConstantsBase,
        FlextTapOracleOicConstantsEnums,
        FlextTapOracleOicConstantsValues.TapOracleOic,
    ):
        """OIC connection configuration and domain enumerations."""


c = FlextTapOracleOicConstants
__all__: list[str] = ["FlextTapOracleOicConstants", "c"]
