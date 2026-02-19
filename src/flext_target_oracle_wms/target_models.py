"""Target-side transformation helpers for Oracle WMS loading."""

from __future__ import annotations

import json

from flext_core import FlextResult, FlextTypes as t


class WMSTypeConverter:
    """Convert source scalar values to Oracle-friendly payload values."""

    def convert_singer_to_oracle(
        self,
        singer_type: str,
        value: object,
    ) -> FlextResult[object]:
        """Convert a single source value according to Singer type."""
        if value is None:
            return FlextResult[object].ok(None)
        if singer_type in {"object", "array"}:
            return FlextResult[object].ok(json.dumps(value))
        if singer_type in {"integer", "number"}:
            try:
                as_text = str(value)
                converted: object = float(as_text) if "." in as_text else int(as_text)
                return FlextResult[object].ok(converted)
            except (TypeError, ValueError):
                return FlextResult[object].ok(str(value))
        return FlextResult[object].ok(str(value))


class WMSDataTransformer:
    """Transform incoming Singer record payloads for loading."""

    def __init__(self, type_converter: WMSTypeConverter | None = None) -> None:
        """Initialize data transformer with optional converter."""
        self.type_converter = type_converter or WMSTypeConverter()

    def transform_record(
        self,
        record: dict[str, t.GeneralValueType],
        schema: dict[str, t.GeneralValueType] | None = None,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Transform one record with optional schema-aware coercion."""
        transformed: dict[str, t.GeneralValueType] = {}
        properties = schema.get("properties", {}) if schema is not None else {}
        for key, value in record.items():
            singer_type = "string"
            if isinstance(properties, dict):
                prop = properties.get(key)
                if isinstance(prop, dict):
                    kind = prop.get("type")
                    if isinstance(kind, str):
                        singer_type = kind
            converted = self.type_converter.convert_singer_to_oracle(singer_type, value)
            if converted.is_failure:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    converted.error or "Conversion failed",
                )
            transformed[str(key).upper()] = value
        return FlextResult[dict[str, t.GeneralValueType]].ok(transformed)


class WMSSchemaMapper:
    """Map Singer schema payloads to Oracle DDL-friendly structures."""

    def map_stream_schema(
        self,
        stream_name: str,
        schema: dict[str, t.GeneralValueType],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Build normalized schema map for table creation."""
        return FlextResult[dict[str, t.GeneralValueType]].ok(
            {
                "stream_name": stream_name,
                "table_name": stream_name.upper(),
                "schema": schema,
            },
        )


class WMSTableManager:
    """Maintain in-memory stream-to-table mappings for the target run."""

    def __init__(self) -> None:
        """Initialize table manager map."""
        self._stream_tables: dict[str, str] = {}

    def register_stream(
        self,
        stream_name: str,
    ) -> FlextResult[str]:
        """Register a stream and return table name."""
        table_name = stream_name.upper()
        self._stream_tables[stream_name] = table_name
        return FlextResult[str].ok(table_name)

    def get_table_name(self, stream_name: str) -> FlextResult[str]:
        """Get registered table name for stream."""
        table_name = self._stream_tables.get(stream_name)
        if table_name is None:
            return FlextResult[str].fail(f"Stream not registered: {stream_name}")
        return FlextResult[str].ok(table_name)


__all__ = [
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
]
