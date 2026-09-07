"""Typed public fixtures for flext-tap-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

from flext_tap_oracle_oic import FlextTapOracleOic, m, t


@pytest.fixture
def tap_oracle_oic() -> FlextTapOracleOic:
    """Return the real public tap with its typed defaults."""
    return FlextTapOracleOic(validate_config=False)


@pytest.fixture
def tap_instance(tap_oracle_oic: FlextTapOracleOic) -> m.Meltano.TapInstance:
    """Build the public Meltano request from the tap's typed settings."""
    connection_config = t.json_mapping_adapter().validate_python(
        tap_oracle_oic.oic_settings.TapOracleOic.model_dump(mode="json")
    )
    config = m.Meltano.TapConfig(
        tap_type=tap_oracle_oic.name,
        connection_config=connection_config,
        stream_config={},
    )
    return m.Meltano.TapInstance.model_validate({
        "tap_type": tap_oracle_oic.name,
        "config": config,
    })
