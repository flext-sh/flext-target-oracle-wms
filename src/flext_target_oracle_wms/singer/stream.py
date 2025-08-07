"""Singer WMS stream processing using flext-core patterns."""

from __future__ import annotations

from typing import TYPE_CHECKING

# Import from flext-core for foundational patterns
from flext_core import (
    FlextResult,
    get_logger,
)

if TYPE_CHECKING:
    from flext_target_oracle_wms.patterns import WMSDataTransformer, WMSTableManager

logger = get_logger(__name__)


class WMSStreamProcessingStats:
    """WMS stream processing statistics - mutable for performance."""

    def __init__(
        self,
        stream_name: str,
        schema: dict[str, object] | None = None,
    ) -> None:
        """Initialize stream processing statistics."""
        self.stream_name = stream_name
        self.schema = schema or {}
        self.records_processed = 0
        self.records_success = 0
        self.records_failed = 0
        self.batches_processed = 0
        self.errors: list[str] = []
        self.schema_validation_enabled = bool(schema and schema.get("properties"))

    @property
    def success_rate(self) -> float:
        """Calculate success rate percentage."""
        if self.records_processed == 0:
            return 0.0
        return (self.records_success / self.records_processed) * 100.0


class SingerWMSStreamProcessor:
    """Process Singer WMS streams using flext-core patterns."""

    def __init__(
        self,
        table_manager: WMSTableManager,
        data_transformer: WMSDataTransformer,
    ) -> None:
        """Initialize Singer WMS stream processor."""
        self.table_manager = table_manager
        self.data_transformer = data_transformer
        self._stream_stats: dict[str, WMSStreamProcessingStats] = {}

    def initialize_stream(
        self,
        stream_name: str,
        schema: dict[str, object],
    ) -> FlextResult[None]:
        """Initialize WMS stream processing with schema validation."""
        try:
            # Validate schema structure (schema is already typed as dict[str, object])
            if "type" not in schema:
                return FlextResult.fail(
                    f"Schema missing 'type' field for stream {stream_name}",
                )

            # Store stream stats with schema for validation
            self._stream_stats[stream_name] = WMSStreamProcessingStats(
                stream_name,
                schema,
            )
            logger.info(
                "Initialized WMS stream processing: %s with schema validation",
                stream_name,
            )

            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("WMS stream initialization failed: %s", stream_name)
            return FlextResult.fail(f"Stream initialization failed: {e}")

    def process_record(
        self,
        stream_name: str,
        record: dict[str, object],
    ) -> FlextResult[dict[str, object]]:
        """Process single Singer WMS record."""
        try:
            if stream_name not in self._stream_stats:
                init_result = self.initialize_stream(stream_name, {})
                if not init_result.success:
                    return FlextResult.fail(
                        f"Stream initialization failed: {init_result.error}",
                    )

            stats = self._stream_stats[stream_name]

            # Transform record using WMS data transformer
            transform_result = self.data_transformer.transform_record(record)
            if not transform_result.success:
                stats.records_failed += 1
                stats.errors.append(
                    f"Record transformation failed: {transform_result.error}",
                )
                return FlextResult.fail(transform_result.error or "Transform failed")

            stats.records_processed += 1
            stats.records_success += 1

            return FlextResult.ok(transform_result.data or {})

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("WMS record processing failed for stream: %s", stream_name)
            if stream_name in self._stream_stats:
                self._stream_stats[stream_name].records_failed += 1
                self._stream_stats[stream_name].errors.append(str(e))
            return FlextResult.fail(f"Record processing failed: {e}")

    def process_batch(
        self,
        stream_name: str,
        records: list[dict[str, object]],
    ) -> FlextResult[list[dict[str, object]]]:
        """Process batch of Singer WMS records."""
        try:
            if stream_name not in self._stream_stats:
                init_result = self.initialize_stream(stream_name, {})
                if not init_result.success:
                    return FlextResult.fail(
                        f"Stream initialization failed: {init_result.error}",
                    )

            stats = self._stream_stats[stream_name]
            processed_records = []

            for record in records:
                process_result = self.process_record(stream_name, record)
                if process_result.success and process_result.data is not None:
                    processed_records.append(process_result.data)
                else:
                    logger.warning(
                        "WMS record processing failed: %s",
                        process_result.error,
                    )

            stats.batches_processed += 1

            logger.info(
                "Processed WMS batch for %s: %d/%d records",
                stream_name, len(processed_records), len(records),
            )

            return FlextResult.ok(processed_records)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("WMS batch processing failed for stream: %s", stream_name)
            return FlextResult.fail(f"Batch processing failed: {e}")

    def get_stream_stats(
        self,
        stream_name: str,
    ) -> FlextResult[WMSStreamProcessingStats]:
        """Get processing statistics for WMS stream."""
        if stream_name not in self._stream_stats:
            return FlextResult.fail(f"WMS stream not found: {stream_name}")

        return FlextResult.ok(self._stream_stats[stream_name])

    def get_all_stats(self) -> FlextResult[dict[str, WMSStreamProcessingStats]]:
        """Get all WMS stream processing statistics."""
        try:
            return FlextResult.ok(self._stream_stats.copy())

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Failed to get WMS stream statistics")
            return FlextResult.fail(f"Statistics retrieval failed: {e}")

    def reset_stream_stats(self, stream_name: str) -> FlextResult[None]:
        """Reset statistics for WMS stream."""
        try:
            if stream_name in self._stream_stats:
                self._stream_stats[stream_name] = WMSStreamProcessingStats(
                    stream_name=stream_name,
                )
                logger.info("Reset WMS stream statistics: %s", stream_name)

            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Failed to reset WMS stream statistics: %s", stream_name)
            return FlextResult.fail(f"Statistics reset failed: {e}")

    def finalize_stream(
        self,
        stream_name: str,
    ) -> FlextResult[WMSStreamProcessingStats]:
        """Finalize WMS stream processing and return final statistics."""
        try:
            if stream_name not in self._stream_stats:
                return FlextResult.fail(f"WMS stream not found: {stream_name}")

            stats = self._stream_stats[stream_name]

            logger.info(
                "Finalized WMS stream %s: %d/%d records successful",
                stream_name, stats.records_success, stats.records_processed,
            )

            return FlextResult.ok(stats)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("WMS stream finalization failed: %s", stream_name)
            return FlextResult.fail(f"Stream finalization failed: {e}")

    def validate_record_schema(
        self,
        record: dict[str, object],
        expected_schema: dict[str, object],
    ) -> FlextResult[bool]:
        """Validate WMS record against expected schema."""
        try:
            properties = expected_schema.get("properties", {})

            if not isinstance(properties, dict):
                return FlextResult.fail("Invalid schema: properties must be a dict")

            # Check required fields
            for prop_name, prop_def in properties.items():
                if prop_name not in record and prop_def.get("anyOf", [{}])[0].get("type") != "null":
                    # Field is missing and required (not nullable)
                    return FlextResult.fail(f"Missing required field: {prop_name}")

            # Basic type validation could be added here
            return FlextResult.ok(data=True)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("WMS schema validation failed")
            return FlextResult.fail(f"Schema validation failed: {e}")

    def handle_schema_change(
        self,
        stream_name: str,
        old_schema: dict[str, object],
        new_schema: dict[str, object],
    ) -> FlextResult[None]:
        """Handle schema changes for WMS stream."""
        try:
            # Log schema change
            logger.info("WMS schema change detected for stream: %s", stream_name)

            # Compare schemas and identify changes
            old_props = old_schema.get("properties", {})
            new_props = new_schema.get("properties", {})

            # Validate that properties are dicts
            if not isinstance(old_props, dict):
                old_props = {}
            if not isinstance(new_props, dict):
                new_props = {}

            added_fields = set(new_props.keys()) - set(old_props.keys())
            removed_fields = set(old_props.keys()) - set(new_props.keys())

            if added_fields:
                logger.info("WMS added fields in %s: %s", stream_name, added_fields)

            if removed_fields:
                logger.warning("WMS removed fields in %s: %s", stream_name, removed_fields)

            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("WMS schema change handling failed: %s", stream_name)
            return FlextResult.fail(f"Schema change handling failed: {e}")
