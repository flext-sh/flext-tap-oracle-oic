"""Python module execution entry point for FLEXT Tap Oracle OIC.

Enables execution via `python -m flext_tap_oracle_oic` with full Singer SDK
CLI support and flext-meltano FlextMeltanoSingerCliTranslator compatibility.

This module provides the main command-line interface for the Oracle Integration
Cloud Singer tap with complete Singer protocol compliance and orchestration
integration through flext-meltano.

Usage:
    python -m flext_tap_oracle_oic --config config.json --discover
    python -m flext_tap_oracle_oic --config config.json --catalog catalog.json
    python -m flext_tap_oracle_oic --config config.json --catalog catalog.json --state state.json

Architecture:
    - Standard Singer TAP protocol (--discover, --catalog, --state)
    - Singer SDK CLI integration for full protocol compliance
    - flext-meltano FlextMeltanoSingerCliTranslator compatibility for orchestration

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tap_oracle_oic.cli import main

if __name__ == "__main__":
    main()
