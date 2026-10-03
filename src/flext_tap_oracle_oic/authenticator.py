"""Oracle OIC OAuth2 authenticator.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_api import FlextApi, FlextApiSettings

from flext_tap_oracle_oic import c, p, r, t, u

if TYPE_CHECKING:
    from flext_tap_oracle_oic import FlextTapOracleOicSettings

logger = u.fetch_logger(__name__)


class FlextTapOracleOicAuthenticator:
    """Real Oracle OIC OAuth2 authenticator implementation."""

    def __init__(
        self,
        settings: FlextTapOracleOicSettings,
        api_client: FlextApi | None = None,
    ) -> None:
        """Initialize authenticator with OAuth2 configuration."""
        # NOTE (multi-agent): settings live on self; methods read
        # self.settings.TapOracleOic.* (namespaced SSOT, ADR-005).
        self.settings = settings
        self._access_token: str | None = None
        if api_client is None:
            api_config = FlextApiSettings.model_validate({})
            self._api_client: FlextApi = FlextApi(runtime_settings=api_config)
        else:
            self._api_client = api_client

    @property
    def access_token(self) -> str | None:
        """Stored OAuth2 access token."""
        return self._access_token

    @property
    def api_client(self) -> FlextApi:
        """HTTP client used for token requests."""
        return self._api_client

    def fetch_access_token(self) -> p.Result[str]:
        """Fetch an OAuth2 access token using the client credentials flow.

        Returns:
            The resulting ``p.Result[str]``.
        """

        def _run_fetch_access_token() -> p.Result[str]:
            token_request_data = "&".join(
                f"{key}={value}"
                for key, value in {
                    "grant_type": "client_credentials",
                    "client_id": self.settings.TapOracleOic.oauth_client_id,
                    "client_secret": self.settings.TapOracleOic.oauth_client_secret,
                    "audience": self.settings.TapOracleOic.oauth_audience,
                }.items()
            )
            response_result = self._api_client.post(
                self.settings.TapOracleOic.oauth_token_url,
                data=token_request_data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            if response_result.failure:
                return r[str].fail_op("OAuth2 request", response_result.error)
            response = response_result.value
            if response.status_code >= c.TapOracleOic.HTTP_ERROR_STATUS_THRESHOLD:
                return r[str].fail(
                    f"OAuth2 request failed with status {response.status_code}",
                )
            token_data: t.JsonMapping
            match response.body:
                case dict() as token_dict:
                    token_data = token_dict
                case str() as body_str:
                    token_data = t.json_mapping_adapter().validate_json(body_str)
                case _:
                    return r[str].fail("Empty or invalid OAuth response body")
            access_token = token_data.get("access_token")
            match access_token:
                case str() as access_token_str if access_token_str:
                    self._access_token = access_token_str
                    logger.info("OAuth2 access token obtained successfully")
                    return r[str].ok(access_token_str)
                case _:
                    return r[str].fail("No valid access token in response")

        try:
            return _run_fetch_access_token()
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            return r[str].fail_op("OAuth2 authentication", e)


__all__: list[str] = ["FlextTapOracleOicAuthenticator"]
