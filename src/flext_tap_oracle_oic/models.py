"""Compatibility facade: re-export tap_models via models.py.

Standardizes imports to use flext_tap_oracle_oic.models across the codebase.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tap_oracle_oic.tap_models import OICIntegration

__all__ = [
    "OICIntegration",
]
