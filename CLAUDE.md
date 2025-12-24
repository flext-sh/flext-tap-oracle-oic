# flext-tap-oracle-oic - FLEXT Singer Ecosystem

**Hierarchy**: PROJECT
**Parent**: [../CLAUDE.md](../CLAUDE.md) - Workspace standards
**Last Update**: 2025-12-07

---

## Project Overview

**FLEXT-Tap-Oracle-OIC** is the Singer tap for Oracle Integration Cloud extraction in the FLEXT ecosystem.

**Version**: 1.0.0  
**Status**: Production-ready  
**Python**: 3.13+

**CRITICAL INTEGRATION DEPENDENCIES**:

- **flext-meltano**: MANDATORY for ALL Singer operations (ZERO TOLERANCE for direct singer-sdk without flext-meltano)
- **flext-oracle-oic**: MANDATORY for ALL Oracle OIC operations (ZERO TOLERANCE for direct OAuth2/httpx imports)
- **flext-core**: Foundation patterns (FlextResult, FlextService, FlextContainer)

---

## Essential Commands

```bash
# Setup and validation
make setup                    # Complete development environment setup
make validate                 # Complete validation (lint + type + security + test)
make check                    # Quick check (lint + type)

# Quality gates
make lint                     # Ruff linting
make type-check               # Pyrefly type checking
make security                 # Bandit security scan
make test                     # Run tests
```

---

## Key Patterns

### Singer Tap Implementation

```python
from flext_core import FlextResult
from flext_tap_oracle_oic import FlextTapOracleOic

tap = FlextTapOracleOic()

# Discover catalog
result = tap.discover()
if result.is_success:
    catalog = result.unwrap()
```

---

## Critical Development Rules

### ZERO TOLERANCE Policies

**ABSOLUTELY FORBIDDEN**:

- ❌ Direct singer-sdk imports (use flext-meltano)
- ❌ Direct Oracle OIC operations (use flext-oracle-oic)
- ❌ Exception-based error handling (use FlextResult)
- ❌ Type ignores or `Any` types

**MANDATORY**:

- ✅ Use `FlextResult[T]` for all operations
- ✅ Use flext-meltano for Singer operations
- ✅ Use flext-oracle-oic for OIC operations
- ✅ Complete type annotations
- ✅ Zero Ruff violations

---

**See Also**:

- [Workspace Standards](../CLAUDE.md)
- [flext-core Patterns](../flext-core/CLAUDE.md)
- [flext-oracle-oic Patterns](../flext-oracle-oic/CLAUDE.md)
- [flext-meltano Patterns](../flext-meltano/CLAUDE.md)
