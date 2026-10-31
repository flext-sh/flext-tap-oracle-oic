"""Singer tap OIC configuration validation utilities.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from urllib.parse import urlparse

from flext_meltano import u

from flext_tap_oracle_oic import c, p, r, t


class FlextTapOracleOicUtilitiesValidation:
    """OIC endpoint and stream configuration validation utilities."""

    @staticmethod
    def validate_oic_endpoint(endpoint_url: str) -> p.Result[str]:
        """Validate an Oracle OIC endpoint URL.

        Args:
            endpoint_url: Candidate OIC endpoint URL.

        Returns:
            Result succeeding with the validated URL, or failing when
            the URL is empty, malformed, or not an OIC endpoint.


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
    def validate_single_stream(
        stream_name: str,
        stream_payload: t.JsonValue,
    ) -> p.Result[bool]:
        """Validate one stream entry of the tap configuration.

        Args:
            stream_name: Name of the stream entry being validated.
            stream_payload: Raw stream entry payload from the config.

        Returns:
            Result succeeding with ``True`` when the entry is valid, or
            the failure describing the first violated rule.


        """
        config_validation = u.validate_value(
            u.strict_json_mapping_adapter(),
            stream_payload,
        )
        if config_validation.failure:
            return r[bool].fail(
                f"Stream '{stream_name}' configuration must be a dictionary: "
                f"{config_validation.error}",
            )
        stream_config = config_validation.value
        if "selected" not in stream_config:
            return r[bool].fail(
                f"Stream '{stream_name}' must have 'selected' field",
            )
        if "page_size" not in stream_config:
            return r[bool].ok(value=True)
        page_size_validation = u.validate_value(
            u.int_adapter(),
            stream_config["page_size"],
        )
        if page_size_validation.failure:
            return r[bool].from_failure(page_size_validation)
        page_size = page_size_validation.value
        max_page_size = c.MAX_PAGE_SIZE
        if page_size <= 0 or page_size > max_page_size:
            return r[bool].fail(
                f"Stream '{stream_name}' page_size must be between 1 and "
                f"{max_page_size}",
            )
        return r[bool].ok(value=True)

    @staticmethod
    def validate_stream_config(settings: t.JsonMapping) -> p.Result[t.JsonMapping]:
        """Validate the OIC tap stream configuration.

        Args:
            settings: Tap settings holding the ``streams`` section to
                validate.

        Returns:
            Result succeeding with the validated settings mapping, or
            the failure describing the first invalid stream.


        """
        if "streams" not in settings:
            return r[t.JsonMapping].fail(
                "Configuration must include 'streams' section",
            )
        streams = settings["streams"]
        stream_validation = u.validate_value(
            u.strict_json_mapping_adapter(),
            streams,
        )
        if stream_validation.failure:
            return r[t.JsonMapping].fail(
                f"Streams configuration must be a dictionary: "
                f"{stream_validation.error}",
            )
        for stream_name, stream_payload in stream_validation.value.items():
            single = FlextTapOracleOicUtilitiesValidation.validate_single_stream(
                stream_name,
                stream_payload,
            )
            if single.failure:
                return r[t.JsonMapping].from_failure(single)
        return r[t.JsonMapping].ok(
            u.json_mapping_adapter().validate_python(settings),
        )


__all__: list[str] = ["FlextTapOracleOicUtilitiesValidation"]
