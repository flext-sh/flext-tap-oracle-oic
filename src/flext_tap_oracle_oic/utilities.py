"""Singer tap utilities for Oracle OIC (Oracle Integration Cloud) operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING
from urllib.parse import urljoin, urlparse

from flext_meltano import FlextMeltanoUtilities
from flext_oracle_oic import u
from flext_tap_oracle_oic import c, p, r, t

if TYPE_CHECKING:
    from collections.abc import (
        MutableMapping,
    )


class FlextTapOracleOicUtilities(u, FlextMeltanoUtilities):
    """Single unified utilities class for Singer tap Oracle OIC operations.

    Follows FLEXT unified class pattern with nested helper classes for
    domain-specific Singer tap functionality with Oracle Integration Cloud.
    Extends ucific operations.
    """

    class TapOracleOic:
        """Tap Oracle OIC-specific utility namespace."""

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

            def _run_build_oic_api_url() -> p.Result[str]:
                validation_result = (
                    FlextTapOracleOicUtilities.TapOracleOic.validate_oic_endpoint(
                        base_url,
                    )
                )
                if validation_result.failure:
                    return r[str].fail_op(
                        "Base URL validation",
                        validation_result.error,
                    )
                normalized_path = (
                    resource_path
                    if resource_path.startswith("/")
                    else f"/{resource_path}"
                )
                api_url = urljoin(base_url, normalized_path)
                if query_params:
                    query_string = "&".join(
                        (f"{k}={v}" for k, v in query_params.items()),
                    )
                    api_url = f"{api_url}?{query_string}"
                return r[str].ok(api_url)

            try:
                return _run_build_oic_api_url()
            except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
                return r[str].fail(f"URL building error: {e}")

        @staticmethod
        def extract_pagination_info(
            response: t.JsonMapping | None,
        ) -> t.JsonMapping:
            """Extract pagination information from OIC response.

            Args:
            response: OIC API response

            Returns:
            t.JsonMapping: Pagination information

            """
            if not response:
                return {
                    "has_more": False,
                    "limit": c.DEFAULT_PAGE_SIZE,
                    "offset": 0,
                    "total_count": 0,
                    "current_page_size": 0,
                }
            items_value = response.get("items")
            try:
                items_list = t.strict_json_list_adapter().validate_python(
                    items_value if items_value is not None else [],
                )
            except c.ValidationError:
                items_list = t.strict_json_list_adapter().validate_python([])
            return t.json_mapping_adapter().validate_python({
                "has_more": response.get("hasMore", False),
                "limit": response.get(
                    "limit",
                    c.DEFAULT_PAGE_SIZE,
                ),
                "offset": response.get("offset", 0),
                "total_count": response.get("count", 0),
                "current_page_size": len(items_list),
            })

        @staticmethod
        def parse_oic_response(
            response_data: t.JsonMapping,
        ) -> p.Result[t.JsonMapping]:
            """Parse Oracle OIC API response.

            Args:
            response_data: Raw API response data

            Returns:
            r[t.JsonMapping]: Parsed response or error

            """
            if not response_data:
                return r[t.JsonMapping].fail(
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
                return r[t.JsonMapping].ok(parsed_response)
            except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
                return r[t.JsonMapping].fail(
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

        @staticmethod
        def extract_integration_metadata(
            integration_data: t.JsonMapping | None,
        ) -> t.JsonMapping:
            """Extract metadata from Oracle OIC integration data.

            Args:
            integration_data: Raw integration data

            Returns:
            t.JsonMapping: Extracted metadata

            """
            if not integration_data:
                return t.json_mapping_adapter().validate_python({})
            metadata: MutableMapping[str, t.JsonValue | None] = {
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
            try:
                connection_list = t.strict_json_list_adapter().validate_python(
                    connections,
                )
            except c.ValidationError:
                connection_list = t.strict_json_list_adapter().validate_python(
                    [],
                )
            metadata["connection_count"] = len(connection_list)
            connection_types: list[str] = []
            for conn in connection_list:
                try:
                    conn_map = t.strict_json_mapping_adapter().validate_python(conn)
                except c.ValidationError:
                    continue
                connection_type = conn_map.get("connectionType")
                if connection_type is not None:
                    connection_types.append(str(connection_type))
            connection_types_payload: t.JsonValueList = list(connection_types)
            metadata["connection_types"] = connection_types_payload
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
            normalized = c.TapOracleOic.NORMALIZE_NON_ALNUM_RE.sub(
                "_",
                integration_name.lower(),
            )
            normalized = c.TapOracleOic.NORMALIZE_REPEATED_UNDERSCORE_RE.sub(
                "_",
                normalized,
            )
            stripped: str = normalized.strip("_")
            return stripped

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
            sanitized = c.TapOracleOic.SANITIZE_CAMEL_BOUNDARY_RE.sub(
                "_",
                field_name,
            ).lower()
            sanitized = c.TapOracleOic.SANITIZE_NON_IDENTIFIER_RE.sub("_", sanitized)
            sanitized = c.TapOracleOic.NORMALIZE_REPEATED_UNDERSCORE_RE.sub(
                "_",
                sanitized,
            )
            if sanitized and sanitized[0].isdigit():
                sanitized = f"field_{sanitized}"
            stripped: str = sanitized.strip("_")
            return stripped

        @staticmethod
        def validate_oic_connection_config(
            settings: t.JsonMapping,
        ) -> p.Result[t.JsonMapping]:
            """Validate Oracle OIC connection configuration.

            Args:
            settings: Configuration dictionary

            Returns:
            r[t.JsonMapping]: Validated settings or error

            """
            required_fields = ["oic_base_url", "username", "password"]
            missing_fields = [
                field for field in required_fields if field not in settings
            ]
            if missing_fields:
                return r[t.JsonMapping].fail(
                    f"Missing required fields: {', '.join(missing_fields)}",
                )
            url_validation = (
                FlextTapOracleOicUtilities.TapOracleOic.validate_oic_endpoint(
                    str(settings["oic_base_url"]),
                )
            )
            if url_validation.failure:
                return r[t.JsonMapping].fail(
                    f"Invalid OIC URL: {url_validation.error}",
                )
            if not str(settings["username"]).strip():
                return r[t.JsonMapping].fail(
                    "Username cannot be empty",
                )
            if not str(settings["password"]).strip():
                return r[t.JsonMapping].fail(
                    "Password cannot be empty",
                )
            if "timeout" in settings:
                try:
                    timeout = t.int_adapter().validate_python(
                        settings["timeout"],
                    )
                except c.ValidationError:
                    timeout = None
                if timeout is None or timeout <= 0:
                    return r[t.JsonMapping].fail(
                        "Timeout must be a positive integer",
                    )
            return r[t.JsonMapping].ok(
                t.json_mapping_adapter().validate_python(settings),
            )

        @staticmethod
        def validate_stream_config(
            settings: t.JsonMapping,
        ) -> p.Result[t.JsonMapping]:
            """Validate OIC tap stream configuration.

            Args:
            settings: Stream configuration

            Returns:
            r[t.JsonMapping]: Validated settings or error

            """
            if "streams" not in settings:
                return r[t.JsonMapping].fail(
                    "Configuration must include 'streams' section",
                )
            streams = settings["streams"]
            try:
                stream_map = t.strict_json_mapping_adapter().validate_python(streams)
            except c.ValidationError:
                return r[t.JsonMapping].fail(
                    "Streams configuration must be a dictionary",
                )
            for stream_name, stream_payload in stream_map.items():
                try:
                    stream_config = t.strict_json_mapping_adapter().validate_python(
                        stream_payload,
                    )
                except c.ValidationError:
                    return r[t.JsonMapping].fail(
                        f"Stream '{stream_name}' configuration must be a dictionary",
                    )
                if "selected" not in stream_config:
                    return r[t.JsonMapping].fail(
                        f"Stream '{stream_name}' must have 'selected' field",
                    )
                if "page_size" in stream_config:
                    try:
                        page_size = t.int_adapter().validate_python(
                            stream_config["page_size"],
                        )
                    except c.ValidationError:
                        page_size = None
                    max_page_size = c.MAX_PAGE_SIZE
                    if page_size is None or page_size <= 0 or page_size > max_page_size:
                        return r[t.JsonMapping].fail(
                            f"Stream '{stream_name}' page_size must be between 1 and {max_page_size}",
                        )
            return r[t.JsonMapping].ok(
                t.json_mapping_adapter().validate_python(settings),
            )

        @staticmethod
        def get_bookmark(
            state: t.JsonMapping,
            stream_name: str,
            bookmark_key: str,
        ) -> t.JsonValue | None:
            """Get bookmark value for a stream.

            Args:
            state: Complete state dictionary
            stream_name: Name of the stream
            bookmark_key: Bookmark key

            Returns:
            t.JsonValue: Bookmark value or None

            """
            stream_state = FlextTapOracleOicUtilities.TapOracleOic.get_stream_state(
                state,
                stream_name,
            )
            return stream_state.get(bookmark_key)

        @staticmethod
        def state_map(state: t.JsonMapping) -> t.JsonMapping:
            """Normalize full state payload to canonical mapping contract."""
            return t.json_mapping_adapter().validate_python(state)

        @staticmethod
        def bookmarks_map(state_map: t.JsonMapping) -> t.JsonMapping:
            """Normalize bookmarks branch from canonical state payload."""
            return t.json_mapping_adapter().validate_python(
                state_map.get("bookmarks", {}),
            )

        @staticmethod
        def get_stream_state(
            state: t.JsonMapping,
            stream_name: str,
        ) -> t.JsonMapping:
            """Get state for a specific stream.

            Args:
            state: Complete state dictionary
            stream_name: Name of the stream

            Returns:
            t.JsonMapping: Stream state

            """
            state_map = FlextTapOracleOicUtilities.TapOracleOic.state_map(state)
            bookmarks = FlextTapOracleOicUtilities.TapOracleOic.bookmarks_map(
                state_map,
            )
            return t.json_mapping_adapter().validate_python(
                bookmarks.get(stream_name, {}),
            )

        @staticmethod
        def set_bookmark(
            state: t.JsonMapping,
            stream_name: str,
            bookmark_key: str,
            bookmark_value: t.JsonValue,
        ) -> t.JsonMapping:
            """Set bookmark value for a stream.

            Args:
            state: Complete state dictionary
            stream_name: Name of the stream
            bookmark_key: Bookmark key
            bookmark_value: Bookmark value

            Returns:
            t.JsonMapping: Updated state

            """
            state_map = FlextTapOracleOicUtilities.TapOracleOic.state_map(
                state,
            )
            bookmarks = FlextTapOracleOicUtilities.TapOracleOic.bookmarks_map(
                state_map,
            )
            stream_bookmarks = t.json_mapping_adapter().validate_python(
                bookmarks.get(stream_name, {}),
            )
            updated_stream_bookmarks: t.JsonMapping = {
                **stream_bookmarks,
                bookmark_key: bookmark_value,
            }
            updated_bookmarks = t.json_mapping_adapter().validate_python({
                **bookmarks,
                stream_name: updated_stream_bookmarks,
            })
            return t.json_mapping_adapter().validate_python({
                **state_map,
                "bookmarks": updated_bookmarks,
            })

        @staticmethod
        def set_stream_state(
            state: t.JsonMapping,
            stream_name: str,
            stream_state: t.JsonMapping,
        ) -> t.JsonMapping:
            """Set state for a specific stream.

            Args:
            state: Complete state dictionary
            stream_name: Name of the stream
            stream_state: State data for the stream

            Returns:
            t.JsonMapping: Updated state

            """
            state_map = FlextTapOracleOicUtilities.TapOracleOic.state_map(
                state,
            )
            bookmarks = FlextTapOracleOicUtilities.TapOracleOic.bookmarks_map(
                state_map,
            )
            normalized_stream_state = t.json_mapping_adapter().validate_python(
                stream_state,
            )
            updated_bookmarks = t.json_mapping_adapter().validate_python({
                **bookmarks,
                stream_name: normalized_stream_state,
            })
            return t.json_mapping_adapter().validate_python({
                **state_map,
                "bookmarks": updated_bookmarks,
            })

        @staticmethod
        def update_pagination_bookmark(
            state: t.JsonMapping,
            stream_name: str,
            pagination_info: t.JsonMapping,
        ) -> t.JsonMapping:
            """Update pagination bookmark for stream.

            Args:
            state: Complete state dictionary
            stream_name: Name of the stream
            pagination_info: Pagination information

            Returns:
            t.JsonMapping: Updated state

            """
            offset = pagination_info.get("offset", 0)
            page_size = pagination_info.get("current_page_size", 0)
            try:
                offset_val = t.int_adapter().validate_python(offset)
                page_size_val = t.int_adapter().validate_python(
                    page_size,
                )
            except c.ValidationError as e:
                msg = (
                    f"Invalid pagination parameters: offset={offset}, size={page_size}"
                )
                raise ValueError(msg) from e
            return FlextTapOracleOicUtilities.TapOracleOic.set_bookmark(
                state,
                stream_name,
                "pagination_offset",
                offset_val + page_size_val,
            )

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
                return c.DEFAULT_PAGE_SIZE
            calculated_size = max(1, total_records // target_requests)
            return min(calculated_size, 1000)

        @staticmethod
        def estimate_extraction_time(
            record_count: int,
            records_per_second: float = 10.0,
        ) -> t.JsonMapping:
            """Estimate extraction time for OIC data.

            Args:
            record_count: Number of records to extract
            records_per_second: Processing rate

            Returns:
            t.JsonMapping: Time estimation

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

        @staticmethod
        def as_oic_envelope(
            value: t.JsonMapping,
        ) -> t.JsonMapping | None:
            """Return normalized envelope payload when OIC wrapper keys are present."""
            try:
                envelope = t.strict_json_mapping_adapter().validate_python(value)
            except c.ValidationError:
                return None
            return (
                envelope
                if any(
                    key in envelope for key in ("items", "data", "totalSize", "count")
                )
                else None
            )


u = FlextTapOracleOicUtilities

__all__: list[str] = ["FlextTapOracleOicUtilities", "u"]
