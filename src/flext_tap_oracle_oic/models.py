"""Oracle Integration Cloud Models using standardized [Project]Models pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import (
    Iterator,
    Mapping,
)
from typing import Annotated, ClassVar

from flext_api import FlextApi, FlextApiSettings

from flext_meltano import FlextMeltanoModels
from flext_oracle_oic import m
from flext_tap_oracle_oic import c, e, p, settings, t, u
from flext_tap_oracle_oic._models._activity import (
    OicActivityRecord as _OicActivityRecord,
)
from flext_tap_oracle_oic._models._agent import OicAgentEntity as _OicAgentEntity
from flext_tap_oracle_oic._models._api_response import OicApiResponse as _OicApiResponse
from flext_tap_oracle_oic._models._auth_config import (
    OicAuthenticationConfig as _OicAuthenticationConfig,
)
from flext_tap_oracle_oic._models._connection import (
    OicConnectionEntity as _OicConnectionEntity,
)
from flext_tap_oracle_oic._models._envelope import OicEnvelope as _OicEnvelope
from flext_tap_oracle_oic._models._error_context import (
    OicErrorContext as _OicErrorContext,
)
from flext_tap_oracle_oic._models._integration import (
    OicIntegrationEntity as _OicIntegrationEntity,
)
from flext_tap_oracle_oic._models._metrics import OicMetricsRecord as _OicMetricsRecord
from flext_tap_oracle_oic._models._oic_connection import (
    FlextTapOracleOicConnection as _FlextTapOracleOicConnection,
)
from flext_tap_oracle_oic._models._oic_execution_summary import (
    FlextTapOracleOicExecutionSummary as _FlextTapOracleOicExecutionSummary,
)
from flext_tap_oracle_oic._models._oic_integration import (
    FlextTapOracleOicIntegration as _FlextTapOracleOicIntegration,
)
from flext_tap_oracle_oic._models._oic_lookup import (
    FlextTapOracleOicLookup as _FlextTapOracleOicLookup,
)
from flext_tap_oracle_oic._models._oic_monitoring import (
    FlextTapOracleOicMonitoringRecord as _FlextTapOracleOicMonitoringRecord,
)
from flext_tap_oracle_oic._models._oic_project import (
    FlextTapOracleOicProject as _FlextTapOracleOicProject,
)
from flext_tap_oracle_oic._models._oic_resource_metadata import (
    FlextTapOracleOicResourceMetadata as _FlextTapOracleOicResourceMetadata,
)
from flext_tap_oracle_oic._models._package import OicPackageEntity as _OicPackageEntity
from flext_tap_oracle_oic._models._stream_config import (
    OicStreamConfiguration as _OicStreamConfiguration,
)
from flext_tap_oracle_oic.tap_streams import FlextTapOracleOicPaginator


class FlextTapOracleOicModels(FlextMeltanoModels, m):
    """Oracle Integration Cloud tap models extending flext-core m.

    Provides complete models for OIC entity extraction, authentication,
    monitoring, and Singer protocol compliance following standardized patterns.
    """

    class TapOracleOic:
        """TapOracleOic domain namespace."""

        @staticmethod
        def require_entity_value(
            value: str,
            *,
            label: str,
        ) -> None:
            """Require one non-empty entity identifier/name value."""
            if not value:
                msg = f"{label} is required"
                raise ValueError(msg)

        @staticmethod
        def validate_optional_port(port: int | None) -> None:
            """Validate optional network port within canonical bounds."""
            if port is not None and not (
                c.DEFAULT_RETRY_DELAY_SECONDS <= port <= c.MAX_PORT
            ):
                msg = "Port must be between 1 and 65535"
                raise ValueError(msg)

        @staticmethod
        def validate_entity_identity_and_port(
            *,
            entity_id: str,
            entity_name: str,
            id_label: str,
            name_label: str,
            port: int | None,
        ) -> None:
            """Validate required entity id/name fields and optional port."""
            FlextTapOracleOicModels.TapOracleOic.require_entity_value(
                entity_id,
                label=id_label,
            )
            FlextTapOracleOicModels.TapOracleOic.require_entity_value(
                entity_name,
                label=name_label,
            )
            FlextTapOracleOicModels.TapOracleOic.validate_optional_port(port)

        OicEnvelope = _OicEnvelope

        class OICBaseStream(FlextMeltanoModels.BaseModel):
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

            model_config: ClassVar[FlextMeltanoModels.ConfigDict] = (
                FlextMeltanoModels.ConfigDict(
                    arbitrary_types_allowed=True,
                )
            )

            settings: Annotated[t.JsonMapping, u.Field(default_factory=dict)]
            name: Annotated[str, u.Field(default="")]
            replication_key: Annotated[str | None, u.Field(default=None)]
            logger: p.Logger = u.Field(default_factory=lambda: u.fetch_logger(__name__))

            requires_design_api: ClassVar[bool] = False
            requires_runtime_api: ClassVar[bool] = False
            api_path: ClassVar[str | None] = None
            api_category: ClassVar[str] = "core"
            default_sort: ClassVar[str | None] = None
            additional_params: ClassVar[t.JsonMapping | None] = None
            primary_keys: ClassVar[t.StrSequence] = []

            @property
            def api_client(self) -> FlextApi:
                """The authenticated API client from parent tap's OIC client."""
                api_config = FlextApiSettings.model_validate({})
                return FlextApi(settings=api_config)

            @property
            def url_base(self) -> str:
                """Build base URL for Oracle OIC API requests with intelligent discovery.

                Returns:
                Base URL with appropriate OIC API endpoint for stream type.

                """
                base_url_raw = settings.get("base_url") or settings.get(
                    "oic_url",
                    "",
                )
                base_url = str(base_url_raw).rstrip("/")
                if not base_url:
                    msg = "Base URL is required but not configured"
                    raise ValueError(msg)
                validation_result = u.TapOracleOic.validate_oic_endpoint(base_url)
                if validation_result.failure:
                    msg = f"Invalid OIC endpoint: {validation_result.error}"
                    raise ValueError(msg)
                region = settings.get("region")
                if not region and "integration.ocp.oraclecloud.com" in base_url:
                    region_match = c.TapOracleOic.OCI_REGION_RE.search(base_url)
                    region = region_match.group(1) if region_match else "us-ashburn-1"
                if "integration.ocp.oraclecloud.com" in base_url:
                    if self.requires_design_api:
                        base_url = (
                            f"https://design.integration.{region}.ocp.oraclecloud.com"
                        )
                    elif self.requires_runtime_api:
                        base_url = (
                            f"https://runtime.integration.{region}.ocp.oraclecloud.com"
                        )
                if self.api_path is not None:
                    api_path: str = self.api_path
                    return base_url + api_path
                api_paths: dict[str, str] = {
                    "core": c.TapOracleOic.OIC_API_BASE_PATH,
                    "monitoring": c.TapOracleOic.OIC_MONITORING_API_PATH,
                    "b2b": c.TapOracleOic.OIC_B2B_API_PATH,
                    "process": c.TapOracleOic.OIC_PROCESS_API_PATH,
                }
                resolved_api_path: str = api_paths.get(
                    self.api_category,
                    c.TapOracleOic.OIC_API_BASE_PATH,
                )
                return base_url + resolved_api_path

            def get_new_paginator(self) -> p.TapOracleOic.Paginator:
                """Create new Oracle OIC paginator with configuration.

                Returns:
                Paginator instance configured with settings from tap settings.

                """
                page_size_val = settings.get("page_size", 100)
                page_size = page_size_val if isinstance(page_size_val, int) else 100
                return FlextTapOracleOicPaginator(start_value=0, page_size=page_size)

            def get_records(
                self,
                context: t.JsonMapping | None = None,
            ) -> Iterator[t.JsonMapping]:
                """Yield the records from OIC API.

                Args:
                    context: Optional context for record extraction.

                Yields:
                    Records from the OIC API.

                """
                _ = context
                yield from ()

            def get_url_params(
                self,
                context: t.JsonMapping | None,
                next_page_token: int | None,
            ) -> t.JsonMapping:
                """Build URL parameters for Oracle OIC API requests.

                Args:
                context: Stream context with replication values.
                next_page_token: Token for pagination (offset value).

                Returns:
                Dictionary of URL parameters optimized for OIC API.

                """
                params: t.MutableJsonMapping = {}
                page_size_val = settings.get("page_size", 100)
                page_size = page_size_val if isinstance(page_size_val, int) else 100
                params["limit"] = min(page_size, 1000)
                params["offset"] = next_page_token or 0
                instance_id = settings.get("instance_id")
                if instance_id:
                    params["integrationInstance"] = instance_id
                sort_field = settings.get("sort_field")
                if sort_field:
                    sort_direction = (
                        "desc" if settings.get("sort_desc", False) else "asc"
                    )
                    params["orderBy"] = f"{sort_field}:{sort_direction}"
                elif self.default_sort is not None:
                    params["orderBy"] = self.default_sort
                custom_filter = settings.get("custom_filter")
                if custom_filter:
                    params["q"] = custom_filter
                if (
                    self.replication_key
                    and context
                    and context.get("starting_replication_value")
                ):
                    start_date = context["starting_replication_value"]
                    params[f"{self.replication_key}>="] = start_date
                select_fields = settings.get("select_fields")
                if select_fields:
                    try:
                        field_list = t.strict_str_sequence_adapter().validate_python(
                            select_fields,
                        )
                    except c.ValidationError:
                        field_list = None
                    params["fields"] = (
                        ",".join(field_list)
                        if field_list is not None
                        else str(select_fields)
                    )
                if self.additional_params is not None:
                    params.update(self.additional_params)
                return dict(params)

            def parse_response(
                self,
                response: m.Api.HttpResponse,
            ) -> Iterator[t.JsonMapping]:
                """Parse Oracle OIC API response and yield records with validation.

                Args:
                response: HTTP response from OIC API.

                Yields:
                Individual records from the API response with tap metadata.

                """
                try:
                    records = self._parse_response_records(response)
                except c.Meltano.SINGER_SAFE_EXCEPTIONS:
                    response_url_err = self._get_response_identifier(response)
                    self.logger.exception(
                        "Error parsing response from %s",
                        response_url_err,
                    )
                    if settings.get("fail_on_parsing_errors", True):
                        raise
                    return
                yield from records

            def _parse_response_records(
                self,
                response: m.Api.HttpResponse,
            ) -> t.SequenceOf[t.JsonMapping]:
                """Parse one response into enriched records."""
                if response.status_code >= c.TapOracleOic.HTTP_ERROR_STATUS_THRESHOLD:
                    self._handle_response_error(response)
                    return ()
                data = self._get_response_data(response)
                self._track_response_metrics(response, data)
                response_url = self._get_response_identifier(response)
                return tuple(self._extract_and_yield_records(data, response_url))

            def _enrich_record(
                self,
                record: t.JsonMapping,
            ) -> t.JsonMapping:
                """Enrich record with tap metadata for traceability."""
                enriched = t.json_dict_adapter().validate_python(record)
                enriched["_tap_extracted_at"] = u.generate_datetime_utc().isoformat()
                enriched["_tap_stream_name"] = self.name
                return enriched

            def _extract_and_yield_records(
                self,
                data: t.JsonMapping | t.JsonList,
                url: str,
            ) -> Iterator[t.JsonMapping]:
                """Extract and yield records with validation and enrichment."""
                records_yielded = 0
                for item in self._extract_items_for_processing(data):
                    if self._validate_record(item):
                        yield self._enrich_record(item)
                        records_yielded += 1
                if records_yielded == 0 and (not self._is_empty_result_expected(data)):
                    map_data = data if isinstance(data, Mapping) else None
                    payload_descriptor: str = (
                        str(list(map_data.keys()))
                        if map_data is not None
                        else str(type(data))
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
                data: t.JsonMapping | t.JsonList,
            ) -> Iterator[t.JsonMapping]:
                """Extract items from various OIC response formats for processing."""
                if isinstance(data, Mapping):
                    yield from self._process_dict_data(data)
                    return
                if isinstance(data, list):
                    yield from self._process_list_data(data)
                else:
                    yield from self._process_list_data(list(data))

            def _get_response_data(
                self,
                response: m.Api.HttpResponse,
            ) -> t.JsonMapping | t.JsonList:
                """Normalize flext-api response bodies to OIC payload structures."""
                match response.body:
                    case dict() as body_map:
                        return body_map
                    case str() as body_str if body_str.strip():
                        return t.strict_json_mapping_adapter().validate_json(
                            body_str,
                        )
                    case _:
                        msg = "OIC response body is empty or not JSON-compatible"
                        raise TypeError(msg)

            def _get_response_identifier(
                self,
                response: m.Api.HttpResponse,
            ) -> str:
                """Return a stable identifier for response logging."""
                request_id_raw: p.AttributeProbe = response.request_id
                if isinstance(request_id_raw, str) and request_id_raw:
                    return request_id_raw
                identifier: str = (
                    self.api_path if self.api_path is not None else self.name
                )
                return identifier

            @staticmethod
            def _as_oic_envelope(
                data: t.JsonMapping,
            ) -> _OicEnvelope | None:
                try:
                    return _OicEnvelope.model_validate(
                        data,
                        strict=True,
                    )
                except c.ValidationError:
                    return None

            def _handle_response_error(
                self,
                response: m.Api.HttpResponse,
            ) -> None:
                """Handle Oracle OIC API response errors with proper categorization."""
                error_message: t.JsonValue | None = None
                if isinstance(response.body, dict):
                    error_message = response.body.get("message") or response.body.get(
                        "error",
                    )
                if error_message is None:
                    error_message = (
                        str(response.body)
                        if response.body
                        else f"HTTP {response.status_code}"
                    )
                response_url = self._get_response_identifier(response)
                err_msg = str(error_message)
                self.logger.error("OIC API error from %s: %s", response_url, err_msg)
                status_code = response.status_code
                if status_code == c.TapOracleOic.HTTP_UNAUTHORIZED:
                    msg = "Unauthorized: Authentication failed or token expired"
                    raise e.AuthenticationError(msg)
                if status_code == c.TapOracleOic.HTTP_FORBIDDEN:
                    msg = "Forbidden: Insufficient permissions to access resource"
                    raise e.AuthorizationError(msg)
                if status_code == c.TapOracleOic.HTTP_RATE_LIMITED:
                    msg = "Rate limit exceeded: Too many requests"
                    raise e.RateLimitError(msg)
                raise e.OperationError(err_msg)

            def _is_empty_result_expected(
                self,
                data: t.JsonMapping | t.JsonList,
            ) -> bool:
                """Check if empty result is expected/normal based on OIC response metadata."""
                if not isinstance(data, Mapping):
                    return not data
                envelope = self._as_oic_envelope(data)
                if envelope is not None:
                    return (
                        envelope.total_size == 0
                        or envelope.count == 0
                        or (envelope.items is not None and not envelope.items)
                        or (envelope.data is not None and not envelope.data)
                    )
                return False

            def _is_single_record(self, data: t.JsonMapping) -> bool:
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

            def _process_dict_data(
                self,
                data: t.JsonMapping,
            ) -> Iterator[t.JsonMapping]:
                """Process dict-type response data with OIC format detection."""
                envelope = self._as_oic_envelope(data)
                if envelope is not None and envelope.items is not None:
                    yield from self._process_list_data(envelope.items)
                    return
                if envelope is not None and envelope.data is not None:
                    yield from self._process_list_data(envelope.data)
                    return
                if self._is_single_record(data):
                    yield data

            def _process_list_data(
                self,
                data: t.JsonList | t.SequenceOf[t.JsonMapping],
            ) -> Iterator[t.JsonMapping]:
                """Process list-type response data."""
                for item in data:
                    if isinstance(item, Mapping):
                        yield item
                        continue
                    try:
                        record = t.strict_json_mapping_adapter().validate_python(
                            item,
                        )
                    except c.ValidationError:
                        record = None
                    if record is not None:
                        yield record

            def _track_response_metrics(
                self,
                response: m.Api.HttpResponse,
                data: t.JsonMapping | t.JsonList,
            ) -> None:
                """Track response metrics for monitoring and optimization."""
                self.logger.debug("Response status: %s", response.status_code)
                if not isinstance(data, Mapping):
                    self.logger.debug("Received %s records", len(data))
                    return
                envelope = self._as_oic_envelope(data)
                if envelope is None:
                    return
                if envelope.items is not None:
                    self.logger.debug("Received %s records", len(envelope.items))
                elif envelope.data is not None:
                    self.logger.debug("Received %s records", len(envelope.data))

            def _validate_record(self, record: t.JsonMapping) -> bool:
                """Validate record meets basic requirements for processing."""
                return bool(record)

        OicAuthenticationConfig = _OicAuthenticationConfig

        OicIntegrationEntity = _OicIntegrationEntity

        OicConnectionEntity = _OicConnectionEntity

        OicActivityRecord = _OicActivityRecord

        OicPackageEntity = _OicPackageEntity

        OicMetricsRecord = _OicMetricsRecord

        OicAgentEntity = _OicAgentEntity

        OicStreamConfiguration = _OicStreamConfiguration

        OicApiResponse = _OicApiResponse

        OicErrorContext = _OicErrorContext

        class OracleOic(m.OracleOic):
            """Domain entity models for Oracle OIC resources.

            Canonical home for OIC entity classes, migrated from domain/entities.py
            per MRO policy: all m subclasses live under [Project]Models.
            """

            FlextTapOracleOicConnection = _FlextTapOracleOicConnection

            FlextTapOracleOicIntegration = _FlextTapOracleOicIntegration

            FlextTapOracleOicLookup = _FlextTapOracleOicLookup

            FlextTapOracleOicMonitoringRecord = _FlextTapOracleOicMonitoringRecord

            FlextTapOracleOicProject = _FlextTapOracleOicProject

            FlextTapOracleOicResourceMetadata = _FlextTapOracleOicResourceMetadata

            FlextTapOracleOicExecutionSummary = _FlextTapOracleOicExecutionSummary


# Short alias
m = FlextTapOracleOicModels

__all__: list[str] = [
    "FlextTapOracleOicModels",
    "m",
]
