# Triagem SonarCloud — flext-sh/flext-tap-oracle-oic

Gerado do dump da plataforma SonarCloud (2026-08-06).

Bead de rastreio: `mro-2wjm.18`

## Resumo

**28 issues** — BLOCKER 0, CRITICAL 10, MAJOR 4, MINOR 14
Tipos: VULNERABILITY 4, BUG 0, CODE_SMELL 24

| regra | issues |
|---|---|
| `python:S116` | 11 |
| `python:S1192` | 8 |
| `python:S3776` | 2 |
| `githubactions:S8233` | 2 |
| `githubactions:S8264` | 1 |
| `text:S8565` | 1 |
| `python:S7504` | 1 |
| `python:S6353` | 1 |

## Issues

Coluna **Decisão**: `corrigir` / `falso-positivo` / `risco-aceito`.

| # | sev | tipo | regra | componente | linha | Decisão |
|---|---|---|---|---|---|---|
| 1 | CRITICAL | CODE_SMELL | `python:S1192` | `src/flext_tap_oracle_oic/_models/streams.py` | 87 | |
| 2 | CRITICAL | CODE_SMELL | `python:S1192` | `src/flext_tap_oracle_oic/_models/streams.py` | 92 | |
| 3 | CRITICAL | CODE_SMELL | `python:S1192` | `src/flext_tap_oracle_oic/_models/streams.py` | 97 | |
| 4 | CRITICAL | CODE_SMELL | `python:S1192` | `src/flext_tap_oracle_oic/_models/streams.py` | 102 | |
| 5 | CRITICAL | CODE_SMELL | `python:S1192` | `src/flext_tap_oracle_oic/_models/streams.py` | 142 | |
| 6 | CRITICAL | CODE_SMELL | `python:S1192` | `src/flext_tap_oracle_oic/_models/streams.py` | 246 | |
| 7 | CRITICAL | CODE_SMELL | `python:S3776` | `src/flext_tap_oracle_oic/models.py` | 222 | |
| 8 | CRITICAL | CODE_SMELL | `python:S1192` | `src/flext_tap_oracle_oic/models.py` | 479 | |
| 9 | CRITICAL | CODE_SMELL | `python:S1192` | `src/flext_tap_oracle_oic/tap.py` | 130 | |
| 10 | CRITICAL | CODE_SMELL | `python:S3776` | `src/flext_tap_oracle_oic/utilities.py` | 335 | |
| 11 | MAJOR | VULNERABILITY | `githubactions:S8264` | `.github/workflows/docs.yml` | 18 | |
| 12 | MAJOR | VULNERABILITY | `githubactions:S8233` | `.github/workflows/docs.yml` | 19 | |
| 13 | MAJOR | VULNERABILITY | `githubactions:S8233` | `.github/workflows/docs.yml` | 20 | |
| 14 | MAJOR | VULNERABILITY | `text:S8565` | `pyproject.toml` | - | |
| 15 | MINOR | CODE_SMELL | `python:S7504` | `conftest.py` | 20 | |
| 16 | MINOR | CODE_SMELL | `python:S6353` | `src/flext_tap_oracle_oic/constants.py` | 40 | |
| 17 | MINOR | CODE_SMELL | `python:S116` | `src/flext_tap_oracle_oic/models.py` | 111 | |
| 18 | MINOR | CODE_SMELL | `python:S116` | `src/flext_tap_oracle_oic/models.py` | 493 | |
| 19 | MINOR | CODE_SMELL | `python:S116` | `src/flext_tap_oracle_oic/models.py` | 495 | |
| 20 | MINOR | CODE_SMELL | `python:S116` | `src/flext_tap_oracle_oic/models.py` | 497 | |
| 21 | MINOR | CODE_SMELL | `python:S116` | `src/flext_tap_oracle_oic/models.py` | 499 | |
| 22 | MINOR | CODE_SMELL | `python:S116` | `src/flext_tap_oracle_oic/models.py` | 501 | |
| 23 | MINOR | CODE_SMELL | `python:S116` | `src/flext_tap_oracle_oic/models.py` | 503 | |
| 24 | MINOR | CODE_SMELL | `python:S116` | `src/flext_tap_oracle_oic/models.py` | 505 | |
| 25 | MINOR | CODE_SMELL | `python:S116` | `src/flext_tap_oracle_oic/models.py` | 507 | |
| 26 | MINOR | CODE_SMELL | `python:S116` | `src/flext_tap_oracle_oic/models.py` | 509 | |
| 27 | MINOR | CODE_SMELL | `python:S116` | `src/flext_tap_oracle_oic/models.py` | 511 | |
| 28 | MINOR | CODE_SMELL | `python:S5685` | `src/flext_tap_oracle_oic/tap.py` | 306 | |

## Como triar

1. **BLOCKER e CRITICAL primeiro**, e todo VULNERABILITY independente de severidade.
2. Classificar: **corrigir**, **falso-positivo** (marcar na plataforma SonarCloud com justificativa), **risco-aceito** (com prazo).
3. CODE_SMELL em volume alto sugere padrão — corrigir a causa raiz, não issue a issue.

Dados brutos: `~/sonarqube-violations/by-repo/flext-sh__flext-tap-oracle-oic.json`

