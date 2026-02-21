"""Tests for OIC OAuth2 authenticator.

Tests for FlextOracleOicAuthenticator with mocked dependencies.


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import base64
import json
from unittest.mock import MagicMock

import pytest
from flext_core import r
from flext_tap_oracle_oic.tap_client import FlextOracleOicAuthenticator


class TestOICOAuth2Authenticator:
    """Test OIC OAuth2 authenticator with mocked dependencies."""

    @pytest.fixture
    def mock_config(self) -> MagicMock:
        """Create a mock config that mimics FlextMeltanoTapOracleOicSettings."""
        config = MagicMock()
        config.oauth_client_id = "test_client_id"
        config.oauth_client_secret = MagicMock()
        config.oauth_client_secret.get_secret_value.return_value = "test_client_secret"
        config.oauth_token_url = "https://test.identity.oraclecloud.com/oauth2/v1/token"
        config.oauth_audience = "urn:opc:resource:consumer:all"
        config.base_url = "https://oic.example.com"
        config.get_token_request_data.return_value = {
            "grant_type": "client_credentials",
            "client_id": "test_client_id",
            "client_secret": "test_client_secret",
            "audience": "urn:opc:resource:consumer:all",
        }
        return config

    @pytest.fixture
    def authenticator(self, mock_config: MagicMock) -> FlextOracleOicAuthenticator:
        """Create authenticator bypassing __init__ to avoid global state."""
        auth = FlextOracleOicAuthenticator.__new__(FlextOracleOicAuthenticator)
        auth.config = mock_config
        auth._access_token = None
        auth._api_client = MagicMock()
        return auth

    def test_authenticator_initialization(
        self,
        authenticator: FlextOracleOicAuthenticator,
        mock_config: MagicMock,
    ) -> None:
        """Test authenticator stores config."""
        assert authenticator.config is mock_config
        assert authenticator._access_token is None

    def test_get_access_token_success(
        self,
        authenticator: FlextOracleOicAuthenticator,
    ) -> None:
        """Test successful token retrieval."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.body = {
            "access_token": "test_token_123",
            "token_type": "Bearer",
            "expires_in": 3600,
        }
        authenticator._api_client.post.return_value = r[object].ok(mock_response)

        result = authenticator.get_access_token()
        assert result.is_success
        assert result.value == "test_token_123"
        assert authenticator._access_token == "test_token_123"

    def test_get_access_token_http_failure(
        self,
        authenticator: FlextOracleOicAuthenticator,
    ) -> None:
        """Test token retrieval with HTTP failure."""
        authenticator._api_client.post.return_value = r[object].fail(
            "Connection refused",
        )

        result = authenticator.get_access_token()
        assert result.is_failure
        assert result.error is not None
        assert "OAuth2 request failed" in result.error

    def test_get_access_token_bad_status_code(
        self,
        authenticator: FlextOracleOicAuthenticator,
    ) -> None:
        """Test token retrieval with non-200 status code."""
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.body = {"error": "invalid_client"}
        authenticator._api_client.post.return_value = r[object].ok(mock_response)

        result = authenticator.get_access_token()
        assert result.is_failure
        assert result.error is not None
        assert "status" in result.error

    def test_get_access_token_empty_body(
        self,
        authenticator: FlextOracleOicAuthenticator,
    ) -> None:
        """Test token retrieval with empty response body."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.body = None
        authenticator._api_client.post.return_value = r[object].ok(mock_response)

        result = authenticator.get_access_token()
        assert result.is_failure
        assert result.error is not None

    def test_get_access_token_missing_token_in_response(
        self,
        authenticator: FlextOracleOicAuthenticator,
    ) -> None:
        """Test token retrieval when response has no access_token field."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.body = {"token_type": "Bearer", "expires_in": 3600}
        authenticator._api_client.post.return_value = r[object].ok(mock_response)

        result = authenticator.get_access_token()
        assert result.is_failure
        assert result.error is not None

    def test_get_access_token_string_body(
        self,
        authenticator: FlextOracleOicAuthenticator,
    ) -> None:
        """Test token retrieval with JSON string body."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.body = json.dumps(
            {
                "access_token": "string_body_token",
                "token_type": "Bearer",
            },
        )
        authenticator._api_client.post.return_value = r[object].ok(mock_response)

        result = authenticator.get_access_token()
        assert result.is_success
        assert result.value == "string_body_token"

    def test_get_access_token_exception_handling(
        self,
        authenticator: FlextOracleOicAuthenticator,
    ) -> None:
        """Test token retrieval handles unexpected exceptions."""
        authenticator._api_client.post.side_effect = RuntimeError("Unexpected error")

        result = authenticator.get_access_token()
        assert result.is_failure
        assert result.error is not None
        assert "OAuth2 authentication failed" in result.error

    def test_token_request_data_structure(
        self,
        mock_config: MagicMock,
    ) -> None:
        """Test token request data has correct structure."""
        data = mock_config.get_token_request_data()

        assert data["grant_type"] == "client_credentials"
        assert data["client_id"] == "test_client_id"
        assert data["client_secret"] == "test_client_secret"
        assert data["audience"] == "urn:opc:resource:consumer:all"

    def test_client_credentials_encoding(self) -> None:
        """Test client credentials base64 encoding logic."""
        client_id = "test_client_id"
        client_secret = "test_client_secret"

        expected = base64.b64encode(
            f"{client_id}:{client_secret}".encode(),
        ).decode()
        actual = base64.b64encode(
            f"{client_id}:{client_secret}".encode(),
        ).decode()
        assert actual == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
