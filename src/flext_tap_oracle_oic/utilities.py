"""Singer tap utilities for Oracle OIC (Oracle Integration Cloud) operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import re
from collections.abc import (
    Mapping,
    MutableMapping,
    Sequence,
)
from datetime import UTC, datetime
from typing import ClassVar
from urllib.parse import urljoin, urlparse

from flext_meltano import u
from flext_oracle_oic import FlextOracleOicUtilities
from flext_tap_oracle_oic import c, p, r, t


class FlextTapOracleOicUtilities(u, FlextOracleOicUtilities):
    """Single unified utilities class for Singer tap Oracle OIC operations.

    Follows FLEXT unified class pattern with nested helper classes for
    domain-specific Singer tap functionality with Oracle Integration Cloud.
    Extends ucific operations.
    """

    DEFAULT_BATCH_SIZE: ClassVar[int] = 100
    DEFAULT_TIMEOUT: ClassVar[int] = 30
    MAX_RETRIES: ClassVar[int] = 3
    DEFAULT_PAGE_SIZE: ClassVar[int] = 50

    @staticmethod
    def _as_list(value: t.ContainerValue | None) -> Sequence[t.ContainerValue] | None:
        """Strict list validation via Pydantic adapter."""
        try:
            return t.STRICT_LIST_ADAPTER.validate_python(
                value,
            )
        except c.ValidationError:
            return None

    @staticmethod
    def _as_map(
        value: t.ContainerValue | None,
    ) -> t.ContainerValueMapping | None:
        """Strict map validation via Pydantic adapter."""
        try:
            return t.STRICT_MAP_ADAPTER.validate_python(value)
        except c.ValidationError:
            return None

    @staticmethod
    def _as_int(value: t.ContainerValue | None) -> int | None:
        """Strict integer validation via Pydantic adapter."""
        try:
            return t.STRICT_INT_ADAPTER.validate_python(value)
        except c.ValidationError:
            return None

    class TapOracleOic:
        """OIC tap domain utilities.

        Singer protocol utilities (emit_schema, emit_record, emit_state,
        process_stdin, build_catalog_entry) are in the parent:
        ``u.Meltano.Singer.*`` — accessed via MRO, never duplicated here.
        """

        class OicApiProcessing:
            """Oracle OIC API processing utilities."""

            @staticmethod
            def build_oic_api_url(
                base_url: str,
                resource_path: str,
                query_params: t.StrMapping | None = None,
            ) -> p.Result[str]:
                """Build Oracle OIC API URL with proper formatting.

                Args:
                base_url: Base OIC URL
                resource_path: API resource path
                query_params: Optional query parameters

                Returns:
                r[str]: Complete API URL or error

                """
                try:
                    validation_result = FlextTapOracleOicUtilities.TapOracleOic.OicApiProcessing.validate_oic_endpoint(
                        base_url,
                    )
                    if validation_result.failure:
                        return r[str].fail(
                            f"Base URL validation failed: {validation_result.error}",
                        )
                    if not resource_path.startswith("/"):
                        resource_path = f"/{resource_path}"
                    api_url = urljoin(base_url, resource_path)
                    if query_params:
                        query_string = "&".join(
                            (f"{k}={v}" for k, v in query_params.items()),
                        )
                        api_url = f"{api_url}?{query_string}"
                    return r[str].ok(api_url)
                except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
                    return r[str].fail(f"URL building error: {e}")

            @staticmethod
            def extract_pagination_info(
                response: Mapping[str, t.ContainerValueMapping] | None,
            ) -> t.ContainerValueMapping:
                """Extract pagination information from OIC response.

                Args:
                response: OIC API response

                Returns:
                t.ContainerValueMapping: Pagination information

                """
                if not response:
                    return {
                        "has_more": False,
                        "limit": FlextTapOracleOicUtilities.DEFAULT_PAGE_SIZE,
                        "offset": 0,
                        "total_count": 0,
                        "current_page_size": 0,
                    }
                items: t.ContainerValue = response.get("items", [])
                items_list_raw = FlextTapOracleOicUtilities._as_list(items)
                items_list: Sequence[t.ContainerValue] = (
                    items_list_raw if items_list_raw is not None else []
                )
                return {
                    "has_more": response.get("hasMore", False),
                    "limit": response.get(
                        "limit",
                        FlextTapOracleOicUtilities.DEFAULT_PAGE_SIZE,
                    ),
                    "offset": response.get("offset", 0),
                    "total_count": response.get("count", 0),
                    "current_page_size": len(items_list),
                }

            @staticmethod
            def parse_oic_response(
                response_data: t.ContainerValueMapping,
            ) -> p.Result[t.ContainerValueMapping]:
                """Parse Oracle OIC API response.

                Args:
                response_data: Raw API response data

                Returns:
                r[t.ContainerValueMapping]: Parsed response or error

                """
                if not response_data:
                    return r[t.ContainerValueMapping].fail(
                        "Response data cannot be empty",
                    )
                try:
                    parsed_response = {
                        "items": response_data.get("items", []),
                        "count": response_data.get("count", 0),
                        "hasMore": response_data.get("hasMore", False),
                        "limit": response_data.get("limit", 0),
                        "offset": response_data.get("offset", 0),
                    }
                    if "data" in response_data:
                        parsed_response["items"] = response_data["data"]
                    return r[t.ContainerValueMapping].ok(parsed_response)
                except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
                    return r[t.ContainerValueMapping].fail(
                        f"Response parsing error: {e}",
                    )

            @staticmethod
            def validate_oic_endpoint(endpoint_url: str) -> p.Result[str]:
                """Validate Oracle OIC endpoint URL.

                Args:
                endpoint_url: OIC endpoint URL

                Returns:
                r[str]: Validated URL or error

                """
                if not endpoint_url:
                    return r[str].fail("OIC endpoint URL cannot be empty")
                try:
                    parsed = urlparse(endpoint_url)
                    if not parsed.scheme or not parsed.netloc:
                        return r[str].fail("Invalid URL format")
                    if "oic" not in parsed.netloc.lower():
                        return r[str].fail("URL does not appear to be an OIC endpoint")
                    return r[str].ok(endpoint_url)
                except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
                    return r[str].fail(f"URL validation error: {e}")

        class OicDataProcessing:
            """Oracle OIC data processing utilities."""

            @staticmethod
            def extract_integration_metadata(
                integration_data: t.ContainerValueMapping | None,
            ) -> t.ContainerValueMapping:
                """Extract metadata from Oracle OIC integration data.

                Args:
                integration_data: Raw integration data

                Returns:
                t.ContainerValueMapping: Extracted metadata

                """
                if not integration_data:
                    return {}
                metadata: MutableMapping[str, t.ContainerValue | None] = {
                    "id": integration_data.get("id"),
                    "name": integration_data.get("name"),
                    "version": integration_data.get("version"),
                    "status": integration_data.get("status"),
                    "created": integration_data.get("timeCreated"),
                    "updated": integration_data.get("timeUpdated"),
                    "description": integration_data.get("description"),
                    "type": integration_data.get("style"),
                }
                connections = integration_data.get("connectionInstances", [])
                connection_list_raw = FlextTapOracleOicUtilities._as_list(connections)
                connection_list: Sequence[t.ContainerValue] = (
                    connection_list_raw if connection_list_raw is not None else []
                )
                metadata["connection_count"] = len(connection_list)
                connection_types: t.StrSequence = [
                    str(connection_type)
                    for conn in connection_list
                    if (conn_map := FlextTapOracleOicUtilities._as_map(conn))
                    is not None
                    and (connection_type := conn_map.get("connectionType")) is not None
                ]
                metadata["connection_types"] = list(connection_types)
                return {k: v for k, v in metadata.items() if v is not None}

            @staticmethod
            def format_oic_timestamp(timestamp_str: str) -> p.Result[str]:
                """Format Oracle OIC timestamp to ISO format.

                Args:
                timestamp_str: OIC timestamp string

                Returns:
                r[str]: ISO formatted timestamp or error

                """
                if not timestamp_str:
                    return r[str].fail("Timestamp string cannot be empty")
                try:
                    formats = [
                        "%Y-%m-%dT%H:%M:%S.%fZ",
                        "%Y-%m-%dT%H:%M:%SZ",
                        "%Y-%m-%dT%H:%M:%S%z",
                        "%Y-%m-%dT%H:%M:%S.%f%z",
                        "%Y-%m-%dT%H:%M:%S",
                        "%Y-%m-%d %H:%M:%S",
                    ]
                    for fmt in formats:
                        try:
                            dt_naive = datetime.strptime(timestamp_str, fmt)
                            dt = (
                                dt_naive.replace(tzinfo=UTC)
                                if dt_naive.tzinfo is None
                                else dt_naive
                            )
                            return r[str].ok(dt.isoformat())
                        except ValueError:
                            continue
                    return r[str].fail(f"Unsupported timestamp format: {timestamp_str}")
                except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
                    return r[str].fail(f"Timestamp formatting error: {e}")

            @staticmethod
            def normalize_integration_name(integration_name: str) -> str:
                """Normalize Oracle OIC integration name.

                Args:
                integration_name: Raw integration name

                Returns:
                str: Normalized integration name

                """
                if not integration_name:
                    return ""
                normalized = re.sub(r"[^a-zA-Z0-9]", "_", integration_name.lower())
                normalized = re.sub(r"_+", "_", normalized)
                return normalized.strip("_")

            @staticmethod
            def sanitize_oic_field_name(field_name: str) -> str:
                """Sanitize OIC field name for JSON schema.

                Args:
                field_name: Raw field name

                Returns:
                str: Sanitized field name

                """
                if not field_name:
                    return ""
                sanitized = re.sub(r"(?<!^)(?=[A-Z])", "_", field_name).lower()
                sanitized = re.sub(r"[^a-zA-Z0-9_]", "_", sanitized)
                sanitized = re.sub(r"_+", "_", sanitized)
                if sanitized and sanitized[0].isdigit():
                    sanitized = f"field_{sanitized}"
                return sanitized.strip("_")

        class ConfigValidation:
            """Configuration validation utilities."""

            @staticmethod
            def validate_oic_connection_config(
                settings: Mapping[str, t.ContainerValueMapping],
            ) -> p.Result[t.ContainerValueMapping]:
                """Validate Oracle OIC connection configuration.

                Args:
                settings: Configuration dictionary

                Returns:
                r[t.ContainerValueMapping]: Validated settings or error

                """
                required_fields = ["oic_base_url", "username", "password"]
                missing_fields = [
                    field for field in required_fields if field not in settings
                ]
                if missing_fields:
                    return r[t.ContainerValueMapping].fail(
                        f"Missing required fields: {', '.join(missing_fields)}",
                    )
                url_validation = FlextTapOracleOicUtilities.TapOracleOic.OicApiProcessing.validate_oic_endpoint(
                    str(settings["oic_base_url"]),
                )
                if url_validation.failure:
                    return r[t.ContainerValueMapping].fail(
                        f"Invalid OIC URL: {url_validation.error}",
                    )
                if not str(settings["username"]).strip():
                    return r[t.ContainerValueMapping].fail(
                        "Username cannot be empty",
                    )
                if not str(settings["password"]).strip():
                    return r[t.ContainerValueMapping].fail(
                        "Password cannot be empty",
                    )
                if "timeout" in settings:
                    timeout = FlextTapOracleOicUtilities._as_int(settings["timeout"])
                    if timeout is None or timeout <= 0:
                        return r[t.ContainerValueMapping].fail(
                            "Timeout must be a positive integer",
                        )
                return r[t.ContainerValueMapping].ok(settings)

            @staticmethod
            def validate_stream_config(
                settings: Mapping[str, t.ContainerValueMapping],
            ) -> p.Result[t.ContainerValueMapping]:
                """Validate OIC tap stream configuration.

                Args:
                settings: Stream configuration

                Returns:
                r[t.ContainerValueMapping]: Validated settings or error

                """
                if "streams" not in settings:
                    return r[t.ContainerValueMapping].fail(
                        "Configuration must include 'streams' section",
                    )
                streams = settings["streams"]
                stream_map = FlextTapOracleOicUtilities._as_map(streams)
                if stream_map is None:
                    return r[t.ContainerValueMapping].fail(
                        "Streams configuration must be a dictionary",
                    )
                for stream_name, stream_payload in stream_map.items():
                    stream_config = FlextTapOracleOicUtilities._as_map(stream_payload)
                    if stream_config is None:
                        return r[t.ContainerValueMapping].fail(
                            f"Stream '{stream_name}' configuration must be a dictionary",
                        )
                    if "selected" not in stream_config:
                        return r[t.ContainerValueMapping].fail(
                            f"Stream '{stream_name}' must have 'selected' field",
                        )
                    if "page_size" in stream_config:
                        page_size = FlextTapOracleOicUtilities._as_int(
                            stream_config["page_size"],
                        )
                        max_page_size = c.TapOracleOic.TapOicProcessing.MAX_PAGE_SIZE
                        if (
                            page_size is None
                            or page_size <= 0
                            or page_size > max_page_size
                        ):
                            return r[t.ContainerValueMapping].fail(
                                f"Stream '{stream_name}' page_size must be between 1 and {max_page_size}",
                            )
                return r[t.ContainerValueMapping].ok(settings)

        class StateManagement:
            """State management utilities for incremental syncs."""

            @staticmethod
            def get_bookmark(
                state: Mapping[str, t.ContainerValueMapping],
                stream_name: str,
                bookmark_key: str,
            ) -> t.ContainerValue | None:
                """Get bookmark value for a stream.

                Args:
                state: Complete state dictionary
                stream_name: Name of the stream
                bookmark_key: Bookmark key

                Returns:
                t.ContainerValue: Bookmark value or None

                """
                stream_state = FlextTapOracleOicUtilities.TapOracleOic.StateManagement.get_stream_state(
                    state,
                    stream_name,
                )
                return stream_state.get(bookmark_key)

            @staticmethod
            def get_stream_state(
                state: Mapping[str, t.ContainerValueMapping],
                stream_name: str,
            ) -> t.ContainerValueMapping:
                """Get state for a specific stream.

                Args:
                state: Complete state dictionary
                stream_name: Name of the stream

                Returns:
                t.ContainerValueMapping: Stream state

                """
                bookmarks = state.get("bookmarks", {})
                bookmark_map = FlextTapOracleOicUtilities._as_map(bookmarks)
                if bookmark_map is None:
                    return {}
                stream_bookmarks = FlextTapOracleOicUtilities._as_map(
                    bookmark_map.get(stream_name, {}),
                )
                return stream_bookmarks if stream_bookmarks is not None else {}

            @staticmethod
            def set_bookmark(
                state: Mapping[str, t.ContainerValueMapping],
                stream_name: str,
                bookmark_key: str,
                bookmark_value: t.ContainerValue,
            ) -> t.ContainerValueMapping:
                """Set bookmark value for a stream.

                Args:
                state: Complete state dictionary
                stream_name: Name of the stream
                bookmark_key: Bookmark key
                bookmark_value: Bookmark value

                Returns:
                t.ContainerValueMapping: Updated state

                """
                state_copy: t.MutableContainerValueMapping = dict(state)
                if "bookmarks" not in state_copy:
                    empty_bookmarks: t.MutableContainerValueMapping = {}
                    state_copy["bookmarks"] = empty_bookmarks
                bookmarks = state_copy["bookmarks"]
                bookmark_map = FlextTapOracleOicUtilities._as_map(bookmarks)
                if bookmark_map is not None:
                    updated_bookmark_map = dict(bookmark_map)
                    if stream_name not in updated_bookmark_map:
                        empty_stream_bookmarks: MutableMapping[
                            str, t.ContainerValue
                        ] = {}
                        updated_bookmark_map[stream_name] = empty_stream_bookmarks
                    stream_bookmarks = FlextTapOracleOicUtilities._as_map(
                        updated_bookmark_map[stream_name],
                    )
                    if stream_bookmarks is not None:
                        updated_stream_bookmarks = dict(stream_bookmarks)
                        updated_stream_bookmarks[bookmark_key] = bookmark_value
                        updated_bookmark_map[stream_name] = updated_stream_bookmarks
                        state_copy["bookmarks"] = updated_bookmark_map
                return state_copy

            @staticmethod
            def set_stream_state(
                state: Mapping[str, t.ContainerValueMapping],
                stream_name: str,
                stream_state: Mapping[str, t.ContainerValueMapping],
            ) -> t.ContainerValueMapping:
                """Set state for a specific stream.

                Args:
                state: Complete state dictionary
                stream_name: Name of the stream
                stream_state: State data for the stream

                Returns:
                t.ContainerValueMapping: Updated state

                """
                state_copy: t.MutableContainerValueMapping = dict(state)
                if "bookmarks" not in state_copy:
                    empty_bookmarks: t.MutableContainerValueMapping = {}
                    state_copy["bookmarks"] = empty_bookmarks
                bookmarks = state_copy["bookmarks"]
                bookmark_map = FlextTapOracleOicUtilities._as_map(bookmarks)
                if bookmark_map is not None:
                    updated_bookmark_map = dict(bookmark_map)
                    updated_bookmark_map[stream_name] = dict(stream_state)
                    state_copy["bookmarks"] = updated_bookmark_map
                return state_copy

            @staticmethod
            def update_pagination_bookmark(
                state: Mapping[str, t.ContainerValueMapping],
                stream_name: str,
                pagination_info: Mapping[str, t.ContainerValueMapping],
            ) -> t.ContainerValueMapping:
                """Update pagination bookmark for stream.

                Args:
                state: Complete state dictionary
                stream_name: Name of the stream
                pagination_info: Pagination information

                Returns:
                t.ContainerValueMapping: Updated state

                """
                offset = pagination_info.get("offset", 0)
                page_size = pagination_info.get("current_page_size", 0)
                try:
                    offset_val = t.STRICT_INT_ADAPTER.validate_python(offset)
                    page_size_val = t.STRICT_INT_ADAPTER.validate_python(page_size)
                except c.ValidationError as e:
                    msg = f"Invalid pagination parameters: offset={offset}, size={page_size}"
                    raise ValueError(msg) from e
                return FlextTapOracleOicUtilities.TapOracleOic.StateManagement.set_bookmark(
                    state,
                    stream_name,
                    "pagination_offset",
                    offset_val + page_size_val,
                )

        class PerformanceUtilities:
            """Performance optimization utilities for OIC operations."""

            @staticmethod
            def calculate_optimal_page_size(
                total_records: int,
                target_requests: int = 10,
            ) -> int:
                """Calculate optimal page size for OIC API requests.

                Args:
                total_records: Total number of records to fetch
                target_requests: Target number of API requests

                Returns:
                int: Optimal page size

                """
                if total_records <= 0:
                    return FlextTapOracleOicUtilities.DEFAULT_PAGE_SIZE
                calculated_size = max(1, total_records // target_requests)
                return min(calculated_size, 1000)

            @staticmethod
            def estimate_extraction_time(
                record_count: int,
                records_per_second: float = 10.0,
            ) -> t.ContainerValueMapping:
                """Estimate extraction time for OIC data.

                Args:
                record_count: Number of records to extract
                records_per_second: Processing rate

                Returns:
                t.ContainerValueMapping: Time estimation

                """
                if record_count <= 0:
                    return {"estimated_seconds": 0, "estimated_minutes": 0}
                estimated_seconds = record_count / max(records_per_second, 1.0)
                estimated_minutes = estimated_seconds / 60
                return {
                    "estimated_seconds": round(estimated_seconds, 2),
                    "estimated_minutes": round(estimated_minutes, 2),
                    "record_count": record_count,
                    "rate_per_second": records_per_second,
                }


u = FlextTapOracleOicUtilities

__all__: list[str] = ["FlextTapOracleOicUtilities", "u"]
