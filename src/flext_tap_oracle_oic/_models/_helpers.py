"""Shared validation helpers for TapOracleOic entity models.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tap_oracle_oic import c


class FlextTapOracleOicModelsHelpers:
    """Canonical namespace owner."""

    @staticmethod
    def require_entity_value(value: str, *, label: str) -> None:
        """Require one non-empty entity identifier/name value.

        Raises:
            ValueError: If ``not value``.
        """
        if not value:
            msg = f"{label} is required"
            raise ValueError(msg)

    @staticmethod
    def validate_optional_port(port: int | None) -> None:
        """Validate optional network port within canonical bounds.

        Raises:
            ValueError: If Port must be between 1 and 65535.
        """
        if port is not None and not (
            c.DEFAULT_RETRY_DELAY_SECONDS <= port <= c.MAX_PORT
        ):
            msg = "Port must be between 1 and 65535"
            raise ValueError(msg)

    @staticmethod
    def validate_entity_identity_and_port(
        *,
        entity_id: str,
        entity_name: str,
        id_label: str,
        name_label: str,
        port: int | None,
    ) -> None:
        """Validate required entity id/name fields and optional port."""
        FlextTapOracleOicModelsHelpers.require_entity_value(entity_id, label=id_label)
        FlextTapOracleOicModelsHelpers.require_entity_value(
            entity_name, label=name_label
        )
        FlextTapOracleOicModelsHelpers.validate_optional_port(port)


__all__: list[str] = ["FlextTapOracleOicModelsHelpers"]
