# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is **flext-tap-oracle-oic**, a Singer Tap for Oracle Integration Cloud (OIC) data extraction. It's part of the FLEXT ecosystem, an enterprise-grade distributed data integration platform. The tap implements Clean Architecture + Domain-Driven Design (DDD) patterns using Python 3.13+ with zero-tolerance quality standards.

## Architecture

### Core Components
- **TapOracleOIC**: Main Singer tap class implementing Singer SDK patterns
- **OICBaseStream**: Base class for all OIC data streams with authentication, pagination, and error handling
- **OICTapClient**: Oracle OIC API client with OAuth2/IDCS authentication (imported from flext-oracle-oic-ext)
- **Consolidated Streams**: Single source of truth for all OIC entity streams (integrations, connections, packages, etc.)

### Dependencies
- **flext-core**: Foundation library providing FlextResult, logging, DI patterns
- **flext-meltano**: Singer SDK integration and Meltano patterns
- **flext-oracle-oic-ext**: Shared OIC client patterns and authentication
- **flext-observability**: Monitoring, metrics, and health checks

### Stream Architecture
All streams inherit from `OICBaseStream` providing:
- OAuth2/IDCS authentication with automatic token refresh
- Intelligent pagination with retry logic and error recovery
- Rate limiting and performance optimization
- Data quality validation and comprehensive error handling

## Development Commands

### Essential Commands
```bash
# Complete setup
make setup                    # Install deps + pre-commit hooks + dev environment

# Quality gates (run before committing)
make validate                 # Complete validation: lint + type + security + test
make check                    # Quick health check: lint + type-check
make lint                     # Run ruff linting
make type-check               # Run mypy type checking with strict mode
make security                 # Run bandit + pip-audit security scanning
make format                   # Auto-format code with ruff

# Testing
make test                     # Run all tests with 90% coverage requirement
make test-unit                # Unit tests only (exclude integration)
make test-integration         # Integration tests only
make test-singer              # Singer protocol specific tests
make test-fast                # Tests without coverage (faster feedback)

## TODO: GAPS DE ARQUITETURA IDENTIFICADOS - PRIORIDADE ALTA

### 🚨 GAP 1: Oracle OIC Extension Dependency Gap
**Status**: ALTO - Dependency em flext-oracle-oic-ext pode criar circular dependencies
**Problema**:
- OICTapClient imported from flext-oracle-oic-ext mas relationship não clear
- Extension library pode não ser properly layered
- Shared client patterns podem estar na wrong layer

**TODO**:
- [ ] Review architecture de flext-oracle-oic-ext integration
- [ ] Ensure proper layering entre tap e extension
- [ ] Document client sharing patterns
- [ ] Avoid circular dependencies

### 🚨 GAP 2: OAuth2/IDCS Authentication Complexity
**Status**: ALTO - Authentication patterns podem ser over-engineered
**Problema**:
- OAuth2/IDCS authentication com automatic token refresh é complex
- Error recovery logic pode não be optimal
- Rate limiting implementation pode conflict com Singer patterns

**TODO**:
- [ ] Simplify authentication patterns onde possível
- [ ] Optimize token refresh e error recovery
- [ ] Align rate limiting com Singer SDK patterns
- [ ] Document authentication best practices

### 🚨 GAP 3: Stream Consolidation vs Maintainability
**Status**: ALTO - Consolidated streams podem impact maintainability
**Problema**:
- Single source of truth para all OIC entities pode be hard to maintain
- Stream inheritance hierarchy pode be complex
- Testing individual streams pode be challenging

**TODO**:
- [ ] Review stream organization para balance consolidation vs maintainability
- [ ] Simplify stream inheritance hierarchy
- [ ] Improve individual stream testing patterns
- [ ] Document stream organization principles
make coverage-html            # Generate HTML coverage report
```

### Singer Tap Operations
```bash
# Discovery and catalog
make discover                 # Generate catalog.json from OIC API discovery
make catalog                  # Alias for discover

# Data extraction
make run                      # Run tap extraction with config.json + catalog.json
make sync                     # Alias for run

# Configuration validation
make validate-config          # Validate config.json structure
```

### Oracle OIC Operations
```bash
# OIC connectivity testing  
make oic-test                 # Test OIC API connectivity and authentication
make oic-auth                 # Test OAuth2/IDCS authentication flow
make oic-endpoints            # List available OIC API endpoints
```

### Development Workflow
```bash
# Single test file
pytest tests/test_auth.py -v

# Specific test markers
pytest -m unit                # Unit tests only
pytest -m integration         # Integration tests only
pytest -m singer              # Singer protocol tests

# Debug failing tests
pytest tests/test_client.py -v -s --pdb

# Watch mode (if available)
pytest-watch tests/
```

## Configuration

### Required Configuration (config.json)
```json
{
  "base_url": "https://your-instance.integration.ocp.oraclecloud.com",
  "oauth_client_id": "your_client_id", 
  "oauth_client_secret": "your_client_secret",
  "oauth_token_url": "https://idcs-tenant.identity.oraclecloud.com/oauth2/v1/token",
  "oauth_client_aud": "https://your-instance.integration.ocp.oraclecloud.com:443/urn:opc:resource:consumer::all"
}
```

### Optional Configuration
- `include_extended`: Enable extended stream functionality (default: false)
- `page_size`: API pagination size (default: 100)
- `request_timeout`: Request timeout in seconds (default: 30)
- `max_retries`: Maximum retry attempts (default: 3)
- `start_date`: Start date for incremental extraction

## Available Streams

### Core Business Streams
- **integrations**: Integration definitions, configurations, and metadata
- **connections**: Connection configurations and credentials
- **packages**: Integration packages and versions
- **agents**: OIC agents and connectivity agents

### Infrastructure Streams  
- **libraries**: Shared libraries and schemas
- **certificates**: Security certificates and keystores
- **adapters**: Adapter configurations and properties
- **recipes**: Integration recipes and templates

### Monitoring Streams
- **activity**: Integration activity and execution logs
- **metrics**: Performance metrics and statistics
- **tracking**: Message tracking and audit trails
- **alerts**: System alerts and notifications

## Quality Standards

### Zero Tolerance Quality Gates
- **Coverage**: Minimum 90% test coverage enforced
- **Type Safety**: Strict MyPy with no untyped code allowed
- **Linting**: Ruff with ALL rules enabled (comprehensive rule set)
- **Security**: Bandit security scanning + pip-audit dependency checks
- **PEP8**: Strict code formatting and style compliance

### Testing Strategy
- **Unit Tests**: Comprehensive test coverage for all business logic
- **Integration Tests**: Real OIC API integration testing with mocks
- **Singer Tests**: Singer protocol compliance validation
- **E2E Tests**: Complete pipeline testing from config to output

## Authentication

### OAuth2/IDCS Flow
1. Client credentials configured in config.json
2. Token obtained from IDCS OAuth2 endpoint
3. Access token used for OIC API calls with automatic refresh
4. Audience-based scoping for OIC resource access

### Required IDCS Setup
- Create IDCS Application with OAuth2 client credentials
- Configure audience for OIC instance
- Grant necessary OIC API permissions

## Error Handling

### Built-in Error Recovery
- **Authentication**: Automatic token refresh on 401 errors
- **Rate Limiting**: Intelligent backoff on 429 errors  
- **Network Issues**: Configurable retry logic with exponential backoff
- **Data Quality**: Schema validation with detailed error reporting

### Debugging
```bash
# Enable debug logging
export FLEXT_LOG_LEVEL=debug
export SINGER_SDK_LOG_LEVEL=debug

# Run with detailed output
make run > output.jsonl 2> debug.log

# Test authentication separately
make oic-auth
```

## Integration with FLEXT Ecosystem

### Meltano Integration
This tap is designed for use with Meltano/dbt pipelines:
```bash
# Via flext-meltano
meltano add extractor tap-oracle-oic
meltano extract tap-oracle-oic target-jsonl
```

### Shared Libraries
- Uses `flext-core` for result patterns, logging, and DI
- Leverages `flext-oracle-oic-ext` for common OIC client functionality
- Integrates with `flext-observability` for monitoring and metrics

## Troubleshooting

### Common Issues
**Authentication Failures**: Check IDCS client credentials and audience configuration
**Rate Limiting**: Reduce page_size or increase request delays
**SSL/TLS Issues**: Verify OIC instance certificates and network connectivity
**Schema Errors**: Run `make discover` to refresh catalog with latest OIC schema

### Diagnostics
```bash
make diagnose                 # Full project health check
make doctor                   # Project health + validation
make oic-test                 # Test OIC connectivity specifically
```