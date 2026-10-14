"""Oracle Integration Cloud paginator.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_tap_oracle_oic import c, t
from flext_tap_oracle_oic._models import FlextTapOracleOicEnvelope

if TYPE_CHECKING:
    from flext_api import FlextApiModels


class FlextTapOracleOicPaginator:
    """Oracle OIC paginator with Singer's raw-token return contract.

    Empty collections terminate pagination. Invalid collection values raise
    their validation error; they never represent a successfully exhausted page.
    
    """

    def __init__(
        self,
        start_value: int = c.TapOracleOic.DEFAULT_PAGINATOR_START,
        page_size: int = c.TapOracleOic.DEFAULT_PAGINATOR_PAGE_SIZE,
    ) -> None:
        """Initialize the paginator with starting offset and page size.

        Args:
            start_value: Initial replication offset.
            page_size: Initial number of records requested per page; later
                adapted to observed response times within configured bounds.

        
        """
        self.current_value: int = start_value
        self._page_size: int = page_size
        self._max_page_size: int = c.TapOracleOic.PAGINATOR_MAX_PAGE_SIZE
        self._min_page_size: int = c.TapOracleOic.PAGINATOR_MIN_PAGE_SIZE
        self._adaptive_sizing: bool = True
        self._response_times: list[float] = []

    def fetch_next(self, response: FlextApiModels.Api.HttpResponse) -> int | None:
        """Return the raw Singer page token for one response.

        Args:
            response: HTTP response of the page just fetched.

        Returns:
            Next offset when the page is full, or ``None`` when the
            collection is exhausted; malformed payloads raise.

        
        """
        data = self._normalize_response_payload(response)
        return self._calculate_next_offset(data)

    @staticmethod
    def _normalize_response_payload(
        response: FlextApiModels.Api.HttpResponse,
    ) -> t.JsonMapping:
        """Normalize flext-api response bodies to OIC pagination payloads.

        Args:
            response: HTTP response whose body is normalized.

        Returns:
            The JSON object payload of the response body.

        Raises:
            TypeError: If Pagination requires a JSON object response body.

        
        """
        match response.body:
            case dict() as body_map:
                return body_map
            case _:
                msg = "Pagination requires a JSON object response body"
                raise TypeError(msg)

    def _calculate_next_offset(self, data: t.JsonMapping) -> int | None:
        """Calculate the next offset based on the OIC response format.

        Args:
            data: Normalized JSON payload of the response.

        Returns:
            Next offset when the page holds a full page of items, or
            ``None`` when pagination is exhausted.

        
        """
        items = self._extract_items_from_response(data)
        if items is None or not items or len(items) < self._page_size:
            return None
        return self.current_value + len(items)

    @staticmethod
    def _extract_items_from_response(
        data: t.JsonMapping,
    ) -> t.SequenceOf[t.JsonMapping] | None:
        """Extract items from the supported OIC response formats.

        Args:
            data: Normalized JSON payload of the response.

        Returns:
            Item mappings from the ``items`` or ``data`` envelope field, or
            ``None`` when neither is present.

        
        """
        envelope = FlextTapOracleOicEnvelope.model_validate(data, strict=True)
        if envelope.items is not None:
            items: t.SequenceOf[t.JsonMapping] = envelope.items
            return items
        if envelope.data is not None:
            payload: t.SequenceOf[t.JsonMapping] = envelope.data
            return payload
        return None

    def _track_response_time(self, response_time: float) -> None:
        """Track one response time and adapt the page size.

        Args:
            response_time: Observed request duration in seconds.

        
        """
        self._response_times.append(response_time)
        if len(self._response_times) > c.TapOracleOic.RESPONSE_TIME_HISTORY_SIZE:
            self._response_times.pop(0)
        if len(self._response_times) >= c.TapOracleOic.MIN_RESPONSE_SAMPLES:
            avg_time = sum(self._response_times) / len(self._response_times)
            if (
                avg_time > c.TapOracleOic.SLOW_RESPONSE_THRESHOLD
                and self._page_size > self._min_page_size
            ):
                self._page_size = max(self._min_page_size, int(self._page_size * 0.8))
            elif avg_time < 1.0 and self._page_size < self._max_page_size:
                self._page_size = min(self._max_page_size, int(self._page_size * 1.2))


__all__: list[str] = ["FlextTapOracleOicPaginator"]
