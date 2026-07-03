"""Component integration tests for target Oracle WMS.

Tests target initialization and component wiring.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from tests.constants import c
from tests.models import m
from tests.typings import t
from tests.utilities import u


def _valid_config() -> t.JsonMapping:
    return {
        "wms_auth": {
            "base_url": "https://test.wms.example.com",
            "username": "user",
            "password": "pass",
        },
    }


def _schema_msg(stream: str = "items") -> m.Meltano.SingerSchemaMessage:
    return m.Meltano.SingerSchemaMessage(
        type=c.Meltano.SingerMessageType.SCHEMA,
        stream=stream,
        schema_definition={
            "type": "object",
        },
        key_properties=["id"],
    )


def _record_msg(
    stream: str = "items",
    record: t.JsonMapping | None = None,
) -> m.Meltano.SingerRecordMessage:
    return m.Meltano.SingerRecordMessage(
        type=c.Meltano.SingerMessageType.RECORD,
        stream=stream,
        record=record or {"id": "1"},
    )


class TestsFlextTargetOracleWmsSinks:
    """Verify target initializes all expected sub-components."""

    def test_target_has_catalog_manager(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        assert isinstance(target.catalog_manager, u.TargetOracleWms.CatalogManager)

    def test_target_has_table_manager(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        assert isinstance(target.table_manager, u.TargetOracleWms.WMSTableManager)

    def test_target_has_data_transformer(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        assert isinstance(target.data_transformer, u.TargetOracleWms.WMSDataTransformer)

    def test_target_has_stream_processor(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        assert isinstance(target.stream_processor, u.TargetOracleWms.StreamProcessor)

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
        assert target.catalog_manager.get_stream("items").success
        assert target.table_manager.get_table_name("items").success

    def test_table_name_is_uppercased_stream(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        schema = _schema_msg("orders")
        target.handle_schema_message(schema)
        table_result = target.table_manager.get_table_name("orders")
        assert table_result.success
        assert table_result.value is not None
        assert table_result.value == "ORDERS"

    def test_record_keys_uppercased(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        schema = _schema_msg("s")
        target.handle_schema_message(schema)
        record = _record_msg("s", {"name": "test"})
        result = target.handle_record_message(record)
        assert result.success
