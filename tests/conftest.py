"""Test configuration for flext-tap-oracle-oic.

Provides pytest fixtures and configuration for testing Oracle OIC tap functionality
using Singer protocol and real Oracle OIC API integration.
"""

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any
from unittest.mock import Mock

import pytest

if TYPE_CHECKING:
    from collections.abc import Generator, Iterator


# Test environment setup
@pytest.fixture(autouse=True)
def set_test_environment() -> Generator[None]:
    """Set test environment variables."""
    os.environ["FLEXT_ENV"] = "test"
    os.environ["FLEXT_LOG_LEVEL"] = "debug"
    os.environ["SINGER_SDK_LOG_LEVEL"] = "debug"
    os.environ["OIC_TEST_MODE"] = "true"
    yield
    # Cleanup
    os.environ.pop("FLEXT_ENV", None)
    os.environ.pop("FLEXT_LOG_LEVEL", None)
    os.environ.pop("SINGER_SDK_LOG_LEVEL", None)
    os.environ.pop("OIC_TEST_MODE", None)


# Oracle OIC configuration fixtures
@pytest.fixture
def basic_oic_config() -> dict[str, object]:
    """Basic Oracle OIC tap configuration."""
    return {
        "base_url": "https://oic-test.integration.ocp.oraclecloud.com",
        "api_version": "v1",
        "oauth_client_id": "test_client_id",
        "oauth_client_secret": "test_client_secret",
        "oauth_token_url": "https://idcs-test.identity.oraclecloud.com/oauth2/v1/token",
        "oauth_client_aud": "https://integration.ocp.oraclecloud.com:443",
        "page_size": 50,
        "request_timeout": 30,
        "max_retries": 3,
        "include_extended": False,
        "include_security": True,
        "enable_bookmarking": True,
    }


@pytest.fixture
def extended_oic_config(basic_oic_config: dict[str, object]) -> dict[str, object]:
    """Extended Oracle OIC tap configuration with all streams."""
    config = basic_oic_config.copy()
    config.update(
        {
            "include_extended": True,
            "include_integration_details": True,
            "include_connection_properties": False,
            "include_package_content": False,
            "stream_categories": ["core", "infrastructure", "security", "metadata"],
            "concurrent_requests": 5,
            "enable_caching": True,
            "cache_ttl": 300,
        },
    )
    return config


@pytest.fixture
def filtered_oic_config(basic_oic_config: dict[str, object]) -> dict[str, object]:
    """Oracle OIC tap configuration with filters."""
    config = basic_oic_config.copy()
    config.update(
        {
            "integration_status_filter": ["ACTIVATED", "CONFIGURED"],
            "connection_type_filter": ["rest", "ftp", "database"],
            "start_date": "2024-01-01T00:00:00Z",
        },
    )
    return config


@pytest.fixture
def performance_oic_config(basic_oic_config: dict[str, object]) -> dict[str, object]:
    """Oracle OIC tap configuration for performance testing."""
    config = basic_oic_config.copy()
    config.update(
        {
            "page_size": 100,
            "concurrent_requests": 10,
            "request_timeout": 60,
            "max_retries": 5,
            "retry_delay": 2.0,
            "enable_caching": True,
            "cache_ttl": 600,
        },
    )
    return config


# Mock OIC API response fixtures
@pytest.fixture
def mock_oauth_token_response() -> dict[str, object]:
    """Mock OAuth2 token response."""
    return {
        "access_token": "mock_access_token_12345",
        "token_type": "Bearer",
        "expires_in": 3600,
        "scope": "https://integration.ocp.oraclecloud.com:443/scope",
    }


@pytest.fixture
def sample_integration_data() -> list[dict[str, object]]:
    """Sample integration data for testing."""
    return [
        {
            "id": "HELLO_WORLD_01",
            "name": "HelloWorld",
            "version": "01.00.0000",
            "status": "ACTIVATED",
            "description": "Sample Hello World integration",
            "pattern": "Orchestration",
            "lastUpdatedTime": "2024-06-19T10:30:00.000Z",
            "createdTime": "2024-06-01T09:15:00.000Z",
            "createdBy": "oic.REDACTED_LDAP_BIND_PASSWORD",
            "lastUpdatedBy": "oic.REDACTED_LDAP_BIND_PASSWORD",
            "connectionRefs": [
                {"id": "REST_CONN_01", "name": "REST Connection"},
                {"id": "FTP_CONN_01", "name": "FTP Connection"},
            ],
            "tracking": {
                "payloadTracking": True,
                "tracing": True,
                "trackingFields": ["orderId", "customerId"],
            },
            "style": "WORKFLOW",
            "lockedBy": None,
            "locked": False,
        },
        {
            "id": "DATA_SYNC_02",
            "name": "DataSyncFlow",
            "version": "02.01.0000",
            "status": "CONFIGURED",
            "description": "Database synchronization flow",
            "pattern": "Map Data",
            "lastUpdatedTime": "2024-06-20T14:45:30.000Z",
            "createdTime": "2024-06-10T11:20:00.000Z",
            "createdBy": "data.engineer",
            "lastUpdatedBy": "data.engineer",
            "connectionRefs": [
                {"id": "DB_SOURCE_01", "name": "Source Database"},
                {"id": "DB_TARGET_01", "name": "Target Database"},
            ],
            "tracking": {
                "payloadTracking": False,
                "tracing": True,
                "trackingFields": ["transactionId"],
            },
            "style": "MAP",
            "lockedBy": "data.engineer",
            "locked": True,
        },
    ]


@pytest.fixture
def mock_integrations_response(
    sample_integration_data: list[dict[str, object]],
) -> dict[str, object]:
    """Mock integrations API response."""
    return {
        "items": sample_integration_data,
        "hasMore": False,
        "count": len(sample_integration_data),
        "offset": 0,
        "limit": 50,
    }


@pytest.fixture
def sample_connection_data() -> list[dict[str, object]]:
    """Sample connection data for testing."""
    return [
        {
            "id": "REST_CONN_01",
            "name": "REST Connection",
            "description": "REST API connection",
            "adapterType": "rest",
            "adapterDisplayName": "REST Adapter",
            "adapterVersion": "24.1.2",
            "status": "CONFIGURED",
            "connectionUrl": "https://api.example.com",
            "createdBy": "oic.REDACTED_LDAP_BIND_PASSWORD",
            "createdDate": "2024-06-01T09:00:00.000Z",
            "modifiedBy": "oic.REDACTED_LDAP_BIND_PASSWORD",
            "modifiedDate": "2024-06-15T16:30:00.000Z",
            "securityPolicy": "OAUTH2",
            "connectionProperties": {
                "baseUrl": "https://api.example.com",
                "authenticationType": "oauth2",
                "clientId": "api_client_123",
                "tokenUrl": "https://api.example.com/oauth/token",
            },
        },
        {
            "id": "FTP_CONN_01",
            "name": "FTP Connection",
            "description": "FTP server connection",
            "adapterType": "ftp",
            "adapterDisplayName": "FTP Adapter",
            "adapterVersion": "24.1.2",
            "status": "CONFIGURED",
            "connectionUrl": "ftp://ftp.example.com",
            "createdBy": "file.REDACTED_LDAP_BIND_PASSWORD",
            "createdDate": "2024-06-05T14:20:00.000Z",
            "modifiedBy": "file.REDACTED_LDAP_BIND_PASSWORD",
            "modifiedDate": "2024-06-18T10:15:00.000Z",
            "securityPolicy": "USERNAME_PASSWORD",
            "connectionProperties": {
                "host": "ftp.example.com",
                "port": "21",
                "username": "ftpuser",
                "authType": "basic",
            },
        },
    ]


@pytest.fixture
def mock_connections_response(
    sample_connection_data: list[dict[str, object]],
) -> dict[str, object]:
    """Mock connections API response."""
    return {
        "items": sample_connection_data,
        "hasMore": False,
        "count": len(sample_connection_data),
        "offset": 0,
        "limit": 50,
    }


@pytest.fixture
def sample_package_data() -> list[dict[str, object]]:
    """Sample package data for testing."""
    return [
        {
            "id": "PACKAGE_01",
            "name": "HelloWorldPackage",
            "version": "1.0",
            "description": "Package containing HelloWorld integration",
            "packageType": "INTEGRATION",
            "status": "COMPLETED",
            "createdBy": "package.REDACTED_LDAP_BIND_PASSWORD",
            "createdTime": "2024-06-01T12:00:00.000Z",
            "lastUpdatedTime": "2024-06-01T12:30:00.000Z",
            "size": 1024000,
            "integrations": ["HELLO_WORLD_01"],
            "connections": ["REST_CONN_01", "FTP_CONN_01"],
        },
        {
            "id": "PACKAGE_02",
            "name": "DataSyncPackage",
            "version": "2.1",
            "description": "Package containing data sync flows",
            "packageType": "INTEGRATION",
            "status": "COMPLETED",
            "createdBy": "data.REDACTED_LDAP_BIND_PASSWORD",
            "createdTime": "2024-06-10T15:30:00.000Z",
            "lastUpdatedTime": "2024-06-20T16:45:00.000Z",
            "size": 2048000,
            "integrations": ["DATA_SYNC_02"],
            "connections": ["DB_SOURCE_01", "DB_TARGET_01"],
        },
    ]


@pytest.fixture
def mock_packages_response(
    sample_package_data: list[dict[str, object]],
) -> dict[str, object]:
    """Mock packages API response."""
    return {
        "items": sample_package_data,
        "hasMore": False,
        "count": len(sample_package_data),
        "offset": 0,
        "limit": 50,
    }


@pytest.fixture
def sample_lookup_data() -> list[dict[str, object]]:
    """Sample lookup data for testing."""
    return [
        {
            "id": "COUNTRY_CODES",
            "name": "CountryCodes",
            "description": "ISO country codes lookup",
            "createdBy": "data.REDACTED_LDAP_BIND_PASSWORD",
            "createdTime": "2024-06-01T10:00:00.000Z",
            "lastUpdatedTime": "2024-06-15T14:30:00.000Z",
            "entries": [
                {"key": "US", "value": "United States"},
                {"key": "CA", "value": "Canada"},
                {"key": "MX", "value": "Mexico"},
            ],
        },
        {
            "id": "ERROR_CODES",
            "name": "ErrorCodes",
            "description": "Application error codes",
            "createdBy": "app.REDACTED_LDAP_BIND_PASSWORD",
            "createdTime": "2024-06-05T08:15:00.000Z",
            "lastUpdatedTime": "2024-06-18T11:20:00.000Z",
            "entries": [
                {"key": "E001", "value": "Invalid request format"},
                {"key": "E002", "value": "Authentication failed"},
                {"key": "E003", "value": "Resource not found"},
            ],
        },
    ]


@pytest.fixture
def mock_lookups_response(
    sample_lookup_data: list[dict[str, object]],
) -> dict[str, object]:
    """Mock lookups API response."""
    return {
        "items": sample_lookup_data,
        "hasMore": False,
        "count": len(sample_lookup_data),
        "offset": 0,
        "limit": 50,
    }


# Extended stream fixtures
@pytest.fixture
def sample_library_data() -> list[dict[str, object]]:
    """Sample library data for testing."""
    return [
        {
            "id": "JS_LIB_01",
            "name": "UtilityFunctions",
            "type": "JAVASCRIPT",
            "description": "Common utility functions",
            "createdBy": "dev.REDACTED_LDAP_BIND_PASSWORD",
            "createdTime": "2024-06-01T11:30:00.000Z",
            "lastUpdatedTime": "2024-06-10T09:45:00.000Z",
            "content": "function formatDate(date) { return date.toISOString(); }",
        },
    ]


@pytest.fixture
def sample_certificate_data() -> list[dict[str, object]]:
    """Sample certificate data for testing."""
    return [
        {
            "id": "CERT_01",
            "name": "APIGatewayCert",
            "type": "X509",
            "status": "ACTIVE",
            "validFrom": "2024-01-01T00:00:00.000Z",
            "validTo": "2025-01-01T00:00:00.000Z",
            "issuer": "CN=CA Authority",
            "subject": "CN=api.example.com",
            "fingerprint": "AA:BB:CC:DD:EE:FF:00:11:22:33:44:55:66:77:88:99:AA:BB:CC:DD",
        },
    ]


@pytest.fixture
def sample_adapter_data() -> list[dict[str, object]]:
    """Sample adapter data for testing."""
    return [
        {
            "id": "rest",
            "name": "REST Adapter",
            "displayName": "REST",
            "version": "24.1.2",
            "description": "REST API adapter",
            "category": "Technology",
            "capabilities": ["invoke", "trigger"],
            "connectionTypes": ["outbound", "inbound"],
        },
    ]


# Singer protocol fixtures
@pytest.fixture
def singer_catalog() -> dict[str, object]:
    """Singer catalog for OIC tap."""
    return {
        "streams": [
            {
                "tap_stream_id": "integrations",
                "schema": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "name": {"type": "string"},
                        "version": {"type": "string"},
                        "status": {"type": "string"},
                        "lastUpdatedTime": {"type": "string", "format": "date-time"},
                    },
                },
                "metadata": [
                    {
                        "breadcrumb": [],
                        "metadata": {
                            "replication-method": "INCREMENTAL",
                            "replication-key": "lastUpdatedTime",
                            "selected": True,
                        },
                    },
                ],
            },
            {
                "tap_stream_id": "connections",
                "schema": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "name": {"type": "string"},
                        "adapterType": {"type": "string"},
                        "status": {"type": "string"},
                        "modifiedDate": {"type": "string", "format": "date-time"},
                    },
                },
                "metadata": [
                    {
                        "breadcrumb": [],
                        "metadata": {
                            "replication-method": "INCREMENTAL",
                            "replication-key": "modifiedDate",
                            "selected": True,
                        },
                    },
                ],
            },
        ],
    }


@pytest.fixture
def singer_state() -> dict[str, object]:
    """Singer state for OIC tap."""
    return {
        "currently_syncing": None,
        "bookmarks": {
            "integrations": {
                "replication_key_value": "2024-06-01T00:00:00.000Z",
                "version": 1,
            },
            "connections": {
                "replication_key_value": "2024-06-01T00:00:00.000Z",
                "version": 1,
            },
        },
    }


# Error handling fixtures
@pytest.fixture
def mock_http_error_response() -> Mock:
    """Mock HTTP error response."""
    error_response = Mock()
    error_response.status_code = 401
    error_response.reason = "Unauthorized"
    error_response.text = (
        '{"error": "invalid_token", "error_description": "Token has expired"}'
    )
    error_response.headers = {"Content-Type": "application/json"}
    return error_response


@pytest.fixture
def mock_rate_limit_response() -> Mock:
    """Mock rate limit error response."""
    error_response = Mock()
    error_response.status_code = 429
    error_response.reason = "Too Many Requests"
    error_response.text = '{"error": "rate_limit_exceeded"}'
    error_response.headers = {"Content-Type": "application/json", "Retry-After": "60"}
    return error_response


# Performance testing fixtures
@pytest.fixture
def large_integration_dataset() -> list[dict[str, object]]:
    """Large integration dataset for performance testing."""
    integrations = []

    for i in range(1000):
        integration = {
            "id": f"INTEGRATION_{i:04d}",
            "name": f"Integration{i:04d}",
            "version": "01.00.0000",
            "status": "ACTIVATED" if i % 2 == 0 else "CONFIGURED",
            "description": f"Test integration number {i}",
            "pattern": "Orchestration" if i % 3 == 0 else "Map Data",
            "lastUpdatedTime": f"2024-06-{(i % 30) + 1:02d}T{(i % 24):02d}:00:00.000Z",
            "createdTime": "2024-06-01T09:00:00.000Z",
            "createdBy": "test.user",
            "lastUpdatedBy": "test.user",
        }
        integrations.append(integration)

    return integrations


@pytest.fixture
def benchmark_config() -> dict[str, object]:
    """Configuration for performance benchmarking."""
    return {
        "max_records_to_process": 1000,
        "expected_processing_time": 30.0,  # seconds
        "memory_limit": 100 * 1024 * 1024,  # 100MB
        "page_sizes": [25, 50, 100, 200],
        "concurrent_request_counts": [1, 3, 5, 10],
    }


# Pytest markers for test categorization
def pytest_configure(config: pytest.Config) -> None:
    """Configure pytest markers."""
    config.addinivalue_line("markers", "unit: Unit tests")
    config.addinivalue_line("markers", "integration: Integration tests")
    config.addinivalue_line("markers", "e2e: End-to-end tests")
    config.addinivalue_line("markers", "oic: Oracle OIC-specific tests")
    config.addinivalue_line("markers", "singer: Singer protocol tests")
    config.addinivalue_line("markers", "oauth: OAuth2 authentication tests")
    config.addinivalue_line("markers", "performance: Performance tests")
    config.addinivalue_line("markers", "extended: Extended stream tests")
    config.addinivalue_line("markers", "slow: Slow tests")


# Mock services
@pytest.fixture
def mock_oic_client() -> type[Any]:
    """Mock Oracle OIC client for testing."""

    class MockOICClient:
        def __init__(self, config: dict[str, object]) -> None:
            self.config = config
            self.authenticated = False
            self.call_count: dict[str, int] = {}

        async def authenticate(self) -> bool:
            self.authenticated = True
            return True

        async def get_integrations(self, **kwargs: object) -> dict[str, object]:  # noqa: ARG002
            self.call_count["get_integrations"] = (
                self.call_count.get("get_integrations", 0) + 1
            )
            return {
                "success": True,
                "items": [],
                "hasMore": False,
                "count": 0,
            }

        async def get_connections(self, **kwargs: object) -> dict[str, object]:  # noqa: ARG002
            self.call_count["get_connections"] = (
                self.call_count.get("get_connections", 0) + 1
            )
            return {
                "success": True,
                "items": [],
                "hasMore": False,
                "count": 0,
            }

        def paginate_request(
            self,
            request_func: object,  # noqa: ARG002
            **kwargs: object,  # noqa: ARG002
        ) -> Iterator[Any]:
            """Mock pagination."""
            yield from []

    return MockOICClient


@pytest.fixture
def mock_oauth_authenticator() -> type[Any]:
    """Mock OAuth2 authenticator for testing."""

    class MockOAuthAuthenticator:
        def __init__(self, config: dict[str, object]) -> None:
            self.config = config
            self.token = None
            self.token_expires_at = None

        async def get_access_token(self) -> dict[str, object]:
            return {
                "success": True,
                "value": "mock_access_token_12345",
            }

        def is_token_valid(self) -> bool:
            return True

        async def refresh_token(self) -> dict[str, object]:
            return await self.get_access_token()

    return MockOAuthAuthenticator
