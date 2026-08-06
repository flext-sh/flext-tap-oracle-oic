# AGENTS.md — flext-tap-oracle-oic

> **Parent workspace law** lives in [`../AGENTS.md`](../AGENTS.md) — read it first.
> Universal engineering core: `~/.agents/UNIVERSAL_CORE.md`. Composition: global skills + parent/root `AGENTS.md` + this scope delta. Do not re-embed universal law.
>
> **Standalone / independent mode:** when `../AGENTS.md` does not resolve, pin the parent raw `AGENTS.md` URL to the same branch/release as this package (never `main`).

<!-- AIHUB-AGENTS-SCOPE-LOCAL-BEGIN -->
**Package:** `flext_tap_oracle_oic` · deps: `flext-api`, `flext-cli`, `flext-core`, `flext-meltano`, `flext-oracle-oic`

## Overview

Singer **tap** (extractor) for Oracle Integration Cloud. Thin driver over `flext-meltano` (ADR-006), delegating REST access to `flext-oracle-oic`.

## Structure

```text
src/flext_tap_oracle_oic/
├── api.py            # FlextTapOracleOicService(FlextMeltanoTapServiceBase)
├── tap.py            # OAuth2 client-credentials authentication
├── tap_streams.py    # stream topology (+ _models/streams.py::ALL_STREAMS)
├── constants.py typings.py protocols.py models.py utilities.py   # AUTO-GENERATED facets
└── _models/
```

## Code Map

| Symbol | Kind | Location | Role |
|--------|------|----------|------|
| `FlextTapOracleOicService` | class | `api.py` | `FlextMeltanoTapServiceBase` |
| tap | code | `tap.py` | OAuth2 auth; uses `_models/streams.py::ALL_STREAMS` |

## Conventions (specific to this package)

- Settings use `settings.TapOracleOic.*`.
- Config/settings canonical pattern: ADR-012.
- Codemod governance (ast-grep + make mod): ADR-014.

## Anti-Patterns / Gotchas

- **`_models/*` deliberately imports `flext_meltano` utilities directly** (not the own facade) to avoid facade import cycles — keep that pattern.

## Commands

```bash
make check PROJECT=flext-tap-oracle-oic
make test  PROJECT=flext-tap-oracle-oic       # tests/unit
```
<!-- AIHUB-AGENTS-SCOPE-LOCAL-END -->
