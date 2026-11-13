"""Oracle OIC record fetcher for the declarative Singer tap.

The tap exposes the Singer CLI through ``FlextMeltanoDeclarativeTap``; this
service owns the consumer-side record retrieval that the declarative runtime
delegates to a ``p.Meltano.RecordFetcher``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tap_oracle_oic import (
    FlextTapOracleOic,
    FlextTapOracleOicPaginator,
    c,
    m,
    p,
    r,
    t,
)


class FlextTapOracleOicExtractService:
    """Fetch one OIC stream's records through the authenticated API client."""

    @staticmethod
    def fetch(
        request: p.Meltano.FetchRequest,
    ) -> p.Result[p.Meltano.FetchResult]:
        """Fetch every record of ``request.stream_name`` by paginating OIC.

        Args:
            request: Fetch request naming the stream and carrying the flat
                Singer configuration parsed by the declarative tap CLI.

        Returns:
            Result succeeding with the stream records, or failing with the
            first authentication, transport, or response failure.

        """
        tap = FlextTapOracleOic(settings=request.config, validate_config=False)
        stream = next(
            (
                candidate
                for candidate in tap.discover_oic_streams()
                if candidate.name == request.stream_name
            ),
            None,
        )
        if stream is None:
            return r[p.Meltano.FetchResult].fail(
                f"Unknown stream: {request.stream_name}",
            )
        paginator = FlextTapOracleOicPaginator(
            page_size=c.TapOracleOic.DEFAULT_PAGE_SIZE,
        )
        records: list[t.JsonMapping] = []
        while True:
            response = tap.client.get(
                f"{stream.path}?limit={paginator.page_size}"
                f"&offset={paginator.current_value}",
            )
            if response.failure:
                return r[p.Meltano.FetchResult].from_failure(response)
            records.extend(paginator.items(response.value))
            next_offset = paginator.fetch_next(response.value)
            if next_offset is None:
                return r[p.Meltano.FetchResult].ok(
                    m.Meltano.FetchResult(records=tuple(records)),
                )
            paginator.current_value = next_offset


__all__: list[str] = ["FlextTapOracleOicExtractService"]
