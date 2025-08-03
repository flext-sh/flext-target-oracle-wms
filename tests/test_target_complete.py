"""COMPREHENSIVE tests for Singer Target Oracle WMS - REAL flext-core integration targeting 90%+ coverage."""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

# DRY: Import from REAL implementation - NO DUPLICATION
from flext_core import FlextResult

from flext_target_oracle_wms.singer.target import SingerTargetOracleWMS


class TestSingerTargetOracleWMSComprehensive:
    """Comprehensive tests targeting uncovered Singer target functionality."""

    @pytest.fixture
    def oracle_wms_config(self) -> dict[str, object]:
        """Oracle WMS configuration for testing."""
        return {
            "base_url": "https://test.wms.ocs.oraclecloud.com",
            "username": "test_user",
            "password": "test_password",
            "environment": "test",
            "timeout": 30.0,
            "max_retries": 3,
            "batch_size": 1000,
            "load_method": "APPEND_ONLY",
            "table_prefix": "TEST_",
            "default_target_schema": "WMS_TEST",
        }

    @pytest.mark.asyncio
    async def test_setup_with_oracle_client_failure(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test setup when Oracle WMS client fails to start."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock client start to fail
        with patch.object(
            target.oracle_client,
            "start",
            new_callable=AsyncMock,
        ) as mock_start:
            mock_start.return_value = FlextResult.fail("Connection failed")

            result = await target.setup()
            assert not result.is_success
            assert result.error is not None
            assert "Connection failed" in result.error

    @pytest.mark.asyncio
    async def test_setup_with_exception(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test setup when unexpected exception occurs."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock client start to raise exception
        with patch.object(
            target.oracle_client,
            "start",
            new_callable=AsyncMock,
        ) as mock_start:
            mock_start.side_effect = RuntimeError("Unexpected error")

            result = await target.setup()
            assert not result.is_success
            assert result.error is not None
            assert "Setup failed" in result.error

    @pytest.mark.asyncio
    async def test_process_schema_message_invalid_type(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test processing message with invalid type."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        invalid_message = {
            "type": "RECORD",  # Should be SCHEMA
            "stream": "test_table",
            "schema": {"type": "object"},
        }

        result = await target.process_schema_message(invalid_message)
        assert not result.is_success
        assert result.error is not None
        assert "Not a SCHEMA message" in result.error

    @pytest.mark.asyncio
    async def test_process_schema_message_missing_stream(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test processing SCHEMA message with missing stream."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        invalid_message = {
            "type": "SCHEMA",
            # Missing stream
            "schema": {"type": "object"},
        }

        result = await target.process_schema_message(invalid_message)
        assert not result.is_success
        assert result.error is not None
        assert "missing stream or schema" in result.error

    @pytest.mark.asyncio
    async def test_process_schema_message_missing_schema(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test processing SCHEMA message with missing schema."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        invalid_message = {
            "type": "SCHEMA",
            "stream": "test_table",
            # Missing schema
        }

        result = await target.process_schema_message(invalid_message)
        assert not result.is_success
        assert result.error is not None
        assert "missing stream or schema" in result.error

    @pytest.mark.asyncio
    async def test_process_schema_message_catalog_failure(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test processing SCHEMA message when catalog add fails."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock catalog manager to fail
        with patch.object(target.catalog_manager, "add_stream") as mock_add:
            mock_add.return_value = FlextResult.fail("Catalog add failed")

            schema_message = {
                "type": "SCHEMA",
                "stream": "test_table",
                "schema": {"type": "object", "properties": {"id": {"type": "integer"}}},
            }

            result = await target.process_schema_message(schema_message)
            assert not result.is_success
            assert result.error is not None
            assert "Catalog add failed" in result.error

    @pytest.mark.asyncio
    async def test_process_schema_message_stream_init_failure(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test processing SCHEMA message when stream initialization fails."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock stream processor to fail
        with patch.object(target.stream_processor, "initialize_stream") as mock_init:
            mock_init.return_value = FlextResult.fail("Stream init failed")

            schema_message = {
                "type": "SCHEMA",
                "stream": "test_table",
                "schema": {"type": "object", "properties": {"id": {"type": "integer"}}},
            }

            result = await target.process_schema_message(schema_message)
            assert not result.is_success
            assert result.error is not None
            assert "Stream init failed" in result.error

    @pytest.mark.asyncio
    async def test_process_schema_message_table_creation_failure(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test processing SCHEMA message when table creation fails."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock table manager to fail SQL generation
        with patch.object(
            target.table_manager,
            "generate_create_table_sql",
        ) as mock_sql:
            mock_sql.return_value = FlextResult.fail("SQL generation failed")

            schema_message = {
                "type": "SCHEMA",
                "stream": "test_table",
                "schema": {"type": "object", "properties": {"id": {"type": "integer"}}},
            }

            result = await target.process_schema_message(schema_message)
            assert not result.is_success
            assert result.error is not None
            assert "SQL generation failed" in result.error

    @pytest.mark.asyncio
    async def test_process_schema_message_exception_handling(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test SCHEMA message processing exception handling."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock catalog manager to raise exception
        with patch.object(target.catalog_manager, "add_stream") as mock_add:
            mock_add.side_effect = RuntimeError("Unexpected error")

            schema_message = {
                "type": "SCHEMA",
                "stream": "test_table",
                "schema": {"type": "object"},
            }

            result = await target.process_schema_message(schema_message)
            assert not result.is_success
            assert result.error is not None
            assert "SCHEMA processing failed" in result.error

    @pytest.mark.asyncio
    async def test_process_record_message_invalid_type(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test processing message with invalid type for RECORD."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        invalid_message = {
            "type": "SCHEMA",  # Should be RECORD
            "stream": "test_table",
            "record": {"id": 1},
        }

        result = await target.process_record_message(invalid_message)
        assert not result.is_success
        assert result.error is not None
        assert "Not a RECORD message" in result.error

    @pytest.mark.asyncio
    async def test_process_record_message_missing_fields(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test processing RECORD message with missing required fields."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Missing stream
        invalid_message1 = {
            "type": "RECORD",
            "record": {"id": 1},
        }

        result = await target.process_record_message(invalid_message1)
        assert not result.is_success
        assert result.error is not None
        assert "missing stream or record" in result.error

        # Missing record
        invalid_message2 = {
            "type": "RECORD",
            "stream": "test_table",
        }

        result = await target.process_record_message(invalid_message2)
        assert not result.is_success
        assert result.error is not None
        assert "missing stream or record" in result.error

    @pytest.mark.asyncio
    async def test_process_record_message_stream_processing_failure(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test RECORD processing when stream processing fails."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock stream processor to fail
        with patch.object(target.stream_processor, "process_record") as mock_process:
            mock_process.return_value = FlextResult.fail("Record processing failed")

            record_message = {
                "type": "RECORD",
                "stream": "test_table",
                "record": {"id": 1, "name": "Test"},
            }

            result = await target.process_record_message(record_message)
            assert not result.is_success
            assert result.error is not None
            assert "Record processing failed" in result.error

    @pytest.mark.asyncio
    async def test_process_record_message_insertion_failure(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test RECORD processing when record insertion fails."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock _insert_record to fail
        with patch.object(
            target,
            "_insert_record",
            new_callable=AsyncMock,
        ) as mock_insert:
            mock_insert.return_value = FlextResult.fail("Insertion failed")

            record_message = {
                "type": "RECORD",
                "stream": "test_table",
                "record": {"id": 1, "name": "Test"},
            }

            result = await target.process_record_message(record_message)
            assert not result.is_success
            assert result.error is not None
            assert "Insertion failed" in result.error

    def test_process_state_message_invalid_type(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test processing message with invalid type for STATE."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        invalid_message = {
            "type": "RECORD",  # Should be STATE
            "value": {"bookmarks": {}},
        }

        result = target.process_state_message(invalid_message)
        assert not result.is_success
        assert result.error is not None
        assert "Not a STATE message" in result.error

    def test_process_state_message_json_serialization_error(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test STATE message processing with JSON serialization error."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Create message with non-serializable content
        class NonSerializable:
            pass

        invalid_message = {
            "type": "STATE",
            "value": {"bookmarks": {"test": NonSerializable()}},
        }

        result = target.process_state_message(invalid_message)
        assert not result.is_success
        assert result.error is not None
        assert "STATE processing failed" in result.error

    @pytest.mark.asyncio
    async def test_ensure_table_exists_no_client(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test _ensure_table_exists when Oracle client is None."""
        target = SingerTargetOracleWMS(oracle_wms_config)
        target.oracle_client = None  # Simulate uninitialized client

        result = await target._ensure_table_exists(
            "test_table",
            "test_schema",
            "CREATE TABLE test",
        )
        assert not result.is_success
        assert result.error is not None
        assert "Oracle WMS client not initialized" in result.error

    @pytest.mark.asyncio
    async def test_ensure_table_exists_exception(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test _ensure_table_exists exception handling."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock to raise exception
        with patch.object(target, "oracle_client", None):
            # Force an exception by accessing None
            result = await target._ensure_table_exists(
                "test_table",
                "test_schema",
                "CREATE TABLE test",
            )
            assert not result.is_success
            assert result.error is not None
            assert "Oracle WMS client not initialized" in result.error

    @pytest.mark.asyncio
    async def test_insert_record_complex_data_types(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test _insert_record with complex data types."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        complex_record = {
            "id": 123,
            "name": "Test Item",
            "metadata": {"nested": {"value": 42}},
            "tags": ["tag1", "tag2"],
            "active": True,
            "price": 99.99,
            "description": None,
            "created_at": "2023-01-01T12:00:00Z",
        }

        result = await target._insert_record("complex_stream", complex_record)
        # Should succeed with proper parameter preparation
        assert result.is_success

    @pytest.mark.asyncio
    async def test_insert_record_with_underscores(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test _insert_record with fields containing underscores."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        underscore_record = {
            "_sdc_extracted_at": "2023-01-01T12:00:00Z",
            "_sdc_batched_at": "2023-01-01T12:01:00Z",
            "__internal_field": "internal",
            "regular_field": "regular",
        }

        result = await target._insert_record("underscore_stream", underscore_record)
        # Should handle underscore fields properly
        assert result.is_success

    @pytest.mark.asyncio
    async def test_insert_record_exception_handling(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test _insert_record exception handling."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock table manager to raise exception
        with patch.object(
            target.table_manager,
            "generate_table_name",
        ) as mock_table_name:
            mock_table_name.side_effect = RuntimeError("Name generation failed")

            result = await target._insert_record("error_stream", {"id": 1})
            assert not result.is_success
            assert result.error is not None
            assert "Record insertion failed" in result.error

    def test_finalize_with_stream_processor_failure(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test finalize when stream processor stats retrieval fails."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock stream processor to fail stats retrieval
        with patch.object(target.stream_processor, "get_all_stats") as mock_stats:
            mock_stats.return_value = FlextResult.fail("Stats retrieval failed")

            result = target.finalize()
            assert not result.is_success
            assert result.error is not None
            assert "Stats retrieval failed" in result.error

    def test_finalize_with_empty_stats(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test finalize with empty statistics."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock stream processor to return empty stats
        with patch.object(target.stream_processor, "get_all_stats") as mock_stats:
            mock_stats.return_value = FlextResult.ok({})

            result = target.finalize()
            assert result.is_success
            assert result.data is not None

            summary = result.data
            assert summary["total_records_processed"] == 0
            assert summary["total_records_success"] == 0
            assert summary["total_records_failed"] == 0
            assert summary["success_rate"] == 0.0
            assert summary["streams_processed"] == 0

    def test_finalize_exception_handling(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test finalize exception handling."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock stream processor to raise exception
        with patch.object(target.stream_processor, "get_all_stats") as mock_stats:
            mock_stats.side_effect = RuntimeError("Unexpected error")

            result = target.finalize()
            assert not result.is_success
            assert result.error is not None
            assert "Finalization failed" in result.error

    @pytest.mark.asyncio
    async def test_cleanup_with_client_stop_failure(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test cleanup when Oracle client stop fails."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock client stop to fail
        with patch.object(
            target.oracle_client,
            "stop",
            new_callable=AsyncMock,
        ) as mock_stop:
            mock_stop.return_value = FlextResult.fail("Stop failed")

            result = await target.cleanup()
            # Should succeed despite client stop failure (logs warning)
            assert result.is_success

    @pytest.mark.asyncio
    async def test_cleanup_exception_handling(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test cleanup exception handling."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock client stop to raise exception
        with patch.object(
            target.oracle_client,
            "stop",
            new_callable=AsyncMock,
        ) as mock_stop:
            mock_stop.side_effect = RuntimeError("Unexpected error")

            result = await target.cleanup()
            assert not result.is_success
            assert result.error is not None
            assert "Cleanup failed" in result.error

    def test_target_configuration_edge_cases(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test target with various configuration edge cases."""
        # Test with minimal configuration
        minimal_config = {
            "base_url": "https://minimal.wms.example.com",
            "username": "user",
            "password": "pass",
        }

        target = SingerTargetOracleWMS(minimal_config)
        assert target.name == "target-oracle-wms"
        assert target.batch_size == 1000  # Default
        assert target.load_method == "APPEND_ONLY"  # Default
        assert target.table_prefix == ""  # Default

        # Test with maximum configuration
        max_config = {
            **oracle_wms_config,
            "verify_ssl": False,
            "enable_logging": True,
            "enable_plugins": True,
            "plugin_directory": "/custom/plugins",
        }

        target_max = SingerTargetOracleWMS(max_config)
        assert target_max.plugin_enabled is True
        assert target_max.plugin_directory == "/custom/plugins"

    @pytest.mark.asyncio
    async def test_complete_workflow_with_errors(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test complete workflow with mixed success and error scenarios."""
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock Oracle client
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

            # Setup
            setup_result = await target.setup()
            assert setup_result.is_success

            # Process valid SCHEMA
            valid_schema = {
                "type": "SCHEMA",
                "stream": "valid_table",
                "schema": {"type": "object", "properties": {"id": {"type": "integer"}}},
            }
            schema_result = await target.process_schema_message(valid_schema)
            assert schema_result.is_success

            # Process invalid SCHEMA (should fail)
            invalid_schema = {
                "type": "SCHEMA",
                "stream": "",  # Empty stream name
                "schema": {"type": "object"},
            }
            invalid_result = await target.process_schema_message(invalid_schema)
            assert not invalid_result.is_success

            # Process valid RECORD
            valid_record = {
                "type": "RECORD",
                "stream": "valid_table",
                "record": {"id": 123},
            }
            record_result = await target.process_record_message(valid_record)
            assert record_result.is_success

            # Process valid STATE
            valid_state = {
                "type": "STATE",
                "value": {"bookmarks": {"valid_table": {"version": 1}}},
            }
            state_result = target.process_state_message(valid_state)
            assert state_result.is_success

            # Finalize
            finalize_result = target.finalize()
            assert finalize_result.is_success
            assert finalize_result.data is not None

            # Cleanup
            cleanup_result = await target.cleanup()
            assert cleanup_result.is_success
