"""Module test_tap_core.

from typing import Any

"""Core TAP functionality tests.

Tests the main TapOIC class and core functionality without external dependencies.
"""

import pytest

from tap_oracle_oic.tap import TapOIC


class TestTapOIC:
         Test the main TapOIC class."""

    def test_tap_initialization(self) -> None:
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }

        tap = TapOIC(config=config, validate_config=False)

        assert tap.name == "tap-oic"
        assert tap.config == config

    def test_tap_initialization_without_config(self) -> None:
        tap = TapOIC(validate_config=False)

        assert tap.name == "tap-oic"
        assert hasattr(tap, "config")

    def test_core_streams_discovery(self) -> None:
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }

        tap = TapOIC(config=config, validate_config=False)
        streams = tap._get_core_streams()

        assert len(streams) == 6
        stream_names = [stream.name for stream in streams]
        expected_streams = [
            "integrations",
            "connections",
            "packages",
            "lookups",
            "libraries",
            "certificates",
        ]

        for expected in expected_streams:
            assert expected in stream_names

    def test_extended_streams_discovery(self) -> None:
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "include_extended": True,
        }

        tap = TapOIC(config=config, validate_config=False)
        streams = tap._get_infrastructure_streams()

        assert len(streams) == 2
        stream_names = [s.name for s in streams]
        assert "adapters" in stream_names
        assert "agent_groups" in stream_names

    def test_extended_streams_disabled(self) -> None:
            config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "include_extended": False,
        }

        tap = TapOIC(config=config, validate_config=False)
        streams = tap._get_infrastructure_streams()

        assert len(streams) == 0

    def test_discover_streams(self) -> None:
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "include_extended": True,
        }

        tap = TapOIC(config=config, validate_config=False)
        streams = tap.discover_streams()

        # Should have 6 core + 2 infrastructure = 8 streams
        assert len(streams) == 8

    def test_config_validation_warnings(self, caplog) -> None:
        config = {
            "base_url": "http://test.integration.ocp.oraclecloud.com",  # HTTP instead of HTTPS
            "auth_method": "basic",  # Wrong auth method
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "http://test.identity.oraclecloud.com/oauth2/v1/token",  # HTTP
        }

        TapOIC(config=config)

        # Check that warnings were logged
        assert "not recommended" in caplog.text
        assert "should use HTTPS" in caplog.text

    def test_missing_required_fields_warning(self, caplog) -> None:
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            # Missing oauth_client_id, oauth_client_secret, oauth_token_url
        }

        # Use validate_config=False and call our validation method directly
        tap = TapOIC(config=config, validate_config=False)
        tap._validate_oic_config()

        assert "Missing required fields" in caplog.text

    def test_capabilities(self) -> None:
        tap = TapOIC(validate_config=False)

        expected_capabilities = ["catalog", "state", "discover"]

        for capability in expected_capabilities:
            assert capability in [cap.value for cap in tap.supported_capabilities]


class TestTapOICIntegration:
         """Integration tests for TapOIC."""

    def test_streams_have_correct_tap_reference(self) -> None:
            config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }

        tap = TapOIC(config=config, validate_config=False)
        streams = tap._get_core_streams()

        # Verify that all streams have the TAP instance as reference
        for stream in streams:
            assert hasattr(stream, "_tap")
            assert stream._tap is tap


@pytest.fixture
def sample_config() -> Any:
        return {
        "base_url": "https://test.integration.ocp.oraclecloud.com",
        "oauth_client_id": "test_client_id",
        "oauth_client_secret": "test_client_secret",
        "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
    }


@pytest.fixture
def sample_config_with_extended() -> Any:
        return {
        "base_url": "https://test.integration.ocp.oraclecloud.com",
        "oauth_client_id": "test_client_id",
        "oauth_client_secret": "test_client_secret",
        "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        "include_extended": True,
        "include_monitoring": True,
        "include_logs": True,
        "include_artifacts": True,
    }


class TestTapOICWithFixtures:
         """Tests using fixtures."""

    def test_tap_with_sample_config(self, sample_config) -> None:
        tap = TapOIC(config=sample_config, validate_config=False)

        assert tap.config["base_url"] == sample_config["base_url"]
        assert tap.config["oauth_client_id"] == sample_config["oauth_client_id"]

    def test_streams_count_with_extended_config(self,
        sample_config_with_extended,
    ) -> None:
        tap = TapOIC(config=sample_config_with_extended, validate_config=False)

        core_streams = tap._get_core_streams()
        extended_streams = tap._get_infrastructure_streams()

        assert len(core_streams) == 6
        assert len(extended_streams) >= 2  # At least adapters and agent_groups streams
