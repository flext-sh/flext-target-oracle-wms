"""Component integration tests for target Oracle WMS.

Tests target initialization and component wiring.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import tm

from tests import c, m, p, t, u


def _valid_config() -> t.JsonMapping:
    return {
        "wms_auth": {
            "base_url": "https://test.wms.example.com",
            "username": "user",
            "password": "pass",
        }
    }


def _schema_msg(stream: str = "items") -> p.Meltano.SingerSchemaMessage:
    return m.Meltano.SingerSchemaMessage(
        type=c.Meltano.SingerMessageType.SCHEMA,
        stream=stream,
        schema_definition={"type": "object"},
        key_properties=["id"],
    )


def _record_msg(
    stream: str = "items", record: t.JsonMapping | None = None
) -> p.Meltano.SingerRecordMessage:
    return m.Meltano.SingerRecordMessage(
        type=c.Meltano.SingerMessageType.RECORD,
        stream=stream,
        record=record or {"id": "1"},
    )


class TestsFlextTargetOracleWmsSinks:
    """Verify target initializes all expected sub-components."""

    def test_target_has_catalog_manager(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        tm.that(target.catalog_manager, is_=u.TargetOracleWms.CatalogManager)

    def test_target_has_table_manager(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        tm.that(target.table_manager, is_=u.TargetOracleWms.WMSTableManager)

    def test_target_has_data_transformer(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        tm.that(target.data_transformer, is_=u.TargetOracleWms.WMSDataTransformer)

    def test_target_has_stream_processor(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        tm.that(target.stream_processor, is_=u.TargetOracleWms.StreamProcessor)

    def test_stream_processor_uses_table_manager(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        assert target.stream_processor.table_manager is target.table_manager

    def test_stream_processor_uses_data_transformer(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        assert target.stream_processor.data_transformer is target.data_transformer

    def test_schema_registers_in_both_catalog_and_table(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        schema = _schema_msg("items")
        target.handle_schema_message(schema)
        tm.ok(target.catalog_manager.get_stream("items"))
        tm.ok(target.table_manager.get_table_name("items"))

    def test_table_name_is_uppercased_stream(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        schema = _schema_msg("orders")
        target.handle_schema_message(schema)
        table_result = target.table_manager.get_table_name("orders")
        tm.ok(table_result)
        tm.that(table_result.value, none=False)
        tm.that(table_result.value, eq="ORDERS")

    def test_record_keys_uppercased(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        schema = _schema_msg("s")
        target.handle_schema_message(schema)
        record = _record_msg("s", {"name": "test"})
        result = target.handle_record_message(record)
        tm.ok(result)
