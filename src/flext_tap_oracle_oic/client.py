"""Oracle Integration Cloud API client.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_api import FlextApi, FlextApiModels, FlextApiSettings

from flext_tap_oracle_oic import c, p, r, t
from flext_tap_oracle_oic.authenticator import FlextTapOracleOicAuthenticator

if TYPE_CHECKING:
    from flext_tap_oracle_oic import FlextTapOracleOicSettings


class FlextTapOracleOicClient:
    """Real Oracle Integration Cloud API client implementation."""

    def __init__(
        self,
        settings: FlextTapOracleOicSettings,
        authenticator: FlextTapOracleOicAuthenticator,
    ) -> None:
        """Initialize OIC API client."""
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
        """Make authenticated GET request to OIC API.

        Returns:
            The resulting ``p.Result[FlextApiModels.Api.HttpResponse]``.
        """
        url = (
            f"{self.settings.TapOracleOic.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        )
        headers_result = self._get_auth_headers()
        if headers_result.failure:
            return r[FlextApiModels.Api.HttpResponse].fail(
                f"Failed to get auth headers: {headers_result.error}",
            )
        try:
            response_result = self._api_client.get(url, headers=headers_result.value)
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

    def post(
        self,
        endpoint: str,
        data: t.MappingKV[str, t.JsonMapping] | None = None,
    ) -> p.Result[FlextApiModels.Api.HttpResponse]:
        """Make authenticated POST request to OIC API.

        Returns:
            The resulting ``p.Result[FlextApiModels.Api.HttpResponse]``.
        """
        url = (
            f"{self.settings.TapOracleOic.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        )
        headers_result = self._get_auth_headers()
        if headers_result.failure:
            return r[FlextApiModels.Api.HttpResponse].fail(
                f"Failed to get auth headers: {headers_result.error}",
            )
        try:
            json_body = (
                t
                .json_mapping_adapter()
                .dump_json(t.json_mapping_adapter().validate_python(data))
                .decode(c.DEFAULT_ENCODING)
                if data
                else None
            )
            response_result = self._api_client.post(
                url,
                data=json_body,
                headers=headers_result.value,
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

    def _get_auth_headers(self) -> p.Result[t.StrMapping]:
        """Build authorization headers with the OAuth2 token.

        Returns:
            The resulting ``p.Result[t.StrMapping]``.
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
