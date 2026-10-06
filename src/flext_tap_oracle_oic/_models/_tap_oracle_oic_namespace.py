from __future__ import annotations

from flext_tap_oracle_oic import m


class _TapOracleOicNamespace(m.BaseModel):
    """Open, frozen namespace exposing every ``config/*.yaml`` domain model-less."""

    model_config = m.ConfigDict(extra="allow", frozen=True)
