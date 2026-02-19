"""Singer target client primitives for Oracle WMS."""

from __future__ import annotations

import json
import sys

from flext_core import FlextLogger, FlextResult, FlextSettings, FlextTypes as t
from pydantic import Field

from .target_models import WMSDataTransformer, WMSTableManager

logger = FlextLogger(__name__)


class SingerWMSCatalogEntry(FlextSettings):
    """Singer catalog entry model used during stream registration."""

    tap_stream_id: str
    stream: str
    schema_info: dict[str, t.GeneralValueType]
    metadata: list[dict[str, t.GeneralValueType]] = Field(default_factory=list)
    key_properties: list[str] = Field(default_factory=list)
    bookmark_properties: list[str] = Field(default_factory=list)
    replication_method: str = "FULL_TABLE"
    replication_key: str | None = None


class SingerWMSCatalogManager:
    """In-memory Singer catalog manager."""

    def __init__(self) -> None:
        """Initialize internal catalog state."""
        self._catalog_entries: dict[str, SingerWMSCatalogEntry] = {}

    def add_stream(
        self,
        stream_name: str,
        schema: dict[str, t.GeneralValueType],
        metadata: list[dict[str, t.GeneralValueType]] | None = None,
    ) -> FlextResult[bool]:
        """Register a stream with its schema and metadata."""
        self._catalog_entries[stream_name] = SingerWMSCatalogEntry(
            tap_stream_id=stream_name,
            stream=stream_name,
            schema_info=schema,
            metadata=metadata or [],
        )
        return FlextResult[bool].ok(value=True)

    def get_stream(self, stream_name: str) -> FlextResult[SingerWMSCatalogEntry]:
        """Get stream definition from the catalog."""
        entry = self._catalog_entries.get(stream_name)
        if entry is None:
            return FlextResult[SingerWMSCatalogEntry].fail(
                f"WMS stream not found: {stream_name}",
            )
        return FlextResult[SingerWMSCatalogEntry].ok(entry)


class SingerWMSStreamProcessor:
    """Process Singer records using table and transform helpers."""

    def __init__(
        self,
        table_manager: WMSTableManager,
        data_transformer: WMSDataTransformer,
    ) -> None:
        """Initialize stream processor dependencies."""
        self.table_manager = table_manager
        self.data_transformer = data_transformer

    def initialize_stream(
        self,
        stream_name: str,
        schema: dict[str, t.GeneralValueType],
    ) -> FlextResult[bool]:
        """Initialize stream resources and table mapping."""
        _ = schema
        registration = self.table_manager.register_stream(stream_name)
        if registration.is_failure:
            return FlextResult[bool].fail(
                registration.error or "Table registration failed"
            )
        return FlextResult[bool].ok(value=True)

    def process_record(
        self,
        stream_name: str,
        record: dict[str, t.GeneralValueType],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Transform one record and return transformed payload."""
        _ = self.table_manager.get_table_name(stream_name)
        return self.data_transformer.transform_record(record)


class SingerTargetOracleWMS:
    """Singer target runtime with schema/record/state handlers."""

    name = "target-oracle-wms"

    def __init__(self, config: dict[str, t.GeneralValueType]) -> None:
        """Initialize target runtime dependencies."""
        self.config = config
        self.catalog_manager = SingerWMSCatalogManager()
        self.table_manager = WMSTableManager()
        self.data_transformer = WMSDataTransformer()
        self.stream_processor = SingerWMSStreamProcessor(
            self.table_manager,
            self.data_transformer,
        )

    def setup(self) -> FlextResult[bool]:
        """Prepare target runtime state."""
        return FlextResult[bool].ok(value=True)

    def cleanup(self) -> FlextResult[bool]:
        """Release target runtime resources."""
        return FlextResult[bool].ok(value=True)

    def process_lines(self, input_lines: list[str]) -> FlextResult[bool]:
        """Process Singer lines from stdin or tests."""
        for raw_line in input_lines:
            line = raw_line.strip()
            if not line:
                continue
            try:
                message = json.loads(line)
            except json.JSONDecodeError as exc:
                return FlextResult[bool].fail(f"Invalid JSON message: {exc}")
            message_type = message.get("type")
            if message_type == "SCHEMA":
                self.handle_schema_message(message)
            elif message_type == "RECORD":
                self.handle_record_message(message)
            elif message_type == "STATE":
                self.handle_state_message(message)
        return FlextResult[bool].ok(value=True)

    def run(self) -> FlextResult[bool]:
        """Run target processing from stdin."""
        return self.process_lines(list(sys.stdin))

    def handle_schema_message(self, message: dict[str, t.GeneralValueType]) -> None:
        """Handle Singer SCHEMA message."""
        stream = message.get("stream")
        schema = message.get("schema")
        if not isinstance(stream, str) or not isinstance(schema, dict):
            return
        _ = self.catalog_manager.add_stream(stream, schema)
        _ = self.stream_processor.initialize_stream(stream, schema)

    def handle_record_message(self, message: dict[str, t.GeneralValueType]) -> None:
        """Handle Singer RECORD message."""
        stream = message.get("stream")
        record = message.get("record")
        if not isinstance(stream, str) or not isinstance(record, dict):
            return
        _ = self.stream_processor.process_record(stream, record)

    def handle_state_message(self, message: dict[str, t.GeneralValueType]) -> None:
        """Handle Singer STATE message."""
        state = message.get("value")
        logger.debug("Received state", extra={"state": state})


__all__ = [
    "SingerTargetOracleWMS",
    "SingerWMSCatalogEntry",
    "SingerWMSCatalogManager",
    "SingerWMSStreamProcessor",
]
