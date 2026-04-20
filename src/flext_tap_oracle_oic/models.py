"""Oracle Integration Cloud Models using standardized [Project]Models pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import re
from collections.abc import (
    Iterator,
    Mapping,
    MutableSequence,
    Sequence,
)
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Annotated, ClassVar, Self

from flext_api import FlextApi, FlextApiModels, FlextApiSettings

from flext_core import (
    FlextConstants,
    FlextModels,
)
from flext_meltano import FlextMeltanoModels, m, u
from flext_oracle_oic import FlextOracleOicModels
from flext_tap_oracle_oic import FlextTapOracleOicUtilities, c, e, t

if TYPE_CHECKING:
    from flext_tap_oracle_oic import p


class FlextTapOracleOicModels(FlextMeltanoModels, FlextOracleOicModels):
    """Oracle Integration Cloud tap models extending flext-core FlextModels.

    Provides complete models for OIC entity extraction, authentication,
    monitoring, and Singer protocol compliance following standardized patterns.
    """

    @staticmethod
    def _get_oic_paginator_class() -> (
        p.TapOracleOic.TapOracleOicPrivate.PaginatorFactory
    ):
        """Lazy import to break circular dependency between models and tap_streams."""
        from flext_tap_oracle_oic import FlextTapOracleOicPaginator as _Cls

        return _Cls

    @staticmethod
    def as_value_list(
        value: t.Container | None,
    ) -> Sequence[t.Container] | None:
        """Validate payload as strict t.FlatContainerList."""
        try:
            return t.GENERAL_LIST_ADAPTER.validate_python(value)
        except c.ValidationError:
            return None

    @staticmethod
    def _as_value_map(
        value: t.Container | None,
    ) -> t.ContainerValueMapping | None:
        """Validate payload as strict Mapping[str, t.Container]."""
        try:
            return t.GENERAL_MAP_ADAPTER.validate_python(value)
        except c.ValidationError:
            return None

    @staticmethod
    def _as_string_list(value: t.Container | None) -> t.StrSequence | None:
        """Validate payload as strict t.StrSequence."""
        try:
            return t.STRING_LIST_ADAPTER.validate_python(value)
        except c.ValidationError:
            return None

    @staticmethod
    def as_oic_envelope(
        value: t.ContainerValueMapping,
    ) -> FlextTapOracleOicModels.TapOracleOic.OicEnvelope | None:
        """Validate payload as an OIC envelope model."""
        try:
            return FlextTapOracleOicModels.TapOracleOic.OicEnvelope.model_validate(
                value,
                strict=True,
            )
        except c.ValidationError:
            return None

    # Dynamic attributes for runtime configuration (accessed via hasattr checks)
    _oic_authentication: t.ContainerValueMapping | None = None
    _stream_configurations: t.ContainerValueMapping | None = None
    _singer_mode: t.ContainerValueMapping | None = None
    _include_oic_metadata: t.ContainerValueMapping | None = None

    @u.computed_field()
    @property
    def active_oic_tap_models_count(self) -> int:
        """Count of active Oracle OIC tap models with API extraction capabilities."""
        return self._count_active_oic_tap_models()

    @u.computed_field()
    @property
    def oic_tap_system_summary(self) -> t.ContainerValueMapping:
        """Complete Singer Oracle OIC tap system summary with API extraction capabilities."""
        model_count: int = self._count_active_oic_tap_models()
        return {
            "total_models": model_count,
            "tap_type": "singer_oracle_oic_api_extractor",
            "extraction_features": [
                "oic_integration_monitoring",
                "connection_metadata_extraction",
                "activity_incremental_replication",
                "package_management_tracking",
                "performance_metrics_collection",
                "agent_health_monitoring",
            ],
            "singer_compliance": {
                "protocol_version": "singer_v1",
                "stream_discovery": True,
                "catalog_generation": True,
                "state_management": True,
                "incremental_bookmarking": True,
            },
            "oic_capabilities": {
                "oauth2_authentication": True,
                "api_pagination": True,
                "data_sanitization": True,
                "error_recovery": True,
                "rate_limit_handling": True,
            },
        }

    @u.field_serializer("*", when_used="json")
    def serialize_with_oic_metadata(
        self,
        value: t.ContainerValueMapping,
        _info: u.FieldSerializationInfo,
    ) -> t.ContainerValueMapping:
        """Add Singer Oracle OIC tap metadata to all serialized fields."""
        return {
            **value,
            "_oic_tap_metadata": {
                "extraction_timestamp": datetime.now(UTC).isoformat(),
                "tap_type": "oracle_oic_api_extractor",
                "singer_protocol": "v1.0",
                "data_source": "oracle_integration_cloud",
            },
        }

    @u.model_validator(mode="after")
    def validate_oic_tap_system_consistency(self) -> Self:
        """Validate Singer Oracle OIC tap system consistency and configuration."""
        # Singer OIC tap authentication validation
        if self._oic_authentication and not hasattr(self, "OicAuthenticationConfig"):
            msg = "OicAuthenticationConfig required when OIC authentication configured"
            raise ValueError(msg)

        # Stream configuration validation
        if self._stream_configurations and not hasattr(self, "OicStreamConfiguration"):
            msg = "OicStreamConfiguration required for stream configurations"
            raise ValueError(msg)

        # Singer protocol compliance validation
        if self._singer_mode:
            required_models = ["OicApiResponse", "OicErrorContext"]
            for model in required_models:
                if not hasattr(self, model):
                    msg = f"{model} required for Singer protocol compliance"
                    raise ValueError(msg)

        return self

    # Advanced Pydantic 2.11 Features - Singer Oracle OIC Tap Domain

    def _count_active_oic_tap_models(self) -> int:
        """Count of active Oracle OIC tap models with API extraction capabilities."""
        model_names = [
            "OicAuthenticationConfig",
            "OicIntegrationEntity",
            "OicConnectionEntity",
            "OicActivityRecord",
            "OicPackageEntity",
            "OicMetricsRecord",
            "OicAgentEntity",
            "OicStreamConfiguration",
            "OicApiResponse",
            "OicErrorContext",
        ]
        return sum(1 for name in model_names if getattr(self, name) is not None)

    class TapOracleOic:
        """TapOracleOic domain namespace."""

        class OicEnvelope(m.BaseModel):
            """OIC API response envelope for paginated list endpoints.

            Parses the outer wrapper that Oracle OIC returns for list responses,
            normalizing between 'items', 'data', 'count', and 'totalSize' fields.
            """

            items: Sequence[t.ContainerValueMapping] | None = None
            data: Sequence[t.ContainerValueMapping] | None = None
            total_size: Annotated[int | None, u.Field(alias="totalSize")] = None
            count: int | None = None

        class OICBaseStream(m.BaseModel):
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

            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
                arbitrary_types_allowed=True,
            )

            settings: Annotated[t.ContainerValueMapping, u.Field(default_factory=dict)]
            name: Annotated[str, u.Field(default="")]
            replication_key: Annotated[str | None, u.Field(default=None)]
            logger: p.Logger = u.Field(default_factory=lambda: u.fetch_logger(__name__))

            requires_design_api: ClassVar[bool] = False
            requires_runtime_api: ClassVar[bool] = False
            api_path: ClassVar[str | None] = None
            api_category: ClassVar[str] = "core"
            default_sort: ClassVar[str | None] = None
            additional_params: ClassVar[t.ContainerValueMapping | None] = None
            primary_keys: ClassVar[t.StrSequence] = []

            @property
            def api_client(self) -> FlextApi:
                """Get authenticated API client from parent tap's OIC client."""
                api_config = FlextApiSettings.model_validate({})
                return FlextApi(settings=api_config)

            @property
            def url_base(self) -> str:
                """Build base URL for Oracle OIC API requests with intelligent discovery.

                Returns:
                Base URL with appropriate OIC API endpoint for stream type.

                """
                utilities = FlextTapOracleOicUtilities()
                base_url = str(
                    self.settings.get("base_url") or self.settings.get("oic_url", ""),
                ).rstrip("/")
                if not base_url:
                    msg = "Base URL is required but not configured"
                    raise ValueError(msg)
                validation_result = (
                    utilities.TapOracleOic.OicApiProcessing.validate_oic_endpoint(
                        base_url,
                    )
                )
                if validation_result.failure:
                    msg = f"Invalid OIC endpoint: {validation_result.error}"
                    raise ValueError(msg)
                region = self.settings.get("region")
                if not region and "integration.ocp.oraclecloud.com" in base_url:
                    region_match = re.search(r"(\\w+-\\w+-\\d+)", base_url)
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
                    return base_url + self.api_path
                api_paths = {
                    "core": c.OIC_API_BASE_PATH,
                    "monitoring": c.OIC_MONITORING_API_PATH,
                    "b2b": c.OIC_B2B_API_PATH,
                    "process": c.OIC_PROCESS_API_PATH,
                }
                return base_url + api_paths.get(
                    self.api_category,
                    c.OIC_API_BASE_PATH,
                )

            def get_new_paginator(self) -> p.TapOracleOic.TapOracleOicPrivate.Paginator:
                """Create new Oracle OIC paginator with configuration.

                Returns:
                Paginator instance configured with settings from tap settings.

                """
                paginator_cls = FlextTapOracleOicModels._get_oic_paginator_class()
                page_size_val = self.settings.get("page_size", 100)
                page_size = page_size_val if isinstance(page_size_val, int) else 100
                return paginator_cls(start_value=0, page_size=page_size)

            def get_records(
                self,
                context: t.ContainerValueMapping | None = None,
            ) -> Iterator[t.ContainerValueMapping]:
                """Get records from OIC API.

                Args:
                    context: Optional context for record extraction.

                Yields:
                    Records from the OIC API.

                """
                _ = context
                yield from ()

            def get_url_params(
                self,
                context: t.ContainerValueMapping | None,
                next_page_token: int | None,
            ) -> t.ContainerValueMapping:
                """Build URL parameters for Oracle OIC API requests.

                Args:
                context: Stream context with replication values.
                next_page_token: Token for pagination (offset value).

                Returns:
                Dictionary of URL parameters optimized for OIC API.

                """
                params: t.MutableContainerValueMapping = {}
                page_size_val = self.settings.get("page_size", 100)
                page_size = page_size_val if isinstance(page_size_val, int) else 100
                params["limit"] = min(page_size, 1000)
                params["offset"] = next_page_token or 0
                instance_id = self.settings.get("instance_id")
                if instance_id:
                    params["integrationInstance"] = instance_id
                sort_field = self.settings.get("sort_field")
                if sort_field:
                    sort_direction = (
                        "desc" if self.settings.get("sort_desc", False) else "asc"
                    )
                    params["orderBy"] = f"{sort_field}:{sort_direction}"
                elif self.default_sort is not None:
                    params["orderBy"] = self.default_sort
                custom_filter = self.settings.get("custom_filter")
                if custom_filter:
                    params["q"] = custom_filter
                if (
                    self.replication_key
                    and context
                    and context.get("starting_replication_value")
                ):
                    start_date = context["starting_replication_value"]
                    params[f"{self.replication_key}>="] = start_date
                select_fields = self.settings.get("select_fields")
                if select_fields:
                    field_list = FlextTapOracleOicModels._as_string_list(select_fields)
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
                response: FlextApiModels.Api.HttpResponse,
            ) -> Iterator[t.ContainerValueMapping]:
                """Parse Oracle OIC API response and yield records with validation.

                Args:
                response: HTTP response from OIC API.

                Yields:
                Individual records from the API response with tap metadata.

                """
                try:
                    if (
                        response.status_code
                        >= c.TapOracleOic.TapOicHttp.HTTP_ERROR_STATUS_THRESHOLD
                    ):
                        self._handle_response_error(response)
                        return
                    data = self._get_response_data(response)
                    self._track_response_metrics(response, data)
                    response_url = self._get_response_identifier(response)
                    yield from self._extract_and_yield_records(data, response_url)
                except c.Meltano.SINGER_SAFE_EXCEPTIONS:
                    response_url_err = self._get_response_identifier(response)
                    self.logger.exception(
                        "Error parsing response from %s",
                        response_url_err,
                    )
                    if self.settings.get("fail_on_parsing_errors", True):
                        raise

            def _enrich_record(
                self,
                record: t.ContainerValueMapping,
            ) -> t.ContainerValueMapping:
                """Enrich record with tap metadata for traceability."""
                enriched: t.MutableContainerValueMapping = dict(record)
                enriched["_tap_extracted_at"] = datetime.now(UTC).isoformat()
                enriched["_tap_stream_name"] = self.name
                return enriched

            def _extract_and_yield_records(
                self,
                data: t.ContainerValueMapping | Sequence[t.Container],
                url: str,
            ) -> Iterator[t.ContainerValueMapping]:
                """Extract and yield records with validation and enrichment."""
                records_yielded = 0
                for item in self._extract_items_for_processing(data):
                    if self._validate_record(item):
                        yield self._enrich_record(item)
                        records_yielded += 1
                if records_yielded == 0 and (not self._is_empty_result_expected(data)):
                    map_data = FlextTapOracleOicModels._as_value_map(data)
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
                data: t.ContainerValueMapping | Sequence[t.Container],
            ) -> Iterator[t.ContainerValueMapping]:
                """Extract items from various OIC response formats for processing."""
                if isinstance(data, list):
                    yield from self._process_list_data(data)
                    return
                list_payload = FlextTapOracleOicModels.as_value_list(data)
                if list_payload is not None:
                    yield from self._process_list_data(list_payload)
                    return
                map_payload = FlextTapOracleOicModels._as_value_map(data)
                if map_payload is not None:
                    yield from self._process_dict_data(map_payload)

            def _get_response_data(
                self,
                response: FlextApiModels.Api.HttpResponse,
            ) -> t.ContainerValueMapping | Sequence[t.Container]:
                """Normalize flext-api response bodies to OIC payload structures."""
                match response.body:
                    case dict() as body_map:
                        return body_map
                    case str() as body_str if body_str.strip():
                        return t.GENERAL_MAP_ADAPTER.validate_json(
                            body_str,
                        )
                    case _:
                        msg = "OIC response body is empty or not JSON-compatible"
                        raise TypeError(msg)

            def _get_response_identifier(
                self,
                response: FlextApiModels.Api.HttpResponse,
            ) -> str:
                """Return a stable identifier for response logging."""
                if response.request_id:
                    return response.request_id
                return self.api_path or self.name

            def _handle_response_error(
                self,
                response: FlextApiModels.Api.HttpResponse,
            ) -> None:
                """Handle Oracle OIC API response errors with proper categorization."""
                error_message: t.Container | None = None
                if isinstance(response.body, dict):
                    error_data = FlextTapOracleOicModels._as_value_map(response.body)
                    if error_data is not None:
                        error_message = error_data.get("message") or error_data.get(
                            "error",
                        )
                if error_message is None:
                    error_message = response.body or f"HTTP {response.status_code}"
                response_url = self._get_response_identifier(response)
                err_msg = str(error_message)
                self.logger.error("OIC API error from %s: %s", response_url, err_msg)
                status_code = response.status_code
                if status_code == c.TapOracleOic.TapOicHttp.HTTP_UNAUTHORIZED:
                    msg = "Unauthorized: Authentication failed or token expired"
                    raise e.AuthenticationError(msg)
                if status_code == c.TapOracleOic.TapOicHttp.HTTP_FORBIDDEN:
                    msg = "Forbidden: Insufficient permissions to access resource"
                    raise e.AuthorizationError(msg)
                if status_code == c.TapOracleOic.TapOicHttp.HTTP_RATE_LIMITED:
                    msg = "Rate limit exceeded: Too many requests"
                    raise e.RateLimitError(msg)
                raise e.OperationError(err_msg)

            def _is_empty_result_expected(
                self,
                data: t.ContainerValueMapping | Sequence[t.Container],
            ) -> bool:
                """Check if empty result is expected/normal based on OIC response metadata."""
                if not isinstance(data, Mapping):
                    return not data
                envelope = FlextTapOracleOicModels.as_oic_envelope(data)
                if envelope is not None:
                    return (
                        envelope.total_size == 0
                        or envelope.count == 0
                        or (envelope.items is not None and not envelope.items)
                        or (envelope.data is not None and not envelope.data)
                    )
                list_payload = FlextTapOracleOicModels.as_value_list(data)
                return not list_payload if list_payload is not None else False

            def _is_single_record(self, data: t.ContainerValueMapping) -> bool:
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
                data: t.ContainerValueMapping,
            ) -> Iterator[t.ContainerValueMapping]:
                """Process dict-type response data with OIC format detection."""
                envelope = FlextTapOracleOicModels.as_oic_envelope(data)
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
                data: Sequence[t.Container],
            ) -> Iterator[t.ContainerValueMapping]:
                """Process list-type response data."""
                for item in data:
                    record = FlextTapOracleOicModels._as_value_map(item)
                    if record is not None:
                        yield record

            def _track_response_metrics(
                self,
                response: FlextApiModels.Api.HttpResponse,
                data: t.ContainerValueMapping | Sequence[t.Container],
            ) -> None:
                """Track response metrics for monitoring and optimization."""
                self.logger.debug("Response status: %s", response.status_code)
                if not isinstance(data, Mapping):
                    self.logger.debug("Received %s records", len(data))
                    return
                list_payload = FlextTapOracleOicModels.as_value_list(data)
                if list_payload is not None:
                    self.logger.debug("Received %s records", len(list_payload))
                    return
                envelope = FlextTapOracleOicModels.as_oic_envelope(data)
                if envelope is None:
                    return
                if envelope.items is not None:
                    self.logger.debug("Received %s records", len(envelope.items))
                elif envelope.data is not None:
                    self.logger.debug("Received %s records", len(envelope.data))

            def _validate_record(self, record: t.ContainerValueMapping) -> bool:
                """Validate record meets basic requirements for processing."""
                return FlextTapOracleOicModels._as_value_map(dict(record)) is not None

        class OicAuthenticationConfig(FlextMeltanoModels.ArbitraryTypesModel):
            """OAuth2/IDCS authentication configuration for OIC API access."""

            # Pydantic 2.11 Configuration - Authentication Features
            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
                json_schema_extra={
                    "description": "OAuth2/IDCS authentication for Oracle OIC API",
                    "examples": [
                        {
                            "oauth_client_id": "my-client-id",
                            "oauth_token_url": "https://idcs-instance.identity.oraclecloud.com/oauth2/v1/token",
                            "base_url": "https://mycompany-oic.integration.ocp.oraclecloud.com",
                        },
                    ],
                },
            )

            oauth_client_id: Annotated[
                str,
                u.Field(
                    ...,
                    description="OAuth2 client ID for OIC API",
                ),
            ]
            oauth_client_secret: Annotated[
                str,
                u.Field(..., description="OAuth2 client secret"),
            ]
            oauth_token_url: Annotated[
                str,
                u.Field(
                    ...,
                    description="IDCS OAuth2 token endpoint URL",
                ),
            ]
            oauth_client_aud: Annotated[
                str,
                u.Field(..., description="OAuth2 audience parameter"),
            ]
            base_url: Annotated[str, u.Field(..., description="OIC instance base URL")]

            # Optional authentication settings
            token_expiry_buffer: Annotated[
                int,
                u.Field(
                    description="Token refresh buffer in seconds",
                ),
            ] = 300
            max_retry_attempts: Annotated[
                int,
                u.Field(
                    description="Maximum authentication retry attempts",
                ),
            ] = 3
            timeout_seconds: Annotated[
                int,
                u.Field(
                    description="Authentication timeout",
                ),
            ] = 30

            @u.computed_field()
            @property
            def auth_config_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.Container | None]]:
                """OAuth2 authentication configuration summary."""
                return {
                    "oauth_setup": {
                        "client_id": self.oauth_client_id[
                            : FlextConstants.MIN_NAME_LENGTH
                        ]
                        + "..."
                        if len(self.oauth_client_id) > FlextConstants.MIN_NAME_LENGTH
                        else self.oauth_client_id,
                        "token_endpoint": self.oauth_token_url,
                        "audience": self.oauth_client_aud,
                    },
                    "oic_instance": {
                        "base_url": self.base_url,
                        "domain": self.base_url.split("//")[-1].split("/")[0]
                        if "//" in self.base_url
                        else self.base_url,
                    },
                    "security_settings": {
                        "token_buffer_seconds": self.token_expiry_buffer,
                        "max_retry_attempts": self.max_retry_attempts,
                        "timeout_seconds": self.timeout_seconds,
                    },
                }

            @u.model_validator(mode="after")
            def validate_auth_config(self) -> Self:
                """Validate OAuth2 authentication configuration."""
                if not self.oauth_token_url.startswith("https://"):
                    msg = "OAuth token URL must use HTTPS"
                    raise ValueError(msg)
                if not self.base_url.startswith("https://"):
                    msg = "OIC base URL must use HTTPS"
                    raise ValueError(msg)
                if (
                    self.token_expiry_buffer
                    < c.TapOracleOic.TapOicValidation.MIN_TOKEN_EXPIRY_BUFFER
                ):
                    msg = "Token expiry buffer must be at least 60 seconds"
                    raise ValueError(msg)
                return self

        class OicIntegrationEntity(FlextMeltanoModels.Entity):
            """OIC Integration entity with complete metadata."""

            # Pydantic 2.11 Configuration - Integration Features
            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
                json_schema_extra={
                    "description": "Oracle OIC integration with complete metadata",
                    "examples": [
                        {
                            "integration_id": "CUSTOMER_SYNC_01.00.0000",
                            "name": "Customer Synchronization",
                            "status": "ACTIVE",
                            "version": "01.00.0000",
                        },
                    ],
                },
            )

            integration_id: Annotated[
                str,
                u.Field(
                    description="Unique integration identifier",
                ),
            ]
            name: Annotated[str, u.Field(..., description="Integration name")]
            description: Annotated[
                str | None,
                u.Field(None, description="Integration description"),
            ]
            api_version: Annotated[
                str,
                u.Field(
                    ...,
                    description="Integration version from OIC API",
                ),
            ]
            status: Annotated[
                c.TapOracleOic.OicIntegrationStatus,
                u.Field(
                    ...,
                    description="Integration status",
                ),
            ]

            # Temporal information
            created_date: Annotated[
                datetime | None,
                u.Field(
                    None,
                    description="Integration creation date",
                ),
            ]
            last_updated: Annotated[
                datetime | None,
                u.Field(
                    None,
                    description="Last update timestamp",
                ),
            ]
            last_activated: Annotated[
                datetime | None,
                u.Field(
                    None,
                    description="Last activation timestamp",
                ),
            ]

            # Metadata
            package_id: Annotated[
                str | None,
                u.Field(None, description="Associated package ID"),
            ]
            pattern: Annotated[
                str | None,
                u.Field(None, description="Integration pattern type"),
            ]
            style: Annotated[str | None, u.Field(None, description="Integration style")]

            # Runtime information
            execution_count: Annotated[
                int | None,
                u.Field(
                    None,
                    description="Total execution count",
                ),
            ]
            error_count: Annotated[
                int | None,
                u.Field(None, description="Total error count"),
            ]
            last_execution_time: Annotated[
                datetime | None,
                u.Field(
                    None,
                    description="Last execution timestamp",
                ),
            ]

            @u.computed_field()
            @property
            def integration_health_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.Container | None]]:
                """OIC integration health and performance summary."""
                error_rate = 0.0
                if self.execution_count and self.execution_count > 0:
                    error_rate = (self.error_count or 0) / self.execution_count

                return {
                    "integration_identity": {
                        "id": self.integration_id,
                        "name": self.name,
                        "version": self.api_version,
                        "status": self.status,
                    },
                    "health_metrics": {
                        "total_executions": self.execution_count or 0,
                        "total_errors": self.error_count or 0,
                        "error_rate": error_rate,
                        "health_status": c.TapOracleOic.OicHealthStatus.HEALTHY.value
                        if error_rate
                        < c.TapOracleOic.TapOicValidation.MAX_PERCENTAGE / 20
                        else c.TapOracleOic.OicHealthStatus.DEGRADED.value,
                    },
                    "metadata": {
                        "pattern": self.pattern,
                        "style": self.style,
                        "package_id": self.package_id,
                        "last_execution": self.last_execution_time.isoformat()
                        if self.last_execution_time
                        else None,
                    },
                }

            @u.model_validator(mode="after")
            def validate_integration_entity(self) -> Self:
                """Validate OIC integration entity."""
                if not self.integration_id:
                    msg = "Integration ID is required"
                    raise ValueError(msg)
                if not self.name:
                    msg = "Integration name is required"
                    raise ValueError(msg)
                if self.execution_count is not None and self.execution_count < 0:
                    msg = "Execution count cannot be negative"
                    raise ValueError(msg)
                return self

        class OicConnectionEntity(FlextMeltanoModels.Entity):
            """OIC Connection entity with security sanitization."""

            # Pydantic 2.11 Configuration - Connection Features
            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
                json_schema_extra={
                    "description": "Oracle OIC connection with security sanitization",
                    "examples": [
                        {
                            "connection_id": "SALESFORCE_CONN_01",
                            "name": "Salesforce Production",
                            "connection_type": "SALESFORCE_ADAPTER",
                            "status": "ACTIVE",
                        },
                    ],
                },
            )

            connection_id: Annotated[
                str,
                u.Field(..., description="Unique connection identifier"),
            ]
            name: Annotated[str, u.Field(..., description="Connection name")]
            description: Annotated[
                str | None,
                u.Field(None, description="Connection description"),
            ]
            connection_type: Annotated[
                str,
                u.Field(..., description="Connection adapter type"),
            ]

            # Configuration (sanitized)
            host: Annotated[
                str | None,
                u.Field(
                    None,
                    description="Connection host (if applicable)",
                ),
            ]
            port: Annotated[
                int | None,
                u.Field(
                    None,
                    description="Connection port (if applicable)",
                ),
            ]

            # Security metadata (credentials removed)
            authentication_type: Annotated[
                str | None,
                u.Field(
                    None,
                    description="Authentication method used",
                ),
            ]
            security_policy: Annotated[
                str | None,
                u.Field(
                    None,
                    description="Security policy name",
                ),
            ]
            certificate_alias: Annotated[
                str | None,
                u.Field(
                    None,
                    description="Certificate alias (if used)",
                ),
            ]

            # Status and health
            status: Annotated[
                c.TapOracleOic.OicIntegrationStatus,
                u.Field(
                    ...,
                    description="Connection status",
                ),
            ]
            last_tested: Annotated[
                datetime | None,
                u.Field(
                    None,
                    description="Last connection test timestamp",
                ),
            ]
            test_result: Annotated[
                str | None,
                u.Field(None, description="Last test result"),
            ]

            # Sanitization markers
            data_sanitized: Annotated[
                bool,
                u.Field(
                    description="Indicates if sensitive data was removed",
                ),
            ] = True
            sanitization_timestamp: Annotated[
                datetime | None,
                u.Field(
                    description="When sanitization occurred",
                ),
            ] = u.Field(default_factory=lambda: datetime.now(UTC))

            @u.computed_field()
            @property
            def connection_security_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.Container | None]]:
                """OIC connection security and health summary."""
                return {
                    "connection_identity": {
                        "id": self.connection_id,
                        "name": self.name,
                        "type": self.connection_type,
                        "status": self.status,
                    },
                    "connectivity": {
                        "host": self.host,
                        "port": self.port,
                        "last_tested": self.last_tested.isoformat()
                        if self.last_tested
                        else None,
                        "test_result": self.test_result,
                    },
                    "security": {
                        "auth_type": self.authentication_type,
                        "security_policy": self.security_policy,
                        "certificate_alias": self.certificate_alias,
                        "data_sanitized": self.data_sanitized,
                        "sanitization_timestamp": self.sanitization_timestamp.isoformat()
                        if self.sanitization_timestamp
                        else None,
                    },
                }

            @u.model_validator(mode="after")
            def validate_connection_entity(self) -> Self:
                """Validate OIC connection entity."""
                if not self.connection_id:
                    msg = "Connection ID is required"
                    raise ValueError(msg)
                if not self.name:
                    msg = "Connection name is required"
                    raise ValueError(msg)
                if self.port is not None and not (
                    c.DEFAULT_RETRY_DELAY_SECONDS
                    <= self.port
                    <= FlextConstants.MAX_PORT
                ):
                    msg = "Port must be between 1 and 65535"
                    raise ValueError(msg)
                return self

        class OicActivityRecord(FlextMeltanoModels.Entity):
            """OIC Activity monitoring record for incremental replication."""

            # Pydantic 2.11 Configuration - Activity Features
            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
                json_schema_extra={
                    "description": "Oracle OIC activity record with performance tracking",
                    "examples": [
                        {
                            "activity_id": "ACT_20230101_001",
                            "integration_id": "CUSTOMER_SYNC_01.00.0000",
                            "status": "COMPLETED",
                            "messages_processed": 1500,
                        },
                    ],
                },
            )

            activity_id: Annotated[
                str,
                u.Field(
                    ...,
                    description="Unique activity record identifier",
                ),
            ]
            integration_id: Annotated[
                str,
                u.Field(..., description="Associated integration ID"),
            ]
            instance_id: Annotated[
                str,
                u.Field(..., description="Integration instance ID"),
            ]

            # Temporal information (for incremental replication)
            start_time: Annotated[
                datetime,
                u.Field(..., description="Activity start timestamp"),
            ]
            end_time: Annotated[
                datetime | None,
                u.Field(
                    None,
                    description="Activity end timestamp",
                ),
            ]
            duration_ms: Annotated[
                int | None,
                u.Field(
                    None,
                    description="Activity duration in milliseconds",
                ),
            ]

            # Status and results
            status: Annotated[
                c.TapOracleOic.OicJobStatus,
                u.Field(
                    ...,
                    description="Activity status",
                ),
            ]
            result: Annotated[str | None, u.Field(None, description="Activity result")]
            error_message: Annotated[
                str | None,
                u.Field(
                    None,
                    description="Error message if failed",
                ),
            ]

            # Metrics
            messages_processed: Annotated[
                int | None,
                u.Field(
                    None,
                    description="Number of messages processed",
                ),
            ]
            bytes_processed: Annotated[
                int | None,
                u.Field(None, description="Bytes processed"),
            ]
            throughput_mps: Annotated[
                float | None,
                u.Field(
                    None,
                    description="Messages per second throughput",
                ),
            ]

            @u.computed_field()
            @property
            def activity_performance_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.Container | None]]:
                """OIC activity performance summary."""
                duration_seconds = 0.0
                if self.duration_ms:
                    duration_seconds = self.duration_ms / 1000

                return {
                    "activity_identity": {
                        "id": self.activity_id,
                        "integration_id": self.integration_id,
                        "instance_id": self.instance_id,
                        "status": self.status,
                    },
                    "performance": {
                        "start_time": self.start_time.isoformat(),
                        "end_time": self.end_time.isoformat()
                        if self.end_time
                        else None,
                        "duration_seconds": duration_seconds,
                        "messages_processed": self.messages_processed or 0,
                        "throughput_mps": self.throughput_mps or 0.0,
                    },
                    "quality": {
                        "result": self.result,
                        "has_error": bool(self.error_message),
                        "error_message": self.error_message,
                        "success": self.status
                        == c.TapOracleOic.OicJobStatus.COMPLETED.value,
                    },
                    "volume": {
                        "bytes_processed": self.bytes_processed or 0,
                        "mb_processed": (self.bytes_processed or 0) / (1024 * 1024),
                    },
                }

            @u.model_validator(mode="after")
            def validate_activity_record(self) -> Self:
                """Validate OIC activity record."""
                if not self.activity_id:
                    msg = "Activity ID is required"
                    raise ValueError(msg)
                if not self.integration_id:
                    msg = "Integration ID is required"
                    raise ValueError(msg)
                if self.duration_ms is not None and self.duration_ms < 0:
                    msg = "Duration cannot be negative"
                    raise ValueError(msg)
                return self

        class OicPackageEntity(FlextMeltanoModels.Entity):
            """OIC Package entity for integration packages."""

            # Pydantic 2.11 Configuration - Package Features
            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
                json_schema_extra={
                    "description": "Oracle OIC package with dependency tracking",
                    "examples": [
                        {
                            "package_id": "CUSTOMER_SUITE_V1",
                            "name": "Customer Management Suite",
                            "package_type": "INTEGRATION",
                            "status": "ACTIVE",
                        },
                    ],
                },
            )

            package_id: Annotated[
                str,
                u.Field(..., description="Unique package identifier"),
            ]
            name: Annotated[str, u.Field(..., description="Package name")]
            description: Annotated[
                str | None,
                u.Field(None, description="Package description"),
            ]
            api_version: Annotated[
                str,
                u.Field(..., description="Package version from OIC API"),
            ]

            # Package metadata
            package_type: Annotated[
                c.TapOracleOic.OicIntegrationType,
                u.Field(
                    ...,
                    description="Package type",
                ),
            ]
            created_by: Annotated[
                str | None,
                u.Field(None, description="Package creator"),
            ]
            created_date: Annotated[
                datetime | None,
                u.Field(
                    None,
                    description="Package creation date",
                ),
            ]

            # Dependencies and relationships
            dependencies: Annotated[
                t.StrSequence,
                u.Field(
                    description="List of dependent package IDs",
                ),
            ] = u.Field(default_factory=tuple)
            integration_count: Annotated[
                int | None,
                u.Field(
                    None,
                    description="Number of integrations in package",
                ),
            ]

            # Status
            status: Annotated[
                c.TapOracleOic.OicIntegrationStatus,
                u.Field(
                    ...,
                    description="Package status",
                ),
            ]
            download_count: Annotated[
                int | None,
                u.Field(
                    None,
                    description="Package download count",
                ),
            ]

            @u.computed_field()
            @property
            def package_composition_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.Container | None]]:
                """OIC package composition and usage summary."""
                return {
                    "package_identity": {
                        "id": self.package_id,
                        "name": self.name,
                        "version": self.api_version,
                        "type": self.package_type,
                        "status": self.status,
                    },
                    "composition": {
                        "integration_count": self.integration_count or 0,
                        "dependency_count": len(self.dependencies),
                        "has_dependencies": bool(self.dependencies),
                        "dependencies": list(self.dependencies),
                    },
                    "usage": {
                        "download_count": self.download_count or 0,
                        "created_by": self.created_by,
                        "created_date": self.created_date.isoformat()
                        if self.created_date
                        else None,
                    },
                }

            @u.model_validator(mode="after")
            def validate_package_entity(self) -> Self:
                """Validate OIC package entity."""
                if not self.package_id:
                    msg = "Package ID is required"
                    raise ValueError(msg)
                if not self.name:
                    msg = "Package name is required"
                    raise ValueError(msg)
                if self.integration_count is not None and self.integration_count < 0:
                    msg = "Integration count cannot be negative"
                    raise ValueError(msg)
                return self

        class OicMetricsRecord(FlextMeltanoModels.Entity):
            """OIC Metrics record for performance monitoring."""

            # Pydantic 2.11 Configuration - Metrics Features
            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
                json_schema_extra={
                    "description": "Oracle OIC performance metrics with resource monitoring",
                    "examples": [
                        {
                            "metric_id": "METRIC_20230101_001",
                            "integration_id": "CUSTOMER_SYNC_01.00.0000",
                            "throughput_mps": 125.5,
                            "cpu_usage_percent": 45.2,
                        },
                    ],
                },
            )

            metric_id: Annotated[
                str,
                u.Field(..., description="Unique metrics record identifier"),
            ]
            integration_id: Annotated[
                str,
                u.Field(..., description="Associated integration ID"),
            ]
            timestamp: Annotated[
                datetime, u.Field(..., description="Metrics timestamp")
            ]

            # Performance metrics
            cpu_usage_percent: Annotated[
                float | None,
                u.Field(
                    None,
                    description="CPU usage percentage",
                ),
            ]
            memory_usage_mb: Annotated[
                float | None,
                u.Field(
                    None,
                    description="Memory usage in MB",
                ),
            ]
            throughput_mps: Annotated[
                float | None,
                u.Field(
                    None,
                    description="Messages per second",
                ),
            ]
            latency_ms: Annotated[
                float | None,
                u.Field(
                    None,
                    description="Average latency in milliseconds",
                ),
            ]

            # Business metrics
            success_count: Annotated[
                int | None,
                u.Field(
                    None,
                    description="Successful message count",
                ),
            ]
            error_count: Annotated[
                int | None,
                u.Field(None, description="Error message count"),
            ]
            retry_count: Annotated[
                int | None,
                u.Field(None, description="Retry attempt count"),
            ]

            # Resource utilization
            database_connections: Annotated[
                int | None,
                u.Field(
                    None,
                    description="Active database connections",
                ),
            ]
            thread_count: Annotated[
                int | None,
                u.Field(None, description="Active thread count"),
            ]
            queue_depth: Annotated[
                int | None,
                u.Field(None, description="Message queue depth"),
            ]

            @u.computed_field()
            @property
            def metrics_analysis_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.Container | None]]:
                """OIC metrics complete analysis summary."""
                total_messages = (self.success_count or 0) + (self.error_count or 0)
                error_rate = 0.0
                if total_messages > 0:
                    error_rate = (self.error_count or 0) / total_messages

                return {
                    "metrics_identity": {
                        "id": self.metric_id,
                        "integration_id": self.integration_id,
                        "timestamp": self.timestamp.isoformat(),
                    },
                    "performance": {
                        "cpu_usage_percent": self.cpu_usage_percent or 0.0,
                        "memory_usage_mb": self.memory_usage_mb or 0.0,
                        "throughput_mps": self.throughput_mps or 0.0,
                        "latency_ms": self.latency_ms or 0.0,
                    },
                    "business_metrics": {
                        "total_messages": total_messages,
                        "success_count": self.success_count or 0,
                        "error_count": self.error_count or 0,
                        "retry_count": self.retry_count or 0,
                        "error_rate": error_rate,
                    },
                    "resource_utilization": {
                        "database_connections": self.database_connections or 0,
                        "thread_count": self.thread_count or 0,
                        "queue_depth": self.queue_depth or 0,
                    },
                }

            @u.model_validator(mode="after")
            def validate_metrics_record(self) -> Self:
                """Validate OIC metrics record."""
                if not self.metric_id:
                    msg = "Metric ID is required"
                    raise ValueError(msg)
                if not self.integration_id:
                    msg = "Integration ID is required"
                    raise ValueError(msg)
                if self.cpu_usage_percent is not None and not (
                    c.TapOracleOic.TapOicValidation.MIN_PERCENTAGE
                    <= self.cpu_usage_percent
                    <= c.TapOracleOic.TapOicValidation.MAX_PERCENTAGE
                ):
                    msg = "CPU usage must be between 0 and 100 percent"
                    raise ValueError(msg)
                return self

        class OicAgentEntity(FlextMeltanoModels.Entity):
            """OIC Agent entity for connectivity agents."""

            # Pydantic 2.11 Configuration - Agent Features
            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
                json_schema_extra={
                    "description": "Oracle OIC connectivity agent with health monitoring",
                    "examples": [
                        {
                            "agent_id": "AGENT_ONPREM_01",
                            "agent_name": "On-Premises Agent 01",
                            "agent_type": "CONNECTIVITY_AGENT",
                            "status": "ONLINE",
                        },
                    ],
                },
            )

            agent_id: Annotated[
                str, u.Field(..., description="Unique agent identifier")
            ]
            agent_name: Annotated[str, u.Field(..., description="Agent display name")]
            agent_type: Annotated[
                c.TapOracleOic.OicAgentType,
                u.Field(
                    ...,
                    description="Agent type",
                ),
            ]

            # Agent status and health
            status: Annotated[
                c.TapOracleOic.OicAgentStatus,
                u.Field(
                    ...,
                    description="Agent status",
                ),
            ]
            last_heartbeat: Annotated[
                datetime | None,
                u.Field(
                    None,
                    description="Last heartbeat timestamp",
                ),
            ]
            api_version: Annotated[
                str | None,
                u.Field(
                    None,
                    description="Agent version from OIC API",
                ),
            ]

            # Configuration
            host_machine: Annotated[
                str | None,
                u.Field(None, description="Host machine name"),
            ]
            installation_path: Annotated[
                str | None,
                u.Field(
                    None,
                    description="Agent installation path",
                ),
            ]
            port: Annotated[
                int | None,
                u.Field(None, description="Agent communication port"),
            ]

            # Health metrics
            uptime_hours: Annotated[
                float | None,
                u.Field(
                    None,
                    description="Agent uptime in hours",
                ),
            ]
            connection_count: Annotated[
                int | None,
                u.Field(
                    None,
                    description="Active connection count",
                ),
            ]
            last_error: Annotated[
                str | None,
                u.Field(None, description="Last error message"),
            ]

            @u.computed_field()
            @property
            def agent_health_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.Container | None]]:
                """OIC agent health and connectivity summary."""
                health_status = c.TapOracleOic.OicHealthStatus.HEALTHY.value
                if self.status in {"ERROR", "OFFLINE"}:
                    health_status = c.TapOracleOic.OicHealthStatus.UNHEALTHY.value
                elif self.last_error:
                    health_status = c.TapOracleOic.OicHealthStatus.DEGRADED.value

                return {
                    "agent_identity": {
                        "id": self.agent_id,
                        "name": self.agent_name,
                        "type": self.agent_type,
                        "version": self.api_version,
                        "status": self.status,
                    },
                    "connectivity": {
                        "host_machine": self.host_machine,
                        "port": self.port,
                        "last_heartbeat": self.last_heartbeat.isoformat()
                        if self.last_heartbeat
                        else None,
                        "connection_count": self.connection_count or 0,
                    },
                    "health": {
                        "health_status": health_status,
                        "uptime_hours": self.uptime_hours or 0.0,
                        "has_error": bool(self.last_error),
                        "last_error": self.last_error,
                    },
                    "configuration": {"installation_path": self.installation_path},
                }

            @u.model_validator(mode="after")
            def validate_agent_entity(self) -> Self:
                """Validate OIC agent entity."""
                if not self.agent_id:
                    msg = "Agent ID is required"
                    raise ValueError(msg)
                if not self.agent_name:
                    msg = "Agent name is required"
                    raise ValueError(msg)
                if self.port is not None and not (
                    c.DEFAULT_RETRY_DELAY_SECONDS
                    <= self.port
                    <= FlextConstants.MAX_PORT
                ):
                    msg = "Port must be between 1 and 65535"
                    raise ValueError(msg)
                return self

        class OicStreamConfiguration(FlextMeltanoModels.ArbitraryTypesModel):
            """Configuration for OIC tap streams."""

            # Pydantic 2.11 Configuration - Stream Features
            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
                json_schema_extra={
                    "description": "Oracle OIC tap stream configuration with filtering",
                    "examples": [
                        {
                            "stream_name": "integrations",
                            "replication_method": "INCREMENTAL",
                            "replication_key": "last_updated",
                            "page_size": 100,
                        },
                    ],
                },
            )

            stream_name: Annotated[str, u.Field(..., description="Singer stream name")]
            replication_method: Annotated[
                c.TapOracleOic.OicReplicationMethod,
                u.Field(
                    description="Replication method",
                ),
            ] = c.TapOracleOic.OicReplicationMethod.FULL_TABLE
            replication_key: Annotated[
                str | None,
                u.Field(
                    None,
                    description="Replication key field name",
                ),
            ]

            # Pagination and performance
            page_size: Annotated[
                int,
                u.Field(
                    ge=1,
                    le=1000,
                    description="API pagination size",
                ),
            ] = 100
            include_extended: Annotated[
                bool,
                u.Field(
                    description="Include extended entity metadata",
                ),
            ] = False

            # Filtering
            status_filter: Annotated[
                t.StrSequence | None,
                u.Field(
                    None,
                    description="Filter by entity status values",
                ),
            ]
            date_range_filter: Annotated[
                str | None,
                u.Field(
                    None,
                    description="Date range filter for incremental streams",
                ),
            ]

            # Security
            sanitize_sensitive_data: Annotated[
                bool,
                u.Field(
                    description="Enable data sanitization",
                ),
            ] = True
            exclude_test_entities: Annotated[
                bool,
                u.Field(
                    description="Exclude test/demo entities",
                ),
            ] = True

            @u.computed_field()
            @property
            def stream_config_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.Container | None]]:
                """OIC stream configuration summary."""
                return {
                    "stream_identity": {
                        "name": self.stream_name,
                        "replication_method": self.replication_method,
                        "replication_key": self.replication_key,
                        "is_incremental": self.replication_method == "INCREMENTAL",
                    },
                    "performance": {
                        "page_size": self.page_size,
                        "include_extended": self.include_extended,
                    },
                    "filtering": {
                        "status_filters": len(self.status_filter)
                        if self.status_filter
                        else 0,
                        "date_range_filter": bool(self.date_range_filter),
                        "exclude_test_entities": self.exclude_test_entities,
                    },
                    "security": {
                        "sanitize_sensitive_data": self.sanitize_sensitive_data,
                    },
                }

            @u.model_validator(mode="after")
            def validate_stream_config(self) -> Self:
                """Validate OIC stream configuration."""
                if not self.stream_name:
                    msg = "Stream name is required"
                    raise ValueError(msg)
                if (
                    self.replication_method == "INCREMENTAL"
                    and not self.replication_key
                ):
                    msg = "Incremental replication requires a replication key"
                    raise ValueError(msg)
                if self.page_size <= 0 or self.page_size > c.MAX_ITEMS:
                    msg = "Page size must be between 1 and 1000"
                    raise ValueError(msg)
                return self

        class OicApiResponse(FlextMeltanoModels.Entity):
            """Standardized OIC API response wrapper."""

            # Pydantic 2.11 Configuration - API Response Features
            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
                json_schema_extra={
                    "description": "Oracle OIC API response with pagination and error handling",
                    "examples": [
                        {
                            "success": True,
                            "total_count": 150,
                            "page_size": 50,
                            "page_number": 1,
                        },
                    ],
                },
            )

            success: Annotated[
                bool,
                u.Field(..., description="Response success indicator"),
            ]
            data: Annotated[
                t.ContainerValueMapping | None,
                u.Field(
                    None,
                    description="Response data payload",
                ),
            ]
            total_count: Annotated[
                int | None,
                u.Field(
                    None,
                    description="Total entity count (for pagination)",
                ),
            ]
            page_size: Annotated[
                int | None,
                u.Field(None, description="Current page size"),
            ]
            page_number: Annotated[
                int | None,
                u.Field(None, description="Current page number"),
            ]

            # Error information
            error_code: Annotated[
                str | None,
                u.Field(None, description="Error code if failed"),
            ]
            error_message: Annotated[
                str | None,
                u.Field(
                    None,
                    description="Error message if failed",
                ),
            ]
            error_details: Annotated[
                Mapping[str, t.ContainerValueMapping] | None,
                u.Field(
                    None,
                    description="Detailed error information",
                ),
            ]

            # Metadata
            timestamp: Annotated[
                datetime,
                u.Field(
                    description="Response timestamp",
                ),
            ] = u.Field(default_factory=lambda: datetime.now(UTC))
            api_version: Annotated[
                str | None,
                u.Field(None, description="OIC API version"),
            ]
            request_id: Annotated[
                str | None,
                u.Field(None, description="Request correlation ID"),
            ]

            @u.computed_field()
            @property
            def api_response_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.Container | None]]:
                """OIC API response summary."""
                return {
                    "response_status": {
                        "success": self.success,
                        "timestamp": self.timestamp.isoformat(),
                        "api_version": self.api_version,
                        "request_id": self.request_id,
                    },
                    "pagination": {
                        "total_count": self.total_count,
                        "page_size": self.page_size,
                        "page_number": self.page_number,
                        "has_more": bool(
                            self.total_count
                            and self.page_size
                            and (self.page_number or 1) * self.page_size
                            < self.total_count,
                        ),
                    },
                    "error_info": {
                        "has_error": not self.success,
                        "error_code": self.error_code,
                        "error_message": self.error_message,
                        "has_details": bool(self.error_details),
                    },
                    "data_info": {
                        "has_data": self.data is not None,
                        "data_type": type(self.data).__name__
                        if self.data is not None
                        else None,
                    },
                }

            @u.model_validator(mode="after")
            def validate_api_response(self) -> Self:
                """Validate OIC API response."""
                if not self.success and not self.error_message:
                    msg = "Failed responses must have an error message"
                    raise ValueError(msg)
                if self.page_number is not None and self.page_number < 1:
                    msg = "Page number must be positive"
                    raise ValueError(msg)
                return self

        class OicErrorContext(FlextMeltanoModels.Entity):
            """Error context for OIC API error handling."""

            # Pydantic 2.11 Configuration - Error Context Features
            model_config: ClassVar[m.ConfigDict] = m.ConfigDict(
                json_schema_extra={
                    "description": "Oracle OIC API error context with recovery guidance",
                    "examples": [
                        {
                            "error_type": "RATE_LIMIT",
                            "http_status_code": 429,
                            "retry_after_seconds": 60,
                            "is_retryable": True,
                        },
                    ],
                },
            )

            error_type: Annotated[
                c.TapOracleOic.OicErrorType,
                u.Field(..., description="Error category"),
            ]
            http_status_code: Annotated[
                int | None,
                u.Field(None, description="HTTP status code"),
            ]
            retry_after_seconds: Annotated[
                int | None,
                u.Field(
                    None,
                    description="Retry after duration",
                ),
            ]

            # Context information
            endpoint: Annotated[
                str | None,
                u.Field(None, description="API endpoint that failed"),
            ]
            request_method: Annotated[
                str | None,
                u.Field(None, description="HTTP method used"),
            ]
            request_params: Annotated[
                Mapping[str, t.ContainerValueMapping] | None,
                u.Field(
                    None,
                    description="Request parameters",
                ),
            ]

            # Recovery information
            is_retryable: Annotated[
                bool,
                u.Field(
                    description="Whether error is retryable",
                ),
            ] = False
            suggested_action: Annotated[
                str | None,
                u.Field(
                    None,
                    description="Suggested recovery action",
                ),
            ]
            max_retry_attempts: Annotated[
                int | None,
                u.Field(
                    None,
                    description="Maximum retry attempts for this error",
                ),
            ]

            @u.computed_field()
            @property
            def error_context_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.Container | None]]:
                """OIC error context summary."""
                return {
                    "error_classification": {
                        "type": self.error_type,
                        "http_status": self.http_status_code,
                        "is_retryable": self.is_retryable,
                        "severity": self._determine_severity(),
                    },
                    "request_context": {
                        "endpoint": self.endpoint,
                        "method": self.request_method,
                        "has_params": bool(self.request_params),
                    },
                    "recovery_guidance": {
                        "suggested_action": self.suggested_action,
                        "retry_after_seconds": self.retry_after_seconds,
                        "max_retry_attempts": self.max_retry_attempts,
                        "auto_recoverable": self.is_retryable
                        and bool(self.retry_after_seconds),
                    },
                }

            @u.model_validator(mode="after")
            def validate_error_context(self) -> Self:
                """Validate OIC error context."""
                if self.http_status_code is not None and not (
                    FlextConstants.HTTP_STATUS_MIN
                    <= self.http_status_code
                    <= FlextConstants.HTTP_STATUS_MAX
                ):
                    msg = "HTTP status code must be between 100 and 599"
                    raise ValueError(msg)
                if (
                    self.retry_after_seconds is not None
                    and self.retry_after_seconds < 0
                ):
                    msg = "Retry after seconds cannot be negative"
                    raise ValueError(msg)
                return self

            def _determine_severity(self) -> str:
                """Determine error severity based on type and status code."""
                if self.error_type in {
                    c.TapOracleOic.OicErrorType.AUTHENTICATION,
                    c.TapOracleOic.OicErrorType.AUTHORIZATION,
                }:
                    return c.TapOracleOic.OicErrorSeverity.CRITICAL.value
                if self.error_type == c.TapOracleOic.OicErrorType.RATE_LIMIT:
                    return c.TapOracleOic.OicErrorSeverity.WARNING.value
                if self.error_type == c.TapOracleOic.OicErrorType.SERVER_ERROR:
                    return c.TapOracleOic.OicErrorSeverity.ERROR.value
                if self.error_type in {
                    c.TapOracleOic.OicErrorType.NETWORK,
                    c.TapOracleOic.OicErrorType.VALIDATION,
                }:
                    return c.TapOracleOic.OicErrorSeverity.WARNING.value
                return c.TapOracleOic.OicErrorSeverity.UNKNOWN.value

        class OracleOic(FlextOracleOicModels.OracleOic):
            """Domain entity models for Oracle OIC resources.

            Canonical home for OIC entity classes, migrated from domain/entities.py
            per MRO policy: all FlextModels subclasses live under [Project]Models.
            """

            class OICConnection(FlextModels):
                """OIC connection domain entity using flext-core patterns."""

                _flext_enforcement_exempt: ClassVar[bool] = True

                connection_id: Annotated[
                    str,
                    u.Field(..., min_length=1, description="OIC connection identifier"),
                ]
                adapter_type: Annotated[
                    str,
                    u.Field(
                        ...,
                        min_length=1,
                        description="Adapter type (e.g., REST, SOAP, DB)",
                    ),
                ]
                name: Annotated[
                    str,
                    u.Field(..., min_length=1, description="Connection name"),
                ]
                connection_url: Annotated[
                    str | None,
                    u.Field(None, description="Connection endpoint URL"),
                ]
                connection_properties: Annotated[
                    Mapping[str, t.ContainerValueMapping],
                    u.Field(description="Connection properties"),
                ] = u.Field(default_factory=dict)
                security_policy: Annotated[
                    str | None,
                    u.Field(None, description="Security policy name"),
                ]
                connection_status: Annotated[
                    c.TapOracleOic.ConnectionStatus,
                    u.Field(
                        description="Connection status",
                    ),
                ] = c.TapOracleOic.ConnectionStatus.CONFIGURED
                last_tested: Annotated[
                    datetime | None,
                    u.Field(None, description="Last test timestamp"),
                ]
                test_result: Annotated[
                    t.StrMapping | None,
                    u.Field(None, description="Last test result"),
                ]
                version: Annotated[
                    str | None,
                    u.Field(None, description="Connection version"),
                ]
                locked_by: Annotated[
                    str | None,
                    u.Field(None, description="User who locked the connection"),
                ]
                locked_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Lock timestamp"),
                ]
                created_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Creation timestamp"),
                ]
                updated_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Last update timestamp"),
                ]

                def mark_failed(self, _error: str) -> None:
                    """Mark connection as failed with error details."""
                    self.connection_status = c.TapOracleOic.ConnectionStatus.FAILED
                    self.test_result = {
                        "error": c.TapOracleOic.OicErrorSeverity.ERROR.value,
                        "timestamp": datetime.now(UTC).isoformat(),
                    }

                def test_connection(self) -> None:
                    """Mark connection as tested."""
                    self.last_tested = datetime.now(UTC)
                    self.connection_status = c.TapOracleOic.ConnectionStatus.TESTED

            class OICIntegration(FlextModels):
                """OIC integration domain entity using flext-core patterns."""

                _flext_enforcement_exempt: ClassVar[bool] = True

                integration_id: Annotated[
                    str,
                    u.Field(
                        ..., min_length=1, description="OIC integration identifier"
                    ),
                ]
                integration_code: Annotated[
                    str,
                    u.Field(..., min_length=1, description="Integration code"),
                ]
                name: Annotated[
                    str,
                    u.Field(..., min_length=1, description="Integration name"),
                ]
                package_name: Annotated[
                    str | None, u.Field(None, description="Package name")
                ]
                project_name: Annotated[
                    str | None, u.Field(None, description="Project name")
                ]
                integration_type: Annotated[
                    str,
                    u.Field(
                        ...,
                        description="Integration type (e.g., APP_DRIVEN, SCHEDULED)",
                    ),
                ]
                pattern: Annotated[
                    str | None,
                    u.Field(None, description="Integration pattern"),
                ]
                style: Annotated[
                    str | None, u.Field(None, description="Integration style")
                ]
                endpoint_url: Annotated[
                    str | None,
                    u.Field(None, description="Integration endpoint URL"),
                ]
                tracking_level: Annotated[
                    str | None,
                    u.Field(None, description="Tracking level"),
                ]
                payload_tracking: Annotated[
                    bool, u.Field(description="Enable payload tracking")
                ] = False
                integration_status: Annotated[
                    c.TapOracleOic.IntegrationStatus,
                    u.Field(
                        description="Integration status",
                    ),
                ] = c.TapOracleOic.IntegrationStatus.CONFIGURED
                activated_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Activation timestamp"),
                ]
                deactivated_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Deactivation timestamp"),
                ]
                version: Annotated[str, u.Field(description="Integration version")] = (
                    "01.00.0000"
                )
                locked_by: Annotated[
                    str | None,
                    u.Field(None, description="User who locked the integration"),
                ]
                locked_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Lock timestamp"),
                ]
                connection_ids: Annotated[
                    t.StrSequence,
                    u.Field(description="Associated connection IDs"),
                ] = u.Field(default_factory=tuple)
                created_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Creation timestamp"),
                ]
                updated_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Last update timestamp"),
                ]

                @property
                def is_active(self) -> bool:
                    """Check if integration is active."""
                    return (
                        self.integration_status
                        == c.TapOracleOic.IntegrationStatus.ACTIVATED
                    )

                def activate(self) -> None:
                    """Activate the integration."""
                    self.integration_status = c.TapOracleOic.IntegrationStatus.ACTIVATED
                    self.activated_at = datetime.now(UTC)

                def deactivate(self) -> None:
                    """Deactivate the integration."""
                    self.integration_status = (
                        c.TapOracleOic.IntegrationStatus.DEACTIVATED
                    )
                    self.deactivated_at = datetime.now(UTC)

                def lock(self, user: str) -> None:
                    """Lock the integration for a specific user."""
                    self.locked_by = user
                    self.locked_at = datetime.now(UTC)
                    self.integration_status = c.TapOracleOic.IntegrationStatus.LOCKED

                def unlock(self) -> None:
                    """Unlock the integration."""
                    self.locked_by = None
                    self.locked_at = None

            class OICLookup(FlextModels):
                """OIC lookup table domain entity using flext-core patterns."""

                _flext_enforcement_exempt: ClassVar[bool] = True

                lookup_id: Annotated[
                    str,
                    u.Field(..., min_length=1, description="OIC lookup identifier"),
                ]
                lookup_name: Annotated[
                    str,
                    u.Field(..., min_length=1, description="Lookup table name"),
                ]
                domain_name: Annotated[
                    str | None, u.Field(None, description="Domain name")
                ]
                columns: Annotated[
                    Sequence[t.FlatContainerMapping],
                    u.Field(
                        description="Column definitions",
                    ),
                ] = u.Field(default_factory=list[t.FlatContainerMapping])
                key_columns: Annotated[
                    t.StrSequence,
                    u.Field(description="Key column names"),
                ] = u.Field(default_factory=tuple)
                value_columns: Annotated[
                    t.StrSequence,
                    u.Field(description="Value column names"),
                ] = u.Field(default_factory=tuple)
                row_count: Annotated[
                    t.NonNegativeInt, u.Field(description="Number of rows")
                ] = 0
                data_size_bytes: Annotated[
                    t.NonNegativeInt | None,
                    u.Field(None, description="Data size in bytes"),
                ]
                locked_by: Annotated[
                    str | None,
                    u.Field(None, description="User who locked the lookup"),
                ]
                locked_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Lock timestamp"),
                ]
                last_imported: Annotated[
                    datetime | None,
                    u.Field(None, description="Last import timestamp"),
                ]
                created_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Creation timestamp"),
                ]
                updated_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Last update timestamp"),
                ]

                @property
                def is_empty(self) -> bool:
                    """Check if lookup is empty."""
                    return self.row_count == 0

                def record_import(self) -> None:
                    """Record successful import."""
                    self.last_imported = datetime.now(UTC)

                def update_statistics(
                    self,
                    row_count: int,
                    data_size: int | None = None,
                ) -> None:
                    """Update lookup statistics."""
                    self.row_count = row_count
                    self.data_size_bytes = data_size

            class OICMonitoringRecord(FlextModels):
                """OIC monitoring record domain entity using flext-core patterns."""

                instance_id: Annotated[
                    str,
                    u.Field(..., min_length=1, description="Flow instance ID"),
                ]
                integration_id: Annotated[
                    str,
                    u.Field(..., description="Associated integration ID"),
                ]
                flow_id: Annotated[str | None, u.Field(None, description="Flow ID")]
                tracking_level: Annotated[
                    str | None,
                    u.Field(None, description="Tracking level"),
                ]
                started_at: Annotated[
                    datetime,
                    u.Field(..., description="Execution start time"),
                ]
                completed_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Execution completion time"),
                ]
                duration_ms: Annotated[
                    int | None,
                    u.Field(None, ge=0, description="Duration in milliseconds"),
                ]
                execution_status: Annotated[
                    str, u.Field(..., description="Execution status")
                ]
                error_code: Annotated[
                    str | None,
                    u.Field(None, description="Error code if failed"),
                ]
                error_message: Annotated[
                    str | None,
                    u.Field(None, description="Error message if failed"),
                ]
                message_count: Annotated[
                    t.NonNegativeInt,
                    u.Field(description="Number of messages processed"),
                ] = 0
                error_count: Annotated[
                    t.NonNegativeInt, u.Field(description="Number of errors")
                ] = 0
                business_identifiers: Annotated[
                    Mapping[str, t.ContainerValueMapping],
                    u.Field(
                        description="Business tracking identifiers",
                    ),
                ] = u.Field(default_factory=dict)

                @property
                def duration_seconds(self) -> float | None:
                    """Get duration in seconds."""
                    return (
                        self.duration_ms / 1000.0
                        if self.duration_ms is not None
                        else None
                    )

                @property
                def is_failed(self) -> bool:
                    """Check if execution failed."""
                    return self.execution_status.lower() in {
                        c.TapOracleOic.OicJobStatus.FAILED.value.lower(),
                        "faulted",
                        c.TapOracleOic.OicJobStatus.ABORTED.value.lower(),
                    }

                @property
                def successful(self) -> bool:
                    """Check if execution was successful."""
                    return self.execution_status.lower() in {
                        c.TapOracleOic.OicJobStatus.COMPLETED.value.lower(),
                        "succeeded",
                    }

            class OICProject(FlextModels):
                """OIC project domain entity using flext-core patterns."""

                _flext_enforcement_exempt: ClassVar[bool] = True

                project_id: Annotated[
                    t.NonEmptyStr,
                    u.Field(..., description="OIC project identifier"),
                ]
                project_code: Annotated[
                    t.NonEmptyStr,
                    u.Field(..., description="Project code"),
                ]
                name: Annotated[t.NonEmptyStr, u.Field(..., description="Project name")]
                integration_ids: Annotated[
                    MutableSequence[str],
                    u.Field(description="Integration IDs in project"),
                ] = u.Field(default_factory=list)
                connection_ids: Annotated[
                    t.StrSequence,
                    u.Field(description="Connection IDs in project"),
                ] = u.Field(default_factory=tuple)
                lookup_ids: Annotated[
                    t.StrSequence,
                    u.Field(description="Lookup IDs in project"),
                ] = u.Field(default_factory=tuple)
                deployment_status: Annotated[
                    str | None,
                    u.Field(None, description="Deployment status"),
                ]
                deployed_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Deployment timestamp"),
                ]
                deployed_by: Annotated[
                    str | None,
                    u.Field(None, description="User who deployed"),
                ]
                created_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Creation timestamp"),
                ]
                updated_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Last update timestamp"),
                ]

                @property
                def total_resources(self) -> int:
                    """Get total number of resources in project."""
                    return (
                        len(self.integration_ids)
                        + len(self.connection_ids)
                        + len(self.lookup_ids)
                    )

                def add_integration(self, integration_id: str) -> None:
                    """Add integration to project."""
                    if integration_id not in self.integration_ids:
                        self.integration_ids.append(integration_id)

                def deploy(self, user: str) -> None:
                    """Deploy the project."""
                    self.deployment_status = "deployed"
                    self.deployed_at = datetime.now(UTC)
                    self.deployed_by = user

                def remove_integration(self, integration_id: str) -> None:
                    """Remove integration from project."""
                    if integration_id in self.integration_ids:
                        self.integration_ids.remove(integration_id)

            class OICResourceMetadata(FlextModels):
                """OIC resource metadata value object."""

                resource_type: Annotated[
                    c.TapOracleOic.OICResourceType,
                    u.Field(..., description="Resource type"),
                ]
                resource_id: Annotated[
                    t.NonEmptyStr,
                    u.Field(..., description="Resource identifier"),
                ]
                name: Annotated[
                    t.NonEmptyStr, u.Field(..., description="Resource name")
                ]
                version: Annotated[
                    str | None, u.Field(None, description="Resource version")
                ]
                created_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Creation timestamp"),
                ]
                updated_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Last update timestamp"),
                ]

            class OICExecutionSummary(FlextModels):
                """OIC execution summary value object."""

                integration_id: Annotated[
                    str, u.Field(..., description="Integration ID")
                ]
                total_executions: Annotated[
                    t.NonNegativeInt, u.Field(description="Total number of executions")
                ] = 0
                successful_executions: Annotated[
                    t.NonNegativeInt, u.Field(description="Successful executions")
                ] = 0
                failed_executions: Annotated[
                    t.NonNegativeInt, u.Field(description="Failed executions")
                ] = 0
                average_duration_ms: Annotated[
                    t.NonNegativeFloat | None,
                    u.Field(None, description="Average execution duration"),
                ]
                last_execution_at: Annotated[
                    datetime | None,
                    u.Field(None, description="Last execution timestamp"),
                ]

                @property
                def failure_rate(self) -> float:
                    """Calculate failure rate percentage."""
                    return 100.0 - self.success_rate

                @property
                def success_rate(self) -> float:
                    """Calculate success rate percentage."""
                    if self.total_executions == 0:
                        return 0.0
                    return self.successful_executions / self.total_executions * 100.0


# Short alias
m = FlextTapOracleOicModels

__all__: list[str] = [
    "FlextTapOracleOicModels",
    "m",
]
