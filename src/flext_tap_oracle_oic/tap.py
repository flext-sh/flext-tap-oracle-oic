"""Re-export shim — canonical implementation lives in _utilities.tap."""

from __future__ import annotations

from flext_tap_oracle_oic._utilities.tap import (
    FlextOracleOicAuthenticator,
    FlextTapOracleOic,
    FlextTapOracleOicClient,
    logger,
    main,
)

__all__ = [
    "FlextOracleOicAuthenticator",
    "FlextTapOracleOic",
    "FlextTapOracleOicClient",
    "logger",
    "main",
]
