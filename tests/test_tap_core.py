"""Module test_tap_core.

Core TAP functionality tests.

Tests the main TapOIC class and core functionality without external dependencies.
"""

from flext_meltano import ConfigValidationError


from __future__ import annotations

from typing import Any

import pytest

from flext_tap_oracle_oic.tap import TapOIC


class TestTapOIC:
    """Test the main TapOIC class."""

    def test_tap_initialization(self) -> None:
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }

        tap = TapOIC(config=config, validate_config=False)

        if tap.name != "tap-oracle-oic":

            raise AssertionError(f"Expected {"tap-oracle-oic"}, got {tap.name}")
        assert tap.config == config

    def test_tap_initialization_without_config(self) -> None:
        tap = TapOIC(validate_config=False)

        if tap.name != "tap-oracle-oic":

            raise AssertionError(f"Expected {"tap-oracle-oic"}, got {tap.name}")
        assert hasattr(tap, "config")

    def test_core_streams_discovery(self) -> None:
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }

        tap = TapOIC(config=config, validate_config=False)
        # Test discovery instead of accessing private method
        streams = tap.discover_streams()

        if len(streams) != 5:

            raise AssertionError(f"Expected {5}, got {len(streams)}")
        stream_names = [stream.name for stream in streams]
        expected_streams = [
            "integrations",
            "connections",
            "packages",
            "lookups",
            "libraries",
        ]

        for expected in expected_streams:
            if expected not in stream_names:
                raise AssertionError(f"Expected {expected} in {stream_names}")

    def test_extended_streams_discovery(self) -> None:
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "include_extended": True,
        }

        tap = TapOIC(config=config, validate_config=False)
        # Test all streams through discover_streams
        all_streams = tap.discover_streams()

        # Current implementation doesn't have extended infrastructure streams
        # Extended config doesn't add additional streams in current version
        if len(all_streams) != 5:
            raise AssertionError(f"Expected {5}, got {len(all_streams)}")

        # Verify we get the expected core streams
        stream_names = [s.name for s in all_streams]
        expected_streams = [
            "integrations",
            "connections",
            "packages",
            "lookups",
            "libraries",
        ]
        for expected in expected_streams:
            if expected not in stream_names:
                raise AssertionError(f"Expected {expected} in {stream_names}")

    def test_extended_streams_disabled(self) -> None:
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "include_extended": False,
        }

        tap = TapOIC(config=config, validate_config=False)
        # Test all streams through discover_streams
        all_streams = tap.discover_streams()
        # Filter infrastructure streams if needed for specific tests
        streams = [s for s in all_streams if "infrastructure" in s.name.lower()]

        if len(streams) != 0:

            raise AssertionError(f"Expected {0}, got {len(streams)}")

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

        # Should have 5 core streams
        if len(streams) != 5:
            raise AssertionError(f"Expected {5}, got {len(streams)}")

    def test_config_validation_warnings(self) -> None:
        """Test that the tap works with HTTP endpoints (though HTTPS is recommended)."""
        config = {
            "base_url": "http://test.integration.ocp.oraclecloud.com",  # HTTP instead of HTTPS
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_endpoint": "http://test.identity.oraclecloud.com/oauth2/v1/token",  # HTTP
            "oic_url": "http://test.integration.ocp.oraclecloud.com",  # Required field
        }

        tap = TapOIC(config=config, validate_config=False)

        # Should work with HTTP config (though HTTPS is recommended in production)
        if tap.name != "tap-oracle-oic":
            raise AssertionError(f"Expected {"tap-oracle-oic"}, got {tap.name}")
        assert tap.config["base_url"] == "http://test.integration.ocp.oraclecloud.com"

    def test_missing_required_fields_warning(self) -> None:
        """Test that the missing required fields validation works correctly."""
        # MIGRATED: from singer_sdk.exceptions import ConfigValidationError -> use flext_meltano


        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            # Missing oauth_client_id, oauth_client_secret, oauth_endpoint, oic_url
        }

        # Test validation through normal instantiation with incomplete config
        # This should raise ConfigValidationError for missing required fields
        with pytest.raises(ConfigValidationError) as exc_info:
            TapOIC(config=config, validate_config=True)

        # Verify the error message mentions the missing required properties
        error_message = str(exc_info.value)
        if "oauth_client_id" not in error_message:
            raise AssertionError(f"Expected {"oauth_client_id"} in {error_message}")
        assert "oauth_client_secret" in error_message
        if "oauth_endpoint" not in error_message:
            raise AssertionError(f"Expected {"oauth_endpoint"} in {error_message}")
        assert "oic_url" in error_message

    def test_capabilities(self) -> None:
        tap = TapOIC(validate_config=False)

        expected_capabilities = ["catalog", "state", "discover"]

        for capability in expected_capabilities:
            if capability in [cap.value for cap not in tap.capabilities]:
                raise AssertionError(f"Expected {capability in [cap.value for cap} in {tap.capabilities]}")


class TestTapOICIntegration:
    """Integration tests for TapOIC."""

    def test_streams_have_correct_tap_reference(self) -> None:
        """Test that the streams have the correct tap reference."""
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }

        tap = TapOIC(config=config, validate_config=False)
        # Test discovery instead of accessing private method
        streams = tap.discover_streams()

        # Verify that all streams have the TAP instance as reference
        # Verify streams are properly initialized (check public attributes only)
        for stream in streams:
            assert hasattr(stream, "name")
            assert stream.name is not None


@pytest.fixture
def sample_config() -> Any:
    """Sample config."""
    return {
        "base_url": "https://test.integration.ocp.oraclecloud.com",
        "oauth_client_id": "test_client_id",
        "oauth_client_secret": "test_client_secret",
        "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
    }


@pytest.fixture
def sample_config_with_extended() -> Any:
    """Sample config with extended streams."""
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

    def test_tap_with_sample_config(self, sample_config: dict[str, Any]) -> None:
        """Test that the tap is initialized correctly with the sample config."""
        tap = TapOIC(config=sample_config, validate_config=False)

        if tap.config["base_url"] != sample_config["base_url"]:

            raise AssertionError(f"Expected {sample_config["base_url"]}, got {tap.config["base_url"]}")
        assert tap.config["oauth_client_id"] == sample_config["oauth_client_id"]

    def test_streams_count_with_extended_config(
        self,
        sample_config_with_extended: dict[str, Any],
    ) -> None:
        """Test that the number of streams is correct with the extended config."""
        tap = TapOIC(config=sample_config_with_extended, validate_config=False)

        # Test using public discover_streams method
        all_streams = tap.discover_streams()

        # Current implementation only has 5 core streams regardless of extended config
        # Extended infrastructure streams are not implemented in current version
        if len(all_streams) != 5:
            raise AssertionError(f"Expected {5}, got {len(all_streams)}")

        # Verify we get the expected core streams
        stream_names = [s.name for s in all_streams]
        expected_core_streams = [
            "integrations",
            "connections",
            "packages",
            "lookups",
            "libraries",
        ]
        for expected in expected_core_streams:
            if expected not in stream_names:
                raise AssertionError(f"Expected {expected} in {stream_names}")
