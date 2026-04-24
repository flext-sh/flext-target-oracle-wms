"""Tests for WMS target model helpers: WMSTypeConverter, WMSDataTransformer, WMSSchemaMapper, WMSTableManager.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import math

from tests import c, m, t, u


def _schema_msg(
    stream: str = "test_stream",
    key_properties: t.StrSequence | None = None,
) -> m.Meltano.SingerSchemaMessage:
    return m.Meltano.SingerSchemaMessage(
        type=c.Meltano.SingerMessageType.SCHEMA,
        stream=stream,
        schema={
            "type": "object",
        },
        key_properties=key_properties or ["id"],
    )


def _record_msg(
    stream: str = "test_stream",
    record: t.JsonMapping | None = None,
) -> m.Meltano.SingerRecordMessage:
    return m.Meltano.SingerRecordMessage(
        type=c.Meltano.SingerMessageType.RECORD,
        stream=stream,
        record=record or {"id": "1"},
    )


class TestWMSTypeConverter:
    """Tests for WMSTypeConverter.convert_singer_to_oracle."""

    def test_string_type(self) -> None:
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "string",
            "hello",
        )
        assert result.success
        assert result.value == "hello"

    def test_integer_type(self) -> None:
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "integer",
            42,
        )
        assert result.success
        assert result.value == 42

    def test_number_type_float(self) -> None:
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "number",
            math.pi,
        )
        assert result.success
        assert result.value == math.pi

    def test_none_value(self) -> None:
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "string",
            "",
        )
        assert result.success
        assert result.value == ""

    def test_object_type_serializes_to_json(self) -> None:
        data = '{"nested": "value"}'
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "object",
            data,
        )
        assert result.success
        assert result.value is not None
        assert m.TypeAdapter(t.StrictStr).validate_json(str(result.value)) == data

    def test_array_type_serializes_to_json(self) -> None:
        data = "[1, 2, 3]"
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "array",
            data,
        )
        assert result.success
        assert result.value is not None
        assert m.TypeAdapter(t.StrictStr).validate_json(str(result.value)) == data

    def test_boolean_type_becomes_string(self) -> None:
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "boolean",
            True,
        )
        assert result.success
        assert result.value == "True"


class TestWMSDataTransformer:
    """Tests for WMSDataTransformer.transform_record."""

    def test_uppercases_record_keys(self) -> None:
        transformer = u.TargetOracleWms.WMSDataTransformer()
        result = transformer.transform_record(
            _record_msg("s", {"name": "alice", "age": "30"}),
            _schema_msg("s"),
        )
        assert result.success
        assert result.value is not None
        assert "NAME" in result.value.record
        assert "AGE" in result.value.record

    def test_preserves_stream_name(self) -> None:
        transformer = u.TargetOracleWms.WMSDataTransformer()
        result = transformer.transform_record(
            _record_msg("orders", {"id": "1"}),
            _schema_msg("orders"),
        )
        assert result.success
        assert result.value is not None
        assert result.value.stream == "orders"

    def test_uses_custom_type_converter(self) -> None:
        converter = u.TargetOracleWms.WMSTypeConverter()
        transformer = u.TargetOracleWms.WMSDataTransformer(type_converter=converter)
        result = transformer.transform_record(
            _record_msg("s", {"qty": 10}),
            _schema_msg("s"),
        )
        assert result.success
        assert result.value is not None
        assert "QTY" in result.value.record

    def test_transform_without_schema(self) -> None:
        transformer = u.TargetOracleWms.WMSDataTransformer()
        result = transformer.transform_record(_record_msg("s", {"name": "bob"}), None)
        assert result.success
        assert result.value is not None
        assert "NAME" in result.value.record


class TestWMSSchemaMapper:
    """Tests for WMSSchemaMapper.map_stream_schema."""

    def test_returns_catalog_entry(self) -> None:
        mapper = u.TargetOracleWms.WMSSchemaMapper()
        result = mapper.map_stream_schema(_schema_msg("inventory"))
        assert result.success
        assert result.value is not None
        entry = result.value
        assert entry.stream == "inventory"
        assert entry.tap_stream_id == "inventory"
        assert entry.table_name == "INVENTORY"

    def test_preserves_key_properties(self) -> None:
        mapper = u.TargetOracleWms.WMSSchemaMapper()
        result = mapper.map_stream_schema(_schema_msg("s", key_properties=["a", "b"]))
        assert result.value is not None
        assert result.value.key_properties == ["a", "b"]


class TestWMSTableManager:
    """Tests for WMSTableManager."""

    def test_register_stream_returns_uppercase(self) -> None:
        tm = u.TargetOracleWms.WMSTableManager()
        result = tm.register_stream("orders")
        assert result.success
        assert result.value == "ORDERS"

    def test_get_registered_table(self) -> None:
        tm = u.TargetOracleWms.WMSTableManager()
        tm.register_stream("items")
        result = tm.get_table_name("items")
        assert result.success
        assert result.value == "ITEMS"

    def test_get_unregistered_fails(self) -> None:
        tm = u.TargetOracleWms.WMSTableManager()
        result = tm.get_table_name("nope")
        assert result.failure

    def test_multiple_streams(self) -> None:
        tm = u.TargetOracleWms.WMSTableManager()
        tm.register_stream("a")
        tm.register_stream("b")
        result_a = tm.get_table_name("a")
        assert result_a.success
        assert result_a.value is not None
        result_b = tm.get_table_name("b")
        assert result_b.success
        assert result_b.value is not None
        assert result_a.value == "A"
        assert result_b.value == "B"
