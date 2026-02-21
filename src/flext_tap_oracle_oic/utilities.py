"""Singer tap utilities for Oracle OIC (Oracle Integration Cloud) operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import re
from datetime import UTC, datetime
from typing import ClassVar, override
from urllib.parse import urljoin, urlparse

from flext_core import FlextResult, FlextTypes as t
from flext_core.utilities import FlextUtilities as u_core
from flext_meltano import FlextMeltanoModels as m

from flext_tap_oracle_oic.constants import FlextTapOracleOicConstants


class FlextMeltanoTapOracleOicUtilities(u_core):
    """Single unified utilities class for Singer tap Oracle OIC operations.

    Follows FLEXT unified class pattern with nested helper classes for
    domain-specific Singer tap functionality with Oracle Integration Cloud.
    Extends ucific operations.
    """

    # Configuration constants
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
        def create_schema_message(
            stream_name: str,
            schema: dict[str, t.JsonValue],
            key_properties: list[str] | None = None,
        ) -> m.Meltano.SingerSchemaMessage:
            """Create Singer schema message.

            Args:
            stream_name: Name of the stream
            schema: JSON schema for the stream
            key_properties: List of key property names

            Returns:
            dict[str, t.GeneralValueType]: Singer schema message

            """
            return m.Meltano.SingerSchemaMessage(
                stream=stream_name,
                schema=schema,
                key_properties=key_properties or [],
            )

        @staticmethod
        def create_record_message(
            stream_name: str,
            record: dict[str, t.JsonValue],
            time_extracted: datetime | None = None,
        ) -> m.Meltano.SingerRecordMessage:
            """Create Singer record message.

            Args:
            stream_name: Name of the stream
            record: Record data
            time_extracted: Timestamp when record was extracted

            Returns:
            dict[str, t.GeneralValueType]: Singer record message

            """
            extracted_time = time_extracted or datetime.now(UTC)
            return m.Meltano.SingerRecordMessage(
                stream=stream_name,
                record=record,
                time_extracted=extracted_time.isoformat(),
            )

        @staticmethod
        def create_state_message(
            state: dict[str, dict[str, str]],
        ) -> m.Meltano.SingerStateMessage:
            """Create Singer state message.

            Args:
            state: State data

            Returns:
            dict[str, t.GeneralValueType]: Singer state message

            """
            return m.Meltano.SingerStateMessage(value=state)

        @staticmethod
        def write_message(
            message: (
                m.Meltano.SingerSchemaMessage
                | m.Meltano.SingerRecordMessage
                | m.Meltano.SingerStateMessage
            ),
        ) -> None:
            """Write Singer message to stdout.

            Args:
            message: Singer message to write

            """

    class OicApiProcessing:
        """Oracle OIC API processing utilities."""

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

                # Validate OIC-specific URL patterns
                if "oic" not in parsed.netloc.lower():
                    return FlextResult[str].fail(
                        "URL does not appear to be an OIC endpoint",
                    )

                return FlextResult[str].ok(endpoint_url)

            except Exception as e:
                return FlextResult[str].fail(f"URL validation error: {e}")

        @staticmethod
        def build_oic_api_url(
            base_url: str,
            resource_path: str,
            query_params: dict[str, str] | None = None,
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
                # Validate base URL
                validation_result = FlextMeltanoTapOracleOicUtilities.OicApiProcessing.validate_oic_endpoint(
                    base_url,
                )
                if validation_result.is_failure:
                    return FlextResult[str].fail(
                        f"Base URL validation failed: {validation_result.error}",
                    )

                # Ensure resource path starts with /
                if not resource_path.startswith("/"):
                    resource_path = f"/{resource_path}"

                # Build complete URL
                api_url = urljoin(base_url, resource_path)

                # Add query parameters if provided
                if query_params:
                    query_string = "&".join(f"{k}={v}" for k, v in query_params.items())
                    api_url = f"{api_url}?{query_string}"

                return FlextResult[str].ok(api_url)

            except Exception as e:
                return FlextResult[str].fail(f"URL building error: {e}")

        @staticmethod
        def parse_oic_response(
            response_data: dict[str, t.GeneralValueType],
        ) -> FlextResult[dict[str, t.GeneralValueType]]:
            """Parse Oracle OIC API response.

            Args:
            response_data: Raw API response data

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: Parsed response or error

            """
            if not response_data:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    "Response data cannot be empty",
                )

            try:
                # Extract standard OIC response fields
                parsed_response = {
                    "items": response_data.get("items", []),
                    "count": response_data.get("count", 0),
                    "hasMore": response_data.get("hasMore", False),
                    "limit": response_data.get("limit", 0),
                    "offset": response_data.get("offset", 0),
                }

                # Handle different response formats
                if "data" in response_data:
                    parsed_response["items"] = response_data["data"]

                return FlextResult[dict[str, t.GeneralValueType]].ok(parsed_response)

            except Exception as e:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    f"Response parsing error: {e}",
                )

        @staticmethod
        def extract_pagination_info(
            response: dict[str, t.GeneralValueType] | None,
        ) -> dict[str, t.GeneralValueType]:
            """Extract pagination information from OIC response.

            Args:
            response: OIC API response

            Returns:
            dict[str, t.GeneralValueType]: Pagination information

            """
            if not response:
                return {
                    "has_more": False,
                    "limit": FlextMeltanoTapOracleOicUtilities.DEFAULT_PAGE_SIZE,
                    "offset": 0,
                    "total_count": 0,
                    "current_page_size": 0,
                }

            items = response.get("items", [])
            if not isinstance(items, list):
                items = []

            return {
                "has_more": response.get("hasMore", False),
                "limit": response.get(
                    "limit",
                    FlextMeltanoTapOracleOicUtilities.DEFAULT_PAGE_SIZE,
                ),
                "offset": response.get("offset", 0),
                "total_count": response.get("count", 0),
                "current_page_size": len(items),
            }

    class OicDataProcessing:
        """Oracle OIC data processing utilities."""

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

            # Convert to lowercase and replace spaces/special chars with underscores
            normalized = re.sub(r"[^a-zA-Z0-9]", "_", integration_name.lower())

            # Remove multiple consecutive underscores
            normalized = re.sub(r"_+", "_", normalized)

            # Remove leading/trailing underscores
            return normalized.strip("_")

        @staticmethod
        def extract_integration_metadata(
            integration_data: dict[str, t.GeneralValueType] | None,
        ) -> dict[str, t.GeneralValueType]:
            """Extract metadata from Oracle OIC integration data.

            Args:
            integration_data: Raw integration data

            Returns:
            dict[str, t.GeneralValueType]: Extracted metadata

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

            # Extract connection information
            connections = integration_data.get("connectionInstances", [])
            if not isinstance(connections, list):
                connections = []

            metadata["connection_count"] = len(connections)
            metadata["connection_types"] = [
                conn.get("connectionType") if isinstance(conn, dict) else None
                for conn in connections
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
                # Handle common OIC timestamp formats with timezone support
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
                        # Use timezone-aware parsing where possible
                        dt_naive = datetime.strptime(timestamp_str, fmt)
                        # Ensure timezone-aware (assume UTC if not specified)
                        dt = (
                            dt_naive.replace(tzinfo=UTC)
                            if dt_naive.tzinfo is None
                            else dt_naive
                        )
                        return FlextResult[str].ok(dt.isoformat())
                    except ValueError:
                        continue

                return FlextResult[str].fail(
                    f"Unsupported timestamp format: {timestamp_str}",
                )

            except Exception as e:
                return FlextResult[str].fail(f"Timestamp formatting error: {e}")

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

            # Convert camelCase to snake_case
            sanitized = re.sub(r"(?<!^)(?=[A-Z])", "_", field_name).lower()

            # Replace non-alphanumeric with underscores
            sanitized = re.sub(r"[^a-zA-Z0-9_]", "_", sanitized)

            # Remove multiple consecutive underscores
            sanitized = re.sub(r"_+", "_", sanitized)

            # Ensure it doesn't start with a number
            if sanitized and sanitized[0].isdigit():
                sanitized = f"field_{sanitized}"

            return sanitized.strip("_")

    class ConfigValidation:
        """Configuration validation utilities."""

        @staticmethod
        def validate_oic_connection_config(
            config: dict[str, t.GeneralValueType],
        ) -> FlextResult[dict[str, t.GeneralValueType]]:
            """Validate Oracle OIC connection configuration.

            Args:
            config: Configuration dictionary

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: Validated config or error

            """
            required_fields = ["oic_base_url", "username", "password"]
            missing_fields = [field for field in required_fields if field not in config]

            if missing_fields:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    f"Missing required fields: {', '.join(missing_fields)}",
                )

            # Validate OIC base URL
            url_validation = FlextMeltanoTapOracleOicUtilities.OicApiProcessing.validate_oic_endpoint(
                str(config["oic_base_url"]),
            )
            if url_validation.is_failure:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    f"Invalid OIC URL: {url_validation.error}",
                )

            # Validate credentials
            if not str(config["username"]).strip():
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    "Username cannot be empty"
                )

            if not str(config["password"]).strip():
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    "Password cannot be empty"
                )

            # Validate optional timeout
            if "timeout" in config:
                timeout = config["timeout"]
                if not isinstance(timeout, int) or timeout <= 0:
                    return FlextResult[dict[str, t.GeneralValueType]].fail(
                        "Timeout must be a positive integer",
                    )

            return FlextResult[dict[str, t.GeneralValueType]].ok(config)

        @staticmethod
        def validate_stream_config(
            config: dict[str, t.GeneralValueType],
        ) -> FlextResult[dict[str, t.GeneralValueType]]:
            """Validate OIC tap stream configuration.

            Args:
            config: Stream configuration

            Returns:
            FlextResult[dict[str, t.GeneralValueType]]: Validated config or error

            """
            if "streams" not in config:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    "Configuration must include 'streams' section",
                )

            streams = config["streams"]
            if not isinstance(streams, dict):
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    "Streams configuration must be a dictionary",
                )

            # Validate each stream
            for stream_name, stream_config in streams.items():
                if not isinstance(stream_config, dict):
                    return FlextResult[dict[str, t.GeneralValueType]].fail(
                        f"Stream '{stream_name}' configuration must be a dictionary",
                    )

                # Check for required stream fields
                if "selected" not in stream_config:
                    return FlextResult[dict[str, t.GeneralValueType]].fail(
                        f"Stream '{stream_name}' must have 'selected' field",
                    )

                # Validate page size if provided
                if "page_size" in stream_config:
                    page_size = stream_config["page_size"]

                    max_page_size = (
                        FlextTapOracleOicConstants.TapOicProcessing.MAX_PAGE_SIZE
                    )
                    if (
                        not isinstance(page_size, int)
                        or page_size <= 0
                        or page_size > max_page_size
                    ):
                        return FlextResult[dict[str, t.GeneralValueType]].fail(
                            f"Stream '{stream_name}' page_size must be between 1 and {max_page_size}",
                        )

            return FlextResult[dict[str, t.GeneralValueType]].ok(config)

    class StateManagement:
        """State management utilities for incremental syncs."""

        @staticmethod
        def get_stream_state(
            state: dict[str, t.GeneralValueType],
            stream_name: str,
        ) -> dict[str, t.GeneralValueType]:
            """Get state for a specific stream.

            Args:
            state: Complete state dictionary
            stream_name: Name of the stream

            Returns:
            dict[str, t.GeneralValueType]: Stream state

            """
            # state is guaranteed to be dict by type annotation
            bookmarks = state.get("bookmarks", {})
            if not isinstance(bookmarks, dict):
                return {}
            stream_bookmarks = bookmarks.get(stream_name, {})
            return stream_bookmarks if isinstance(stream_bookmarks, dict) else {}

        @staticmethod
        def set_stream_state(
            state: dict[str, t.GeneralValueType],
            stream_name: str,
            stream_state: dict[str, t.GeneralValueType],
        ) -> dict[str, t.GeneralValueType]:
            """Set state for a specific stream.

            Args:
            state: Complete state dictionary
            stream_name: Name of the stream
            stream_state: State data for the stream

            Returns:
            dict[str, t.GeneralValueType]: Updated state

            """
            # state is guaranteed to be dict by type annotation

            if "bookmarks" not in state:
                state["bookmarks"] = {}

            bookmarks = state["bookmarks"]
            if isinstance(bookmarks, dict):
                bookmarks[stream_name] = stream_state

            return state

        @staticmethod
        def get_bookmark(
            state: dict[str, t.GeneralValueType],
            stream_name: str,
            bookmark_key: str,
        ) -> object:
            """Get bookmark value for a stream.

            Args:
            state: Complete state dictionary
            stream_name: Name of the stream
            bookmark_key: Bookmark key

            Returns:
            object: Bookmark value or None

            """
            stream_state = (
                FlextMeltanoTapOracleOicUtilities.StateManagement.get_stream_state(
                    state,
                    stream_name,
                )
            )
            # stream_state is guaranteed to be dict by type annotation
            return stream_state.get(bookmark_key)

        @staticmethod
        def set_bookmark(
            state: dict[str, t.GeneralValueType],
            stream_name: str,
            bookmark_key: str,
            bookmark_value: object,
        ) -> dict[str, t.GeneralValueType]:
            """Set bookmark value for a stream.

            Args:
            state: Complete state dictionary
            stream_name: Name of the stream
            bookmark_key: Bookmark key
            bookmark_value: Bookmark value

            Returns:
            dict[str, t.GeneralValueType]: Updated state

            """
            # state is guaranteed to be dict by type annotation

            if "bookmarks" not in state:
                state["bookmarks"] = {}
            bookmarks = state["bookmarks"]
            if isinstance(bookmarks, dict):
                if stream_name not in bookmarks:
                    bookmarks[stream_name] = {}
                stream_bookmarks = bookmarks[stream_name]
                if isinstance(stream_bookmarks, dict):
                    stream_bookmarks[bookmark_key] = bookmark_value

            return state

        @staticmethod
        def update_pagination_bookmark(
            state: dict[str, t.GeneralValueType],
            stream_name: str,
            pagination_info: dict[str, t.GeneralValueType],
        ) -> dict[str, t.GeneralValueType]:
            """Update pagination bookmark for stream.

            Args:
            state: Complete state dictionary
            stream_name: Name of the stream
            pagination_info: Pagination information

            Returns:
            dict[str, t.GeneralValueType]: Updated state

            """
            # pagination_info is guaranteed to be dict by type annotation

            offset = pagination_info.get("offset", 0)
            page_size = pagination_info.get("current_page_size", 0)

            # Ensure values are numeric
            try:
                offset_val = (
                    int(offset)
                    if offset is not None and isinstance(offset, (int, str, float))
                    else 0
                )
                page_size_val = (
                    int(page_size)
                    if page_size is not None
                    and isinstance(page_size, (int, str, float))
                    else 0
                )
            except (ValueError, TypeError):
                offset_val = 0
                page_size_val = 0

            return FlextMeltanoTapOracleOicUtilities.StateManagement.set_bookmark(
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
                return FlextMeltanoTapOracleOicUtilities.DEFAULT_PAGE_SIZE

            calculated_size = max(1, total_records // target_requests)
            return min(calculated_size, 1000)  # OIC API limit

        @staticmethod
        def estimate_extraction_time(
            record_count: int,
            records_per_second: float = 10.0,
        ) -> dict[str, t.GeneralValueType]:
            """Estimate extraction time for OIC data.

            Args:
            record_count: Number of records to extract
            records_per_second: Processing rate

            Returns:
            dict[str, t.GeneralValueType]: Time estimation

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

    # Proxy methods for backward compatibility
    @classmethod
    def create_schema_message(
        cls,
        stream_name: str,
        schema: dict[str, t.JsonValue],
        key_properties: list[str] | None = None,
    ) -> m.Meltano.SingerSchemaMessage:
        """Proxy method for SingerUtilities.create_schema_message()."""
        return cls.TapOracleOic.create_schema_message(
            stream_name,
            schema,
            key_properties,
        )

    @classmethod
    def create_record_message(
        cls,
        stream_name: str,
        record: dict[str, t.JsonValue],
        time_extracted: datetime | None = None,
    ) -> m.Meltano.SingerRecordMessage:
        """Proxy method for SingerUtilities.create_record_message()."""
        return cls.TapOracleOic.create_record_message(
            stream_name,
            record,
            time_extracted,
        )

    @classmethod
    def validate_oic_endpoint(cls, endpoint_url: str) -> FlextResult[str]:
        """Proxy method for OicApiProcessing.validate_oic_endpoint()."""
        return cls.OicApiProcessing.validate_oic_endpoint(endpoint_url)

    @classmethod
    def build_oic_api_url(
        cls,
        base_url: str,
        resource_path: str,
        query_params: dict[str, str] | None = None,
    ) -> FlextResult[str]:
        """Proxy method for OicApiProcessing.build_oic_api_url()."""
        return cls.OicApiProcessing.build_oic_api_url(
            base_url,
            resource_path,
            query_params,
        )

    @classmethod
    def normalize_integration_name(cls, integration_name: str) -> str:
        """Proxy method for OicDataProcessing.normalize_integration_name()."""
        return cls.OicDataProcessing.normalize_integration_name(integration_name)

    @classmethod
    def format_oic_timestamp(cls, timestamp_str: str) -> FlextResult[str]:
        """Proxy method for OicDataProcessing.format_oic_timestamp()."""
        return cls.OicDataProcessing.format_oic_timestamp(timestamp_str)

    @classmethod
    def validate_oic_connection_config(
        cls,
        config: dict[str, t.GeneralValueType],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Proxy method for ConfigValidation.validate_oic_connection_config()."""
        return cls.ConfigValidation.validate_oic_connection_config(config)

    @classmethod
    def get_stream_state(
        cls,
        state: dict[str, t.GeneralValueType],
        stream_name: str,
    ) -> dict[str, t.GeneralValueType]:
        """Proxy method for StateManagement.get_stream_state()."""
        return cls.StateManagement.get_stream_state(state, stream_name)

    @classmethod
    def set_bookmark(
        cls,
        state: dict[str, t.GeneralValueType],
        stream_name: str,
        bookmark_key: str,
        bookmark_value: object,
    ) -> dict[str, t.GeneralValueType]:
        """Proxy method for StateManagement.set_bookmark()."""
        return cls.StateManagement.set_bookmark(
            state,
            stream_name,
            bookmark_key,
            bookmark_value,
        )


__all__ = [
    "FlextMeltanoTapOracleOicUtilities",
]
