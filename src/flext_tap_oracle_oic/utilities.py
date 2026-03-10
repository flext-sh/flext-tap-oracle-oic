"""Singer tap utilities for Oracle OIC (Oracle Integration Cloud) operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import re
from collections.abc import Mapping
from datetime import UTC, datetime
from typing import ClassVar, override
from urllib.parse import urljoin, urlparse

from flext_core import FlextResult, t
from flext_meltano import FlextMeltanoUtilities, m
from flext_oracle_oic import FlextOracleOicUtilities
from pydantic import ConfigDict, TypeAdapter, ValidationError

from flext_tap_oracle_oic.constants import FlextTapOracleOicConstants

_STRICT_LIST_ADAPTER = TypeAdapter(
    list[t.ContainerValue], config=ConfigDict(strict=True)
)
_STRICT_MAP_ADAPTER = TypeAdapter(
    dict[str, t.ContainerValue], config=ConfigDict(strict=True)
)
_STRICT_INT_ADAPTER = TypeAdapter(int, config=ConfigDict(strict=True))


def _as_list(value: t.ContainerValue) -> list[t.ContainerValue] | None:
    """Strict list validation via Pydantic adapter."""
    try:
        return _STRICT_LIST_ADAPTER.validate_python(value)
    except ValidationError:
        return None


def _as_map(value: t.ContainerValue) -> Mapping[str, t.ContainerValue] | None:
    """Strict map validation via Pydantic adapter."""
    try:
        return _STRICT_MAP_ADAPTER.validate_python(value)
    except ValidationError:
        return None


def _as_int(value: t.ContainerValue) -> int | None:
    """Strict integer validation via Pydantic adapter."""
    try:
        return _STRICT_INT_ADAPTER.validate_python(value)
    except ValidationError:
        return None


def _coerce_int(value: t.ContainerValue) -> int:
    """Coerce potentially numeric values to integer with safe fallback."""
    try:
        return int(str(value))
    except (TypeError, ValueError):
        return 0


class FlextTapOracleOicUtilities(FlextMeltanoUtilities, FlextOracleOicUtilities):
    """Single unified utilities class for Singer tap Oracle OIC operations.

    Follows FLEXT unified class pattern with nested helper classes for
    domain-specific Singer tap functionality with Oracle Integration Cloud.
    Extends ucific operations.
    """

    DEFAULT_BATCH_SIZE: ClassVar[int] = 100
    DEFAULT_TIMEOUT: ClassVar[int] = 30
    MAX_RETRIES: ClassVar[int] = 3
    DEFAULT_PAGE_SIZE: ClassVar[int] = 50

    @override
    def __init__(self) -> None:
        """Initialize Oracle OIC tap utilities."""
        super().__init__()

    class TapOracleOic:
        """Singer protocol utilities for OIC tap operations."""

        @staticmethod
        def create_record_message(
            stream_name: str,
            record: Mapping[str, t.JsonValue],
            time_extracted: datetime | None = None,
        ) -> m.Meltano.SingerRecordMessage:
            """Create Singer record message.

            Args:
            stream_name: Name of the stream
            record: Record data
            time_extracted: Timestamp when record was extracted

            Returns:
            dict[str, t.ContainerValue]: Singer record message

            """
            extracted_time = time_extracted or datetime.now(UTC)
            return m.Meltano.SingerRecordMessage(
                stream=stream_name,
                record=dict(record),
                time_extracted=extracted_time.isoformat(),
            )

        @staticmethod
        def create_schema_message(
            stream_name: str,
            schema: Mapping[str, t.JsonValue],
            key_properties: list[str] | None = None,
        ) -> m.Meltano.SingerSchemaMessage:
            """Create Singer schema message.

            Args:
            stream_name: Name of the stream
            schema: JSON schema for the stream
            key_properties: List of key property names

            Returns:
            dict[str, t.ContainerValue]: Singer schema message

            """
            return m.Meltano.SingerSchemaMessage(
                stream=stream_name,
                schema=dict(schema),
                key_properties=key_properties or [],
            )

        @staticmethod
        def create_state_message(
            state: Mapping[str, t.ContainerValue],
        ) -> m.Meltano.SingerStateMessage:
            """Create Singer state message.

            Args:
            state: State data

            Returns:
            dict[str, t.ContainerValue]: Singer state message

            """
            return m.Meltano.SingerStateMessage(value=dict(state))

        @staticmethod
        def write_message(
            message: m.Meltano.SingerSchemaMessage
            | m.Meltano.SingerRecordMessage
            | m.Meltano.SingerStateMessage,
        ) -> None:
            """Write Singer message to stdout.

            Args:
            message: Singer message to write

            """

    class OicApiProcessing:
        """Oracle OIC API processing utilities."""

        @staticmethod
        def build_oic_api_url(
            base_url: str,
            resource_path: str,
            query_params: Mapping[str, str] | None = None,
        ) -> FlextResult[str]:
            """Build Oracle OIC API URL with proper formatting.

            Args:
            base_url: Base OIC URL
            resource_path: API resource path
            query_params: Optional query parameters

            Returns:
            FlextResult[str]: Complete API URL or error

            """
            try:
                validation_result = (
                    FlextTapOracleOicUtilities.OicApiProcessing.validate_oic_endpoint(
                        base_url
                    )
                )
                if validation_result.is_failure:
                    return FlextResult[str].fail(
                        f"Base URL validation failed: {validation_result.error}"
                    )
                if not resource_path.startswith("/"):
                    resource_path = f"/{resource_path}"
                api_url = urljoin(base_url, resource_path)
                if query_params:
                    query_string = "&".join(
                        (f"{k}={v}" for k, v in query_params.items())
                    )
                    api_url = f"{api_url}?{query_string}"
                return FlextResult[str].ok(api_url)
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ) as e:
                return FlextResult[str].fail(f"URL building error: {e}")

        @staticmethod
        def extract_pagination_info(
            response: Mapping[str, t.ContainerValue] | None,
        ) -> Mapping[str, t.ContainerValue]:
            """Extract pagination information from OIC response.

            Args:
            response: OIC API response

            Returns:
            dict[str, t.ContainerValue]: Pagination information

            """
            if not response:
                return {
                    "has_more": False,
                    "limit": FlextTapOracleOicUtilities.DEFAULT_PAGE_SIZE,
                    "offset": 0,
                    "total_count": 0,
                    "current_page_size": 0,
                }
            items = response.get("items", [])
            items_list_raw = _as_list(items)
            items_list: list[t.ContainerValue] = (
                items_list_raw if items_list_raw is not None else []
            )
            return {
                "has_more": response.get("hasMore", False),
                "limit": response.get(
                    "limit", FlextTapOracleOicUtilities.DEFAULT_PAGE_SIZE
                ),
                "offset": response.get("offset", 0),
                "total_count": response.get("count", 0),
                "current_page_size": len(items_list),
            }

        @staticmethod
        def parse_oic_response(
            response_data: Mapping[str, t.ContainerValue],
        ) -> FlextResult[Mapping[str, t.ContainerValue]]:
            """Parse Oracle OIC API response.

            Args:
            response_data: Raw API response data

            Returns:
            FlextResult[dict[str, t.ContainerValue]]: Parsed response or error

            """
            if not response_data:
                return FlextResult[t.ConfigurationMapping].fail(
                    "Response data cannot be empty"
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
                return FlextResult[t.ConfigurationMapping].ok(parsed_response)
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ) as e:
                return FlextResult[t.ConfigurationMapping].fail(
                    f"Response parsing error: {e}"
                )

        @staticmethod
        def validate_oic_endpoint(endpoint_url: str) -> FlextResult[str]:
            """Validate Oracle OIC endpoint URL.

            Args:
            endpoint_url: OIC endpoint URL

            Returns:
            FlextResult[str]: Validated URL or error

            """
            if not endpoint_url:
                return FlextResult[str].fail("OIC endpoint URL cannot be empty")
            try:
                parsed = urlparse(endpoint_url)
                if not parsed.scheme or not parsed.netloc:
                    return FlextResult[str].fail("Invalid URL format")
                if "oic" not in parsed.netloc.lower():
                    return FlextResult[str].fail(
                        "URL does not appear to be an OIC endpoint"
                    )
                return FlextResult[str].ok(endpoint_url)
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ) as e:
                return FlextResult[str].fail(f"URL validation error: {e}")

    class OicDataProcessing:
        """Oracle OIC data processing utilities."""

        @staticmethod
        def extract_integration_metadata(
            integration_data: Mapping[str, t.ContainerValue] | None,
        ) -> Mapping[str, t.ContainerValue]:
            """Extract metadata from Oracle OIC integration data.

            Args:
            integration_data: Raw integration data

            Returns:
            dict[str, t.ContainerValue]: Extracted metadata

            """
            if not integration_data:
                return {}
            metadata = {
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
            connection_list = _as_list(connections)
            if connection_list is None:
                connection_list = list[t.ContainerValue]()
            metadata["connection_count"] = len(connection_list)
            metadata["connection_types"] = [
                conn_map.get("connectionType")
                if (conn_map := _as_map(conn)) is not None
                else None
                for conn in connection_list
            ]
            return metadata

        @staticmethod
        def format_oic_timestamp(timestamp_str: str) -> FlextResult[str]:
            """Format Oracle OIC timestamp to ISO format.

            Args:
            timestamp_str: OIC timestamp string

            Returns:
            FlextResult[str]: ISO formatted timestamp or error

            """
            if not timestamp_str:
                return FlextResult[str].fail("Timestamp string cannot be empty")
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
                        return FlextResult[str].ok(dt.isoformat())
                    except ValueError:
                        continue
                return FlextResult[str].fail(
                    f"Unsupported timestamp format: {timestamp_str}"
                )
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ) as e:
                return FlextResult[str].fail(f"Timestamp formatting error: {e}")

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
            config: Mapping[str, t.ContainerValue],
        ) -> FlextResult[Mapping[str, t.ContainerValue]]:
            """Validate Oracle OIC connection configuration.

            Args:
            config: Configuration dictionary

            Returns:
            FlextResult[dict[str, t.ContainerValue]]: Validated config or error

            """
            required_fields = ["oic_base_url", "username", "password"]
            missing_fields = [field for field in required_fields if field not in config]
            if missing_fields:
                return FlextResult[t.ConfigurationMapping].fail(
                    f"Missing required fields: {', '.join(missing_fields)}"
                )
            url_validation = (
                FlextTapOracleOicUtilities.OicApiProcessing.validate_oic_endpoint(
                    str(config["oic_base_url"])
                )
            )
            if url_validation.is_failure:
                return FlextResult[t.ConfigurationMapping].fail(
                    f"Invalid OIC URL: {url_validation.error}"
                )
            if not str(config["username"]).strip():
                return FlextResult[t.ConfigurationMapping].fail(
                    "Username cannot be empty"
                )
            if not str(config["password"]).strip():
                return FlextResult[t.ConfigurationMapping].fail(
                    "Password cannot be empty"
                )
            if "timeout" in config:
                timeout = _as_int(config["timeout"])
                if timeout is None or timeout <= 0:
                    return FlextResult[t.ConfigurationMapping].fail(
                        "Timeout must be a positive integer"
                    )
            return FlextResult[t.ConfigurationMapping].ok(config)

        @staticmethod
        def validate_stream_config(
            config: Mapping[str, t.ContainerValue],
        ) -> FlextResult[Mapping[str, t.ContainerValue]]:
            """Validate OIC tap stream configuration.

            Args:
            config: Stream configuration

            Returns:
            FlextResult[dict[str, t.ContainerValue]]: Validated config or error

            """
            if "streams" not in config:
                return FlextResult[t.ConfigurationMapping].fail(
                    "Configuration must include 'streams' section"
                )
            streams = config["streams"]
            stream_map = _as_map(streams)
            if stream_map is None:
                return FlextResult[t.ConfigurationMapping].fail(
                    "Streams configuration must be a dictionary"
                )
            for stream_name, stream_payload in stream_map.items():
                stream_config = _as_map(stream_payload)
                if stream_config is None:
                    return FlextResult[t.ConfigurationMapping].fail(
                        f"Stream '{stream_name}' configuration must be a dictionary"
                    )
                if "selected" not in stream_config:
                    return FlextResult[t.ConfigurationMapping].fail(
                        f"Stream '{stream_name}' must have 'selected' field"
                    )
                if "page_size" in stream_config:
                    page_size = _as_int(stream_config["page_size"])
                    max_page_size = (
                        FlextTapOracleOicConstants.TapOicProcessing.MAX_PAGE_SIZE
                    )
                    if page_size is None or page_size <= 0 or page_size > max_page_size:
                        return FlextResult[t.ConfigurationMapping].fail(
                            f"Stream '{stream_name}' page_size must be between 1 and {max_page_size}"
                        )
            return FlextResult[t.ConfigurationMapping].ok(config)

    class StateManagement:
        """State management utilities for incremental syncs."""

        @staticmethod
        def get_bookmark(
            state: Mapping[str, t.ContainerValue], stream_name: str, bookmark_key: str
        ) -> t.ContainerValue:
            """Get bookmark value for a stream.

            Args:
            state: Complete state dictionary
            stream_name: Name of the stream
            bookmark_key: Bookmark key

            Returns:
            object: Bookmark value or None

            """
            stream_state = FlextTapOracleOicUtilities.StateManagement.get_stream_state(
                state, stream_name
            )
            return stream_state.get(bookmark_key)

        @staticmethod
        def get_stream_state(
            state: Mapping[str, t.ContainerValue], stream_name: str
        ) -> Mapping[str, t.ContainerValue]:
            """Get state for a specific stream.

            Args:
            state: Complete state dictionary
            stream_name: Name of the stream

            Returns:
            dict[str, t.ContainerValue]: Stream state

            """
            bookmarks = state.get("bookmarks", {})
            bookmark_map = _as_map(bookmarks)
            if bookmark_map is None:
                return {}
            stream_bookmarks = _as_map(bookmark_map.get(stream_name, {}))
            return stream_bookmarks if stream_bookmarks is not None else {}

        @staticmethod
        def set_bookmark(
            state: Mapping[str, t.ContainerValue],
            stream_name: str,
            bookmark_key: str,
            bookmark_value: t.ContainerValue,
        ) -> Mapping[str, t.ContainerValue]:
            """Set bookmark value for a stream.

            Args:
            state: Complete state dictionary
            stream_name: Name of the stream
            bookmark_key: Bookmark key
            bookmark_value: Bookmark value

            Returns:
            dict[str, t.ContainerValue]: Updated state

            """
            state_copy: dict[str, t.ContainerValue] = dict(state)
            if "bookmarks" not in state_copy:
                state_copy["bookmarks"] = {}
            bookmarks = state_copy["bookmarks"]
            bookmark_map = _as_map(bookmarks)
            if bookmark_map is not None:
                updated_bookmark_map = dict(bookmark_map)
                if stream_name not in updated_bookmark_map:
                    updated_bookmark_map[stream_name] = {}
                stream_bookmarks = _as_map(updated_bookmark_map[stream_name])
                if stream_bookmarks is not None:
                    updated_stream_bookmarks = dict(stream_bookmarks)
                    updated_stream_bookmarks[bookmark_key] = bookmark_value
                    updated_bookmark_map[stream_name] = updated_stream_bookmarks
                    state_copy["bookmarks"] = updated_bookmark_map
            return state_copy

        @staticmethod
        def set_stream_state(
            state: Mapping[str, t.ContainerValue],
            stream_name: str,
            stream_state: Mapping[str, t.ContainerValue],
        ) -> Mapping[str, t.ContainerValue]:
            """Set state for a specific stream.

            Args:
            state: Complete state dictionary
            stream_name: Name of the stream
            stream_state: State data for the stream

            Returns:
            dict[str, t.ContainerValue]: Updated state

            """
            state_copy: dict[str, t.ContainerValue] = dict(state)
            if "bookmarks" not in state_copy:
                state_copy["bookmarks"] = {}
            bookmarks = state_copy["bookmarks"]
            bookmark_map = _as_map(bookmarks)
            if bookmark_map is not None:
                updated_bookmark_map = dict(bookmark_map)
                updated_bookmark_map[stream_name] = dict(stream_state)
                state_copy["bookmarks"] = updated_bookmark_map
            return state_copy

        @staticmethod
        def update_pagination_bookmark(
            state: Mapping[str, t.ContainerValue],
            stream_name: str,
            pagination_info: Mapping[str, t.ContainerValue],
        ) -> Mapping[str, t.ContainerValue]:
            """Update pagination bookmark for stream.

            Args:
            state: Complete state dictionary
            stream_name: Name of the stream
            pagination_info: Pagination information

            Returns:
            dict[str, t.ContainerValue]: Updated state

            """
            offset = pagination_info.get("offset", 0)
            page_size = pagination_info.get("current_page_size", 0)
            try:
                offset_val = _coerce_int(offset)
                page_size_val = _coerce_int(page_size)
            except (ValueError, TypeError):
                offset_val = 0
                page_size_val = 0
            return FlextTapOracleOicUtilities.StateManagement.set_bookmark(
                state, stream_name, "pagination_offset", offset_val + page_size_val
            )

    class PerformanceUtilities:
        """Performance optimization utilities for OIC operations."""

        @staticmethod
        def calculate_optimal_page_size(
            total_records: int, target_requests: int = 10
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
            record_count: int, records_per_second: float = 10.0
        ) -> Mapping[str, t.ContainerValue]:
            """Estimate extraction time for OIC data.

            Args:
            record_count: Number of records to extract
            records_per_second: Processing rate

            Returns:
            dict[str, t.ContainerValue]: Time estimation

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

    @classmethod
    def build_oic_api_url(
        cls,
        base_url: str,
        resource_path: str,
        query_params: Mapping[str, str] | None = None,
    ) -> FlextResult[str]:
        """Proxy method for OicApiProcessing.build_oic_api_url()."""
        return FlextTapOracleOicUtilities.OicApiProcessing.build_oic_api_url(
            base_url, resource_path, query_params
        )

    @classmethod
    def create_record_message(
        cls,
        stream_name: str,
        record: Mapping[str, t.JsonValue],
        time_extracted: datetime | None = None,
    ) -> m.Meltano.SingerRecordMessage:
        """Proxy method for SingerUtilities.create_record_message()."""
        return FlextTapOracleOicUtilities.TapOracleOic.create_record_message(
            stream_name, record, time_extracted
        )

    @classmethod
    def create_schema_message(
        cls,
        stream_name: str,
        schema: Mapping[str, t.JsonValue],
        key_properties: list[str] | None = None,
    ) -> m.Meltano.SingerSchemaMessage:
        """Proxy method for SingerUtilities.create_schema_message()."""
        return FlextTapOracleOicUtilities.TapOracleOic.create_schema_message(
            stream_name, schema, key_properties
        )

    @classmethod
    def format_oic_timestamp(cls, timestamp_str: str) -> FlextResult[str]:
        """Proxy method for OicDataProcessing.format_oic_timestamp()."""
        return FlextTapOracleOicUtilities.OicDataProcessing.format_oic_timestamp(
            timestamp_str
        )

    @classmethod
    def get_stream_state(
        cls, state: Mapping[str, t.ContainerValue], stream_name: str
    ) -> Mapping[str, t.ContainerValue]:
        """Proxy method for StateManagement.get_stream_state()."""
        return FlextTapOracleOicUtilities.StateManagement.get_stream_state(
            state, stream_name
        )

    @classmethod
    def normalize_integration_name(cls, integration_name: str) -> str:
        """Proxy method for OicDataProcessing.normalize_integration_name()."""
        return FlextTapOracleOicUtilities.OicDataProcessing.normalize_integration_name(
            integration_name
        )

    @classmethod
    def set_bookmark(
        cls,
        state: Mapping[str, t.ContainerValue],
        stream_name: str,
        bookmark_key: str,
        bookmark_value: t.ContainerValue,
    ) -> Mapping[str, t.ContainerValue]:
        """Proxy method for StateManagement.set_bookmark()."""
        return FlextTapOracleOicUtilities.StateManagement.set_bookmark(
            state, stream_name, bookmark_key, bookmark_value
        )

    @classmethod
    def validate_oic_connection_config(
        cls, config: Mapping[str, t.ContainerValue]
    ) -> FlextResult[Mapping[str, t.ContainerValue]]:
        """Proxy method for ConfigValidation.validate_oic_connection_config()."""
        return (
            FlextTapOracleOicUtilities.ConfigValidation.validate_oic_connection_config(
                config
            )
        )

    @classmethod
    def validate_oic_endpoint(cls, endpoint_url: str) -> FlextResult[str]:
        """Proxy method for OicApiProcessing.validate_oic_endpoint()."""
        return FlextTapOracleOicUtilities.OicApiProcessing.validate_oic_endpoint(
            endpoint_url
        )


u = FlextTapOracleOicUtilities
__all__ = ["FlextTapOracleOicUtilities", "u"]
