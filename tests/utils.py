"""Professional test utilities for tap-oic.

This module provides utility functions and helpers for testing following
enterprise testing best practices.
"""

from __future__ import annotations

import json
import os
import signal
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, NoReturn

import pytest
import requests
from packaging import version

if TYPE_CHECKING:
    from collections.abc import Callable, Generator
    from pathlib import Path


class TestDataBuilder:
    """Builder pattern for creating test data consistently."""

    @staticmethod
    def integration_record(
        integration_id: str = "TEST_INTEGRATION_001",
        name: str = "Test Integration",
        status: str = "ACTIVE",
        time_updated: str = "2024-01-15T10:30:00Z",
        **kwargs: object,
    ) -> dict[str, object]:
        record = {
            "id": integration_id,
            "name": name,
            "status": status,
            "timeUpdated": time_updated,
            "description": f"Test integration: {name}",
            "version": "0.9.0",
            "identifier": integration_id.lower(),
        }
        record.update(kwargs)
        return record

    @staticmethod
    def connection_record(
        connection_id: str = "TEST_CONNECTION_001",
        name: str = "Test Connection",
        status: str = "ACTIVE",
        time_updated: str = "2024-01-15T10:30:00Z",
        connection_type: str = "REST",
        **kwargs: object,
    ) -> dict[str, object]:
        record = {
            "id": connection_id,
            "name": name,
            "status": status,
            "timeUpdated": time_updated,
            "connectionType": connection_type,
            "description": f"Test connection: {name}",
            "identifier": connection_id.lower(),
        }
        record.update(kwargs)
        return record

    @staticmethod
    def package_record(
        package_id: str = "TEST_PACKAGE_001",
        name: str = "Test Package",
        status: str = "ACTIVE",
        time_updated: str = "2024-01-15T10:30:00Z",
        version: str = "0.9.0",
        **kwargs: object,
    ) -> dict[str, object]:
        record = {
            "id": package_id,
            "name": name,
            "status": status,
            "timeUpdated": time_updated,
            "version": version,
            "description": f"Test package: {name}",
            "identifier": package_id.lower(),
        }
        record.update(kwargs)
        return record

    @staticmethod
    def monitoring_record(
        instance_id: str = "TEST_INSTANCE_001",
        integration_id: str = "TEST_INTEGRATION_001",
        status: str = "SUCCEEDED",
        start_time: str = "2024-01-15T10:30:00Z",
        end_time: str = "2024-01-15T10:35:00Z",
        **kwargs: object,
    ) -> dict[str, object]:
        record = {
            "instanceId": instance_id,
            "integrationId": integration_id,
            "status": status,
            "startTime": start_time,
            "endTime": end_time,
            "duration": 300000,  # 5 minutes in milliseconds
            "recordsProcessed": 100,
        }
        record.update(kwargs)
        return record

    @staticmethod
    def singer_record(
        stream: str,
        record_data: dict[str, object],
        time_extracted: str | None = None,
    ) -> dict[str, object]:
        if time_extracted is None:
            time_extracted = "2024-01-15T10:35:00Z"

        return {
            "type": "RECORD",
            "stream": stream,
            "record": record_data,
            "time_extracted": time_extracted,
        }

    @staticmethod
    def singer_schema(
        stream: str,
        properties: dict[str, object],
        key_properties: list[str] | None = None,
    ) -> dict[str, object]:
        if key_properties is None:
            key_properties = ["id"]

        return {
            "type": "SCHEMA",
            "stream": stream,
            "schema": {
                "type": "object",
                "properties": properties,
            },
            "key_properties": key_properties,
        }


class TestValidator:
    """Validator utilities for test assertions."""

    @staticmethod
    def validate_tap_instance(tap_instance: Any) -> None:
        assert hasattr(tap_instance, "name")
        assert hasattr(tap_instance, "config")
        assert hasattr(tap_instance, "catalog")
        assert hasattr(tap_instance, "discover_streams")
        if tap_instance.name != "tap-oracle-oic":
            msg: str = f"Expected {'tap-oracle-oic'}, got {tap_instance.name}"
            raise AssertionError(msg)

    @staticmethod
    def validate_stream_schema(stream: Any) -> None:
        assert hasattr(stream, "schema")
        assert stream.schema is not None
        assert isinstance(stream.schema, dict)
        if "type" not in stream.schema:
            msg: str = f"Expected {'type'} in {stream.schema}"
            raise AssertionError(msg)
        if stream.schema["type"] != "object":
            msg: str = f"Expected {'object'}, got {stream.schema['type']}"
            raise AssertionError(msg)
        if "properties" not in stream.schema:
            msg: str = f"Expected {'properties'} in {stream.schema}"
            raise AssertionError(msg)
        assert len(stream.schema["properties"]) > 0

    @staticmethod
    def validate_stream_metadata(stream: Any) -> None:
        assert hasattr(stream, "primary_keys")
        assert stream.primary_keys is not None
        assert len(stream.primary_keys) > 0

        # Ensure primary keys exist in schema
        properties = stream.schema.get("properties", {})
        for key in stream.primary_keys:
            if key not in properties:
                msg: str = f"Primary key {key} missing from schema"
                raise AssertionError(msg)

    @staticmethod
    def validate_singer_record(record: dict[str, object]) -> None:
        if "type" not in record:
            msg: str = f"Expected {'type'} in {record}"
            raise AssertionError(msg)
        if record["type"] != "RECORD":
            msg: str = f"Expected {'RECORD'}, got {record['type']}"
            raise AssertionError(msg)
        if "stream" not in record:
            msg: str = f"Expected {'stream'} in {record}"
            raise AssertionError(msg)
        assert "record" in record
        if "time_extracted" not in record:
            msg: str = f"Expected {'time_extracted'} in {record}"
            raise AssertionError(msg)
        assert isinstance(record["record"], dict)

    @staticmethod
    def validate_config_schema(config_schema: dict[str, object]) -> None:
        if "properties" not in config_schema:
            msg: str = f"Expected {'properties'} in {config_schema}"
            raise AssertionError(msg)
        properties = config_schema["properties"]

        # Required fields
        required_fields = ["base_url", "auth_method"]
        for field in required_fields:
            if field not in properties:
                msg: str = f"Required field {field} missing from properties"
                raise AssertionError(msg)

        # OAuth2 fields
        oauth2_fields = ["oauth_client_id", "oauth_client_secret", "oauth_token_url"]
        for field in oauth2_fields:
            if field not in properties:
                msg: str = f"OAuth2 field {field} missing from properties"
                raise AssertionError(msg)

    @staticmethod
    def validate_performance_metrics(
        metrics: dict[str, object],
        max_duration: float = 5.0,
        max_memory_growth: int = 100 * 1024 * 1024,  # 100MB
    ) -> None:
        if "duration" in metrics:
            assert metrics["duration"] < max_duration, (
                f"Duration {metrics['duration']} exceeds {max_duration}s"
            )

        if "memory_growth" in metrics:
            assert metrics["memory_growth"] < max_memory_growth, (
                f"Memory growth {metrics['memory_growth']} exceeds {max_memory_growth} bytes"
            )


class MockAPIServer:
    """Mock API server for testing HTTP interactions."""

    def __init__(self) -> None:
        self.requests_mock: Any = None
        self.base_url = "https://test-oic.integration.ocp.oraclecloud.com"
        self.token_url = "https://test-idcs.identity.oraclecloud.com/oauth2/v1/token"

    def setup_oauth2_mock(self, token: str = "mock-token-12345") -> None:
        if self.requests_mock is not None:
            self.requests_mock.post(
                self.token_url,
                json={
                    "access_token": token,
                    "token_type": "Bearer",
                    "expires_in": 3600,
                    "scope": "urn:opc:resource:consumer:all",
                },
                status_code=200,
            )

    def setup_integrations_mock(
        self,
        records: list[dict[str, object]] | None = None,
    ) -> None:
        if records is None:
            records = [TestDataBuilder.integration_record()]

        if self.requests_mock is not None:
            self.requests_mock.get(
                f"{self.base_url}/ic/api/integration/v1/integrations",
                json={"items": records},
                status_code=200,
            )

    def setup_connections_mock(
        self,
        records: list[dict[str, object]] | None = None,
    ) -> None:
        if records is None:
            records = [TestDataBuilder.connection_record()]

        if self.requests_mock is not None:
            self.requests_mock.get(
                f"{self.base_url}/ic/api/integration/v1/connections",
                json={"items": records},
                status_code=200,
            )

    def setup_error_response(
        self,
        endpoint: str,
        status_code: int = 500,
        error_message: str = "Internal Server Error",
    ) -> None:
        if self.requests_mock is not None:
            self.requests_mock.get(
                f"{self.base_url}{endpoint}",
                json={"error": error_message},
                status_code=status_code,
            )

    @contextmanager
    def mock_context(self, requests_mock_instance: Any) -> object:
        self.requests_mock = requests_mock_instance
        try:
            yield self
        finally:
            self.requests_mock = None


class PerformanceMeasurer:
    """Utility for measuring performance metrics."""

    def __init__(self) -> None:
        self.start_time: float | None = None
        self.end_time: float | None = None
        self.measurements: list[dict[str, object]] = []

    @contextmanager
    def measure_duration(self) -> Generator[dict[str, object]]:
        self.start_time = time.time()
        metrics = {"start_time": self.start_time}

        try:
            yield metrics
        finally:
            self.end_time = time.time()
            metrics["end_time"] = self.end_time
            if self.start_time is not None:
                metrics["duration"] = self.end_time - self.start_time
            self.measurements.append(metrics)

    def get_average_duration(self) -> float:
        if not self.measurements:
            return 0.0
        return float(
            sum(m["duration"] for m in self.measurements) / len(self.measurements),
        )

    def get_max_duration(self) -> float:
        if not self.measurements:
            return 0.0
        return float(max(m["duration"] for m in self.measurements))


class TestConfigGenerator:
    """Generate test configurations for various scenarios."""

    @staticmethod
    def minimal_oauth2_config() -> dict[str, object]:
        return {
            "base_url": "https://test-oic.integration.ocp.oraclecloud.com",
            "auth_method": "oauth2",
            "oauth_client_id": "test-client",
            "oauth_client_secret": "test-secret",
            "oauth_token_url": "https://test-idcs.identity.oraclecloud.com/oauth2/v1/token",
        }

    @staticmethod
    def full_oauth2_config() -> dict[str, object]:
        return {
            "base_url": "https://test-oic.integration.ocp.oraclecloud.com",
            "auth_method": "oauth2",
            "oauth_client_id": "test-client-id",
            "oauth_client_secret": "test-client-secret",
            "oauth_token_url": "https://test-idcs.identity.oraclecloud.com/oauth2/v1/token",
            "oauth_client_aud": "https://test-oic.integration.ocp.oraclecloud.com",
            "oauth_scope": "urn:opc:resource:consumer:all",
            "request_timeout": 30,
            "max_retries": 3,
            "page_size": 100,
            "include_inactive": True,
            "include_monitoring": True,
            "include_extended": True,
        }

    @staticmethod
    def production_oauth2_config() -> dict[str, object]:
        return {
            "base_url": "https://production-oic.integration.ocp.oraclecloud.com",
            "auth_method": "oauth2",
            "oauth_client_id": "prod-client-id",
            "oauth_client_secret": "prod-client-secret",
            "oauth_token_url": "https://production-idcs.identity.oraclecloud.com/oauth2/v1/token",
            "oauth_client_aud": "https://production-oic.integration.ocp.oraclecloud.com",
            "oauth_scope": "urn:opc:resource:consumer:all",
            "request_timeout": 60,
            "max_retries": 3,
            "page_size": 500,
            "include_monitoring": True,
            "include_extended": True,
        }

    @staticmethod
    def invalid_configs() -> list[dict[str, object]]:
        return [
            # Empty base URL
            {
                "base_url": "",
                "auth_method": "oauth2",
                "oauth_client_id": "test",
                "oauth_client_secret": "test",
                "oauth_token_url": "https://test.com/token",
            },
            # Invalid auth method
            {
                "base_url": "https://test.com",
                "auth_method": "invalid_method",
                "oauth_client_id": "test",
                "oauth_client_secret": "test",
                "oauth_token_url": "https://test.com/token",
            },
            # Missing required OAuth2 fields
            {
                "base_url": "https://test.com",
                "auth_method": "oauth2",
            },
            # Invalid OAuth2 scope
            {
                "base_url": "https://test.com",
                "auth_method": "oauth2",
                "oauth_client_id": "test",
                "oauth_client_secret": "test",
                "oauth_token_url": "https://test.com/token",
                "oauth_scope": "invalid_scope",
            },
        ]


class TestFileManager:
    """Manage test files and temporary data."""

    def __init__(self, temp_dir: Path) -> None:
        self.temp_dir = temp_dir
        self.created_files: list[Path] = []

    def create_config_file(
        self,
        config: dict[str, object],
        filename: str = "test_config.json",
    ) -> Path:
        config_path = self.temp_dir / filename
        with config_path.open("w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)
        self.created_files.append(config_path)
        return config_path

    def create_catalog_file(
        self,
        catalog: dict[str, object],
        filename: str = "test_catalog.json",
    ) -> Path:
        catalog_path = self.temp_dir / filename
        with catalog_path.open("w", encoding="utf-8") as f:
            json.dump(catalog, f, indent=2)
        self.created_files.append(catalog_path)
        return catalog_path

    def create_records_file(
        self,
        records: list[dict[str, object]],
        filename: str = "test_records.jsonl",
    ) -> Path:
        records_path = self.temp_dir / filename
        with records_path.open("w", encoding="utf-8") as f:
            f.writelines(json.dumps(record) + "\n" for record in records)
        self.created_files.append(records_path)
        return records_path

    def cleanup(self) -> None:
        for file_path in self.created_files:
            if file_path.exists():
                file_path.unlink()
        self.created_files.clear()


def skip_if_no_internet() -> None:
    try:
        requests.get("https://www.google.com", timeout=5)
    except requests.RequestException:
        pytest.fail(
            "No internet connection available - Internet connectivity required for testing",
        )


def skip_if_no_production_config() -> None:
    required_vars = ["OIC_BASE_URL", "OIC_CLIENT_ID", "OIC_CLIENT_SECRET"]
    if not all(os.getenv(var) for var in required_vars):
        pytest.fail(
            "Production configuration not available - Required environment variables must be set for testing",
        )


def requires_python_version(min_version: str) -> object:
    def decorator(func: Any) -> object:
        if version.parse(
            f"{sys.version_info.major}.{sys.version_info.minor}",
        ) < version.parse(min_version):

            def test_fail(*args: object, **kwargs: object) -> None:
                pytest.fail(f"Requires Python {min_version} or higher")

            return test_fail
        return func

    return decorator


@contextmanager
def timeout_test(seconds: float) -> object:
    def timeout_handler(signum: int, frame: Any) -> NoReturn:
        msg: str = f"Test timed out after {seconds} seconds"
        raise TimeoutError(msg)

    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(int(seconds))

    try:
        yield
    finally:
        signal.alarm(0)


class ConcurrentTestRunner:
    """Utility for running tests concurrently."""

    def __init__(self, max_workers: int = 4) -> None:
        self.max_workers = max_workers
        self.results: list[dict[str, object]] = []

    def run_tests_parallel(self, test_functions: list[Callable[[], Any]]) -> list[Any]:
        self.results.clear()
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_test: dict[Any, Callable[[], Any]] = {
                executor.submit(test_func): test_func for test_func in test_functions
            }

        for future in as_completed(future_to_test):
            test_func = future_to_test[future]
            try:
                result = future.result()
                self.results.append(
                    {"test": test_func.__name__, "result": result, "success": True},
                )
            except (RuntimeError, ValueError, TypeError) as e:
                self.results.append(
                    {"test": test_func.__name__, "error": str(e), "success": False},
                )

        return self.results

    def get_success_rate(self) -> float:
        if not self.results:
            return 0.0
        successful = sum(1 for r in self.results if r["success"])
        return successful / len(self.results)


def assert_config_valid(config: dict[str, object]) -> None:
    if "base_url" not in config:
        msg = "base_url is required in config"
        raise AssertionError(msg)
    assert "auth_method" in config, "auth_method is required"
    if config["auth_method"] != "oauth2":
        msg: str = (
            f"OIC only supports oauth2 authentication, got {config['auth_method']}"
        )
        raise AssertionError(msg)

    if config["auth_method"] == "oauth2":
        oauth2_required = ["oauth_client_id", "oauth_client_secret", "oauth_token_url"]
        for field in oauth2_required:
            if field not in config:
                msg: str = f"OAuth2 field {field} is required in config"
                raise AssertionError(msg)
    else:
        msg = (
            f"Invalid auth_method: {config['auth_method']}. OIC only supports 'oauth2'"
        )
        raise ValueError(msg)


def assert_stream_quality(stream: Any) -> None:
    TestValidator.validate_stream_schema(stream)
    TestValidator.validate_stream_metadata(stream)

    # Additional quality checks
    assert hasattr(stream, "name")
    assert isinstance(stream.name, str)
    assert len(stream.name) > 0

    # Check for required schema fields
    properties = stream.schema.get("properties", {})
    if "id" not in properties:
        msg = "Stream schema must have 'id' field"
        raise AssertionError(msg)

    # Validate primary keys are meaningful
    for key in stream.primary_keys:
        if key not in properties:
            msg: str = f"Primary key {key} must exist in schema"
            raise AssertionError(msg)
        assert properties[key].get("type") in {
            "string",
            "integer",
        }, f"Primary key {key} must be string or integer"
