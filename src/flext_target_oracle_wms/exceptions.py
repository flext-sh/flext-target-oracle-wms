"""Oracle WMS target exception hierarchy using flext-core patterns.

Copyright (c) 2025 FLEXT Contributors
SPDX-License-Identifier: MIT

Domain-specific exceptions for Oracle WMS target operations inheriting from flext-core.
"""

from __future__ import annotations

from flext_core.exceptions import (
    FlextAuthenticationError,
    FlextConfigurationError,
    FlextConnectionError,
    FlextError,
    FlextProcessingError,
    FlextTimeoutError,
    FlextValidationError,
)


class FlextTargetOracleWmsError(FlextError):
    """Base exception for Oracle WMS target operations."""

    def __init__(
        self,
        message: str = "Oracle WMS target error",
        warehouse_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS target error with context."""
        context = kwargs.copy()
        if warehouse_name is not None:
            context["warehouse_name"] = warehouse_name

        super().__init__(message, error_code="ORACLE_WMS_TARGET_ERROR", context=context)


class FlextTargetOracleWmsConnectionError(FlextConnectionError):
    """Oracle WMS target connection errors."""

    def __init__(
        self,
        message: str = "Oracle WMS target connection failed",
        wms_endpoint: str | None = None,
        database_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS target connection error with context."""
        context = kwargs.copy()
        if wms_endpoint is not None:
            context["wms_endpoint"] = wms_endpoint
        if database_name is not None:
            context["database_name"] = database_name

        super().__init__(f"Oracle WMS target connection: {message}", **context)


class FlextTargetOracleWmsAuthenticationError(FlextAuthenticationError):
    """Oracle WMS target authentication errors."""

    def __init__(
        self,
        message: str = "Oracle WMS target authentication failed",
        username: str | None = None,
        warehouse_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS target authentication error with context."""
        context = kwargs.copy()
        if username is not None:
            context["username"] = username
        if warehouse_name is not None:
            context["warehouse_name"] = warehouse_name

        super().__init__(f"Oracle WMS target auth: {message}", **context)


class FlextTargetOracleWmsValidationError(FlextValidationError):
    """Oracle WMS target validation errors."""

    def __init__(
        self,
        message: str = "Oracle WMS target validation failed",
        field: str | None = None,
        value: object = None,
        entity_type: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS target validation error with context."""
        validation_details = {}
        if field is not None:
            validation_details["field"] = field
        if value is not None:
            validation_details["value"] = str(value)[:100]  # Truncate long values

        context = kwargs.copy()
        if entity_type is not None:
            context["entity_type"] = entity_type

        super().__init__(
            f"Oracle WMS target validation: {message}",
            validation_details=validation_details,
            context=context,
        )


class FlextTargetOracleWmsConfigurationError(FlextConfigurationError):
    """Oracle WMS target configuration errors."""

    def __init__(
        self,
        message: str = "Oracle WMS target configuration error",
        config_key: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS target configuration error with context."""
        context = kwargs.copy()
        if config_key is not None:
            context["config_key"] = config_key

        super().__init__(f"Oracle WMS target config: {message}", **context)


class FlextTargetOracleWmsProcessingError(FlextProcessingError):
    """Oracle WMS target processing errors."""

    def __init__(
        self,
        message: str = "Oracle WMS target processing failed",
        entity_type: str | None = None,
        processing_stage: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS target processing error with context."""
        context = kwargs.copy()
        if entity_type is not None:
            context["entity_type"] = entity_type
        if processing_stage is not None:
            context["processing_stage"] = processing_stage

        super().__init__(f"Oracle WMS target processing: {message}", **context)


class FlextTargetOracleWmsInventoryError(FlextTargetOracleWmsError):
    """Oracle WMS target inventory-specific errors."""

    def __init__(
        self,
        message: str = "Oracle WMS target inventory error",
        item_code: str | None = None,
        location: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS target inventory error with context."""
        context = kwargs.copy()
        if item_code is not None:
            context["item_code"] = item_code
        if location is not None:
            context["location"] = location

        super().__init__(f"Oracle WMS target inventory: {message}", **context)


class FlextTargetOracleWmsShipmentError(FlextTargetOracleWmsError):
    """Oracle WMS target shipment-specific errors."""

    def __init__(
        self,
        message: str = "Oracle WMS target shipment error",
        shipment_id: str | None = None,
        carrier: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS target shipment error with context."""
        context = kwargs.copy()
        if shipment_id is not None:
            context["shipment_id"] = shipment_id
        if carrier is not None:
            context["carrier"] = carrier

        super().__init__(f"Oracle WMS target shipment: {message}", **context)


class FlextTargetOracleWmsTimeoutError(FlextTimeoutError):
    """Oracle WMS target timeout errors."""

    def __init__(
        self,
        message: str = "Oracle WMS target operation timed out",
        operation: str | None = None,
        timeout_seconds: float | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS target timeout error with context."""
        context = kwargs.copy()
        if operation is not None:
            context["operation"] = operation
        if timeout_seconds is not None:
            context["timeout_seconds"] = timeout_seconds

        super().__init__(f"Oracle WMS target timeout: {message}", **context)


class FlextTargetOracleWmsLoadError(FlextTargetOracleWmsError):
    """Oracle WMS target data loading errors."""

    def __init__(
        self,
        message: str = "Oracle WMS target load error",
        table_name: str | None = None,
        record_count: int | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS target load error with context."""
        context = kwargs.copy()
        if table_name is not None:
            context["table_name"] = table_name
        if record_count is not None:
            context["record_count"] = record_count

        super().__init__(f"Oracle WMS target load: {message}", **context)


class FlextTargetOracleWmsTransformationError(FlextProcessingError):
    """Oracle WMS target data transformation errors."""

    def __init__(
        self,
        message: str = "Oracle WMS target transformation failed",
        transformation_type: str | None = None,
        input_format: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize Oracle WMS target transformation error with context."""
        context = kwargs.copy()
        if transformation_type is not None:
            context["transformation_type"] = transformation_type
        if input_format is not None:
            context["input_format"] = input_format

        super().__init__(f"Oracle WMS target transformation: {message}", **context)


__all__ = [
    "FlextTargetOracleWmsAuthenticationError",
    "FlextTargetOracleWmsConfigurationError",
    "FlextTargetOracleWmsConnectionError",
    "FlextTargetOracleWmsError",
    "FlextTargetOracleWmsInventoryError",
    "FlextTargetOracleWmsLoadError",
    "FlextTargetOracleWmsProcessingError",
    "FlextTargetOracleWmsShipmentError",
    "FlextTargetOracleWmsTimeoutError",
    "FlextTargetOracleWmsTransformationError",
    "FlextTargetOracleWmsValidationError",
]
