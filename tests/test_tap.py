"""Tests for tap-oracle-oic."""

from __future__ import annotations

from flext_tap_oracle_oic.tap import TapOIC


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
        assert tap.name == "tap-oracle-oic"
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
        assert len(streams) >= 5
        stream_names = [s.name for s in streams]
        assert "integrations" in stream_names
        assert "connections" in stream_names

    def test_config_validation(self) -> None:
        """Test config validation."""
        import pytest
        # MIGRATED: from singer_sdk.exceptions import ConfigValidationError -> use flext_meltano
        from flext_meltano import ConfigValidationError

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
        assert "integrations" in stream_names
        assert "connections" in stream_names
        assert "packages" in stream_names
        assert "libraries" in stream_names
        assert "lookups" in stream_names
