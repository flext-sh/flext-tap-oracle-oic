"""Oracle Integration Cloud health checks.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from datetime import UTC, datetime

from flext_api import FlextApi, FlextApiModels, FlextApiSettings

from flext_tap_oracle_oic import FlextOracleOicAuthenticator, c, p, t


class FlextTapOracleOicHealthChecker:
    """Health check service for Oracle Integration Cloud."""

    def __init__(
        self, base_url: str, authenticator: FlextOracleOicAuthenticator
    ) -> None:
        """Initialize health checker with base URL and authenticator."""
        self.base_url = base_url.rstrip("/")
        self.authenticator = authenticator
        api_config = FlextApiSettings.model_validate({"base_url": base_url})
        self._api_client = FlextApi(settings=api_config)

    def check_health(self) -> t.StrMapping:
        """Check OIC instance health."""
        try:
            url = f"{self.base_url}/ic/api/integration/v1/integrations?limit=1"
            response_result = self._make_get_request(url)
            if response_result.failure:
                return {
                    "status": c.Monitoring.HealthStatus.ERROR.value,
                    "timestamp": datetime.now(UTC).isoformat(),
                    "instance_url": self.base_url,
                    "api_accessible": "False",
                    "error": str(response_result.error),
                }
            response = response_result.value
            if response.status_code == c.TapOracleOic.HTTP_OK:
                return {
                    "status": c.TapOracleOic.OicHealthStatus.HEALTHY.value,
                    "timestamp": datetime.now(UTC).isoformat(),
                    "instance_url": self.base_url,
                    "api_accessible": "True",
                }
            return {
                "status": c.TapOracleOic.OicHealthStatus.UNHEALTHY.value,
                "timestamp": datetime.now(UTC).isoformat(),
                "instance_url": self.base_url,
                "api_accessible": "False",
                "error": f"API returned status {response.status_code}",
            }
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            return {
                "status": c.Monitoring.HealthStatus.ERROR.value,
                "timestamp": datetime.now(UTC).isoformat(),
                "instance_url": self.base_url,
                "api_accessible": "False",
                "error": str(e),
            }

    def check_monitoring_health(self) -> t.StrMapping:
        """Check OIC monitoring service health."""
        try:
            url = f"{self.base_url}/ic/api/monitoring/v1/instances?limit=1"
            response_result = self._make_get_request(url)
            if response_result.failure:
                return {
                    "service": "monitoring",
                    "status": c.Monitoring.HealthStatus.ERROR.value,
                    "timestamp": datetime.now(UTC).isoformat(),
                    "accessible": "False",
                    "error": str(response_result.error),
                }
            response = response_result.value
            if response.status_code == c.TapOracleOic.HTTP_OK:
                return {
                    "service": "monitoring",
                    "status": c.TapOracleOic.OicHealthStatus.HEALTHY.value,
                    "timestamp": datetime.now(UTC).isoformat(),
                    "accessible": "True",
                }
            return {
                "service": "monitoring",
                "status": c.TapOracleOic.OicHealthStatus.UNHEALTHY.value,
                "timestamp": datetime.now(UTC).isoformat(),
                "accessible": "False",
                "error": f"API returned status {response.status_code}",
            }
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            return {
                "service": "monitoring",
                "status": c.Monitoring.HealthStatus.ERROR.value,
                "timestamp": datetime.now(UTC).isoformat(),
                "accessible": "False",
                "error": str(e),
            }

    def test_connection(self, connection_id: str) -> t.StrMapping:
        """Test specific OIC connection."""
        try:
            url = f"{self.base_url}/ic/api/integration/v1/connections/{connection_id}/test"
            response_result = self._api_client.post(url, headers=self._get_headers())
            if response_result.failure:
                return {
                    "connectionId": connection_id,
                    "status": c.TapOracleOic.OicConnectionTestStatus.ERROR.value,
                    "timestamp": datetime.now(UTC).isoformat(),
                    "error": str(response_result.error),
                }
            response = response_result.value
            if response.status_code in {200, 202}:
                body_: t.ContainerValueMapping
                match response.body:
                    case dict() as body_dict:
                        body_ = body_dict
                    case _:
                        body_ = {}
                body = body_
                status_val = str(
                    body.get(
                        "status",
                        c.TapOracleOic.OicConnectionTestStatus.SUCCESS.value,
                    ),
                )
                test_result_val = str(
                    body.get("testResult", "Connection test successful"),
                )
                details_val = body.get("details")
                return {
                    "connectionId": connection_id,
                    "status": status_val,
                    "timestamp": datetime.now(UTC).isoformat(),
                    "testResult": test_result_val,
                    "details": str(details_val) if details_val is not None else "",
                }
            return {
                "connectionId": connection_id,
                "status": c.TapOracleOic.OicConnectionTestStatus.FAILED.value,
                "timestamp": datetime.now(UTC).isoformat(),
                "error": f"Test failed with status {response.status_code}",
            }
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            return {
                "connectionId": connection_id,
                "status": c.TapOracleOic.OicConnectionTestStatus.ERROR.value,
                "timestamp": datetime.now(UTC).isoformat(),
                "error": str(e),
            }

    def test_integration(self, integration_id: str) -> t.OptionalStrMapping:
        """Test specific OIC integration."""
        try:
            url = f"{self.base_url}/ic/api/integration/v1/integrations/{integration_id}"
            response_result = self._make_get_request(url)
            if response_result.failure:
                return {
                    "integrationId": integration_id,
                    "health": c.Monitoring.HealthStatus.ERROR.value,
                    "timestamp": datetime.now(UTC).isoformat(),
                    "error": str(response_result.error),
                }
            response = response_result.value
            if response.status_code == c.TapOracleOic.HTTP_OK:
                integration_: t.ContainerValueMapping
                match response.body:
                    case dict() as integration_dict:
                        integration_ = integration_dict
                    case _:
                        integration_ = {}
                integration = integration_
                status_val = str(integration.get("status", "UNKNOWN"))
                health_status = c.TapOracleOic.OicHealthStatus.UNKNOWN.value
                if status_val == c.TapOracleOic.OicIntegrationStatus.ACTIVATED.value:
                    health_status = c.TapOracleOic.OicHealthStatus.HEALTHY.value
                elif status_val in {
                    c.TapOracleOic.OicIntegrationStatus.CONFIGURED.value,
                    c.TapOracleOic.OicIntegrationStatus.DRAFT.value,
                }:
                    health_status = c.TapOracleOic.OicHealthStatus.WARNING.value
                elif status_val in {
                    c.TapOracleOic.OicIntegrationStatus.ERROR.value,
                    c.TapOracleOic.OicIntegrationStatus.FAILED.value,
                }:
                    health_status = c.TapOracleOic.OicHealthStatus.UNHEALTHY.value
                name_val = integration.get("name")
                version_val = integration.get("version")
                last_updated_val = integration.get("timeUpdated")
                error_details_val = integration.get("errorDetails")
                return {
                    "integrationId": integration_id,
                    "name": str(name_val) if name_val is not None else None,
                    "status": status_val,
                    "health": health_status,
                    "timestamp": datetime.now(UTC).isoformat(),
                    "version": str(version_val) if version_val is not None else None,
                    "lastUpdated": str(last_updated_val)
                    if last_updated_val is not None
                    else None,
                    "errorDetails": str(error_details_val)
                    if error_details_val is not None
                    else None,
                }
            return {
                "integrationId": integration_id,
                "health": c.Monitoring.HealthStatus.ERROR.value,
                "timestamp": datetime.now(UTC).isoformat(),
                "error": f"Failed to get integration status: {response.status_code}",
            }
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as e:
            return {
                "integrationId": integration_id,
                "health": c.Monitoring.HealthStatus.ERROR.value,
                "timestamp": datetime.now(UTC).isoformat(),
                "error": str(e),
            }

    def _get_headers(self) -> t.StrMapping:
        headers = {
            "Accept": c.TapOracleOic.JSON_MIME,
            "Content-Type": c.TapOracleOic.JSON_MIME,
        }
        token_result = self.authenticator.get_access_token()
        if token_result.success:
            headers["Authorization"] = f"Bearer {token_result.value}"
        return headers

    def _make_get_request(self, url: str) -> p.Result[FlextApiModels.Api.HttpResponse]:
        """Make authenticated GET request."""
        return self._api_client.get(url, headers=self._get_headers())


__all__: list[str] = ["FlextTapOracleOicHealthChecker"]
