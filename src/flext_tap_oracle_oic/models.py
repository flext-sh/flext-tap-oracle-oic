"""Oracle Integration Cloud Models using standardized [Project]Models pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import ClassVar

from flext_meltano import FlextMeltanoModels
from flext_oracle_oic import FlextOracleOicModels

from flext_tap_oracle_oic._models import (
    FlextTapOracleOicActivityRecord,
    FlextTapOracleOicAgentEntity,
    FlextTapOracleOicApiResponse,
    FlextTapOracleOicAuthenticationConfig,
    FlextTapOracleOicConnection,
    FlextTapOracleOicConnectionEntity,
    FlextTapOracleOicEnvelope,
    FlextTapOracleOicErrorContext,
    FlextTapOracleOicExecutionSummary,
    FlextTapOracleOicIntegration,
    FlextTapOracleOicIntegrationEntity,
    FlextTapOracleOicLookup,
    FlextTapOracleOicMetricsRecord,
    FlextTapOracleOicModelsBase,
    FlextTapOracleOicModelsHelpers,
    FlextTapOracleOicModelsStreams,
    FlextTapOracleOicMonitoringRecord,
    FlextTapOracleOicPackageEntity,
    FlextTapOracleOicProject,
    FlextTapOracleOicResourceMetadata,
    FlextTapOracleOicStreamBase,
    FlextTapOracleOicStreamConfiguration,
)


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
        FlextTapOracleOicModelsBase,
        FlextTapOracleOicStreamBase,
        FlextTapOracleOicModelsStreams,
    ):
        """TapOracleOic domain namespace.

        A pure namespace: the collaborator classes are exposed as ``ClassVar``
        references (the ``m.TapOracleOic.*`` consumer surface) and validation
        helpers are inherited from ``FlextTapOracleOicModelsHelpers``; the class
        deliberately does not multiply-inherit the entity models it references.
        """

        OicEnvelope: ClassVar[type] = FlextTapOracleOicEnvelope

        OICBaseStream: ClassVar[type] = FlextTapOracleOicStreamBase
        OicAuthenticationConfig: ClassVar[type] = FlextTapOracleOicAuthenticationConfig

        OicIntegrationEntity: ClassVar[type] = FlextTapOracleOicIntegrationEntity

        OicConnectionEntity: ClassVar[type] = FlextTapOracleOicConnectionEntity

        OicActivityRecord: ClassVar[type] = FlextTapOracleOicActivityRecord

        OicPackageEntity: ClassVar[type] = FlextTapOracleOicPackageEntity

        OicMetricsRecord: ClassVar[type] = FlextTapOracleOicMetricsRecord

        OicAgentEntity: ClassVar[type] = FlextTapOracleOicAgentEntity

        OicStreamConfiguration: ClassVar[type] = FlextTapOracleOicStreamConfiguration

        OicApiResponse: ClassVar[type] = FlextTapOracleOicApiResponse

        OicErrorContext: ClassVar[type] = FlextTapOracleOicErrorContext

        class OracleOic(FlextOracleOicModels.OracleOic):
            """Domain entity models for Oracle OIC resources.

            Canonical home for OIC entity classes, migrated from domain/entities.py
            per MRO policy: all m subclasses live under [Project]Models.
            """

            FlextTapOracleOicConnection: ClassVar[type] = FlextTapOracleOicConnection

            FlextTapOracleOicIntegration: ClassVar[type] = FlextTapOracleOicIntegration

            FlextTapOracleOicLookup: ClassVar[type] = FlextTapOracleOicLookup

            FlextTapOracleOicMonitoringRecord: ClassVar[type] = (
                FlextTapOracleOicMonitoringRecord
            )

            FlextTapOracleOicProject: ClassVar[type] = FlextTapOracleOicProject

            FlextTapOracleOicResourceMetadata: ClassVar[type] = (
                FlextTapOracleOicResourceMetadata
            )

            FlextTapOracleOicExecutionSummary: ClassVar[type] = (
                FlextTapOracleOicExecutionSummary
            )


# Short alias
m = FlextTapOracleOicModels

__all__: list[str] = ["FlextTapOracleOicModels", "m"]
