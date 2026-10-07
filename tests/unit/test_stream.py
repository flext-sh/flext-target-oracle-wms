"""Tests for u.TargetOracleWms.StreamProcessor.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_tests import r, tm

from tests import m, p, t, u
from tests._helpers import _record_msg, _schema_msg


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


class TestsFlextTargetOracleWmsStream:
    """Tests for u.TargetOracleWms.StreamProcessor.initialize_stream.

    Stream lifecycle: init, register, process, failure handling.
    """

    @staticmethod
    def test_initialize_stream_success() -> None:
        """Test initialize stream success."""
        proc = u.TargetOracleWms.StreamProcessor(
            u.TargetOracleWms.WMSTableManager(),
            u.TargetOracleWms.WMSDataTransformer(),
        )
        result = proc.initialize_stream(_schema_msg("orders"))
        tm.ok(result)
        tm.that(result.value, eq=True)

    @staticmethod
    def test_initialize_registers_table() -> None:
        """Test initialize registers table."""
        manager = u.TargetOracleWms.WMSTableManager()
        proc = u.TargetOracleWms.StreamProcessor(
            manager,
            u.TargetOracleWms.WMSDataTransformer(),
        )
        proc.initialize_stream(_schema_msg("items"))
        table_result = manager.get_table_name("items")
        tm.ok(table_result)
        tm.that(table_result.value, eq="ITEMS")

    @staticmethod
    def test_process_record_after_init() -> None:
        """Test process record after init."""
        proc = u.TargetOracleWms.StreamProcessor(
            u.TargetOracleWms.WMSTableManager(),
            u.TargetOracleWms.WMSDataTransformer(),
        )
        schema = _schema_msg("orders")
        proc.initialize_stream(schema)
        result = proc.process_record(_record_msg("orders", {"id": "1"}), schema)
        tm.ok(result)

    @staticmethod
    def test_process_record_without_init_fails() -> None:
        """Test process record without init fails."""
        proc = u.TargetOracleWms.StreamProcessor(
            u.TargetOracleWms.WMSTableManager(),
            u.TargetOracleWms.WMSDataTransformer(),
        )
        result = proc.process_record(
            _record_msg("orders", {"id": "1"}),
            _schema_msg("orders"),
        )
        tm.fail(result)
        error = result.error
        assert error is not None
        assert "not registered" in error.lower() or "lookup" in error.lower()

    @staticmethod
    def test_process_record_uppercases_keys() -> None:
        """Test process record uppercases keys."""
        proc = u.TargetOracleWms.StreamProcessor(
            u.TargetOracleWms.WMSTableManager(),
            u.TargetOracleWms.WMSDataTransformer(),
        )
        schema = _schema_msg("s")
        proc.initialize_stream(schema)
        result = proc.process_record(_record_msg("s", {"name": "hello"}), schema)
        tm.ok(result)
        tm.that(result.value, none=False)
        transformed = result.value
        tm.that(transformed.record, has="NAME")

    @staticmethod
    def test_process_record_with_transformer_failure() -> None:
        """Test process record with transformer failure."""
        manager = u.TargetOracleWms.WMSTableManager()
        proc = u.TargetOracleWms.StreamProcessor(manager, _FailingTransformer())
        manager.register_stream("s")
        result = proc.process_record(_record_msg("s"), _schema_msg("s"))
        tm.fail(result)

    @staticmethod
    def test_two_independent_streams() -> None:
        """Test two independent streams."""
        proc = u.TargetOracleWms.StreamProcessor(
            u.TargetOracleWms.WMSTableManager(),
            u.TargetOracleWms.WMSDataTransformer(),
        )
        schema_a = _schema_msg("alpha")
        schema_b = _schema_msg("beta")
        proc.initialize_stream(schema_a)
        proc.initialize_stream(schema_b)
        r_a = proc.process_record(_record_msg("alpha", {"id": "1"}), schema_a)
        r_b = proc.process_record(_record_msg("beta", {"id": "2"}), schema_b)
        tm.ok(r_a)
        tm.ok(r_b)
