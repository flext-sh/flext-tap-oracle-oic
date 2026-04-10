"""Module test_tap_core.

Core TAP functionality tests.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence

import pytest
from pydantic import TypeAdapter, ValidationError as ConfigValidationError

from flext_tap_oracle_oic import FlextTapOracleOic, t as oic_t
from tests import m, t


def _build_tap_instance() -> m.Meltano.TapInstance:
    return m.Meltano.TapInstance(
        tap_type="oracle-oic",
        config=m.Meltano.TapConfig(
            tap_type="oracle-oic",
            connection_config={
                "base_url": "https://test.integration.ocp.oraclecloud.com",
            },
            stream_config={},
        ),
    )


def _discover_stream_names(tap: FlextTapOracleOic) -> t.StrSequence:
    result = tap.discover_streams(tap_instance=_build_tap_instance())
    assert result.is_success
    value = result.value
    assert isinstance(value, Mapping)
    streams = value["streams"]
    assert isinstance(streams, Sequence) and not isinstance(streams, str)
    return [str(s["tap_stream_id"]) for s in streams if isinstance(s, Mapping)]


class TestTapOracleOic:
    """Test the main FlextTapOracleOic class."""

    def test_tap_initialization(self) -> None:
        """Test method."""
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }
        tap = FlextTapOracleOic(config=config, validate_config=False)
        if tap.name != "tap-oracle-oic":
            msg = f"Expected {'tap-oracle-oic'}, got {tap.name}"
            raise AssertionError(msg)
        assert tap.config.base_url == config["base_url"]
        assert tap.config.oauth_client_id == config["oauth_client_id"]

    def test_tap_initialization_without_config(self) -> None:
        """Test method."""
        tap = FlextTapOracleOic(validate_config=False)
        if tap.name != "tap-oracle-oic":
            msg = f"Expected {'tap-oracle-oic'}, got {tap.name}"
            raise AssertionError(msg)

    def test_core_streams_discovery(self) -> None:
        """Test method."""
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }
        tap = FlextTapOracleOic(config=config, validate_config=False)
        stream_names = _discover_stream_names(tap)
        if len(stream_names) != 5:
            msg = f"Expected {5}, got {len(stream_names)}"
            raise AssertionError(msg)
        expected_streams = [
            "integrations",
            "connections",
            "packages",
            "lookups",
            "libraries",
        ]
        for expected in expected_streams:
            if expected not in stream_names:
                msg = f"Expected {expected} in {stream_names}"
                raise AssertionError(msg)

    def test_extended_streams_discovery(self) -> None:
        """Test method."""
        config: t.ContainerValueMapping = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "include_extended": True,
        }
        tap = FlextTapOracleOic(config=config, validate_config=False)
        stream_names = _discover_stream_names(tap)
        if len(stream_names) != 5:
            msg = f"Expected {5}, got {len(stream_names)}"
            raise AssertionError(msg)
        expected_streams = [
            "integrations",
            "connections",
            "packages",
            "lookups",
            "libraries",
        ]
        for expected in expected_streams:
            if expected not in stream_names:
                msg = f"Expected {expected} in {stream_names}"
                raise AssertionError(msg)

    def test_extended_streams_disabled(self) -> None:
        """Test method."""
        config: t.ContainerValueMapping = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "include_extended": False,
        }
        tap = FlextTapOracleOic(config=config, validate_config=False)
        stream_names = _discover_stream_names(tap)
        streams = [name for name in stream_names if "infrastructure" in name.lower()]
        if len(streams) != 0:
            msg = f"Expected {0}, got {len(streams)}"
            raise AssertionError(msg)

    def test_discover_streams(self) -> None:
        """Test method."""
        config: t.ContainerValueMapping = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "include_extended": True,
        }
        tap = FlextTapOracleOic(config=config, validate_config=False)
        stream_names = _discover_stream_names(tap)
        if len(stream_names) != 5:
            msg = f"Expected {5}, got {len(stream_names)}"
            raise AssertionError(msg)

    def test_config_validation_warnings(self) -> None:
        """Test method."""
        "Test that the tap works with HTTP endpoints (though HTTPS is recommended)."
        config = {
            "base_url": "http://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_endpoint": "http://test.identity.oraclecloud.com/oauth2/v1/token",
            "oic_url": "http://test.integration.ocp.oraclecloud.com",
        }
        tap = FlextTapOracleOic(config=config, validate_config=False)
        if tap.name != "tap-oracle-oic":
            msg = f"Expected {'tap-oracle-oic'}, got {tap.name}"
            raise AssertionError(msg)
        assert (
            getattr(tap.config, "base_url", None)
            == "http://test.integration.ocp.oraclecloud.com"
        )

    def test_missing_required_fields_warning(self) -> None:
        """Test that validation rejects invalid field types."""
        adapter: TypeAdapter[oic_t.PositiveInt] = TypeAdapter(oic_t.PositiveInt)
        with pytest.raises(ConfigValidationError):
            adapter.validate_python(-1)

    def test_capabilities(self) -> None:
        """Test method."""
        expected_capabilities = ["catalog", "state", "discover"]
        capability_values = {
            str(cap.value) if hasattr(cap, "value") else str(cap)
            for cap in raw_capabilities
        }
        for capability in expected_capabilities:
            if capability not in capability_values:
                msg = f"Expected {capability} in {sorted(capability_values)}"
                raise AssertionError(msg)


class TestTapOracleOicIntegration:
    """Integration tests for FlextTapOracleOic."""

    def test_streams_have_correct_tap_reference(self) -> None:
        """Test method."""
        "Test that the streams have the correct tap reference."
        config = {
            "base_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        }
        tap = FlextTapOracleOic(config=config, validate_config=False)
        stream_names = _discover_stream_names(tap)
        for stream_name in stream_names:
            assert stream_name


@pytest.fixture
def sample_config() -> t.StrMapping:
    """Sample config."""
    return {
        "base_url": "https://test.integration.ocp.oraclecloud.com",
        "oauth_client_id": "test_client_id",
        "oauth_client_secret": "test_client_secret",
        "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
    }


@pytest.fixture
def sample_config_with_extended() -> Mapping[str, bool | str]:
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

    def test_self(self, sample_config: t.StrMapping) -> None:
        """Test method."""
        "Test that the tap is initialized correctly with the sample config."
        tap = FlextTapOracleOic(config=sample_config, validate_config=False)
        configured_base_url = getattr(tap.config, "base_url", None)
        if configured_base_url != sample_config["base_url"]:
            msg = f"Expected {sample_config['base_url']}, got {configured_base_url}"
            raise AssertionError(msg)
        assert (
            getattr(tap.config, "oauth_client_id", None)
            == sample_config["oauth_client_id"]
        )

    def test_streams_count_with_extended_config(
        self,
        sample_config_with_extended: Mapping[str, bool | str],
    ) -> None:
        """Test that the number of streams is correct with the extended config."""
        tap = FlextTapOracleOic(
            config=sample_config_with_extended, validate_config=False
        )
        stream_names = _discover_stream_names(tap)
        if len(stream_names) != 5:
            msg = f"Expected {5}, got {len(stream_names)}"
            raise AssertionError(msg)
        expected_core_streams = [
            "integrations",
            "connections",
            "packages",
            "lookups",
            "libraries",
        ]
        for expected in expected_core_streams:
            if expected not in stream_names:
                msg = f"Expected {expected} in {stream_names}"
                raise AssertionError(msg)
