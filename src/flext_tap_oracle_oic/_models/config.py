"""flext-tap-oracle-oic config models — typed business-rule shapes.

Frozen Pydantic shapes for the ``config/tap_oracle_oic.yaml`` business-rule SSOT.
The ``_config.py`` facade validates the model-less YAML slice into these
classes and exposes the ready objects under ``config.TapOracleOic``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class FlextTapOracleOicConfigModels:
    """Namespace of typed flext-tap-oracle-oic config models."""

    class Api(BaseModel):
        """Oracle OIC tap API defaults and connection policy."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        base_url: str = Field(
            description="Default Oracle Integration Cloud base URL.",
        )
        request_timeout: int = Field(
            ge=1,
            description="Default request timeout in seconds.",
        )
        max_retries: int = Field(
            ge=0,
            description="Maximum retry attempts for idempotent requests.",
        )
        page_size: int = Field(
            ge=1,
            description="Default page size for paginated list endpoints.",
        )
        verify_ssl: bool = Field(
            description="Whether to verify TLS certificates by default.",
        )
        http_error_status_threshold: int = Field(
            ge=100,
            le=599,
            description="HTTP status codes at or above this value are treated as errors.",
        )

    class Streams(BaseModel):
        """Oracle OIC tap stream catalog defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        core: tuple[str, ...] = Field(
            description="Core OIC entity streams.",
        )
        infrastructure: tuple[str, ...] = Field(
            description="Infrastructure OIC streams.",
        )

    class Pagination(BaseModel):
        """Oracle OIC tap pagination policy defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        max_page_size: int = Field(
            ge=1,
            description="Maximum page size accepted by the API.",
        )
        min_page_size: int = Field(
            ge=1,
            description="Minimum page size accepted by the API.",
        )
        default_start: int = Field(
            ge=0,
            description="Default start offset for paginated requests.",
        )
        default_page_size: int = Field(
            ge=1,
            description="Default page size for paginated requests.",
        )

    class Thresholds(BaseModel):
        """Oracle OIC tap runtime threshold defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        min_token_expiry_buffer: int = Field(
            ge=0,
            description="Minimum seconds before token expiry to trigger refresh.",
        )
        slow_response_threshold: float = Field(
            ge=0,
            description="Response time in seconds considered slow.",
        )
        response_time_history_size: int = Field(
            ge=1,
            description="Number of response samples kept for rolling metrics.",
        )
        min_response_samples: int = Field(
            ge=1,
            description="Minimum response samples before slow-response alerting.",
        )

    class Percentages(BaseModel):
        """Oracle OIC tap percentage range defaults."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        min: float = Field(
            ge=0,
            le=100,
            description="Minimum percentage value.",
        )
        max: float = Field(
            ge=0,
            le=100,
            description="Maximum percentage value.",
        )

    class TapOracleOic(BaseModel):
        """Root Oracle OIC tap business-rule namespace."""

        model_config = ConfigDict(frozen=True, extra="forbid")

        api: FlextTapOracleOicConfigModels.Api = Field(
            description="Oracle OIC tap API defaults and connection policy.",
        )
        streams: FlextTapOracleOicConfigModels.Streams = Field(
            description="Oracle OIC tap stream catalog defaults.",
        )
        pagination: FlextTapOracleOicConfigModels.Pagination = Field(
            description="Oracle OIC tap pagination policy defaults.",
        )
        thresholds: FlextTapOracleOicConfigModels.Thresholds = Field(
            description="Oracle OIC tap runtime threshold defaults.",
        )
        percentages: FlextTapOracleOicConfigModels.Percentages = Field(
            description="Oracle OIC tap percentage range defaults.",
        )

    class Root(BaseModel):
        """Root flext-tap-oracle-oic config validated from ``config/*.yaml``."""

        model_config = ConfigDict(frozen=True, extra="ignore")

        TapOracleOic: FlextTapOracleOicConfigModels.TapOracleOic = Field(
            description="Oracle OIC tap business-rule config namespace.",
        )


__all__: list[str] = ["FlextTapOracleOicConfigModels"]
