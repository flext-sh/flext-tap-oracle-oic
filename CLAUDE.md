# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Singer protocol tap for Oracle Integration Cloud (OIC) that extracts integration metadata and configurations. It's built using clean architecture patterns with the FLEXT framework, implementing enterprise-grade authentication via OAuth2/IDCS.

## Key Architecture

### Core Components

- **Singer Tap Implementation**: `src/flext_tap_oracle_oic/tap.py` - Main tap class with dependency injection
- **Authentication**: `src/flext_tap_oracle_oic/auth.py` - OAuth2/IDCS authenticator that delegates to flext-auth
- **Configuration**: `src/flext_tap_oracle_oic/config.py` - Pydantic-based configuration with multiple inheritance
- **Stream Definitions**: Multiple stream files for different OIC entity types:
  - `streams_core.py` - Core entities (integrations, connections, lookups)
  - `streams_extended.py` - Extended entities (agents, certificates, libraries)
  - `streams_monitoring.py` - Monitoring and audit streams

### FLEXT Framework Integration

- Uses `flext-core` for dependency injection (Lato container) and domain patterns
- Uses `flext-observability` for structured logging
- Delegates authentication to `flext-auth` for enterprise OAuth2 patterns
- Configuration inherits from `flext-core.config.adapters.singer.SingerTapConfig`

### Authentication Pattern

The tap implements a facade pattern where legacy `OICOAuth2Authenticator` delegates entirely to the enterprise `flext-auth.authentication_implementation.AuthenticationService` while maintaining Singer SDK compatibility.

## Development Commands

### Environment Setup

```bash
# Use workspace virtual environment (NOT project-specific)
source /home/marlonsc/flext/.venv/bin/activate

# Install dependencies
make install-dev
```

### Testing

```bash
# Run all tests
make test

# Run with coverage
make test-coverage

# Run specific test types (uses pytest markers)
pytest -m unit tests/
pytest -m integration tests/
pytest -m oic tests/
```

### Code Quality

```bash
# Run linting (Ruff)
make lint

# Format code
make format

# Type checking (MyPy with strict mode)
make type-check

# Security analysis
make security

# Run all quality checks
make check
```

### Singer Tap Operations

```bash
# Discover available streams
tap-oracle-oic --config config.json --discover > catalog.json

# Run extraction
tap-oracle-oic --config config.json --catalog catalog.json

# Run with state management
tap-oracle-oic --config config.json --catalog catalog.json --state state.json

# Test connection
tap-oracle-oic --config config.json --test
```

## Configuration Structure

The configuration uses multiple inheritance from base config classes:

- `OICAuthConfig` - OAuth2/IDCS authentication settings
- `OICConnectionConfig` - Connection and performance settings
- `StreamSelectionConfig` - Stream filtering and selection
- `DiscoveryConfig` - Catalog discovery settings
- `DataExtractionConfig` - Data extraction behavior

Environment variables use the prefix `TAP_ORACLE_OIC_` with double underscore for nested values.

## Stream Architecture

Streams are categorized by functionality:

- **Core Streams**: Always available (integrations, connections, lookups)
- **Extended Streams**: Optional (libraries, agents, certificates)
- **Monitoring Streams**: Optional (monitoring data, audit logs)

Each stream inherits from a base stream class and implements OIC-specific API endpoints with intelligent pagination and error handling.

## Testing Strategy

Tests are organized with pytest markers:

- `unit` - Unit tests for individual components
- `integration` - Integration tests with mocked OIC responses
- `e2e` - End-to-end tests requiring actual OIC connection
- `oic`, `oracle`, `singer`, `tap`, `stream` - Component-specific markers

Coverage target: 90% minimum with branch coverage enabled.

## Dependencies

### Core Dependencies

- `singer-sdk` - Singer specification implementation
- `flext-core` - FLEXT framework core (dependency injection, domain patterns)
- `flext-observability` - Structured logging
- `requests` - HTTP client
- `oracledb` - Oracle database connectivity

### Development Dependencies

- `pytest` with multiple plugins for comprehensive testing
- `ruff` for linting and formatting
- `mypy` for type checking with strict mode
- `pre-commit` for git hooks

## Important Notes

- This tap follows "ZERO TOLERANCE" architecture principles - no legacy code or fallbacks
- Authentication delegates to enterprise flext-auth service but maintains Singer SDK compatibility
- All configuration is type-safe using Pydantic v2 models
- The codebase uses Python 3.13 with strict typing requirements
- Project is part of the FLEXT workspace and uses shared virtual environment at `/home/marlonsc/flext/.venv`
