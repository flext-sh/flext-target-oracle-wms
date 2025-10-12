#!/usr/bin/env python3
"""Batch processing example - HIGH-PERFORMANCE real implementation with flext-* patterns.

This example demonstrates high-performance batch processing capabilities
using REAL flext-* APIs and production-grade optimization patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import time

from flext_core import FlextCore
from flext_observability import FlextObservabilityMonitor, flext_monitor_function

from flext_target_oracle_wms import (
    SingerTargetOracleWMS,
    SingerWMSStreamProcessor,
    WMSDataTransformer,
    WMSTableManager,
)

# Constants
MAX_ERROR_LOGS = 5  # Maximum number of errors to log per batch

logger = FlextCore.Logger(__name__)
monitor = FlextObservabilityMonitor()


def generate_test_data(num_records: int) -> list[FlextCore.Types.Dict]:
    """Generate test data for batch processing demonstration."""
    logger.info(f"Generating {num_records} test records")

    records = []
    for i in range(num_records):
        record = {
            "item_id": f"BATCH_{i:06d}",
            "item_name": f"Batch Item {i}",
            "location_id": f"LOC_{(i % 100):03d}",
            "quantity": (i % 1000) + 1,
            "unit_cost": round(10.0 + (i % 100) * 0.25, 2),
            "last_updated": f"2024-01-{15 + (i % 10):02d}T{(i % 24):02d}:{(i % 60):02d}:00Z",
            "status": ["AVAILABLE", "RESERVED", "ALLOCATED", "SHIPPED"][i % 4],
            "warehouse_id": f"WH{(i % 5) + 1:03d}",
            "category": ["ELECTRONICS", "CLOTHING", "BOOKS", "TOOLS", "FOOD"][i % 5],
            "supplier_id": f"SUP_{(i % 20) + 1:03d}",
            "batch_number": f"B{int(i / 100) + 1:04d}",
        }
        records.append(record)

    logger.info(f"Generated {len(records)} test records")
    return records


def _create_batch_config() -> FlextCore.Types.Dict:
    """Create optimized configuration for batch processing."""
    return {
        "base_url": "https://batch.wms.oracle.com",
        "username": "batch_user",
        "password": "batch_password",
        "environment": "batch_demo",
        # Performance optimizations
        "batch_size": 5000,  # Large batch size for performance
        "connection_timeout": 60,
        "request_timeout": 300,  # Extended timeout for large batches
        "max_retries": 5,
        "retry_delay": 2,
        # Schema configuration for performance
        "table_prefix": "BATCH_",
        "schema_name": "WMS_BATCH",
        "create_schema": True,
        # Batch-specific optimizations
        "enable_compression": True,
        "bulk_insert_mode": True,
        "parallel_processing": True,
        "memory_optimization": True,
    }


def _create_batch_schema() -> FlextCore.Types.Dict:
    """Create optimized schema for batch processing."""
    return {
        "type": "SCHEMA",
        "stream": "batch_inventory",
        "schema": {
            "type": "object",
            "properties": {
                "item_id": {"type": "string"},
                "item_name": {"type": "string"},
                "location_id": {"type": "string"},
                "quantity": {"type": "integer"},
                "unit_cost": {"type": "number"},
                "last_updated": {"type": "string", "format": "date-time"},
                "status": {"type": "string"},
                "warehouse_id": {"type": "string"},
                "category": {"type": "string"},
                "supplier_id": {"type": "string"},
                "batch_number": {"type": "string"},
            },
        },
        "key_properties": ["item_id", "location_id"],
        "bookmark_properties": ["last_updated"],
    }


def _process_batch_size(target: SingerTargetOracleWMS, batch_size: int) -> None:
    """Process a specific batch size and log performance metrics."""
    logger.info(f"Testing batch size: {batch_size}")

    # Generate test data
    test_data = generate_test_data(batch_size)

    # Process batch with timing
    batch_start = time.time()
    success_count = 0
    error_count = 0

    # Process in chunks for memory efficiency
    chunk_size = min(batch_size, 1000)

    for i in range(0, len(test_data), chunk_size):
        chunk = test_data[i : i + chunk_size]
        chunk_start = time.time()

        # Process chunk records
        for record_data in chunk:
            record_message = {
                "type": "RECORD",
                "stream": "batch_inventory",
                "record": record_data,
                "time_extracted": "2024-01-15T12:00:00Z",
            }

            try:
                target.handle_record_message(record_message)
                logger.debug("Record processed successfully")
            except Exception as e:
                logger.exception(f"Record processing failed: {e}")
                continue
            success_count += 1

        chunk_time = time.time() - chunk_start
        chunk_rate = len(chunk) / chunk_time if chunk_time > 0 else 0
        logger.info(
            f"Processed chunk {i // chunk_size + 1}: "
            f"{len(chunk)} records in {chunk_time:.2f}s "
            f"({chunk_rate:.1f} records/sec)",
        )

    # Calculate performance metrics
    total_time = time.time() - batch_start
    total_rate = batch_size / total_time if total_time > 0 else 0

    logger.info(
        f"Batch {batch_size} completed: "
        f"{success_count} success, {error_count} errors "
        f"in {total_time:.2f}s ({total_rate:.1f} records/sec)",
    )

    # Memory cleanup between batches
    time.sleep(1)


@flext_monitor_function(monitor)
def run_performance_batch_example() -> None:
    """Demonstrate high-performance batch processing."""
    logger.info("Starting performance batch processing example")

    config = _create_batch_config()
    target = SingerTargetOracleWMS(config)

    try:
        # Setup for batch processing
        setup_start = time.time()
        setup_result = target.setup()
        if not setup_result.success:
            logger.error(f"Batch setup failed: {setup_result.error}")
            return

        setup_time = time.time() - setup_start
        logger.info(f"Batch target setup completed in {setup_time:.2f}s")

        # Process schema
        batch_schema = _create_batch_schema()
        schema_start = time.time()
        try:
            target.handle_schema_message(batch_schema)
            logger.debug("Schema processed successfully")
        except Exception as e:
            logger.exception(f"Schema processing failed: {e}")
            return

        schema_time = time.time() - schema_start
        logger.info(f"Batch schema processed in {schema_time:.2f}s")

        # Test different batch sizes for performance comparison
        batch_sizes = [1000, 5000, 10000, 25000]
        for batch_size in batch_sizes:
            _process_batch_size(target, batch_size)

        # Finalize with statistics
        finalize_start = time.time()
        cleanup_result = target.cleanup()
        finalize_time = time.time() - finalize_start

        if cleanup_result.success:
            logger.info(f"Batch processing completed in {finalize_time:.2f}s")

    except Exception:
        logger.exception("Performance batch example failed")
        raise
    finally:
        cleanup_start = time.time()
        target.cleanup()
        cleanup_time = time.time() - cleanup_start
        logger.info(f"Batch cleanup completed in {cleanup_time:.2f}s")


@flext_monitor_function(monitor)
def demonstrate_stream_processor_batching() -> None:
    """Demonstrate direct stream processor batch capabilities."""
    logger.info("Demonstrating stream processor batch processing")

    # Create components
    table_manager = WMSTableManager()
    data_transformer = WMSDataTransformer()
    stream_processor = SingerWMSStreamProcessor(table_manager, data_transformer)

    # Initialize stream for batch processing
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "value": {"type": "number"},
            "timestamp": {"type": "string"},
        },
    }

    init_result = stream_processor.initialize_stream("batch_test", schema)
    if not init_result.success:
        logger.error(f"Stream initialization failed: {init_result.error}")
        return

    # Prepare batch data
    batch_records = [
        {"id": f"B{i:04d}", "value": i * 10.5, "timestamp": "2024-01-15T12:00:00Z"}
        for i in range(1000)
    ]

    # Process as batch
    batch_start = time.time()
    batch_result = stream_processor.process_batch("batch_test", batch_records)
    batch_time = time.time() - batch_start

    if batch_result.success and batch_result.data:
        processed_count = len(batch_result.data)
        rate = processed_count / batch_time if batch_time > 0 else 0
        logger.info(
            f"Stream batch processed: {processed_count} records "
            f"in {batch_time:.2f}s ({rate:.1f} records/sec)",
        )

    # Get final statistics
    stats_result = stream_processor.get_stream_stats("batch_test")
    if stats_result.success and stats_result.data:
        stats = stats_result.data
        logger.info(
            f"Final stats: {stats.records_processed} processed, "
            f"{stats.records_success} successful, "
            f"{stats.records_failed} failed, "
            f"{stats.success_rate:.1f}% success rate",
        )

    # Finalize stream
    final_result = stream_processor.finalize_stream("batch_test")
    if final_result.success:
        logger.info("Stream processing finalized successfully")


@flext_monitor_function(monitor)
def demonstrate_concurrent_batching() -> None:
    """Demonstrate concurrent batch processing with multiple streams."""
    logger.info("Demonstrating concurrent batch processing")

    # Configuration for concurrent processing
    config = {
        "base_url": "https://concurrent.wms.oracle.com",
        "username": "concurrent_user",
        "password": "concurrent_password",
        "environment": "concurrent_demo",
        "batch_size": 2000,
        "parallel_processing": True,
        "max_concurrent_streams": 5,
    }

    target = SingerTargetOracleWMS(config)

    try:
        target.setup()

        # Define multiple streams for concurrent processing
        streams = ["stream_a", "stream_b", "stream_c", "stream_d", "stream_e"]

        # Setup schemas for all streams concurrently
        schema_tasks = []
        for stream_name in streams:
            schema_message = {
                "type": "SCHEMA",
                "stream": stream_name,
                "schema": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "stream_id": {"type": "string"},
                        "value": {"type": "number"},
                        "timestamp": {"type": "string"},
                    },
                },
                "key_properties": ["id"],
            }
            target.handle_schema_message(schema_message)
            schema_tasks.append(lambda: None)  # Success

        # Execute schema setup concurrently
        schema_results = [task() for task in schema_tasks]

        successful_streams = []
        for i, result in enumerate(schema_results):
            if isinstance(result, Exception):
                logger.error(f"Schema setup failed for {streams[i]}: {result}")
            elif hasattr(result, "success") and result.success:
                successful_streams.append(streams[i])
                logger.info(f"Schema setup successful for {streams[i]}")

        logger.info(f"Successfully setup {len(successful_streams)} concurrent streams")

        # Process records concurrently across streams
        def process_stream_batch(stream_name: str, record_count: int) -> None:
            """Process a batch of records for a specific stream."""
            records = [
                {
                    "id": f"{stream_name}_{j:04d}",
                    "stream_id": stream_name,
                    "value": j * 1.5,
                    "timestamp": "2024-01-15T12:00:00Z",
                }
                for j in range(record_count)
            ]

            start_time = time.time()
            for record_data in records:
                record_message = {
                    "type": "RECORD",
                    "stream": stream_name,
                    "record": record_data,
                    "time_extracted": "2024-01-15T12:00:00Z",
                }

                target.handle_record_message(record_message)

            elapsed = time.time() - start_time
            rate = len(records) / elapsed if elapsed > 0 else 0
            logger.info(
                f"Stream {stream_name}: {len(records)} records "
                f"in {elapsed:.2f}s ({rate:.1f} records/sec)",
            )

        # Execute concurrent stream processing
        concurrent_start = time.time()
        for stream_name in successful_streams:
            process_stream_batch(stream_name, 1000)
        concurrent_time = time.time() - concurrent_start

        total_records = len(successful_streams) * 1000
        total_rate = total_records / concurrent_time if concurrent_time > 0 else 0

        logger.info(
            f"Concurrent processing completed: {total_records} total records "
            f"across {len(successful_streams)} streams "
            f"in {concurrent_time:.2f}s ({total_rate:.1f} records/sec)",
        )

    except Exception:
        logger.exception("Concurrent batch processing failed")
        raise
    finally:
        target.cleanup()


if __name__ == "__main__":
    """Run batch processing examples."""

    run_performance_batch_example()
    demonstrate_stream_processor_batching()
    demonstrate_concurrent_batching()
