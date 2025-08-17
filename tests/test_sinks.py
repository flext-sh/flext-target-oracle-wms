"""Tests for Singer Target components - DRY REFACTORED."""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest
from flext_core import FlextResult

from flext_target_oracle_wms import SingerTargetOracleWMS


class TestSingerTargetComponents:
    """Test Singer Target Oracle WMS components - REAL implementation."""

    def test_singer_target_initialization(self) -> None:
        """Test Singer target initialization with components - REAL API."""
        config = {
            "base_url": "https://test.wms.example.com",
            "username": "test_user",
            "password": "test_pass",
            "environment": "test",
        }
        target = SingerTargetOracleWMS(config)

        # Test Singer protocol compliance
        assert target.name == "target-oracle-wms"
        assert target.config == config

        # Test component initialization
        assert target.oracle_client is not None
        assert target.catalog_manager is not None
        assert target.table_manager is not None
        assert target.data_transformer is not None
        assert target.stream_processor is not None

    def test_catalog_manager_functionality(self) -> None:
        """Test catalog manager stream handling - REAL implementation."""
        config = {"base_url": "https://test.wms.example.com"}
        target = SingerTargetOracleWMS(config)

        # Test catalog manager operations
        test_schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
            },
        }

        # Add stream to catalog
        result = target.catalog_manager.add_stream("test_stream", test_schema)
        assert result.success

        # Get stream from catalog
        stream_result = target.catalog_manager.get_stream("test_stream")
        assert stream_result.success
        assert stream_result.data is not None

    def test_table_manager_functionality(self) -> None:
        """Test table manager operations - REAL implementation."""
        config = {"base_url": "https://test.wms.example.com"}
        target = SingerTargetOracleWMS(config)

        # Test table name generation
        table_name = target.table_manager.generate_table_name("test_stream")
        assert isinstance(table_name, str)
        assert table_name == "TEST_STREAM"  # Oracle normalized

        # Test with prefix
        prefixed_name = target.table_manager.generate_table_name(
            "test_stream",
            "PREFIX",
        )
        assert prefixed_name == "PREFIX_TEST_STREAM"

    def test_data_transformer_functionality(self) -> None:
        """Test data transformer operations - REAL implementation."""
        config = {"base_url": "https://test.wms.example.com"}
        target = SingerTargetOracleWMS(config)

        # Test record transformation
        test_record = {"field1": "value1", "field2": 123, "field3": True}
        test_schema = {
            "properties": {
                "field1": {"type": "string"},
                "field2": {"type": "integer"},
                "field3": {"type": "boolean"},
            },
        }

        result = target.data_transformer.transform_record(test_record, test_schema)
        assert result.success
        assert result.data is not None

        transformed = result.data
        assert "FIELD1" in transformed  # Oracle normalized
        assert "FIELD2" in transformed
        assert "FIELD3" in transformed
        assert transformed["FIELD1"] == "value1"
        assert transformed["FIELD2"] == 123
        assert transformed["FIELD3"] == 1  # Boolean converted to 1/0

    def test_stream_processor_functionality(self) -> None:
        """Test stream processor operations - REAL implementation."""
        config = {"base_url": "https://test.wms.example.com"}
        target = SingerTargetOracleWMS(config)

        # Initialize stream
        test_schema = {
            "type": "object",
            "properties": {"id": {"type": "string"}},
        }

        init_result = target.stream_processor.initialize_stream(
            "test_stream",
            test_schema,
        )
        assert init_result.success

        # Process record
        test_record = {"id": "TEST001"}
        process_result = target.stream_processor.process_record(
            "test_stream",
            test_record,
        )
        assert process_result.success
        assert process_result.data is not None

    def test_oracle_wms_client_integration(self) -> None:
        """Test Oracle WMS client integration - REAL flext-oracle-wms."""
        config = {
            "base_url": "https://test.wms.example.com",
            "username": "test_user",
            "password": "test_pass",
            "timeout": 30.0,
            "max_retries": 3,
        }
        target = SingerTargetOracleWMS(config)

        # Test client configuration
        assert target.oracle_client is not None
        # Oracle client should be configured with proper settings
        # (We can't test actual connection without real Oracle WMS instance)

    def test_configuration_options(self) -> None:
        """Test target configuration options - REAL implementation."""
        config = {
            "base_url": "https://test.wms.example.com",
            "batch_size": 500,
            "load_method": "UPSERT",
            "table_prefix": "TEST_",
            "enable_plugins": True,
            "plugin_directory": "./custom_plugins",
        }
        target = SingerTargetOracleWMS(config)

        # Test configuration is applied
        assert target.batch_size == 500
        assert target.load_method == "UPSERT"
        assert target.table_prefix == "TEST_"
        assert target.plugin_enabled is True
        assert target.plugin_directory == "./custom_plugins"

    @pytest.mark.asyncio
    async def test_target_lifecycle(self) -> None:
        """Test complete target lifecycle - REAL implementation."""
        config = {"base_url": "https://test.wms.example.com"}
        target = SingerTargetOracleWMS(config)

        # Mock oracle client for testing using patch

        with (
            patch.object(
                target.oracle_client,
                "start",
                new_callable=AsyncMock,
            ) as mock_start,
            patch.object(
                target.oracle_client,
                "stop",
                new_callable=AsyncMock,
            ) as mock_stop,
        ):
            mock_start.return_value = FlextResult.ok(None)
            mock_stop.return_value = FlextResult.ok(None)

            # Test setup
            setup_result = await target.setup()
            assert setup_result.success

            # Test finalization
            finalize_result = target.finalize()
            assert finalize_result.success
            assert finalize_result.data is not None

            # Test cleanup
            cleanup_result = await target.cleanup()
            assert cleanup_result.success
