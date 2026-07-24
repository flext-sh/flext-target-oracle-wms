"""Tests for u.TargetOracleWms.StreamProcessor.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, override

from flext_tests import r, tm
from tests import c, m, u

if TYPE_CHECKING:
    from tests import p, t


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
    stream: str = "test_stream", record: t.JsonMapping | None = None
) -> m.Meltano.SingerRecordMessage:
    return m.Meltano.SingerRecordMessage(
        type=c.Meltano.SingerMessageType.RECORD,
        stream=stream,
        record=record or {"id": "1"},
    )


class TestsFlextTargetOracleWmsStream:
    """Tests for u.TargetOracleWms.StreamProcessor.initialize_stream."""

    def test_initialize_stream_success(self) -> None:
        proc = u.TargetOracleWms.StreamProcessor(
            u.TargetOracleWms.WMSTableManager(), u.TargetOracleWms.WMSDataTransformer()
        )
        result = proc.initialize_stream(_schema_msg("orders"))
        tm.ok(result)
        tm.that(result.value, eq=True)

    def test_initialize_registers_table(self) -> None:
        manager = u.TargetOracleWms.WMSTableManager()
        proc = u.TargetOracleWms.StreamProcessor(
            manager, u.TargetOracleWms.WMSDataTransformer()
        )
        proc.initialize_stream(_schema_msg("items"))
        table_result = manager.get_table_name("items")
        tm.ok(table_result)
        tm.that(table_result.value, eq="ITEMS")

    def test_process_record_after_init(self) -> None:
        proc = u.TargetOracleWms.StreamProcessor(
            u.TargetOracleWms.WMSTableManager(), u.TargetOracleWms.WMSDataTransformer()
        )
        schema = _schema_msg("orders")
        proc.initialize_stream(schema)
        result = proc.process_record(_record_msg("orders", {"id": "1"}), schema)
        tm.ok(result)

    def test_process_record_without_init_fails(self) -> None:
        proc = u.TargetOracleWms.StreamProcessor(
            u.TargetOracleWms.WMSTableManager(), u.TargetOracleWms.WMSDataTransformer()
        )
        result = proc.process_record(
            _record_msg("orders", {"id": "1"}), _schema_msg("orders")
        )
        tm.fail(result)
        error = result.error
        assert error is not None
        assert "not registered" in error.lower() or "lookup" in error.lower()

    def test_process_record_uppercases_keys(self) -> None:
        proc = u.TargetOracleWms.StreamProcessor(
            u.TargetOracleWms.WMSTableManager(), u.TargetOracleWms.WMSDataTransformer()
        )
        schema = _schema_msg("s", schema={"type": "object"})
        proc.initialize_stream(schema)
        result = proc.process_record(_record_msg("s", {"name": "hello"}), schema)
        tm.ok(result)
        tm.that(result.value, none=False)
        transformed = result.value
        tm.that(transformed.record, has="NAME")

    def test_process_record_with_transformer_failure(self) -> None:
        manager = u.TargetOracleWms.WMSTableManager()
        proc = u.TargetOracleWms.StreamProcessor(manager, _FailingTransformer())
        manager.register_stream("s")
        result = proc.process_record(_record_msg("s"), _schema_msg("s"))
        tm.fail(result)

    def test_two_independent_streams(self) -> None:
        proc = u.TargetOracleWms.StreamProcessor(
            u.TargetOracleWms.WMSTableManager(), u.TargetOracleWms.WMSDataTransformer()
        )
        schema_a = _schema_msg("alpha")
        schema_b = _schema_msg("beta")
        proc.initialize_stream(schema_a)
        proc.initialize_stream(schema_b)
        r_a = proc.process_record(_record_msg("alpha", {"id": "1"}), schema_a)
        r_b = proc.process_record(_record_msg("beta", {"id": "2"}), schema_b)
        tm.ok(r_a)
        tm.ok(r_b)
