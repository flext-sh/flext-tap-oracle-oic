"""Singer Oracle OIC tap protocols for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Protocol, runtime_checkable

from flext_core import t
from flext_meltano import FlextMeltanoModels, FlextMeltanoProtocols
from flext_oracle_oic.protocols import FlextOracleOicProtocols


class FlextTapOracleOicProtocols(FlextMeltanoProtocols, FlextOracleOicProtocols):
    """Singer Tap Oracle OIC protocols extending Oracle and Meltano protocols.

    Extends both FlextOracleOicProtocols and FlextMeltanoProtocols via multiple inheritance
    to inherit all Oracle OIC protocols, Meltano protocols, and foundation protocols.

    Architecture:
    - EXTENDS: FlextOracleOicProtocols (inherits .OracleOic.* protocols)
    - EXTENDS: FlextMeltanoProtocols (inherits .Meltano.* protocols)
    - ADDS: Tap Oracle OIC-specific protocols in Tap.OracleOic namespace
    - PROVIDES: Root-level alias `p` for convenient access

    Usage:
    from flext_tap_oracle_oic.protocols import p

    # Foundation protocols (inherited)
    result: p.Result[str]
    service: p.Service[str]

    # Oracle protocols (inherited)
    connection: p.OracleOic.Connection

    # Meltano protocols (inherited)
    tap: p.Meltano.Tap

    # Tap Oracle OIC-specific protocols
    oic_connection: p.Tap.OracleOic.OicConnection
    """

    class TapOracleOic:
        """Singer Tap domain protocols."""

        class OracleOic:
            """Singer Tap Oracle OIC domain protocols."""

            @runtime_checkable
            class OicConnection(
                FlextOracleOicProtocols.Service[Mapping[str, t.ContainerValue]],
                Protocol,
            ):
                """Protocol for Oracle OIC connection."""

                def connect(
                    self,
                    config: Mapping[str, Mapping[str, t.ContainerValue]],
                ) -> FlextMeltanoProtocols.Result[Mapping[str, t.ContainerValue]]:
                    """Connect to Oracle OIC with provided configuration."""
                    ...

            @runtime_checkable
            class IntegrationDiscovery(
                FlextOracleOicProtocols.Service[Mapping[str, t.ContainerValue]],
                Protocol,
            ):
                """Protocol for OIC integration discovery."""

                def discover_integrations(
                    self,
                    config: Mapping[str, Mapping[str, t.ContainerValue]],
                ) -> FlextMeltanoProtocols.Result[
                    Sequence[Mapping[str, t.ContainerValue]]
                ]:
                    """Discover available integrations in Oracle OIC."""
                    ...

            @runtime_checkable
            class DataExtraction(
                FlextOracleOicProtocols.Service[Mapping[str, t.ContainerValue]],
                Protocol,
            ):
                """Protocol for OIC data extraction."""

                def extract_integration_data(
                    self,
                    integration: str,
                ) -> FlextMeltanoProtocols.Result[
                    Sequence[Mapping[str, t.ContainerValue]]
                ]:
                    """Extract data from an Oracle OIC integration."""
                    ...

            @runtime_checkable
            class StreamGeneration(
                FlextOracleOicProtocols.Service[Mapping[str, t.ContainerValue]],
                Protocol,
            ):
                """Protocol for Singer stream generation."""

                def generate_catalog(
                    self,
                    config: Mapping[str, Mapping[str, t.ContainerValue]],
                ) -> FlextMeltanoProtocols.Result[
                    FlextMeltanoModels.Meltano.SingerCatalog
                ]:
                    """Generate Singer catalog for OIC entities."""
                    ...

            @runtime_checkable
            class Monitoring(
                FlextOracleOicProtocols.Service[Mapping[str, t.ContainerValue]],
                Protocol,
            ):
                """Protocol for OIC extraction monitoring."""

                def track_progress(
                    self,
                    integration: str,
                    records: int,
                ) -> FlextMeltanoProtocols.Result[bool]:
                    """Track OIC integration data extraction progress."""
                    ...


class TapOracleOicPrivate:
    """Private structural protocols for internal flext-tap-oracle-oic use."""

    class PropertiesListLike(Protocol):
        """Structural protocol for singer PropertiesList-compatible objects."""

        def to_dict(self) -> Mapping[str, t.ContainerValue]:
            """Convert properties list to dictionary representation."""
            ...


p = FlextTapOracleOicProtocols
__all__ = ["FlextTapOracleOicProtocols", "TapOracleOicPrivate", "p"]
