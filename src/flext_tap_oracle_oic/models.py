"""Oracle Integration Cloud Models using standardized [Project]Models pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Iterator, Mapping
from typing import Annotated, ClassVar

from flext_meltano import FlextMeltanoModels
from flext_oracle_oic import FlextOracleOicModels

from flext_tap_oracle_oic import c, e, p, t, u
from flext_tap_oracle_oic._models._activity import (
    FlextTapOracleOicActivityRecord,
    FlextTapOracleOicActivityRecord as _OicActivityRecord,
)
from flext_tap_oracle_oic._models._agent import (
    FlextTapOracleOicAgentEntity,
    FlextTapOracleOicAgentEntity as _OicAgentEntity,
)
from flext_tap_oracle_oic._models._api_response import (
    FlextTapOracleOicApiResponse,
    FlextTapOracleOicApiResponse as _OicApiResponse,
)
from flext_tap_oracle_oic._models._auth_config import (
    FlextTapOracleOicAuthenticationConfig,
    FlextTapOracleOicAuthenticationConfig as _OicAuthenticationConfig,
)
from flext_tap_oracle_oic._models._connection import (
    FlextTapOracleOicConnectionEntity,
    FlextTapOracleOicConnectionEntity as _OicConnectionEntity,
)
from flext_tap_oracle_oic._models._envelope import (
    FlextTapOracleOicEnvelope,
    FlextTapOracleOicEnvelope as _OicEnvelope,
)
from flext_tap_oracle_oic._models._error_context import (
    FlextTapOracleOicErrorContext,
    FlextTapOracleOicErrorContext as _OicErrorContext,
)
from flext_tap_oracle_oic._models._helpers import FlextTapOracleOicModelsHelpers
from flext_tap_oracle_oic._models._integration import (
    FlextTapOracleOicIntegrationEntity,
    FlextTapOracleOicIntegrationEntity as _OicIntegrationEntity,
)
from flext_tap_oracle_oic._models._metrics import (
    FlextTapOracleOicMetricsRecord,
    FlextTapOracleOicMetricsRecord as _OicMetricsRecord,
)
from flext_tap_oracle_oic._models._oic_connection import (
    FlextTapOracleOicConnection,
    FlextTapOracleOicConnection as _FlextTapOracleOicConnection,
)
from flext_tap_oracle_oic._models._oic_execution_summary import (
    FlextTapOracleOicExecutionSummary,
    FlextTapOracleOicExecutionSummary as _FlextTapOracleOicExecutionSummary,
)
from flext_tap_oracle_oic._models._oic_integration import (
    FlextTapOracleOicIntegration,
    FlextTapOracleOicIntegration as _FlextTapOracleOicIntegration,
)
from flext_tap_oracle_oic._models._oic_lookup import (
    FlextTapOracleOicLookup,
    FlextTapOracleOicLookup as _FlextTapOracleOicLookup,
)
from flext_tap_oracle_oic._models._oic_monitoring import (
    FlextTapOracleOicMonitoringRecord,
    FlextTapOracleOicMonitoringRecord as _FlextTapOracleOicMonitoringRecord,
)
from flext_tap_oracle_oic._models._oic_project import (
    FlextTapOracleOicProject,
    FlextTapOracleOicProject as _FlextTapOracleOicProject,
)
from flext_tap_oracle_oic._models._oic_resource_metadata import (
    FlextTapOracleOicResourceMetadata,
    FlextTapOracleOicResourceMetadata as _FlextTapOracleOicResourceMetadata,
)
from flext_tap_oracle_oic._models._package import (
    FlextTapOracleOicPackageEntity,
    FlextTapOracleOicPackageEntity as _OicPackageEntity,
)
from flext_tap_oracle_oic._models._stream_config import (
    FlextTapOracleOicStreamConfiguration,
    FlextTapOracleOicStreamConfiguration as _OicStreamConfiguration,
)
from flext_tap_oracle_oic._models.streams import FlextTapOracleOicModelsStreams
from flext_tap_oracle_oic._models.stream_base import FlextTapOracleOicStreamBase
from flext_tap_oracle_oic.tap_streams import FlextTapOracleOicPaginator as _OicPaginator


class FlextTapOracleOicModels(FlextMeltanoModels, FlextOracleOicModels):
    """Oracle Integration Cloud tap models extending flext-core m.

    Provides complete models for OIC entity extraction, authentication,
    monitoring, and Singer protocol compliance following standardized patterns.
    """

    class TapOracleOic(
        FlextTapOracleOicActivityRecord,
        FlextTapOracleOicAgentEntity,
        FlextTapOracleOicApiResponse,
        FlextTapOracleOicAuthenticationConfig,
        FlextTapOracleOicConnectionEntity,
        FlextTapOracleOicEnvelope,
        FlextTapOracleOicErrorContext,
        FlextTapOracleOicModelsHelpers,
        FlextTapOracleOicIntegrationEntity,
        FlextTapOracleOicMetricsRecord,
        FlextTapOracleOicConnection,
        FlextTapOracleOicExecutionSummary,
        FlextTapOracleOicIntegration,
        FlextTapOracleOicLookup,
        FlextTapOracleOicMonitoringRecord,
        FlextTapOracleOicProject,
        FlextTapOracleOicResourceMetadata,
        FlextTapOracleOicPackageEntity,
        FlextTapOracleOicStreamConfiguration,
        FlextTapOracleOicModelsStreams,
    ):
        """TapOracleOic domain namespace."""

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
            FlextTapOracleOicModels.TapOracleOic.require_entity_value(
                entity_id,
                label=id_label,
            )
            FlextTapOracleOicModels.TapOracleOic.require_entity_value(
                entity_name,
                label=name_label,
            )
            FlextTapOracleOicModels.TapOracleOic.validate_optional_port(port)

        OicEnvelope = _OicEnvelope

        OICBaseStream = FlextTapOracleOicStreamBase
        OicAuthenticationConfig = _OicAuthenticationConfig

        OicIntegrationEntity = _OicIntegrationEntity

        OicConnectionEntity = _OicConnectionEntity

        OicActivityRecord = _OicActivityRecord

        OicPackageEntity = _OicPackageEntity

        OicMetricsRecord = _OicMetricsRecord

        OicAgentEntity = _OicAgentEntity

        OicStreamConfiguration = _OicStreamConfiguration

        OicApiResponse = _OicApiResponse

        OicErrorContext = _OicErrorContext

        class OracleOic(FlextOracleOicModels.OracleOic):
            """Domain entity models for Oracle OIC resources.

            Canonical home for OIC entity classes, migrated from domain/entities.py
            per MRO policy: all m subclasses live under [Project]Models.
            """

            FlextTapOracleOicConnection = _FlextTapOracleOicConnection

            FlextTapOracleOicIntegration = _FlextTapOracleOicIntegration

            FlextTapOracleOicLookup = _FlextTapOracleOicLookup

            FlextTapOracleOicMonitoringRecord = _FlextTapOracleOicMonitoringRecord

            FlextTapOracleOicProject = _FlextTapOracleOicProject

            FlextTapOracleOicResourceMetadata = _FlextTapOracleOicResourceMetadata

            FlextTapOracleOicExecutionSummary = _FlextTapOracleOicExecutionSummary


# Short alias
m = FlextTapOracleOicModels

__all__: list[str] = ["FlextTapOracleOicModels", "m"]
