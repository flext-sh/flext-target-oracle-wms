"""Oracle WMS sink implementation using flext-core patterns."""

from __future__ import annotations

from dataclasses import field
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any

# Import from flext-core for foundational patterns
from flext_core import (
    FlextResult,
    FlextValueObject as FlextDomainBaseModel,
)

# Using Singer SDK directly for SQLSink
# MIGRATED: Singer SDK imports centralized via flext-meltano
from flext_meltano import SQLSink

# Import from new modular architecture

try:
    from sqlalchemy.dialects import oracle
except ImportError:
    oracle = None

if TYPE_CHECKING:
    from flext_target_oracle_wms.target import TargetOracleWMS


class WMSProcessingResult(FlextDomainBaseModel):
    """Result of WMS processing operations using flext-core patterns."""

    processed_count: int = 0
    success_count: int = 0
    error_count: int = 0
    errors: list[str] = field(default_factory=list)

    @property
    def success_rate(self) -> float:
        """Calculate success rate as percentage."""
        if self.processed_count == 0:
            return 0.0
        return (self.success_count / self.processed_count) * 100.0

    def add_success(self) -> None:
        """Record a successful operation."""
        self.processed_count += 1
        self.success_count += 1

    def add_error(self, error_message: str) -> None:
        """Record a failed operation."""
        self.processed_count += 1
        self.error_count += 1
        self.errors.append(error_message)


class OracleWMSSink(SQLSink[Any]):
    """Oracle WMS sink for handling WMS-specific data loading."""

    def __init__(
        self,
        target: TargetOracleWMS,
        stream_name: str,
        schema: dict[str, Any] | None = None,
        key_properties: list[str] | None = None,
    ) -> None:
        """Initialize Oracle WMS sink."""
        super().__init__(target, stream_name, schema, key_properties)
        self.target: TargetOracleWMS = target
        self._processing_result = WMSProcessingResult()

    @property
    def connector(self) -> Any:
        """Get database connector."""
        return self.target.engine

    def setup(self) -> None:
        """Setup the sink."""
        super().setup()
        self.logger.info(
            f"Oracle WMS sink setup completed for stream: {self.stream_name}",
        )

    def process_record(self, record: dict[str, Any], context: dict[str, Any]) -> None:
        """Process a single record with WMS-specific logic."""
        try:
            # Add WMS metadata if configured
            if self.target.config.get("add_record_metadata", True):
                record = self._add_wms_metadata(record)

            # Validate record if configured
            if self.target.config.get("validate_records", True):
                validation_result = self._validate_wms_record(record)
                if not validation_result.is_success:
                    self._processing_result.add_error(
                        f"Validation failed: {validation_result.error}",
                    )
                    return

            # Process the record using parent SQLSink logic
            super().process_record(record, context)
            self._processing_result.add_success()

            self.logger.debug(
                f"Successfully processed WMS record for stream: {self.stream_name}",
            )

        except Exception as e:
            error_msg = f"Error processing WMS record: {e}"
            self.logger.exception(error_msg)
            self._processing_result.add_error(error_msg)

    def _add_wms_metadata(self, record: dict[str, Any]) -> dict[str, Any]:
        """Add WMS-specific metadata to record."""
        enriched_record = record.copy()

        # Add processing timestamp
        enriched_record["_wms_processed_at"] = datetime.now(UTC).isoformat()

        # Add stream information
        enriched_record["_wms_stream_name"] = self.stream_name

        # Add target information
        enriched_record["_wms_target"] = "flext-target-oracle-wms"

        return enriched_record

    def _validate_wms_record(self, record: dict[str, Any]) -> FlextResult[bool]:
        """Validate WMS record against schema and business rules."""
        try:
            # Basic validation - ensure record is not empty
            if not record:
                return FlextResult.fail("Record is empty")

            # WMS-specific validations
            required_fields = self._get_required_wms_fields()
            for field in required_fields:
                if field not in record or record[field] is None:
                    return FlextResult.fail(
                        f"Required WMS field '{field}' is missing or null",
                    )

            # Validate data types for key WMS fields
            validation_result = self._validate_wms_data_types(record)
            if not validation_result.is_success:
                return validation_result

            return FlextResult.ok(True)

        except Exception as e:
            return FlextResult.fail(f"Validation error: {e}")

    def _get_required_wms_fields(self) -> list[str]:
        """Get list of required fields for WMS records."""
        # Define required fields based on stream type
        common_fields = []

        stream_specific_fields = {
            "inventory": ["item_id", "location_id", "quantity"],
            "orders": ["order_id", "order_type", "status"],
            "shipments": ["shipment_id", "carrier", "tracking_number"],
            "receipts": ["receipt_id", "supplier", "received_date"],
        }

        specific_fields = stream_specific_fields.get(self.stream_name, [])
        return common_fields + specific_fields

    def _validate_wms_data_types(self, record: dict[str, Any]) -> FlextResult[bool]:
        """Validate data types for WMS-specific fields."""
        try:
            # Validate numeric fields
            numeric_fields = ["quantity", "weight", "volume", "cost"]
            for field in numeric_fields:
                if field in record and record[field] is not None:
                    try:
                        float(record[field])
                    except (ValueError, TypeError):
                        return FlextResult.fail(f"Field '{field}' must be numeric")

            # Validate date fields
            date_fields = ["received_date", "shipped_date", "expected_date"]
            for field in date_fields:
                if field in record and record[field] is not None:
                    if not isinstance(record[field], (str, datetime)):
                        return FlextResult.fail(
                            f"Field '{field}' must be a date string or datetime",
                        )

            return FlextResult.ok(True)

        except Exception as e:
            return FlextResult.fail(f"Data type validation error: {e}")

    def get_processing_result(self) -> WMSProcessingResult:
        """Get processing results."""
        return self._processing_result

    def process_batch(self, context: dict[str, Any]) -> None:
        """Process a batch of records."""
        try:
            super().process_batch(context)

            # Log batch processing results
            result = self._processing_result
            self.logger.info(
                f"WMS batch processing completed for {self.stream_name}. "
                f"Success: {result.success_count}, Errors: {result.error_count}, "
                f"Success Rate: {result.success_rate:.2f}%",
            )

        except Exception as e:
            error_msg = f"Batch processing error for stream {self.stream_name}: {e}"
            self.logger.exception(error_msg)
            self._processing_result.add_error(error_msg)

    def teardown(self) -> None:
        """Teardown the sink."""
        super().teardown()

        # Log final results
        result = self._processing_result
        self.logger.info(
            f"Oracle WMS sink teardown for {self.stream_name}. "
            f"Total processed: {result.processed_count}, "
            f"Success: {result.success_count}, "
            f"Errors: {result.error_count}",
        )

    @property
    def schema_name(self) -> str | None:
        """Get schema name for this sink."""
        return self.target.config.get(
            "default_target_schema",
        ) or self.target.config.get("schema", "WMS")

    def conform_name(self, name: str, object_type: str | None = None) -> str:
        """Conform a stream property name to one suitable for the target system."""
        # Oracle naming conventions: uppercase, underscores, max 30 chars
        conformed_name = name.upper().replace(" ", "_").replace("-", "_")

        # Truncate to Oracle's 30 character limit for identifiers
        if len(conformed_name) > 30:
            conformed_name = conformed_name[:30]

        return conformed_name
