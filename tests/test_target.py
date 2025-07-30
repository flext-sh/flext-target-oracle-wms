"""Tests for TargetOracleWMS."""

from __future__ import annotations

# DRY: Import from REAL implementation - NO DUPLICATION
from flext_target_oracle_wms import TargetOracleWMS


class TestTargetOracleWMS:
    """Test the TargetOracleWMS class."""

    def test_target_initialization(self) -> None:
        """Test target can be initialized with config - DRY REFACTORED."""
        config = {
            "base_url": "https://test.wms.example.com",
            "username": "test_user",
            "password": "test_pass",
            "environment": "test",
        }
        target = TargetOracleWMS(config)
        if target.name != "target-oracle-wms":
            msg = f"Expected target-oracle-wms, got {target.name}"
            raise AssertionError(msg)
        assert target.config == config

    def test_target_configuration_options(self) -> None:
        """Test target configuration options - REAL implementation."""
        config = {
            "base_url": "https://test.wms.example.com",
            "batch_size": 500,
            "load_method": "UPSERT",
            "table_prefix": "TEST_",
        }
        target = TargetOracleWMS(config)
        assert target.batch_size == 500
        assert target.load_method == "UPSERT"
        assert target.table_prefix == "TEST_"

    def test_target_plugin_system(self) -> None:
        """Test target plugin system - REAL flext-plugin integration."""
        config = {
            "base_url": "https://test.wms.example.com",
            "enable_plugins": True,
            "plugin_directory": "./custom_plugins",
        }
        target = TargetOracleWMS(config)
        assert target.plugin_enabled is True
        assert target.plugin_directory == "./custom_plugins"

    def test_target_components_initialization(self) -> None:
        """Test that WMS components are initialized correctly - REAL implementation."""
        config = {"base_url": "https://test.wms.example.com"}
        target = TargetOracleWMS(config)

        # Test that components are initialized
        assert target.catalog_manager is not None
        assert target.table_manager is not None
        assert target.data_transformer is not None
        assert target.stream_processor is not None
        assert target.oracle_client is not None

    def test_oracle_wms_client_integration(self) -> None:
        """Test Oracle WMS client integration - REAL flext-oracle-wms."""
        config = {"base_url": "https://test.wms.example.com"}
        target = TargetOracleWMS(config)
        assert target.oracle_client is not None

    def test_wms_table_manager_integration(self) -> None:
        """Test WMS table manager functionality - REAL implementation."""
        config = {"base_url": "https://test.wms.example.com"}
        target = TargetOracleWMS(config)

        # Test table name generation
        table_name = target.table_manager.generate_table_name("test_stream")
        assert isinstance(table_name, str)
        assert len(table_name) > 0

    def test_data_transformer_integration(self) -> None:
        """Test data transformer functionality - REAL implementation."""
        config = {"base_url": "https://test.wms.example.com"}
        target = TargetOracleWMS(config)

        # Test record transformation with REAL data transformer API
        test_record = {"field1": "value1", "field2": 123}
        test_schema = {
            "properties": {"field1": {"type": "string"}, "field2": {"type": "integer"}},
        }

        result = target.data_transformer.transform_record(test_record, test_schema)
        assert result.is_success
        assert result.data is not None

        # Test transformed data structure
        transformed_data = result.data
        assert isinstance(transformed_data, dict)
        assert (
            "FIELD1" in transformed_data
        )  # Oracle column names are normalized to uppercase
        assert "FIELD2" in transformed_data
        assert transformed_data["FIELD1"] == "value1"
        assert transformed_data["FIELD2"] == 123
