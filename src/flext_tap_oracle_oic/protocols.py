"""Singer Oracle OIC tap protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextProtocols, FlextResult, FlextTypes


class FlextMeltanoTapOracleOicProtocols:
    """Singer Tap Oracle OIC protocols with explicit re-exports from FlextProtocols foundation.

    Domain Extension Pattern (Phase 3):
    - Explicit re-export of foundation protocols (not inheritance)
    - Domain-specific protocols organized in TapOracleOic namespace
    - 100% backward compatibility through aliases
    """

    class TapOracleOic:
        """Singer Tap Oracle OIC domain protocols."""

        @runtime_checkable
        class OicConnectionProtocol(FlextProtocols.Service, Protocol):
            """Protocol for Oracle OIC connection."""

            def connect(self, config: FlextTypes.Dict) -> FlextResult[object]: ...

        @runtime_checkable
        class IntegrationDiscoveryProtocol(FlextProtocols.Service, Protocol):
            """Protocol for OIC integration discovery."""

            def discover_integrations(
                self, config: FlextTypes.Dict
            ) -> FlextResult[list[FlextTypes.Dict]]: ...

        @runtime_checkable
        class DataExtractionProtocol(FlextProtocols.Service, Protocol):
            """Protocol for OIC data extraction."""

            def extract_integration_data(
                self, integration: str
            ) -> FlextResult[list[FlextTypes.Dict]]: ...

        @runtime_checkable
        class StreamGenerationProtocol(FlextProtocols.Service, Protocol):
            """Protocol for Singer stream generation."""

            def generate_catalog(
                self, config: FlextTypes.Dict
            ) -> FlextResult[FlextTypes.Dict]: ...

        @runtime_checkable
        class MonitoringProtocol(FlextProtocols.Service, Protocol):
            """Protocol for OIC extraction monitoring."""

            def track_progress(
                self, integration: str, records: int
            ) -> FlextResult[None]: ...

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
