"""🚨 ARCHITECTURAL COMPLIANCE: ZERO EXCEPTION DUPLICATION using flext-core Factory.

✅ REFATORAÇÃO COMPLETA: 230+ linhas de código duplicado ELIMINADAS.

- ANTES: 286 linhas com 11 classes manuais de exceptions + helpers
- DEPOIS: <60 linhas usando factory pattern limpo e DRY
- REDUÇÃO: 230+ linhas eliminadas = ~80% redução
- PADRÃO: Usa create_module_exception_classes() de flext-core
- ARQUITETURA: Funcionalidades genéricas permanecem nas bibliotecas abstratas
- EXPOSIÇÃO: API pública correta através do factory pattern

Oracle WMS Target Exception Hierarchy - ZERO DUPLICATION.

Copyright (c) 2025 FLEXT Contributors
SPDX-License-Identifier: MIT

Domain-specific exceptions for Oracle WMS target operations using factory pattern to eliminate duplication.
"""

from __future__ import annotations

# 🚨 ZERO DUPLICATION: Use flext-core exception factory - eliminates 230+ lines
from flext_core import create_module_exception_classes

# Generate all standard exceptions using factory pattern
_target_oracle_wms_exceptions = create_module_exception_classes("flext_target_oracle_wms")

# Export factory-created exception classes (using actual factory keys)
FlextTargetOracleWmsError = _target_oracle_wms_exceptions["FlextTargetOracleWmsError"]
FlextTargetOracleWmsValidationError = _target_oracle_wms_exceptions["FlextTargetOracleWmsValidationError"]
FlextTargetOracleWmsConfigurationError = _target_oracle_wms_exceptions["FlextTargetOracleWmsConfigurationError"]
FlextTargetOracleWmsProcessingError = _target_oracle_wms_exceptions["FlextTargetOracleWmsProcessingError"]
FlextTargetOracleWmsConnectionError = _target_oracle_wms_exceptions["FlextTargetOracleWmsConnectionError"]
FlextTargetOracleWmsAuthenticationError = _target_oracle_wms_exceptions["FlextTargetOracleWmsAuthenticationError"]
FlextTargetOracleWmsTimeoutError = _target_oracle_wms_exceptions["FlextTargetOracleWmsTimeoutError"]

# Create backward-compatible aliases for existing code
FlextTargetOracleWmsSchemaError = FlextTargetOracleWmsValidationError  # Schema is validation
FlextTargetOracleWmsLoadError = FlextTargetOracleWmsProcessingError  # Load is processing
FlextTargetOracleWmsWriteError = FlextTargetOracleWmsProcessingError  # Write is processing
FlextTargetOracleWmsDataError = FlextTargetOracleWmsProcessingError  # Data is processing


__all__ = [
    "FlextTargetOracleWmsAuthenticationError",
    "FlextTargetOracleWmsConfigurationError",
    "FlextTargetOracleWmsConnectionError",
    "FlextTargetOracleWmsDataError",
    "FlextTargetOracleWmsError",
    "FlextTargetOracleWmsLoadError",
    "FlextTargetOracleWmsProcessingError",
    "FlextTargetOracleWmsSchemaError",
    "FlextTargetOracleWmsTimeoutError",
    "FlextTargetOracleWmsValidationError",
    "FlextTargetOracleWmsWriteError",
]
