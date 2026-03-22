"""Tests for WMS target model helpers: WMSTypeConverter, WMSDataTransformer, WMSSchemaMapper, WMSTableManager.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import math

from pydantic import TypeAdapter

from flext_target_oracle_wms import (
    WMSDataTransformer,
    WMSSchemaMapper,
    WMSTableManager,
    WMSTypeConverter,
    m,
)


def _schema_msg(
    stream: str = "test_stream",
    properties: dict[str, dict[str, str]] | None = None,
    key_properties: list[str] | None = None,
) -> m.Meltano.SingerSchemaMessage:
    return m.Meltano.SingerSchemaMessage.model_validate({
        "type": "SCHEMA",
        "stream": stream,
        "schema": {
            "type": "object",
            "properties": properties or {"id": {"type": "string"}},
        },
        "key_properties": key_properties or ["id"],
    })


def _record_msg(
    stream: str = "test_stream", record: dict[str, object] | None = None
) -> m.Meltano.SingerRecordMessage:
    return m.Meltano.SingerRecordMessage.model_validate({
        "type": "RECORD",
        "stream": stream,
        "record": record or {"id": "1"},
    })


class TestWMSTypeConverter:
    """Tests for WMSTypeConverter.convert_singer_to_oracle."""

    def test_string_type(self) -> None:
        result = WMSTypeConverter().convert_singer_to_oracle("string", "hello")
        assert result.is_success
        assert result.value == "hello"

    def test_integer_type(self) -> None:
        result = WMSTypeConverter().convert_singer_to_oracle("integer", 42)
        assert result.is_success
        assert result.value == 42

    def test_number_type_float(self) -> None:
        result = WMSTypeConverter().convert_singer_to_oracle("number", math.pi)
        assert result.is_success
        assert result.value == math.pi

    def test_none_value(self) -> None:
        result = WMSTypeConverter().convert_singer_to_oracle("string", "")
        assert result.is_success
        assert result.value == ""

    def test_object_type_serializes_to_json(self) -> None:
        data = '{"nested": "value"}'
        result = WMSTypeConverter().convert_singer_to_oracle("object", data)
        assert result.is_success
        assert result.value is not None
        assert TypeAdapter(str).validate_json(str(result.value)) == data

    def test_array_type_serializes_to_json(self) -> None:
        data = "[1, 2, 3]"
        result = WMSTypeConverter().convert_singer_to_oracle("array", data)
        assert result.is_success
        assert result.value is not None
        assert TypeAdapter(str).validate_json(str(result.value)) == data

    def test_boolean_type_becomes_string(self) -> None:
        result = WMSTypeConverter().convert_singer_to_oracle("boolean", True)
        assert result.is_success
        assert result.value == "True"


class TestWMSDataTransformer:
    """Tests for WMSDataTransformer.transform_record."""

    def test_uppercases_record_keys(self) -> None:
        transformer = WMSDataTransformer()
        result = transformer.transform_record(
            _record_msg("s", {"name": "alice", "age": "30"}),
            _schema_msg(
                "s", properties={"name": {"type": "string"}, "age": {"type": "string"}}
            ),
        )
        assert result.is_success
        assert result.value is not None
        assert "NAME" in result.value.record
        assert "AGE" in result.value.record

    def test_preserves_stream_name(self) -> None:
        transformer = WMSDataTransformer()
        result = transformer.transform_record(
            _record_msg("orders", {"id": "1"}), _schema_msg("orders")
        )
        assert result.is_success
        assert result.value is not None
        assert result.value.stream == "orders"

    def test_uses_custom_type_converter(self) -> None:
        converter = WMSTypeConverter()
        transformer = WMSDataTransformer(type_converter=converter)
        result = transformer.transform_record(
            _record_msg("s", {"qty": 10}),
            _schema_msg("s", properties={"qty": {"type": "integer"}}),
        )
        assert result.is_success
        assert result.value is not None
        assert result.value.record["QTY"] == 10

    def test_transform_without_schema(self) -> None:
        transformer = WMSDataTransformer()
        result = transformer.transform_record(_record_msg("s", {"name": "bob"}), None)
        assert result.is_success
        assert result.value is not None
        assert "NAME" in result.value.record


class TestWMSSchemaMapper:
    """Tests for WMSSchemaMapper.map_stream_schema."""

    def test_returns_catalog_entry(self) -> None:
        mapper = WMSSchemaMapper()
        result = mapper.map_stream_schema(_schema_msg("inventory"))
        assert result.is_success
        assert result.value is not None
        entry = result.value
        assert entry.stream == "inventory"
        assert entry.tap_stream_id == "inventory"
        assert entry.table_name == "INVENTORY"

    def test_preserves_key_properties(self) -> None:
        mapper = WMSSchemaMapper()
        result = mapper.map_stream_schema(_schema_msg("s", key_properties=["a", "b"]))
        assert result.value is not None
        assert result.value.key_properties == ["a", "b"]


class TestWMSTableManager:
    """Tests for WMSTableManager."""

    def test_register_stream_returns_uppercase(self) -> None:
        tm = WMSTableManager()
        result = tm.register_stream("orders")
        assert result.is_success
        assert result.value == "ORDERS"

    def test_get_registered_table(self) -> None:
        tm = WMSTableManager()
        tm.register_stream("items")
        result = tm.get_table_name("items")
        assert result.is_success
        assert result.value == "ITEMS"

    def test_get_unregistered_fails(self) -> None:
        tm = WMSTableManager()
        result = tm.get_table_name("nope")
        assert result.is_failure

    def test_multiple_streams(self) -> None:
        tm = WMSTableManager()
        tm.register_stream("a")
        tm.register_stream("b")
        result_a = tm.get_table_name("a")
        assert result_a.is_success
        assert result_a.value is not None
        result_b = tm.get_table_name("b")
        assert result_b.is_success
        assert result_b.value is not None
        assert result_a.value == "A"
        assert result_b.value == "B"
