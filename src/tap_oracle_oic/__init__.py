"""Professional Singer tap for Oracle Integration Cloud (OIC) data extraction."""

from __future__ import annotations

from tap_oracle_oic.__version__ import __version__
from tap_oracle_oic.tap import TapOIC

__all__ = ["TapOIC", "__version__"]
