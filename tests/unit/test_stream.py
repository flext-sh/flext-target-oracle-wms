"""Tests for u.TargetOracleWms.StreamProcessor.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from tests import c, m, p, r, t, tm, u


class TestsFlextTargetOracleWmsStream:
    """Tests for u.TargetOracleWms.StreamProcessor.initialize_stream.

    Stream lifecycle: init, register, process, failure handling.
    """

    class FailingTransformer(u.TargetOracleWms.WMSDataTransformer):
        """Real transformer subclass forcing transform_record to fail (no Mock)."""

        __test__ = False

        @override
        def transform_record(
            self,
            record_message: m.Meltano.SingerRecordMessage | t.JsonMapping,
            schema_message: m.Meltano.SingerSchemaMessage | t.JsonMapping | None = None,
        ) -> p.Result[m.Meltano.SingerRecordMessage]:
            _ = record_message, schema_message
            return r[m.Meltano.SingerRecordMessage].fail("transformer error")

    @staticmethod
    def test_initialize_stream_success() -> None:
        """Test initialize stream success."""
        proc = u.TargetOracleWms.StreamProcessor(
            u.TargetOracleWms.WMSTableManager(),
            u.TargetOracleWms.WMSDataTransformer(),
        )
        result = proc.initialize_stream(u.TargetOracleWms.Tests.schema_msg("orders"))
        tm.ok(result)
        tm.ok(result.value)

    @staticmethod
    def test_initialize_registers_table() -> None:
        """Test initialize registers table."""
        manager = u.TargetOracleWms.WMSTableManager()
        proc = u.TargetOracleWms.StreamProcessor(
            manager,
            u.TargetOracleWms.WMSDataTransformer(),
        )
        proc.initialize_stream(u.TargetOracleWms.Tests.schema_msg("items"))
        table_result = manager.get_table_name("items")
        tm.ok(table_result, eq="ITEMS")

    @staticmethod
    def test_process_record_after_init() -> None:
        """Test process record after init."""
        proc = u.TargetOracleWms.StreamProcessor(
            u.TargetOracleWms.WMSTableManager(),
            u.TargetOracleWms.WMSDataTransformer(),
        )
        schema = u.TargetOracleWms.Tests.schema_msg("orders")
        proc.initialize_stream(schema)
        result = proc.process_record(
            u.TargetOracleWms.Tests.record_msg(
                "orders", {"id": c.ParserBooleanToken.ONE}
            ),
            schema,
        )
        tm.ok(result)

    @staticmethod
    def test_process_record_without_init_fails() -> None:
        """Test process record without init fails."""
        proc = u.TargetOracleWms.StreamProcessor(
            u.TargetOracleWms.WMSTableManager(),
            u.TargetOracleWms.WMSDataTransformer(),
        )
        result = proc.process_record(
            u.TargetOracleWms.Tests.record_msg(
                "orders", {"id": c.ParserBooleanToken.ONE}
            ),
            u.TargetOracleWms.Tests.schema_msg("orders"),
        )
        error = tm.fail(result)
        tm.ok("not registered" in error.lower() or "lookup" in error.lower())

    @staticmethod
    def test_process_record_with_transformer_failure() -> None:
        """Test process record with transformer failure."""
        manager = u.TargetOracleWms.WMSTableManager()
        proc = u.TargetOracleWms.StreamProcessor(
            manager,
            TestsFlextTargetOracleWmsStream.FailingTransformer(),
        )
        manager.register_stream("s")
        result = proc.process_record(
            u.TargetOracleWms.Tests.record_msg("s"),
            u.TargetOracleWms.Tests.schema_msg("s"),
        )
        tm.fail(result)
