"""Real Oracle Integration Cloud client implementation.

Enterprise client using flext-core patterns with real Oracle OIC connectivity.
Zero tolerance for mock implementations - real OAuth2 and REST API integration.
"""

from __future__ import annotations

import json
from datetime import datetime, timedelta
from typing import Any
from urllib.parse import urljoin

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from flext_core.domain.types import ServiceResult
from flext_observability.logging import get_logger

logger = get_logger(__name__)


class OracleOICClient:
    """Real Oracle Integration Cloud client with enterprise features."""

    def __init__(
        self,
        base_url: str,
        oauth_client_id: str,
        oauth_client_secret: str,
        oauth_endpoint: str,
        oauth_scope: str = "urn:opc:resource:consumer:all",
    ) -> None:
        """Initialize Oracle OIC client.

        Args:
            base_url: Oracle OIC base URL (e.g., https://myoic-instance.integration.ocp.oraclecloud.com)
            oauth_client_id: OAuth2 client ID from Oracle IDCS
            oauth_client_secret: OAuth2 client secret from Oracle IDCS
            oauth_endpoint: OAuth2 token endpoint URL
            oauth_scope: OAuth2 scope for OIC access

        """
        self.base_url = base_url.rstrip("/")
        self.oauth_client_id = oauth_client_id
        self.oauth_client_secret = oauth_client_secret
        self.oauth_endpoint = oauth_endpoint
        self.oauth_scope = oauth_scope

        # Session with retry strategy
        self.session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS"],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        # Authentication state
        self._access_token: str | None = None
        self._token_expires_at: datetime | None = None

        logger.info(
            "Oracle OIC client initialized",
            extra={
                "base_url": self.base_url,
                "oauth_scope": self.oauth_scope,
            },
        )

    def _get_access_token(self) -> ServiceResult[str]:
        """Get OAuth2 access token from Oracle IDCS.

        Returns:
            ServiceResult with access token or error.

        """
        try:
            # Check if current token is still valid
            if (
                self._access_token
                and self._token_expires_at
                and datetime.now() < self._token_expires_at
            ):
                return ServiceResult.success(self._access_token)

            # Request new token
            auth_payload = {
                "grant_type": "client_credentials",
                "scope": self.oauth_scope,
            }

            response = requests.post(
                self.oauth_endpoint,
                data=auth_payload,
                auth=(self.oauth_client_id, self.oauth_client_secret),
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=30,
            )

            if response.status_code != 200:
                return ServiceResult.fail(
                    f"OAuth2 authentication failed: {response.status_code} - {response.text}",
                )

            token_data = response.json()
            self._access_token = token_data["access_token"]

            # Calculate token expiration (with 5 minute buffer)
            expires_in = token_data.get("expires_in", 3600)
            self._token_expires_at = datetime.now().replace(
                second=0,
                microsecond=0,
            ) + timedelta(seconds=expires_in - 300)

            logger.info(
                "OAuth2 token obtained successfully",
                extra={
                    "expires_at": self._token_expires_at.isoformat(),
                },
            )

            return ServiceResult.success(self._access_token)

        except Exception as e:
            logger.exception("Failed to obtain OAuth2 token")
            return ServiceResult.fail(f"OAuth2 token request failed: {e}")

    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> ServiceResult[dict[str, Any]]:
        """Make authenticated request to Oracle OIC API.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            params: Query parameters
            **kwargs: Additional request arguments

        Returns:
            ServiceResult with response data or error.

        """
        try:
            # Get valid access token
            token_result = self._get_access_token()
            if not token_result.is_success:
                return ServiceResult.fail(
                    f"Authentication failed: {token_result.error}",
                )

            # Prepare request
            url = urljoin(self.base_url, endpoint)
            headers = {
                "Authorization": f"Bearer {token_result.data}",
                "Accept": "application/json",
            }
            headers.update(kwargs.pop("headers", {}))

            # Make request
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                headers=headers,
                timeout=60,
                **kwargs,
            )

            # Handle response
            if response.status_code == 401:
                # Token might be expired, clear cache and retry once
                self._access_token = None
                self._token_expires_at = None
                logger.warning("Token expired, retrying authentication")
                return self._make_request(method, endpoint, params, **kwargs)

            if not response.ok:
                return ServiceResult.fail(
                    f"API request failed: {response.status_code} - {response.text}",
                )

            # Parse JSON response
            try:
                data = response.json()
            except json.JSONDecodeError:
                data = {"content": response.text}

            logger.debug(
                "API request successful",
                extra={
                    "method": method,
                    "endpoint": endpoint,
                    "status_code": response.status_code,
                },
            )

            return ServiceResult.success(data)

        except Exception as e:
            logger.exception("API request failed")
            return ServiceResult.fail(f"Request failed: {e}")

    def get_integrations(
        self,
        limit: int = 100,
        offset: int = 0,
    ) -> ServiceResult[dict[str, Any]]:
        """Get list of integrations from Oracle OIC.

        Args:
            limit: Maximum number of integrations to return
            offset: Number of integrations to skip

        Returns:
            ServiceResult with integrations data.

        """
        params = {
            "limit": limit,
            "offset": offset,
        }

        return self._make_request("GET", "/ic/api/integration/v1/integrations", params)

    def get_integration_details(
        self, integration_id: str,
    ) -> ServiceResult[dict[str, Any]]:
        """Get detailed information about a specific integration.

        Args:
            integration_id: Integration identifier

        Returns:
            ServiceResult with integration details.

        """
        endpoint = f"/ic/api/integration/v1/integrations/{integration_id}"
        return self._make_request("GET", endpoint)

    def get_connections(
        self,
        limit: int = 100,
        offset: int = 0,
    ) -> ServiceResult[dict[str, Any]]:
        """Get list of connections from Oracle OIC.

        Args:
            limit: Maximum number of connections to return
            offset: Number of connections to skip

        Returns:
            ServiceResult with connections data.

        """
        params = {
            "limit": limit,
            "offset": offset,
        }

        return self._make_request("GET", "/ic/api/integration/v1/connections", params)

    def get_connection_details(
        self, connection_id: str,
    ) -> ServiceResult[dict[str, Any]]:
        """Get detailed information about a specific connection.

        Args:
            connection_id: Connection identifier

        Returns:
            ServiceResult with connection details.

        """
        endpoint = f"/ic/api/integration/v1/connections/{connection_id}"
        return self._make_request("GET", endpoint)

    def get_lookups(
        self,
        limit: int = 100,
        offset: int = 0,
    ) -> ServiceResult[dict[str, Any]]:
        """Get list of lookups from Oracle OIC.

        Args:
            limit: Maximum number of lookups to return
            offset: Number of lookups to skip

        Returns:
            ServiceResult with lookups data.

        """
        params = {
            "limit": limit,
            "offset": offset,
        }

        return self._make_request("GET", "/ic/api/integration/v1/lookups", params)

    def get_packages(
        self,
        limit: int = 100,
        offset: int = 0,
    ) -> ServiceResult[dict[str, Any]]:
        """Get list of packages from Oracle OIC.

        Args:
            limit: Maximum number of packages to return
            offset: Number of packages to skip

        Returns:
            ServiceResult with packages data.

        """
        params = {
            "limit": limit,
            "offset": offset,
        }

        return self._make_request("GET", "/ic/api/integration/v1/packages", params)

    def get_libraries(
        self,
        limit: int = 100,
        offset: int = 0,
    ) -> ServiceResult[dict[str, Any]]:
        """Get list of libraries from Oracle OIC.

        Args:
            limit: Maximum number of libraries to return
            offset: Number of libraries to skip

        Returns:
            ServiceResult with libraries data.

        """
        params = {
            "limit": limit,
            "offset": offset,
        }

        return self._make_request("GET", "/ic/api/integration/v1/libraries", params)

    def test_connection(self) -> ServiceResult[dict[str, Any]]:
        """Test connection to Oracle OIC.

        Returns:
            ServiceResult with connection test results.

        """
        logger.info("Testing Oracle OIC connection")

        # Test authentication first
        token_result = self._get_access_token()
        if not token_result.is_success:
            return ServiceResult.fail(
                f"Authentication test failed: {token_result.error}",
            )

        # Test API connectivity with a simple endpoint
        health_result = self._make_request(
            "GET", "/ic/api/integration/v1/integrations", {"limit": 1},
        )
        if not health_result.is_success:
            return ServiceResult.fail(
                f"API connectivity test failed: {health_result.error}",
            )

        logger.info("Oracle OIC connection test successful")
        return ServiceResult.success(
            {
                "status": "connected",
                "authentication": "success",
                "api_connectivity": "success",
                "timestamp": datetime.now().isoformat(),
            },
        )

    def close(self) -> None:
        """Close the client session."""
        if self.session:
            self.session.close()
            logger.info("Oracle OIC client session closed")
