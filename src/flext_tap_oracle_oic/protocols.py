"""Singer Oracle OIC tap protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextProtocols, FlextResult


class FlextTapOracleOicProtocols(FlextProtocols):
    """Singer Oracle OIC tap protocols extending FlextProtocols with Oracle Integration Cloud interfaces.

    This class provides protocol definitions for Singer Oracle OIC tap operations including
    OIC connection management, integration flow extraction, monitoring, and cloud-specific optimizations.
    """

    @runtime_checkable
    class OicConnectionProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Oracle Integration Cloud connection operations."""

        def establish_oic_connection(
            self,
            connection_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Establish connection to Oracle Integration Cloud.

            Args:
                connection_config: OIC connection configuration

            Returns:
                FlextResult[dict[str, object]]: Connection details or error

            """

        def test_oic_connectivity(
            self, connection_config: dict[str, object]
        ) -> FlextResult[bool]:
            """Test Oracle Integration Cloud connectivity.

            Args:
                connection_config: OIC connection configuration

            Returns:
                FlextResult[bool]: Connection test result or error

            """

        def authenticate_oauth(
            self, auth_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Authenticate using OAuth for OIC access.

            Args:
                auth_config: OAuth authentication configuration

            Returns:
                FlextResult[dict[str, object]]: Authentication tokens or error

            """

        def validate_oic_credentials(
            self, connection_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Validate OIC credentials and permissions.

            Args:
                connection_config: OIC connection configuration

            Returns:
                FlextResult[dict[str, object]]: Validation results or error

            """

    @runtime_checkable
    class IntegrationDiscoveryProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Oracle Integration Cloud discovery operations."""

        def discover_integrations(
            self, discovery_config: dict[str, object]
        ) -> FlextResult[list[dict[str, object]]]:
            """Discover available OIC integrations.

            Args:
                discovery_config: Integration discovery configuration

            Returns:
                FlextResult[list[dict[str, object]]]: Discovered integrations or error

            """

        def discover_connections(
            self, discovery_config: dict[str, object]
        ) -> FlextResult[list[dict[str, object]]]:
            """Discover OIC connections and adapters.

            Args:
                discovery_config: Connection discovery configuration

            Returns:
                FlextResult[list[dict[str, object]]]: Discovered connections or error

            """

        def discover_packages(
            self, discovery_config: dict[str, object]
        ) -> FlextResult[list[dict[str, object]]]:
            """Discover OIC packages and their contents.

            Args:
                discovery_config: Package discovery configuration

            Returns:
                FlextResult[list[dict[str, object]]]: Discovered packages or error

            """

        def discover_lookups(
            self, discovery_config: dict[str, object]
        ) -> FlextResult[list[dict[str, object]]]:
            """Discover OIC lookup tables and transformations.

            Args:
                discovery_config: Lookup discovery configuration

            Returns:
                FlextResult[list[dict[str, object]]]: Discovered lookups or error

            """

    @runtime_checkable
    class DataExtractionProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Oracle Integration Cloud data extraction operations."""

        def extract_integration_data(
            self,
            integration_id: str,
            extraction_config: dict[str, object],
        ) -> FlextResult[list[dict[str, object]]]:
            """Extract data from OIC integration flows.

            Args:
                integration_id: OIC integration identifier
                extraction_config: Data extraction parameters

            Returns:
                FlextResult[list[dict[str, object]]]: Extracted integration data or error

            """

        def extract_monitoring_data(
            self,
            monitoring_config: dict[str, object],
        ) -> FlextResult[list[dict[str, object]]]:
            """Extract monitoring and tracking data from OIC.

            Args:
                monitoring_config: Monitoring data extraction parameters

            Returns:
                FlextResult[list[dict[str, object]]]: Monitoring data or error

            """

        def extract_audit_logs(
            self,
            audit_config: dict[str, object],
        ) -> FlextResult[list[dict[str, object]]]:
            """Extract audit logs from OIC.

            Args:
                audit_config: Audit log extraction parameters

            Returns:
                FlextResult[list[dict[str, object]]]: Audit log data or error

            """

        def extract_error_messages(
            self,
            error_config: dict[str, object],
        ) -> FlextResult[list[dict[str, object]]]:
            """Extract error messages and fault details from OIC.

            Args:
                error_config: Error extraction parameters

            Returns:
                FlextResult[list[dict[str, object]]]: Error message data or error

            """

    @runtime_checkable
    class CloudApiProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Oracle Integration Cloud API operations."""

        def call_management_api(
            self,
            endpoint: str,
            method: str,
            parameters: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Call OIC management API endpoints.

            Args:
                endpoint: API endpoint path
                method: HTTP method
                parameters: API call parameters

            Returns:
                FlextResult[dict[str, object]]: API response or error

            """

        def call_monitoring_api(
            self,
            endpoint: str,
            filters: dict[str, object],
        ) -> FlextResult[list[dict[str, object]]]:
            """Call OIC monitoring API endpoints.

            Args:
                endpoint: Monitoring API endpoint
                filters: Monitoring filters and parameters

            Returns:
                FlextResult[list[dict[str, object]]]: Monitoring data or error

            """

        def handle_rate_limiting(
            self, request_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Handle OIC API rate limiting and throttling.

            Args:
                request_config: Request configuration for rate limiting

            Returns:
                FlextResult[dict[str, object]]: Rate limiting status or error

            """

        def manage_pagination(
            self,
            api_config: dict[str, object],
        ) -> FlextResult[list[dict[str, object]]]:
            """Manage API response pagination for large datasets.

            Args:
                api_config: API pagination configuration

            Returns:
                FlextResult[list[dict[str, object]]]: Paginated results or error

            """

    @runtime_checkable
    class StreamGenerationProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Singer stream generation from OIC data."""

        def generate_integration_stream(
            self,
            integration_data: dict[str, object],
            stream_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Generate Singer stream for OIC integration data.

            Args:
                integration_data: OIC integration metadata
                stream_config: Stream configuration

            Returns:
                FlextResult[dict[str, object]]: Stream definition or error

            """

        def generate_monitoring_stream(
            self,
            monitoring_data: dict[str, object],
            stream_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Generate Singer stream for OIC monitoring data.

            Args:
                monitoring_data: OIC monitoring metadata
                stream_config: Stream configuration

            Returns:
                FlextResult[dict[str, object]]: Stream definition or error

            """

        def generate_audit_stream(
            self,
            audit_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Generate Singer stream for OIC audit logs.

            Args:
                audit_config: Audit stream configuration

            Returns:
                FlextResult[dict[str, object]]: Stream definition or error

            """

        def determine_extraction_method(
            self,
            integration_type: str,
            extraction_config: dict[str, object],
        ) -> FlextResult[str]:
            """Determine optimal extraction method for OIC integration type.

            Args:
                integration_type: Type of OIC integration
                extraction_config: Extraction configuration

            Returns:
                FlextResult[str]: Extraction method (API, BULK, STREAMING) or error

            """

    @runtime_checkable
    class PerformanceProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Oracle Integration Cloud performance optimization operations."""

        def optimize_api_calls(
            self, api_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Optimize OIC API calls for performance.

            Args:
                api_config: API configuration parameters

            Returns:
                FlextResult[dict[str, object]]: Optimization results or error

            """

        def configure_connection_pooling(
            self, pool_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Configure connection pooling for OIC access.

            Args:
                pool_config: Connection pooling configuration

            Returns:
                FlextResult[dict[str, object]]: Pool configuration result or error

            """

        def monitor_cloud_performance(
            self, performance_metrics: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Monitor OIC cloud performance metrics.

            Args:
                performance_metrics: Performance monitoring data

            Returns:
                FlextResult[dict[str, object]]: Performance analysis or error

            """

        def optimize_data_transfer(
            self, transfer_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Optimize data transfer from OIC cloud.

            Args:
                transfer_config: Data transfer configuration

            Returns:
                FlextResult[dict[str, object]]: Optimization results or error

            """

    @runtime_checkable
    class ValidationProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Oracle Integration Cloud data validation operations."""

        def validate_integration_status(
            self,
            integration_id: str,
            validation_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Validate OIC integration status and health.

            Args:
                integration_id: OIC integration identifier
                validation_config: Validation configuration

            Returns:
                FlextResult[dict[str, object]]: Validation results or error

            """

        def check_data_consistency(
            self,
            extracted_data: list[dict[str, object]],
            consistency_config: dict[str, object],
        ) -> FlextResult[dict[str, object]]:
            """Check consistency of extracted OIC data.

            Args:
                extracted_data: Extracted data to validate
                consistency_config: Consistency check configuration

            Returns:
                FlextResult[dict[str, object]]: Consistency check results or error

            """

        def detect_schema_changes(
            self,
            integration_data: dict[str, object],
            schema_config: dict[str, object],
        ) -> FlextResult[list[dict[str, object]]]:
            """Detect schema changes in OIC integrations.

            Args:
                integration_data: Integration data to analyze
                schema_config: Schema change detection configuration

            Returns:
                FlextResult[list[dict[str, object]]]: Detected schema changes or error

            """

        def validate_cloud_connectivity(
            self, connectivity_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Validate OIC cloud connectivity and network access.

            Args:
                connectivity_config: Connectivity validation configuration

            Returns:
                FlextResult[dict[str, object]]: Connectivity validation results or error

            """

    @runtime_checkable
    class MonitoringProtocol(FlextProtocols.Domain.Service, Protocol):
        """Protocol for Oracle Integration Cloud monitoring operations."""

        def track_extraction_metrics(
            self, extraction_id: str, metrics: dict[str, object]
        ) -> FlextResult[bool]:
            """Track OIC extraction metrics.

            Args:
                extraction_id: Extraction identifier
                metrics: Extraction metrics data

            Returns:
                FlextResult[bool]: Metric tracking success status

            """

        def monitor_integration_health(
            self, integration_id: str
        ) -> FlextResult[dict[str, object]]:
            """Monitor OIC integration health status.

            Args:
                integration_id: Integration identifier

            Returns:
                FlextResult[dict[str, object]]: Health status or error

            """

        def get_cloud_status(
            self, status_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Get OIC cloud service status.

            Args:
                status_config: Status check configuration

            Returns:
                FlextResult[dict[str, object]]: Cloud status or error

            """

        def create_monitoring_dashboard(
            self, dashboard_config: dict[str, object]
        ) -> FlextResult[dict[str, object]]:
            """Create monitoring dashboard for OIC tap operations.

            Args:
                dashboard_config: Dashboard configuration

            Returns:
                FlextResult[dict[str, object]]: Dashboard creation result or error

            """

    # Convenience aliases for easier downstream usage
    TapOracleOicConnectionProtocol = OicConnectionProtocol
    TapOracleOicIntegrationDiscoveryProtocol = IntegrationDiscoveryProtocol
    TapOracleOicDataExtractionProtocol = DataExtractionProtocol
    TapOracleOicCloudApiProtocol = CloudApiProtocol
    TapOracleOicStreamGenerationProtocol = StreamGenerationProtocol
    TapOracleOicPerformanceProtocol = PerformanceProtocol
    TapOracleOicValidationProtocol = ValidationProtocol
    TapOracleOicMonitoringProtocol = MonitoringProtocol


__all__ = [
    "FlextTapOracleOicProtocols",
]
