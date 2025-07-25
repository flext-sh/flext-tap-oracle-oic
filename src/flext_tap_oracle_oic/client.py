"""Oracle Integration Cloud client - REFACTORED to eliminate code duplication.

Uses ExtendedOICClient from flext-oracle-oic-ext library instead of reimplementing.
This eliminates 372 lines of duplicated OIC client functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import get_logger
from flext_oracle_oic_ext import ExtendedOICClient

logger = get_logger(__name__)

# Alias for backward compatibility - uses library implementation
OracleOICClient = ExtendedOICClient

__all__ = ["OracleOICClient"]
