# CLAUDE.local.md - TAP-ORACLE-OIC PROJECT SPECIFICS

**Hierarquia**: **PROJECT-SPECIFIC**  
**Projeto**: Tap Oracle OIC - Enterprise Integration Cloud Data Extractor  
**Status**: PRODUCTION READY - Active OIC metadata extraction  
**Framework**: Singer Protocol + OAuth2/IDCS + Oracle Integration Cloud  
**Última Atualização**: 2025-06-26

**Referência Global**: `/home/marlonsc/CLAUDE.md` → Universal principles  
**Referência Workspace**: `../CLAUDE.md` → PyAuto workspace patterns  
**Referência Cross-Workspace**: `/home/marlonsc/CLAUDE.local.md` → Cross-workspace issues

---

## 🎯 PROJECT-SPECIFIC CONFIGURATION

### Virtual Environment Usage

```bash
# MANDATORY: Use workspace venv
source /home/marlonsc/pyauto/.venv/bin/activate
# NOT project-specific venv
```

### Agent Coordination

```bash
# Read workspace coordination first
cat /home/marlonsc/pyauto/.token | tail -5
# Use project .token only for project-specific coordination
```

### Project-Specific Environment Variables

```bash
# Tap Oracle OIC specific configurations
export TAP_OIC_BASE_URL=https://instance-region.integration.ocp.oraclecloud.com
export TAP_OIC_OAUTH_CLIENT_ID=oic_tap_client_id
export TAP_OIC_OAUTH_CLIENT_SECRET=secure_oauth_secret
export TAP_OIC_OAUTH_TOKEN_URL=https://idcs-tenant.identity.oraclecloud.com/oauth2/v1/token
export TAP_OIC_INCLUDE_EXTENDED=true
export TAP_OIC_PAGE_SIZE=100
export TAP_OIC_START_DATE=2024-01-01T00:00:00Z
export TAP_OIC_REQUEST_TIMEOUT=30
export TAP_OIC_MAX_RETRIES=3
export TAP_OIC_LOG_LEVEL=DEBUG
```

---

## 🏗️ TAP ORACLE OIC ARCHITECTURE

### **Purpose & Role**

- **Integration Metadata Extractor**: Complete OIC integration catalog and configuration extraction
- **Singer Protocol Compliance**: Standardized data extraction following Singer specifications
- **OAuth2/IDCS Authentication**: Enterprise-grade security for Oracle Cloud access
- **Integration Governance**: Enables integration documentation and compliance tracking
- **Cross-System Synchronization**: Facilitates OIC metadata sync across environments

### **Core Singer Components**

```python
# Tap Oracle OIC structure
src/tap_oracle_oic/
├── tap.py               # Main Singer tap implementation
├── streams.py           # Stream definitions (integrations, connections)
├── streams_core.py      # Core OIC entity streams
├── streams_extended.py  # Extended OIC functionality streams
├── streams_infrastructure.py # Infrastructure and monitoring streams
├── streams_monitoring.py # Monitoring and analytics streams
├── auth.py              # OAuth2/IDCS authentication
├── config.py            # Configuration management
├── health.py            # Health check utilities
└── constants.py         # OIC API constants and endpoints
```

### **Oracle OIC Data Streams**

- **Integrations Stream**: Integration flows, mappings, and configurations
- **Connections Stream**: Connection adapters and configurations
- **Packages Stream**: Integration package metadata and versions
- **Lookups Stream**: Lookup table definitions and data
- **Certificates Stream**: Security certificates and credentials
- **Agents Stream**: On-premises agent configurations

---

## 🔧 PROJECT-SPECIFIC TECHNICAL DETAILS

### **Development Commands**

```bash
# MANDATORY: Always from workspace venv
source /home/marlonsc/pyauto/.venv/bin/activate

# Core development workflow
make install-dev       # Install development dependencies
make test              # Run comprehensive test suite
make test-unit         # Unit tests only
make test-integration  # Integration tests with OIC
make test-e2e          # End-to-end tests with OAuth2
make lint              # Code quality checks
make format            # Code formatting

# Singer tap operations
tap-oracle-oic --config config.json --discover > catalog.json
tap-oracle-oic --config config.json --catalog catalog.json
tap-oracle-oic --config config.json --catalog catalog.json --state state.json
```

### **OAuth2/IDCS Authentication Testing**

```bash
# Test OAuth2 authentication flow
tap-oracle-oic --config config.json --test-auth

# Test with debug authentication
export TAP_OIC_LOG_LEVEL=DEBUG
export TAP_OIC_AUTH_DEBUG=true
tap-oracle-oic --config config.json --discover

# Test token refresh functionality
tap-oracle-oic --config config.json --test-token-refresh
```

### **OIC Integration Testing**

```bash
# Test OIC API connectivity
tap-oracle-oic --config config.json --test-connection

# Test specific streams
tap-oracle-oic --config config.json --test-stream integrations
tap-oracle-oic --config config.json --test-stream connections

# Test with production OIC instance
tap-oracle-oic --config prod_config.json --catalog catalog.json --dry-run
```

---

## 🚨 PROJECT-SPECIFIC KNOWN ISSUES

### **Oracle OIC Integration Challenges**

- **OAuth2 Token Management**: Complex token lifecycle and refresh handling
- **API Rate Limiting**: OIC imposes strict rate limits requiring intelligent throttling
- **Large Integration Metadata**: Memory management for extensive integration catalogs
- **Multi-Region Support**: Handling different OIC regional endpoints
- **Version Compatibility**: OIC API evolution and backward compatibility

### **Singer Protocol OIC Considerations**

```python
# OIC-specific Singer patterns
class OICSingerPatterns:
    """Production patterns for OIC Singer implementation."""

    def handle_oauth2_token_lifecycle(self):
        """Manage OAuth2 token lifecycle efficiently."""
        # Monitor token expiration
        if self.token_expires_soon():
            self.refresh_access_token()

        # Handle token refresh during extraction
        try:
            return self.make_api_request(endpoint)
        except OAuthTokenExpiredError:
            self.refresh_access_token()
            return self.make_api_request(endpoint)

    def extract_large_integration_metadata(self):
        """Handle large OIC integration catalogs efficiently."""
        # Use cursor-based pagination for large datasets
        cursor = None
        while True:
            page_response = self.get_integrations_page(
                cursor=cursor,
                page_size=self.config.page_size
            )

            for integration in page_response.integrations:
                yield self.transform_integration_record(integration)

            cursor = page_response.next_cursor
            if not cursor:
                break

    def handle_oic_api_rate_limiting(self):
        """Implement intelligent rate limiting for OIC API."""
        # Exponential backoff with jitter
        if self.rate_limit_exceeded():
            wait_time = min(
                self.base_delay * (2 ** self.retry_count),
                self.max_delay
            )
            # Add jitter to prevent thundering herd
            jitter = random.uniform(0.1, 0.3) * wait_time
            await asyncio.sleep(wait_time + jitter)
```

### **Production OIC Edge Cases**

```bash
# Common OIC extraction issues
1. Token Expiration: OAuth2 tokens expiring during long extractions
2. API Versioning: OIC API changes affecting stream schemas
3. Large Package Export: Integration packages exceeding memory limits
4. Multi-Tenant Access: Cross-tenant permissions and scoping
5. Connection State: OIC connections in various lifecycle states
```

---

## 🎯 PROJECT-SPECIFIC SUCCESS METRICS

### **Singer Protocol OIC Compliance**

- **Schema Discovery**: 100% automatic stream detection for all OIC entities
- **OAuth2 Reliability**: 99.99% successful authentication attempts
- **Data Extraction Rate**: >10,000 integration records/hour extraction
- **Incremental Sync Efficiency**: <5 minute sync cycles for metadata changes
- **API Error Handling**: 95% automatic recovery from transient API errors

### **Enterprise OIC Integration Goals**

- **Metadata Coverage**: 100% OIC integration metadata extraction
- **Multi-Environment Support**: Seamless extraction across dev/test/prod OIC instances
- **Governance Compliance**: Complete audit trail for integration changes
- **Documentation Automation**: 90% reduction in manual integration documentation
- **Cross-System Sync**: Real-time sync of OIC metadata to governance systems

---

## 🔗 PROJECT-SPECIFIC INTEGRATIONS

### **Singer Ecosystem Integration**

- **Target Compatibility**: Works with all Singer-compliant targets
- **Meltano Plugin**: Official Meltano Hub plugin for OIC extraction
- **Schema Evolution**: Automatic adaptation to OIC API changes
- **State Management**: Advanced incremental sync with bookmark management

### **PyAuto Ecosystem Integration**

- **target-oracle-oic**: Round-trip integration for OIC metadata management
- **flext-oracle-oic**: Unified FLX adapter with Singer tap integration
- **oracle-oic-ext**: Meltano extension for lifecycle management
- **gruponos-meltane-native**: POC reference implementation

### **Oracle Cloud Integration**

```python
# Production OIC integration configuration
class ProductionOICIntegration:
    """Production OIC integration for enterprise environments."""

    # Multi-environment configuration
    PRODUCTION_CONFIG = {
        "base_url": "https://prod-region.integration.ocp.oraclecloud.com",
        "oauth_client_id": "${OIC_PROD_CLIENT_ID}",
        "oauth_client_secret": "${OIC_PROD_CLIENT_SECRET}",
        "oauth_token_url": "https://prod-idcs.identity.oraclecloud.com/oauth2/v1/token",

        # Performance optimization
        "page_size": 200,
        "request_timeout": 60,
        "max_retries": 5,
        "retry_backoff_factor": 2,

        # Advanced features
        "include_extended": True,
        "include_monitoring": True,
        "include_infrastructure": True,
        "extract_packages": True,
        "extract_lookups": True,

        # Incremental sync configuration
        "start_date": "2024-01-01T00:00:00Z",
        "incremental_strategy": "timestamp",
        "bookmark_properties": ["last_updated", "created_time"],

        # Stream selection
        "selected_streams": [
            "integrations",
            "connections",
            "packages",
            "lookups",
            "certificates",
            "agents",
            "monitoring_metrics"
        ]
    }

    # Development environment configuration
    DEV_CONFIG = {
        **PRODUCTION_CONFIG,
        "base_url": "https://dev-region.integration.ocp.oraclecloud.com",
        "oauth_token_url": "https://dev-idcs.identity.oraclecloud.com/oauth2/v1/token",
        "page_size": 50,  # Smaller pages for dev
        "include_extended": False,  # Reduced scope for dev
    }
```

---

## 📊 PROJECT-SPECIFIC MONITORING

### **OIC Singer Tap Metrics**

```python
# Key metrics for OIC tap monitoring
TAP_OIC_METRICS = {
    "oauth_token_refresh_rate": "OAuth2 token refresh frequency",
    "integration_extraction_rate": "Integrations extracted per minute",
    "api_response_time": "Average OIC API response time",
    "rate_limit_hit_rate": "Frequency of API rate limit encounters",
    "schema_discovery_time": "Time to discover all OIC streams",
    "extraction_completeness": "Percentage of available metadata extracted",
}
```

### **OIC Health Monitoring**

```bash
# Comprehensive OIC monitoring
tap-oracle-oic --config config.json --test-connection --detailed
tap-oracle-oic --config config.json --health-check --all-streams
tap-oracle-oic --config config.json --performance-test --duration 300
```

---

## 📋 PROJECT-SPECIFIC MAINTENANCE

### **Regular Maintenance Tasks**

- **Daily**: Monitor OAuth2 token usage and extraction performance
- **Weekly**: Review API rate limiting and optimize request patterns
- **Monthly**: Update OIC API client libraries and test compatibility
- **Quarterly**: Performance optimization and schema evolution review

### **Singer Protocol Updates**

```bash
# Keep Singer SDK and OIC dependencies updated
pip install --upgrade singer-sdk requests-oauthlib

# Validate Singer compliance
singer-check-tap --tap tap-oracle-oic --config config.json
singer-validate-catalog --catalog oic-catalog.json
```

### **Emergency Procedures**

```bash
# OIC tap emergency troubleshooting
1. Test OAuth2 flow: tap-oracle-oic --config config.json --test-auth
2. Check OIC service status: curl -I ${OIC_BASE_URL}/ic/api/integration/v1/integrations
3. Reset OAuth2 tokens: tap-oracle-oic --config config.json --reset-auth
4. Enable debug mode: export TAP_OIC_LOG_LEVEL=DEBUG && tap-oracle-oic --config config.json --discover
5. Test specific streams: tap-oracle-oic --config config.json --test-stream integrations --debug
```

---

**PROJECT SUMMARY**: Singer tap empresarial para Oracle Integration Cloud com autenticação OAuth2/IDCS e extração completa de metadados de integração para governança e sincronização cross-system.

**CRITICAL SUCCESS FACTOR**: Manter autenticação OAuth2 robusta e extração eficiente de metadados OIC, garantindo compatibilidade total com Singer protocol para governança empresarial.

---

_Última Atualização: 2025-06-26_  
_Próxima Revisão: Semanal durante extrações ativas_  
_Status: PRODUCTION READY - Extração ativa de metadados OIC em produção_
