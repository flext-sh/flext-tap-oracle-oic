"""FLEXT service orchestrator for tap-oracle-oic.

Thin facade — all infrastructure from ``FlextMeltanoTapServiceBase`` via MRO.
The Singer CLI runs through ``FlextMeltanoDeclarativeTap``: the canonical
stream registry declares the catalog and ``FlextTapOracleOicExtractService``
fetches records from the authenticated OIC client.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Annotated, override

from flext_meltano import FlextMeltanoTapServiceBase

from flext_tap_oracle_oic import (
    FlextTapOracleOic,
    FlextTapOracleOicExtractService,
    m,
    p,
    t,
)


class FlextTapOracleOicService(FlextMeltanoTapServiceBase):
    """Orchestrator for tap-oracle-oic over the declarative Singer contract."""

    tap_name: Annotated[
        t.NonEmptyStr,
        m.Field(description="Canonical Singer tap identifier."),
    ] = "tap-oracle-oic"

    @override
    def create_tap_instance(
        self,
        _settings: p.Settings | t.JsonMapping | None = None,
    ) -> p.Meltano.SingerTapInstance:
        """Build the declarative Singer tap from the canonical stream registry.

        Args:
            _settings: Unused; the Singer CLI parses ``--config`` after the
                instance exists, so the catalog is built config-free.

        Returns:
            The resulting ``p.Meltano.SingerTapInstance``.

        """
        tap = FlextTapOracleOic(validate_config=False)
        spec = m.Meltano.TapSpec(
            tap_name=self.tap_name,
            config_jsonschema=tap.config_jsonschema,
            streams=tuple(
                m.Meltano.StreamSpec(
                    name=stream.name,
                    json_schema=stream.stream_schema,
                    primary_keys=tuple(stream.primary_keys),
                    replication_key=stream.replication_key,
                )
                for stream in tap.discover_oic_streams()
            ),
        )
        return self.build_declarative_tap(
            spec,
            FlextTapOracleOicExtractService(),
        )


tap_oracle_oic: FlextTapOracleOicService = FlextTapOracleOicService.fetch_global()
"""Shared ``FlextTapOracleOicService`` instance for the Oracle OIC tap."""

__all__: list[str] = ["FlextTapOracleOicService", "tap_oracle_oic"]
