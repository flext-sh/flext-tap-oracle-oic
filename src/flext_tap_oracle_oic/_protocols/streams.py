# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_tap_oracle_oic/_protocols/streams
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols

from flext_tap_oracle_oic import t


class FlextTapOracleOicProtocolsStreams:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class IntegrationsStream(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def settings(self) -> t.JsonMapping:
            """Runtime stream settings passed by the tap."""
            ...

        name: str
        replication_key: str | None
        stream_schema: t.JsonMapping
        path: str

    @runtime_checkable
    class ConnectionsStream(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def settings(self) -> t.JsonMapping:
            """Runtime stream settings passed by the tap."""
            ...

        name: str
        replication_key: str | None
        stream_schema: t.JsonMapping
        path: str

    @runtime_checkable
    class PackagesStream(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def settings(self) -> t.JsonMapping:
            """Runtime stream settings passed by the tap."""
            ...

        name: str
        replication_key: str | None
        stream_schema: t.JsonMapping
        path: str

    @runtime_checkable
    class LookupsStream(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def settings(self) -> t.JsonMapping:
            """Runtime stream settings passed by the tap."""
            ...

        name: str
        replication_key: str | None
        stream_schema: t.JsonMapping
        path: str

    @runtime_checkable
    class LibrariesStream(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def settings(self) -> t.JsonMapping:
            """Runtime stream settings passed by the tap."""
            ...

        name: str
        replication_key: str | None
        stream_schema: t.JsonMapping
        path: str

    @runtime_checkable
    class CertificatesStream(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def settings(self) -> t.JsonMapping:
            """Runtime stream settings passed by the tap."""
            ...

        name: str
        replication_key: str | None
        stream_schema: t.JsonMapping
        path: str

    @runtime_checkable
    class AdaptersStream(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def settings(self) -> t.JsonMapping:
            """Runtime stream settings passed by the tap."""
            ...

        name: str
        replication_key: str | None
        stream_schema: t.JsonMapping
        path: str

    @runtime_checkable
    class ProjectsStream(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def settings(self) -> t.JsonMapping:
            """Runtime stream settings passed by the tap."""
            ...

        name: str
        replication_key: str | None
        stream_schema: t.JsonMapping
        path: str

    @runtime_checkable
    class ExecutionsStream(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def settings(self) -> t.JsonMapping:
            """Runtime stream settings passed by the tap."""
            ...

        name: str
        replication_key: str | None
        stream_schema: t.JsonMapping
        path: str

    @runtime_checkable
    class MetricsStream(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def settings(self) -> t.JsonMapping:
            """Runtime stream settings passed by the tap."""
            ...

        name: str
        replication_key: str | None
        stream_schema: t.JsonMapping
        path: str


__all__: list[str] = [
    "FlextTapOracleOicProtocolsStreams",
]
