"""Oracle WMS Target Exception Hierarchy.

Domain-specific exceptions for Oracle WMS target operations using factory pattern to eliminate duplication.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import FlextCore


# Oracle WMS Target exception hierarchy using flext-core base classes
class FlextTargetOracleWmsError(FlextCore.Exceptions.Error):
    """Base error for Oracle WMS target operations."""


class FlextTargetOracleWmsValidationError(FlextCore.Exceptions.ValidationError):
    """Oracle WMS target validation errors."""


class FlextTargetOracleWmsConfigurationError(FlextCore.Exceptions.ConfigurationError):
    """Oracle WMS target configuration errors."""


class FlextTargetOracleWmsProcessingError(FlextCore.Exceptions.ProcessingError):
    """Oracle WMS target processing errors."""


class FlextTargetOracleWmsConnectionError(FlextCore.Exceptions.ConnectionError):
    """Oracle WMS target connection errors."""


class FlextTargetOracleWmsAuthenticationError(FlextCore.Exceptions.AuthenticationError):
    """Oracle WMS target authentication errors."""


class FlextTargetOracleWmsTimeoutError(FlextCore.Exceptions.TimeoutError):
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
