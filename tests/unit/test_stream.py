"""Tests for FlextTargetOracleWmsStreamProcessor.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_target_oracle_wms import (
    StreamProcessor as FlextTargetOracleWmsStreamProcessor,
)
from tests import c, m, p, r, t, u


class _FailingTransformer(u.TargetOracleWms.WMSDataTransformer):
    """Real transformer subclass forcing transform_record to fail (no Mock)."""

    @override
    def transform_record(
        self,
        record_message: m.Meltano.SingerRecordMessage | t.JsonMapping,
        schema_message: m.Meltano.SingerSchemaMessage | t.JsonMapping | None = None,
    ) -> p.Result[m.Meltano.SingerRecordMessage]:
        _ = record_message, schema_message
        return r[m.Meltano.SingerRecordMessage].fail("transformer error")


def _schema_msg(
    stream: str = "test_stream",
    schema: t.JsonMapping | None = None,
    key_properties: t.StrSequence | None = None,
) -> m.Meltano.SingerSchemaMessage:
    return m.Meltano.SingerSchemaMessage(
        type=c.Meltano.SingerMessageType.SCHEMA,
        stream=stream,
        schema_definition=schema or {"type": "object"},
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


class TestsFlextTargetOracleWmsStream:
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
        proc = FlextTargetOracleWmsStreamProcessor(tm, _FailingTransformer())
        tm.register_stream("s")
        result = proc.process_record(_record_msg("s"), _schema_msg("s"))
        assert result.failure

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
