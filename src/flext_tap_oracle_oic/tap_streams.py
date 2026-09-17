"""Oracle Integration Cloud paginator.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_tap_oracle_oic import c, r, t, u
from ._models._envelope import OicEnvelope

if TYPE_CHECKING:
    from flext_api import FlextApiModels

    from flext_tap_oracle_oic import p


def _as_oic_envelope(value: t.JsonMapping) -> p.Result[OicEnvelope]:
    try:
        return r[OicEnvelope].ok(
            OicEnvelope.model_validate(value, strict=True)
        )
    except c.ValidationError as e:
        return r[OicEnvelope].fail(
            f"Invalid OIC envelope format: {e}", exception=e
        )


class FlextTapOracleOicPaginator:
    """Oracle OIC API paginator with adaptive page sizing."""

    def __init__(
        self,
        start_value: int = c.TapOracleOic.DEFAULT_PAGINATOR_START,
        page_size: int = c.TapOracleOic.DEFAULT_PAGINATOR_PAGE_SIZE,
    ) -> None:
        """Initialize paginator with starting offset and page size."""
        self.current_value: int = start_value
        self._page_size: int = page_size
        self._max_page_size: int = c.TapOracleOic.PAGINATOR_MAX_PAGE_SIZE
        self._min_page_size: int = c.TapOracleOic.PAGINATOR_MIN_PAGE_SIZE
        self._adaptive_sizing: bool = True
        self._response_times: list[float] = []

    def get_next(self, response: FlextApiModels.Api.HttpResponse) -> p.Result[int | None]:
        """Calculate next offset for Oracle OIC pagination."""
        data = self._normalize_response_payload(response)
        return self._calculate_next_offset(data)

    def _normalize_response_payload(
        self, response: FlextApiModels.Api.HttpResponse
    ) -> t.JsonMapping:
        """Normalize flext-api response bodies to OIC pagination payloads."""
        match response.body:
            case dict() as body_map:
                return body_map
            case _:
                msg = "Pagination requires a JSON object response body"
                raise TypeError(msg)

    def _calculate_next_offset(self, data: t.JsonMapping) -> p.Result[int | None]:
        """Calculate next offset based on OIC response format."""
        items_result = self._extract_items_from_response(data)
        if items_result.failure:
            return r[int | None].fail(
                "Failed to extract items from response", exception=items_result.exception
            )
        items = items_result.unwrap()
        if items is None or not items or len(items) < self._page_size:
            return r[int | None].ok(None)
        return r[int | None].ok(self.current_value + len(items))

    def _extract_items_from_response(
        self, data: t.JsonMapping
    ) -> p.Result[t.SequenceOf[t.JsonMapping] | None]:
        """Extract items from various OIC response formats."""
        envelope_result = _as_oic_envelope(data)
        if envelope_result.failure:
            return r[t.SequenceOf[t.JsonMapping] | None].fail(
                "Not an OIC envelope format", exception=envelope_result.exception
            )
        envelope = envelope_result.unwrap()
        if envelope.items is not None:
            items: t.SequenceOf[t.JsonMapping] = envelope.items
            return r[t.SequenceOf[t.JsonMapping] | None].ok(items)
        if envelope.data is not None:
            payload: t.SequenceOf[t.JsonMapping] = envelope.data
            return r[t.SequenceOf[t.JsonMapping] | None].ok(payload)
        return r[t.SequenceOf[t.JsonMapping] | None].ok(None)

    def _track_response_time(self, response_time: float) -> None:
        """Track response times for adaptive page sizing."""
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
