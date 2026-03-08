"""FLEXT Tap Oracle OIC Configuration - Enhanced FlextSettings Implementation.

Single unified configuration class for Oracle Integration Cloud Singer tap
operations following FLEXT 1.0.0 patterns with enhanced singleton, SecretStr,
and Pydantic 2.11+ features.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import FlextConstants, FlextResult

from flext_tap_oracle_oic.typings import t


def create_oracle_oic_tap_config(
    oauth_params: Mapping[str, t.ContainerValue],
    connection_params: Mapping[str, t.ContainerValue],
    tap_params: Mapping[str, t.ContainerValue] | None = None,
) -> FlextResult[FlextTapOracleOicSettings]:
    """Create Oracle Integration Cloud tap configuration using grouped parameters.

    Args:
        oauth_params: OAuth2/IDCS authentication parameters
        connection_params: OIC connection parameters
        tap_params: Optional tap-specific parameters

    Returns:
        FlextResult containing validated Oracle OIC tap configuration

    """
    try:
        tap_config: dict[str, t.ContainerValue] = (
            dict(tap_params) if tap_params is not None else {}
        )
        tap_config.setdefault(
            "batch_size", FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE
        )
        tap_config.setdefault("stream_prefix", "oic")
        config_data = {**oauth_params, **connection_params, **tap_config}
        config_instance = FlextTapOracleOicSettings.model_validate(config_data)
        return FlextResult[FlextTapOracleOicSettings].ok(config_instance)
    except (ValueError, TypeError, KeyError, AttributeError, OSError) as e:
        return FlextResult[FlextTapOracleOicSettings].fail(
            f"Oracle OIC tap configuration creation failed: {e}"
        )


def validate_oracle_oic_tap_configuration(
    config: FlextTapOracleOicSettings,
) -> FlextResult[bool]:
    """Validate Oracle Integration Cloud tap configuration using FlextSettings patterns - ZERO DUPLICATION."""
    required_fields = [
        (config.oauth_client_id, "OAuth client ID is required"),
        (
            config.oauth_client_secret.get_secret_value(),
            "OAuth client secret is required",
        ),
        (config.oauth_audience, "OAuth audience is required"),
    ]
    for field_value, error_message in required_fields:
        if not (field_value and str(field_value).strip()):
            return FlextResult[bool].fail(error_message)
    if config.timeout <= 0:
        return FlextResult[bool].fail("Timeout must be positive")
    if config.max_retries < 0:
        return FlextResult[bool].fail("Max retries cannot be negative")
    if config.page_size <= 0:
        return FlextResult[bool].fail("Page size must be positive")
    return FlextResult[bool].ok(value=True)


__all__: list[str] = [
    "FlextTapOracleOicSettings",
    "create_oracle_oic_tap_config",
    "validate_oracle_oic_tap_configuration",
]
