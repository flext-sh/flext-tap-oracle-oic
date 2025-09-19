"""Entry point for Oracle Integration Cloud Singer Tap.

This module provides the main command-line interface for the tap-oic Singer tap.
It can be executed as a module using:
          python -m tap_oic

Architecture:
    Improved CLI with 100% Singer SDK compatibility and organized subcommands
- Default: Standard Singer TAP protocol (--discover, --catalog, etc.)
- Extended: Well-organized subcommands (extract, lifecycle, monitor, admin)


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tap_oracle_oic.tap_client import TapOracleOIC


def main() -> None:
    """Provide entry point for Oracle OIC tap."""
    TapOracleOIC.cli()


if __name__ == "__main__":
    main()
