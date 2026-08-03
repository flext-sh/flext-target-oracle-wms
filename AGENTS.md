# AGENTS.md — flext-target-oracle-wms

> **Parent workspace law** lives in [`../AGENTS.md`](../AGENTS.md) — read it first.
> Universal engineering core: `~/.agents/UNIVERSAL_CORE.md`. Composition: global skills + parent/root `AGENTS.md` + this scope delta. Do not re-embed universal law.
>
> **Standalone / independent mode:** when `../AGENTS.md` does not resolve, pin the parent raw `AGENTS.md` URL to the same branch/release as this package (never `main`).

<!-- AIHUB-AGENTS-SCOPE-LOCAL-BEGIN -->
**Package:** `flext_target_oracle_wms` · deps: `flext-cli`, `flext-core`, `flext-db-oracle`, `flext-meltano`, `flext-observability`, `flext-oracle-wms`

## Overview

Singer **target** (loader) for Oracle WMS. Thin driver over `flext-meltano` (ADR-006), delegating WMS logic to `flext-oracle-wms`.

## Structure

```text
src/flext_target_oracle_wms/
├── api.py            # FlextTargetOracleWmsService(FlextMeltanoTargetServiceBase) — delegates sink creation
├── target.py cli.py
├── _utilities/service_runtime.py   # FlextTargetOracleWmsServiceRuntime — WMS target + sink creation
├── constants.py typings.py protocols.py models.py utilities.py   # AUTO-GENERATED facets
```

## Code Map

| Symbol | Kind | Location | Role |
|--------|------|----------|------|
| `FlextTargetOracleWmsService` | class | `api.py` | target service; delegates to the runtime |
| `FlextTargetOracleWmsServiceRuntime` | class | `_utilities/service_runtime.py` | WMS sink creation + transform |

## Conventions (specific to this package)

- **One canonical service path** through `api.py` + `service_runtime.py` — no parallel `simple_api` branch. WMS config uses namespaced settings.

## Commands

```bash
make check PROJECT=flext-target-oracle-wms
make test  PROJECT=flext-target-oracle-wms       # tests/{unit,integration,examples}
```
<!-- AIHUB-AGENTS-SCOPE-LOCAL-END -->
