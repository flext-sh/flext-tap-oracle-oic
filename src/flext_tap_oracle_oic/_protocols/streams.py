# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_tap_oracle_oic/_protocols/streams
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_tap_oracle_oic._protocols import FlextTapOracleOicProtocolsBase


class FlextTapOracleOicProtocolsStreams:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class IntegrationsStream(FlextTapOracleOicProtocolsBase.StreamBase, Protocol):
        """Structural data contract projected from the owning model."""

        path: str

    @runtime_checkable
    class ConnectionsStream(FlextTapOracleOicProtocolsBase.StreamBase, Protocol):
        """Structural data contract projected from the owning model."""

        path: str

    @runtime_checkable
    class PackagesStream(FlextTapOracleOicProtocolsBase.StreamBase, Protocol):
        """Structural data contract projected from the owning model."""

        path: str

    @runtime_checkable
    class LookupsStream(FlextTapOracleOicProtocolsBase.StreamBase, Protocol):
        """Structural data contract projected from the owning model."""

        path: str

    @runtime_checkable
    class LibrariesStream(FlextTapOracleOicProtocolsBase.StreamBase, Protocol):
        """Structural data contract projected from the owning model."""

        path: str

    @runtime_checkable
    class CertificatesStream(FlextTapOracleOicProtocolsBase.StreamBase, Protocol):
        """Structural data contract projected from the owning model."""

        path: str

    @runtime_checkable
    class AdaptersStream(FlextTapOracleOicProtocolsBase.StreamBase, Protocol):
        """Structural data contract projected from the owning model."""

        path: str

    @runtime_checkable
    class ProjectsStream(FlextTapOracleOicProtocolsBase.StreamBase, Protocol):
        """Structural data contract projected from the owning model."""

        path: str

    @runtime_checkable
    class ExecutionsStream(FlextTapOracleOicProtocolsBase.StreamBase, Protocol):
        """Structural data contract projected from the owning model."""

        path: str

    @runtime_checkable
    class MetricsStream(FlextTapOracleOicProtocolsBase.StreamBase, Protocol):
        """Structural data contract projected from the owning model."""

        path: str


__all__: list[str] = [
    "FlextTapOracleOicProtocolsStreams",
]
