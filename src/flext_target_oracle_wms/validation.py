"""Data validation for Oracle WMS target using DI pattern.

This module provides WMS-specific data validation using dependency injection
to access Oracle validation services. Follows Clean Architecture principles.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any

import structlog
from flext_core import FlextError as FlextServiceError, get_logger
from jsonschema import Draft7Validator

logger = get_logger(__name__)

if TYPE_CHECKING:
    from collections.abc import Mapping

struct_logger = structlog.get_logger(__name__)

# Oracle validation provider will be injected at runtime
_validation_provider: Any | None = None


def set_validation_provider(provider: Any) -> None:
    """Set the Oracle validation provider via dependency injection.

    Args:
        provider: Oracle validation provider implementation

    """
    global _validation_provider
    _validation_provider = provider


def _get_validation_provider() -> Any:
    """Get validation provider or raise error if not set.

    Returns:
        Oracle validation provider

    Raises:
        RuntimeError: If no validation provider has been injected

    """
    if _validation_provider is None:
        error_msg = "Oracle validation provider not injected - call set_validation_provider() first"
        logger.error(error_msg)
        raise FlextServiceError(error_msg)
    return _validation_provider


class WMSDataValidator:
    """Validate data according to WMS requirements and schema using DI pattern.

    Uses dependency injection to access Oracle WMS validation patterns
    while adding JSON schema validation capability.
    """

    def __init__(self, schema: dict[str, Any]) -> None:
        """Initialize validator.

        Args:
        ----
            schema: JSON schema for validation

        """
        self.schema = schema
        self._validator = Draft7Validator(schema)

    def validate_record(self, record: dict[str, Any]) -> list[str]:
        """Validate a single record using DI.

        Args:
        ----
            record: Record to validate

        Returns:
        -------
            List of validation errors (empty if valid)

        """
        errors: list[str] = []
        # JSON schema validation
        schema_errors = self._validate_schema(record)
        errors.extend(schema_errors)

        # Use injected Oracle WMS validation provider
        try:
            provider = _get_validation_provider()
            wms_validation_result = provider.validate_wms_record(record)
            if wms_validation_result.is_success:
                wms_errors = wms_validation_result.data or []
                errors.extend(wms_errors)
            else:
                errors.append(f"WMS validation failed: {wms_validation_result.error}")
        except RuntimeError as e:
            # Provider not injected - log warning but continue with schema only
            logger.warning(f"Oracle validation provider not available: {e}")

        return errors

    def _validate_schema(self, record: dict[str, Any]) -> list[str]:
        """Validate against JSON schema."""
        errors: list[str] = []
        for error in self._validator.iter_errors(record):
            error_path = ".".join(str(p) for p in error.path)
            errors.append(f"Schema validation error at {error_path}: {error.message}")
        return errors

    def _is_valid_datetime(self, value: object) -> bool:
        """Check if value is a valid datetime string."""
        if not isinstance(value, str):
            return False
        # Try common ISO 8601 formats
        formats = [
            "%Y-%m-%dT%H:%M:%S.%fZ",
            "%Y-%m-%dT%H:%M:%SZ",
            "%Y-%m-%dT%H:%M:%S",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d",
        ]
        for fmt in formats:
            try:
                # Parse as naive datetime, then make timezone aware
                datetime.strptime(value, fmt).replace(tzinfo=UTC)
            except ValueError:
                continue
            else:
                # If we reach here, parsing was successful
                return True
        # Try ISO format parsing as fallback
        try:
            datetime.fromisoformat(value)
        except (ValueError, TypeError, AttributeError) as e:
            logger.debug("ISO format validation failed: %s", e)
            return False
        else:
            return True

    def _is_valid_decimal(self, value: object, precision: int, scale: int) -> bool:
        """Check if value is a valid decimal with given precision and scale."""
        try:
            # Convert to string to check precision
            if value is None:
                return False
            str_value = str(float(value)) if isinstance(value, (int, float, str)) else str(value)
            # Remove negative sign for counting
            str_value = str_value.removeprefix("-")
            # Split by decimal point
            parts = str_value.split(".")
            # Check total digits
            total_digits = len(parts[0]) + (len(parts[1]) if len(parts) > 1 else 0)
            if total_digits > precision:
                return False
            # Check decimal places
            return not (len(parts) > 1 and len(parts[1]) > scale)
        except (ValueError, TypeError):
            return False

    def _get_valid_statuses(self, _record: dict[str, Any]) -> list[str]:
        """Get valid status values based on record type."""
        # This would be customized based on entity type
        # For now, return common WMS statuses
        if "order" in self.schema.get("title", "").lower():
            return ["CREATED", "ALLOCATED", "PICKED", "PACKED", "SHIPPED", "CANCELLED"]
        if "inventory" in self.schema.get("title", "").lower():
            return ["AVAILABLE", "ALLOCATED", "DAMAGED", "HOLD", "QUARANTINE"]
        if "task" in self.schema.get("title", "").lower():
            return ["PENDING", "ASSIGNED", "IN_PROGRESS", "COMPLETED", "CANCELLED"]
        return []

    def sanitize_record(self, record: dict[str, Any]) -> dict[str, Any]:
        """Sanitize record data for WMS compatibility using DI.

        Args:
        ----
            record: Record to sanitize

        Returns:
        -------
            Sanitized record

        """
        sanitized = record.copy()

        try:
            provider = _get_validation_provider()

            # Convert datetime fields to ISO format
            datetime_fields = provider.datetime_fields
            for field in datetime_fields:
                if sanitized.get(field):
                    sanitized[field] = self._format_datetime(sanitized[field])

            # Ensure decimal values are properly formatted
            decimal_fields = provider.decimal_fields
            for field in decimal_fields:
                if field in sanitized and sanitized[field] is not None:
                    # WMS requires decimals as strings to preserve precision
                    sanitized[field] = str(sanitized[field])

        except RuntimeError:
            # Provider not injected - use fallback behavior
            logger.warning(
                "Oracle validation provider not available, using fallback sanitization",
            )

        # Upper case certain fields
        uppercase_fields = ["company_code", "facility_code", "item_code", "lpn"]
        for field in uppercase_fields:
            if field in sanitized and isinstance(sanitized[field], str):
                sanitized[field] = sanitized[field].upper()

        # Remove null values if not allowed
        if not self.schema.get("additionalProperties", True):
            sanitized = {k: v for k, v in sanitized.items() if v is not None}

        return sanitized

    def _format_datetime(self, value: object) -> str:
        """Format datetime value to ISO 8601."""
        if isinstance(value, str):
            try:
                dt = datetime.fromisoformat(value)
                return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")[:-3] + "Z"
            except (ValueError, TypeError, AttributeError) as e:
                logger.debug("Datetime formatting error: %s", e)
                return value
        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")[:-3] + "Z"
        if value is not None:
            return str(value)
        return ""

    def validate_batch(self, records: list[dict[str, Any]]) -> dict[str, Any]:
        """Validate a batch of records.

        Args:
        ----
            records: List of records to validate

        Returns:
        -------
            Validation report

        """
        report: dict[str, Any] = {
            "total_records": len(records),
            "valid_records": 0,
            "invalid_records": 0,
            "errors_by_record": {},
            "error_summary": {},
        }
        for i, record in enumerate(records):
            errors = self.validate_record(record)
            if errors:
                report["invalid_records"] += 1
                report["errors_by_record"][i] = errors
                # Summarize errors
                for error in errors:
                    error_type = error.split(":")[0]
                    report["error_summary"][error_type] = (
                        report["error_summary"].get(error_type, 0) + 1
                    )
            else:
                report["valid_records"] += 1
        return report
