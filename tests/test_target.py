"""Tests for TargetOracleWMS."""

from __future__ import annotations

from typing import Any

import pytest

from flext_target_oracle_wms.sinks.generic import (
    GenericWMSSink,
)
from flext_target_oracle_wms.sinks.inventory import (
    InventorySink,
)
from flext_target_oracle_wms.sinks.orders import (
    OrderSink,
)
from flext_target_oracle_wms.sinks.warehouse import (
    WarehouseSink,
)
from flext_target_oracle_wms.target import TargetOracleWMS


class TestTargetOracleWMS:
    """Test the TargetOracleWMS class."""

    def test_target_initialization(self, config: dict[str, Any]) -> None:
        """Test target can be initialized with config."""
        target = TargetOracleWMS(config=config)
        if target.name != "target-oracle-wms":
            raise AssertionError(f"Expected {"target-oracle-wms"}, got {target.name}")
        assert target.config == config

    def test_get_sink_class_inventory_streams(self) -> None:
        """Test that inventory streams return InventorySink."""
        target = TargetOracleWMS(config={})
        inventory_streams = ["inventory", "lots", "locations", "cycle_counts"]
        for stream_name in inventory_streams:
            sink_class = target.get_sink_class(stream_name)
            if sink_class != InventorySink:
                raise AssertionError(f"Expected {InventorySink}, got {sink_class}")

    def test_get_sink_class_order_streams(self) -> None:
        """Test that order streams return OrderSink."""
        target = TargetOracleWMS(config={})
        order_streams = ["orders", "order_lines", "shipments", "allocations"]
        for stream_name in order_streams:
            sink_class = target.get_sink_class(stream_name)
            if sink_class != OrderSink:
                raise AssertionError(f"Expected {OrderSink}, got {sink_class}")

    def test_get_sink_class_warehouse_streams(self) -> None:
        """Test that warehouse streams return WarehouseSink."""
        target = TargetOracleWMS(config={})
        warehouse_streams = ["tasks", "workers", "equipment", "zones"]
        for stream_name in warehouse_streams:
            sink_class = target.get_sink_class(stream_name)
            if sink_class != WarehouseSink:
                raise AssertionError(f"Expected {WarehouseSink}, got {sink_class}")

    def test_get_sink_class_generic_streams(self) -> None:
        """Test that unknown streams return GenericWMSSink."""
        target = TargetOracleWMS(config={})
        generic_streams = ["unknown", "custom_entity", "some_other_stream"]
        for stream_name in generic_streams:
            sink_class = target.get_sink_class(stream_name)
            if sink_class != GenericWMSSink:
                raise AssertionError(f"Expected {GenericWMSSink}, got {sink_class}")

    def test_max_parallelism(self) -> None:
        """Test max parallelism property."""
        target = TargetOracleWMS(config={})
        if target.max_parallelism != 4:
            raise AssertionError(f"Expected {4}, got {target.max_parallelism}")

    def test_config_validation_required_fields(self) -> None:
        """Test that required config fields are validated."""
        # Missing required fields should fail
        with pytest.raises(ValueError, match="Configuration validation failed"):
            TargetOracleWMS(config={}, validate_config=True)
        # All required fields present should succeed
        valid_config = {
            "base_url": "https://test.com",
            "username": "user",
            "password": "pass",
        }
        target = TargetOracleWMS(config=valid_config, validate_config=True)
        if target.config != valid_config:
            raise AssertionError(f"Expected {valid_config}, got {target.config}")

    def test_config_schema(self) -> None:
        """Test config schema is properly defined."""
        schema = TargetOracleWMS.config_jsonschema
        # Check required properties
        if "properties" not in schema:
            raise AssertionError(f"Expected {"properties"} in {schema}")
        assert "base_url" in schema["properties"]
        if "username" not in schema["properties"]:
            raise AssertionError(f"Expected {"username"} in {schema["properties"]}")
        assert "password" in schema["properties"]
        # Check optional properties
        if "timeout" not in schema["properties"]:
            raise AssertionError(f"Expected {"timeout"} in {schema["properties"]}")
        assert "enable_kpi_calculation" in schema["properties"]
        if "enable_alerts" not in schema["properties"]:
            raise AssertionError(f"Expected {"enable_alerts"} in {schema["properties"]}")
        assert "output_path" in schema["properties"]
        if "output_format" not in schema["properties"]:
            raise AssertionError(f"Expected {"output_format"} in {schema["properties"]}")
        # Check required fields
        if schema["required"] != ["base_url", "username", "password"]:
            raise AssertionError(f"Expected {["base_url", "username", "password"]}, got {schema["required"]}")
        # Check secret fields
        if not (schema["properties"]["password"]["secret"]):
            raise AssertionError(f"Expected True, got {schema["properties"]["password"]["secret"]}")
        assert schema["properties"]["database_url"]["secret"] is True
