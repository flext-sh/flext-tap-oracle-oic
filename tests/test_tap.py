"""Tests for tap-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest
from pydantic import ValidationError as ConfigValidationError

from flext_tap_oracle_oic import m
from flext_tap_oracle_oic.tap_client import TapOracleOic


def _build_source_config() -> m.Meltano.DataSourceConfig:
    return m.Meltano.DataSourceConfig(
        source_type="oracle-oic",
        connection_config={
            "base_url": "https://test.integration.ocp.oraclecloud.com",
        },
        stream_config={},
        source_version="latest",
    )


def _discover_stream_names(tap: TapOracleOic) -> list[str]:
    result = tap.discover_streams(source_config=_build_source_config())
    assert result.is_success
    assert result.value is not None
    return [str(stream["tap_stream_id"]) for stream in result.value["streams"]]


class TestTapOracleOic:
    """Test cases for TapOracleOic."""

    def test_tap_initialization(self) -> None:
        """Test method."""
        "Test tap initialization function."
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client",
            "oauth_client_secret": "test_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }
        tap = TapOracleOic(config=config, validate_config=False)
        if tap.name != "tap-oracle-oic":
            msg = f"Expected {'tap-oracle-oic'}, got {tap.name}"
            raise AssertionError(msg)
        assert tap.config == config

    def test_discover_streams(self) -> None:
        """Test method."""
        "Test discover streams function."
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client",
            "oauth_client_secret": "test_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }
        tap = TapOracleOic(config=config, validate_config=False)
        stream_names = _discover_stream_names(tap)
        if len(stream_names) < 5:
            msg = f"Expected {len(stream_names)} >= {5}"
            raise AssertionError(msg)
        if "integrations" not in stream_names:
            msg = f"Expected {'integrations'} in {stream_names}"
            raise AssertionError(msg)
        assert "connections" in stream_names

    def test_config_validation(self) -> None:
        """Test method."""
        "Test config validation."
        config = {"base_url": "https://test.integration.ocp.oraclecloud.com"}
        with pytest.raises(ConfigValidationError):
            TapOracleOic(config=config, validate_config=True)

    def test_include_extended_streams(self) -> None:
        """Test method."""
        "Test include extended streams function."
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client",
            "oauth_client_secret": "test_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "include_extended": True,
        }
        tap = TapOracleOic(config=config, validate_config=False)
        stream_names = _discover_stream_names(tap)
        if "integrations" not in stream_names:
            msg = f"Expected {'integrations'} in {stream_names}"
            raise AssertionError(msg)
        assert "connections" in stream_names
        if "packages" not in stream_names:
            msg = f"Expected {'packages'} in {stream_names}"
            raise AssertionError(msg)
        assert "libraries" in stream_names
        if "lookups" not in stream_names:
            msg = f"Expected {'lookups'} in {stream_names}"
            raise AssertionError(msg)
