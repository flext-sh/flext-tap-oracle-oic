"""Oracle Integration Cloud Models using standardized [Project]Models pattern.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import re
from collections.abc import Iterator, Mapping, Sequence
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Annotated, ClassVar, Literal, Self

import requests
from flext_api import FlextApi, FlextApiSettings
from flext_core import (
    FlextConstants,
    FlextExceptions,
    FlextLogger,
    FlextModels,
    t as _core_t,
)
from flext_meltano import FlextMeltanoModels
from flext_oracle_oic import FlextOracleOicModels
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    FieldSerializationInfo,
    TypeAdapter,
    ValidationError,
    computed_field,
    field_serializer,
    model_validator,
)

from flext_tap_oracle_oic import c, t
from flext_tap_oracle_oic.constants import (
    FlextTapOracleOicConstants,
)
from flext_tap_oracle_oic.utilities import FlextTapOracleOicUtilities

if TYPE_CHECKING:
    from flext_tap_oracle_oic.tap_streams import OICPaginator


def _get_oic_paginator_class() -> type[OICPaginator]:
    """Lazy import to break circular dependency between models and tap_streams."""
    from flext_tap_oracle_oic.tap_streams import OICPaginator as _Cls  # noqa: PLC0415 — lazy import breaks circular dependency with tap_streams

    return _Cls


# Type aliases for OIC domain literals (PEP 695 `type` stmts in nested classes
# aren't resolvable by mypy/pyright with `from __future__ import annotations`)
OicIntegrationStatusLiteral = Literal[
    "ACTIVE",
    "INACTIVE",
    "DRAFT",
    "ERROR",
    "TESTING",
    "DEPRECATED",
]
OicJobStatusLiteral = Literal["RUNNING", "COMPLETED", "FAILED", "ABORTED", "SUSPENDED"]
OicIntegrationTypeLiteral = Literal[
    "INTEGRATION",
    "LIBRARY",
    "TEMPLATE",
    "RECIPE",
    "CONNECTIVITY_AGENT",
]
OicAgentTypeLiteral = Literal["ON_PREMISES_AGENT", "FILE_AGENT"]
OicAgentStatusLiteral = Literal["ONLINE", "OFFLINE", "MAINTENANCE"]
OicReplicationMethodLiteral = Literal["FULL_TABLE", "INCREMENTAL"]
OicErrorTypeLiteral = Literal[
    "AUTHENTICATION",
    "AUTHORIZATION",
    "RATE_LIMIT",
    "SERVER_ERROR",
    "NETWORK",
    "VALIDATION",
]


class OicEnvelope(BaseModel):
    """OIC API response envelope for paginated list endpoints.

    Parses the outer wrapper that Oracle OIC returns for list responses,
    normalizing between 'items', 'data', 'count', and 'totalSize' fields.
    """

    items: Sequence[Mapping[str, t.ContainerValue]] | None = None
    data: Sequence[Mapping[str, t.ContainerValue]] | None = None
    total_size: Annotated[int | None, Field(default=None, alias="totalSize")]
    count: int | None = None


_GENERAL_LIST_ADAPTER = TypeAdapter(
    Sequence[_core_t.ContainerValue],
    config=ConfigDict(strict=True),
)
_GENERAL_MAP_ADAPTER = TypeAdapter(
    Mapping[str, _core_t.ContainerValue],
    config=ConfigDict(strict=True),
)
_STRING_LIST_ADAPTER = TypeAdapter(Sequence[str], config=ConfigDict(strict=True))


def _as_value_list(value: t.ContainerValue | None) -> Sequence[t.ContainerValue] | None:
    """Validate payload as strict Sequence[t.NormalizedValue]."""
    try:
        return _GENERAL_LIST_ADAPTER.validate_python(value)
    except ValidationError:
        return None


def _as_value_map(
    value: t.ContainerValue | None,
) -> Mapping[str, t.ContainerValue] | None:
    """Validate payload as strict Mapping[str, t.NormalizedValue]."""
    try:
        return _GENERAL_MAP_ADAPTER.validate_python(value)
    except ValidationError:
        return None


def _as_string_list(value: t.ContainerValue | None) -> Sequence[str] | None:
    """Validate payload as strict Sequence[str]."""
    try:
        return _STRING_LIST_ADAPTER.validate_python(value)
    except ValidationError:
        return None


def _as_oic_envelope(value: Mapping[str, t.ContainerValue]) -> OicEnvelope | None:
    """Validate payload as an OIC envelope model."""
    try:
        return OicEnvelope.model_validate(value, strict=True)
    except ValidationError:
        return None


class FlextTapOracleOicModels(FlextMeltanoModels, FlextOracleOicModels):
    """Oracle Integration Cloud tap models extending flext-core FlextModels.

    Provides complete models for OIC entity extraction, authentication,
    monitoring, and Singer protocol compliance following standardized patterns.
    """

    # Dynamic attributes for runtime configuration (accessed via hasattr checks)
    _oic_authentication: Mapping[str, t.ContainerValue] | None = None
    _stream_configurations: Mapping[str, t.ContainerValue] | None = None
    _singer_mode: Mapping[str, t.ContainerValue] | None = None
    _include_oic_metadata: Mapping[str, t.ContainerValue] | None = None

    # Pydantic 2.11 Configuration - Enterprise Singer Oracle OIC Tap Features
    model_config: ClassVar[ConfigDict] = ConfigDict(
        validate_assignment=True,
        use_enum_values=True,
        arbitrary_types_allowed=True,
        extra="forbid",
        frozen=False,
        validate_return=True,
        ser_json_timedelta="iso8601",
        ser_json_bytes="base64",
        hide_input_in_errors=True,
        json_schema_extra={
            "title": "FLEXT Singer Oracle OIC Tap Models",
            "description": "Enterprise Oracle Integration Cloud API extraction models with Singer protocol compliance",
            "examples": [
                {
                    "tap_name": "tap-oracle-oic",
                    "extraction_mode": "api_incremental_replication",
                    "oic_instance": "https://mycompany-oic.integration.ocp.oraclecloud.com",
                },
            ],
            "tags": ["singer", "oracle-oic", "tap", "extraction", "integration-cloud"],
            "version": "2.11.0",
        },
    )

    @computed_field
    def active_oic_tap_models_count(self) -> int:
        """Count of active Oracle OIC tap models with API extraction capabilities."""
        return self._count_active_oic_tap_models()

    @computed_field
    def oic_tap_system_summary(self) -> Mapping[str, t.ContainerValue]:
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

    @field_serializer("*", when_used="json")
    def serialize_with_oic_metadata(
        self,
        value: Mapping[str, t.ContainerValue],
        _info: FieldSerializationInfo,
    ) -> Mapping[str, t.ContainerValue]:
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

    @model_validator(mode="after")
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

        class OICBaseStream(BaseModel):
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

            model_config: ClassVar[ConfigDict] = ConfigDict(
                arbitrary_types_allowed=True
            )

            config: Mapping[str, t.ContainerValue] = Field(default_factory=dict)
            name: str = Field(default="")
            replication_key: str | None = Field(default=None)
            logger: FlextLogger = Field(default_factory=lambda: FlextLogger(__name__))

            requires_design_api: ClassVar[bool] = False
            requires_runtime_api: ClassVar[bool] = False
            api_path: ClassVar[str | None] = None
            api_category: ClassVar[str] = "core"
            default_sort: ClassVar[str | None] = None
            additional_params: ClassVar[Mapping[str, t.ContainerValue] | None] = None
            primary_keys: ClassVar[Sequence[str]] = []

            @property
            def api_client(self) -> FlextApi:
                """Get authenticated API client from parent tap's OIC client."""
                api_config = FlextApiSettings.model_validate({})
                return FlextApi(api_config)

            @property
            def url_base(self) -> str:
                """Build base URL for Oracle OIC API requests with intelligent discovery.

                Returns:
                Base URL with appropriate OIC API endpoint for stream type.

                """
                utilities = FlextTapOracleOicUtilities()
                base_url = str(
                    self.config.get("base_url") or self.config.get("oic_url", ""),
                ).rstrip("/")
                if not base_url:
                    msg = "Base URL is required but not configured"
                    raise ValueError(msg)
                validation_result = utilities.OicApiProcessing.validate_oic_endpoint(
                    base_url
                )
                if validation_result.is_failure:
                    msg = f"Invalid OIC endpoint: {validation_result.error}"
                    raise ValueError(msg)
                region = self.config.get("region")
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
                    "core": FlextTapOracleOicConstants.OIC_API_BASE_PATH,
                    "monitoring": FlextTapOracleOicConstants.OIC_MONITORING_API_PATH,
                    "b2b": FlextTapOracleOicConstants.OIC_B2B_API_PATH,
                    "process": FlextTapOracleOicConstants.OIC_PROCESS_API_PATH,
                }
                return base_url + api_paths.get(
                    self.api_category,
                    FlextTapOracleOicConstants.OIC_API_BASE_PATH,
                )

            def get_new_paginator(self) -> OICPaginator:
                """Create new Oracle OIC paginator with configuration.

                Returns:
                OICPaginator instance configured with settings from tap config.

                """
                paginator_cls = _get_oic_paginator_class()
                page_size_val = self.config.get("page_size", 100)
                page_size = page_size_val if isinstance(page_size_val, int) else 100
                return paginator_cls(start_value=0, page_size=page_size)

            def get_records(
                self,
                context: Mapping[str, t.ContainerValue] | None = None,
            ) -> Iterator[Mapping[str, t.ContainerValue]]:
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
                context: Mapping[str, t.ContainerValue] | None,
                next_page_token: int | None,
            ) -> Mapping[str, t.ContainerValue]:
                """Build URL parameters for Oracle OIC API requests.

                Args:
                context: Stream context with replication values.
                next_page_token: Token for pagination (offset value).

                Returns:
                Dictionary of URL parameters optimized for OIC API.

                """
                params: Mapping[str, t.ContainerValue] = {}
                page_size_val = self.config.get("page_size", 100)
                page_size = page_size_val if isinstance(page_size_val, int) else 100
                params["limit"] = min(page_size, 1000)
                params["offset"] = next_page_token or 0
                instance_id = self.config.get("instance_id")
                if instance_id:
                    params["integrationInstance"] = instance_id
                sort_field = self.config.get("sort_field")
                if sort_field:
                    sort_direction = (
                        "desc" if self.config.get("sort_desc", False) else "asc"
                    )
                    params["orderBy"] = f"{sort_field}:{sort_direction}"
                elif self.default_sort is not None:
                    params["orderBy"] = self.default_sort
                custom_filter = self.config.get("custom_filter")
                if custom_filter:
                    params["q"] = custom_filter
                if (
                    self.replication_key
                    and context
                    and context.get("starting_replication_value")
                ):
                    start_date = context["starting_replication_value"]
                    params[f"{self.replication_key}>="] = start_date
                select_fields = self.config.get("select_fields")
                if select_fields:
                    field_list = _as_string_list(select_fields)
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
                response: requests.Response,
            ) -> Iterator[Mapping[str, t.ContainerValue]]:
                """Parse Oracle OIC API response and yield records with validation.

                Args:
                response: HTTP response from OIC API.

                Yields:
                Individual records from the API response with tap metadata.

                """
                try:
                    if not response.ok:
                        self._handle_response_error(response)
                        return
                    try:
                        data = response.json()
                    except (ValueError, TypeError, KeyError):
                        self.logger.exception(
                            "Failed to parse JSON from %s", response.url
                        )
                        if self.config.get("fail_on_parsing_errors", True):
                            raise
                        return
                    self._track_response_metrics(response, data)
                    response_url = str(getattr(response, "url", "unknown"))
                    yield from self._extract_and_yield_records(data, response_url)
                except (ValueError, TypeError, KeyError, AttributeError):
                    response_url_err = str(getattr(response, "url", "unknown"))
                    self.logger.exception(
                        "Error parsing response from %s", response_url_err
                    )
                    if self.config.get("fail_on_parsing_errors", True):
                        raise

            def _enrich_record(
                self,
                record: Mapping[str, t.ContainerValue],
            ) -> Mapping[str, t.ContainerValue]:
                """Enrich record with tap metadata for traceability."""
                enriched: Mapping[str, t.ContainerValue] = dict(record)
                enriched["_tap_extracted_at"] = datetime.now(UTC).isoformat()
                enriched["_tap_stream_name"] = self.name
                return enriched

            def _extract_and_yield_records(
                self,
                data: Mapping[str, t.ContainerValue],
                url: str,
            ) -> Iterator[Mapping[str, t.ContainerValue]]:
                """Extract and yield records with validation and enrichment."""
                records_yielded = 0
                for item in self._extract_items_for_processing(data):
                    if self._validate_record(item):
                        yield self._enrich_record(item)
                        records_yielded += 1
                if records_yielded == 0 and (not self._is_empty_result_expected(data)):
                    map_data = _as_value_map(data)
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
                data: Mapping[str, t.ContainerValue],
            ) -> Iterator[Mapping[str, t.ContainerValue]]:
                """Extract items from various OIC response formats for processing."""
                list_payload = _as_value_list(data)
                if list_payload is not None:
                    yield from self._process_list_data(list_payload)
                    return
                map_payload = _as_value_map(data)
                if map_payload is not None:
                    yield from self._process_dict_data(map_payload)

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
                if status_code == c.TapOicHttp.HTTP_UNAUTHORIZED:
                    msg = "Unauthorized: Authentication failed or token expired"
                    raise FlextExceptions.AuthenticationError(msg)
                if status_code == c.TapOicHttp.HTTP_FORBIDDEN:
                    msg = "Forbidden: Insufficient permissions to access resource"
                    raise FlextExceptions.AuthorizationError(msg)
                if status_code == c.TapOicHttp.HTTP_RATE_LIMITED:
                    msg = "Rate limit exceeded: Too many requests"
                    raise FlextExceptions.RateLimitError(msg)
                raise_for_status = getattr(response, "raise_for_status", None)
                if raise_for_status is not None:
                    raise_for_status()

            def _is_empty_result_expected(
                self, data: Mapping[str, t.ContainerValue]
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

            def _is_single_record(self, data: Mapping[str, t.ContainerValue]) -> bool:
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
                data: Mapping[str, t.ContainerValue],
            ) -> Iterator[Mapping[str, t.ContainerValue]]:
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

            def _process_list_data(
                self,
                data: Sequence[t.ContainerValue],
            ) -> Iterator[Mapping[str, t.ContainerValue]]:
                """Process list-type response data."""
                for item in data:
                    record = _as_value_map(item)
                    if record is not None:
                        yield record

            def _track_response_metrics(
                self,
                response: requests.Response,
                data: Mapping[str, t.ContainerValue],
            ) -> None:
                """Track response metrics for monitoring and optimization."""
                if getattr(response, "elapsed", None) is not None:
                    self.logger.debug(
                        "Response time: %.2fs", response.elapsed.total_seconds()
                    )
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

            def _validate_record(self, record: Mapping[str, t.ContainerValue]) -> bool:
                """Validate record meets basic requirements for processing."""
                return _as_value_map(dict(record)) is not None

        class OicAuthenticationConfig(FlextModels.ArbitraryTypesModel):
            """OAuth2/IDCS authentication configuration for OIC API access."""

            # Pydantic 2.11 Configuration - Authentication Features
            model_config: ClassVar[ConfigDict] = ConfigDict(
                validate_assignment=True,
                extra="forbid",
                frozen=False,
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
                Field(
                    ...,
                    description="OAuth2 client ID for OIC API",
                ),
            ]
            oauth_client_secret: Annotated[
                str,
                Field(..., description="OAuth2 client secret"),
            ]
            oauth_token_url: Annotated[
                str,
                Field(
                    ...,
                    description="IDCS OAuth2 token endpoint URL",
                ),
            ]
            oauth_client_aud: Annotated[
                str,
                Field(..., description="OAuth2 audience parameter"),
            ]
            base_url: Annotated[str, Field(..., description="OIC instance base URL")]

            # Optional authentication settings
            token_expiry_buffer: Annotated[
                int,
                Field(
                    default=300,
                    description="Token refresh buffer in seconds",
                ),
            ]
            max_retry_attempts: Annotated[
                int,
                Field(
                    default=3,
                    description="Maximum authentication retry attempts",
                ),
            ]
            timeout_seconds: Annotated[
                int,
                Field(
                    default=30,
                    description="Authentication timeout",
                ),
            ]

            @computed_field
            def auth_config_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.ContainerValue | None]]:
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

            @model_validator(mode="after")
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
                    < c.TapOicValidation.MIN_TOKEN_EXPIRY_BUFFER
                ):
                    msg = "Token expiry buffer must be at least 60 seconds"
                    raise ValueError(msg)
                return self

        class OicIntegrationEntity(FlextModels.Entity):
            """OIC Integration entity with complete metadata."""

            # Pydantic 2.11 Configuration - Integration Features
            model_config: ClassVar[ConfigDict] = ConfigDict(
                validate_assignment=True,
                extra="forbid",
                frozen=False,
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
                Field(
                    ...,
                    description="Unique integration identifier",
                ),
            ]
            name: Annotated[str, Field(..., description="Integration name")]
            description: Annotated[
                str | None,
                Field(None, description="Integration description"),
            ]
            api_version: Annotated[
                str,
                Field(
                    ...,
                    description="Integration version from OIC API",
                ),
            ]
            status: Annotated[
                OicIntegrationStatusLiteral,
                Field(
                    ...,
                    description="Integration status",
                ),
            ]

            # Temporal information
            created_date: Annotated[
                datetime | None,
                Field(
                    None,
                    description="Integration creation date",
                ),
            ]
            last_updated: Annotated[
                datetime | None,
                Field(
                    None,
                    description="Last update timestamp",
                ),
            ]
            last_activated: Annotated[
                datetime | None,
                Field(
                    None,
                    description="Last activation timestamp",
                ),
            ]

            # Metadata
            package_id: Annotated[
                str | None,
                Field(None, description="Associated package ID"),
            ]
            pattern: Annotated[
                str | None,
                Field(None, description="Integration pattern type"),
            ]
            style: Annotated[str | None, Field(None, description="Integration style")]

            # Runtime information
            execution_count: Annotated[
                int | None,
                Field(
                    None,
                    description="Total execution count",
                ),
            ]
            error_count: Annotated[
                int | None,
                Field(None, description="Total error count"),
            ]
            last_execution_time: Annotated[
                datetime | None,
                Field(
                    None,
                    description="Last execution timestamp",
                ),
            ]

            @computed_field
            def integration_health_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.ContainerValue | None]]:
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
                        "health_status": "healthy"
                        if error_rate < c.TapOicValidation.MAX_PERCENTAGE / 20
                        else "degraded",
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

            @model_validator(mode="after")
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

        class OicConnectionEntity(FlextModels.Entity):
            """OIC Connection entity with security sanitization."""

            # Pydantic 2.11 Configuration - Connection Features
            model_config: ClassVar[ConfigDict] = ConfigDict(
                validate_assignment=True,
                extra="forbid",
                frozen=False,
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
                Field(..., description="Unique connection identifier"),
            ]
            name: Annotated[str, Field(..., description="Connection name")]
            description: Annotated[
                str | None,
                Field(None, description="Connection description"),
            ]
            connection_type: Annotated[
                str,
                Field(..., description="Connection adapter type"),
            ]

            # Configuration (sanitized)
            host: Annotated[
                str | None,
                Field(
                    None,
                    description="Connection host (if applicable)",
                ),
            ]
            port: Annotated[
                int | None,
                Field(
                    None,
                    description="Connection port (if applicable)",
                ),
            ]

            # Security metadata (credentials removed)
            authentication_type: Annotated[
                str | None,
                Field(
                    None,
                    description="Authentication method used",
                ),
            ]
            security_policy: Annotated[
                str | None,
                Field(
                    None,
                    description="Security policy name",
                ),
            ]
            certificate_alias: Annotated[
                str | None,
                Field(
                    None,
                    description="Certificate alias (if used)",
                ),
            ]

            # Status and health
            status: Annotated[
                OicIntegrationStatusLiteral,
                Field(
                    ...,
                    description="Connection status",
                ),
            ]
            last_tested: Annotated[
                datetime | None,
                Field(
                    None,
                    description="Last connection test timestamp",
                ),
            ]
            test_result: Annotated[
                str | None,
                Field(None, description="Last test result"),
            ]

            # Sanitization markers
            data_sanitized: Annotated[
                bool,
                Field(
                    default=True,
                    description="Indicates if sensitive data was removed",
                ),
            ]
            sanitization_timestamp: Annotated[
                datetime | None,
                Field(
                    default_factory=lambda: datetime.now(UTC),
                    description="When sanitization occurred",
                ),
            ]

            @computed_field
            def connection_security_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.ContainerValue | None]]:
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

            @model_validator(mode="after")
            def validate_connection_entity(self) -> Self:
                """Validate OIC connection entity."""
                if not self.connection_id:
                    msg = "Connection ID is required"
                    raise ValueError(msg)
                if not self.name:
                    msg = "Connection name is required"
                    raise ValueError(msg)
                if self.port is not None and not (
                    FlextConstants.MIN_PORT <= self.port <= FlextConstants.MAX_PORT
                ):
                    msg = "Port must be between 1 and 65535"
                    raise ValueError(msg)
                return self

        class OicActivityRecord(FlextModels.Entity):
            """OIC Activity monitoring record for incremental replication."""

            # Pydantic 2.11 Configuration - Activity Features
            model_config: ClassVar[ConfigDict] = ConfigDict(
                validate_assignment=True,
                extra="forbid",
                frozen=False,
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
                Field(
                    ...,
                    description="Unique activity record identifier",
                ),
            ]
            integration_id: Annotated[
                str,
                Field(..., description="Associated integration ID"),
            ]
            instance_id: Annotated[
                str,
                Field(..., description="Integration instance ID"),
            ]

            # Temporal information (for incremental replication)
            start_time: Annotated[
                datetime,
                Field(..., description="Activity start timestamp"),
            ]
            end_time: Annotated[
                datetime | None,
                Field(
                    None,
                    description="Activity end timestamp",
                ),
            ]
            duration_ms: Annotated[
                int | None,
                Field(
                    None,
                    description="Activity duration in milliseconds",
                ),
            ]

            # Status and results
            status: Annotated[
                OicJobStatusLiteral,
                Field(
                    ...,
                    description="Activity status",
                ),
            ]
            result: Annotated[str | None, Field(None, description="Activity result")]
            error_message: Annotated[
                str | None,
                Field(
                    None,
                    description="Error message if failed",
                ),
            ]

            # Metrics
            messages_processed: Annotated[
                int | None,
                Field(
                    None,
                    description="Number of messages processed",
                ),
            ]
            bytes_processed: Annotated[
                int | None,
                Field(None, description="Bytes processed"),
            ]
            throughput_mps: Annotated[
                float | None,
                Field(
                    None,
                    description="Messages per second throughput",
                ),
            ]

            @computed_field
            def activity_performance_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.ContainerValue | None]]:
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
                        "success": self.status == "COMPLETED",
                    },
                    "volume": {
                        "bytes_processed": self.bytes_processed or 0,
                        "mb_processed": (self.bytes_processed or 0) / (1024 * 1024),
                    },
                }

            @model_validator(mode="after")
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

        class OicPackageEntity(FlextModels.Entity):
            """OIC Package entity for integration packages."""

            # Pydantic 2.11 Configuration - Package Features
            model_config: ClassVar[ConfigDict] = ConfigDict(
                validate_assignment=True,
                extra="forbid",
                frozen=False,
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
                Field(..., description="Unique package identifier"),
            ]
            name: Annotated[str, Field(..., description="Package name")]
            description: Annotated[
                str | None,
                Field(None, description="Package description"),
            ]
            api_version: Annotated[
                str,
                Field(..., description="Package version from OIC API"),
            ]

            # Package metadata
            package_type: Annotated[
                OicIntegrationTypeLiteral,
                Field(
                    ...,
                    description="Package type",
                ),
            ]
            created_by: Annotated[
                str | None,
                Field(None, description="Package creator"),
            ]
            created_date: Annotated[
                datetime | None,
                Field(
                    None,
                    description="Package creation date",
                ),
            ]

            # Dependencies and relationships
            dependencies: Annotated[
                Sequence[str],
                Field(
                    default_factory=list,
                    description="List of dependent package IDs",
                ),
            ]
            integration_count: Annotated[
                int | None,
                Field(
                    None,
                    description="Number of integrations in package",
                ),
            ]

            # Status
            status: Annotated[
                OicIntegrationStatusLiteral,
                Field(
                    ...,
                    description="Package status",
                ),
            ]
            download_count: Annotated[
                int | None,
                Field(
                    None,
                    description="Package download count",
                ),
            ]

            @computed_field
            def package_composition_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.ContainerValue | None]]:
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
                        "dependencies": Sequence[t.ContainerValue](self.dependencies),
                    },
                    "usage": {
                        "download_count": self.download_count or 0,
                        "created_by": self.created_by,
                        "created_date": self.created_date.isoformat()
                        if self.created_date
                        else None,
                    },
                }

            @model_validator(mode="after")
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

        class OicMetricsRecord(FlextModels.Entity):
            """OIC Metrics record for performance monitoring."""

            # Pydantic 2.11 Configuration - Metrics Features
            model_config: ClassVar[ConfigDict] = ConfigDict(
                validate_assignment=True,
                extra="forbid",
                frozen=False,
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
                Field(..., description="Unique metrics record identifier"),
            ]
            integration_id: Annotated[
                str,
                Field(..., description="Associated integration ID"),
            ]
            timestamp: Annotated[datetime, Field(..., description="Metrics timestamp")]

            # Performance metrics
            cpu_usage_percent: Annotated[
                float | None,
                Field(
                    None,
                    description="CPU usage percentage",
                ),
            ]
            memory_usage_mb: Annotated[
                float | None,
                Field(
                    None,
                    description="Memory usage in MB",
                ),
            ]
            throughput_mps: Annotated[
                float | None,
                Field(
                    None,
                    description="Messages per second",
                ),
            ]
            latency_ms: Annotated[
                float | None,
                Field(
                    None,
                    description="Average latency in milliseconds",
                ),
            ]

            # Business metrics
            success_count: Annotated[
                int | None,
                Field(
                    None,
                    description="Successful message count",
                ),
            ]
            error_count: Annotated[
                int | None,
                Field(None, description="Error message count"),
            ]
            retry_count: Annotated[
                int | None,
                Field(None, description="Retry attempt count"),
            ]

            # Resource utilization
            database_connections: Annotated[
                int | None,
                Field(
                    None,
                    description="Active database connections",
                ),
            ]
            thread_count: Annotated[
                int | None,
                Field(None, description="Active thread count"),
            ]
            queue_depth: Annotated[
                int | None,
                Field(None, description="Message queue depth"),
            ]

            @computed_field
            def metrics_analysis_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.ContainerValue | None]]:
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

            @model_validator(mode="after")
            def validate_metrics_record(self) -> Self:
                """Validate OIC metrics record."""
                if not self.metric_id:
                    msg = "Metric ID is required"
                    raise ValueError(msg)
                if not self.integration_id:
                    msg = "Integration ID is required"
                    raise ValueError(msg)
                if self.cpu_usage_percent is not None and not (
                    c.TapOicValidation.MIN_PERCENTAGE
                    <= self.cpu_usage_percent
                    <= c.TapOicValidation.MAX_PERCENTAGE
                ):
                    msg = "CPU usage must be between 0 and 100 percent"
                    raise ValueError(msg)
                return self

        class OicAgentEntity(FlextModels.Entity):
            """OIC Agent entity for connectivity agents."""

            # Pydantic 2.11 Configuration - Agent Features
            model_config: ClassVar[ConfigDict] = ConfigDict(
                validate_assignment=True,
                extra="forbid",
                frozen=False,
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

            agent_id: Annotated[str, Field(..., description="Unique agent identifier")]
            agent_name: Annotated[str, Field(..., description="Agent display name")]
            agent_type: Annotated[
                OicAgentTypeLiteral,
                Field(
                    ...,
                    description="Agent type",
                ),
            ]

            # Agent status and health
            status: Annotated[
                OicAgentStatusLiteral,
                Field(
                    ...,
                    description="Agent status",
                ),
            ]
            last_heartbeat: Annotated[
                datetime | None,
                Field(
                    None,
                    description="Last heartbeat timestamp",
                ),
            ]
            api_version: Annotated[
                str | None,
                Field(
                    None,
                    description="Agent version from OIC API",
                ),
            ]

            # Configuration
            host_machine: Annotated[
                str | None,
                Field(None, description="Host machine name"),
            ]
            installation_path: Annotated[
                str | None,
                Field(
                    None,
                    description="Agent installation path",
                ),
            ]
            port: Annotated[
                int | None,
                Field(None, description="Agent communication port"),
            ]

            # Health metrics
            uptime_hours: Annotated[
                float | None,
                Field(
                    None,
                    description="Agent uptime in hours",
                ),
            ]
            connection_count: Annotated[
                int | None,
                Field(
                    None,
                    description="Active connection count",
                ),
            ]
            last_error: Annotated[
                str | None,
                Field(None, description="Last error message"),
            ]

            @computed_field
            def agent_health_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.ContainerValue | None]]:
                """OIC agent health and connectivity summary."""
                health_status = "healthy"
                if self.status in {"ERROR", "OFFLINE"}:
                    health_status = "unhealthy"
                elif self.last_error:
                    health_status = "degraded"

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

            @model_validator(mode="after")
            def validate_agent_entity(self) -> Self:
                """Validate OIC agent entity."""
                if not self.agent_id:
                    msg = "Agent ID is required"
                    raise ValueError(msg)
                if not self.agent_name:
                    msg = "Agent name is required"
                    raise ValueError(msg)
                if self.port is not None and not (
                    FlextConstants.MIN_PORT <= self.port <= FlextConstants.MAX_PORT
                ):
                    msg = "Port must be between 1 and 65535"
                    raise ValueError(msg)
                return self

        class OicStreamConfiguration(FlextModels.ArbitraryTypesModel):
            """Configuration for OIC tap streams."""

            # Pydantic 2.11 Configuration - Stream Features
            model_config: ClassVar[ConfigDict] = ConfigDict(
                validate_assignment=True,
                extra="forbid",
                frozen=False,
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

            stream_name: Annotated[str, Field(..., description="Singer stream name")]
            replication_method: Annotated[
                OicReplicationMethodLiteral,
                Field(
                    default="FULL_TABLE",
                    description="Replication method",
                ),
            ]
            replication_key: Annotated[
                str | None,
                Field(
                    None,
                    description="Replication key field name",
                ),
            ]

            # Pagination and performance
            page_size: Annotated[
                int,
                Field(
                    default=100,
                    ge=1,
                    le=1000,
                    description="API pagination size",
                ),
            ]
            include_extended: Annotated[
                bool,
                Field(
                    default=False,
                    description="Include extended entity metadata",
                ),
            ]

            # Filtering
            status_filter: Annotated[
                Sequence[str] | None,
                Field(
                    None,
                    description="Filter by entity status values",
                ),
            ]
            date_range_filter: Annotated[
                str | None,
                Field(
                    None,
                    description="Date range filter for incremental streams",
                ),
            ]

            # Security
            sanitize_sensitive_data: Annotated[
                bool,
                Field(
                    default=True,
                    description="Enable data sanitization",
                ),
            ]
            exclude_test_entities: Annotated[
                bool,
                Field(
                    default=True,
                    description="Exclude test/demo entities",
                ),
            ]

            @computed_field
            def stream_config_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.ContainerValue | None]]:
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

            @model_validator(mode="after")
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
                if (
                    self.page_size <= 0
                    or self.page_size > FlextConstants.MAX_BATCH_SIZE
                ):
                    msg = "Page size must be between 1 and 1000"
                    raise ValueError(msg)
                return self

        class OicApiResponse(FlextModels.Entity):
            """Standardized OIC API response wrapper."""

            # Pydantic 2.11 Configuration - API Response Features
            model_config: ClassVar[ConfigDict] = ConfigDict(
                validate_assignment=True,
                extra="forbid",
                frozen=False,
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
                Field(..., description="Response success indicator"),
            ]
            data: Annotated[
                Mapping[str, t.ContainerValue] | None,
                Field(
                    None,
                    description="Response data payload",
                ),
            ]
            total_count: Annotated[
                int | None,
                Field(
                    None,
                    description="Total entity count (for pagination)",
                ),
            ]
            page_size: Annotated[
                int | None,
                Field(None, description="Current page size"),
            ]
            page_number: Annotated[
                int | None,
                Field(None, description="Current page number"),
            ]

            # Error information
            error_code: Annotated[
                str | None,
                Field(None, description="Error code if failed"),
            ]
            error_message: Annotated[
                str | None,
                Field(
                    None,
                    description="Error message if failed",
                ),
            ]
            error_details: Annotated[
                Mapping[str, Mapping[str, t.ContainerValue]] | None,
                Field(
                    None,
                    description="Detailed error information",
                ),
            ]

            # Metadata
            timestamp: Annotated[
                datetime,
                Field(
                    default_factory=lambda: datetime.now(UTC),
                    description="Response timestamp",
                ),
            ]
            api_version: Annotated[
                str | None,
                Field(None, description="OIC API version"),
            ]
            request_id: Annotated[
                str | None,
                Field(None, description="Request correlation ID"),
            ]

            @computed_field
            def api_response_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.ContainerValue | None]]:
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

            @model_validator(mode="after")
            def validate_api_response(self) -> Self:
                """Validate OIC API response."""
                if not self.success and not self.error_message:
                    msg = "Failed responses must have an error message"
                    raise ValueError(msg)
                if self.page_number is not None and self.page_number < 1:
                    msg = "Page number must be positive"
                    raise ValueError(msg)
                return self

        class OicErrorContext(FlextModels.Entity):
            """Error context for OIC API error handling."""

            # Pydantic 2.11 Configuration - Error Context Features
            model_config: ClassVar[ConfigDict] = ConfigDict(
                validate_assignment=True,
                extra="forbid",
                frozen=False,
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
                OicErrorTypeLiteral,
                Field(..., description="Error category"),
            ]
            http_status_code: Annotated[
                int | None,
                Field(None, description="HTTP status code"),
            ]
            retry_after_seconds: Annotated[
                int | None,
                Field(
                    None,
                    description="Retry after duration",
                ),
            ]

            # Context information
            endpoint: Annotated[
                str | None,
                Field(None, description="API endpoint that failed"),
            ]
            request_method: Annotated[
                str | None,
                Field(None, description="HTTP method used"),
            ]
            request_params: Annotated[
                Mapping[str, Mapping[str, t.ContainerValue]] | None,
                Field(
                    None,
                    description="Request parameters",
                ),
            ]

            # Recovery information
            is_retryable: Annotated[
                bool,
                Field(
                    default=False,
                    description="Whether error is retryable",
                ),
            ]
            suggested_action: Annotated[
                str | None,
                Field(
                    None,
                    description="Suggested recovery action",
                ),
            ]
            max_retry_attempts: Annotated[
                int | None,
                Field(
                    None,
                    description="Maximum retry attempts for this error",
                ),
            ]

            @computed_field
            def error_context_summary(
                self,
            ) -> Mapping[str, Mapping[str, t.ContainerValue | None]]:
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

            @model_validator(mode="after")
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
                    c.OicErrorType.AUTHENTICATION,
                    c.OicErrorType.AUTHORIZATION,
                }:
                    return "critical"
                if self.error_type == c.OicErrorType.RATE_LIMIT:
                    return "warning"
                if self.error_type == c.OicErrorType.SERVER_ERROR:
                    return "error"
                if self.error_type in {
                    c.OicErrorType.NETWORK,
                    c.OicErrorType.VALIDATION,
                }:
                    return "warning"
                return "unknown"

    class OracleOic:
        """Domain entity models for Oracle OIC resources.

        Canonical home for OIC entity classes, migrated from domain/entities.py
        per MRO policy: all FlextModels subclasses live under [Project]Models.
        """

        class OICConnection(FlextModels):
            """OIC connection domain entity using flext-core patterns."""

            model_config: ClassVar[ConfigDict] = ConfigDict(frozen=False)
            connection_id: Annotated[
                str,
                Field(..., min_length=1, description="OIC connection identifier"),
            ]
            adapter_type: Annotated[
                str,
                Field(
                    ..., min_length=1, description="Adapter type (e.g., REST, SOAP, DB)"
                ),
            ]
            name: Annotated[
                str, Field(..., min_length=1, description="Connection name")
            ]
            connection_url: Annotated[
                str | None,
                Field(None, description="Connection endpoint URL"),
            ]
            connection_properties: Annotated[
                Mapping[str, Mapping[str, t.ContainerValue]],
                Field(default_factory=dict, description="Connection properties"),
            ]
            security_policy: Annotated[
                str | None,
                Field(None, description="Security policy name"),
            ]
            connection_status: Annotated[
                c.ConnectionStatus,
                Field(
                    default=c.ConnectionStatus.CONFIGURED,
                    description="Connection status",
                ),
            ]
            last_tested: Annotated[
                datetime | None,
                Field(None, description="Last test timestamp"),
            ]
            test_result: Annotated[
                Mapping[str, str] | None,
                Field(None, description="Last test result"),
            ]
            version: Annotated[
                str | None, Field(None, description="Connection version")
            ]
            locked_by: Annotated[
                str | None,
                Field(None, description="User who locked the connection"),
            ]
            locked_at: Annotated[
                datetime | None, Field(None, description="Lock timestamp")
            ]
            created_at: Annotated[
                datetime | None,
                Field(None, description="Creation timestamp"),
            ]
            updated_at: Annotated[
                datetime | None,
                Field(None, description="Last update timestamp"),
            ]

            def mark_failed(self, _error: str) -> None:
                """Mark connection as failed with error details."""
                self.connection_status = c.ConnectionStatus.FAILED
                self.test_result = {
                    "error": "error",
                    "timestamp": datetime.now(UTC).isoformat(),
                }

            def test_connection(self) -> None:
                """Mark connection as tested."""
                self.last_tested = datetime.now(UTC)
                self.connection_status = c.ConnectionStatus.TESTED

        class OICIntegration(FlextModels):
            """OIC integration domain entity using flext-core patterns."""

            model_config: ClassVar[ConfigDict] = ConfigDict(frozen=False)
            integration_id: Annotated[
                str,
                Field(..., min_length=1, description="OIC integration identifier"),
            ]
            integration_code: Annotated[
                str,
                Field(..., min_length=1, description="Integration code"),
            ]
            name: Annotated[
                str, Field(..., min_length=1, description="Integration name")
            ]
            package_name: Annotated[str | None, Field(None, description="Package name")]
            project_name: Annotated[str | None, Field(None, description="Project name")]
            integration_type: Annotated[
                str,
                Field(
                    ..., description="Integration type (e.g., APP_DRIVEN, SCHEDULED)"
                ),
            ]
            pattern: Annotated[
                str | None, Field(None, description="Integration pattern")
            ]
            style: Annotated[str | None, Field(None, description="Integration style")]
            endpoint_url: Annotated[
                str | None,
                Field(None, description="Integration endpoint URL"),
            ]
            tracking_level: Annotated[
                str | None, Field(None, description="Tracking level")
            ]
            payload_tracking: Annotated[
                bool,
                Field(default=False, description="Enable payload tracking"),
            ]
            integration_status: Annotated[
                c.IntegrationStatus,
                Field(
                    default=c.IntegrationStatus.CONFIGURED,
                    description="Integration status",
                ),
            ]
            activated_at: Annotated[
                datetime | None,
                Field(None, description="Activation timestamp"),
            ]
            deactivated_at: Annotated[
                datetime | None,
                Field(None, description="Deactivation timestamp"),
            ]
            version: Annotated[
                str,
                Field(default="01.00.0000", description="Integration version"),
            ]
            locked_by: Annotated[
                str | None,
                Field(None, description="User who locked the integration"),
            ]
            locked_at: Annotated[
                datetime | None, Field(None, description="Lock timestamp")
            ]
            connection_ids: Annotated[
                Sequence[str],
                Field(default_factory=list, description="Associated connection IDs"),
            ]
            created_at: Annotated[
                datetime | None,
                Field(None, description="Creation timestamp"),
            ]
            updated_at: Annotated[
                datetime | None,
                Field(None, description="Last update timestamp"),
            ]

            @property
            def is_active(self) -> bool:
                """Check if integration is active."""
                return self.integration_status == c.IntegrationStatus.ACTIVATED

            def activate(self) -> None:
                """Activate the integration."""
                self.integration_status = c.IntegrationStatus.ACTIVATED
                self.activated_at = datetime.now(UTC)

            def deactivate(self) -> None:
                """Deactivate the integration."""
                self.integration_status = c.IntegrationStatus.DEACTIVATED
                self.deactivated_at = datetime.now(UTC)

            def lock(self, user: str) -> None:
                """Lock the integration for a specific user."""
                self.locked_by = user
                self.locked_at = datetime.now(UTC)
                self.integration_status = c.IntegrationStatus.LOCKED

            def unlock(self) -> None:
                """Unlock the integration."""
                self.locked_by = None
                self.locked_at = None

        class OICLookup(FlextModels):
            """OIC lookup table domain entity using flext-core patterns."""

            model_config: ClassVar[ConfigDict] = ConfigDict(frozen=False)
            lookup_id: Annotated[
                str,
                Field(..., min_length=1, description="OIC lookup identifier"),
            ]
            lookup_name: Annotated[
                str,
                Field(..., min_length=1, description="Lookup table name"),
            ]
            domain_name: Annotated[str | None, Field(None, description="Domain name")]
            columns: Annotated[
                Sequence[Mapping[str, t.Container]],
                Field(
                    default_factory=list,
                    description="Column definitions",
                ),
            ]
            key_columns: Annotated[
                Sequence[str],
                Field(default_factory=list, description="Key column names"),
            ]
            value_columns: Annotated[
                Sequence[str],
                Field(default_factory=list, description="Value column names"),
            ]
            row_count: Annotated[
                int, Field(default=0, ge=0, description="Number of rows")
            ]
            data_size_bytes: Annotated[
                int | None,
                Field(None, ge=0, description="Data size in bytes"),
            ]
            locked_by: Annotated[
                str | None,
                Field(None, description="User who locked the lookup"),
            ]
            locked_at: Annotated[
                datetime | None, Field(None, description="Lock timestamp")
            ]
            last_imported: Annotated[
                datetime | None,
                Field(None, description="Last import timestamp"),
            ]
            created_at: Annotated[
                datetime | None,
                Field(None, description="Creation timestamp"),
            ]
            updated_at: Annotated[
                datetime | None,
                Field(None, description="Last update timestamp"),
            ]

            @property
            def is_empty(self) -> bool:
                """Check if lookup is empty."""
                return self.row_count == 0

            def record_import(self) -> None:
                """Record successful import."""
                self.last_imported = datetime.now(UTC)

            def update_statistics(
                self, row_count: int, data_size: int | None = None
            ) -> None:
                """Update lookup statistics."""
                self.row_count = row_count
                self.data_size_bytes = data_size

        class OICMonitoringRecord(FlextModels):
            """OIC monitoring record domain entity using flext-core patterns."""

            instance_id: Annotated[
                str,
                Field(..., min_length=1, description="Flow instance ID"),
            ]
            integration_id: Annotated[
                str, Field(..., description="Associated integration ID")
            ]
            flow_id: Annotated[str | None, Field(None, description="Flow ID")]
            tracking_level: Annotated[
                str | None, Field(None, description="Tracking level")
            ]
            started_at: Annotated[
                datetime, Field(..., description="Execution start time")
            ]
            completed_at: Annotated[
                datetime | None,
                Field(None, description="Execution completion time"),
            ]
            duration_ms: Annotated[
                int | None,
                Field(None, ge=0, description="Duration in milliseconds"),
            ]
            execution_status: Annotated[str, Field(..., description="Execution status")]
            error_code: Annotated[
                str | None, Field(None, description="Error code if failed")
            ]
            error_message: Annotated[
                str | None,
                Field(None, description="Error message if failed"),
            ]
            message_count: Annotated[
                int,
                Field(default=0, ge=0, description="Number of messages processed"),
            ]
            error_count: Annotated[
                int, Field(default=0, ge=0, description="Number of errors")
            ]
            business_identifiers: Annotated[
                Mapping[str, Mapping[str, t.ContainerValue]],
                Field(
                    default_factory=dict, description="Business tracking identifiers"
                ),
            ]

            @property
            def duration_seconds(self) -> float | None:
                """Get duration in seconds."""
                return (
                    self.duration_ms / 1000.0 if self.duration_ms is not None else None
                )

            @property
            def is_failed(self) -> bool:
                """Check if execution failed."""
                return self.execution_status.lower() in {"failed", "faulted", "aborted"}

            @property
            def successful(self) -> bool:
                """Check if execution was successful."""
                return self.execution_status.lower() in {"completed", "succeeded"}

        class OICProject(FlextModels):
            """OIC project domain entity using flext-core patterns."""

            model_config: ClassVar[ConfigDict] = ConfigDict(frozen=False)
            project_id: Annotated[
                str,
                Field(..., min_length=1, description="OIC project identifier"),
            ]
            project_code: Annotated[
                str, Field(..., min_length=1, description="Project code")
            ]
            name: Annotated[str, Field(..., min_length=1, description="Project name")]
            integration_ids: Annotated[
                Sequence[str],
                Field(default_factory=list, description="Integration IDs in project"),
            ]
            connection_ids: Annotated[
                Sequence[str],
                Field(default_factory=list, description="Connection IDs in project"),
            ]
            lookup_ids: Annotated[
                Sequence[str],
                Field(default_factory=list, description="Lookup IDs in project"),
            ]
            deployment_status: Annotated[
                str | None,
                Field(None, description="Deployment status"),
            ]
            deployed_at: Annotated[
                datetime | None,
                Field(None, description="Deployment timestamp"),
            ]
            deployed_by: Annotated[
                str | None, Field(None, description="User who deployed")
            ]
            created_at: Annotated[
                datetime | None,
                Field(None, description="Creation timestamp"),
            ]
            updated_at: Annotated[
                datetime | None,
                Field(None, description="Last update timestamp"),
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
            """OIC resource metadata value t.NormalizedValue."""

            resource_type: Annotated[
                c.OICResourceType,
                Field(..., description="Resource type"),
            ]
            resource_id: Annotated[
                str,
                Field(..., min_length=1, description="Resource identifier"),
            ]
            name: Annotated[str, Field(..., min_length=1, description="Resource name")]
            version: Annotated[str | None, Field(None, description="Resource version")]
            created_at: Annotated[
                datetime | None,
                Field(None, description="Creation timestamp"),
            ]
            updated_at: Annotated[
                datetime | None,
                Field(None, description="Last update timestamp"),
            ]

        class OICExecutionSummary(FlextModels):
            """OIC execution summary value t.NormalizedValue."""

            integration_id: Annotated[str, Field(..., description="Integration ID")]
            total_executions: Annotated[
                int,
                Field(default=0, ge=0, description="Total number of executions"),
            ]
            successful_executions: Annotated[
                int,
                Field(default=0, ge=0, description="Successful executions"),
            ]
            failed_executions: Annotated[
                int,
                Field(default=0, ge=0, description="Failed executions"),
            ]
            average_duration_ms: Annotated[
                float | None,
                Field(None, ge=0, description="Average execution duration"),
            ]
            last_execution_at: Annotated[
                datetime | None,
                Field(None, description="Last execution timestamp"),
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

__all__ = [
    "FlextTapOracleOicModels",
    "OicEnvelope",
    "m",
]
