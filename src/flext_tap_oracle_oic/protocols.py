"""Singer Oracle OIC tap protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextResult, p


class FlextMeltanoTapOracleOicProtocols:
    """Singer Tap Oracle OIC protocols with explicit re-exports from p foundation.

    Domain Extension Pattern (Phase 3):
    - Explicit re-export of foundation protocols (not inheritance)
    - Domain-specific protocols organized in TapOracleOic namespace
    - 100% backward compatibility through aliases
    """

    class TapOracleOic:
        """Singer Tap Oracle OIC domain protocols."""

        @runtime_checkable
        class OicConnectionProtocol(p.Service, Protocol):
            """Protocol for Oracle OIC connection."""

            def connect(self, config: dict[str, object]) -> FlextResult[object]:
                """Connect to Oracle OIC with provided configuration."""

        @runtime_checkable
        class IntegrationDiscoveryProtocol(p.Service, Protocol):
            """Protocol for OIC integration discovery."""

            def discover_integrations(
                self,
                config: dict[str, object],
            ) -> FlextResult[list[dict[str, object]]]:
                """Discover available integrations in Oracle OIC."""

        @runtime_checkable
        class DataExtractionProtocol(p.Service, Protocol):
            """Protocol for OIC data extraction."""

            def extract_integration_data(
                self,
                integration: str,
            ) -> FlextResult[list[dict[str, object]]]:
                """Extract data from an Oracle OIC integration."""

        @runtime_checkable
        class StreamGenerationProtocol(p.Service, Protocol):
            """Protocol for Singer stream generation."""

            def generate_catalog(
                self,
                config: dict[str, object],
            ) -> FlextResult[dict[str, object]]:
                """Generate Singer catalog for OIC entities."""

        @runtime_checkable
        class MonitoringProtocol(p.Service, Protocol):
            """Protocol for OIC extraction monitoring."""

            def track_progress(
                self,
                integration: str,
                records: int,
            ) -> FlextResult[None]:
                """Track OIC integration data extraction progress."""

    @runtime_checkable
    class OicConnectionProtocol(TapOracleOic.OicConnectionProtocol):
        """OicConnectionProtocol - real inheritance."""

    @runtime_checkable
    class IntegrationDiscoveryProtocol(TapOracleOic.IntegrationDiscoveryProtocol):
        """IntegrationDiscoveryProtocol - real inheritance."""

    @runtime_checkable
    class DataExtractionProtocol(TapOracleOic.DataExtractionProtocol):
        """DataExtractionProtocol - real inheritance."""

    @runtime_checkable
    class StreamGenerationProtocol(TapOracleOic.StreamGenerationProtocol):
        """StreamGenerationProtocol - real inheritance."""

    @runtime_checkable
    class MonitoringProtocol(TapOracleOic.MonitoringProtocol):
        """MonitoringProtocol - real inheritance."""

    @runtime_checkable
    class TapOracleOicConnectionProtocol(TapOracleOic.OicConnectionProtocol):
        """TapOracleOicConnectionProtocol - real inheritance."""

    @runtime_checkable
    class TapOracleOicIntegrationDiscoveryProtocol(
        TapOracleOic.IntegrationDiscoveryProtocol,
    ):
        """TapOracleOicIntegrationDiscoveryProtocol - real inheritance."""

    @runtime_checkable
    class TapOracleOicDataExtractionProtocol(TapOracleOic.DataExtractionProtocol):
        """TapOracleOicDataExtractionProtocol - real inheritance."""

    @runtime_checkable
    class TapOracleOicStreamGenerationProtocol(TapOracleOic.StreamGenerationProtocol):
        """TapOracleOicStreamGenerationProtocol - real inheritance."""

    @runtime_checkable
    class TapOracleOicMonitoringProtocol(TapOracleOic.MonitoringProtocol):
        """TapOracleOicMonitoringProtocol - real inheritance."""


__all__ = [
    "FlextMeltanoTapOracleOicProtocols",
]
