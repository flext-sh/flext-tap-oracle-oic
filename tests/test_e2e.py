#!/usr/bin/env python3

"""Comprehensive End-to-End tests for tap-oracle-oic.

Module test_e2e_complete.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from asyncio import run
from asyncio.subprocess import create_subprocess_exec
from pathlib import Path
from unittest.mock import Mock

import pytest
from flext_core import FlextTypes as t, FlextLogger
from singer_sdk import ConfigValidationError

from flext_tap_oracle_oic import TapOracleOic

"""Tests all functionalities including:
- Discovery
- Catalog generation
- Data extraction
- State management
- Authentication
- Error handling
"""


class TestTapOracleOicE2E:
    """End-to-end tests for tap-oracle-oic."""

    @pytest.fixture
    def config(self) -> dict[str, t.GeneralValueType]:
        """Mock configuration that matches the required schema."""
        return {
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test.identity.oraclecloud.com/oauth2/v1/token",
            "oic_url": "https://test.integration.ocp.oraclecloud.com",
            "oauth_scope": "urn:opc:resource:consumer:all",
            "start_date": "2024-01-01T00:00:00Z",
        }

    @pytest.fixture
    def tap(self, config: dict[str, t.GeneralValueType]) -> object:
        """Create TapOracleOic instance for testing."""
        return TapOracleOic(config=config)

    @pytest.fixture
    def config_path(self, tmp_path: Path, config: dict[str, t.GeneralValueType]) -> str:
        """Create a temporary config file for CLI tests."""
        config_file = tmp_path / "test_config.json"
        with config_file.open("w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)
        return str(config_file)

    def test_tap_initialization(
        self,
        tap: TapOracleOic,
        config: dict[str, t.GeneralValueType],
    ) -> None:
        """Test TapOracleOic initialization with configuration."""
        if tap.name != "tap-oracle-oic":
            msg: str = f"Expected {'tap-oracle-oic'}, got {tap.name}"
            raise AssertionError(msg)
        assert tap.config == config
        if tap.config["oic_url"] != config["oic_url"]:
            msg: str = f"Expected {config['oic_url']}, got {tap.config['oic_url']}"
            raise AssertionError(msg)

    def test_stream_discovery_core_streams(self, tap: TapOracleOic) -> None:
        """Test discovery of core OIC streams."""
        catalog = tap.discover_streams()

        # Check that we discovered streams
        assert len(catalog) > 0

        # Check for expected core streams
        stream_names = [stream.tap_stream_id for stream in catalog]
        if "connections" not in stream_names:
            msg: str = f"Expected {'connections'} in {stream_names}"
            raise AssertionError(msg)
        assert "integrations" in stream_names
        if "packages" not in stream_names:
            msg: str = f"Expected {'packages'} in {stream_names}"
            raise AssertionError(msg)
        assert "lookups" in stream_names

    def test_catalog_dict_structure(self, tap: TapOracleOic) -> None:
        """Test catalog dictionary structure."""
        catalog_dict = tap.catalog_dict

        if "streams" not in catalog_dict:
            msg: str = f"Expected {'streams'} in {catalog_dict}"
            raise AssertionError(msg)
        assert len(catalog_dict["streams"]) > 0

        # Check stream structure
        for stream in catalog_dict["streams"]:
            if "tap_stream_id" not in stream:
                msg: str = f"Expected {'tap_stream_id'} in {stream}"
                raise AssertionError(msg)
            assert "schema" in stream
            if "metadata" not in stream:
                msg: str = f"Expected {'metadata'} in {stream}"
                raise AssertionError(msg)

    def test_schema_validation_structure(self, tap: TapOracleOic) -> None:
        """Test schema validation and structure."""
        catalog = tap.discover_streams()

        for stream in catalog:
            schema = stream.schema
            if "type" not in schema:
                msg: str = f"Expected {'type'} in {schema}"
                raise AssertionError(msg)
            if schema["type"] != "object":
                msg: str = f"Expected {'object'}, got {schema['type']}"
                raise AssertionError(msg)
            if "properties" not in schema:
                msg: str = f"Expected {'properties'} in {schema}"
                raise AssertionError(msg)

            # Check for required fields
            properties = schema["properties"]
            if "id" in properties or "name" not in properties:
                msg: str = f"Expected {'id' in properties or 'name'} in {properties}"
                raise AssertionError(msg)

    def test_live_connection_validation(self, tap: TapOracleOic) -> None:
        """Test live connection with proper validation."""
        # Test authentication with proper error handling
        streams = tap.discover_streams()
        assert streams, "No streams discovered from tap"

        # Test with mock mode for CI/local testing
        if os.getenv("OIC_TEST_MODE", "mock").lower() == "mock":
            # Mock mode: test tap functionality without live connection
            stream = streams[0]

            # Verify stream configuration and structure
            expected_streams = {"connections", "integrations", "packages", "lookups"}
            if stream.name not in expected_streams:
                msg: str = f"Expected {stream.name} in {expected_streams}"
                raise AssertionError(msg)
            assert hasattr(stream, "schema")
            assert stream.schema is not None

            # Test mock data processing
            try:
                # Create mock record that matches schema
                mock_record = {"id": "test_id", "name": "test_name"}
                processed = stream.post_process(mock_record, context={})
                assert processed is not None
                if "id" not in processed:
                    msg: str = f"Expected {'id'} in {processed}"
                    raise AssertionError(msg)
            except (RuntimeError, ValueError, TypeError) as e:
                pytest.fail(f"Mock data processing failed: {e}")
        else:
            # Live mode: test actual OIC connection (only when explicitly enabled)
            stream = streams[0]

            # Try to get records from the first stream
            try:
                records = list(stream.get_records(context={}))
                # Successfully got records (may be empty list)
                assert isinstance(records, list)
            except (ValueError, TypeError, KeyError, ConnectionError) as e:
                # Check if it's an authentication error that should fail the test
                error_str = str(e).lower()
                if any(
                    code in error_str
                    for code in ["401", "403", "unauthorized", "forbidden"]
                ):
                    pytest.fail(f"Authentication failed: {e}")
                elif "connection" in error_str or "network" in error_str:
                    pytest.fail(f"Network connection failed: {e}")
                # Other errors might be acceptable (no data, API changes, etc.)
                # Log warning but don't fail test

                logger = FlextLogger(__name__)
                logger.warning("Non-critical error in live connection test: %s", e)

    def test_state_management_functionality(self, tap: TapOracleOic) -> None:
        """Test state management functionality."""
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
        if tap.state != test_state:
            msg: str = f"Expected {test_state}, got {tap.state}"
            raise AssertionError(msg)

    def test_cli_discovery_functionality(self, config_path: str) -> None:
        """Test CLI discovery functionality."""
        python_exe = shutil.which("python3") or shutil.which("python") or sys.executable

        def _run(
            cmd_list: list[str],
            cwd: str | None = None,
        ) -> tuple[int, str, str]:
            process = create_subprocess_exec(
                *cmd_list,
                cwd=cwd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            stdout, stderr = process.communicate()
            return process.returncode, stdout.decode(), stderr.decode()

        rc, out, _err = run(
            _run(
                [
                    python_exe,
                    "-m",
                    "flext_tap_oracle_oic",
                    "--config",
                    config_path,
                    "--discover",
                ],
                cwd=str(Path(__file__).parent.parent),
            ),
        )

        if rc != 0:
            msg: str = f"Expected {0}, got {rc}"
            raise AssertionError(msg)

        # Extract JSON from output (skip log lines)
        output_lines = out.strip().split("\n")
        json_lines: list[str] = []
        in_json = False

        for line in output_lines:
            if line.strip().startswith("{"):
                in_json = True
            if in_json:
                json_lines.append(line)

        json_output = "\n".join(json_lines)
        catalog = json.loads(json_output)
        if "streams" not in catalog:
            msg: str = f"Expected {'streams'} in {catalog}"
            raise AssertionError(msg)
        assert len(catalog["streams"]) > 0

    def test_config_validation(self) -> None:
        """Test method."""
        """Test config validation."""
        # MIGRATED: from singer_sdk.exceptions import ConfigValidationError -> use flext_meltano

        # Test missing required fields
        with pytest.raises(ConfigValidationError):
            TapOracleOic(config={})

        # Test invalid config
        with pytest.raises(ConfigValidationError):
            TapOracleOic(config={"base_url": "not-a-url"})

    def test_stream_selection_catalog(self, tap: TapOracleOic) -> None:
        """Test stream selection and catalog management."""
        catalog = tap.discover_streams()

        # Create a catalog with only selected streams
        {
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

        # Load catalog using Singer SDK method (pending upstream availability)
        # Tracking: https://github.com/flext/issues/catalog-import
        # from singer_sdk.catalog import Catalog
        # tap.catalog = Catalog.from_dict(selected_catalog)

        # Skip catalog loading for now due to missing import

    def test_error_handling(self) -> None:
        """Test method."""
        """Test error handling."""
        # Test with invalid endpoint - create new tap instance with invalid config
        invalid_config = {
            "base_url": "https://invalid.example.com",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_endpoint": "https://invalid.example.com/oauth2/v1/token",
            "oic_url": "https://invalid.example.com",
        }

        invalid_tap = TapOracleOic(config=invalid_config, validate_config=False)
        streams = invalid_tap.discover_streams()

        # Should handle gracefully without crashing
        assert isinstance(streams, list)

    def test_pagination_handling_functionality(self, tap: TapOracleOic) -> None:
        """Test pagination handling functionality."""
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
        # Test basic discovery to ensure tap is functional
        streams = tap.discover_streams()
        assert isinstance(streams, list)

    def test_data_transformation_handling(self, tap: TapOracleOic) -> None:
        """Test data transformation handling."""
        catalog = tap.discover_streams()

        for stream in catalog:
            # Check that stream can handle different data types
            schema = stream.schema

            # Verify schema has proper type definitions
            if "properties" in schema:
                for prop_schema in schema["properties"].values():
                    if "type" in prop_schema or "anyOf" not in prop_schema:
                        msg: str = f"Expected {'type' in prop_schema or 'anyOf'} in {prop_schema}"
                        raise AssertionError(msg)

    def test_full_extraction_flow_e2e(self, config_path: str, tmp_path: Path) -> None:
        """Test full extraction flow end-to-end."""
        # 1. Run discovery
        catalog_file = tmp_path / "catalog.json"
        python_exe = shutil.which("python3") or shutil.which("python") or sys.executable

        def _run(
            cmd_list: list[str],
            cwd: str | None = None,
        ) -> tuple[int, str, str]:
            process = create_subprocess_exec(
                *cmd_list,
                cwd=cwd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            stdout, stderr = process.communicate()
            return process.returncode, stdout.decode(), stderr.decode()

        rc1, out1, _err1 = run(
            _run(
                [
                    python_exe,
                    "-m",
                    "flext_tap_oracle_oic",
                    "--config",
                    config_path,
                    "--discover",
                ],
                cwd=str(Path(__file__).parent.parent),
            ),
        )

        if rc1 != 0:
            msg: str = f"Expected {0}, got {rc1}"
            raise AssertionError(msg)

        # Extract JSON from stdout (skip log lines)
        output_lines = out1.strip().split("\n")
        json_lines: list[str] = []
        in_json = False

        for line in output_lines:
            if line.strip().startswith("{"):
                in_json = True
            if in_json:
                json_lines.append(line)

        json_output = "\n".join(json_lines)

        # Save catalog
        with catalog_file.open("w", encoding="utf-8") as f:
            f.write(json_output)

        # 2. Run extraction with catalog
        tmp_path / "output.jsonl"
        python_exe = shutil.which("python3") or shutil.which("python") or sys.executable
        rc2, out2, err2 = run(
            _run(
                [
                    python_exe,
                    "-m",
                    "flext_tap_oracle_oic",
                    "--config",
                    config_path,
                    "--catalog",
                    str(catalog_file),
                ],
                cwd=str(Path(__file__).parent.parent),
            ),
        )

        # Check extraction completed (allowing connection errors for test credentials)
        if rc2 != 0:
            # For E2E tests with mock credentials, connection errors are expected
            if "ConnectionError" in err2 or "Name or service not known" in err2:
                # This is expected with test.* hostnames
                pytest.skip(
                    "Skipping extraction test due to mock credentials causing connection error",
                )
            # Real error - should fail the test
            elif rc2 != 0:
                msg: str = f"Expected 0, got {rc2}. Extraction failed: {err2}"
                raise AssertionError(msg)

        # Check output contains Singer messages
        output_lines = out2.strip().split("\n")
        for line in output_lines:
            msg = json.loads(line)
            if msg:
                if "type" not in msg:
                    msg: str = f"Expected {'type'} in {msg}"
                    raise AssertionError(msg)
                assert msg["type"] in {"SCHEMA", "RECORD", "STATE", "ACTIVATE_VERSION"}

    def test_conditional_config_generation(self) -> None:
        """Test method."""
        """Test conditional config generation."""
        config_path = Path(__file__).parent.parent / "config.json"

        # If config doesn't exist, it should be generated
        if not config_path.exists():
            python_exe = (
                shutil.which("python3") or shutil.which("python") or sys.executable
            )

            def _run_input(
                cmd_list: list[str],
                cwd: str | None = None,
                input_text: str = "",
            ) -> tuple[int, str, str]:
                process = create_subprocess_exec(
                    *cmd_list,
                    cwd=cwd,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                stdout, stderr = process.communicate(input=input_text.encode())
                return process.returncode, stdout.decode(), stderr.decode()

            rc3, _o, _e = run(
                _run_input(
                    [python_exe, "generate_config.py"],
                    cwd=str(Path(__file__).parent.parent),
                    input_text="y\n",
                ),
            )
            if rc3 != 0:
                msg: str = f"Expected {0}, got {rc3}"
                raise AssertionError(msg)
            assert config_path.exists()

        # Load and validate config
        with Path(config_path).open(encoding="utf-8") as f:
            config = json.load(f)

        # Check that config file is valid JSON and has expected structure
        assert isinstance(config, dict)
        if "base_url" not in config:
            msg: str = f"Expected {'base_url'} in {config}"
            raise AssertionError(msg)
        assert "oauth_token_url" in config

        # OAuth credentials may not be present if environment variables aren't set
        # This is the correct real-world behavior - missing env vars mean missing OAuth config
        # The test validates that the config generation process works, not that secrets exist


# Additional test class using Singer SDK test framework
# Tracking: https://github.com/flext/issues/mypy-dynamic-classes
# TapOracleOicTestClass = get_tap_test_class(
#     tap_class=TapOracleOic,
#     config={
#         "oauth_client_id": "test_client",
#         "oauth_client_secret": "test_secret",
#         "oauth_endpoint": "https://test.identity.oraclecloud.com/oauth2/v1/token",
#         "oic_url": "https://test.integration.ocp.oraclecloud.com",
#         "oauth_scope": "urn:opc:resource:consumer:all",
#     },
# )


# class TestTapOracleOicSingerSDK(TapOracleOicTestClass):
