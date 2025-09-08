"""Benchmark tests for production performance measurement - REAL flext-* API usage.

These benchmarks measure actual performance characteristics using REAL flext-* APIs
following SOLID principles for comprehensive performance validation.



Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import asyncio
import gc
from collections.abc import Callable
from unittest.mock import AsyncMock, MagicMock, patch

from flext_core import FlextTypes

from flext_target_oracle_wms import (
    FlextTargetFactory,
    FlextTargetMonitoringFactory,
    SingerTargetOracleWMS,
    SingerWMSCatalogManager,
    SingerWMSStreamProcessor,
    WMSDataTransformer,
    WMSSchemaMapper,
    WMSTableManager,
    WMSTypeConverter,
    create_oracle_wms_target,
)


class TestFactoryPerformanceBenchmarks:
    """Benchmark factory pattern performance for production optimization."""

    def test_factory_target_creation_benchmark(self, benchmark: Callable) -> None:
        """Benchmark target creation performance with factory patterns."""

        def create_target_with_factory() -> SingerTargetOracleWMS:
            """Create target using factory pattern - measured operation."""
            with patch(
                "flext_target_oracle_wms.factory.SingerTargetOracleWMS",
            ) as mock_target:
                mock_target.return_value = MagicMock()
                result = create_oracle_wms_target(
                    base_url="https://benchmark.wms.oracle.com",
                    username="benchmark_user",
                    password="benchmark_password",
                    preset="production",
                )
                assert result.success
                return result.data

        # Benchmark factory target creation
        result = benchmark(create_target_with_factory)
        assert result is not None

    def test_preset_configuration_benchmark(self, benchmark: Callable) -> None:
        """Benchmark preset configuration application performance."""

        def apply_preset_configuration() -> list[dict]:
            """Apply preset configuration - measured operation."""
            factory = FlextTargetFactory()
            # Simulate multiple preset applications
            configs = []
            for preset_name in ["development", "staging", "production", "testing"]:
                if preset_name in factory.PRESETS:
                    config = {
                        "base_url": f"https://{preset_name}.wms.oracle.com",
                        "username": f"{preset_name}_user",
                        "password": f"{preset_name}_password",
                        **factory.PRESETS[preset_name],
                    }
                    configs.append(config)
            return configs

        # Benchmark preset configuration
        configs = benchmark(apply_preset_configuration)
        assert len(configs) == 4
        assert all("batch_size" in config for config in configs)

    def test_monitoring_factory_benchmark(self, benchmark: Callable) -> None:
        """Benchmark monitoring factory creation performance."""

        def create_monitored_target() -> SingerTargetOracleWMS:
            """Create monitored target - measured operation."""
            with (
                patch(
                    "flext_target_oracle_wms.factory.FlextObservabilityMonitor",
                ),
                patch(
                    "flext_target_oracle_wms.factory.SingerTargetOracleWMS",
                ) as mock_target,
            ):
                mock_target.return_value = MagicMock()
                factory = FlextTargetMonitoringFactory("benchmark_monitor")
                from flext_target_oracle_wms import MonitoredTargetCreationRequest

                request = MonitoredTargetCreationRequest(
                    base_url="https://monitored-benchmark.wms.oracle.com",
                    username="monitor_user",
                    password="monitor_password",
                    preset="production",
                    monitor_name="benchmark_monitor",
                )
                result = factory.create_monitored_target(request)
                assert result.success
                return result.data

        # Benchmark monitored target creation
        result = benchmark(create_monitored_target)
        assert result is not None


class TestPatternsPerformanceBenchmarks:
    """Benchmark WMS patterns performance for optimization."""

    def test_data_transformation_benchmark(self, benchmark: Callable) -> None:
        """Benchmark data transformation performance."""
        # Create test data
        large_record = {f"field_{i}": f"value_{i}" for i in range(100)}
        large_record.update(
            {
                "nested_object": {"inner": {"deep": "value"}},
                "large_array": list(range(50)),
                "json_data": {"complex": {"structure": list(range(20))}},
            },
        )
        transformer = WMSDataTransformer()

        def transform_large_record() -> dict:
            """Transform large record - measured operation."""
            result = transformer.transform_record(large_record, None)
            assert result.success
            return result.data

        # Benchmark transformation
        transformed = benchmark(transform_large_record)
        assert transformed is not None
        assert len(transformed) > 0

    def test_schema_mapping_benchmark(self, benchmark: Callable) -> None:
        """Benchmark schema mapping performance."""
        # Create complex schema
        complex_schema = {
            "type": "object",
            "properties": {
                f"field_{i}": {
                    "type": "string" if i % 2 == 0 else "number",
                    "maxLength": 255 if i % 2 == 0 else None,
                }
                for i in range(50)
            },
        }
        complex_schema["properties"].update(
            {
                "date_field": {"type": "string", "format": "date-time"},
                "nested_object": {
                    "type": "object",
                    "properties": {
                        "inner_field": {"type": "string"},
                    },
                },
                "array_field": {"type": "array", "items": {"type": "string"}},
            },
        )
        mapper = WMSSchemaMapper()

        def map_complex_schema() -> dict:
            """Map complex schema - measured operation."""
            result = mapper.map_singer_schema_to_oracle(complex_schema)
            assert result.success
            return result.data

        # Benchmark schema mapping
        mapped_schema = benchmark(map_complex_schema)
        assert mapped_schema is not None
        assert len(mapped_schema) > 0

    def test_type_conversion_benchmark(self, benchmark: Callable) -> None:
        """Benchmark type conversion performance."""
        converter = WMSTypeConverter()
        # Test data with various types
        test_conversions = (
            [("string", f"test_string_{i}") for i in range(20)]
            + [("integer", i) for i in range(20)]
            + [("number", float(i) + 0.5) for i in range(20)]
            + [("boolean", i % 2 == 0) for i in range(20)]
            + [("object", {"key": f"value_{i}"}) for i in range(10)]
            + [("array", list(range(i, i + 5))) for i in range(10)]
        )

        def convert_all_types() -> FlextTypes.Core.List:
            """Convert all types - measured operation."""
            results = []
            for singer_type, value in test_conversions:
                result = converter.convert_singer_to_oracle(singer_type, value)
                assert result.success
                results.append(result.data)
            return results

        # Benchmark type conversions
        converted = benchmark(convert_all_types)
        assert len(converted) == len(test_conversions)

    def test_table_sql_generation_benchmark(self, benchmark: Callable) -> None:
        """Benchmark SQL generation performance."""
        manager = WMSTableManager()
        # Complex schema for SQL generation
        complex_schema = {
            "type": "object",
            "properties": {
                f"column_{i}": {
                    "type": ["string", "number", "boolean"][i % 3],
                }
                for i in range(30)
            },
        }

        def generate_complex_sql() -> tuple[str, str]:
            """Generate complex SQL - measured operation."""
            create_result = manager.generate_create_table_sql(
                "benchmark_table",
                "benchmark_schema",
                complex_schema,
            )
            assert create_result.success
            columns = [f"column_{i}" for i in range(30)]
            insert_result = manager.generate_insert_sql(
                "benchmark_table",
                "benchmark_schema",
                columns,
            )
            assert insert_result.success
            return (create_result.data, insert_result.data)

        # Benchmark SQL generation
        create_sql, insert_sql = benchmark(generate_complex_sql)
        assert "CREATE TABLE" in create_sql
        assert "INSERT INTO" in insert_sql


class TestStreamPerformanceBenchmarks:
    """Benchmark stream processing performance."""

    def test_stream_processing_benchmark(self, benchmark: Callable) -> None:
        """Benchmark stream processing performance."""
        table_manager = WMSTableManager()
        data_transformer = WMSDataTransformer()
        processor = SingerWMSStreamProcessor(table_manager, data_transformer)
        # Initialize test stream
        test_schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "value": {"type": "number"},
                "active": {"type": "boolean"},
            },
        }
        init_result = processor.initialize_stream("benchmark_stream", test_schema)
        assert init_result.success
        # Generate test records
        test_records = [
            {
                "id": f"record_{i}",
                "name": f"name_{i}",
                "value": float(i * 10),
                "active": i % 2 == 0,
            }
            for i in range(100)
        ]

        def process_batch_records() -> dict:
            """Process batch of records - measured operation."""
            result = processor.process_batch("benchmark_stream", test_records)
            assert result.success
            # Get stats
            stats_result = processor.get_stream_stats("benchmark_stream")
            assert stats_result.success
            return stats_result.data

        # Benchmark batch processing
        stats = benchmark(process_batch_records)
        assert stats is not None
        assert stats.records_processed >= 100


class TestCatalogPerformanceBenchmarks:
    """Benchmark catalog management performance."""

    def test_catalog_operations_benchmark(self, benchmark: Callable) -> None:
        """Benchmark catalog operations performance."""
        manager = SingerWMSCatalogManager()
        # Generate multiple streams for catalog
        test_streams = []
        for i in range(50):
            stream_data = {
                "stream": f"stream_{i}",
                "schema": {
                    "type": "object",
                    "properties": {f"field_{j}": {"type": "string"} for j in range(5)},
                },
                "metadata": [
                    {
                        "breadcrumb": [],
                        "metadata": {
                            "table-key-properties": ["field_0"],
                            "replication-key": "field_1",
                        },
                    },
                ],
            }
            test_streams.append(stream_data)

        def perform_catalog_operations() -> dict:
            """Perform multiple catalog operations - measured operation."""
            # Add streams
            for stream_data in test_streams:
                result = manager.add_stream(
                    stream_data["stream"],
                    stream_data["schema"],
                    stream_data["metadata"],
                )
                assert result.success
            # List streams
            list_result = manager.list_streams()
            assert list_result.success
            # Convert to Singer catalog
            catalog_result = manager.to_singer_catalog()
            assert catalog_result.success
            return catalog_result.data

        # Benchmark catalog operations
        catalog = benchmark(perform_catalog_operations)
        assert catalog is not None
        assert len(catalog.get("streams", [])) == 50


class TestIntegrationPerformanceBenchmarks:
    """Benchmark complete integration workflows."""

    def test_end_to_end_performance_benchmark(self, benchmark: Callable) -> None:
        """Benchmark complete end-to-end workflow performance."""

        async def complete_workflow() -> dict | None:
            """Complete workflow - measured operation."""
            config = {
                "base_url": "https://e2e-benchmark.wms.oracle.com",
                "username": "e2e_user",
                "password": "e2e_password",
                "batch_size": "100",
            }
            with patch("flext_oracle_wms.FlextOracleWmsClient") as mock_client_class:
                # Setup mocked client for performance testing
                mock_client = AsyncMock()
                mock_client_class.return_value = mock_client
                mock_client.start.return_value = MagicMock(success=True)
                mock_client.stop.return_value = MagicMock(success=True)
                mock_client.execute_query.return_value = MagicMock(
                    success=True,
                    data=[],
                )
                target = SingerTargetOracleWMS(config)
                # 1. Setup
                setup_result = await target.setup()
                assert setup_result.success
                # 2. Process schema
                schema_message = {
                    "type": "SCHEMA",
                    "stream": "benchmark_stream",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string"},
                            "value": {"type": "number"},
                            "timestamp": {"type": "string", "format": "date-time"},
                        },
                    },
                    "key_properties": ["id"],
                }
                schema_result = await target.process_schema_message(schema_message)
                assert schema_result.success
                # 3. Process multiple records
                for i in range(20):
                    record_message = {
                        "type": "RECORD",
                        "stream": "benchmark_stream",
                        "record": {
                            "id": f"benchmark_{i}",
                            "value": float(i * 100),
                            "timestamp": "2024-01-15T12:00:00Z",
                        },
                        "time_extracted": "2024-01-15T12:00:00Z",
                    }
                    record_result = await target.process_record_message(record_message)
                    assert record_result.success
                # 4. Finalize
                finalize_result = target.finalize()
                assert finalize_result.success
                # 5. Cleanup
                cleanup_result = await target.cleanup()
                assert cleanup_result.success
                return finalize_result.data

        # Benchmark complete workflow
        # Note: asyncio.run needed for benchmark with async functions

        def sync_wrapper() -> dict | None:
            return asyncio.run(complete_workflow())

        result = benchmark(sync_wrapper)
        assert result is not None


class TestMemoryEfficiencyBenchmarks:
    """Benchmark memory efficiency for large-scale operations."""

    def test_memory_efficient_batch_processing(self, benchmark: Callable) -> None:
        """Benchmark memory usage during large batch processing."""
        table_manager = WMSTableManager()
        data_transformer = WMSDataTransformer()
        processor = SingerWMSStreamProcessor(table_manager, data_transformer)
        # Initialize stream
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "large_data": {"type": "string"},
                "metadata": {"type": "object"},
            },
        }
        init_result = processor.initialize_stream("memory_test", schema)
        assert init_result.success

        def process_large_batch() -> dict:
            """Process large batch efficiently - measured operation."""
            # Force garbage collection before measurement
            gc.collect()
            # Generate large records
            large_records = []
            for i in range(500):  # Smaller than production but sufficient for benchmark
                record = {
                    "id": f"large_record_{i}",
                    "large_data": "x" * 1000,  # 1KB per record
                    "metadata": {
                        "processed_at": "2024-01-15T12:00:00Z",
                        "batch_id": f"batch_{i // 100}",
                        "extra_data": list(range(10)),  # Additional data
                    },
                }
                large_records.append(record)
            # Process in batches to test memory efficiency
            batch_size = 100
            for start_idx in range(0, len(large_records), batch_size):
                batch = large_records[start_idx : start_idx + batch_size]
                result = processor.process_batch("memory_test", batch)
                assert result.success
                # Clear batch to help with memory
                del batch
            # Get final stats
            stats_result = processor.get_stream_stats("memory_test")
            assert stats_result.success
            # Force garbage collection after processing
            gc.collect()
            return stats_result.data

        # Benchmark memory-efficient processing
        stats = benchmark(process_large_batch)
        assert stats.records_processed >= 500
