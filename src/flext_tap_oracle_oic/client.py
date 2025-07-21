"""Oracle Integration Cloud client using centralized patterns.

Refactored to use centralized OIC patterns from flext-core.
Eliminates code duplication while maintaining enterprise features.
"""

from __future__ import annotations

from typing import Any

from flext_core.config.oracle_oic import (
    OICAuthConfig,
    OICConnectionConfig,
    OICTapClient,
)
from flext_core.domain.types import ServiceResult
from flext_observability.logging import get_logger
from pydantic import SecretStr

logger = get_logger(__name__)


class OracleOICClient:
    """Oracle Integration Cloud client using centralized patterns from flext-core.

    Refactored implementation using centralized authentication and API patterns.
    Eliminates code duplication while maintaining enterprise features.
    """

    def __init__(
        self,
        base_url: str,
        oauth_client_id: str,
        oauth_client_secret: str,
        oauth_endpoint: str,
        oauth_scope: str = "urn:opc:resource:consumer:all",
    ) -> None:
        """Initialize Oracle OIC client using centralized patterns.

        Args:
            base_url: Oracle OIC base URL
            oauth_client_id: OAuth2 client ID from Oracle IDCS
            oauth_client_secret: OAuth2 client secret from Oracle IDCS
            oauth_endpoint: OAuth2 token endpoint URL
            oauth_scope: OAuth2 scope for OIC access

        """
        # Create centralized auth config
        auth_config = OICAuthConfig(
            oauth_client_id=oauth_client_id,
            oauth_client_secret=SecretStr(oauth_client_secret),
            oauth_token_url=oauth_endpoint,
            oauth_scope=oauth_scope,
        )

        # Create centralized connection config
        connection_config = OICConnectionConfig(base_url=base_url)

        # Create centralized authenticator
        from flext_core.config.oracle_oic import OICTapAuthenticator

        authenticator = OICTapAuthenticator(auth_config)

        # Use centralized OIC Tap client
        self._central_client = OICTapClient(
            connection_config=connection_config,
            authenticator=authenticator,
        )

        # Store configuration for test compatibility
        self._base_url = base_url
        self._oauth_client_id = oauth_client_id
        self._oauth_client_secret = oauth_client_secret

        logger.info(
            "Oracle OIC client initialized using centralized patterns",
            extra={
                "base_url": base_url,
                "oauth_scope": oauth_scope,
            },
        )

    @property
    def base_url(self) -> str:
        """Get base URL for test compatibility."""
        return self._base_url

    @property
    def oauth_client_id(self) -> str:
        """Get OAuth client ID for test compatibility."""
        return self._oauth_client_id

    @property
    def oauth_client_secret(self) -> str:
        """Get OAuth client secret for test compatibility."""
        return self._oauth_client_secret

    @property
    def session(self) -> Any:
        """Get HTTP session for test compatibility."""
        return (
            self._central_client._session  # noqa: SLF001 - Test compatibility access
            if hasattr(self._central_client, "_session")
            else None
        )

    def get_auth_headers(self) -> dict[str, str]:
        """Get authentication headers for test compatibility."""
        token_result = self._get_access_token()
        if token_result.is_success:
            return {"Authorization": f"Bearer {token_result.data}"}
        return {}

    def get_access_token(self) -> ServiceResult[str]:
        """Get access token for test compatibility."""
        return self._get_access_token()

    def get(self, endpoint: str, **kwargs: Any) -> ServiceResult[dict[str, Any]]:
        """Make GET request for test compatibility."""
        return self._make_request("GET", endpoint, **kwargs)

    def _get_access_token(self) -> ServiceResult[str]:
        """Get OAuth2 access token using centralized authentication.

        Returns:
            ServiceResult with access token or error.

        """
        return self._central_client.authenticator.get_access_token()

    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> ServiceResult[dict[str, Any]]:
        """Make authenticated request using centralized client.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            params: Query parameters
            **kwargs: Additional request arguments

        Returns:
            ServiceResult with response data or error.

        """
        return self._central_client.make_request(
            method=method,
            endpoint=endpoint,
            params=params,
            **kwargs,
        )

    def get_integrations(
        self,
        limit: int = 100,
        offset: int = 0,
        status_filter: list[str] | None = None,
    ) -> ServiceResult[list[dict[str, Any]]]:
        """Get list of integrations using centralized client.

        Args:
            limit: Maximum number of integrations to return
            offset: Number of integrations to skip
            status_filter: Filter integrations by status

        Returns:
            ServiceResult with integrations data.

        """
        return self._central_client.get_integrations(
            status_filter=status_filter,
            page_size=limit,
        )

    def get_integration_details(
        self,
        integration_id: str,
    ) -> ServiceResult[dict[str, Any]]:
        """Get detailed information about a specific integration using centralized client.

        Args:
            integration_id: Integration identifier

        Returns:
            ServiceResult with integration details.

        """
        endpoint = f"/integrations/{integration_id}"
        return self._central_client.make_request("GET", endpoint)

    def get_connections(
        self,
        limit: int = 100,
        offset: int = 0,
        type_filter: list[str] | None = None,
    ) -> ServiceResult[list[dict[str, Any]]]:
        """Get list of connections using centralized client.

        Args:
            limit: Maximum number of connections to return
            offset: Number of connections to skip
            type_filter: Filter connections by adapter type

        Returns:
            ServiceResult with connections data.

        """
        return self._central_client.get_connections(
            type_filter=type_filter,
            page_size=limit,
        )

    def get_connection_details(
        self,
        connection_id: str,
    ) -> ServiceResult[dict[str, Any]]:
        """Get detailed information about a specific connection using centralized client.

        Args:
            connection_id: Connection identifier

        Returns:
            ServiceResult with connection details.

        """
        endpoint = f"/connections/{connection_id}"
        return self._central_client.make_request("GET", endpoint)

    def get_lookups(
        self,
        limit: int = 100,
        offset: int = 0,
    ) -> ServiceResult[list[dict[str, Any]]]:
        """Get list of lookups using centralized client.

        Args:
            limit: Maximum number of lookups to return
            offset: Number of lookups to skip

        Returns:
            ServiceResult with lookups data.

        """
        return self._central_client.get_lookups(page_size=limit)

    def get_packages(
        self,
        limit: int = 100,
        offset: int = 0,
    ) -> ServiceResult[list[dict[str, Any]]]:
        """Get list of packages using centralized client.

        Args:
            limit: Maximum number of packages to return
            offset: Number of packages to skip

        Returns:
            ServiceResult with packages data.

        """
        return self._central_client.get_packages(page_size=limit)

    def get_libraries(
        self,
        limit: int = 100,
        offset: int = 0,
    ) -> ServiceResult[dict[str, Any]]:
        """Get list of libraries using centralized client.

        Args:
            limit: Maximum number of libraries to return
            offset: Number of libraries to skip

        Returns:
            ServiceResult with libraries data.

        """
        endpoint = "/libraries"
        params = {"limit": limit, "offset": offset}
        return self._central_client.make_request("GET", endpoint, params=params)

    def test_connection(self) -> ServiceResult[dict[str, Any]]:
        """Test connection to Oracle OIC using centralized client.

        Returns:
            ServiceResult with connection test results.

        """
        logger.info("Testing Oracle OIC connection using centralized patterns")

        # Test authentication first
        token_result = self._get_access_token()
        if not token_result.is_success:
            return ServiceResult.fail(
                f"Authentication test failed: {token_result.error}",
            )

        # Test API connectivity with a simple endpoint
        health_result = self._central_client.get_integrations(page_size=1)
        if not health_result.is_success:
            return ServiceResult.fail(
                f"API connectivity test failed: {health_result.error}",
            )

        logger.info("Oracle OIC connection test successful")
        from datetime import UTC, datetime

        return ServiceResult.ok(
            {
                "status": "connected",
                "authentication": "success",
                "api_connectivity": "success",
                "timestamp": datetime.now(UTC).isoformat(),
            },
        )

    def close(self) -> None:
        """Close the client session using centralized patterns."""
        # The centralized client handles session cleanup internally
        logger.info("Oracle OIC client closed (centralized session management)")
