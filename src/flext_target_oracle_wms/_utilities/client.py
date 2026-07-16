"""Singer target client classes for Oracle WMS — u.TargetOracleWms.Client.*."""

from __future__ import annotations

import sys
from collections.abc import (
    MutableMapping,
)
from typing import ClassVar

from flext_core import e, r
from flext_meltano import u
from flext_target_oracle_wms import c, m, p, t
from flext_target_oracle_wms._utilities.helpers import (
    FlextTargetOracleWmsUtilitiesHelpers,
)


class FlextTargetOracleWmsUtilitiesClient:
    """Public namespace class wrapping all WMS client implementations."""

    class CatalogManager:
        """In-memory Singer catalog manager — u.TargetOracleWms.Client.CatalogManager."""

        def __init__(self) -> None:
            """Initialize catalog storage for stream metadata."""
            self._catalog_entries: MutableMapping[
                str,
                m.Meltano.SingerCatalogEntry,
            ] = {}

        def add_stream(
            self,
            schema_message: m.Meltano.SingerSchemaMessage,
        ) -> p.Result[bool]:
            """Register one stream schema entry."""
            typed_schema = m.Meltano.SingerSchemaMessage.model_validate(schema_message)
            stream_name = typed_schema.stream
            entry_result = u.Meltano.build_catalog_entry(
                stream_name=stream_name,
                schema=typed_schema.schema_definition,
                key_properties=typed_schema.key_properties,
            )
            if entry_result.failure:
                return r[bool].fail(
                    entry_result.error or f"Failed to register stream: {stream_name}",
                )
            self._catalog_entries[stream_name] = entry_result.value
            return r[bool].ok(value=True)

        def get_stream(
            self,
            stream_name: str,
        ) -> p.Result[p.Meltano.SingerCatalogEntry]:
            """Return catalog entry for a stream or a failure."""
            entry = self._catalog_entries.get(stream_name)
            if entry is None:
                return e.fail_not_found(
                    "WMS stream",
                    stream_name,
                    result_type=r[p.Meltano.SingerCatalogEntry],
                )
            return r[p.Meltano.SingerCatalogEntry].ok(entry)

    class StreamProcessor:
        """Process Singer records using table and transform helpers.

        Accessible as u.TargetOracleWms.Client.StreamProcessor.
        """

        def __init__(
            self,
            table_manager: FlextTargetOracleWmsUtilitiesHelpers.WMSTableManager,
            data_transformer: FlextTargetOracleWmsUtilitiesHelpers.WMSDataTransformer,
        ) -> None:
            """Initialize processing dependencies."""
            self.table_manager = table_manager
            self.data_transformer = data_transformer

        def initialize_stream(
            self,
            schema_message: m.Meltano.SingerSchemaMessage,
        ) -> p.Result[bool]:
            """Register stream metadata in table manager."""
            typed_schema = m.Meltano.SingerSchemaMessage.model_validate(schema_message)
            registration = self.table_manager.register_stream(typed_schema.stream)
            if registration.failure:
                return r[bool].fail(registration.error or "Table registration failed")
            return r[bool].ok(value=True)

        def process_record(
            self,
            record_message: m.Meltano.SingerRecordMessage,
            schema_message: m.Meltano.SingerSchemaMessage | t.JsonMapping,
        ) -> p.Result[p.Meltano.SingerRecordMessage]:
            """Transform one typed Singer record."""
            typed_record = m.Meltano.SingerRecordMessage.model_validate(record_message)
            table_lookup = self.table_manager.get_table_name(typed_record.stream)
            if table_lookup.failure:
                return r[p.Meltano.SingerRecordMessage].fail(
                    table_lookup.error or "Table lookup failed",
                )
            return self.data_transformer.transform_record(typed_record, schema_message)

    class Target:
        """Singer target runtime with schema/record/state handlers.

        Accessible as u.TargetOracleWms.Client.Target.
        """

        name = "target-oracle-wms"
        _state_type: ClassVar[str] = "STATE"
        _schema_type: ClassVar[str] = "SCHEMA"
        _record_type: ClassVar[str] = "RECORD"
        logger: ClassVar[p.Logger] = u.fetch_logger(__name__)

        def __init__(
            self,
            settings: t.JsonMapping | m.TargetOracleWms.WmsTargetConfig,
        ) -> None:
            """Initialize target runtime with validated settings."""
            # AGENT-COORDINATION (2026-07-11, bead mro-nwc.19): store the validated config as
            # settings. Previously the model_validate result was assigned to a local and
            # discarded, so the public `settings` accessor was missing (test_init_with_valid_config).
            settings = m.TargetOracleWms.WmsTargetConfig.model_validate(settings)
            self.catalog_manager = FlextTargetOracleWmsUtilitiesClient.CatalogManager()
            self.table_manager = FlextTargetOracleWmsUtilitiesHelpers.WMSTableManager()
            self.data_transformer = (
                FlextTargetOracleWmsUtilitiesHelpers.WMSDataTransformer()
            )
            self.stream_processor = FlextTargetOracleWmsUtilitiesClient.StreamProcessor(
                self.table_manager,
                self.data_transformer,
            )
            self._schemas: MutableMapping[str, m.Meltano.SingerSchemaMessage] = {}

        def cleanup(self) -> p.Result[bool]:
            """Release target runtime resources."""
            return r[bool].ok(value=True)

        def handle_record_message(
            self,
            message: m.Meltano.SingerRecordMessage,
        ) -> p.Result[bool]:
            """Handle one RECORD message."""
            typed_record = m.Meltano.SingerRecordMessage.model_validate(message)
            schema_message = self._schemas.get(typed_record.stream)
            if schema_message is None:
                return r[bool].fail(
                    f"Schema not registered for stream: {typed_record.stream}",
                )
            process_result = self.stream_processor.process_record(
                typed_record,
                schema_message,
            )
            if process_result.failure:
                return r[bool].fail(process_result.error or "Record processing failed")
            return r[bool].ok(value=True)

        def handle_schema_message(
            self,
            message: m.Meltano.SingerSchemaMessage,
        ) -> p.Result[bool]:
            """Handle one SCHEMA message."""
            typed_schema = m.Meltano.SingerSchemaMessage.model_validate(message)
            add_result = self.catalog_manager.add_stream(typed_schema)
            if add_result.failure:
                return add_result
            init_result = self.stream_processor.initialize_stream(typed_schema)
            if init_result.success:
                self._schemas[typed_schema.stream] = typed_schema
            return init_result

        def handle_state_message(
            self,
            message: m.Meltano.SingerStateMessage,
        ) -> p.Result[bool]:
            """Handle one STATE message."""
            typed_state = m.Meltano.SingerStateMessage.model_validate(message)
            self.logger.debug("Received state", state=str(typed_state.value))
            return r[bool].ok(value=True)

        def _dispatch_message(
            self,
            message_type: str,
            message: t.JsonMapping,
        ) -> p.Result[bool]:
            """Dispatch a single Singer message to the appropriate handler."""
            match message_type:
                case message_type if message_type == self._schema_type:
                    return self.handle_schema_message(
                        m.Meltano.SingerSchemaMessage.model_validate(message),
                    )
                case message_type if message_type == self._record_type:
                    return self.handle_record_message(
                        m.Meltano.SingerRecordMessage.model_validate(message),
                    )
                case message_type if message_type == self._state_type:
                    return self.handle_state_message(
                        m.Meltano.SingerStateMessage.model_validate(message),
                    )
                case _:
                    return r[bool].ok(value=True)

        def process_lines(self, input_lines: t.StrSequence) -> p.Result[bool]:
            """Parse and process Singer JSON lines."""
            for raw_line in input_lines:
                line = raw_line.strip()
                if not line:
                    continue
                try:
                    message = t.CONTAINER_MAP_ADAPTER.validate_json(line)
                except c.ValidationError as exc:
                    return r[bool].fail(f"Invalid JSON message: {exc}")
                message_type = str(message.get("type", ""))
                try:
                    dispatch_result = self._dispatch_message(message_type, message)
                except c.ValidationError as exc:
                    return r[bool].fail(f"Invalid Singer message: {exc}")
                if dispatch_result.failure:
                    return dispatch_result
            return r[bool].ok(value=True)

        def run(self) -> p.Result[bool]:
            """Run target processing loop using stdin."""
            return self.process_lines(list(sys.stdin))

        def setup(self) -> p.Result[bool]:
            """Prepare target runtime state."""
            return r[bool].ok(value=True)


__all__: list[str] = [
    "FlextTargetOracleWmsUtilitiesClient",
]
