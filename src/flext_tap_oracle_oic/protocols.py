"""Singer Oracle OIC tap protocols for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Protocol, runtime_checkable

from flext_api import FlextApiModels

from flext_meltano import FlextMeltanoModels, FlextMeltanoProtocols
from flext_oracle_oic import FlextOracleOicProtocols
from flext_tap_oracle_oic import t


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
    from flext_tap_oracle_oic import p

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
                FlextOracleOicProtocols.Service[t.ContainerValueMapping],
                Protocol,
            ):
                """Protocol for Oracle OIC connection."""

                def connect(
                    self,
                    settings: Mapping[str, t.ContainerValueMapping],
                ) -> FlextMeltanoProtocols.Result[t.ContainerValueMapping]:
                    """Connect to Oracle OIC with provided configuration."""
                    ...

            @runtime_checkable
            class IntegrationDiscovery(
                FlextOracleOicProtocols.Service[t.ContainerValueMapping],
                Protocol,
            ):
                """Protocol for OIC integration discovery."""

                def discover_integrations(
                    self,
                    settings: Mapping[str, t.ContainerValueMapping],
                ) -> FlextMeltanoProtocols.Result[Sequence[t.ContainerValueMapping]]:
                    """Discover available integrations in Oracle OIC."""
                    ...

            @runtime_checkable
            class DataExtraction(
                FlextOracleOicProtocols.Service[t.ContainerValueMapping],
                Protocol,
            ):
                """Protocol for OIC data extraction."""

                def extract_integration_data(
                    self,
                    integration: str,
                ) -> FlextMeltanoProtocols.Result[Sequence[t.ContainerValueMapping]]:
                    """Extract data from an Oracle OIC integration."""
                    ...

            @runtime_checkable
            class StreamGeneration(
                FlextOracleOicProtocols.Service[t.ContainerValueMapping],
                Protocol,
            ):
                """Protocol for Singer stream generation."""

                def generate_catalog(
                    self,
                    settings: Mapping[str, t.ContainerValueMapping],
                ) -> FlextMeltanoProtocols.Result[
                    FlextMeltanoModels.Meltano.SingerCatalog
                ]:
                    """Generate Singer catalog for OIC entities."""
                    ...

            @runtime_checkable
            class Monitoring(
                FlextOracleOicProtocols.Service[t.ContainerValueMapping],
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

            @runtime_checkable
            class Paginator(Protocol):
                """Structural paginator contract used by stream models."""

                current_value: int

                def get_next(
                    self,
                    response: FlextApiModels.Api.HttpResponse,
                ) -> int | None:
                    """Return the next pagination token for a response."""
                    ...

            @runtime_checkable
            class PaginatorFactory(Protocol):
                """Factory contract for paginator class objects."""

                def __call__(
                    self,
                    start_value: int = 0,
                    page_size: int = 100,
                ) -> FlextTapOracleOicProtocols.TapOracleOic.TapOracleOicPrivate.Paginator:
                    """Build a paginator instance."""
                    ...

            @runtime_checkable
            class PropertiesListLike(Protocol):
                """Structural protocol for singer PropertiesList-compatible objects."""

                def to_dict(self) -> t.ContainerValueMapping:
                    """Convert properties list to dictionary representation."""
                    ...


p = FlextTapOracleOicProtocols
__all__: list[str] = ["FlextTapOracleOicProtocols", "p"]
