"""Singer Oracle OIC tap protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextCore


class FlextMeltanoTapOracleOicProtocols:
    """Singer Tap Oracle OIC protocols with explicit re-exports from FlextCore.Protocols foundation.

    Domain Extension Pattern (Phase 3):
    - Explicit re-export of foundation protocols (not inheritance)
    - Domain-specific protocols organized in TapOracleOic namespace
    - 100% backward compatibility through aliases
    """

    Foundation = FlextCore.Protocols.Foundation
    Domain = FlextCore.Protocols.Domain
    Application = FlextCore.Protocols.Application
    Infrastructure = FlextCore.Protocols.Infrastructure
    Extensions = FlextCore.Protocols.Extensions
    Commands = FlextCore.Protocols.Commands

    class TapOracleOic:
        """Singer Tap Oracle OIC domain protocols."""

        @runtime_checkable
        class OicConnectionProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for Oracle OIC connection."""

            def connect(
                self, config: FlextCore.Types.Dict
            ) -> FlextCore.Result[object]: ...

        @runtime_checkable
        class IntegrationDiscoveryProtocol(
            FlextCore.Protocols.Domain.Service, Protocol
        ):
            """Protocol for OIC integration discovery."""

            def discover_integrations(
                self, config: FlextCore.Types.Dict
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]: ...

        @runtime_checkable
        class DataExtractionProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for OIC data extraction."""

            def extract_integration_data(
                self, integration: str
            ) -> FlextCore.Result[list[FlextCore.Types.Dict]]: ...

        @runtime_checkable
        class StreamGenerationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for Singer stream generation."""

            def generate_catalog(
                self, config: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]: ...

        @runtime_checkable
        class MonitoringProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for OIC extraction monitoring."""

            def track_progress(
                self, integration: str, records: int
            ) -> FlextCore.Result[None]: ...

    OicConnectionProtocol = TapOracleOic.OicConnectionProtocol
    IntegrationDiscoveryProtocol = TapOracleOic.IntegrationDiscoveryProtocol
    DataExtractionProtocol = TapOracleOic.DataExtractionProtocol
    StreamGenerationProtocol = TapOracleOic.StreamGenerationProtocol
    MonitoringProtocol = TapOracleOic.MonitoringProtocol

    TapOracleOicConnectionProtocol = TapOracleOic.OicConnectionProtocol
    TapOracleOicIntegrationDiscoveryProtocol = TapOracleOic.IntegrationDiscoveryProtocol
    TapOracleOicDataExtractionProtocol = TapOracleOic.DataExtractionProtocol
    TapOracleOicStreamGenerationProtocol = TapOracleOic.StreamGenerationProtocol
    TapOracleOicMonitoringProtocol = TapOracleOic.MonitoringProtocol


__all__ = [
    "FlextMeltanoTapOracleOicProtocols",
]
