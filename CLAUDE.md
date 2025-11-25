# FLEXT-Target-Oracle-WMS Project Guidelines

**Reference**: See [../CLAUDE.md](../CLAUDE.md) for FLEXT ecosystem standards and general rules.

---

## Project Overview

**FLEXT-Target-Oracle-WMS** is the Singer target for Oracle Warehouse Management System loading in the FLEXT ecosystem.

**Version**: 0.9.0  
**Status**: Production-ready  
**Python**: 3.13+

**CRITICAL INTEGRATION DEPENDENCIES**:
- **flext-meltano**: MANDATORY for ALL Singer operations (ZERO TOLERANCE for direct singer-sdk without flext-meltano)
- **flext-oracle-wms**: MANDATORY for ALL Oracle WMS operations (ZERO TOLERANCE for bypassing WMS domain)
- **flext-db-oracle**: MANDATORY for ALL Oracle Database operations (ZERO TOLERANCE for direct SQLAlchemy/oracledb imports)
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

### Singer Target Implementation

```python
from flext_core import FlextResult
from flext_target_oracle_wms import FlextTargetOracleWms

target = FlextTargetOracleWms()

# Process records
result = target.write_record(record)
if result.is_success:
    print("Record written to Oracle WMS")
```

---

## Critical Development Rules

### ZERO TOLERANCE Policies

**ABSOLUTELY FORBIDDEN**:
- ❌ Direct singer-sdk imports (use flext-meltano)
- ❌ Direct Oracle WMS operations (use flext-oracle-wms)
- ❌ Direct SQLAlchemy/oracledb imports (use flext-db-oracle)
- ❌ Exception-based error handling (use FlextResult)
- ❌ Type ignores or `Any` types

**MANDATORY**:
- ✅ Use `FlextResult[T]` for all operations
- ✅ Use flext-meltano for Singer operations
- ✅ Use flext-oracle-wms for WMS operations
- ✅ Use flext-db-oracle for Oracle operations
- ✅ Complete type annotations
- ✅ Zero Ruff violations

---

**Additional Resources**: [../CLAUDE.md](../CLAUDE.md) (workspace), [README.md](README.md) (overview)
