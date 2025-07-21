"""Professional Singer tap for Oracle Integration Cloud (OIC) data extraction.

Copyright (c) 2025 FLEXT Team. All rights reserved.
"""

from __future__ import annotations

import importlib.metadata

try:
    __version__ = importlib.metadata.version("flext-tap-oracle-oic")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0-dev"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())
from flext_tap_oracle_oic.tap import TapOIC

__all__ = ["TapOIC", "__version__", "__version_info__"]
