# CLAUDE.md - FLEXT Tap Oracle OIC Quality Refactoring Guide

**Project**: FLEXT Tap Oracle OIC - Enterprise Oracle Integration Cloud Extraction  
**Status**: Quality Refactoring Required · 1.0.0 Release Preparation | **Architecture**: Clean Architecture + DDD  
**Dependencies**: Python 3.13+, flext-core, flext-oracle-oic-ext, flext-meltano, singer-sdk  
**Coverage Target**: 75% minimum (proven achievable), 100% aspirational target | **Current Type Status**: Requires Assessment
**Authority**: FLEXT-TAP-ORACLE-OIC | **Last Updated**: 2025-01-08

**Hierarchy**: This document provides project-specific standards based on workspace-level patterns defined in [../CLAUDE.md](../CLAUDE.md). For architectural principles, quality gates, and MCP server usage, reference the main workspace standards.

## 📋 DOCUMENT STRUCTURE & REFERENCES

**Quick Links**:
- **[~/.claude/commands/flext.md](~/.claude/commands/flext.md)**: Optimization command for module refactoring (USE with `/flext` command)
- **[../CLAUDE.md](../CLAUDE.md)**: FLEXT ecosystem standards and domain library rules

**CRITICAL INTEGRATION DEPENDENCIES**:
- **flext-meltano**: MANDATORY for ALL Singer operations (ZERO TOLERANCE for direct singer-sdk without flext-meltano)
- **flext-oracle-oic-ext**: MANDATORY for ALL Oracle OIC operations (ZERO TOLERANCE for direct OAuth2/httpx imports)
- **flext-core**: Foundation patterns (FlextResult, FlextService, FlextContainer)

## 🔗 MCP SERVER INTEGRATION (MANDATORY)

| MCP Server              | Purpose                                                         | Status          |
| ----------------------- | --------------------------------------------------------------- | --------------- |
| **serena-flext**        | Semantic code analysis, symbol manipulation, refactoring        | **MANDATORY**   |
| **sequential-thinking** | Oracle OIC data processing and Singer protocol architecture     | **RECOMMENDED** |
| **context7**            | Third-party library documentation (Singer SDK, Oracle OIC)      | **RECOMMENDED** |
| **github**              | Repository operations and Singer ecosystem PRs                  | **ACTIVE**      |

**Usage**: `claude mcp list` for available servers, leverage for Singer-specific development patterns and Oracle OIC extraction analysis.

---

## 🎯 PROJECT MISSION STATEMENT

Transform FLEXT Tap Oracle OIC into a **production-ready, enterprise-grade Oracle Integration Cloud extraction tap** implementing Singer protocol with zero tolerance quality standards. This tap provides comprehensive OIC entity extraction with OAuth2/IDCS authentication, intelligent error recovery, and seamless integration with the broader FLEXT ecosystem.

### 🏆 SUCCESS CRITERIA (EVIDENCE-BASED VALIDATION)

- **✅ 90% Test Coverage**: Real functional tests with comprehensive OIC API scenarios (measured via `pytest --cov=src --cov-report=term`)
- **✅ Zero Tolerance Quality**: MyPy strict + Ruff ALL rules + Bandit security (measured via `make validate`)
- **✅ Singer Protocol Compliance**: Full catalog discovery + data extraction working (verified via `make discover && make run`)
- **✅ OIC Authentication Excellence**: OAuth2/IDCS flow with automatic token refresh (verified via `make oic-auth`)
- **✅ Stream Consolidation**: Single source of truth for all OIC entity streams (verified via architecture review)

---

## 🚫 PROJECT PROHIBITIONS (ZERO TOLERANCE ENFORCEMENT)

### ⛔ ABSOLUTELY FORBIDDEN ACTIONS

1. **Quality Degradation**:
   - NEVER reduce test coverage below 90%
   - NEVER suppress MyPy/Ruff errors without proper resolution
   - NEVER disable security scanning (Bandit/pip-audit)
   - NEVER compromise Singer protocol compliance

2. **Architectural Violations**:
   - NEVER bypass Clean Architecture layer boundaries
   - NEVER duplicate functionality available in flext-oracle-oic-ext
   - NEVER create circular dependencies between layers
   - NEVER ignore FlextResult pattern for error handling

3. **OIC Integration Violations**:
   - NEVER implement OAuth2 authentication from scratch (use flext-oracle-oic-ext)
   - NEVER hardcode OIC API endpoints or configuration
   - NEVER ignore API rate limiting and error handling
   - NEVER bypass OIC security and authentication requirements

4. **Singer Protocol Violations**:
   - NEVER return data without proper Singer RECORD messages
   - NEVER skip catalog discovery implementation
   - NEVER ignore incremental replication patterns for monitoring streams
   - NEVER create non-compliant stream schemas

---

## 🏗️ PROJECT ARCHITECTURE (CURRENT STATE ANALYSIS REQUIRED)

### Core Architecture Layers

```python
# FLEXT Tap Oracle OIC follows Clean Architecture with infrastructure reuse
src/flext_tap_oracle_oic/
   domain/                    # Core business logic (OIC entities)
      entities.py             # Domain entities: Integration, Connection, Package, Activity
   application/               # Application services (orchestration layer)
      services.py             # Business logic with FlextResult pattern
   infrastructure/            # External integrations (OIC API, OAuth2, file system)
   tap.py                     # Main TapOracleOIC class (Singer SDK implementation)
   streams.py                 # Consolidated streams with single source of truth
   config.py                  # Configuration models with Pydantic validation
   client.py                  # OIC API client with OAuth2 authentication
   auth.py                    # Authentication handling with token management
```

### Service Architecture Pattern (MANDATORY)

```python
class FlextTapOracleOicService(FlextDomainService):
    """Single unified service class following flext-core patterns.

    This class consolidates all Oracle OIC tap-related operations,
    leveraging flext-oracle-oic-ext infrastructure while maintaining
    a unified interface for OIC entity extraction.
    """

    def __init__(self, **data) -> None:
        """Initialize service with proper dependency injection."""
        super().__init__(**data)
        self._container = FlextContainer.get_global()
        self._logger = FlextLogger(__name__)
        self._oic_client = self._container.get(OicApiClient)  # From flext-oracle-oic-ext

    def extract_integrations(self, config: dict) -> FlextResult[list[dict]]:
        """Extract OIC integrations with comprehensive error handling."""
        if not config or not config.get("base_url"):
            return FlextResult[list[dict]].fail("Configuration with base_url is required")

        try:
            # Authenticate using flext-oracle-oic-ext
            auth_result = self._oic_client.authenticate(
                client_id=config["oauth_client_id"],
                client_secret=config["oauth_client_secret"],
                token_url=config["oauth_token_url"],
                audience=config["oauth_client_aud"]
            )

            if auth_result.is_failure:
                return FlextResult[list[dict]].fail(f"OIC authentication failed: {auth_result.error}")

            # Extract integrations with pagination
            extraction_result = self._oic_client.get_integrations_paginated(
                page_size=config.get("page_size", 100),
                include_extended=config.get("include_extended", False)
            )

            if extraction_result.is_success:
                return FlextResult[list[dict]].ok(extraction_result.value)
            else:
                return FlextResult[list[dict]].fail(f"Integration extraction failed: {extraction_result.error}")

        except Exception as e:
            self._logger.error(f"OIC integration extraction error: {e}")
            return FlextResult[list[dict]].fail(f"OIC extraction error: {str(e)}")

    def extract_connections(self, config: dict) -> FlextResult[list[dict]]:
        """Extract OIC connections with security considerations."""
        try:
            # Use authenticated client for connection extraction
            connections_result = self._oic_client.get_connections_paginated(
                page_size=config.get("page_size", 100),
                include_sensitive_data=False  # Never expose credentials
            )

            if connections_result.is_success:
                # Sanitize sensitive information
                sanitized_connections = self._sanitize_connection_data(connections_result.value)
                return FlextResult[list[dict]].ok(sanitized_connections)
            else:
                return FlextResult[list[dict]].fail(f"Connection extraction failed: {connections_result.error}")

        except Exception as e:
            self._logger.error(f"OIC connection extraction error: {e}")
            return FlextResult[list[dict]].fail(f"Connection extraction error: {str(e)}")

    def extract_monitoring_data(
        self,
        config: dict,
        stream_type: str,
        start_date: Optional[str] = None
    ) -> FlextResult[Iterator[dict]]:
        """Extract OIC monitoring data with incremental support."""
        try:
            # For monitoring streams (activity, metrics, tracking, alerts)
            monitoring_result = self._oic_client.get_monitoring_data(
                stream_type=stream_type,
                start_date=start_date,
                page_size=config.get("page_size", 100),
                include_detailed_metrics=config.get("include_extended", False)
            )

            if monitoring_result.is_success:
                return FlextResult[Iterator[dict]].ok(monitoring_result.value)
            else:
                return FlextResult[Iterator[dict]].fail(f"Monitoring data extraction failed: {monitoring_result.error}")

        except Exception as e:
            self._logger.error(f"OIC monitoring extraction error: {e}")
            return FlextResult[Iterator[dict]].fail(f"Monitoring extraction error: {str(e)}")

    def _sanitize_connection_data(self, connections: list[dict]) -> list[dict]:
        """Sanitize connection data to remove sensitive information."""
        sanitized = []
        for conn in connections:
            sanitized_conn = conn.copy()
            # Remove sensitive fields
            sensitive_fields = ["password", "clientSecret", "privateKey", "certificateData"]
            for field in sensitive_fields:
                sanitized_conn.pop(field, None)
            # Mark as sanitized
            sanitized_conn["_data_sanitized"] = True
            sanitized.append(sanitized_conn)
        return sanitized

    def validate_configuration(self, config: dict) -> FlextResult[bool]:
        """Validate tap configuration with business rules."""
        # Implementation with comprehensive validation
        required_fields = ["base_url", "oauth_client_id", "oauth_client_secret", "oauth_token_url", "oauth_client_aud"]
        for field in required_fields:
            if not config.get(field):
                return FlextResult[bool].fail(f"Required configuration field missing: {field}")

        return FlextResult[bool].ok(True)
```

---

## ⚡ IMPLEMENTATION STRATEGY (PRIORITY-BASED EXECUTION)

### Phase 1: Foundation Assessment & Repair (MANDATORY FIRST)

#### 1.1 Current State Discovery (INVESTIGATE FIRST)

```bash
# MANDATORY: Complete ecosystem understanding
find flext-core/src -name "*.py" -exec grep -l "FlextDomainService\|FlextResult\|FlextContainer" {} \;
# Read EVERY file that shows up - understand what's available

# Map flext-oracle-oic-ext integration capabilities
grep -r "from flext_oracle_oic_ext" src/ --include="*.py" | cut -d: -f2 | sort | uniq
# Understand current OIC client integration patterns

# Check current Singer SDK integration
python -c "from flext_tap_oracle_oic import TapOracleOIC; help(TapOracleOIC.discover_streams)"
# Verify current API compatibility

# Count current test coverage
pytest --cov=src --cov-report=term | grep "TOTAL"
# Get baseline coverage before improvements

# Map current failure patterns
pytest --tb=no -q | tail -1 | grep -oE "[0-9]+ failed"
# Understand current test landscape
```

#### 1.2 Quality Gate Assessment

```bash
# Type checking status
mypy src/ --strict --show-error-codes 2>&1 | wc -l
# Count current type errors (target: 0)

# Linting status
ruff check src/ --statistics | grep "errors"
# Count current linting errors (target: 0)

# Security scan
bandit -r src/ -f json 2>/dev/null | jq '.metrics._totals' || echo "Security scan needed"
# Assess security status

# Singer protocol compliance
make discover 2>&1 | grep -E "ERROR|FAILED" | wc -l
# Test current Singer compliance
```

### Phase 2: Service Architecture & Stream Consolidation (CONSOLIDATION FOCUS)

#### 2.1 Stream Consolidation Excellence

```python
# Consolidated streams implementation (SINGLE SOURCE OF TRUTH)
class OICBaseStream(Stream):
    """Base class for all OIC data streams with unified functionality."""

    def __init__(self, tap: TapOracleOIC, name: str, **kwargs):
        """Initialize OIC stream with authentication and pagination."""
        super().__init__(tap, name, **kwargs)
        self._service = self._container.get(FlextTapOracleOicService)
        self._config = tap.config.model_dump()

    def get_records(self, context: dict | None) -> Iterable[dict[str, object]]:
        """Base record extraction with error handling and authentication."""
        # Implemented by subclasses with specific OIC entity logic
        raise NotImplementedError("Subclasses must implement get_records")

    def request_records(self, context: dict | None) -> Iterator[dict]:
        """Make authenticated request with retry logic and rate limiting."""
        # Common request pattern for all OIC streams
        # Handles authentication, pagination, rate limiting, error recovery
        pass

# Consolidated stream definitions
class IntegrationsStream(OICBaseStream):
    """OIC integrations stream with comprehensive metadata extraction."""

    name = "integrations"
    primary_keys = ["id"]
    replication_key = "lastUpdated"

    def get_records(self, context: dict | None) -> Iterable[dict[str, object]]:
        result = self._service.extract_integrations(self._config)
        if result.is_success:
            for integration in result.value:
                yield self._transform_integration_record(integration)
        else:
            raise RuntimeError(f"Integration extraction failed: {result.error}")

class ConnectionsStream(OICBaseStream):
    """OIC connections stream with security sanitization."""

    name = "connections"
    primary_keys = ["id"]
    replication_key = "lastUpdated"

    def get_records(self, context: dict | None) -> Iterable[dict[str, object]]:
        result = self._service.extract_connections(self._config)
        if result.is_success:
            for connection in result.value:
                yield self._transform_connection_record(connection)
        else:
            raise RuntimeError(f"Connection extraction failed: {result.error}")

# Monitoring streams with incremental replication
class ActivityStream(OICBaseStream):
    """OIC activity stream with incremental replication."""

    name = "activity"
    primary_keys = ["id"]
    replication_key = "timestamp"
    replication_method = "INCREMENTAL"

    def get_records(self, context: dict | None) -> Iterable[dict[str, object]]:
        start_date = self._get_starting_timestamp(context)
        result = self._service.extract_monitoring_data(self._config, "activity", start_date)
        if result.is_success:
            for activity in result.value:
                yield self._transform_activity_record(activity)
        else:
            raise RuntimeError(f"Activity extraction failed: {result.error}")
```

#### 2.2 OAuth2/IDCS Authentication Excellence

```python
class OICAuthenticationManager:
    """Enhanced OAuth2/IDCS authentication with comprehensive error handling."""

    def __init__(self, container: FlextContainer):
        self._container = container
        self._oic_client = container.get(OicApiClient)  # From flext-oracle-oic-ext
        self._logger = FlextLogger(__name__)
        self._token_cache = {}
        self._token_expiry = {}

    def authenticate_with_retry(self, config: dict) -> FlextResult[str]:
        """Authenticate with automatic retry and token caching."""
        cache_key = self._generate_cache_key(config)

        # Check cached token
        if self._is_token_valid(cache_key):
            return FlextResult[str].ok(self._token_cache[cache_key])

        # Perform authentication with retry logic
        max_retries = config.get("max_retries", 3)
        for attempt in range(max_retries + 1):
            auth_result = self._oic_client.authenticate(
                client_id=config["oauth_client_id"],
                client_secret=config["oauth_client_secret"],
                token_url=config["oauth_token_url"],
                audience=config["oauth_client_aud"]
            )

            if auth_result.is_success:
                # Cache successful authentication
                token = auth_result.value["access_token"]
                expires_in = auth_result.value.get("expires_in", 3600)
                self._cache_token(cache_key, token, expires_in)
                return FlextResult[str].ok(token)

            if attempt < max_retries:
                # Exponential backoff for retries
                wait_time = 2 ** attempt
                self._logger.warning(f"Authentication attempt {attempt + 1} failed, retrying in {wait_time}s")
                time.sleep(wait_time)

        return FlextResult[str].fail(f"Authentication failed after {max_retries + 1} attempts")
```

### Phase 3: Singer Protocol & OIC API Excellence (PROTOCOL COMPLIANCE)

#### 3.1 Dynamic Schema Discovery

```python
def discover_oic_schemas(self, config: dict) -> dict:
    """Discover OIC entity schemas dynamically from API metadata."""
    try:
        # Get sample data from each stream type
        stream_schemas = {}

        # Core business streams
        business_streams = ["integrations", "connections", "packages", "agents"]
        for stream_name in business_streams:
            sample_result = self._service.get_sample_data(config, stream_name, limit=5)
            if sample_result.is_success:
                schema = self._generate_schema_from_samples(stream_name, sample_result.value)
                stream_schemas[stream_name] = schema

        # Infrastructure streams
        infra_streams = ["libraries", "certificates", "adapters", "recipes"]
        for stream_name in infra_streams:
            sample_result = self._service.get_sample_data(config, stream_name, limit=5)
            if sample_result.is_success:
                schema = self._generate_schema_from_samples(stream_name, sample_result.value)
                stream_schemas[stream_name] = schema

        # Monitoring streams (with incremental replication)
        monitoring_streams = ["activity", "metrics", "tracking", "alerts"]
        for stream_name in monitoring_streams:
            sample_result = self._service.get_sample_data(config, stream_name, limit=5)
            if sample_result.is_success:
                schema = self._generate_schema_from_samples(stream_name, sample_result.value)
                schema["replication_method"] = "INCREMENTAL"
                schema["replication_key"] = self._get_replication_key_for_stream(stream_name)
                stream_schemas[stream_name] = schema

        return stream_schemas

    except Exception as e:
        self._logger.error(f"Schema discovery failed: {e}")
        return self._get_default_schemas()

def _generate_schema_from_samples(self, stream_name: str, samples: list[dict]) -> dict:
    """Generate Singer schema from OIC API sample data."""
    properties = {
        "id": {"type": "string", "description": "OIC entity unique identifier"},
        "lastUpdated": {"type": "string", "format": "date-time", "description": "Last update timestamp"}
    }

    # Analyze sample data for additional properties
    for sample in samples:
        for field_name, field_value in sample.items():
            if field_name not in properties:
                properties[field_name] = self._infer_field_schema(field_value)

    return {
        "type": "object",
        "properties": properties,
        "required": ["id"],
        "additionalProperties": True
    }
```

#### 3.2 Error Recovery & Rate Limiting

```python
class OICApiErrorHandler:
    """Comprehensive error handling for OIC API interactions."""

    ERROR_STRATEGIES = {
        401: "refresh_token_and_retry",      # Unauthorized - refresh OAuth token
        429: "rate_limit_backoff",           # Rate limited - exponential backoff
        500: "server_error_retry",           # Server error - retry with backoff
        503: "service_unavailable_retry",    # Service unavailable - retry
        404: "entity_not_found_skip",        # Entity not found - skip and continue
        403: "permission_denied_fail"        # Forbidden - fail permanently
    }

    def handle_api_error(self, error_code: int, error_details: dict, config: dict) -> FlextResult[str]:
        """Handle API errors with appropriate recovery strategies."""
        strategy = self.ERROR_STRATEGIES.get(error_code, "unknown_error_fail")

        if strategy == "refresh_token_and_retry":
            return self._refresh_token_and_retry(error_details, config)
        elif strategy == "rate_limit_backoff":
            return self._handle_rate_limiting(error_details, config)
        elif strategy == "server_error_retry":
            return self._handle_server_error(error_details, config)
        elif strategy == "entity_not_found_skip":
            return FlextResult[str].ok("SKIP")  # Signal to skip this entity
        else:
            return FlextResult[str].fail(f"Unrecoverable API error: {error_code} - {error_details}")
```

### Phase 4: Integration Testing Excellence (REAL OIC TESTING)

#### 4.1 Comprehensive Test Suite

```python
@pytest.mark.integration
def test_oic_authentication_flow():
    """Test complete OAuth2/IDCS authentication flow."""
    # Test token acquisition
    # Test token refresh
    # Test token caching
    # Test authentication failure scenarios
    pass

@pytest.mark.integration
def test_oic_stream_extraction():
    """Test data extraction from all OIC stream types."""
    # Test integrations stream
    # Test connections stream (with sanitization)
    # Test monitoring streams (with incremental replication)
    # Test error handling and recovery
    pass

@pytest.mark.performance
def test_large_oic_environment():
    """Test performance with enterprise-scale OIC environment."""
    # Test with 1000+ integrations
    # Test pagination performance
    # Test memory usage
    # Test concurrent stream processing
    pass

@pytest.mark.security
def test_data_sanitization():
    """Test security and data sanitization."""
    # Test connection data sanitization
    # Test credential scrubbing
    # Test sensitive data handling
    # Test audit trail compliance
    pass
```

---

## 🔧 ESSENTIAL COMMANDS (DAILY DEVELOPMENT)

### Quality Gates (MANDATORY BEFORE ANY COMMIT)

```bash
# NEVER SKIP: Complete validation pipeline
make validate                # lint + type + security + test (90% coverage)

# Quick validation during development
make check                   # lint + type-check + test

# Individual quality components
make lint                    # Ruff linting (ALL rules enabled)
make type-check              # MyPy strict mode validation
make security                # Bandit + pip-audit security scanning
make format                  # Auto-format code with Ruff
```

### Singer Tap Operations

```bash
# Essential Singer protocol operations
make discover                # Generate catalog.json from OIC API discovery
make run                     # Run tap extraction with config + catalog
make validate-config         # Validate tap configuration JSON

# OIC-specific testing
make oic-test                # Test OIC API connectivity and authentication
make oic-auth                # Test OAuth2/IDCS authentication flow
make oic-endpoints           # List available OIC API endpoints
```

### Testing Strategy (90% COVERAGE TARGET)

```bash
# Comprehensive testing approach
make test                    # All tests with 90% coverage requirement
make test-unit               # Unit tests only (exclude integration)
make test-integration        # Integration tests with real OIC API
make test-singer             # Singer protocol compliance tests
make coverage-html           # Generate HTML coverage report for analysis

# OIC-specific testing
pytest -m auth               # Authentication tests
pytest -m oic                # OIC-specific functionality tests
pytest -m security           # Security and data sanitization tests
pytest -m "not slow"         # Fast tests for quick feedback loop
```

### OIC Development Environment

```bash
# Configuration setup
export OIC_BASE_URL="https://your-instance.integration.ocp.oraclecloud.com"
export OIC_CLIENT_ID="your_oauth_client_id"
export OIC_CLIENT_SECRET="your_oauth_client_secret"
export OIC_TOKEN_URL="https://idcs-tenant.identity.oraclecloud.com/oauth2/v1/token"
export OIC_AUDIENCE="https://your-instance.integration.ocp.oraclecloud.com:443/urn:opc:resource:consumer::all"

# Test authentication and discovery
poetry run tap-oracle-oic --config config.json --discover > catalog.json
poetry run tap-oracle-oic --config config.json --catalog catalog.json --state state.json
```

---

## 📊 SUCCESS METRICS (EVIDENCE-BASED MEASUREMENT)

### Code Quality Metrics (AUTOMATED VALIDATION)

```bash
# Coverage measurement (TARGET: 90%)
pytest --cov=src --cov-report=term | grep "TOTAL" | awk '{print $4}'

# Type safety assessment (TARGET: 0 errors)
mypy src/ --strict --show-error-codes 2>&1 | wc -l

# Linting compliance (TARGET: 0 errors)
ruff check src/ --statistics | grep -o "[0-9]\+ errors"

# Security assessment (TARGET: 0 critical vulnerabilities)
bandit -r src/ -f json 2>/dev/null | jq '.metrics._totals.SEVERITY_RISK_HIGH' || echo 0
```

### Singer Protocol Compliance (FUNCTIONAL VALIDATION)

```bash
# Catalog discovery success
make discover >/dev/null 2>&1 && echo "✅ Discovery OK" || echo "❌ Discovery FAILED"

# Data extraction success
make run >/dev/null 2>&1 && echo "✅ Extraction OK" || echo "❌ Extraction FAILED"

# Schema validation
singer-check-tap --catalog catalog.json < /dev/null && echo "✅ Schema OK" || echo "❌ Schema FAILED"
```

### OIC Integration Functionality (DOMAIN-SPECIFIC VALIDATION)

```bash
# OIC authentication test
make oic-auth >/dev/null 2>&1 && echo "✅ OIC Auth OK" || echo "❌ OIC Auth FAILED"

# OIC API connectivity test
make oic-test >/dev/null 2>&1 && echo "✅ OIC API OK" || echo "❌ OIC API FAILED"

# flext-oracle-oic-ext integration test
python -c "
from flext_oracle_oic_ext import OicApiClient
from flext_core import FlextContainer
client = FlextContainer.get_global().get(OicApiClient)
print('✅ OIC client integration OK')
" && echo "OIC integration OK"

# Stream consolidation validation
python -c "
from flext_tap_oracle_oic import TapOracleOIC
tap = TapOracleOIC({})
streams = list(tap.discover_streams())
print(f'✅ {len(streams)} consolidated streams discovered')
" && echo "Stream consolidation OK"
```

---

## 🔍 PROJECT-SPECIFIC CONTEXT (OIC DOMAIN EXPERTISE)

### Oracle Integration Cloud (OIC) Integration Excellence

#### OIC API Entities and Relationships

```python
OIC_ENTITY_MODEL = {
    # Core Business Entities
    "integrations": {
        "description": "Integration definitions and configurations",
        "primary_key": "id",
        "replication_key": "lastUpdated",
        "relationships": ["connections", "packages", "libraries"],
        "security_level": "standard"
    },
    "connections": {
        "description": "Connection configurations and credentials",
        "primary_key": "id",
        "replication_key": "lastUpdated",
        "relationships": ["adapters", "certificates"],
        "security_level": "high",  # Contains sensitive data
        "sanitization_required": True
    },
    "packages": {
        "description": "Integration packages and versions",
        "primary_key": "id",
        "replication_key": "version",
        "relationships": ["integrations", "libraries"],
        "security_level": "standard"
    },

    # Infrastructure Entities
    "agents": {
        "description": "OIC agents and connectivity agents",
        "primary_key": "id",
        "replication_key": "lastHeartbeat",
        "relationships": ["connections"],
        "security_level": "standard"
    },
    "libraries": {
        "description": "Shared libraries and schemas",
        "primary_key": "id",
        "replication_key": "lastUpdated",
        "relationships": ["integrations", "packages"],
        "security_level": "standard"
    },
    "certificates": {
        "description": "Security certificates and keystores",
        "primary_key": "id",
        "replication_key": "expiryDate",
        "relationships": ["connections"],
        "security_level": "high",
        "sanitization_required": True
    },

    # Monitoring Entities (Incremental Replication)
    "activity": {
        "description": "Integration activity and execution logs",
        "primary_key": "id",
        "replication_key": "timestamp",
        "replication_method": "INCREMENTAL",
        "relationships": ["integrations"],
        "security_level": "standard",
        "retention_policy": "90_days"
    },
    "metrics": {
        "description": "Performance metrics and statistics",
        "primary_key": "id",
        "replication_key": "timestamp",
        "replication_method": "INCREMENTAL",
        "relationships": ["integrations", "activity"],
        "security_level": "standard",
        "retention_policy": "30_days"
    }
}
```

#### OAuth2/IDCS Authentication Patterns

```python
class OICAuthenticationConfig:
    """OIC authentication configuration patterns and requirements."""

    IDCS_OAUTH2_FLOW = {
        "grant_type": "client_credentials",
        "scope": "https://your-instance.integration.ocp.oraclecloud.com:443/urn:opc:resource:consumer::all",
        "token_endpoint": "https://idcs-tenant.identity.oraclecloud.com/oauth2/v1/token",
        "content_type": "application/x-www-form-urlencoded",
        "authorization": "Basic <base64(client_id:client_secret)>"
    }

    REQUIRED_OIC_PERMISSIONS = [
        "OIC_INTEGRATION_ADMIN",      # Read integrations and configurations
        "OIC_MONITORING_ADMIN",       # Read activity streams and metrics
        "OIC_CONNECTION_ADMIN",       # Read connection configurations (sanitized)
        "OIC_PACKAGE_ADMIN"          # Read packages and libraries
    ]

    TOKEN_MANAGEMENT = {
        "default_expiry": 3600,       # 1 hour default token expiry
        "refresh_threshold": 300,     # Refresh token 5 minutes before expiry
        "max_retries": 3,            # Maximum authentication retry attempts
        "backoff_factor": 2.0        # Exponential backoff multiplier
    }
```

#### API Performance and Rate Limiting

```python
class OICApiPerformanceOptimization:
    """OIC API performance optimization and rate limiting strategies."""

    RATE_LIMITING_CONFIG = {
        "requests_per_minute": 300,   # OIC API rate limit (may vary by instance)
        "burst_allowance": 50,        # Burst requests allowed
        "backoff_strategy": "exponential",  # Backoff strategy for rate limits
        "max_backoff_seconds": 300    # Maximum backoff time (5 minutes)
    }

    PAGINATION_STRATEGIES = {
        "default_page_size": 100,     # Default pagination size
        "max_page_size": 1000,        # Maximum allowed page size
        "optimal_page_sizes": {       # Optimized page sizes by entity type
            "integrations": 50,        # Integrations have rich metadata
            "connections": 100,        # Connections are medium complexity
            "activity": 500,           # Activity records are lightweight
            "metrics": 1000           # Metrics records are very lightweight
        }
    }

    PERFORMANCE_HINTS = {
        "concurrent_streams": 3,       # Safe concurrent stream processing
        "connection_pooling": True,    # Enable HTTP connection pooling
        "compression": True,           # Enable gzip compression
        "timeout_settings": {
            "connection_timeout": 30,   # Connection establishment timeout
            "read_timeout": 120,        # Data read timeout
            "total_timeout": 300       # Total request timeout
        }
    }
```

### Security and Data Sanitization Excellence

#### Data Sanitization Patterns

```python
class OICDataSanitizer:
    """Comprehensive data sanitization for OIC entities."""

    SENSITIVE_FIELDS = {
        "connections": [
            "password", "clientSecret", "privateKey", "certificateData",
            "securityToken", "apiKey", "connectionString", "credentials"
        ],
        "certificates": [
            "privateKey", "keystore", "certificateChain", "passphrase"
        ],
        "integrations": [
            "basicAuthPassword", "oauthClientSecret", "tokenSecret"
        ]
    }

    SANITIZATION_STRATEGIES = {
        "remove": "completely_remove_field",
        "mask": "replace_with_asterisks",
        "hash": "replace_with_sha256_hash",
        "reference": "replace_with_reference_id"
    }

    def sanitize_entity(self, entity_type: str, data: dict) -> dict:
        """Sanitize entity data based on security requirements."""
        sensitive_fields = self.SENSITIVE_FIELDS.get(entity_type, [])
        sanitized_data = data.copy()

        for field in sensitive_fields:
            if field in sanitized_data:
                # Remove sensitive data completely
                sanitized_data.pop(field, None)
                # Add sanitization marker
                sanitized_data[f"_{field}_sanitized"] = True

        # Add global sanitization marker
        sanitized_data["_data_sanitized"] = True
        sanitized_data["_sanitization_timestamp"] = datetime.utcnow().isoformat()

        return sanitized_data
```

### flext-oracle-oic-ext Integration Patterns

#### Infrastructure Service Integration

```python
# MANDATORY: Use flext-oracle-oic-ext for all OIC operations (NEVER implement directly)
from flext_oracle_oic_ext import (
    OicApiClient,              # Primary OIC API client interface
    OicAuthenticationManager,  # OAuth2/IDCS authentication handling
    OicEntityExtractor,        # Entity extraction utilities
    OicSchemaAnalyzer,         # Schema discovery and analysis
    OicErrorHandler           # Error handling and recovery
)

class FlextTapOracleOicService(FlextDomainService):
    """Service leveraging flext-oracle-oic-ext infrastructure."""

    def __init__(self, **data) -> None:
        super().__init__(**data)
        # Get OIC services from infrastructure layer
        self._oic_client = self._container.get(OicApiClient)
        self._auth_manager = self._container.get(OicAuthenticationManager)
        self._entity_extractor = self._container.get(OicEntityExtractor)
        self._schema_analyzer = self._container.get(OicSchemaAnalyzer)
```

---

## 🎯 QUALITY ACHIEVEMENT ROADMAP (PHASE-BY-PHASE SUCCESS)

### Week 1: Foundation & Authentication Excellence (PREREQUISITE SUCCESS)

- [ ] **Quality Gate Repair**: Achieve `make validate` success (0 errors)
- [ ] **flext-oracle-oic-ext Integration Assessment**: Document current integration patterns and capabilities
- [ ] **OAuth2/IDCS Flow Validation**: Ensure authentication works with token refresh
- [ ] **Test Coverage Assessment**: Document current coverage and identify critical gaps

### Week 2: Stream Consolidation & Service Architecture (CONSOLIDATION SUCCESS)

- [ ] **Stream Consolidation**: Single source of truth implementation in consolidated streams
- [ ] **Unified Service Implementation**: `FlextTapOracleOicService` with all functionality
- [ ] **Base Stream Enhancement**: `OICBaseStream` with authentication, pagination, error handling
- [ ] **FlextResult Migration**: Replace all exception handling with FlextResult pattern

### Week 3: OIC API Excellence & Schema Discovery (API MASTERY)

- [ ] **Dynamic Schema Discovery**: Schema generation from OIC API metadata
- [ ] **Error Recovery Implementation**: Comprehensive error handling for all API scenarios
- [ ] **Data Sanitization**: Security-focused data sanitization for sensitive entities
- [ ] **Performance Optimization**: Rate limiting, pagination, concurrent processing

### Week 4: Integration Testing Excellence (90% COVERAGE TARGET)

- [ ] **Authentication Tests**: Complete OAuth2/IDCS flow testing
- [ ] **Stream Integration Tests**: Real OIC API tests for all entity types
- [ ] **Security Tests**: Data sanitization and credential handling validation
- [ ] **Coverage Validation**: Achieve and maintain 90% test coverage

### Success Validation (EVIDENCE-BASED CONFIRMATION)

```bash
# Final success confirmation (ALL must pass)
make validate                    # ✅ Zero errors
pytest --cov=src --cov-report=term | grep "90%"  # ✅ Coverage target
make discover && make run        # ✅ Singer compliance
make oic-auth                    # ✅ OIC authentication excellence
python -c "from flext_oracle_oic_ext import OicApiClient; print('✅ Infrastructure integration')"
```

---

**PROJECT AUTHORITY**: FLEXT-TAP-ORACLE-OIC  
**REFACTORING AUTHORITY**: Evidence-based validation required for all success claims  
**QUALITY AUTHORITY**: Zero tolerance - 90% coverage, zero type errors, full Singer compliance  
**INTEGRATION AUTHORITY**: Must leverage flext-oracle-oic-ext infrastructure efficiently while maintaining stream consolidation and security excellence

---

## Pydantic v2 Compliance Standards

**Status**: ✅ Fully Pydantic v2 Compliant
**Verified**: October 22, 2025 (Phase 7 Ecosystem Audit)

### Verification

```bash
make audit-pydantic-v2     # Expected: Status: PASS, Violations: 0
```

### Reference

- **Complete Guide**: `../flext-core/docs/pydantic-v2-modernization/PYDANTIC_V2_STANDARDS_GUIDE.md`
- **Phase 7 Report**: `../flext-core/docs/pydantic-v2-modernization/PHASE_7_COMPLETION_REPORT.md`
