"""Tests for SingerWMSStreamProcessor.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from unittest.mock import MagicMock

from flext_core import r

from flext_target_oracle_wms.target_client import SingerWMSStreamProcessor
from flext_target_oracle_wms.target_models import WMSDataTransformer, WMSTableManager


def _schema_msg(
    stream: str = "test_stream",
    schema: dict[str, object] | None = None,
    key_properties: list[str] | None = None,
) -> dict[str, object]:
    return {
        "type": "SCHEMA",
        "stream": stream,
        "schema": schema
        or {"type": "object", "properties": {"id": {"type": "string"}}},
        "key_properties": key_properties or ["id"],
    }


def _record_msg(
    stream: str = "test_stream", record: dict[str, object] | None = None
) -> dict[str, object]:
    return {"type": "RECORD", "stream": stream, "record": record or {"id": "1"}}


class TestStreamProcessorInitialize:
    """Tests for SingerWMSStreamProcessor.initialize_stream."""

    def test_initialize_stream_success(self) -> None:
        proc = SingerWMSStreamProcessor(WMSTableManager(), WMSDataTransformer())
        result = proc.initialize_stream(_schema_msg("orders"))
        assert result.is_success
        assert result.value is True

    def test_initialize_registers_table(self) -> None:
        tm = WMSTableManager()
        proc = SingerWMSStreamProcessor(tm, WMSDataTransformer())
        proc.initialize_stream(_schema_msg("items"))
        table_result = tm.get_table_name("items")
        assert table_result.is_success
        assert table_result.value == "ITEMS"


class TestStreamProcessorRecord:
    """Tests for SingerWMSStreamProcessor.process_record."""

    def test_process_record_after_init(self) -> None:
        proc = SingerWMSStreamProcessor(WMSTableManager(), WMSDataTransformer())
        schema = _schema_msg("orders")
        proc.initialize_stream(schema)
        result = proc.process_record(_record_msg("orders", {"id": "1"}), schema)
        assert result.is_success

    def test_process_record_without_init_fails(self) -> None:
        proc = SingerWMSStreamProcessor(WMSTableManager(), WMSDataTransformer())
        result = proc.process_record(
            _record_msg("orders", {"id": "1"}), _schema_msg("orders")
        )
        assert result.is_failure
        assert (
            "not registered" in (result.error or "").lower()
            or "lookup" in (result.error or "").lower()
        )

    def test_process_record_uppercases_keys(self) -> None:
        proc = SingerWMSStreamProcessor(WMSTableManager(), WMSDataTransformer())
        schema = _schema_msg(
            "s", schema={"type": "object", "properties": {"name": {"type": "string"}}}
        )
        proc.initialize_stream(schema)
        result = proc.process_record(_record_msg("s", {"name": "hello"}), schema)
        assert result.is_success
        transformed = result.value
        assert "NAME" in transformed.record

    def test_process_record_with_transformer_failure(self) -> None:
        tm = WMSTableManager()
        dt = MagicMock(spec=WMSDataTransformer)
        dt.transform_record.return_value = r[object].fail("transformer error")
        proc = SingerWMSStreamProcessor(tm, dt)
        tm.register_stream("s")
        result = proc.process_record(_record_msg("s"), _schema_msg("s"))
        assert result.is_failure


class TestStreamProcessorMultipleStreams:
    """Tests for processing multiple streams."""

    def test_two_independent_streams(self) -> None:
        proc = SingerWMSStreamProcessor(WMSTableManager(), WMSDataTransformer())
        schema_a = _schema_msg("alpha")
        schema_b = _schema_msg("beta")
        proc.initialize_stream(schema_a)
        proc.initialize_stream(schema_b)
        r_a = proc.process_record(_record_msg("alpha", {"id": "1"}), schema_a)
        r_b = proc.process_record(_record_msg("beta", {"id": "2"}), schema_b)
        assert r_a.is_success
        assert r_b.is_success
