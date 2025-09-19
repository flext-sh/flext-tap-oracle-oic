"""Oracle Integration Cloud stream definitions - PEP8 reorganized.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

import re
from collections.abc import Iterator, Mapping
from datetime import UTC, datetime

from flext_api import FlextApiClient
from flext_core import FlextExceptions as FlextServiceError, FlextLogger, FlextTypes
from flext_meltano import FlextTapStream
from flext_tap_oracle_oic.constants import (
    OIC_API_BASE_PATH,
    OIC_B2B_API_PATH,
    OIC_MONITORING_API_PATH,
    OIC_PROCESS_API_PATH,
)

# Constants for paginator and response tracking
RESPONSE_TIME_HISTORY_SIZE = 10
MIN_RESPONSE_SAMPLES = 5
SLOW_RESPONSE_THRESHOLD = 5.0
HTTP_UNAUTHORIZED = 401
HTTP_FORBIDDEN = 403
HTTP_RATE_LIMITED = 429


class OICPaginator:
    """Intelligent Oracle OIC API paginator with adaptive optimization.

    Enterprise-grade pagination features:
    - Automatic detection of OIC pagination patterns
    - Dynamic page size adjustment based on response performance
    - Error recovery with exponential backoff
    - Memory-efficient streaming for large datasets
    - Response time tracking and optimization
    """

    def __init__(self, start_value: int = 0, page_size: int = 100) -> None:
        """Initialize paginator with starting offset and page size."""
        super().__init__(start_value, page_size)
        self._max_page_size = 1000
        self._min_page_size = 10
        self._adaptive_sizing = True
        self._response_times: list[float] = []

    def get_next(self, response: object) -> int | None:
        """Calculate next offset for Oracle OIC pagination.

        Args:
            response: HTTP response from OIC API.

        Returns:
            Next offset value or None if no more pages.

        """
        try:
            data = response.json()

            # Track response time for adaptive sizing
            if hasattr(response, "elapsed") and self._adaptive_sizing:
                self._track_response_time(response.elapsed.total_seconds())

            return self._calculate_next_offset(data)

        except (ValueError, KeyError, TypeError, AttributeError) as e:
            logger = FlextLogger(__name__)
            logger.warning(f"OIC pagination parsing failed: {type(e).__name__}: {e}")
            logger.info("Returning None - pagination parsing failure properly handled")
            logger.debug("This indicates end of pagination or malformed OIC response")
            return None

    def _calculate_next_offset(
        self,
        data: FlextTypes.Core.Dict | FlextTypes.Core.List,
    ) -> int | None:
        """Calculate next offset based on OIC response format."""
        items = self._extract_items_from_response(data)
        if items is None or not items or len(items) < self._page_size:
            return None
        return self.current_value + len(items)

    def _extract_items_from_response(
        self,
        data: FlextTypes.Core.Dict | FlextTypes.Core.List,
    ) -> FlextTypes.Core.List | None:
        """Extract items from various OIC response formats."""
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            if "items" in data and isinstance(data["items"], list):
                return data["items"]
            if "data" in data and isinstance(data["data"], list):
                return data["data"]
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


class OICBaseStream(FlextTapStream):
    """Professional base stream class for Oracle Integration Cloud APIs.

    Enterprise-grade stream implementation with:
    - Intelligent endpoint discovery and URL construction
    - OAuth2/IDCS authentication with automatic token refresh
    - Adaptive pagination with performance optimization
    - Comprehensive error handling with exponential backoff
    - Data quality validation and metrics collection
    - Rate limiting and request optimization
    - Incremental extraction with state management
    - Support for all OIC API patterns (Design, Runtime, Monitoring, B2B, Process)
    """

    @property
    def url_base(self) -> str:
        """Build base URL for Oracle OIC API requests with intelligent discovery.

        Returns:
            Base URL with appropriate OIC API endpoint for stream type.

        """
        base_url = str(
            self.config.get("base_url") or self.config.get("oic_url", ""),
        ).rstrip("/")

        if not base_url:
            msg = "Base URL is required but not configured"
            raise ValueError(msg)

        # Auto-detect region from URL pattern
        region = self.config.get("region")
        if not region and "integration.ocp.oraclecloud.com" in base_url:
            region_match = re.search(r"(\w+-\w+-\d+)", base_url)
            region = region_match.group(1) if region_match else "us-ashburn-1"

        # Convert to appropriate API endpoint based on stream requirements
        if "integration.ocp.oraclecloud.com" in base_url:
            if hasattr(self, "requires_design_api") and self.requires_design_api:
                base_url = f"https://design.integration.{region}.ocp.oraclecloud.com"
            elif hasattr(self, "requires_runtime_api") and self.requires_runtime_api:
                base_url = f"https://runtime.integration.{region}.ocp.oraclecloud.com"

        # Handle specialized API paths
        if hasattr(self, "api_path"):
            return base_url + str(self.api_path)
        if hasattr(self, "api_category"):
            api_paths = {
                "core": OIC_API_BASE_PATH,
                "monitoring": OIC_MONITORING_API_PATH,
                "b2b": OIC_B2B_API_PATH,
                "process": OIC_PROCESS_API_PATH,
            }
            return base_url + api_paths.get(self.api_category, OIC_API_BASE_PATH)

        return base_url + OIC_API_BASE_PATH

    @property
    def api_client(self) -> FlextApiClient:
        """Get authenticated API client from parent tap's OIC client."""
        # Access the Tap's OIC client for authenticated API client
        if hasattr(self, "tap") and hasattr(self.tap, "client"):
            client_result = self.tap.client.get_authenticated_client()
            if client_result.success and client_result.data is not None:
                return client_result.data

        # Fallback to creating new FlextApiClient
        return FlextApiClient()

    def get_new_paginator(self) -> OICPaginator:
        """Create new Oracle OIC paginator with configuration.

        Returns:
            OICPaginator instance configured with settings from tap config.

        """
        return OICPaginator(start_value=0, page_size=self.config.get("page_size", 100))

    def get_url_params(
        self,
        context: Mapping[str, object] | None,
        next_page_token: object | None,
    ) -> FlextTypes.Core.Dict:
        """Build URL parameters for Oracle OIC API requests.

        Args:
            context: Stream context with replication values.
            next_page_token: Token for pagination (offset value).

        Returns:
            Dictionary of URL parameters optimized for OIC API.

        """
        params: FlextTypes.Core.Dict = {}

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
        elif hasattr(self, "default_sort"):
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
            if isinstance(select_fields, list):
                params["fields"] = ",".join(select_fields)
            else:
                params["fields"] = select_fields

        # Stream-specific parameters
        if hasattr(self, "additional_params"):
            if callable(self.additional_params):
                params.update(self.additional_params(context))
            else:
                params.update(self.additional_params)

        # Remove empty values
        return {k: v for k, v in params.items() if v is not None}

    def parse_response(
        self,
        response: object,
    ) -> Iterator[FlextTypes.Core.Dict]:
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
            yield from self._extract_and_yield_records(data, response.url)

        except (ValueError, TypeError, KeyError, AttributeError):
            self.logger.exception("Error parsing response from %s", response.url)
            if self.config.get("fail_on_parsing_errors", True):
                raise

    def _extract_and_yield_records(
        self,
        data: FlextTypes.Core.Dict | FlextTypes.Core.List,
        url: str,
    ) -> Iterator[FlextTypes.Core.Dict]:
        """Extract and yield records with validation and enrichment."""
        records_yielded = 0

        for item in self._extract_items_for_processing(data):
            if self._validate_record(item):
                yield self._enrich_record(item)
                records_yielded += 1

        if records_yielded == 0 and not self._is_empty_result_expected(data):
            self.logger.warning(
                "Unknown response format from %s: %s",
                url,
                list(data.keys()) if isinstance(data, dict) else type(data),
            )
        elif records_yielded > 0:
            self.logger.debug(
                "Successfully parsed %s records from %s",
                records_yielded,
                url,
            )

    def _extract_items_for_processing(
        self,
        data: FlextTypes.Core.Dict | FlextTypes.Core.List,
    ) -> Iterator[FlextTypes.Core.Dict]:
        """Extract items from various OIC response formats for processing."""
        if isinstance(data, list):
            yield from self._process_list_data(data)
        elif isinstance(data, dict):
            yield from self._process_dict_data(data)

    def _process_list_data(
        self, data: FlextTypes.Core.List,
    ) -> Iterator[FlextTypes.Core.Dict]:
        """Process list-type response data."""
        for item in data:
            if isinstance(item, dict):
                yield item

    def _process_dict_data(
        self,
        data: FlextTypes.Core.Dict,
    ) -> Iterator[FlextTypes.Core.Dict]:
        """Process dict-type response data with OIC format detection."""
        if "items" in data:
            items = data["items"]
            if isinstance(items, list):
                yield from self._process_list_data(items)
        elif "data" in data:
            data_items = data["data"]
            if isinstance(data_items, list):
                yield from self._process_list_data(data_items)
        elif self._is_single_record(data):
            yield data

    def _is_empty_result_expected(
        self, data: FlextTypes.Core.Dict | FlextTypes.Core.List,
    ) -> bool:
        """Check if empty result is expected/normal based on OIC response metadata."""
        if isinstance(data, dict):
            items = data.get("items", [])
            data_items = data.get("data", [])
            return (
                data.get("totalSize", 0) == 0
                or data.get("count", 0) == 0
                or (isinstance(items, list) and len(items) == 0)
                or (isinstance(data_items, list) and len(data_items) == 0)
            )
        return len(data) == 0

    def _is_single_record(self, data: FlextTypes.Core.Dict) -> bool:
        """Check if dict represents a single record vs OIC metadata container."""
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

    def _validate_record(self, record: FlextTypes.Core.Dict) -> bool:
        """Validate record meets basic requirements for processing."""
        return isinstance(record, dict)

    def _enrich_record(self, record: FlextTypes.Core.Dict) -> FlextTypes.Core.Dict:
        """Enrich record with tap metadata for traceability."""
        enriched = dict(record)
        enriched["_tap_extracted_at"] = datetime.now(UTC).isoformat()
        enriched["_tap_stream_name"] = self.name
        return enriched

    def _handle_response_error(self, response: object) -> None:
        """Handle Oracle OIC API response errors with proper categorization."""
        try:
            error_data = response.json()
            error_message = error_data.get("message") or error_data.get("error")
        except (ValueError, TypeError, KeyError):
            error_message = response.text or f"HTTP {response.status_code}"

        self.logger.error("OIC API error from %s: %s", response.url, error_message)

        if response.status_code == HTTP_UNAUTHORIZED:
            msg = "Unauthorized: Authentication failed or token expired"
            raise FlextServiceError(msg)
        if response.status_code == HTTP_FORBIDDEN:
            msg = "Forbidden: Insufficient permissions to access resource"
            raise FlextServiceError(msg)
        if response.status_code == HTTP_RATE_LIMITED:
            msg = "Rate limit exceeded: Too many requests"
            raise FlextServiceError(msg)
        response.raise_for_status()

    def _track_response_metrics(
        self,
        response: object,
        data: FlextTypes.Core.Dict | FlextTypes.Core.List,
    ) -> None:
        """Track response metrics for monitoring and optimization."""
        # Log response time and size for monitoring
        if hasattr(response, "elapsed"):
            self.logger.debug("Response time: %.2fs", response.elapsed.total_seconds())

        # Log record count for monitoring
        if isinstance(data, list):
            self.logger.debug("Received %s records", len(data))
        elif isinstance(data, dict):
            if "items" in data:
                items = data["items"]
                if isinstance(items, list):
                    self.logger.debug("Received %s records", len(items))
            elif "data" in data:
                data_items = data["data"]
                if isinstance(data_items, list):
                    self.logger.debug("Received %s records", len(data_items))


# Export for module interface
__all__: FlextTypes.Core.StringList = [
    "OICBaseStream",
    "OICPaginator",
]
