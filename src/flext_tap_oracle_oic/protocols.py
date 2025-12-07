"""Singer Oracle OIC tap protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_db_oracle.protocols import FlextDbOracleProtocols as p_db_oracle
from flext_meltano.protocols import FlextMeltanoProtocols as p_meltano


class FlextMeltanoTapOracleOicProtocols(p_meltano, p_db_oracle):
    """Singer Tap Oracle OIC protocols extending Oracle and Meltano protocols.

    Extends both FlextDbOracleProtocols and FlextMeltanoProtocols via multiple inheritance
    to inherit all Oracle protocols, Meltano protocols, and foundation protocols.

    Architecture:
    - EXTENDS: FlextDbOracleProtocols (inherits .Database.* protocols)
    - EXTENDS: FlextMeltanoProtocols (inherits .Meltano.* protocols)
    - ADDS: Tap Oracle OIC-specific protocols in TapOracleOic namespace
    - PROVIDES: Root-level alias `p` for convenient access
    """

    class TapOracleOic:
        """Singer Tap Oracle OIC domain protocols."""

        @runtime_checkable
        class OicConnectionProtocol(p_db_oracle.Service[object], Protocol):
            """Protocol for Oracle OIC connection."""

            def connect(self, config: dict[str, object]) -> p_meltano.Result[object]:
                """Connect to Oracle OIC with provided configuration."""
                ...

        @runtime_checkable
        class IntegrationDiscoveryProtocol(p_db_oracle.Service[object], Protocol):
            """Protocol for OIC integration discovery."""

            def discover_integrations(
                self,
                config: dict[str, object],
            ) -> p_meltano.Result[list[dict[str, object]]]:
                """Discover available integrations in Oracle OIC."""
                ...

        @runtime_checkable
        class DataExtractionProtocol(p_db_oracle.Service[object], Protocol):
            """Protocol for OIC data extraction."""

            def extract_integration_data(
                self,
                integration: str,
            ) -> p_meltano.Result[list[dict[str, object]]]:
                """Extract data from an Oracle OIC integration."""
                ...

        @runtime_checkable
        class StreamGenerationProtocol(p_db_oracle.Service[object], Protocol):
            """Protocol for Singer stream generation."""

            def generate_catalog(
                self,
                config: dict[str, object],
            ) -> p_meltano.Result[dict[str, object]]:
                """Generate Singer catalog for OIC entities."""
                ...

        @runtime_checkable
        class MonitoringProtocol(p_db_oracle.Service[object], Protocol):
            """Protocol for OIC extraction monitoring."""

            def track_progress(
                self,
                integration: str,
                records: int,
            ) -> p_meltano.Result[bool]:
                """Track OIC integration data extraction progress."""
                ...


# Runtime alias for simplified usage
p = FlextMeltanoTapOracleOicProtocols

__all__ = [
    "FlextMeltanoTapOracleOicProtocols",
    "p",
]
