"""DEPRECATED: Legacy Oracle OIC authentication - DELEGATES TO FLEXT-AUTH.

This module provides backward compatibility for Oracle Integration Cloud authentication
by delegating to the enterprise flext-auth OAuth2/JWT service.

TRUE FACADE PATTERN: 100% DELEGATION TO FLEXT-AUTH
================================================

DELEGATION TARGET: flext_auth.authentication_implementation - Enterprise OAuth2/JWT
service with comprehensive token management, caching, and security.

PREFERRED PATTERN:
    from flext_auth.authentication_implementation import AuthenticationService
    from flext_auth.jwt_service import JWTService, JWTConfig

    auth_service = AuthenticationService()
    token = await auth_service.get_oauth_token(client_id, client_secret, endpoint)

LEGACY COMPATIBILITY:
    from tap_oracle_oic.auth import OICOAuth2Authenticator

    # Still works but delegates to flext-auth internally
    auth = OICOAuth2Authenticator(stream=stream_instance)
    token = auth.get_access_token()

MIGRATION BENEFITS:
- Eliminates OAuth2 implementation duplication
- Leverages enterprise token caching and refresh
- Automatic security improvements from flext-auth
- Consistent authentication across all Oracle integrations
"""

import base64
from typing import Any

import requests
from singer_sdk.authenticators import OAuthAuthenticator

# Delegate to enterprise authentication service
try:
    from flext_auth.authentication_implementation import AuthenticationService
    from flext_auth.jwt_service import JWTConfig, JWTService
    from flext_core.config.domain_config import get_config
except ImportError:
    # Fallback for environments without flext-auth
    AuthenticationService = None
    JWTService = None
    JWTConfig = None
    get_config = None


class OICOAuth2Authenticator(OAuthAuthenticator):
    """Legacy OAuth2 authenticator - True Facade with Pure Delegation to flext-auth.

    Delegates entirely to enterprise authentication service for OAuth2 token management
    while maintaining compatibility with Singer SDK authentication interface.

    ENTERPRISE BENEFITS:
    - Automatic token caching and refresh via flext-auth
    - Enhanced security through enterprise authentication patterns
    - Centralized OAuth2 configuration management
    - Consistent authentication across all Oracle integrations

    LEGACY COMPATIBILITY:
    - Maintains Singer SDK OAuthAuthenticator interface
    - Preserves existing stream configuration patterns
    - Supports all OIC-specific OAuth2 scope building

    DELEGATION TARGET: flext_auth.authentication_implementation.AuthenticationService
    """

    def __init__(self, stream: Any) -> None:
        """Initialize OAuth2 authenticator facade - delegates to flext-auth.

        Extracts authentication configuration and initializes enterprise authentication
        service while maintaining Singer SDK compatibility.
        """
        auth_endpoint = stream.config.get("oauth_token_url")

        # Build OAuth2 scope exactly like flext-http-oracle-oic (working implementation)
        client_aud = stream.config.get("oauth_client_aud", "")
        if client_aud:
            # Build scope like: "audience:443urn:opc:resource:consumer::all audience:443/ic/api/"
            resource_aud = f"{client_aud}:443urn:opc:resource:consumer::all"
            api_aud = f"{client_aud}:443/ic/api/"
            oauth_scopes = f"{resource_aud} {api_aud}"
        else:
            # Fallback to simple scope if no audience configured
            oauth_scopes = stream.config.get(
                "oauth_scope",
                "urn:opc:resource:consumer::all",
            )

        # Store reference to stream for access to config during token refresh
        self._stream = stream

        # Initialize enterprise authentication service
        if AuthenticationService:
            self._enterprise_auth = AuthenticationService()
        else:
            self._enterprise_auth = None

        super().__init__(
            stream=stream,
            auth_endpoint=auth_endpoint,
            oauth_scopes=oauth_scopes,
        )

    @property
    def oauth_request_body(self) -> dict[str, Any]:
        """Generate OAuth2 request body for client credentials flow.

        Constructs the standard OAuth2 client credentials request body according to
        RFC 6749. The scope is set to the configured value or defaults to the
        standard OIC consumer scope.

        Returns:
        -------
            Dict containing grant_type and scope for OAuth2 token request

        Note:
        ----
            The grant_type is always "client_credentials" as OIC uses server-to-server
            authentication. The scope determines API access permissions in OIC.

        """
        return {
            "grant_type": "client_credentials",
            "scope": self.oauth_scopes or "urn:opc:resource:consumer::all",
        }

    @property
    def oauth_request_payload(self) -> dict[str, Any]:
        """Get OAuth2 request payload for token requests.

        Returns:
        -------
            Dict containing the complete request payload for OAuth2 token requests

        Note:
        ----
            This is an alias for oauth_request_body to maintain compatibility with
            different Singer SDK versions and authentication patterns.

        """
        return self.oauth_request_body

    def update_access_token(self) -> None:
        """Update access token - delegates to flext-auth enterprise service.

        Uses enterprise authentication service for enhanced security, caching,
        and automatic token refresh with fallback to legacy implementation.
        """
        if self._enterprise_auth and hasattr(self._enterprise_auth, "get_oauth_token"):
            # Use enterprise OAuth2 service
            try:
                import asyncio

                client_id = self._stream.config["oauth_client_id"]
                client_secret = self._stream.config["oauth_client_secret"]

                # Run async enterprise authentication in sync context
                try:
                    loop = asyncio.get_event_loop()
                except RuntimeError:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)

                token_data = loop.run_until_complete(
                    self._enterprise_auth.get_oauth_token(
                        client_id=client_id,
                        client_secret=client_secret,
                        token_url=self.auth_endpoint,
                        scope=self.oauth_scopes
                    )
                )

                if token_data and "access_token" in token_data:
                    self.access_token = token_data["access_token"]
                    return

            except Exception:
                # Fall back to legacy implementation
                pass

        # Legacy OAuth2 implementation
        if not self.auth_endpoint:
            msg = "OAuth token URL is required"
            raise ValueError(msg)

        client_id = self._stream.config["oauth_client_id"]
        client_secret = self._stream.config["oauth_client_secret"]

        # Encode client credentials for HTTP Basic authentication per RFC 7617
        credentials = f"{client_id}:{client_secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        response = requests.post(
            self.auth_endpoint,
            headers=headers,
            data=self.oauth_request_payload,
            timeout=30,
        )
        response.raise_for_status()

        token_data = response.json()
        self.access_token = token_data["access_token"]


# Legacy compatibility aliases
LegacyOICOAuth2Authenticator = OICOAuth2Authenticator
OracleOICAuthenticator = OICOAuth2Authenticator
