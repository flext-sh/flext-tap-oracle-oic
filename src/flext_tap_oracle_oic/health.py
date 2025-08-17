"""Oracle Integration Cloud Health Check Utilities.

This module provides health checking capabilities for OIC connections,
integrations, and the overall OIC instance health.
"""

from __future__ import annotations

from datetime import UTC, datetime

import requests

from flext_tap_oracle_oic import OAuthAuthenticator

JSON_MIME = "application/json"
# Constants
HTTP_OK = 200


class OICHealthChecker:
    """Health check utilities for Oracle Integration Cloud."""

    def __init__(self, base_url: str, authenticator: OAuthAuthenticator) -> None:
      """Initialize health checker with base URL and authenticator."""
      self.base_url = base_url.rstrip("/")
      self.authenticator = authenticator

    def _get_headers(self) -> dict[str, str]:
      headers = {
          "Accept": JSON_MIME,
          "Content-Type": JSON_MIME,
      }
      # Add auth header
      auth_headers = self.authenticator.auth_headers
      if auth_headers:
          headers.update(auth_headers)
      return headers

    def check_health(self) -> dict[str, object]:
      """Check OIC instance health."""
      try:
          # Try to access the integrations endpoint as a health check
          url = f"{self.base_url}/ic/api/integration/v1/integrations?limit=1"
          response = requests.get(url, headers=self._get_headers(), timeout=30)

          if response.status_code == HTTP_OK:
              return {
                  "status": "healthy",
                  "timestamp": datetime.now(UTC).isoformat(),
                  "instance_url": self.base_url,
                  "api_accessible": True,
                  "response_time_ms": int(response.elapsed.total_seconds() * 1000),
              }
          return {
              "status": "unhealthy",
              "timestamp": datetime.now(UTC).isoformat(),
              "instance_url": self.base_url,
              "api_accessible": False,
              "error": f"API returned status {response.status_code}",
              "response_time_ms": int(response.elapsed.total_seconds() * 1000),
          }
      except (requests.RequestException, ValueError, KeyError) as e:
          return {
              "status": "error",
              "timestamp": datetime.now(UTC).isoformat(),
              "instance_url": self.base_url,
              "api_accessible": False,
              "error": str(e),
          }

    def test_connection(self, connection_id: str) -> dict[str, object]:
      """Test specific OIC connection."""
      try:
          # Call the connection test endpoint
          url = f"{self.base_url}/ic/api/integration/v1/connections/{connection_id}/test"
          response = requests.post(url, headers=self._get_headers(), timeout=60)

          if response.status_code in {200, 202}:
              result = response.json() if response.text else {}
              return {
                  "connectionId": connection_id,
                  "status": result.get("status", "success"),
                  "timestamp": datetime.now(UTC).isoformat(),
                  "testResult": result.get(
                      "testResult",
                      "Connection test successful",
                  ),
                  "details": result.get("details", {}),
                  "response_time_ms": int(response.elapsed.total_seconds() * 1000),
              }
          return {
              "connectionId": connection_id,
              "status": "failed",
              "timestamp": datetime.now(UTC).isoformat(),
              "error": f"Test failed with status {response.status_code}",
              "details": response.text or {},
              "response_time_ms": int(response.elapsed.total_seconds() * 1000),
          }
      except (requests.RequestException, ValueError, KeyError) as e:
          return {
              "connectionId": connection_id,
              "status": "error",
              "timestamp": datetime.now(UTC).isoformat(),
              "error": str(e),
          }

    def test_integration(self, integration_id: str) -> dict[str, object]:
      """Test specific OIC integration."""
      try:
          # Get integration details
          url = f"{self.base_url}/ic/api/integration/v1/integrations/{integration_id}"
          response = requests.get(url, headers=self._get_headers(), timeout=30)

          if response.status_code == HTTP_OK:
              integration = response.json()
              status = integration.get("status", "UNKNOWN")

              # Determine health based on status
              if status == "ACTIVATED":
                  health_status = "healthy"
              elif status in {"CONFIGURED", "DRAFT"}:
                  health_status = "inactive"
              elif status in {"ERROR", "FAILED"}:
                  health_status = "unhealthy"
              else:
                  health_status = "unknown"

              return {
                  "integrationId": integration_id,
                  "name": integration.get("name"),
                  "status": status,
                  "health": health_status,
                  "timestamp": datetime.now(UTC).isoformat(),
                  "version": integration.get("version"),
                  "lastUpdated": integration.get("timeUpdated"),
                  "errorDetails": integration.get("errorDetails"),
              }
          return {
              "integrationId": integration_id,
              "health": "error",
              "timestamp": datetime.now(UTC).isoformat(),
              "error": f"Failed to get integration status: {response.status_code}",
          }
      except (requests.RequestException, ValueError, KeyError) as e:
          return {
              "integrationId": integration_id,
              "health": "error",
              "timestamp": datetime.now(UTC).isoformat(),
              "error": str(e),
          }

    def check_monitoring_health(self) -> dict[str, object]:
      """Check OIC monitoring service health."""
      try:
          # Try to access monitoring endpoint
          url = f"{self.base_url}/ic/api/monitoring/v1/instances?limit=1"
          response = requests.get(url, headers=self._get_headers(), timeout=30)

          if response.status_code == HTTP_OK:
              return {
                  "service": "monitoring",
                  "status": "healthy",
                  "timestamp": datetime.now(UTC).isoformat(),
                  "accessible": True,
                  "response_time_ms": int(response.elapsed.total_seconds() * 1000),
              }
          return {
              "service": "monitoring",
              "status": "unhealthy",
              "timestamp": datetime.now(UTC).isoformat(),
              "accessible": False,
              "error": f"API returned status {response.status_code}",
          }
      except (requests.RequestException, ValueError, KeyError) as e:
          return {
              "service": "monitoring",
              "status": "error",
              "timestamp": datetime.now(UTC).isoformat(),
              "accessible": False,
              "error": str(e),
          }
