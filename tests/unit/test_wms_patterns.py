"""Tests for WMS target model helpers.

Covers WMSTypeConverter, WMSDataTransformer, and WMSTableManager.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import math

from tests import t, tm, u
from tests._helpers import _record_msg, _schema_msg


class TestsFlextTargetOracleWmsWmsPatterns:
    """Tests for WMSTypeConverter.convert_singer_to_oracle."""

    @staticmethod
    def test_string_type() -> None:
        """Test string type."""
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "string",
            "hello",
        )
        tm.ok(result)
        tm.that(result.value, eq="hello")

    @staticmethod
    def test_integer_type() -> None:
        """Test integer type."""
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "integer",
            42,
        )
        tm.ok(result)
        tm.that(result.value, eq=42)

    @staticmethod
    def test_number_type_float() -> None:
        """Test number type float."""
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "number",
            math.pi,
        )
        tm.ok(result)
        tm.that(result.value, eq=math.pi)

    @staticmethod
    def test_none_value() -> None:
        """Test none value."""
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "string",
            "",
        )
        tm.ok(result)
        tm.that(result.value, eq="")

    @staticmethod
    def test_object_type_serializes_to_json() -> None:
        """Test object type serializes to json."""
        data = '{"nested": "value"}'
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "object",
            data,
        )
        tm.ok(result)
        tm.that(result.value, none=False)
        tm.that(t.str_adapter().validate_json(str(result.value)), eq=data)

    @staticmethod
    def test_array_type_serializes_to_json() -> None:
        """Test array type serializes to json."""
        data = "[1, 2, 3]"
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "array",
            data,
        )
        tm.ok(result)
        tm.that(result.value, none=False)
        tm.that(t.str_adapter().validate_json(str(result.value)), eq=data)

    @staticmethod
    def test_boolean_type_becomes_string() -> None:
        """Test boolean type becomes string."""
        result = u.TargetOracleWms.WMSTypeConverter().convert_singer_to_oracle(
            "boolean",
            value=True,
        )
        tm.ok(result)
        tm.that(result.value, eq="True")

    @staticmethod
    def test_uppercases_record_keys() -> None:
        """Test uppercases record keys."""
        transformer = u.TargetOracleWms.WMSDataTransformer()
        result = transformer.transform_record(
            _record_msg("s", {"name": "alice", "age": "30"}),
            _schema_msg("s"),
        )
        tm.ok(result)
        tm.that(result.value, none=False)
        tm.that(result.value.record, has="NAME")
        tm.that(result.value.record, has="AGE")

    @staticmethod
    def test_preserves_stream_name() -> None:
        """Test preserves stream name."""
        transformer = u.TargetOracleWms.WMSDataTransformer()
        result = transformer.transform_record(
            _record_msg("orders", {"id": "1"}),
            _schema_msg("orders"),
        )
        tm.ok(result)
        tm.that(result.value, none=False)
        tm.that(result.value.stream, eq="orders")

    @staticmethod
    def test_uses_custom_type_converter() -> None:
        """Test uses custom type converter."""
        converter = u.TargetOracleWms.WMSTypeConverter()
        transformer = u.TargetOracleWms.WMSDataTransformer(type_converter=converter)
        result = transformer.transform_record(
            _record_msg("s", {"qty": 10}),
            _schema_msg("s"),
        )
        tm.ok(result)
        tm.that(result.value, none=False)
        tm.that(result.value.record, has="QTY")

    @staticmethod
    def test_transform_without_schema() -> None:
        """Test transform without schema."""
        transformer = u.TargetOracleWms.WMSDataTransformer()
        result = transformer.transform_record(_record_msg("s", {"name": "bob"}), None)
        tm.ok(result)
        tm.that(result.value, none=False)
        tm.that(result.value.record, has="NAME")

    @staticmethod
    def test_register_stream_returns_uppercase() -> None:
        """Test register stream returns uppercase."""
        manager = u.TargetOracleWms.WMSTableManager()
        result = manager.register_stream("orders")
        tm.ok(result)
        tm.that(result.value, eq="ORDERS")

    @staticmethod
    def test_get_registered_table() -> None:
        """Test get registered table."""
        manager = u.TargetOracleWms.WMSTableManager()
        manager.register_stream("items")
        result = manager.get_table_name("items")
        tm.ok(result)
        tm.that(result.value, eq="ITEMS")

    @staticmethod
    def test_get_unregistered_fails() -> None:
        """Test get unregistered fails."""
        manager = u.TargetOracleWms.WMSTableManager()
        result = manager.get_table_name("nope")
        tm.fail(result)

    @staticmethod
    def test_multiple_streams() -> None:
        """Test multiple streams."""
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
