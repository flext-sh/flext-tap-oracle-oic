"""Oracle Integration Cloud Health Check Utilities.

This module provides health checking capabilities for OIC connections,
integrations, and the overall OIC instance health.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from datetime import UTC, datetime

from flext_api import FlextApi
from flext_api.models import FlextApiModels
from flext_api.settings import FlextApiSettings
from flext_core import FlextResult

from flext_tap_oracle_oic.tap_client import (
    FlextOracleOicAuthenticator as OAuthAuthenticator,
)
from flext_tap_oracle_oic.typings import t

JSON_MIME = "application/json"
# Constants
HTTP_OK = 200


class OICHealthChecker:
    """Health check utilities for Oracle Integration Cloud."""

    def __init__(self, base_url: str, authenticator: OAuthAuthenticator) -> None:
        """Initialize health checker with base URL and authenticator."""
        self.base_url = base_url.rstrip("/")
        self.authenticator = authenticator
        api_config = FlextApiSettings(base_url=base_url)
        self._api_client = FlextApi(api_config)

    def _get_headers(self) -> dict[str, str]:
        headers = {
            "Accept": JSON_MIME,
            "Content-Type": JSON_MIME,
        }
        # Add auth header from authenticator
        token_result = self.authenticator.get_access_token()
        if token_result.is_success:
            headers["Authorization"] = f"Bearer {token_result.value}"
        return headers

    def _make_get_request(self, url: str) -> FlextResult[FlextApiModels.HttpResponse]:
        """Make authenticated GET request."""
        return self._api_client.get(
            url,
            headers=self._get_headers(),
        )

    def check_health(self) -> dict[str, t.GeneralValueType]:
        """Check OIC instance health."""
        try:
            # Try to access the integrations endpoint as a health check
            url = f"{self.base_url}/ic/api/integration/v1/integrations?limit=1"
            response_result = self._make_get_request(url)

            if response_result.is_failure:
                return {
                    "status": "error",
                    "timestamp": datetime.now(UTC).isoformat(),
                    "instance_url": self.base_url,
                    "api_accessible": "False",
                    "error": str(response_result.error),
                }

            response = response_result.value
            if response.status_code == HTTP_OK:
                return {
                    "status": "healthy",
                    "timestamp": datetime.now(UTC).isoformat(),
                    "instance_url": self.base_url,
                    "api_accessible": "True",
                }
            return {
                "status": "unhealthy",
                "timestamp": datetime.now(UTC).isoformat(),
                "instance_url": self.base_url,
                "api_accessible": "False",
                "error": f"API returned status {response.status_code}",
            }
        except Exception as e:
            return {
                "status": "error",
                "timestamp": datetime.now(UTC).isoformat(),
                "instance_url": self.base_url,
                "api_accessible": "False",
                "error": str(e),
            }

    def test_connection(self, connection_id: str) -> dict[str, t.GeneralValueType]:
        """Test specific OIC connection."""
        try:
            # Call the connection test endpoint
            url = f"{self.base_url}/ic/api/integration/v1/connections/{connection_id}/test"
            response_result = self._api_client.post(
                url,
                headers=self._get_headers(),
            )

            if response_result.is_failure:
                return {
                    "connectionId": connection_id,
                    "status": "error",
                    "timestamp": datetime.now(UTC).isoformat(),
                    "error": str(response_result.error),
                }

            response = response_result.value
            if response.status_code in {200, 202}:
                body = response.body if isinstance(response.body, dict) else {}
                status_val = str(body.get("status", "success"))
                test_result_val = str(
                    body.get("testResult", "Connection test successful")
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
                "status": "failed",
                "timestamp": datetime.now(UTC).isoformat(),
                "error": f"Test failed with status {response.status_code}",
            }
        except Exception as e:
            return {
                "connectionId": connection_id,
                "status": "error",
                "timestamp": datetime.now(UTC).isoformat(),
                "error": str(e),
            }

    def test_integration(self, integration_id: str) -> dict[str, t.GeneralValueType]:
        """Test specific OIC integration."""
        try:
            # Get integration details
            url = f"{self.base_url}/ic/api/integration/v1/integrations/{integration_id}"
            response_result = self._make_get_request(url)

            if response_result.is_failure:
                return {
                    "integrationId": integration_id,
                    "health": "error",
                    "timestamp": datetime.now(UTC).isoformat(),
                    "error": str(response_result.error),
                }

            response = response_result.value
            if response.status_code == HTTP_OK:
                integration = response.body if isinstance(response.body, dict) else {}
                status_val = str(integration.get("status", "UNKNOWN"))

                # Determine health based on status
                health_status = "unknown"
                if status_val == "ACTIVATED":
                    health_status = "healthy"
                elif status_val in {"CONFIGURED", "DRAFT"}:
                    health_status = "warning"
                elif status_val in {"ERROR", "FAILED"}:
                    health_status = "unhealthy"

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
                "health": "error",
                "timestamp": datetime.now(UTC).isoformat(),
                "error": f"Failed to get integration status: {response.status_code}",
            }
        except Exception as e:
            return {
                "integrationId": integration_id,
                "health": "error",
                "timestamp": datetime.now(UTC).isoformat(),
                "error": str(e),
            }

    def check_monitoring_health(self) -> dict[str, t.GeneralValueType]:
        """Check OIC monitoring service health."""
        try:
            # Try to access monitoring endpoint
            url = f"{self.base_url}/ic/api/monitoring/v1/instances?limit=1"
            response_result = self._make_get_request(url)

            if response_result.is_failure:
                return {
                    "service": "monitoring",
                    "status": "error",
                    "timestamp": datetime.now(UTC).isoformat(),
                    "accessible": "False",
                    "error": str(response_result.error),
                }

            response = response_result.value
            if response.status_code == HTTP_OK:
                return {
                    "service": "monitoring",
                    "status": "healthy",
                    "timestamp": datetime.now(UTC).isoformat(),
                    "accessible": "True",
                }
            return {
                "service": "monitoring",
                "status": "unhealthy",
                "timestamp": datetime.now(UTC).isoformat(),
                "accessible": "False",
                "error": f"API returned status {response.status_code}",
            }
        except Exception as e:
            return {
                "service": "monitoring",
                "status": "error",
                "timestamp": datetime.now(UTC).isoformat(),
                "accessible": "False",
                "error": str(e),
            }
