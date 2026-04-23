"""Tests for FlextTargetOracleWmsStreamProcessor.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from unittest.mock import MagicMock

from flext_target_oracle_wms import (
    StreamProcessor as FlextTargetOracleWmsStreamProcessor,
)
from tests import m, r, t, u


def _schema_msg(
    stream: str = "test_stream",
    schema: t.JsonMapping | None = None,
    key_properties: t.StrSequence | None = None,
) -> m.Meltano.SingerSchemaMessage:
    return m.Meltano.SingerSchemaMessage.model_validate({
        "type": "SCHEMA",
        "stream": stream,
        "schema": schema or {"type": "object"},
        "key_properties": key_properties or ["id"],
    })


def _record_msg(
    stream: str = "test_stream",
    record: t.JsonMapping | None = None,
) -> m.Meltano.SingerRecordMessage:
    return m.Meltano.SingerRecordMessage.model_validate({
        "type": "RECORD",
        "stream": stream,
        "record": record or {"id": "1"},
    })


class TestStreamProcessorInitialize:
    """Tests for FlextTargetOracleWmsStreamProcessor.initialize_stream."""

    def test_initialize_stream_success(self) -> None:
        proc = FlextTargetOracleWmsStreamProcessor(
            u.TargetOracleWms.WMSTableManager(),
            u.TargetOracleWms.WMSDataTransformer(),
        )
        result = proc.initialize_stream(_schema_msg("orders"))
        assert result.success
        assert result.value is True

    def test_initialize_registers_table(self) -> None:
        tm = u.TargetOracleWms.WMSTableManager()
        proc = FlextTargetOracleWmsStreamProcessor(
            tm,
            u.TargetOracleWms.WMSDataTransformer(),
        )
        proc.initialize_stream(_schema_msg("items"))
        table_result = tm.get_table_name("items")
        assert table_result.success
        assert table_result.value == "ITEMS"


class TestStreamProcessorRecord:
    """Tests for FlextTargetOracleWmsStreamProcessor.process_record."""

    def test_process_record_after_init(self) -> None:
        proc = FlextTargetOracleWmsStreamProcessor(
            u.TargetOracleWms.WMSTableManager(),
            u.TargetOracleWms.WMSDataTransformer(),
        )
        schema = _schema_msg("orders")
        proc.initialize_stream(schema)
        result = proc.process_record(_record_msg("orders", {"id": "1"}), schema)
        assert result.success

    def test_process_record_without_init_fails(self) -> None:
        proc = FlextTargetOracleWmsStreamProcessor(
            u.TargetOracleWms.WMSTableManager(),
            u.TargetOracleWms.WMSDataTransformer(),
        )
        result = proc.process_record(
            _record_msg("orders", {"id": "1"}),
            _schema_msg("orders"),
        )
        assert result.failure
        assert result.error is not None
        assert (
            "not registered" in result.error.lower() or "lookup" in result.error.lower()
        )

    def test_process_record_uppercases_keys(self) -> None:
        proc = FlextTargetOracleWmsStreamProcessor(
            u.TargetOracleWms.WMSTableManager(),
            u.TargetOracleWms.WMSDataTransformer(),
        )
        schema = _schema_msg(
            "s",
            schema={
                "type": "object",
            },
        )
        proc.initialize_stream(schema)
        result = proc.process_record(_record_msg("s", {"name": "hello"}), schema)
        assert result.success
        assert result.value is not None
        transformed = result.value
        assert "NAME" in transformed.record

    def test_process_record_with_transformer_failure(self) -> None:
        tm = u.TargetOracleWms.WMSTableManager()
        dt = MagicMock(spec=u.TargetOracleWms.WMSDataTransformer)
        dt.transform_record.return_value = r.fail("transformer error")
        proc = FlextTargetOracleWmsStreamProcessor(tm, dt)
        tm.register_stream("s")
        result = proc.process_record(_record_msg("s"), _schema_msg("s"))
        assert result.failure


class TestStreamProcessorMultipleStreams:
    """Tests for processing multiple streams."""

    def test_two_independent_streams(self) -> None:
        proc = FlextTargetOracleWmsStreamProcessor(
            u.TargetOracleWms.WMSTableManager(),
            u.TargetOracleWms.WMSDataTransformer(),
        )
        schema_a = _schema_msg("alpha")
        schema_b = _schema_msg("beta")
        proc.initialize_stream(schema_a)
        proc.initialize_stream(schema_b)
        r_a = proc.process_record(_record_msg("alpha", {"id": "1"}), schema_a)
        r_b = proc.process_record(_record_msg("beta", {"id": "2"}), schema_b)
        assert r_a.success
        assert r_b.success
