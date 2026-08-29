# Triagem SonarCloud — flext-sh/flext-target-oracle-wms

Gerado do dump da plataforma SonarCloud (2026-08-06).

Bead: `mro-2wjm.22`

## Resumo

**19 issues** — BLOCKER 0, CRITICAL 0, MAJOR 6, MINOR 13
Tipos: VULNERABILITY 5, BUG 0, CODE_SMELL 14 · **Debt total: 90min**

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

## Como usar

Cada issue traz a **mensagem do SonarQube** (descreve o problema e o impacto), o **código real** (linha `>>>`), o tipo e o effort estimado.
**Decisão**: `corrigir` / `falso-positivo` (marcar na plataforma com justificativa) / `risco-aceito`. Ordem: BLOCKER → CRITICAL → VULNERABILITY → MAJOR. CODE_SMELL em volume pede correção de padrão.

## Issues

### 1 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8264`
**Local**: `.github/workflows/docs.yml:18` · **Effort**: 5min

> Move this read permission from workflow level to job level.

```yaml
       14        - ".github/workflows/docs.yml"
       15    workflow_dispatch:
       16  
       17  permissions:
>>>    18    contents: read
       19    pages: write
       20    id-token: write
       21  
       22  concurrency:
```

**Decisão**: pendente

### 2 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8233`
**Local**: `.github/workflows/docs.yml:19` · **Effort**: 5min

> Move this write permission from workflow level to job level.

```yaml
       15    workflow_dispatch:
       16  
       17  permissions:
       18    contents: read
>>>    19    pages: write
       20    id-token: write
       21  
       22  concurrency:
       23    group: pages
```

**Decisão**: pendente

### 3 · 🟡 MAJOR · VULNERABILITY · `githubactions:S8233`
**Local**: `.github/workflows/docs.yml:20` · **Effort**: 5min

> Move this write permission from workflow level to job level.

```yaml
       16  
       17  permissions:
       18    contents: read
       19    pages: write
>>>    20    id-token: write
       21  
       22  concurrency:
       23    group: pages
       24    cancel-in-progress: false
```

**Decisão**: pendente

### 4 · 🟡 MAJOR · VULNERABILITY · `text:S8565`
**Local**: `pyproject.toml:-` · **Effort**: 5min

> Dependency versions are not predictable if the lock file (uv.lock, poetry.lock, pdm.lock or pylock.toml) is missing.

**Decisão**: pendente

### 5 · 🟡 MAJOR · VULNERABILITY · `python:S2068`
**Local**: `src/flext_target_oracle_wms/cli.py:93` · **Effort**: 30min

> "password" detected here, review this potentially hard-coded credential.

```python
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

**Decisão**: pendente

### 6 · 🟡 MAJOR · CODE_SMELL · `python:S5778`
**Local**: `tests/unit/test_target.py:107` · **Effort**: 5min

> Refactor this exception test to have only one invocation possibly throwing an exception.

```python
      103  
      104      def test_invalid_load_method_rejected(self) -> None:
      105          # load_method is typed as the LoadMethods.Method enum, so an unknown value
      106          # is rejected at construction (data-shape validation lives in the model).
>>>   107          with pytest.raises(c.ValidationError):
      108              m.TargetOracleWms.WmsTargetConfig.model_validate({
      109                  **_valid_config(),
      110                  "load_method": "BOGUS",
      111              })
```

**Decisão**: pendente

### 7 · ⚪ MINOR · CODE_SMELL · `python:S7504`
**Local**: `conftest.py:20` · **Effort**: 5min

> Remove this unnecessary `list()` call on an already iterable object.

```python
       16      if (
       17          existing_package is None
       18          or Path(getattr(existing_package, "__file__", "")).resolve() != init_file
       19      ):
>>>    20          for module_name in list(sys.modules):
       21              if module_name == package_name or module_name.startswith(
       22                  f"{package_name}."
       23              ):
       24                  sys.modules.pop(module_name, None)
```

**Decisão**: pendente

### 8 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_target_oracle_wms/utilities.py:24` · **Effort**: 2min

> Rename this field "Client" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
       20  
       21      class TargetOracleWms:
       22          """Project-local namespace aggregating Client and Helpers public classes."""
       23  
>>>    24          Client = FlextTargetOracleWmsUtilitiesClient
       25          Helpers = FlextTargetOracleWmsUtilitiesHelpers
       26  
       27          # Direct nested-class access for canonical u.TargetOracleWms.<Class> usage
       28          CatalogManager = FlextTargetOracleWmsUtilitiesClient.CatalogManager
```

**Decisão**: pendente

### 9 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_target_oracle_wms/utilities.py:25` · **Effort**: 2min

> Rename this field "Helpers" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
       21      class TargetOracleWms:
       22          """Project-local namespace aggregating Client and Helpers public classes."""
       23  
       24          Client = FlextTargetOracleWmsUtilitiesClient
>>>    25          Helpers = FlextTargetOracleWmsUtilitiesHelpers
       26  
       27          # Direct nested-class access for canonical u.TargetOracleWms.<Class> usage
       28          CatalogManager = FlextTargetOracleWmsUtilitiesClient.CatalogManager
       29          StreamProcessor = FlextTargetOracleWmsUtilitiesClient.StreamProcessor
```

**Decisão**: pendente

### 10 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_target_oracle_wms/utilities.py:28` · **Effort**: 2min

> Rename this field "CatalogManager" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
       24          Client = FlextTargetOracleWmsUtilitiesClient
       25          Helpers = FlextTargetOracleWmsUtilitiesHelpers
       26  
       27          # Direct nested-class access for canonical u.TargetOracleWms.<Class> usage
>>>    28          CatalogManager = FlextTargetOracleWmsUtilitiesClient.CatalogManager
       29          StreamProcessor = FlextTargetOracleWmsUtilitiesClient.StreamProcessor
       30          Target = FlextTargetOracleWmsUtilitiesClient.Target
       31          Validation = FlextTargetOracleWmsUtilitiesHelpers.Validation
       32          WMSDataTransformer = FlextTargetOracleWmsUtilitiesHelpers.WMSDataTransformer
```

**Decisão**: pendente

### 11 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_target_oracle_wms/utilities.py:29` · **Effort**: 2min

> Rename this field "StreamProcessor" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
       25          Helpers = FlextTargetOracleWmsUtilitiesHelpers
       26  
       27          # Direct nested-class access for canonical u.TargetOracleWms.<Class> usage
       28          CatalogManager = FlextTargetOracleWmsUtilitiesClient.CatalogManager
>>>    29          StreamProcessor = FlextTargetOracleWmsUtilitiesClient.StreamProcessor
       30          Target = FlextTargetOracleWmsUtilitiesClient.Target
       31          Validation = FlextTargetOracleWmsUtilitiesHelpers.Validation
       32          WMSDataTransformer = FlextTargetOracleWmsUtilitiesHelpers.WMSDataTransformer
       33          WMSSchemaMapper = FlextTargetOracleWmsUtilitiesHelpers.WMSSchemaMapper
```

**Decisão**: pendente

### 12 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_target_oracle_wms/utilities.py:30` · **Effort**: 2min

> Rename this field "Target" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
       26  
       27          # Direct nested-class access for canonical u.TargetOracleWms.<Class> usage
       28          CatalogManager = FlextTargetOracleWmsUtilitiesClient.CatalogManager
       29          StreamProcessor = FlextTargetOracleWmsUtilitiesClient.StreamProcessor
>>>    30          Target = FlextTargetOracleWmsUtilitiesClient.Target
       31          Validation = FlextTargetOracleWmsUtilitiesHelpers.Validation
       32          WMSDataTransformer = FlextTargetOracleWmsUtilitiesHelpers.WMSDataTransformer
       33          WMSSchemaMapper = FlextTargetOracleWmsUtilitiesHelpers.WMSSchemaMapper
       34          WMSTableManager = FlextTargetOracleWmsUtilitiesHelpers.WMSTableManager
```

**Decisão**: pendente

### 13 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_target_oracle_wms/utilities.py:31` · **Effort**: 2min

> Rename this field "Validation" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
       27          # Direct nested-class access for canonical u.TargetOracleWms.<Class> usage
       28          CatalogManager = FlextTargetOracleWmsUtilitiesClient.CatalogManager
       29          StreamProcessor = FlextTargetOracleWmsUtilitiesClient.StreamProcessor
       30          Target = FlextTargetOracleWmsUtilitiesClient.Target
>>>    31          Validation = FlextTargetOracleWmsUtilitiesHelpers.Validation
       32          WMSDataTransformer = FlextTargetOracleWmsUtilitiesHelpers.WMSDataTransformer
       33          WMSSchemaMapper = FlextTargetOracleWmsUtilitiesHelpers.WMSSchemaMapper
       34          WMSTableManager = FlextTargetOracleWmsUtilitiesHelpers.WMSTableManager
       35          WMSTypeConverter = FlextTargetOracleWmsUtilitiesHelpers.WMSTypeConverter
```

**Decisão**: pendente

### 14 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_target_oracle_wms/utilities.py:32` · **Effort**: 2min

> Rename this field "WMSDataTransformer" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
       28          CatalogManager = FlextTargetOracleWmsUtilitiesClient.CatalogManager
       29          StreamProcessor = FlextTargetOracleWmsUtilitiesClient.StreamProcessor
       30          Target = FlextTargetOracleWmsUtilitiesClient.Target
       31          Validation = FlextTargetOracleWmsUtilitiesHelpers.Validation
>>>    32          WMSDataTransformer = FlextTargetOracleWmsUtilitiesHelpers.WMSDataTransformer
       33          WMSSchemaMapper = FlextTargetOracleWmsUtilitiesHelpers.WMSSchemaMapper
       34          WMSTableManager = FlextTargetOracleWmsUtilitiesHelpers.WMSTableManager
       35          WMSTypeConverter = FlextTargetOracleWmsUtilitiesHelpers.WMSTypeConverter
       36          create_record_message = staticmethod(
```

**Decisão**: pendente

### 15 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_target_oracle_wms/utilities.py:33` · **Effort**: 2min

> Rename this field "WMSSchemaMapper" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
       29          StreamProcessor = FlextTargetOracleWmsUtilitiesClient.StreamProcessor
       30          Target = FlextTargetOracleWmsUtilitiesClient.Target
       31          Validation = FlextTargetOracleWmsUtilitiesHelpers.Validation
       32          WMSDataTransformer = FlextTargetOracleWmsUtilitiesHelpers.WMSDataTransformer
>>>    33          WMSSchemaMapper = FlextTargetOracleWmsUtilitiesHelpers.WMSSchemaMapper
       34          WMSTableManager = FlextTargetOracleWmsUtilitiesHelpers.WMSTableManager
       35          WMSTypeConverter = FlextTargetOracleWmsUtilitiesHelpers.WMSTypeConverter
       36          create_record_message = staticmethod(
       37              FlextTargetOracleWmsUtilitiesHelpers.create_record_message
```

**Decisão**: pendente

### 16 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_target_oracle_wms/utilities.py:34` · **Effort**: 2min

> Rename this field "WMSTableManager" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
       30          Target = FlextTargetOracleWmsUtilitiesClient.Target
       31          Validation = FlextTargetOracleWmsUtilitiesHelpers.Validation
       32          WMSDataTransformer = FlextTargetOracleWmsUtilitiesHelpers.WMSDataTransformer
       33          WMSSchemaMapper = FlextTargetOracleWmsUtilitiesHelpers.WMSSchemaMapper
>>>    34          WMSTableManager = FlextTargetOracleWmsUtilitiesHelpers.WMSTableManager
       35          WMSTypeConverter = FlextTargetOracleWmsUtilitiesHelpers.WMSTypeConverter
       36          create_record_message = staticmethod(
       37              FlextTargetOracleWmsUtilitiesHelpers.create_record_message
       38          )
```

**Decisão**: pendente

### 17 · ⚪ MINOR · CODE_SMELL · `python:S116`
**Local**: `src/flext_target_oracle_wms/utilities.py:35` · **Effort**: 2min

> Rename this field "WMSTypeConverter" to match the regular expression ^[_a-z][_a-z0-9]*$.

```python
       31          Validation = FlextTargetOracleWmsUtilitiesHelpers.Validation
       32          WMSDataTransformer = FlextTargetOracleWmsUtilitiesHelpers.WMSDataTransformer
       33          WMSSchemaMapper = FlextTargetOracleWmsUtilitiesHelpers.WMSSchemaMapper
       34          WMSTableManager = FlextTargetOracleWmsUtilitiesHelpers.WMSTableManager
>>>    35          WMSTypeConverter = FlextTargetOracleWmsUtilitiesHelpers.WMSTypeConverter
       36          create_record_message = staticmethod(
       37              FlextTargetOracleWmsUtilitiesHelpers.create_record_message
       38          )
       39          create_schema_message = staticmethod(
```

**Decisão**: pendente

### 18 · ⚪ MINOR · CODE_SMELL · `python:S8714`
**Local**: `tests/examples/test_examples.py:229` · **Effort**: 5min

> Remove this try/except block and let the test fail naturally if an exception is raised.

```python
      225          example_files = list(examples_dir.glob("*.py"))
      226          for example_file in example_files:
      227              if example_file.name == "__init__.py":
      228                  continue
>>>   229              try:
      230                  content = example_file.read_text(encoding="utf-8")
      231                  compiled = compile(content, str(example_file), "exec")
      232              except SyntaxError as e:
      233                  pytest.fail(f"Syntax error in {example_file.name}: {e}")
```

**Decisão**: pendente

### 19 · ⚪ MINOR · CODE_SMELL · `python:S8714`
**Local**: `tests/examples/test_examples.py:234` · **Effort**: 5min

> Remove this try/except block and let the test fail naturally if an exception is raised.

```python
      230                  content = example_file.read_text(encoding="utf-8")
      231                  compiled = compile(content, str(example_file), "exec")
      232              except SyntaxError as e:
      233                  pytest.fail(f"Syntax error in {example_file.name}: {e}")
>>>   234              try:
      235                  tm.that(compiled, none=False)
      236              except (
      237                  ValueError,
      238                  TypeError,
```

**Decisão**: pendente
