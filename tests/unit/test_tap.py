"""Tests for tap-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import (
    Mapping,
    Sequence,
)

import pytest
from flext_tests import tm

from flext_tap_oracle_oic.tap import FlextTapOracleOic as TapOracleOic
from tests import c, m, t


def _build_tap_instance() -> p.Meltano.TapInstance:
    return m.Meltano.TapInstance(
        tap_type="oracle-oic",
        settings=m.Meltano.TapConfig(
            tap_type="oracle-oic",
            connection_config={
                "base_url": "https://test.integration.ocp.oraclecloud.com",
            },
            stream_config={},
        ),
    )


def _discover_stream_names(tap: TapOracleOic) -> t.StrSequence:
    result = tap.discover_streams(tap_instance=_build_tap_instance())
    tm.ok(result)
    value = result.value
    tm.that(value, is_=Mapping)
    streams = value["streams"]
    assert isinstance(streams, Sequence) and not isinstance(streams, str)
    return [str(s["tap_stream_id"]) for s in streams if isinstance(s, Mapping)]


class TestsFlextTapOracleOicTap:
    """Test cases for TapOracleOic."""

    def test_tap_initialization(self) -> None:
        """Test method."""
        "Test tap initialization function."
        settings = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client",
            "oauth_client_secret": "test_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }
        tap = TapOracleOic(settings=settings, validate_config=False)
        if tap.name != "tap-oracle-oic":
            msg = f"Expected {'tap-oracle-oic'}, got {tap.name}"
            raise AssertionError(msg)
        tm.that(tap.oic_settings.TapOracleOic.base_url, eq=settings["base_url"])
        assert (
            tap.oic_settings.TapOracleOic.oauth_client_id == settings["oauth_client_id"]
        )

    def test_discover_streams(self) -> None:
        """Test method."""
        "Test discover streams function."
        settings = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client",
            "oauth_client_secret": "test_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }
        tap = TapOracleOic(settings=settings, validate_config=False)
        stream_names = _discover_stream_names(tap)
        if len(stream_names) < 5:
            msg = f"Expected {len(stream_names)} >= {5}"
            raise AssertionError(msg)
        if "integrations" not in stream_names:
            msg = f"Expected {'integrations'} in {stream_names}"
            raise AssertionError(msg)
        tm.that(stream_names, has="connections")

    def test_config_validation(self) -> None:
        """Test method."""
        "Test settings validation rejects invalid field types."

        adapter: m.TypeAdapter[t.PositiveInt] = m.TypeAdapter(t.PositiveInt)
        with pytest.raises(c.ValidationError):
            adapter.validate_python(-1)

    def test_include_extended_streams(self) -> None:
        """Test method."""
        "Test include extended streams function."
        settings: t.JsonMapping = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client",
            "oauth_client_secret": "test_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "include_extended": True,
        }
        tap = TapOracleOic(settings=settings, validate_config=False)
        stream_names = _discover_stream_names(tap)
        if "integrations" not in stream_names:
            msg = f"Expected {'integrations'} in {stream_names}"
            raise AssertionError(msg)
        tm.that(stream_names, has="connections")
        if "packages" not in stream_names:
            msg = f"Expected {'packages'} in {stream_names}"
            raise AssertionError(msg)
        tm.that(stream_names, has="libraries")
        if "lookups" not in stream_names:
            msg = f"Expected {'lookups'} in {stream_names}"
            raise AssertionError(msg)
