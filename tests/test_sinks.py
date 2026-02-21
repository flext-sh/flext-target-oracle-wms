"""Component integration tests for target Oracle WMS.

Tests target initialization and component wiring.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import t

from flext_target_oracle_wms.target_client import (
    SingerTargetOracleWMS,
    SingerWMSCatalogManager,
    SingerWMSStreamProcessor,
)
from flext_target_oracle_wms.target_models import WMSDataTransformer, WMSTableManager


def _valid_config() -> dict[str, t.GeneralValueType]:
    return {
        "wms_auth": {
            "base_url": "https://test.wms.example.com",
            "username": "user",
            "password": "pass",
        },
    }


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
        schema = {
            "type": "SCHEMA",
            "stream": "items",
            "schema": {"type": "object", "properties": {"id": {"type": "string"}}},
            "key_properties": ["id"],
        }
        target.handle_schema_message(schema)
        assert target.catalog_manager.get_stream("items").is_success
        assert target.table_manager.get_table_name("items").is_success

    def test_table_name_is_uppercased_stream(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        schema = {
            "type": "SCHEMA",
            "stream": "orders",
            "schema": {"type": "object", "properties": {"id": {"type": "string"}}},
            "key_properties": ["id"],
        }
        target.handle_schema_message(schema)
        assert target.table_manager.get_table_name("orders").value == "ORDERS"


class TestTransformationIntegration:
    """Verify transformer pipeline through target record handling."""

    def test_record_keys_uppercased(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        schema = {
            "type": "SCHEMA",
            "stream": "s",
            "schema": {"type": "object", "properties": {"name": {"type": "string"}}},
            "key_properties": ["name"],
        }
        target.handle_schema_message(schema)
        record = {"type": "RECORD", "stream": "s", "record": {"name": "test"}}
        result = target.handle_record_message(record)
        assert result.is_success
