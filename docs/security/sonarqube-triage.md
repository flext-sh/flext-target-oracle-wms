# Triagem SonarCloud — flext-sh/flext-target-oracle-wms

Gerado do dump da plataforma SonarCloud (2026-08-06).

Bead de rastreio: `mro-2wjm.22`

## Resumo

**19 issues** — BLOCKER 0, CRITICAL 0, MAJOR 6, MINOR 13
Tipos: VULNERABILITY 5, BUG 0, CODE_SMELL 14

| regra | issues |
|---|---|
| `python:S116` | 10 |
| `githubactions:S8233` | 2 |
| `python:S8714` | 2 |
| `githubactions:S8264` | 1 |
| `text:S8565` | 1 |
| `python:S2068` | 1 |
| `python:S5778` | 1 |
| `python:S7504` | 1 |

## Issues

Coluna **Decisão**: `corrigir` / `falso-positivo` / `risco-aceito`.

| # | sev | tipo | regra | componente | linha | Decisão |
|---|---|---|---|---|---|---|
| 1 | MAJOR | VULNERABILITY | `githubactions:S8264` | `.github/workflows/docs.yml` | 18 | |
| 2 | MAJOR | VULNERABILITY | `githubactions:S8233` | `.github/workflows/docs.yml` | 19 | |
| 3 | MAJOR | VULNERABILITY | `githubactions:S8233` | `.github/workflows/docs.yml` | 20 | |
| 4 | MAJOR | VULNERABILITY | `text:S8565` | `pyproject.toml` | - | |
| 5 | MAJOR | VULNERABILITY | `python:S2068` | `src/flext_target_oracle_wms/cli.py` | 93 | |
| 6 | MAJOR | CODE_SMELL | `python:S5778` | `tests/unit/test_target.py` | 107 | |
| 7 | MINOR | CODE_SMELL | `python:S7504` | `conftest.py` | 20 | |
| 8 | MINOR | CODE_SMELL | `python:S116` | `src/flext_target_oracle_wms/utilities.py` | 24 | |
| 9 | MINOR | CODE_SMELL | `python:S116` | `src/flext_target_oracle_wms/utilities.py` | 25 | |
| 10 | MINOR | CODE_SMELL | `python:S116` | `src/flext_target_oracle_wms/utilities.py` | 28 | |
| 11 | MINOR | CODE_SMELL | `python:S116` | `src/flext_target_oracle_wms/utilities.py` | 29 | |
| 12 | MINOR | CODE_SMELL | `python:S116` | `src/flext_target_oracle_wms/utilities.py` | 30 | |
| 13 | MINOR | CODE_SMELL | `python:S116` | `src/flext_target_oracle_wms/utilities.py` | 31 | |
| 14 | MINOR | CODE_SMELL | `python:S116` | `src/flext_target_oracle_wms/utilities.py` | 32 | |
| 15 | MINOR | CODE_SMELL | `python:S116` | `src/flext_target_oracle_wms/utilities.py` | 33 | |
| 16 | MINOR | CODE_SMELL | `python:S116` | `src/flext_target_oracle_wms/utilities.py` | 34 | |
| 17 | MINOR | CODE_SMELL | `python:S116` | `src/flext_target_oracle_wms/utilities.py` | 35 | |
| 18 | MINOR | CODE_SMELL | `python:S8714` | `tests/examples/test_examples.py` | 229 | |
| 19 | MINOR | CODE_SMELL | `python:S8714` | `tests/examples/test_examples.py` | 234 | |

## Como triar

1. **BLOCKER e CRITICAL primeiro**, e todo VULNERABILITY independente de severidade.
2. Classificar: **corrigir**, **falso-positivo** (marcar na plataforma SonarCloud com justificativa), **risco-aceito** (com prazo).
3. CODE_SMELL em volume alto sugere padrão — corrigir a causa raiz, não issue a issue.

Dados brutos: `~/sonarqube-violations/by-repo/flext-sh__flext-target-oracle-wms.json`

