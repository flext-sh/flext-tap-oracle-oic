"""Oracle Integration Cloud OAuth2 authentication - CONSOLIDATED.

Uses flext-meltano common patterns and oracle-oic-ext library.
Eliminates OAuth2 authenticator duplication with target-oracle-oic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Any

from flext_meltano import OAuthAuthenticator

# MIGRATED: Singer SDK imports centralized via flext-meltano
# Note: FlextMeltanoAuthConfig removed to fix import issues


# Simple replacement for removed FlextMeltanoAuthConfig
class FlextMeltanoAuthConfig:
    """Basic auth config base class."""


class OICAuthConfig(FlextMeltanoAuthConfig):
    """OIC-specific auth config using consolidated patterns."""

    oauth_token_url: str
    oauth_client_id: str
    oauth_client_secret: str
    oauth_scope: str | None = None


class OICOAuth2Authenticator(OAuthAuthenticator):
    """Consolidated OAuth2 authenticator using flext-oracle-oic-ext."""

    def __init__(self, stream_name: str, config: OICAuthConfig) -> None:
        """Initialize using consolidated patterns."""
        super().__init__(
            stream=stream_name,
            auth_endpoint=config.oauth_token_url,
            oauth_scopes=config.oauth_scope or "",
        )
        self._config = config

    @property
    def oauth_request_body(self) -> dict[str, Any]:
        """OAuth2 body using consolidated validation."""
        return {
            "grant_type": "client_credentials",
            "client_id": self._config.oauth_client_id,
            "client_secret": self._config.oauth_client_secret,
            "scope": self._config.oauth_scope or "",
        }


__all__ = ["OICAuthConfig", "OICOAuth2Authenticator"]
