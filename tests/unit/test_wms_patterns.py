"""Tests for WMS target model helpers: WMSTypeConverter, WMSDataTransformer, WMSSchemaMapper, WMSTableManager.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import math

from flext_tests import tm

from tests import c, m, p, t, u


def _schema_msg(
    stream: str = "test_stream", key_properties: t.StrSequence | None = None
) -> p.Meltano.SingerSchemaMessage:
    return m.Meltano.SingerSchemaMessage(
        type=c.Meltano.SingerMessageType.SCHEMA,
        stream=stream,
        schema_definition={"type": "object"},
        key_properties=key_properties or ["id"],
    )


def _record_msg(
    stream: str = "test_stream", record: t.JsonMapping | None = None
) -> p.Meltano.SingerRecordMessage:
    return m.Meltano.SingerRecordMessage(
        type=c.Meltano.SingerMessageType.RECORD,
        stream=stream,
        record=record or {"id": "1"},
    )


class TestsFlextTargetOracleWmsWmsPatterns:
    """Tests for WMSTypeConverter.convert_singer_to_oracle."""

    def test_string_type(self) -> None:
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "string", "hello"
        )
        tm.ok(result)
        tm.that(result.value, eq="hello")

    def test_integer_type(self) -> None:
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "integer", 42
        )
        tm.ok(result)
        tm.that(result.value, eq=42)

    def test_number_type_float(self) -> None:
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "number", math.pi
        )
        tm.ok(result)
        tm.that(result.value, eq=math.pi)

    def test_none_value(self) -> None:
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "string", ""
        )
        tm.ok(result)
        tm.that(result.value, eq="")

    def test_object_type_serializes_to_json(self) -> None:
        data = '{"nested": "value"}'
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "object", data
        )
        tm.ok(result)
        tm.that(result.value, none=False)
        tm.that(m.TypeAdapter(t.StrictStr).validate_json(str(result.value)), eq=data)

    def test_array_type_serializes_to_json(self) -> None:
        data = "[1, 2, 3]"
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "array", data
        )
        tm.ok(result)
        tm.that(result.value, none=False)
        tm.that(m.TypeAdapter(t.StrictStr).validate_json(str(result.value)), eq=data)

    def test_boolean_type_becomes_string(self) -> None:
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "boolean", True
        )
        tm.ok(result)
        tm.that(result.value, eq="True")

    def test_uppercases_record_keys(self) -> None:
        transformer = u.TargetOracleWms.WMSDataTransformer()
        result = transformer.transform_record(
            _record_msg("s", {"name": "alice", "age": "30"}), _schema_msg("s")
        )
        tm.ok(result)
        tm.that(result.value, none=False)
        tm.that(result.value.record, has="NAME")
        tm.that(result.value.record, has="AGE")

    def test_preserves_stream_name(self) -> None:
        transformer = u.TargetOracleWms.WMSDataTransformer()
        result = transformer.transform_record(
            _record_msg("orders", {"id": "1"}), _schema_msg("orders")
        )
        tm.ok(result)
        tm.that(result.value, none=False)
        tm.that(result.value.stream, eq="orders")

    def test_uses_custom_type_converter(self) -> None:
        converter = u.TargetOracleWms.WMSTypeConverter()
        transformer = u.TargetOracleWms.WMSDataTransformer(type_converter=converter)
        result = transformer.transform_record(
            _record_msg("s", {"qty": 10}), _schema_msg("s")
        )
        tm.ok(result)
        tm.that(result.value, none=False)
        tm.that(result.value.record, has="QTY")

    def test_transform_without_schema(self) -> None:
        transformer = u.TargetOracleWms.WMSDataTransformer()
        result = transformer.transform_record(_record_msg("s", {"name": "bob"}), None)
        tm.ok(result)
        tm.that(result.value, none=False)
        tm.that(result.value.record, has="NAME")

    def test_returns_catalog_entry(self) -> None:
        mapper = u.TargetOracleWms.WMSSchemaMapper()
        result = mapper.map_stream_schema(_schema_msg("inventory"))
        tm.ok(result)
        tm.that(result.value, none=False)
        entry = result.value
        tm.that(entry.stream, eq="inventory")
        tm.that(entry.tap_stream_id, eq="inventory")
        tm.that(entry.table_name, eq="INVENTORY")

    def test_preserves_key_properties(self) -> None:
        mapper = u.TargetOracleWms.WMSSchemaMapper()
        result = mapper.map_stream_schema(_schema_msg("s", key_properties=["a", "b"]))
        tm.that(result.value, none=False)
        tm.that(result.value.key_properties, eq=["a", "b"])

    def test_register_stream_returns_uppercase(self) -> None:
        manager = u.TargetOracleWms.WMSTableManager()
        result = manager.register_stream("orders")
        tm.ok(result)
        tm.that(result.value, eq="ORDERS")

    def test_get_registered_table(self) -> None:
        manager = u.TargetOracleWms.WMSTableManager()
        manager.register_stream("items")
        result = manager.get_table_name("items")
        tm.ok(result)
        tm.that(result.value, eq="ITEMS")

    def test_get_unregistered_fails(self) -> None:
        manager = u.TargetOracleWms.WMSTableManager()
        result = manager.get_table_name("nope")
        tm.fail(result)

    def test_multiple_streams(self) -> None:
        manager = u.TargetOracleWms.WMSTableManager()
        manager.register_stream("a")
        manager.register_stream("b")
        result_a = manager.get_table_name("a")
        tm.ok(result_a)
        tm.that(result_a.value, none=False)
        result_b = manager.get_table_name("b")
        tm.ok(result_b)
        tm.that(result_b.value, none=False)
        tm.that(result_a.value, eq="A")
        tm.that(result_b.value, eq="B")
