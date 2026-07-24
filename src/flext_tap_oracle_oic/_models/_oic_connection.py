"""OracleOic.FlextTapOracleOicConnection entity model.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from flext_oracle_oic import m
from flext_tap_oracle_oic import c, t, u

if TYPE_CHECKING:
    from datetime import datetime


class FlextTapOracleOicConnection(m):
    """OIC connection domain entity using flext-core patterns."""

    connection_id: Annotated[
        str, u.Field(..., min_length=1, description="OIC connection identifier")
    ]
    adapter_type: Annotated[
        str,
        u.Field(..., min_length=1, description="Adapter type (e.g., REST, SOAP, DB)"),
    ]
    name: Annotated[str, u.Field(..., min_length=1, description="Connection name")]
    connection_url: Annotated[
        str | None, u.Field(None, description="Connection endpoint URL")
    ]
    connection_properties: Annotated[
        t.MappingKV[str, t.JsonMapping], u.Field(description="Connection properties")
    ] = u.Field(default_factory=dict)
    security_policy: Annotated[
        str | None, u.Field(None, description="Security policy name")
    ]
    connection_status: Annotated[
        c.TapOracleOic.ConnectionStatus, u.Field(description="Connection status")
    ] = c.TapOracleOic.ConnectionStatus.CONFIGURED
    last_tested: Annotated[
        datetime | None, u.Field(None, description="Last test timestamp")
    ]
    test_result: Annotated[
        t.StrMapping | None, u.Field(None, description="Last test result")
    ]
    version: Annotated[str | None, u.Field(None, description="Connection version")]
    locked_by: Annotated[
        str | None, u.Field(None, description="User who locked the connection")
    ]
    locked_at: Annotated[datetime | None, u.Field(None, description="Lock timestamp")]
    created_at: Annotated[
        datetime | None, u.Field(None, description="Creation timestamp")
    ]
    updated_at: Annotated[
        datetime | None, u.Field(None, description="Last update timestamp")
    ]

    def mark_failed(self, _error: str) -> None:
        """Mark connection as failed with error details."""
        self.connection_status = c.TapOracleOic.ConnectionStatus.FAILED
        self.test_result = {
            "error": c.TapOracleOic.OicErrorSeverity.ERROR.value,
            "timestamp": u.now().isoformat(),
        }

    def test_connection(self) -> None:
        """Mark connection as tested."""
        self.last_tested = u.now()
        self.connection_status = c.TapOracleOic.ConnectionStatus.TESTED


__all__: list[str] = ["FlextTapOracleOicConnection"]
