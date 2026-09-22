# Triagem Snyk Code (SAST) — flext-sh/flext-target-oracle-wms

<!-- TOC START -->
- [Resumo](#resumo)
- [Como usar este documento](#como-usar-este-documento)
- [Achados](#achados)
  - [1 · 🟡 MEDIUM · Use of Hardcoded Passwords](#1-medium-use-of-hardcoded-passwords)
  - [2 · 🟡 MEDIUM · Use of Hardcoded Passwords](#2-medium-use-of-hardcoded-passwords)
  - [3 · 🟡 MEDIUM · Use of Hardcoded Passwords](#3-medium-use-of-hardcoded-passwords)
  - [4 · 🟡 MEDIUM · Use of Hardcoded Passwords](#4-medium-use-of-hardcoded-passwords)
<!-- TOC END -->

Gerado do scan Snyk (dump 2026-08-06). Bead: `mro-qmmv`

## Resumo

**4 achados** — critical 0, high 0, medium 4, low 0

| categoria                  | achados |
| -------------------------- | ------- |
| Use of Hardcoded Passwords | 4       |

## Como usar este documento

Cada achado traz o **código real** extraído da worktree (linha `>>>` = sink reportado),
a regra completa e o CWE. Preencha **Decisão**: `corrigir` / `falso-positivo` (registrar
em `.snyk`) / `risco-aceito` (com prazo).

## Achados

### 1 · 🟡 MEDIUM · Use of Hardcoded Passwords

**Local**: `examples/01_basic_usage.py:35` · **CWE**: -

```python notest
       31
       32  WMS_AUTH: Final[Mapping[str, str]] = MappingProxyType({
       33      "base_url": "https://wms.example.oraclecloud.com",
       34      "username": "wms_user",
>>>    35      "password": "wms_pass",
       36  })
       37  BATCH_SIZE: Final[int] = 100
       38
       39
```

**Decisão**:

### 2 · 🟡 MEDIUM · Use of Hardcoded Passwords

**Local**: `examples/02_batch_processing.py:31` · **CWE**: -

```python notest
       27
       28  _BATCH_WMS_AUTH: dict[str, t.JsonValue] = {
       29      "base_url": "https://wms.example.oraclecloud.com",
       30      "username": "wms_batch_user",
>>>    31      "password": "wms_batch_pass",
       32  }
       33  BATCH_CONFIG: Final[t.JsonMapping] = MappingProxyType({
       34      "wms_auth": _BATCH_WMS_AUTH,
       35      "batch_size": 500,
```

**Decisão**:

### 3 · 🟡 MEDIUM · Use of Hardcoded Passwords

**Local**: `examples/04_factory_usage.py:37` · **CWE**: -

```python notest
       33
       34  TARGET_CONFIG: Final[Mapping[str, str]] = MappingProxyType({
       35      "base_url": "https://wms.example.oraclecloud.com",
       36      "username": "wms_target_user",
>>>    37      "password": "wms_target_pass",
       38  })
       39
       40
       41  @flext_monitor_function(monitor)
```

**Decisão**:

### 4 · 🟡 MEDIUM · Use of Hardcoded Passwords

**Local**: `src/flext_target_oracle_wms/cli.py:93` · **CWE**: -

```python notest
       89              m.TargetOracleWms.WmsTargetConfig.model_validate({
       90                  "wms_auth": {
       91                      "base_url": "https://invalid.wms.ocs.oraclecloud.com",
       92                      "username": "oracle",
>>>    93                      "password": "oracle",
       94                  }
       95              })
       96          )
       97
```

**Decisão**:
