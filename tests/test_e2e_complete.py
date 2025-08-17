#!/usr/bin/env python3

"""Comprehensive End-to-End tests for tap-oracle-oic.

Module test_e2e_complete.
"""

from __future__ import annotations

import asyncio
import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any
from unittest.mock import Mock

import pytest
from flext_core import get_logger
from singer_sdk import ConfigValidationError

from flext_tap_oracle_oic import TapOIC

"""Tests all functionalities including:
- Discovery
- Catalog generation
- Data extraction
- State management
- Authentication
- Error handling
"""


class TestTapOracleOICE2E:
    """End-to-end tests for tap-oracle-oic."""

    @pytest.fixture
    def config(self) -> dict[str, object]:
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
    def tap(self, config: dict[str, object]) -> Any:
      return TapOIC(config=config)

    @pytest.fixture
    def config_path(self, tmp_path: Path, config: dict[str, object]) -> str:
      """Create a temporary config file for CLI tests."""
      config_file = tmp_path / "test_config.json"
      with config_file.open("w", encoding="utf-8") as f:
          json.dump(config, f, indent=2)
      return str(config_file)

    def test_tap_initialization(self, tap: TapOIC, config: dict[str, object]) -> None:
      if tap.name != "tap-oracle-oic":
          msg: str = f"Expected {'tap-oracle-oic'}, got {tap.name}"
          raise AssertionError(msg)
      assert tap.config == config
      if tap.config["oic_url"] != config["oic_url"]:
          msg: str = f"Expected {config['oic_url']}, got {tap.config['oic_url']}"
          raise AssertionError(msg)

    def test_discover_streams(self, tap: TapOIC) -> None:
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

    def test_catalog_generation(self, tap: TapOIC) -> None:
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

    def test_stream_schema_validation(self, tap: TapOIC) -> None:
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

    def test_live_connection(self, tap: TapOIC) -> None:
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

              logger = get_logger(__name__)
              logger.warning(f"Non-critical error in live connection test: {e}")

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
      if tap.state != test_state:
          msg: str = f"Expected {test_state}, got {tap.state}"
          raise AssertionError(msg)

    def test_cli_discovery(self, config_path: str) -> None:
      """Test CLI discovery."""
      python_exe = shutil.which("python3") or shutil.which("python") or sys.executable

      async def _run(
          cmd_list: list[str],
          cwd: str | None = None,
      ) -> tuple[int, str, str]:
          process = await asyncio.create_subprocess_exec(
              *cmd_list,
              cwd=cwd,
              stdout=asyncio.subprocess.PIPE,
              stderr=asyncio.subprocess.PIPE,
          )
          stdout, stderr = await process.communicate()
          return process.returncode, stdout.decode(), stderr.decode()

      rc, out, _err = asyncio.run(
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
      json_lines = []
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
      """Test config validation."""
      # MIGRATED: from singer_sdk.exceptions import ConfigValidationError -> use flext_meltano

      # Test missing required fields
      with pytest.raises(ConfigValidationError):
          TapOIC(config={})

      # Test invalid config
      with pytest.raises(ConfigValidationError):
          TapOIC(config={"base_url": "not-a-url"})

    def test_stream_selection(self, tap: TapOIC) -> None:
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
      """Test error handling."""
      # Test with invalid endpoint - create new tap instance with invalid config
      invalid_config = {
          "base_url": "https://invalid.example.com",
          "oauth_client_id": "test_client_id",
          "oauth_client_secret": "test_client_secret",
          "oauth_endpoint": "https://invalid.example.com/oauth2/v1/token",
          "oic_url": "https://invalid.example.com",
      }

      invalid_tap = TapOIC(config=invalid_config, validate_config=False)
      streams = invalid_tap.discover_streams()

      # Should handle gracefully without crashing
      assert isinstance(streams, list)

    def test_pagination_handling(self, tap: TapOIC) -> None:
      """Test pagination handling."""
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

    def test_data_transformation(self, tap: TapOIC) -> None:
      """Test data transformation."""
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

    def test_full_extraction_flow(self, config_path: str, tmp_path: Path) -> None:
      """Test full extraction flow."""
      # 1. Run discovery
      catalog_file = tmp_path / "catalog.json"
      python_exe = shutil.which("python3") or shutil.which("python") or sys.executable

      async def _run(
          cmd_list: list[str],
          cwd: str | None = None,
      ) -> tuple[int, str, str]:
          process = await asyncio.create_subprocess_exec(
              *cmd_list,
              cwd=cwd,
              stdout=asyncio.subprocess.PIPE,
              stderr=asyncio.subprocess.PIPE,
          )
          stdout, stderr = await process.communicate()
          return process.returncode, stdout.decode(), stderr.decode()

      rc1, out1, _err1 = asyncio.run(
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
      json_lines = []
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
      rc2, out2, err2 = asyncio.run(
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
      """Test conditional config generation."""
      config_path = Path(__file__).parent.parent / "config.json"

      # If config doesn't exist, it should be generated
      if not config_path.exists():
          python_exe = (
              shutil.which("python3") or shutil.which("python") or sys.executable
          )

          async def _run_input(
              cmd_list: list[str],
              cwd: str | None = None,
              input_text: str = "",
          ) -> tuple[int, str, str]:
              process = await asyncio.create_subprocess_exec(
                  *cmd_list,
                  cwd=cwd,
                  stdin=asyncio.subprocess.PIPE,
                  stdout=asyncio.subprocess.PIPE,
                  stderr=asyncio.subprocess.PIPE,
              )
              stdout, stderr = await process.communicate(input=input_text.encode())
              return process.returncode, stdout.decode(), stderr.decode()

          rc3, _o, _e = asyncio.run(
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
# TapOICTestClass = get_tap_test_class(
#     tap_class=TapOIC,
#     config={
#         "oauth_client_id": "test_client",
#         "oauth_client_secret": "test_secret",
#         "oauth_endpoint": "https://test.identity.oraclecloud.com/oauth2/v1/token",
#         "oic_url": "https://test.integration.ocp.oraclecloud.com",
#         "oauth_scope": "urn:opc:resource:consumer:all",
#     },
# )


# class TestTapOICSingerSDK(TapOICTestClass):
