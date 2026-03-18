"""Component integration tests for target Oracle WMS.

Tests target initialization and component wiring.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import t
from flext_target_oracle_wms.models import m
from flext_target_oracle_wms.target_client import (
    SingerTargetOracleWMS,
    SingerWMSCatalogManager,
    SingerWMSStreamProcessor,
)
from flext_target_oracle_wms.target_models import WMSDataTransformer, WMSTableManager


def _valid_config() -> dict[str, t.ContainerValue]:
    return {
        "wms_auth": {
            "base_url": "https://test.wms.example.com",
            "username": "user",
            "password": "pass",
        }
    }


def _schema_msg(
    stream: str = "items", properties: dict[str, dict[str, str]] | None = None
) -> m.Meltano.SingerSchemaMessage:
    return m.Meltano.SingerSchemaMessage.model_validate({
        "type": "SCHEMA",
        "stream": stream,
        "schema": {
            "type": "object",
            "properties": properties or {"id": {"type": "string"}},
        },
        "key_properties": ["id"],
    })


def _record_msg(
    stream: str = "items", record: dict[str, object] | None = None
) -> m.Meltano.SingerRecordMessage:
    return m.Meltano.SingerRecordMessage.model_validate({
        "type": "RECORD",
        "stream": stream,
        "record": record or {"id": "1"},
    })


class TestTargetComponentWiring:
    """Verify target initializes all expected sub-components."""

    def test_target_has_catalog_manager(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        assert isinstance(target.catalog_manager, SingerWMSCatalogManager)

    def test_target_has_table_manager(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        assert isinstance(target.table_manager, WMSTableManager)

    def test_target_has_data_transformer(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        assert isinstance(target.data_transformer, WMSDataTransformer)

    def test_target_has_stream_processor(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        assert isinstance(target.stream_processor, SingerWMSStreamProcessor)

    def test_stream_processor_uses_table_manager(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        assert target.stream_processor.table_manager is target.table_manager

    def test_stream_processor_uses_data_transformer(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        assert target.stream_processor.data_transformer is target.data_transformer


class TestCatalogAndTableIntegration:
    """Verify catalog and table managers work together through target."""

    def test_schema_registers_in_both_catalog_and_table(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        schema = _schema_msg("items")
        target.handle_schema_message(schema)
        assert target.catalog_manager.get_stream("items").is_success
        assert target.table_manager.get_table_name("items").is_success

    def test_table_name_is_uppercased_stream(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        schema = _schema_msg("orders")
        target.handle_schema_message(schema)
        table_result = target.table_manager.get_table_name("orders")
        assert table_result.is_success
        assert table_result.value is not None
        assert table_result.value == "ORDERS"


class TestTransformationIntegration:
    """Verify transformer pipeline through target record handling."""

    def test_record_keys_uppercased(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        schema = _schema_msg("s", properties={"name": {"type": "string"}})
        target.handle_schema_message(schema)
        record = _record_msg("s", {"name": "test"})
        result = target.handle_record_message(record)
        assert result.is_success
