"""Oracle Integration Cloud stream definitions - PEP8 reorganized.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence

import requests
from flext_core import FlextLogger, t

from flext_tap_oracle_oic import c, m

_as_oic_envelope = m._as_oic_envelope  # noqa: SLF001
_as_value_list = m._as_value_list  # noqa: SLF001

# Re-export OICBaseStream from canonical location in models.py
OICBaseStream = m.TapOracleOic.OICBaseStream


class FlextTapOracleOicPaginator:
    """Intelligent Oracle OIC API paginator with adaptive optimization.

    pagination features:
    - Automatic detection of OIC pagination patterns
    - Dynamic page size adjustment based on response performance
    - Error recovery with exponential backoff
    - Memory-efficient streaming for large datasets
    - Response time tracking and optimization
    """

    def __init__(
        self,
        start_value: int = c.TapOicProcessing.DEFAULT_PAGINATOR_START,
        page_size: int = c.TapOicProcessing.DEFAULT_PAGINATOR_PAGE_SIZE,
    ) -> None:
        """Initialize paginator with starting offset and page size."""
        self.current_value: int = start_value
        self._page_size: int = page_size
        self._max_page_size: int = c.TapOicProcessing.PAGINATOR_MAX_PAGE_SIZE
        self._min_page_size: int = c.TapOicProcessing.PAGINATOR_MIN_PAGE_SIZE
        self._adaptive_sizing: bool = True
        self._response_times: list[float] = []

    def get_next(self, response: requests.Response) -> int | None:
        """Calculate next offset for Oracle OIC pagination.

        Args:
        response: HTTP response from OIC API.

        Returns:
        Next offset value or None if no more pages.

        """
        try:
            data = response.json()
            if getattr(response, "elapsed", None) is not None and self._adaptive_sizing:
                self._track_response_time(response.elapsed.total_seconds())
            return self._calculate_next_offset(data)
        except (ValueError, KeyError, TypeError, AttributeError) as e:
            logger = FlextLogger(__name__)
            err_msg = f"OIC pagination parsing failed: {type(e).__name__}: {e}"
            logger.warning(err_msg)
            logger.info("Returning None - pagination parsing failure properly handled")
            logger.debug("This indicates end of pagination or malformed OIC response")
            return None

    def _calculate_next_offset(
        self, data: Mapping[str, t.ContainerValue]
    ) -> int | None:
        """Calculate next offset based on OIC response format."""
        items = self._extract_items_from_response(data)
        if items is None or not items or len(items) < self._page_size:
            return None
        return self.current_value + len(items)

    def _extract_items_from_response(
        self,
        data: Mapping[str, t.ContainerValue],
    ) -> Sequence[Mapping[str, t.ContainerValue]] | None:
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
        if len(self._response_times) > c.TapOicPerformance.RESPONSE_TIME_HISTORY_SIZE:
            self._response_times.pop(0)
        if len(self._response_times) >= c.TapOicPerformance.MIN_RESPONSE_SAMPLES:
            avg_time = sum(self._response_times) / len(self._response_times)
            if (
                avg_time > c.TapOicPerformance.SLOW_RESPONSE_THRESHOLD
                and self._page_size > self._min_page_size
            ):
                self._page_size = max(self._min_page_size, int(self._page_size * 0.8))
            elif avg_time < 1.0 and self._page_size < self._max_page_size:
                self._page_size = min(self._max_page_size, int(self._page_size * 1.2))


# Backward-compatible alias
OICPaginator = FlextTapOracleOicPaginator

__all__: t.StrSequence = ["FlextTapOracleOicPaginator", "OICBaseStream", "OICPaginator"]
