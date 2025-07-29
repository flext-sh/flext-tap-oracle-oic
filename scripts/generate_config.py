#!/usr/bin/env python3
"""Generate config.json from .env file for tap-oracle-oic.

This script uses the centralized FLEXT configuration generator to eliminate
code duplication and ensure consistent configuration patterns across all
Oracle OIC projects.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Add flext-core to path for configuration generator
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "flext-core" / "src"))

# 🚨 ARCHITECTURAL COMPLIANCE: Using DI container
from flext_tap_oracle_oic.infrastructure.di_container import (
    get_base_config,
    get_domain_entity,
    get_domain_value_object,
    get_field,
    get_service_result,
)

FlextResult = get_service_result()
DomainEntity = get_domain_entity()
Field = get_field()
FlextValueObject = get_domain_value_object()
BaseConfig = get_base_config()


def main() -> None:
    """Generate config.json file for tap-oracle-oic."""
    try:
        # Generate configuration using centralized generator
        config = generate_project_config(
            project_type=ProjectType.TAP_ORACLE_OIC,
            config_path="config.json",
            overwrite=False,
        )

        print("✅ Successfully generated tap-oracle-oic configuration")
        print("📄 Configuration saved to: config.json")
        print(f"🔧 Configuration includes: {', '.join(config.keys())}")

    except (RuntimeError, ValueError, TypeError) as e:
        print(f"❌ Error generating configuration: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
