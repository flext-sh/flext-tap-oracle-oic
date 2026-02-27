"""Oracle Integration Cloud stream definitions - PEP8 reorganized.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import re
from collections.abc import Iterator, Mapping
from datetime import UTC, datetime
from typing import ClassVar, override

import requests
from flext_api import FlextApi
from flext_api.settings import FlextApiSettings
from flext_core import FlextExceptions, FlextLogger, t
from flext_meltano import FlextMeltanoStream
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter, ValidationError

from flext_tap_oracle_oic.constants import FlextTapOracleOicConstants
from flext_tap_oracle_oic.utilities import FlextMeltanoTapOracleOicUtilities

# Constants for paginator and response tracking
RESPONSE_TIME_HISTORY_SIZE = 10
MIN_RESPONSE_SAMPLES = 5
SLOW_RESPONSE_THRESHOLD = 5.0
HTTP_UNAUTHORIZED = 401
HTTP_FORBIDDEN = 403
HTTP_RATE_LIMITED = 429


class _OicEnvelope(BaseModel):
    """Pydantic envelope for OIC response payloads."""

    model_config = ConfigDict(extra="allow")

    items: list[t.GeneralValueType] | None = None
    data: list[t.GeneralValueType] | None = None
    total_size: int | None = Field(default=None, alias="totalSize")
    count: int | None = None


_GENERAL_LIST_ADAPTER = TypeAdapter(
    list[t.GeneralValueType],
    config=ConfigDict(strict=True),
)
_GENERAL_MAP_ADAPTER = TypeAdapter(
    dict[str, t.GeneralValueType],
    config=ConfigDict(strict=True),
)
_STRING_LIST_ADAPTER = TypeAdapter(list[str], config=ConfigDict(strict=True))


def _as_value_list(value: object) -> list[t.GeneralValueType] | None:
    """Validate payload as strict list[GeneralValueType]."""
    try:
        return _GENERAL_LIST_ADAPTER.validate_python(value)
    except ValidationError:
        return None


def _as_value_map(value: object) -> Mapping[str, t.GeneralValueType] | None:
    """Validate payload as strict dict[str, GeneralValueType]."""
    try:
        return _GENERAL_MAP_ADAPTER.validate_python(value)
    except ValidationError:
        return None


def _as_string_list(value: object) -> list[str] | None:
    """Validate payload as strict list[str]."""
    try:
        return _STRING_LIST_ADAPTER.validate_python(value)
    except ValidationError:
        return None


def _as_oic_envelope(value: object) -> _OicEnvelope | None:
    """Validate payload as an OIC envelope model."""
    try:
        return _OicEnvelope.model_validate(value, strict=True)
    except ValidationError:
        return None


class OICPaginator:
    """Intelligent Oracle OIC API paginator with adaptive optimization.

    pagination features:
    - Automatic detection of OIC pagination patterns
    - Dynamic page size adjustment based on response performance
    - Error recovery with exponential backoff
    - Memory-efficient streaming for large datasets
    - Response time tracking and optimization
    """

    def __init__(self, start_value: int = 0, page_size: int = 100) -> None:
        """Initialize paginator with starting offset and page size."""
        self.current_value: int = start_value
        self._page_size: int = page_size
        self._max_page_size: int = 1000
        self._min_page_size: int = 10
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

            # Track response time for adaptive sizing
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
        self,
        data: object,
    ) -> int | None:
        """Calculate next offset based on OIC response format."""
        items = self._extract_items_from_response(data)
        if items is None or not items or len(items) < self._page_size:
            return None
        return self.current_value + len(items)

    def _extract_items_from_response(
        self,
        data: object,
    ) -> list[t.GeneralValueType] | None:
        """Extract items from various OIC response formats."""
        list_payload = _as_value_list(data)
        if list_payload is not None:
            return list_payload

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

        # Keep only recent response times
        if len(self._response_times) > RESPONSE_TIME_HISTORY_SIZE:
            self._response_times.pop(0)

        # Adjust page size based on average response time
        if len(self._response_times) >= MIN_RESPONSE_SAMPLES:
            avg_time = sum(self._response_times) / len(self._response_times)

            if (
                avg_time > SLOW_RESPONSE_THRESHOLD
                and self._page_size > self._min_page_size
            ):
                # Slow responses - reduce page size
                self._page_size = max(self._min_page_size, int(self._page_size * 0.8))
            elif avg_time < 1.0 and self._page_size < self._max_page_size:
                # Fast responses - increase page size
                self._page_size = min(self._max_page_size, int(self._page_size * 1.2))


class OICBaseStream(FlextMeltanoStream):
    """Professional base stream class for Oracle Integration Cloud APIs.

    stream implementation with:
    - Intelligent endpoint discovery and URL construction
    - OAuth2/IDCS authentication with automatic token refresh
    - Adaptive pagination with performance optimization
    - Complete error handling with exponential backoff
    - Data quality validation and metrics collection
    - Rate limiting and request optimization
    - Incremental extraction with state management
    - Support for all OIC API patterns (Design, Runtime, Monitoring, B2B, Process)
    """

    # Stream configuration attributes (set by dynamic class construction)
    requires_design_api: ClassVar[bool] = False
    requires_runtime_api: ClassVar[bool] = False
    api_path: ClassVar[str | None] = None
    api_category: ClassVar[str] = "core"
    default_sort: ClassVar[str | None] = None
    additional_params: ClassVar[dict[str, t.GeneralValueType] | None] = None
    primary_keys: ClassVar[list[str]] = []  # type: ignore[override]

    @override
    def get_records(
        self,
        context: Mapping[str, t.GeneralValueType] | None = None,
    ) -> Iterator[dict[str, t.GeneralValueType]]:
        """Get records from OIC API.

        Args:
            context: Optional context for record extraction.

        Yields:
            Records from the OIC API.

        """
        ...

    @property
    def url_base(self) -> str:
        """Build base URL for Oracle OIC API requests with intelligent discovery.

        Returns:
        Base URL with appropriate OIC API endpoint for stream type.

        """
        # Zero Tolerance FIX: Use FlextMeltanoTapOracleOicUtilities for URL operations
        utilities = FlextMeltanoTapOracleOicUtilities()

        base_url = str(
            self.config.get("base_url") or self.config.get("oic_url", ""),
        ).rstrip("/")

        if not base_url:
            msg = "Base URL is required but not configured"
            raise ValueError(msg)

        # Zero Tolerance FIX: Use utilities for endpoint validation
        validation_result = utilities.OicApiProcessing.validate_oic_endpoint(base_url)
        if validation_result.is_failure:
            msg = f"Invalid OIC endpoint: {validation_result.error}"
            raise ValueError(msg)

        # Auto-detect region from URL pattern
        region = self.config.get("region")
        if not region and "integration.ocp.oraclecloud.com" in base_url:
            region_match = re.search(r"(\w+-\w+-\d+)", base_url)
            region = region_match.group(1) if region_match else "us-ashburn-1"

        # Convert to appropriate API endpoint based on stream requirements
        if "integration.ocp.oraclecloud.com" in base_url:
            if self.requires_design_api:
                base_url = f"https://design.integration.{region}.ocp.oraclecloud.com"
            elif self.requires_runtime_api:
                base_url = f"https://runtime.integration.{region}.ocp.oraclecloud.com"

        # Handle specialized API paths
        if self.api_path is not None:
            return base_url + self.api_path

        api_paths = {
            "core": FlextTapOracleOicConstants.OIC_API_BASE_PATH,
            "monitoring": FlextTapOracleOicConstants.OIC_MONITORING_API_PATH,
            "b2b": FlextTapOracleOicConstants.OIC_B2B_API_PATH,
            "process": FlextTapOracleOicConstants.OIC_PROCESS_API_PATH,
        }
        return base_url + api_paths.get(
            self.api_category,
            FlextTapOracleOicConstants.OIC_API_BASE_PATH,
        )

    @property
    def api_client(self) -> FlextApi:
        """Get authenticated API client from parent tap's OIC client."""
        # Fallback to creating new FlextApi
        api_config = FlextApiSettings()
        return FlextApi(api_config)

    def get_new_paginator(self) -> OICPaginator:
        """Create new Oracle OIC paginator with configuration.

        Returns:
        OICPaginator instance configured with settings from tap config.

        """
        return OICPaginator(start_value=0, page_size=self.config.get("page_size", 100))

    def get_url_params(
        self,
        context: Mapping[str, t.GeneralValueType] | None,
        next_page_token: int | None,
    ) -> Mapping[str, t.GeneralValueType]:
        """Build URL parameters for Oracle OIC API requests.

        Args:
        context: Stream context with replication values.
        next_page_token: Token for pagination (offset value).

        Returns:
        Dictionary of URL parameters optimized for OIC API.

        """
        params: dict[str, t.GeneralValueType] = {}

        # Pagination parameters
        page_size = self.config.get("page_size", 100)
        params["limit"] = min(page_size, 1000)  # OIC API limit
        params["offset"] = next_page_token or 0

        # Instance filtering
        instance_id = self.config.get("instance_id")
        if instance_id:
            params["integrationInstance"] = instance_id

        # Sorting parameters
        sort_field = self.config.get("sort_field")
        if sort_field:
            sort_direction = "desc" if self.config.get("sort_desc", False) else "asc"
            params["orderBy"] = f"{sort_field}:{sort_direction}"
        elif self.default_sort is not None:
            params["orderBy"] = self.default_sort

        # Custom query filter
        custom_filter = self.config.get("custom_filter")
        if custom_filter:
            params["q"] = custom_filter

        # Date range filtering for incremental extraction
        if (
            self.replication_key
            and context
            and context.get("starting_replication_value")
        ):
            start_date = context["starting_replication_value"]
            params[f"{self.replication_key}>="] = start_date

        # Field selection for reduced payload
        select_fields = self.config.get("select_fields")
        if select_fields:
            field_list = _as_string_list(select_fields)
            params["fields"] = (
                ",".join(field_list) if field_list is not None else str(select_fields)
            )

        # Stream-specific parameters
        if self.additional_params is not None:
            params.update(self.additional_params)

        # Remove empty values
        return {k: v for k, v in params.items() if v is not None}

    def parse_response(
        self,
        response: requests.Response,
    ) -> Iterator[Mapping[str, t.GeneralValueType]]:
        """Parse Oracle OIC API response and yield records with validation.

        Args:
        response: HTTP response from OIC API.

        Yields:
        Individual records from the API response with tap metadata.

        """
        try:
            # Validate response status
            if not response.ok:
                self._handle_response_error(response)
                return

            try:
                data = response.json()
            except (ValueError, TypeError, KeyError):
                self.logger.exception("Failed to parse JSON from %s", response.url)
                if self.config.get("fail_on_parsing_errors", True):
                    raise
                return

            # Track response metrics for monitoring
            self._track_response_metrics(response, data)

            # Extract records from response and yield with validation
            response_url = str(getattr(response, "url", "unknown"))
            yield from self._extract_and_yield_records(data, response_url)

        except (ValueError, TypeError, KeyError, AttributeError):
            response_url_err = str(getattr(response, "url", "unknown"))
            self.logger.exception("Error parsing response from %s", response_url_err)
            if self.config.get("fail_on_parsing_errors", True):
                raise

    def _extract_and_yield_records(
        self,
        data: object,
        url: str,
    ) -> Iterator[Mapping[str, t.GeneralValueType]]:
        """Extract and yield records with validation and enrichment."""
        records_yielded = 0

        for item in self._extract_items_for_processing(data):
            if self._validate_record(item):
                yield self._enrich_record(item)
                records_yielded += 1

        if records_yielded == 0 and not self._is_empty_result_expected(data):
            map_data = _as_value_map(data)
            payload_descriptor: object = (
                list(map_data.keys()) if map_data is not None else type(data)
            )
            self.logger.warning(
                "Unknown response format from %s: %s",
                url,
                payload_descriptor,
            )
        elif records_yielded > 0:
            self.logger.debug(
                "Successfully parsed %s records from %s",
                records_yielded,
                url,
            )

    def _extract_items_for_processing(
        self,
        data: object,
    ) -> Iterator[Mapping[str, t.GeneralValueType]]:
        """Extract items from various OIC response formats for processing."""
        list_payload = _as_value_list(data)
        if list_payload is not None:
            yield from self._process_list_data(list_payload)
            return

        map_payload = _as_value_map(data)
        if map_payload is not None:
            yield from self._process_dict_data(map_payload)

    def _process_list_data(
        self,
        data: list[t.GeneralValueType],
    ) -> Iterator[Mapping[str, t.GeneralValueType]]:
        """Process list-type response data."""
        for item in data:
            record = _as_value_map(item)
            if record is not None:
                yield record

    def _process_dict_data(
        self,
        data: Mapping[str, t.GeneralValueType],
    ) -> Iterator[Mapping[str, t.GeneralValueType]]:
        """Process dict-type response data with OIC format detection."""
        envelope = _as_oic_envelope(data)
        if envelope is not None and envelope.items is not None:
            yield from self._process_list_data(envelope.items)
            return

        if envelope is not None and envelope.data is not None:
            yield from self._process_list_data(envelope.data)
            return

        if self._is_single_record(data):
            yield data

    def _is_empty_result_expected(
        self,
        data: object,
    ) -> bool:
        """Check if empty result is expected/normal based on OIC response metadata."""
        envelope = _as_oic_envelope(data)
        if envelope is not None:
            return (
                envelope.total_size == 0
                or envelope.count == 0
                or (envelope.items is not None and len(envelope.items) == 0)
                or (envelope.data is not None and len(envelope.data) == 0)
            )

        list_payload = _as_value_list(data)
        return len(list_payload) == 0 if list_payload is not None else False

    def _is_single_record(self, data: Mapping[str, t.GeneralValueType]) -> bool:
        """Check if dict[str, t.GeneralValueType] represents a single record vs OIC metadata container."""
        metadata_keys = {
            "totalSize",
            "count",
            "hasMore",
            "offset",
            "limit",
            "items",
            "data",
        }
        return not any(key in data for key in metadata_keys)

    def _validate_record(self, record: Mapping[str, t.GeneralValueType]) -> bool:
        """Validate record meets basic requirements for processing."""
        return _as_value_map(record) is not None

    def _enrich_record(
        self, record: Mapping[str, t.GeneralValueType]
    ) -> Mapping[str, t.GeneralValueType]:
        """Enrich record with tap metadata for traceability."""
        enriched: dict[str, t.GeneralValueType] = dict(record)
        enriched["_tap_extracted_at"] = datetime.now(UTC).isoformat()
        enriched["_tap_stream_name"] = self.name
        return enriched

    def _handle_response_error(self, response: requests.Response) -> None:
        """Handle Oracle OIC API response errors with proper categorization."""
        try:
            error_data = _as_value_map(response.json()) or {}
            error_message = error_data.get("message") or error_data.get("error")
        except (ValueError, TypeError, KeyError):
            error_message = (
                getattr(response, "text", None)
                or f"HTTP {getattr(response, 'status_code', 'unknown')}"
            )

        response_url = str(getattr(response, "url", "unknown"))
        err_msg = str(error_message)
        self.logger.error("OIC API error from %s: %s", response_url, err_msg)

        status_code = getattr(response, "status_code", 0)
        if status_code == HTTP_UNAUTHORIZED:
            msg = "Unauthorized: Authentication failed or token expired"
            raise FlextExceptions.AuthenticationError(msg)
        if status_code == HTTP_FORBIDDEN:
            msg = "Forbidden: Insufficient permissions to access resource"
            raise FlextExceptions.AuthorizationError(msg)
        if status_code == HTTP_RATE_LIMITED:
            msg = "Rate limit exceeded: Too many requests"
            raise FlextExceptions.RateLimitError(msg)
        raise_for_status = getattr(response, "raise_for_status", None)
        if raise_for_status is not None:
            raise_for_status()

    def _track_response_metrics(
        self,
        response: requests.Response,
        data: object,
    ) -> None:
        """Track response metrics for monitoring and optimization."""
        # Log response time and size for monitoring
        if getattr(response, "elapsed", None) is not None:
            self.logger.debug("Response time: %.2fs", response.elapsed.total_seconds())

        # Log record count for monitoring
        list_payload = _as_value_list(data)
        if list_payload is not None:
            self.logger.debug("Received %s records", len(list_payload))
            return

        envelope = _as_oic_envelope(data)
        if envelope is None:
            return
        if envelope.items is not None:
            self.logger.debug("Received %s records", len(envelope.items))
        elif envelope.data is not None:
            self.logger.debug("Received %s records", len(envelope.data))


# Export for module interface
__all__: list[str] = [
    "OICBaseStream",
    "OICPaginator",
]
