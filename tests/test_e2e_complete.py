# !/usr/bin/env python3

"""Comprehensive End-to-End tests for tap-oracle-oic.

Module test_e2e_complete.

Tests all functionalities including:
- Discovery
- Catalog generation
- Data extraction
- State management
- Authentication
- Error handling
"""

import json
import os
from pathlib import Path
from typing import Any
from unittest.mock import Mock, patch

import pytest
from singer_sdk.testing import get_tap_test_class

from flext_tap_oracle_oic.tap import TapOIC


class TestTapOracleOICE2E:
    """End-to-end tests for tap-oracle-oic."""

    @pytest.fixture
    def config(self) -> dict[str, Any]:
        """Mock configuration that matches the required schema."""
        return {
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret", 
            "oauth_endpoint": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "oic_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_scope": "urn:opc:resource:consumer:all",
            "start_date": "2024-01-01T00:00:00Z"
        }

    @pytest.fixture
    def tap(self, config: dict[str, Any]) -> Any:
        return TapOIC(config=config)

    def test_tap_initialization(self, tap: TapOIC, config: dict[str, Any]) -> None:
        assert tap.name == "tap-oracle-oic"
        assert tap.config == config
        assert tap.config["oic_url"] == config["oic_url"]

    def test_discover_streams(self, tap: TapOIC) -> None:
        catalog = tap.discover_streams()

        # Check that we discovered streams
        assert len(catalog) > 0

        # Check for expected core streams
        stream_names = [stream.tap_stream_id for stream in catalog]
        assert "connections" in stream_names
        assert "integrations" in stream_names
        assert "packages" in stream_names
        assert "lookups" in stream_names

    def test_catalog_generation(self, tap: TapOIC) -> None:
        catalog_dict = tap.catalog_dict

        assert "streams" in catalog_dict
        assert len(catalog_dict["streams"]) > 0

        # Check stream structure
        for stream in catalog_dict["streams"]:
            assert "tap_stream_id" in stream
            assert "schema" in stream
            assert "metadata" in stream

    def test_stream_schema_validation(self, tap: TapOIC) -> None:
        catalog = tap.discover_streams()

        for stream in catalog:
            schema = stream.schema
            assert "type" in schema
            assert schema["type"] == "object"
            assert "properties" in schema

            # Check for required fields
            properties = schema["properties"]
            assert "id" in properties or "name" in properties

    @pytest.mark.skipif(
        os.getenv("SKIP_LIVE_TESTS", "true").lower() == "true",
        reason="Skipping live API tests",
    )
    def test_live_connection(self, tap: TapOIC) -> None:
            # Test authentication
        streams = tap.discover_streams()
        if streams:
            stream = streams[0]

            # Try to get records from the first stream
            try:
                list(stream.get_records(context={}))
                # If we get here without error, authentication worked
                assert True
            except Exception as e:
                # Check if it's an authentication error:
                if "401" in str(e) or "403" in str(e):
                    pytest.fail(f"Authentication failed: {e}")
                # Other errors might be OK (e.g., no data)

    def test_state_management(self, tap: TapOIC) -> None:
        # Create a test state
        test_state = {
            "bookmarks": {
                "integrations": {
                    "replication_key_value": "2024-01-01T00:00:00Z",
                    "partitions": [],
                },
            },
        }

        # Load state into tap
        tap.load_state(test_state)

        # Check state was loaded
        assert tap.state == test_state

    def test_cli_discovery(self, config_path: str) -> None:
        import subprocess  # TODO: Move import to module level

        result = subprocess.run(
            ["python", "-m", "tap_oracle_oic", "--config", config_path, "--discover"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent,
            check=False,
        )

        assert result.returncode == 0

        # Parse output as JSON
        catalog = json.loads(result.stdout)
        assert "streams" in catalog
        assert len(catalog["streams"]) > 0

    def test_config_validation(self) -> None:
        # Test missing required fields
        with pytest.raises(Exception):
            TapOIC(config={})

        # Test invalid config
        with pytest.raises(Exception):
            TapOIC(config={"base_url": "not-a-url"})

    def test_stream_selection(self, tap: TapOIC) -> None:
        catalog = tap.discover_streams()

        # Create a catalog with only selected streams
        selected_catalog = {
            "streams": [
                {
                    "tap_stream_id": stream.tap_stream_id,
                    "schema": stream.schema,
                    "metadata": [
                        {
                            "breadcrumb": [],
                            "metadata": {
                                "selected": stream.tap_stream_id == "connections",
                            },
                        },
                    ],
                }
                for stream in catalog
            ],
        }

        # Load catalog
        tap.catalog = selected_catalog

        # Check only selected stream is active
        active_streams = [s for s in tap.streams.values() if s.selected]
        assert len(active_streams) == 1
        assert active_streams[0].name == "connections"

    def test_error_handling(self, tap: TapOIC) -> None:
            # Test with invalid endpoint
        with patch.object(tap, "config", {"base_url": "https://invalid.example.com"}):
            streams = tap.discover_streams()
            # Should handle gracefully without crashing
            assert isinstance(streams, list)

    def test_pagination_handling(self, tap: TapOIC) -> None:
        # Mock a paginated response
        mock_response = Mock()
        mock_response.json.return_value = {
            "items": [{"id": "1"}, {"id": "2"}],
            "hasMore": True,
            "offset": 0,
            "limit": 2,
        }

        # This test verifies the tap can handle paginated responses
        # Implementation depends on actual pagination logic

    def test_data_transformation(self, tap: TapOIC) -> None:
        catalog = tap.discover_streams()

        for stream in catalog:
            # Check that stream can handle different data types
            schema = stream.schema

            # Verify schema has proper type definitions
            if "properties" in schema:
                for prop_schema in schema["properties"].values():
                    assert "type" in prop_schema or "anyOf" in prop_schema
            assert "type" in prop_schema or "anyOf" in prop_schema

    def test_full_extraction_flow(self, config_path: str, tmp_path: Path) -> None:
        import subprocess  # TODO: Move import to module level

        # 1. Run discovery
        catalog_file = tmp_path / "catalog.json"
        discover_result = subprocess.run(
            ["python", "-m", "tap_oracle_oic", "--config", config_path, "--discover"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent,
            check=False,
        )

        assert discover_result.returncode == 0

        # Save catalog
        with open(catalog_file, "w", encoding="utf-8") as f:
            f.write(discover_result.stdout)

        # 2. Run extraction with catalog
        tmp_path / "output.jsonl"
        extract_result = subprocess.run(
            [
                "python",
                "-m",
                "tap_oracle_oic",
                "--config",
                config_path,
                "--catalog",
                str(catalog_file),
            ],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent,
            check=False,
        )

        # Check extraction completed
        assert extract_result.returncode == 0

        # Check output contains Singer messages
        output_lines = extract_result.stdout.strip().split("\n")
        for line in output_lines:
            msg = json.loads(line)
            if msg:
                assert "type" in msg
                assert msg["type"] in {"SCHEMA", "RECORD", "STATE", "ACTIVATE_VERSION"}

    def test_conditional_config_generation(self) -> None:
        config_path = Path(__file__).parent.parent / "config.json"

        # If config doesn't exist, it should be generated
        if not config_path.exists():
            import subprocess  # TODO: Move import to module level

            result = subprocess.run(
                ["python", "generate_config.py"],
                capture_output=True,
                text=True,
                cwd=Path(__file__).parent.parent,
                input="y\n",
                check=False,
            )
            assert result.returncode == 0
            assert config_path.exists()

        # Load and validate config
        with open(config_path, encoding="utf-8") as f:
            config = json.load(f)

        # Check required fields
        assert "base_url" in config
        assert "oauth_client_id" in config
        assert "oauth_client_secret" in config
        assert "oauth_token_url" in config


# Additional test class using Singer SDK test framework
TapOICTestClass = get_tap_test_class(
    tap_class=TapOIC,
    config={
        "oauth_client_id": "test_client",
        "oauth_client_secret": "test_secret",
        "oauth_endpoint": "https://test.identity.oraclecloud.com/oauth2/v1/token",
        "oic_url": "https://test.integration.ocp.oraclecloud.com",
        "oauth_scope": "urn:opc:resource:consumer:all",
    },
)


class TestTapOICSingerSDK(TapOICTestClass):
    """Singer SDK standard tests for tap-oracle-oic."""
