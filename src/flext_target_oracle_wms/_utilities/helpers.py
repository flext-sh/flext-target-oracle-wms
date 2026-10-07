"""WMS helper classes — u.TargetOracleWms.{WMSTableManager,WMSDataTransformer,...}.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_target_oracle_wms/_utilities/helpers
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_cli import u
from flext_meltano import c as meltano_c

from flext_core import r
from flext_target_oracle_wms import (
    FlextTargetOracleWmsConstants as c,
    FlextTargetOracleWmsModels as m,
    FlextTargetOracleWmsTypes as t,
)

if TYPE_CHECKING:
    from flext_target_oracle_wms import p


class FlextTargetOracleWmsUtilitiesHelpers:
    """Private namespace class wrapping all WMS helper implementations."""

    class WMSTypeConverter:
        """Convert source scalar values to Oracle-friendly payload values."""

        @staticmethod
        def convert_singer_to_oracle(
            singer_type: str,
            value: t.JsonValue,
        ) -> p.Result[t.JsonValue]:
            """Convert a single source value according to Singer type.

            Returns:
                The resulting ``p.Result[t.JsonValue]``.
            """
            if singer_type in {"object", "array"}:
                return r[t.JsonValue].ok(
                    t
                    .json_value_adapter()
                    .dump_json(u.normalize_to_json_value(value))
                    .decode(c.DEFAULT_ENCODING),
                )
            if singer_type in {"integer", "number"}:
                try:
                    as_text = str(value)
                    converted: t.JsonValue = (
                        float(as_text) if "." in as_text else int(as_text)
                    )
                    return r[t.JsonValue].ok(converted)
                except meltano_c.Meltano.SINGER_SAFE_EXCEPTIONS:
                    return r[t.JsonValue].ok(str(value))
            return r[t.JsonValue].ok(str(value))

    class WMSDataTransformer:
        """Transform incoming Singer record payloads for loading."""

        def __init__(
            self,
            type_converter: FlextTargetOracleWmsUtilitiesHelpers.WMSTypeConverter
            | None = None,
        ) -> None:
            """Initialize data transformer with optional converter."""
            self.type_converter = (
                type_converter
                or FlextTargetOracleWmsUtilitiesHelpers.WMSTypeConverter()
            )

        def transform_record(
            self,
            record_message: m.Meltano.SingerRecordMessage | t.JsonMapping,
            schema_message: m.Meltano.SingerSchemaMessage | t.JsonMapping | None = None,
        ) -> p.Result[m.Meltano.SingerRecordMessage]:
            """Transform one typed Singer RECORD payload with optional typed schema.

            Returns:
                The resulting ``p.Result[m.Meltano.SingerRecordMessage]``.
            """
            typed_record = m.Meltano.SingerRecordMessage.model_validate(record_message)
            transformed: t.MutableJsonMapping = {}
            empty_schema: t.MutableJsonMapping = {}
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
                    return r[m.Meltano.SingerRecordMessage].from_failure(converted)
                transformed[key.upper()] = converted.value
            return r[m.Meltano.SingerRecordMessage].ok(
                m.Meltano.SingerRecordMessage.model_validate({
                    "type": typed_record.type,
                    "stream": typed_record.stream,
                    "record": transformed,
                    "time_extracted": typed_record.time_extracted,
                    "version": typed_record.version,
                }),
            )

    class WMSTableManager:
        """Maintain in-memory stream-to-table mappings for the target run."""

        def __init__(self) -> None:
            """Initialize table manager map."""
            self._stream_tables: t.MutableStrMapping = {}

        def get_table_name(self, stream_name: str) -> p.Result[str]:
            """Get registered table name for stream.

            Returns:
                The resulting ``p.Result[str]``.
            """
            table_name = self._stream_tables.get(stream_name)
            if table_name is None:
                return r[str].fail(f"Stream not registered: {stream_name}")
            return r[str].ok(table_name)

        def register_stream(self, stream_name: str) -> p.Result[str]:
            """Register a stream and return table name.

            Returns:
                The resulting ``p.Result[str]``.
            """
            table_name = stream_name.upper()
            self._stream_tables[stream_name] = table_name
            return r[str].ok(table_name)


__all__: list[str] = ["FlextTargetOracleWmsUtilitiesHelpers"]
