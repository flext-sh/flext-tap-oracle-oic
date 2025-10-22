"""Singer Oracle OIC tap protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextProtocols, FlextResult


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

            def connect(self, config: dict[str, object]) -> FlextResult[object]:
                """Connect to Oracle OIC with provided configuration."""

        @runtime_checkable
        class IntegrationDiscoveryProtocol(FlextProtocols.Service, Protocol):
            """Protocol for OIC integration discovery."""

            def discover_integrations(
                self, config: dict[str, object]
            ) -> FlextResult[list[dict[str, object]]]:
                """Discover available integrations in Oracle OIC."""

        @runtime_checkable
        class DataExtractionProtocol(FlextProtocols.Service, Protocol):
            """Protocol for OIC data extraction."""

            def extract_integration_data(
                self, integration: str
            ) -> FlextResult[list[dict[str, object]]]:
                """Extract data from an Oracle OIC integration."""

        @runtime_checkable
        class StreamGenerationProtocol(FlextProtocols.Service, Protocol):
            """Protocol for Singer stream generation."""

            def generate_catalog(
                self, config: dict[str, object]
            ) -> FlextResult[dict[str, object]]:
                """Generate Singer catalog for OIC entities."""

        @runtime_checkable
        class MonitoringProtocol(FlextProtocols.Service, Protocol):
            """Protocol for OIC extraction monitoring."""

            def track_progress(
                self, integration: str, records: int
            ) -> FlextResult[None]:
                """Track OIC integration data extraction progress."""

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
