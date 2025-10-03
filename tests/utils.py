"""Test utilities for Oracle OIC tap.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import concurrent.futures
import time
from collections.abc import Callable, Generator
from contextlib import contextmanager
from pathlib import Path

from flext_core import FlextTypes


class TestDataBuilder:
    """Builder pattern for creating test data consistently."""

    @staticmethod
    def integration_record(
        integration_id: str = "TEST_INTEGRATION_001",
        name: str = "Test Integration",
        status: str = "ACTIVE",
        time_updated: str = "2024-01-15T10:30:00Z",
        **kwargs: object,
    ) -> FlextTypes.Dict:
        """Create a test integration record with default values."""
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
    ) -> FlextTypes.Dict:
        """Create a test connection record with default values."""
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
    ) -> FlextTypes.Dict:
        """Create a test package record with default values."""
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
    ) -> FlextTypes.Dict:
        """Create a test monitoring record with default values."""
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
        record_data: FlextTypes.Dict,
        time_extracted: str | None = None,
    ) -> FlextTypes.Dict:
        """Create a Singer record with the given stream and data."""
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
        properties: FlextTypes.Dict,
        key_properties: FlextTypes.StringList | None = None,
    ) -> FlextTypes.Dict:
        """Create a Singer schema with the given stream and properties."""
        if key_properties is None:
            key_properties = ["id"]
        return {
            "type": "SCHEMA",
            "stream": stream,
            "schema": {"properties": properties},
            "key_properties": key_properties,
        }


class TestValidator:
    """Validator utilities for test assertions."""

    @staticmethod
    def validate_tap_instance(tap_instance: object) -> None:
        """Validate tap instance has required attributes."""
        assert hasattr(tap_instance, "name")
        assert hasattr(tap_instance, "config")
        assert hasattr(tap_instance, "catalog")

    @staticmethod
    def validate_stream_schema(stream: object) -> None:
        """Validate stream schema structure."""
        assert hasattr(stream, "schema")
        assert stream.schema is not None
        assert isinstance(stream.schema, dict)
        assert "properties" in stream.schema
        assert isinstance(stream.schema["properties"], dict)
        assert len(stream.schema["properties"]) > 0

    @staticmethod
    def validate_stream_metadata(stream: object) -> None:
        """Validate stream metadata structure."""
        assert hasattr(stream, "primary_keys")
        assert stream.primary_keys is not None
        assert len(stream.primary_keys) > 0

    @staticmethod
    def validate_singer_record(record: FlextTypes.Dict) -> None:
        """Validate Singer record structure."""
        if "type" not in record:
            msg: str = f"Expected {'type'} in {record}"
            raise AssertionError(msg)
        assert record["type"] == "RECORD"
        assert "stream" in record
        assert "record" in record
        assert isinstance(record["record"], dict)

    @staticmethod
    def validate_config_schema(config_schema: FlextTypes.Dict) -> None:
        """Validate configuration schema structure."""
        if "properties" not in config_schema:
            msg: str = f"Expected {'properties'} in {config_schema}"
            raise AssertionError(msg)
        assert isinstance(config_schema["properties"], dict)
        assert len(config_schema["properties"]) > 0

    @staticmethod
    def validate_performance_metrics(
        metrics: FlextTypes.Dict,
        max_duration: float = 5.0,
    ) -> None:
        """Validate performance metrics meet requirements."""
        if "duration" in metrics:
            assert metrics["duration"] < max_duration, (
                f"Duration {metrics['duration']} exceeds {max_duration}s"
            )


class MockAPIServer:
    """Mock API server for testing HTTP interactions."""

    def __init__(self) -> None:
        """Initialize the mock API server."""
        self.requests_mock: object = None
        self.base_url = "https://test-oic.integration.ocp.oraclecloud.com"
        self.token_url = "https://test-idcs.identity.oraclecloud.com/oauth2/v1/token"

    def setup_oauth2_mock(self, token: str = "mock-token-12345") -> None:
        """Setup OAuth2 authentication mock."""
        if self.requests_mock is not None:
            self.requests_mock.post(
                self.token_url,
                json={"access_token": token, "token_type": "Bearer"},
                status_code=200,
            )

    def setup_integrations_mock(
        self,
        records: list[FlextTypes.Dict] | None = None,
    ) -> None:
        """Setup integrations endpoint mock."""
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
        records: list[FlextTypes.Dict] | None = None,
    ) -> None:
        """Setup connections endpoint mock."""
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
        """Setup error response mock."""
        if self.requests_mock is not None:
            self.requests_mock.get(
                f"{self.base_url}{endpoint}",
                json={"error": error_message},
                status_code=status_code,
            )

    @contextmanager
    def mock_context(self, requests_mock_instance: object) -> object:
        """Provide mock context for testing."""
        self.requests_mock = requests_mock_instance
        try:
            yield self
        finally:
            self.requests_mock = None


class PerformanceMeasurer:
    """Utility for measuring performance metrics."""

    def __init__(self) -> None:
        """Initialize the performance measurer."""
        self.start_time: float | None = None
        self.end_time: float | None = None
        self.measurements: list[FlextTypes.Dict] = []

    @contextmanager
    def measure_duration(self) -> Generator[FlextTypes.Dict]:
        """Measure execution duration."""
        self.start_time = time.time()
        metrics = {"start_time": self.start_time}
        try:
            yield metrics
        finally:
            self.end_time = time.time()
            metrics["duration"] = self.end_time - self.start_time
            self.measurements.append(metrics)

    def get_average_duration(self) -> float:
        """Get average duration from all measurements."""
        if not self.measurements:
            return 0.0
        return float(
            sum(m["duration"] for m in self.measurements) / len(self.measurements),
        )

    def get_max_duration(self) -> float:
        """Get maximum duration from all measurements."""
        if not self.measurements:
            return 0.0
        return float(max(m["duration"] for m in self.measurements))


class TestConfigGenerator:
    """Generate test configurations for various scenarios."""

    @staticmethod
    def minimal_oauth2_config() -> FlextTypes.Dict:
        """Create minimal OAuth2 configuration."""
        return {
            "base_url": "https://test-oic.integration.ocp.oraclecloud.com",
            "auth_method": "oauth2",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test-idcs.identity.oraclecloud.com/oauth2/v1/token",
        }

    @staticmethod
    def full_oauth2_config() -> FlextTypes.Dict:
        """Create full OAuth2 configuration."""
        return {
            "base_url": "https://test-oic.integration.ocp.oraclecloud.com",
            "auth_method": "oauth2",
            "oauth_client_id": "test_client_id",
            "oauth_client_secret": "test_client_secret",
            "oauth_token_url": "https://test-idcs.identity.oraclecloud.com/oauth2/v1/token",
            "oauth_scope": "urn:opc:idm:__myscopes__",
            "oauth_audience": "https://test-oic.integration.ocp.oraclecloud.com",
            "oauth_grant_type": "client_credentials",
            "oauth_timeout": 30,
            "oauth_retry_attempts": 3,
        }

    @staticmethod
    def production_oauth2_config() -> FlextTypes.Dict:
        """Create production OAuth2 configuration."""
        return {
            "base_url": "https://production-oic.integration.ocp.oraclecloud.com",
            "auth_method": "oauth2",
            "oauth_client_id": "prod_client_id",
            "oauth_client_secret": "prod_client_secret",
            "oauth_token_url": "https://prod-idcs.identity.oraclecloud.com/oauth2/v1/token",
            "oauth_scope": "urn:opc:idm:__myscopes__",
            "oauth_audience": "https://production-oic.integration.ocp.oraclecloud.com",
            "oauth_grant_type": "client_credentials",
            "oauth_timeout": 60,
            "oauth_retry_attempts": 5,
        }

    @staticmethod
    def invalid_configs() -> list[FlextTypes.Dict]:
        """Get invalid configuration examples."""
        return [
            # Empty base URL
            {
                "base_url": "",
                "auth_method": "oauth2",
                "oauth_client_id": "test_client_id",
                "oauth_client_secret": "test_client_secret",
            },
            # Missing client ID
            {
                "base_url": "https://test-oic.integration.ocp.oraclecloud.com",
                "auth_method": "oauth2",
                "oauth_client_secret": "test_client_secret",
            },
            # Missing client secret
            {
                "base_url": "https://test-oic.integration.ocp.oraclecloud.com",
                "auth_method": "oauth2",
                "oauth_client_id": "test_client_id",
            },
            # Invalid auth method
            {
                "base_url": "https://test-oic.integration.ocp.oraclecloud.com",
                "auth_method": "invalid_method",
                "oauth_client_id": "test_client_id",
                "oauth_client_secret": "test_client_secret",
            },
            # Invalid token URL
            {
                "base_url": "https://test-oic.integration.ocp.oraclecloud.com",
                "auth_method": "oauth2",
                "oauth_client_id": "test_client_id",
                "oauth_client_secret": "test_client_secret",
                "oauth_token_url": "invalid-url",
            },
        ]


class TestFileManager:
    """Manage test files and cleanup."""

    def __init__(self) -> None:
        """Initialize the test file manager."""
        self.created_files: list[Path] = []

    def create_config_file(
        self,
        config: FlextTypes.Dict,
        filename: str = "test_config.json",
    ) -> Path:
        """Create a test configuration file."""
        config_path = Path(filename)
        config_path.write_text(str(config), encoding="utf-8")
        self.created_files.append(config_path)
        return config_path

    def create_catalog_file(
        self,
        catalog: FlextTypes.Dict,
        filename: str = "test_catalog.json",
    ) -> Path:
        """Create a test catalog file."""
        catalog_path = Path(filename)
        catalog_path.write_text(str(catalog), encoding="utf-8")
        self.created_files.append(catalog_path)
        return catalog_path

    def create_records_file(
        self,
        records: list[FlextTypes.Dict],
        filename: str = "test_records.jsonl",
    ) -> Path:
        """Create a test records file."""
        records_path = Path(filename)
        with records_path.open("w", encoding="utf-8") as f:
            for record in records:
                f.write(str(record) + "\n")
        self.created_files.append(records_path)
        return records_path

    def cleanup(self) -> None:
        """Clean up created test files."""
        for file_path in self.created_files:
            if file_path.exists():
                file_path.unlink()
        self.created_files.clear()


class TestRunner:
    """Run tests in parallel and collect results."""

    def __init__(self) -> None:
        """Initialize the test runner."""
        self.results: list[FlextTypes.Dict] = []

    def run_tests_parallel(
        self,
        test_functions: list[Callable[[], object]],
    ) -> FlextTypes.List:
        """Run multiple test functions in parallel."""
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(test_func) for test_func in test_functions]
            for future in concurrent.futures.as_completed(futures):
                try:
                    result = future.result()
                    self.results.append({"status": "success", "result": result})
                except Exception as e:
                    self.results.append({"status": "error", "error": str(e)})

        return self.results

    def get_success_rate(self) -> float:
        """Get success rate of executed tests."""
        if not self.results:
            return 0.0
        success_count = sum(1 for r in self.results if r["status"] == "success")
        return float(success_count / len(self.results))
