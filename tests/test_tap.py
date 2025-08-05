"""Tests for tap-oracle-oic."""

from __future__ import annotations

import pytest
from flext_tap_oracle_oic.tap import TapOIC
from pydantic import ValidationError as ConfigValidationError


class TestTapOIC:
    """Test cases for TapOIC."""

    def test_tap_initialization(self) -> None:
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client",
            "oauth_client_secret": "test_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }
        tap = TapOIC(config=config, validate_config=False)
        if tap.name != "tap-oracle-oic":
            msg: str = f"Expected {'tap-oracle-oic'}, got {tap.name}"
            raise AssertionError(msg)
        assert tap.config == config

    def test_discover_streams(self) -> None:
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client",
            "oauth_client_secret": "test_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }
        tap = TapOIC(config=config, validate_config=False)
        streams = tap.discover_streams()

        # Should have at least core streams
        if len(streams) < 5:
            msg: str = f"Expected {len(streams)} >= {5}"
            raise AssertionError(msg)
        stream_names = [s.name for s in streams]
        if "integrations" not in stream_names:
            msg: str = f"Expected {'integrations'} in {stream_names}"
            raise AssertionError(msg)
        assert "connections" in stream_names

    def test_config_validation(self) -> None:
        """Test config validation."""
        # MIGRATED: from singer_sdk.exceptions import ConfigValidationError -> use flext_meltano

        # Missing required fields should raise exception when validation is enabled
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
        }
        with pytest.raises(ConfigValidationError):
            TapOIC(config=config, validate_config=True)

    def test_include_extended_streams(self) -> None:
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client",
            "oauth_client_secret": "test_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "include_extended": True,
        }
        tap = TapOIC(config=config, validate_config=False)
        streams = tap.discover_streams()

        # Should include core streams
        stream_names = [s.name for s in streams]
        if "integrations" not in stream_names:
            msg: str = f"Expected {'integrations'} in {stream_names}"
            raise AssertionError(msg)
        assert "connections" in stream_names
        if "packages" not in stream_names:
            msg: str = f"Expected {'packages'} in {stream_names}"
            raise AssertionError(msg)
        assert "libraries" in stream_names
        if "lookups" not in stream_names:
            msg: str = f"Expected {'lookups'} in {stream_names}"
            raise AssertionError(msg)
