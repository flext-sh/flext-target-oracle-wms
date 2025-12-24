"""Integration tests for Oracle WMS target using REAL flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from unittest.mock import Mock, patch

import pytest
from flext import FlextResult

from flext_target_oracle_wms import SingerTargetOracleWMS

# Constants from REAL Oracle WMS requirements
EXPECTED_BULK_SIZE = 2


@pytest.mark.integration
@pytest.mark.oracle
class TestOracleWMSIntegration:
    """Integration tests using REAL flext-oracle-wms client patterns."""

    @pytest.fixture
    def oracle_wms_config(self) -> dict[str, object]:
        """Oracle WMS configuration using REAL API parameters."""
        return {
            "base_url": "https://test.wms.ocs.oraclecloud.com",
            "username": "test_user",
            "password": "test_password",
            "environment": "test",
            "timeout": 30.0,
            "max_retries": 3,
            "batch_size": EXPECTED_BULK_SIZE,
            "load_method": "APPEND_ONLY",
            "table_prefix": "TEST_",
            "default_target_schema": "WMS_TEST",
        }

    def test_singer_target_setup(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test SingerTarget can setup Oracle WMS client using REAL APIs."""
        # DRY: Use REAL implementation
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock the oracle_client.start() to return success using patch
        with patch.object(
            target.oracle_client,
            "start",
            new_callable=Mock,
        ) as mock_start:
            mock_start.return_value = FlextResult[None].ok(None)

            # Test setup using REAL flext-core patterns
            setup_result = target.setup()
            assert setup_result.success
            assert setup_result.error is None

    def test_schema_message_processing(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test Singer SCHEMA message processing using REAL flext-core patterns."""
        # DRY: Use REAL implementation
        target = SingerTargetOracleWMS(oracle_wms_config)

        # REAL Singer SCHEMA message format
        schema_message = {
            "type": "SCHEMA",
            "stream": "test_table",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "created_at": {"type": "string", "format": "date-time"},
                    "is_active": {"type": "boolean"},
                },
            },
            "key_properties": ["id"],
        }

        # Test SCHEMA message processing using REAL flext-core patterns
        schema_result = target.process_schema_message(schema_message)
        assert schema_result.success
        assert schema_result.error is None

    def test_record_message_processing(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test Singer RECORD message processing using REAL flext-core patterns."""
        # DRY: Use REAL implementation
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Initialize stream first (required before processing records)
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "created_at": {"type": "string", "format": "date-time"},
                "is_active": {"type": "boolean"},
            },
        }
        target.catalog_manager.add_stream("test_table", schema)
        target.stream_processor.initialize_stream("test_table", schema)

        # REAL Singer RECORD message format
        record_message = {
            "type": "RECORD",
            "stream": "test_table",
            "record": {
                "id": 1,
                "name": "John Doe",
                "created_at": "2023-01-01T12:00:00Z",
                "is_active": True,
            },
            "time_extracted": "2023-01-01T12:00:00Z",
        }

        # Test RECORD message processing using REAL flext-core patterns
        record_result = target.process_record_message(record_message)
        assert record_result.success
        assert record_result.error is None

    def test_state_message_processing(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test Singer STATE message processing using REAL flext-core patterns."""
        # DRY: Use REAL implementation
        target = SingerTargetOracleWMS(oracle_wms_config)

        # REAL Singer STATE message format
        state_message = {
            "type": "STATE",
            "value": {
                "bookmarks": {
                    "test_table": {
                        "last_updated": "2023-01-01T12:00:00Z",
                        "version": 1,
                    },
                },
            },
        }

        # Test STATE message processing using REAL flext-core patterns
        state_result = target.process_state_message(state_message)
        assert state_result.success
        assert state_result.error is None

    def test_target_cleanup(
        self,
        oracle_wms_config: dict[str, object],
    ) -> None:
        """Test Oracle WMS Target cleanup using REAL flext-core patterns."""
        # DRY: Use REAL implementation
        target = SingerTargetOracleWMS(oracle_wms_config)

        # Mock dependencies for testing using patch

        with (
            patch.object(
                target.oracle_client,
                "start",
                new_callable=Mock,
            ) as mock_start,
            patch.object(
                target.oracle_client,
                "stop",
                new_callable=Mock,
            ) as mock_stop,
        ):
            mock_start.return_value = FlextResult[None].ok(None)
            mock_stop.return_value = FlextResult[None].ok(None)

            # Test setup and cleanup cycle
            target.setup()
            cleanup_result = target.cleanup()

            assert cleanup_result.success
            assert cleanup_result.error is None
