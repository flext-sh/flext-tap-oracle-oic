"""Oracle Integration Cloud paginator.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import (
    Sequence,
)

from flext_api import FlextApiModels

from flext_tap_oracle_oic import c, m, t, u

_as_oic_envelope = m.as_oic_envelope
_as_value_list = m.as_value_list


class FlextTapOracleOicPaginator:
    """Oracle OIC API paginator with adaptive page sizing."""

    def __init__(
        self,
        start_value: int = c.TapOracleOic.TapOicProcessing.DEFAULT_PAGINATOR_START,
        page_size: int = c.TapOracleOic.TapOicProcessing.DEFAULT_PAGINATOR_PAGE_SIZE,
    ) -> None:
        """Initialize paginator with starting offset and page size."""
        self.current_value: int = start_value
        self._page_size: int = page_size
        self._max_page_size: int = (
            c.TapOracleOic.TapOicProcessing.PAGINATOR_MAX_PAGE_SIZE
        )
        self._min_page_size: int = (
            c.TapOracleOic.TapOicProcessing.PAGINATOR_MIN_PAGE_SIZE
        )
        self._adaptive_sizing: bool = True
        self._response_times: list[float] = []

    def get_next(self, response: FlextApiModels.Api.HttpResponse) -> int | None:
        """Calculate next offset for Oracle OIC pagination."""
        try:
            data = self._normalize_response_payload(response)
            return self._calculate_next_offset(data)
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            logger = u.fetch_logger(__name__)
            err_msg = f"OIC pagination parsing failed: {type(e).__name__}: {e}"
            logger.warning(err_msg)
            logger.info("Returning None - pagination parsing failure properly handled")
            logger.debug("This indicates end of pagination or malformed OIC response")
            return None

    def _normalize_response_payload(
        self,
        response: FlextApiModels.Api.HttpResponse,
    ) -> t.ContainerValueMapping:
        """Normalize flext-api response bodies to OIC pagination payloads."""
        match response.body:
            case dict() as body_map:
                return body_map
            case _:
                msg = "Pagination requires a JSON object response body"
                raise TypeError(msg)

    def _calculate_next_offset(
        self,
        data: t.ContainerValueMapping,
    ) -> int | None:
        """Calculate next offset based on OIC response format."""
        items = self._extract_items_from_response(data)
        if items is None or not items or len(items) < self._page_size:
            return None
        return self.current_value + len(items)

    def _extract_items_from_response(
        self,
        data: t.ContainerValueMapping,
    ) -> Sequence[t.ContainerValueMapping] | None:
        """Extract items from various OIC response formats."""
        list_payload = _as_value_list(data)
        if list_payload is not None:
            return [item for item in list_payload if isinstance(item, dict)]
        envelope = _as_oic_envelope(data)
        if envelope is None:
            return None
        if envelope.items is not None:
            return envelope.items
        if envelope.data is not None:
            return envelope.data
        return None

    def _track_response_time(self, response_time: float) -> None:
        """Track response times for adaptive page sizing."""
        self._response_times.append(response_time)
        if (
            len(self._response_times)
            > c.TapOracleOic.TapOicPerformance.RESPONSE_TIME_HISTORY_SIZE
        ):
            self._response_times.pop(0)
        if (
            len(self._response_times)
            >= c.TapOracleOic.TapOicPerformance.MIN_RESPONSE_SAMPLES
        ):
            avg_time = sum(self._response_times) / len(self._response_times)
            if (
                avg_time > c.TapOracleOic.TapOicPerformance.SLOW_RESPONSE_THRESHOLD
                and self._page_size > self._min_page_size
            ):
                self._page_size = max(self._min_page_size, int(self._page_size * 0.8))
            elif avg_time < 1.0 and self._page_size < self._max_page_size:
                self._page_size = min(self._max_page_size, int(self._page_size * 1.2))


__all__: list[str] = ["FlextTapOracleOicPaginator"]
