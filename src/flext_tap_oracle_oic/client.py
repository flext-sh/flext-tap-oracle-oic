"""Oracle Integration Cloud API client.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_api import FlextApi, FlextApiModels, FlextApiSettings

from flext_tap_oracle_oic import c, p, r, t, u

if TYPE_CHECKING:
    from flext_tap_oracle_oic import (
        FlextTapOracleOicAuthenticator,
        FlextTapOracleOicSettings,
    )


class FlextTapOracleOicClient:
    """Real Oracle Integration Cloud API client implementation."""

    def __init__(
        self,
        settings: FlextTapOracleOicSettings,
        authenticator: FlextTapOracleOicAuthenticator,
    ) -> None:
        """Initialize the OIC API client.

        Args:
            settings: Namespaced tap settings supplying the OIC base URL
                and HTTP timeout.
            authenticator: Authenticator providing the OAuth2 bearer token.


        """
        # NOTE (multi-agent): settings live on self; fetch/post read
        # self.settings.TapOracleOic.base_url (namespaced SSOT, ADR-005).
        self.settings = settings
        self.authenticator = authenticator
        api_config = FlextApiSettings.model_validate({
            "base_url": settings.TapOracleOic.base_url.rstrip("/"),
            "timeout": settings.TapOracleOic.timeout,
        })
        self._api_client = FlextApi(runtime_settings=api_config)

    def get(self, endpoint: str) -> p.Result[FlextApiModels.Api.HttpResponse]:
        """Perform an authenticated GET request to the OIC API.

        Args:
            endpoint: API path relative to the configured OIC base URL.

        Returns:
            Result succeeding with the HTTP response, or failing with the
            auth, transport, or HTTP-status error.


        """
        return self._dispatch(endpoint)

    def post(
        self,
        endpoint: str,
        data: t.MappingKV[str, t.JsonMapping] | None = None,
    ) -> p.Result[FlextApiModels.Api.HttpResponse]:
        """Perform an authenticated POST request to the OIC API.

        Args:
            endpoint: API path relative to the configured OIC base URL.
            data: Optional JSON request body mapping.

        Returns:
            Result succeeding with the HTTP response, or failing with the
            auth, transport, or HTTP-status error.


        """
        return self._dispatch(endpoint, is_post=True, body=self._encode_body(data))

    def _dispatch(
        self,
        endpoint: str,
        *,
        is_post: bool = False,
        body: str | None = None,
    ) -> p.Result[FlextApiModels.Api.HttpResponse]:
        """Send one authenticated request and normalize its outcome.

        Args:
            endpoint: API path relative to the configured OIC base URL.
            is_post: Send a POST instead of a GET request.
            body: Encoded request body for POST requests.

        Returns:
            Result succeeding with the HTTP response, or failing with the
            auth, transport, or HTTP-status error.


        """
        headers_result = self._get_auth_headers()
        if headers_result.failure:
            return r[FlextApiModels.Api.HttpResponse].fail(
                f"Failed to get auth headers: {headers_result.error}",
            )
        url = (
            f"{self.settings.TapOracleOic.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        )
        try:
            response_result = (
                self._api_client.post(url, data=body, headers=headers_result.value)
                if is_post
                else self._api_client.get(url, headers=headers_result.value)
            )
            if response_result.failure:
                return r[FlextApiModels.Api.HttpResponse].fail_op(
                    "OIC API request",
                    response_result.error,
                )
            response = response_result.value
            if response.status_code >= c.TapOracleOic.HTTP_ERROR_STATUS_THRESHOLD:
                return r[FlextApiModels.Api.HttpResponse].fail(
                    f"OIC API request failed with status {response.status_code}",
                )
            return r[FlextApiModels.Api.HttpResponse].ok(response)
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            return r[FlextApiModels.Api.HttpResponse].fail_op("OIC API request", e)

    @staticmethod
    def _encode_body(data: t.MappingKV[str, t.JsonMapping] | None) -> str | None:
        """Encode an optional JSON request body.

        Args:
            data: Optional JSON request body mapping.

        Returns:
            JSON-encoded body string, or ``None`` when no data is given.


        """
        if not data:
            return None
        return (
            u
            .json_mapping_adapter()
            .dump_json(u.json_mapping_adapter().validate_python(data))
            .decode(c.DEFAULT_ENCODING)
        )

    def _get_auth_headers(self) -> p.Result[t.StrMapping]:
        """Build the authorization headers carrying the OAuth2 bearer token.

        Returns:
            Result succeeding with the request headers, or failing when the
            access token cannot be fetched.


        """
        token_result = self.authenticator.fetch_access_token()
        if token_result.failure:
            return r[t.StrMapping].fail(
                f"Failed to fetch access token: {token_result.error}",
            )
        headers: t.MutableStrMapping = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        headers["Authorization"] = f"Bearer {token_result.value}"
        return r[t.StrMapping].ok(headers)


__all__: list[str] = ["FlextTapOracleOicClient"]
