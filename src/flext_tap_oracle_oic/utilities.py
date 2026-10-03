"""Singer tap utilities for Oracle OIC (Oracle Integration Cloud) operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from urllib.parse import urlparse

from flext_meltano import FlextMeltanoUtilities
from flext_oracle_oic import FlextOracleOicUtilities

from flext_tap_oracle_oic import c, p, r, t


class FlextTapOracleOicUtilities(FlextOracleOicUtilities, FlextMeltanoUtilities):
    """Single unified utilities class for Singer tap Oracle OIC operations.

    Follows FLEXT unified class pattern with nested helper classes for
    domain-specific Singer tap functionality with Oracle Integration Cloud.
    """

    class TapOracleOic:
        """Tap Oracle OIC-specific utility namespace."""

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
                return r[str].fail(f"URL validation error: {e}", exception=e)

        @staticmethod
        def validate_stream_config(settings: t.JsonMapping) -> p.Result[t.JsonMapping]:
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
            stream_validation = u.validate_value(
                t.strict_json_mapping_adapter(),
                streams,
            )
            if stream_validation.failure:
                return r[t.JsonMapping].fail(
                    f"Streams configuration must be a dictionary: {stream_validation.error}",
                )
            stream_map = stream_validation.value
            for stream_name, stream_payload in stream_map.items():
                config_validation = u.validate_value(
                    t.strict_json_mapping_adapter(),
                    stream_payload,
                )
                if config_validation.failure:
                    return r[t.JsonMapping].fail(
                        f"Stream '{stream_name}' configuration must be a dictionary: "
                        f"{config_validation.error}",
                    )
                stream_config = config_validation.value
                if "selected" not in stream_config:
                    return r[t.JsonMapping].fail(
                        f"Stream '{stream_name}' must have 'selected' field",
                    )
                if "page_size" in stream_config:
                    page_size_validation = u.validate_value(
                        t.int_adapter(),
                        stream_config["page_size"],
                    )
                    if page_size_validation.failure:
                        return r[t.JsonMapping].from_failure(page_size_validation)
                    page_size = page_size_validation.value
                    max_page_size = c.MAX_PAGE_SIZE
                    if page_size <= 0 or page_size > max_page_size:
                        return r[t.JsonMapping].fail(
                            f"Stream '{stream_name}' page_size must be between 1 and {max_page_size}",
                        )
            return r[t.JsonMapping].ok(
                t.json_mapping_adapter().validate_python(settings),
            )


u = FlextTapOracleOicUtilities

__all__: list[str] = ["FlextTapOracleOicUtilities", "u"]
