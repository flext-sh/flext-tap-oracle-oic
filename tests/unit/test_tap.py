"""Observable behavior of the public Oracle OIC tap facade.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from flext_api import m as api_m
from flext_tests import tm

from flext_tap_oracle_oic import FlextTapOracleOicPaginator, FlextTapOracleOicSettings, c
from tests import u

if TYPE_CHECKING:
    from flext_tap_oracle_oic import FlextTapOracleOic, m


class TestsFlextTapOracleOic:
    """Public tap construction and Singer discovery contracts."""

    def test_default_tap_exposes_typed_public_settings(
        self, tap_oracle_oic: FlextTapOracleOic, tap_instance: m.Meltano.TapInstance
    ) -> None:
        """The public facade exposes typed settings and its request identity."""
        tm.that(tap_oracle_oic.oic_settings, is_=FlextTapOracleOicSettings)
        tm.that(tap_instance.tap_type, eq=tap_oracle_oic.name)

    def test_discovery_returns_the_canonical_public_stream_catalog(
        self, tap_oracle_oic: FlextTapOracleOic, tap_instance: m.Meltano.TapInstance
    ) -> None:
        """Discovery returns exactly the streams owned by the public constants."""
        names = u.TapOracleOic.Tests.discover_stream_names(tap_oracle_oic, tap_instance)

        tm.that(names, eq=tuple(c.TapOracleOic.CORE_STREAMS))

    @pytest.mark.parametrize("envelope_key", ["items", "data"])
    def test_paginator_returns_raw_tokens_and_stops_on_empty_pages(
        self, envelope_key: str
    ) -> None:
        """Singer consumes a token or None, never a result wrapper."""
        paginator = FlextTapOracleOicPaginator()
        records = [
            {"id": str(index)}
            for index in range(c.TapOracleOic.DEFAULT_PAGINATOR_PAGE_SIZE)
        ]
        response = api_m.Api.HttpResponse(
            status_code=200, body={envelope_key: records}
        )

        tm.that(
            paginator.get_next(response),
            eq=paginator.current_value + len(records),
        )
        empty_response = api_m.Api.HttpResponse(
            status_code=200, body={envelope_key: []}
        )
        assert paginator.get_next(empty_response) is None

    @pytest.mark.parametrize("envelope_key", ["items", "data"])
    def test_paginator_rejects_malformed_pages(self, envelope_key: str) -> None:
        """Malformed collection payloads cannot signal successful exhaustion."""
        response = api_m.Api.HttpResponse(
            status_code=200, body={envelope_key: "not-a-collection"}
        )

        with pytest.raises(c.ValidationError):
            FlextTapOracleOicPaginator().get_next(response)
