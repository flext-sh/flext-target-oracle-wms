"""Target-side transformation helpers for Oracle WMS loading."""

from __future__ import annotations

import json

from flext_core import FlextResult, t

from .models import m


class WMSTypeConverter:
    """Convert source scalar values to Oracle-friendly payload values."""

    def convert_singer_to_oracle(
        self, singer_type: str, value: t.ContainerValue
    ) -> FlextResult[t.JsonValue]:
        """Convert a single source value according to Singer type."""
        if value is None:
            return FlextResult[t.JsonValue].ok("")
        if singer_type in {"object", "array"}:
            return FlextResult[t.JsonValue].ok(json.dumps(value))
        if singer_type in {"integer", "number"}:
            try:
                as_text = str(value)
                converted: t.JsonValue = (
                    float(as_text) if "." in as_text else int(as_text)
                )
                return FlextResult[t.JsonValue].ok(converted)
            except (TypeError, ValueError):
                return FlextResult[t.JsonValue].ok(str(value))
        return FlextResult[t.JsonValue].ok(str(value))


class WMSDataTransformer:
    """Transform incoming Singer record payloads for loading."""

    def __init__(self, type_converter: WMSTypeConverter | None = None) -> None:
        """Initialize data transformer with optional converter."""
        self.type_converter = type_converter or WMSTypeConverter()

    def transform_record(
        self,
        record_message: t.ContainerValue,
        schema_message: t.ContainerValue | None = None,
    ) -> FlextResult[m.Meltano.SingerRecordMessage]:
        """Transform one typed Singer RECORD payload with optional typed schema."""
        typed_record = m.Meltano.SingerRecordMessage.model_validate(record_message)
        transformed: dict[str, t.JsonValue] = {}
        schema_definition = (
            m.Meltano.SingerSchemaMessage.model_validate(
                schema_message
            ).schema_definition
            if schema_message is not None
            else {}
        )
        schema_props = m.TargetOracleWms.SingerSchemaProperties.model_validate(
            schema_definition
        )
        for key, value in typed_record.record.items():
            prop_schema = schema_props.properties.get(key)
            resolved_type = prop_schema.type if prop_schema is not None else "string"
            converted = self.type_converter.convert_singer_to_oracle(
                resolved_type, value
            )
            if converted.is_failure:
                return FlextResult[m.Meltano.SingerRecordMessage].fail(
                    converted.error or "Conversion failed"
                )
            transformed[str(key).upper()] = converted.value
        return FlextResult[m.Meltano.SingerRecordMessage].ok(
            m.Meltano.SingerRecordMessage(
                stream=typed_record.stream,
                record=transformed,
                time_extracted=typed_record.time_extracted,
                version=typed_record.version,
            )
        )


class WMSSchemaMapper:
    """Map Singer schema payloads to Oracle DDL-friendly structures."""

    def map_stream_schema(
        self, schema_message: t.ContainerValue
    ) -> FlextResult[m.Meltano.SingerCatalogEntry]:
        """Build normalized schema map for table creation."""
        typed_schema = m.Meltano.SingerSchemaMessage.model_validate(schema_message)
        return FlextResult[m.Meltano.SingerCatalogEntry].ok(
            m.Meltano.SingerCatalogEntry(
                tap_stream_id=typed_schema.stream,
                stream=typed_schema.stream,
                schema=typed_schema.schema_definition,
                key_properties=typed_schema.key_properties,
                table_name=typed_schema.stream.upper(),
            )
        )


class WMSTableManager:
    """Maintain in-memory stream-to-table mappings for the target run."""

    def __init__(self) -> None:
        """Initialize table manager map."""
        self._stream_tables: dict[str, str] = {}

    def get_table_name(self, stream_name: str) -> FlextResult[str]:
        """Get registered table name for stream."""
        table_name = self._stream_tables.get(stream_name)
        if table_name is None:
            return FlextResult[str].fail(f"Stream not registered: {stream_name}")
        return FlextResult[str].ok(table_name)

    def register_stream(self, stream_name: str) -> FlextResult[str]:
        """Register a stream and return table name."""
        table_name = stream_name.upper()
        self._stream_tables[stream_name] = table_name
        return FlextResult[str].ok(table_name)


__all__ = [
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
]
