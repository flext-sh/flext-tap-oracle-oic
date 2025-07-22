"""Oracle Integration Cloud OAuth2 authentication.

Refactored to use centralized patterns from flext-core.
Eliminates code duplication across Oracle OIC projects.
"""

from __future__ import annotations

from typing import Any

from singer_sdk.authenticators import OAuthAuthenticator

from flext_tap_oracle_oic.oic_config import (
    OICAuthConfig,
    OICTapAuthenticator,
)


class OICOAuth2Authenticator(OAuthAuthenticator):
    """Oracle Integration Cloud OAuth2 authenticator using centralized patterns.

    Refactored to use flext-core centralized authentication patterns.
    Eliminates code duplication while maintaining Singer SDK compatibility.
    """

    def __init__(self, stream: Any) -> None:
        """Initialize authenticator using centralized OIC patterns."""
        auth_endpoint = stream.config.get("oauth_token_url") or stream.config.get(
            "oauth_endpoint",
        )

        # Handle missing oauth_token_url gracefully
        if not auth_endpoint:
            auth_endpoint = (
                "https://placeholder.identity.oraclecloud.com/oauth2/v1/token"
            )

        # Create centralized auth config
        auth_config = OICAuthConfig(
            oauth_client_id=stream.config.get("oauth_client_id", ""),
            oauth_client_secret=stream.config.get("oauth_client_secret", ""),
            oauth_token_url=auth_endpoint,
            oauth_client_aud=stream.config.get("oauth_client_aud"),
            oauth_scope=stream.config.get("oauth_scope", ""),
        )

        # Use centralized authenticator
        self._central_auth = OICTapAuthenticator(auth_config)

        # Build OAuth2 scopes using centralized logic
        oauth_scopes = self._central_auth.get_oauth_scopes()

        # Store reference to stream for Singer SDK compatibility
        self._stream = stream

        super().__init__(
            stream=stream,
            auth_endpoint=auth_endpoint,
            oauth_scopes=oauth_scopes,
        )

    @property
    def oauth_request_body(self) -> dict[str, Any]:
        """Generate OAuth2 request body using centralized patterns.

        Returns:
            Dict containing grant_type and scope for OAuth2 token request

        """
        return self._central_auth.get_oauth_request_body()

    @property
    def oauth_request_payload(self) -> dict[str, Any]:
        """Get OAuth2 request payload for token endpoint.

        Returns:
            Dictionary containing OAuth2 request body parameters.

        """
        return self.oauth_request_body

    def update_access_token(self) -> None:
        """Update access token using centralized OAuth2 implementation.

        Uses centralized OIC authentication patterns from flext-core.
        """
        if not self.auth_endpoint:
            error_msg = "OAuth token URL not configured"
            raise ValueError(error_msg)

        # Use centralized authentication
        token_result = self._central_auth.get_access_token()
        if not token_result.success:
            msg = f"Authentication failed: {token_result.error}"
            raise ValueError(msg)

        self.access_token = token_result.data


# Legacy compatibility aliases
LegacyOICOAuth2Authenticator = OICOAuth2Authenticator
OracleOICAuthenticator = OICOAuth2Authenticator
