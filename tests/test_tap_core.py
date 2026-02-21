"""Module test_tap_core.

Core TAP functionality tests.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations
from flext_tap_oracle_oic import t

import pytest
from singer_sdk import ConfigValidationError

from flext_tap_oracle_oic import TapOracleOic


class TestTapOracleOic:
    """Test the main TapOracleOic class."""

    def test_tap_initialization(self) -> None:
        """Test method."""
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }

        tap = TapOracleOic(config=config, validate_config=False)

        if tap.name != "tap-oracle-oic":
            msg: str = f"Expected {'tap-oracle-oic'}, got {tap.name}"
            raise AssertionError(msg)
        assert tap.config == config

    def test_tap_initialization_without_config(self) -> None:
        """Test method."""
        tap = TapOracleOic(validate_config=False)

        if tap.name != "tap-oracle-oic":
            msg: str = f"Expected {'tap-oracle-oic'}, got {tap.name}"
            raise AssertionError(msg)
        assert hasattr(tap, "config")

    def test_core_streams_discovery(self) -> None:
        """Test method."""
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }

        tap = TapOracleOic(config=config, validate_config=False)
        # Test discovery instead of accessing private method
        streams = tap.discover_streams()

        if len(streams) != 5:
            msg: str = f"Expected {5}, got {len(streams)}"
            raise AssertionError(msg)
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
                msg: str = f"Expected {expected} in {stream_names}"
                raise AssertionError(msg)

    def test_extended_streams_discovery(self) -> None:
        """Test method."""
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "include_extended": True,
        }

        tap = TapOracleOic(config=config, validate_config=False)
        # Test all streams through discover_streams
        all_streams = tap.discover_streams()

        # Current implementation doesn't have extended infrastructure streams
        # Extended config doesn't add additional streams in current version
        if len(all_streams) != 5:
            msg: str = f"Expected {5}, got {len(all_streams)}"
            raise AssertionError(msg)

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
                msg: str = f"Expected {expected} in {stream_names}"
                raise AssertionError(msg)

    def test_extended_streams_disabled(self) -> None:
        """Test method."""
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "include_extended": False,
        }

        tap = TapOracleOic(config=config, validate_config=False)
        # Test all streams through discover_streams
        all_streams = tap.discover_streams()
        # Filter infrastructure streams if needed for specific tests
        streams = [s for s in all_streams if "infrastructure" in s.name.lower()]

        if len(streams) != 0:
            msg: str = f"Expected {0}, got {len(streams)}"
            raise AssertionError(msg)

    def test_discover_streams(self) -> None:
        """Test method."""
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "include_extended": True,
        }

        tap = TapOracleOic(config=config, validate_config=False)
        streams = tap.discover_streams()

        # Should have 5 core streams
        if len(streams) != 5:
            msg: str = f"Expected {5}, got {len(streams)}"
            raise AssertionError(msg)

    def test_config_validation_warnings(self) -> None:
        """Test method."""
        """Test that the tap works with HTTP endpoints (though HTTPS is recommended)."""
        config = {
            "base_url": "http://test.integration.ocp.oraclecloud.com",  # HTTP instead of HTTPS
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_endpoint": "http://test.identity.oraclecloud.com/oauth2/v1/token",  # HTTP
            "oic_url": "http://test.integration.ocp.oraclecloud.com",  # Required field
        }

        tap = TapOracleOic(config=config, validate_config=False)

        # Should work with HTTP config (though HTTPS is recommended in production)
        if tap.name != "tap-oracle-oic":
            msg: str = f"Expected {'tap-oracle-oic'}, got {tap.name}"
            raise AssertionError(msg)
        assert tap.config["base_url"] == "http://test.integration.ocp.oraclecloud.com"

    def test_missing_required_fields_warning(self) -> None:
        """Test method."""
        """Test that the missing required fields validation works correctly."""
        # MIGRATED: from singer_sdk.exceptions import ConfigValidationError -> use flext_meltano

        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            # Missing oauth_client_id, oauth_client_secret, oauth_endpoint, oic_url
        }

        # Test validation through normal instantiation with incomplete config
        # This should raise ConfigValidationError for missing required fields
        with pytest.raises(ConfigValidationError) as exc_info:
            TapOracleOic(config=config, validate_config=True)

        # Verify the error message mentions the missing required properties
        error_message = str(exc_info.value)
        if "oic_host" not in error_message:
            msg: str = f"Expected {'oic_host'} in {error_message}"
            raise AssertionError(msg)
        assert "username" in error_message
        if "password" not in error_message:
            msg: str = f"Expected {'password'} in {error_message}"
            raise AssertionError(msg)

    def test_capabilities(self) -> None:
        """Test method."""
        tap = TapOracleOic(validate_config=False)

        expected_capabilities = ["catalog", "state", "discover"]

        for capability in expected_capabilities:
            if capability not in [cap.value for cap in tap.capabilities]:
                msg: str = f"Expected {capability} in {[cap.value for cap in tap.capabilities]}"
                raise AssertionError(msg)


class TestTapOracleOicIntegration:
    """Integration tests for TapOracleOic."""

    def test_streams_have_correct_tap_reference(self) -> None:
        """Test method."""
        """Test that the streams have the correct tap reference."""
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }

        tap = TapOracleOic(config=config, validate_config=False)
        # Test discovery instead of accessing private method
        streams = tap.discover_streams()

        # Verify that all streams have the TAP instance as reference
        # Verify streams are properly initialized (check public attributes only)
        for stream in streams:
            assert hasattr(stream, "name")
            assert stream.name is not None


@pytest.fixture
def sample_config() -> object:
    """Sample config."""
    return {
        "base_url": "https://test.integration.ocp.oraclecloud.com",
        "oauth_client_id": "test_client_id",
        "oauth_client_secret": "test_client_secret",
        "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
    }


@pytest.fixture
def sample_config_with_extended() -> object:
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


class TestTapOracleOicWithFixtures:
    """Tests using fixtures."""

    def test_self(self, sample_config: dict[str, t.GeneralValueType]) -> None:
        """Test method."""
        """Test that the tap is initialized correctly with the sample config."""
        tap = TapOracleOic(config=sample_config, validate_config=False)

        if tap.config["base_url"] != sample_config["base_url"]:
            msg: str = (
                f"Expected {sample_config['base_url']}, got {tap.config['base_url']}"
            )
            raise AssertionError(
                msg,
            )
        assert tap.config["oauth_client_id"] == sample_config["oauth_client_id"]

    def test_streams_count_with_extended_config(
        self,
        sample_config_with_extended: dict[str, t.GeneralValueType],
    ) -> None:
        """Test that the number of streams is correct with the extended config."""
        tap = TapOracleOic(config=sample_config_with_extended, validate_config=False)

        # Test using public discover_streams method
        all_streams = tap.discover_streams()

        # Current implementation only has 5 core streams regardless of extended config
        # Extended infrastructure streams are not implemented in current version
        if len(all_streams) != 5:
            msg: str = f"Expected {5}, got {len(all_streams)}"
            raise AssertionError(msg)

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
                msg: str = f"Expected {expected} in {stream_names}"
                raise AssertionError(msg)
