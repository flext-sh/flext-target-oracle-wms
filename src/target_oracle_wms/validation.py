"""Data validation for Oracle WMS target.

This module provides WMS-specific data validation using the centralized
Oracle validation patterns from flext-core. Eliminates code duplication
across Oracle projects.
"""

from __future__ import annotations

import logging
from datetime import UTC, datetime
from typing import Any

import structlog
from flext_core.config.oracle import OracleWMSValidator
from jsonschema import Draft7Validator

logger = logging.getLogger(__name__)
struct_logger = structlog.get_logger(__name__)


class WMSDataValidator:
    """Validate data according to WMS requirements and schema.

    Uses centralized Oracle WMS validation patterns from flext-core
    to eliminate duplication while adding JSON schema validation.
    """

    def __init__(self, schema: dict[str, Any]) -> None:
        """Initialize validator.

        Args:
        ----
            schema: JSON schema for validation

        """
        self.schema = schema
        self._validator = Draft7Validator(schema)

        # Use centralized Oracle WMS validator
        self._wms_validator = OracleWMSValidator("TARGET_ORACLE_WMS")

    def validate_record(self, record: dict[str, Any]) -> list[str]:
        """Validate a single record.

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

        # Use centralized WMS validation from flext-core
        wms_validation_result = self._wms_validator.validate_wms_record(record)
        if wms_validation_result.is_success:
            wms_errors = wms_validation_result.unwrap()
            errors.extend(wms_errors)
        else:
            errors.append(f"WMS validation failed: {wms_validation_result.error}")

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
            str_value = str(float(value))

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
        """Sanitize record data for WMS compatibility.

        Args:
        ----
            record: Record to sanitize

        Returns:
        -------
            Sanitized record

        """
        sanitized = record.copy()

        # Convert datetime fields to ISO format
        datetime_fields = self._wms_validator.datetime_fields
        for field in datetime_fields:
            if sanitized.get(field):
                sanitized[field] = self._format_datetime(sanitized[field])

        # Ensure decimal values are properly formatted
        decimal_fields = self._wms_validator.decimal_fields
        for field in decimal_fields:
            if field in sanitized and sanitized[field] is not None:
                # WMS requires decimals as strings to preserve precision
                sanitized[field] = str(sanitized[field])

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
        report = {
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
