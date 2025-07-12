"""Professional Singer tap for Oracle Integration Cloud (OIC) data extraction.

Copyright (c) 2025 FLEXT Team. All rights reserved.
"""

from __future__ import annotations

from flext_tap_oracle_oic.__version__ import __version__
from flext_tap_oracle_oic.tap import TapOIC

__all__ = ["TapOIC", "__version__"]
