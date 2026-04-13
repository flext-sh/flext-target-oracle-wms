"""WMS helper classes — u.TargetOracleWms.{WMSTableManager,WMSDataTransformer,...}."""

from __future__ import annotations

from collections.abc import Mapping

from flext_target_oracle_wms import c, m, p, r, t


class _WmsHelpers:
    """Private namespace class wrapping all WMS helper implementations."""

    class Validation:
        """Validation helpers for runtime target configuration."""

        @staticmethod
        def validate_wms_target_config(
            settings: t.ContainerValueMapping,
        ) -> p.Result[bool]:
            """Validate minimal required target configuration fields."""
            required = {"base_url", "username", "password"}
            missing = sorted(key for key in required if key not in settings)
            if missing:
                return r[bool].fail(
                    f"Missing required configuration fields: {missing}",
                )
            load_method = settings.get(
                "load_method",
                c.TargetOracleWms.LoadMethods.APPEND_ONLY,
            )
            if load_method not in c.TargetOracleWms.LoadMethods.VALID_LOAD_METHODS:
                return r[bool].fail("Invalid load_method")
            return r[bool].ok(value=True)

    class WMSTypeConverter:
        """Convert source scalar values to Oracle-friendly payload values."""

        def convert_singer_to_oracle(
            self,
            singer_type: str,
            value: t.Container | t.ContainerValue,
        ) -> p.Result[t.Container]:
            """Convert a single source value according to Singer type."""
            if singer_type in {"object", "array"}:
                return r[t.Container].ok(
                    t.NV_ADAPTER.dump_json(value).decode("utf-8"),
                )
            if singer_type in {"integer", "number"}:
                try:
                    as_text = str(value)
                    converted: t.Container = (
                        float(as_text) if "." in as_text else int(as_text)
                    )
                    return r[t.Container].ok(converted)
                except c.Meltano.SINGER_SAFE_EXCEPTIONS:
                    return r[t.Container].ok(str(value))
            return r[t.Container].ok(str(value))

    class WMSDataTransformer:
        """Transform incoming Singer record payloads for loading."""

        def __init__(
            self,
            type_converter: _WmsHelpers.WMSTypeConverter | None = None,
        ) -> None:
            """Initialize data transformer with optional converter."""
            self.type_converter = type_converter or _WmsHelpers.WMSTypeConverter()

        def transform_record(
            self,
            record_message: m.Meltano.SingerRecordMessage | t.ContainerValueMapping,
            schema_message: m.Meltano.SingerSchemaMessage
            | t.ContainerValueMapping
            | None = None,
        ) -> p.Result[m.Meltano.SingerRecordMessage]:
            """Transform one typed Singer RECORD payload with optional typed schema."""
            typed_record = m.Meltano.SingerRecordMessage.model_validate(
                record_message,
            )
            transformed: t.MutableFlatContainerMapping = {}
            empty_schema: t.MutableFlatContainerMapping = {}
            schema_definition = (
                m.Meltano.SingerSchemaMessage.model_validate(
                    schema_message,
                ).schema_definition
                if schema_message is not None
                else empty_schema
            )
            schema_props = m.TargetOracleWms.SingerSchemaProperties.model_validate(
                schema_definition,
            )
            for key, value in typed_record.record.items():
                prop_schema = schema_props.properties.get(key)
                resolved_type = (
                    prop_schema.type if prop_schema is not None else "string"
                )
                converted = self.type_converter.convert_singer_to_oracle(
                    resolved_type,
                    value,
                )
                if converted.failure:
                    return r[m.Meltano.SingerRecordMessage].fail(
                        converted.error or "Conversion failed",
                    )
                transformed[str(key).upper()] = converted.value
            return r[m.Meltano.SingerRecordMessage].ok(
                m.Meltano.SingerRecordMessage.model_validate({
                    "type": typed_record.type,
                    "stream": typed_record.stream,
                    "record": transformed,
                    "time_extracted": typed_record.time_extracted,
                    "version": typed_record.version,
                }),
            )

    class WMSSchemaMapper:
        """Map Singer schema payloads to Oracle DDL-friendly structures."""

        def map_stream_schema(
            self,
            schema_message: m.Meltano.SingerSchemaMessage | t.ContainerValueMapping,
        ) -> p.Result[m.Meltano.SingerCatalogEntry]:
            """Build normalized schema map for table creation."""
            typed_schema = m.Meltano.SingerSchemaMessage.model_validate(
                schema_message,
            )
            return r[m.Meltano.SingerCatalogEntry].ok(
                m.Meltano.SingerCatalogEntry.model_validate({
                    "tap_stream_id": typed_schema.stream,
                    "stream": typed_schema.stream,
                    "schema": typed_schema.schema_definition,
                    "key_properties": typed_schema.key_properties,
                    "table_name": typed_schema.stream.upper(),
                }),
            )

    class WMSTableManager:
        """Maintain in-memory stream-to-table mappings for the target run."""

        def __init__(self) -> None:
            """Initialize table manager map."""
            self._stream_tables: t.MutableStrMapping = {}

        def get_table_name(self, stream_name: str) -> p.Result[str]:
            """Get registered table name for stream."""
            table_name = self._stream_tables.get(stream_name)
            if table_name is None:
                return r[str].fail(f"Stream not registered: {stream_name}")
            return r[str].ok(table_name)

        def register_stream(self, stream_name: str) -> p.Result[str]:
            """Register a stream and return table name."""
            table_name = stream_name.upper()
            self._stream_tables[stream_name] = table_name
            return r[str].ok(table_name)

    @staticmethod
    def create_record_message(
        stream_name: str,
        record: t.ContainerValueMapping,
    ) -> Mapping[str, t.ContainerValue | t.ContainerValueMapping]:
        """Create a Singer RECORD message payload."""
        return {"type": "RECORD", "stream": stream_name, "record": record}

    @staticmethod
    def create_schema_message(
        stream_name: str,
        schema: t.ContainerValueMapping,
        key_properties: t.StrSequence | None = None,
    ) -> Mapping[str, t.ContainerValue | t.ContainerValueMapping | t.StrSequence]:
        """Create a Singer SCHEMA message payload."""
        return {
            "type": "SCHEMA",
            "stream": stream_name,
            "schema": schema,
            "key_properties": key_properties or [],
        }

    @staticmethod
    def create_state_message(
        state: t.ContainerValueMapping,
    ) -> Mapping[str, t.ContainerValue | t.ContainerValueMapping]:
        """Create a Singer STATE message payload."""
        return {"type": "STATE", "value": state}


# Public names — re-exported from namespace for backward compatibility with auto-generated __init__.py
Validation = _WmsHelpers.Validation
WMSTypeConverter = _WmsHelpers.WMSTypeConverter
WMSDataTransformer = _WmsHelpers.WMSDataTransformer
WMSSchemaMapper = _WmsHelpers.WMSSchemaMapper
WMSTableManager = _WmsHelpers.WMSTableManager
create_record_message = _WmsHelpers.create_record_message
create_schema_message = _WmsHelpers.create_schema_message
create_state_message = _WmsHelpers.create_state_message

__all__: list[str] = [
    "Validation",
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
    "create_record_message",
    "create_schema_message",
    "create_state_message",
]
