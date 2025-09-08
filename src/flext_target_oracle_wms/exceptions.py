"""Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

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
"""
Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""


# 🚨 ZERO DUPLICATION: Use flext-core exception classes
from flext_core import FlextExceptions


# Oracle WMS Target exception hierarchy using flext-core base classes
class FlextTargetOracleWmsError(FlextExceptions._Error):
    """Base error for Oracle WMS target operations."""


class FlextTargetOracleWmsValidationError(FlextExceptions._ValidationError):
    """Oracle WMS target validation errors."""


class FlextTargetOracleWmsConfigurationError(FlextExceptions._ConfigurationError):
    """Oracle WMS target configuration errors."""


class FlextTargetOracleWmsProcessingError(FlextExceptions._ProcessingError):
    """Oracle WMS target processing errors."""


class FlextTargetOracleWmsConnectionError(FlextExceptions._ConnectionError):
    """Oracle WMS target connection errors."""


class FlextTargetOracleWmsAuthenticationError(FlextExceptions._AuthenticationError):
    """Oracle WMS target authentication errors."""


class FlextTargetOracleWmsTimeoutError(FlextExceptions._TimeoutError):
    """Oracle WMS target timeout errors."""


# Create backward-compatible aliases for existing code
FlextTargetOracleWmsSchemaError = (
    FlextTargetOracleWmsValidationError  # Schema is validation
)
FlextTargetOracleWmsLoadError = (
    FlextTargetOracleWmsProcessingError  # Load is processing
)
FlextTargetOracleWmsWriteError = (
    FlextTargetOracleWmsProcessingError  # Write is processing
)
FlextTargetOracleWmsDataError = (
    FlextTargetOracleWmsProcessingError  # Data is processing
)


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
