"""Oracle Integration Cloud configuration patterns.

This module provides OIC-specific configuration classes that should be used
by the tap-oracle-oic project. These are CONCRETE implementations specific
to Oracle OIC and should NOT be in flext-core (abstract foundation).

Architectural principle: flext-core provides abstract patterns,
concrete projects implement specific functionality.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any

import httpx
from flext_core.domain.shared_types import ServiceResult
from flext_observability.logging import get_logger
from pydantic import BaseModel, Field, SecretStr

logger = get_logger(__name__)


class OICAuthConfig(BaseModel):
    """Oracle Integration Cloud authentication configuration."""

    oauth_client_id: str = Field(..., description="OAuth2 client ID from Oracle IDCS")
    oauth_client_secret: SecretStr = Field(
        ..., description="OAuth2 client secret from Oracle IDCS",
    )
    oauth_token_url: str = Field(..., description="OAuth2 token endpoint URL")
    oauth_client_aud: str | None = Field(
        None, description="OAuth2 audience (auto-detected if not provided)",
    )
    oauth_scope: str = Field("", description="OAuth2 scope for OIC access")


class OICConnectionConfig(BaseModel):
    """Oracle Integration Cloud connection configuration."""

    base_url: str = Field(..., description="Oracle OIC instance base URL")
    api_version: str = Field("v1", description="OIC API version")
    timeout: int = Field(30, description="Request timeout in seconds")


class OICTapAuthenticator:
    """Oracle Integration Cloud OAuth2 authenticator for Singer taps."""

    def __init__(self, auth_config: OICAuthConfig) -> None:
        """Initialize OIC authenticator with configuration."""
        self.auth_config = auth_config
        self._access_token: str | None = None
        self._token_expires_at: datetime | None = None

    def get_oauth_scopes(self) -> list[str]:
        """Get OAuth2 scopes for OIC access."""
        if self.auth_config.oauth_scope:
            return [self.auth_config.oauth_scope]
        return ["urn:opc:resource:consumer:all"]

    def get_oauth_request_body(self) -> dict[str, Any]:
        """Generate OAuth2 request body for token request."""
        return {
            "grant_type": "client_credentials",
            "scope": " ".join(self.get_oauth_scopes()),
        }

    async def get_access_token(self) -> ServiceResult[str]:
        """Get OAuth2 access token from Oracle IDCS."""
        try:
            # Check if we have a valid cached token
            if self._access_token and self._is_token_valid():
                return ServiceResult.ok(self._access_token)

            # Request new token
            token_result = await self._request_new_token()
            if token_result.is_success:
                # Cache the token
                self._access_token = token_result.data
                # Set expiration (assume 1 hour if not provided)
                self._token_expires_at = datetime.now(UTC).replace(microsecond=0)
                # Add 50 minutes (safe margin)
                import datetime as dt

                self._token_expires_at += dt.timedelta(minutes=50)

            return token_result

        except Exception as e:
            logger.exception("Failed to get OIC access token")
            return ServiceResult.fail(f"Token request failed: {e}")

    def _is_token_valid(self) -> bool:
        """Check if cached token is still valid."""
        if not self._token_expires_at:
            return False

        now = datetime.now(UTC)
        # Add small buffer (5 minutes)
        buffer_time = now.replace(microsecond=0)
        import datetime as dt

        buffer_time += dt.timedelta(minutes=5)

        return self._token_expires_at > buffer_time

    async def _request_new_token(self) -> ServiceResult[str]:
        """Request new OAuth2 token from Oracle IDCS."""
        try:
            # Prepare request
            auth = (
                self.auth_config.oauth_client_id,
                self.auth_config.oauth_client_secret.get_secret_value(),
            )

            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json",
            }

            data = self.get_oauth_request_body()

            # Add audience if provided
            if self.auth_config.oauth_client_aud:
                data["aud"] = self.auth_config.oauth_client_aud

            # Make token request
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.auth_config.oauth_token_url,
                    auth=auth,
                    headers=headers,
                    data=data,
                    timeout=30,
                )

            response.raise_for_status()
            token_data = response.json()

            access_token = token_data.get("access_token")
            if not access_token:
                return ServiceResult.fail("No access token in response")

            logger.info("Successfully obtained OIC access token")
            return ServiceResult.ok(access_token)

        except httpx.RequestError as e:
            logger.exception("OIC token request failed", error=str(e))
            return ServiceResult.fail(f"Token request failed: {e}")
        except Exception as e:
            logger.exception("Unexpected error during token request")
            return ServiceResult.fail(f"Unexpected token error: {e}")


class OICTapClient:
    """Oracle Integration Cloud API client for Singer taps."""

    def __init__(
        self,
        connection_config: OICConnectionConfig,
        authenticator: OICTapAuthenticator,
    ) -> None:
        """Initialize OIC client with configuration and authenticator."""
        self.connection_config = connection_config
        self.authenticator = authenticator
        self._session: httpx.AsyncClient | None = None

    @property
    def base_url(self) -> str:
        """Get OIC base URL."""
        return self.connection_config.base_url.rstrip("/")

    @property
    def api_version(self) -> str:
        """Get OIC API version."""
        return self.connection_config.api_version

    async def _get_authenticated_session(self) -> ServiceResult[httpx.AsyncClient]:
        """Get authenticated HTTP session."""
        try:
            if not self._session:
                # Get access token
                token_result = await self.authenticator.get_access_token()
                if not token_result.is_success:
                    return ServiceResult.fail(
                        f"Authentication failed: {token_result.error}",
                    )

                # Create session with token
                headers = {
                    "Authorization": f"Bearer {token_result.data}",
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                }

                self._session = httpx.AsyncClient(
                    headers=headers,
                    timeout=self.connection_config.timeout,
                )

            return ServiceResult.ok(self._session)

        except Exception as e:
            logger.exception("Failed to create authenticated session")
            return ServiceResult.fail(f"Session creation failed: {e}")

    async def make_request(
        self,
        method: str,
        endpoint: str,
        params: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> ServiceResult[dict[str, Any]]:
        """Make authenticated request to OIC API."""
        try:
            session_result = await self._get_authenticated_session()
            if not session_result.is_success:
                return ServiceResult.fail(session_result.error)

            session = session_result.data

            # Build full URL
            endpoint = endpoint.lstrip("/")
            url = f"{self.base_url}/ic/api/{self.api_version}/{endpoint}"

            # Make request
            response = await session.request(
                method=method,
                url=url,
                params=params,
                **kwargs,
            )

            response.raise_for_status()

            # Parse JSON response
            data = response.json()
            return ServiceResult.ok(data)

        except httpx.HTTPStatusError as e:
            logger.exception(
                "OIC API HTTP error",
                status_code=e.response.status_code,
                url=str(e.response.url),
            )
            return ServiceResult.fail(f"OIC API error: {e}")
        except httpx.RequestError as e:
            logger.exception("OIC API request failed", error=str(e))
            return ServiceResult.fail(f"Request failed: {e}")
        except Exception as e:
            logger.exception("Unexpected error in OIC API request")
            return ServiceResult.fail(f"Unexpected error: {e}")

    async def get_integrations(
        self,
        status_filter: list[str] | None = None,
        page_size: int = 100,
    ) -> ServiceResult[dict[str, Any]]:
        """Get integration flows from OIC."""
        params = {"limit": page_size}

        if status_filter:
            params["q"] = f"status in ({','.join(status_filter)})"

        return await self.make_request("GET", "integrations", params=params)

    async def get_connections(
        self,
        type_filter: list[str] | None = None,
        page_size: int = 100,
    ) -> ServiceResult[dict[str, Any]]:
        """Get adapter connections from OIC."""
        params = {"limit": page_size}

        if type_filter:
            params["q"] = f"adapterType in ({','.join(type_filter)})"

        return await self.make_request("GET", "connections", params=params)

    async def get_packages(
        self,
        page_size: int = 100,
    ) -> ServiceResult[dict[str, Any]]:
        """Get integration packages from OIC."""
        params = {"limit": page_size}
        return await self.make_request("GET", "packages", params=params)

    async def get_lookups(
        self,
        page_size: int = 100,
    ) -> ServiceResult[dict[str, Any]]:
        """Get lookup tables from OIC."""
        params = {"limit": page_size}
        return await self.make_request("GET", "lookups", params=params)

    def close(self) -> None:
        """Close the HTTP session."""
        if self._session:
            import asyncio

            asyncio.run(self._session.aclose())
            self._session = None
        logger.info("OIC client session closed")
