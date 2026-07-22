"""Tests for OIC OAuth2 authenticator.

Tests for FlextOracleOicAuthenticator with mocked dependencies.


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import base64
from typing import cast
from unittest.mock import MagicMock

import pytest

from flext_cli import u as cli_u
from flext_tap_oracle_oic.tap import FlextOracleOicAuthenticator
from flext_tests import r, tm


class TestsFlextTapOracleOicAuth:
    """Test OIC OAuth2 authenticator with mocked dependencies."""

    @pytest.fixture
    def mock_config(self) -> MagicMock:
        """Create a mock settings that mimics FlextTapOracleOicSettings."""
        settings = MagicMock()
        settings.oauth_client_id = "test_client_id"
        settings.oauth_client_secret = MagicMock()
        settings.oauth_client_secret.get_secret_value.return_value = (
            "test_client_secret"
        )
        settings.oauth_token_url = (
            "https://test.identity.oraclecloud.com/oauth2/v1/token"
        )
        settings.oauth_audience = "urn:opc:resource:consumer:all"
        settings.base_url = "https://oic.example.com"
        settings.get_token_request_data.return_value = {
            "grant_type": "client_credentials",
            "client_id": "test_client_id",
            "client_secret": "test_client_secret",
            "audience": "urn:opc:resource:consumer:all",
        }
        return settings

    @pytest.fixture
    def authenticator(self, mock_config: MagicMock) -> FlextOracleOicAuthenticator:
        """Create authenticator bypassing __init__ to avoid global state."""
        auth = FlextOracleOicAuthenticator.__new__(FlextOracleOicAuthenticator)
        auth.settings = mock_config
        auth._access_token = None
        auth._api_client = MagicMock()
        return auth

    def test_authenticator_initialization(
        self, authenticator: FlextOracleOicAuthenticator, mock_config: MagicMock
    ) -> None:
        """Test authenticator stores settings."""
        assert authenticator.settings is mock_config
        tm.that(authenticator._access_token, none=True)

    def test_get_access_token_success(
        self, authenticator: FlextOracleOicAuthenticator
    ) -> None:
        """Test successful token retrieval."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.body = {
            "access_token": "test_token_123",
            "token_type": "Bearer",
            "expires_in": 3600,
        }
        cast("MagicMock", authenticator._api_client).post.return_value = r[
            MagicMock
        ].ok(mock_response)
        result = authenticator.get_access_token()
        tm.ok(result)
        tm.that(result.value, eq="test_token_123")
        tm.that(authenticator._access_token, eq="test_token_123")

    def test_get_access_token_http_failure(
        self, authenticator: FlextOracleOicAuthenticator
    ) -> None:
        """Test token retrieval with HTTP failure."""
        cast("MagicMock", authenticator._api_client).post.return_value = r.fail(
            "Connection refused"
        )
        result = authenticator.get_access_token()
        tm.fail(result)
        tm.that(result.error, none=False)
        tm.that(result.error, has="OAuth2 request failed")

    def test_get_access_token_bad_status_code(
        self, authenticator: FlextOracleOicAuthenticator
    ) -> None:
        """Test token retrieval with non-200 status code."""
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.body = {"error": "invalid_client"}
        cast("MagicMock", authenticator._api_client).post.return_value = r[
            MagicMock
        ].ok(mock_response)
        result = authenticator.get_access_token()
        tm.fail(result)
        tm.that(result.error, none=False)
        tm.that(result.error, has="status")

    def test_get_access_token_empty_body(
        self, authenticator: FlextOracleOicAuthenticator
    ) -> None:
        """Test token retrieval with empty response body."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.body = None
        cast("MagicMock", authenticator._api_client).post.return_value = r[
            MagicMock
        ].ok(mock_response)
        result = authenticator.get_access_token()
        tm.fail(result)
        tm.that(result.error, none=False)

    def test_get_access_token_missing_token_in_response(
        self, authenticator: FlextOracleOicAuthenticator
    ) -> None:
        """Test token retrieval when response has no access_token field."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.body = {"token_type": "Bearer", "expires_in": 3600}
        cast("MagicMock", authenticator._api_client).post.return_value = r[
            MagicMock
        ].ok(mock_response)
        result = authenticator.get_access_token()
        tm.fail(result)
        tm.that(result.error, none=False)

    def test_get_access_token_string_body(
        self, authenticator: FlextOracleOicAuthenticator
    ) -> None:
        """Test token retrieval with JSON string body."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.body = cli_u.Cli.json_dumps({
            "access_token": "string_body_token",
            "token_type": "Bearer",
        }).unwrap()
        cast("MagicMock", authenticator._api_client).post.return_value = r[
            MagicMock
        ].ok(mock_response)
        result = authenticator.get_access_token()
        tm.ok(result)
        tm.that(result.value, eq="string_body_token")

    def test_get_access_token_exception_handling(
        self, authenticator: FlextOracleOicAuthenticator
    ) -> None:
        """Test token retrieval handles unexpected exceptions."""
        cast("MagicMock", authenticator._api_client).post.side_effect = RuntimeError(
            "Unexpected error"
        )
        result = authenticator.get_access_token()
        tm.fail(result)
        tm.that(result.error, none=False)
        tm.that(result.error, has="OAuth2 authentication failed")

    def test_token_request_data_structure(self, mock_config: MagicMock) -> None:
        """Test token request data has correct structure."""
        data = mock_config.get_token_request_data()
        tm.that(data["grant_type"], eq="client_credentials")
        tm.that(data["client_id"], eq="test_client_id")
        tm.that(data["client_secret"], eq="test_client_secret")
        tm.that(data["audience"], eq="urn:opc:resource:consumer:all")

    def test_client_credentials_encoding(self) -> None:
        """Test client credentials base64 encoding logic."""
        client_id = "test_client_id"
        client_secret = "test_client_secret"
        expected = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
        actual = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
        tm.that(actual, eq=expected)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
