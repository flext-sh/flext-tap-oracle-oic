"""Compatibility facade: re-export tap_models via models.py.

Standardizes imports to use flext_tap_oracle_oic.models across the codebase.
"""

from __future__ import annotations

from .tap_models import *  # noqa: F401,F403
