"""Singer target client primitives for Oracle WMS."""

from __future__ import annotations

import sys
from typing import ClassVar

from flext_core import FlextLogger, r, t
from pydantic import TypeAdapter, ValidationError

from .models import m
from .target_models import WMSDataTransformer, WMSTableManager

logger = FlextLogger(__name__)


class SingerWMSCatalogManager:
    """In-memory Singer catalog manager."""

    def __init__(self) -> None:
        """Initialize catalog storage for stream metadata."""
        self._catalog_entries: dict[str, m.Meltano.SingerCatalogEntry] = {}

    def add_stream(self, schema_message) -> r[bool]:
        """Register one stream schema entry."""
        typed_schema = m.Meltano.SingerSchemaMessage.model_validate(schema_message)
        stream_name = typed_schema.stream
        self._catalog_entries[stream_name] = (
            m.Meltano.SingerCatalogEntry.model_validate({
                "tap_stream_id": stream_name,
                "stream": stream_name,
                "schema": typed_schema.schema_definition,
                "key_properties": typed_schema.key_properties,
            })
        )
        return r[bool].ok(value=True)

    def get_stream(self, stream_name: str) -> r[m.Meltano.SingerCatalogEntry]:
        """Return catalog entry for a stream or a failure."""
        entry = self._catalog_entries.get(stream_name)
        if entry is None:
            return r[m.Meltano.SingerCatalogEntry].fail(
                f"WMS stream not found: {stream_name}"
            )
        return r[m.Meltano.SingerCatalogEntry].ok(entry)


class SingerWMSStreamProcessor:
    """Process Singer records using table and transform helpers."""

    def __init__(
        self, table_manager: WMSTableManager, data_transformer: WMSDataTransformer
    ) -> None:
        """Initialize processing dependencies."""
        self.table_manager = table_manager
        self.data_transformer = data_transformer

    def initialize_stream(self, schema_message) -> r[bool]:
        """Register stream metadata in table manager."""
        typed_schema = m.Meltano.SingerSchemaMessage.model_validate(schema_message)
        registration = self.table_manager.register_stream(typed_schema.stream)
        if registration.is_failure:
            return r[bool].fail(registration.error or "Table registration failed")
        return r[bool].ok(value=True)

    def process_record(
        self, record_message, schema_message
    ) -> r[m.Meltano.SingerRecordMessage]:
        """Transform one typed Singer record."""
        typed_record = m.Meltano.SingerRecordMessage.model_validate(record_message)
        table_lookup = self.table_manager.get_table_name(typed_record.stream)
        if table_lookup.is_failure:
            return r[m.Meltano.SingerRecordMessage].fail(
                table_lookup.error or "Table lookup failed"
            )
        return self.data_transformer.transform_record(typed_record, schema_message)


class SingerTargetOracleWMS:
    """Singer target runtime with schema/record/state handlers."""

    name = "target-oracle-wms"
    _state_type: ClassVar[str] = "STATE"
    _schema_type: ClassVar[str] = "SCHEMA"
    _record_type: ClassVar[str] = "RECORD"

    def __init__(self, config) -> None:
        """Initialize target runtime with validated config."""
        self.config = m.TargetOracleWms.WmsTargetConfig.model_validate(config)
        self.catalog_manager = SingerWMSCatalogManager()
        self.table_manager = WMSTableManager()
        self.data_transformer = WMSDataTransformer()
        self.stream_processor = SingerWMSStreamProcessor(
            self.table_manager, self.data_transformer
        )
        self._schemas: dict[str, object] = {}

    def cleanup(self) -> r[bool]:
        """Release target runtime resources."""
        return r[bool].ok(value=True)

    def handle_record_message(self, message) -> r[bool]:
        """Handle one RECORD message."""
        typed_record = m.Meltano.SingerRecordMessage.model_validate(message)
        schema_message = self._schemas.get(typed_record.stream)
        if schema_message is None:
            return r[bool].fail(
                f"Schema not registered for stream: {typed_record.stream}"
            )
        process_result = self.stream_processor.process_record(
            typed_record, schema_message
        )
        if process_result.is_failure:
            return r[bool].fail(process_result.error or "Record processing failed")
        return r[bool].ok(value=True)

    def handle_schema_message(self, message) -> r[bool]:
        """Handle one SCHEMA message."""
        typed_schema = m.Meltano.SingerSchemaMessage.model_validate(message)
        result = self.catalog_manager.add_stream(typed_schema).flow_through(
            lambda _: self.stream_processor.initialize_stream(typed_schema),
        )
        if result.is_success:
            self._schemas[typed_schema.stream] = typed_schema
        return result

    def handle_state_message(self, message) -> r[bool]:
        """Handle one STATE message."""
        typed_state = m.Meltano.SingerStateMessage.model_validate(message)
        logger.debug("Received state", state=str(typed_state.value))
        return r[bool].ok(value=True)

    def process_lines(self, input_lines: list[str]) -> r[bool]:
        """Parse and process Singer JSON lines."""
        for raw_line in input_lines:
            line = raw_line.strip()
            if not line:
                continue
            message_adapter: TypeAdapter[dict[str, t.ContainerValue]] = TypeAdapter(
                dict[str, t.ContainerValue]
            )
            try:
                message = message_adapter.validate_json(line)
            except ValidationError as exc:
                return r[bool].fail(f"Invalid JSON message: {exc}")
            message_type = str(message.get("type", ""))
            try:
                if message_type == self._schema_type:
                    parsed_schema = m.Meltano.SingerSchemaMessage.model_validate(
                        message
                    )
                    schema_result = self.handle_schema_message(parsed_schema)
                    if schema_result.is_failure:
                        return schema_result
                elif message_type == self._record_type:
                    parsed_record = m.Meltano.SingerRecordMessage.model_validate(
                        message
                    )
                    record_result = self.handle_record_message(parsed_record)
                    if record_result.is_failure:
                        return record_result
                elif message_type == self._state_type:
                    parsed_state = m.Meltano.SingerStateMessage.model_validate(message)
                    state_result = self.handle_state_message(parsed_state)
                    if state_result.is_failure:
                        return state_result
            except ValidationError as exc:
                return r[bool].fail(f"Invalid Singer message: {exc}")
        return r[bool].ok(value=True)

    def run(self) -> r[bool]:
        """Run target processing loop using stdin."""
        return self.process_lines(list(sys.stdin))

    def setup(self) -> r[bool]:
        """Prepare target runtime state."""
        return r[bool].ok(value=True)


__all__ = [
    "SingerTargetOracleWMS",
    "SingerWMSCatalogManager",
    "SingerWMSStreamProcessor",
]
