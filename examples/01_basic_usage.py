"""Basic usage example for flext-target-oracle-wms - PRODUCTION REAL IMPLEMENTATION.

This example demonstrates the basic usage of the Oracle WMS target with REAL
flext-* APIs and production-quality patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import json
from pathlib import Path

from flext_core import FlextLogger, t
from flext_observability import FlextObservabilityMonitor, flext_monitor_function

from flext_target_oracle_wms import SingerTargetOracleWMS

logger = FlextLogger(__name__)
monitor = FlextObservabilityMonitor()


@flext_monitor_function(monitor)
def run_basic_example() -> None:
    """Run basic Oracle WMS target example with REAL configuration."""
    logger.info("Starting basic Oracle WMS target example")
    config: dict[str, t.ContainerValue] = {
        "base_url": "https://example.wms.oracle.com",
        "username": "demo_user",
        "password": "demo_password",
        "batch_size": 1000,
        "table_prefix": "DEMO_",
        "schema_name": "WMS_DEMO",
    }
    target = SingerTargetOracleWMS(config)
    try:
        setup_result = target.setup()
        if not setup_result.is_success:
            logger.error(f"Target setup failed: {setup_result.error}")
            return
        logger.info("Target setup successful")
        schema_message = {
            "type": "SCHEMA",
            "stream": "inventory",
            "schema": {
                "type": "object",
                "properties": {
                    "item_id": {"type": "string"},
                    "item_name": {"type": "string"},
                    "location_id": {"type": "string"},
                    "quantity": {"type": "number"},
                    "unit_cost": {"type": "number"},
                    "last_updated": {"type": "string", "format": "date-time"},
                    "status": {"type": "string"},
                    "warehouse_id": {"type": "string"},
                },
            },
            "key_properties": ["item_id", "location_id"],
            "bookmark_properties": ["last_updated"],
        }
        try:
            target.handle_schema_message(schema_message)
            logger.info("Schema processed successfully")
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ):
            logger.exception("Schema processing failed")
            return
        inventory_records = [
            {
                "item_id": "ITM001",
                "item_name": "Widget A",
                "location_id": "LOC001",
                "quantity": 100.0,
                "unit_cost": 25.5,
                "last_updated": "2024-01-15T10:30:00Z",
                "status": "AVAILABLE",
                "warehouse_id": "WH001",
            },
            {
                "item_id": "ITM002",
                "item_name": "Widget B",
                "location_id": "LOC002",
                "quantity": 75.0,
                "unit_cost": 18.75,
                "last_updated": "2024-01-15T11:00:00Z",
                "status": "AVAILABLE",
                "warehouse_id": "WH001",
            },
            {
                "item_id": "ITM003",
                "item_name": "Widget C",
                "location_id": "LOC001",
                "quantity": 200.0,
                "unit_cost": 12.25,
                "last_updated": "2024-01-15T11:30:00Z",
                "status": "RESERVED",
                "warehouse_id": "WH002",
            },
        ]
        for record_data in inventory_records:
            record_message = {
                "type": "RECORD",
                "stream": "inventory",
                "record": record_data,
                "time_extracted": "2024-01-15T12:00:00Z",
            }
            try:
                target.handle_record_message(record_message)
                logger.debug("Record processed successfully")
            except (
                ValueError,
                TypeError,
                KeyError,
                AttributeError,
                OSError,
                RuntimeError,
                ImportError,
            ):
                logger.exception("Record processing failed")
                continue
            logger.info(f"Processed record for item {record_data['item_id']}")
        state_message = {
            "type": "STATE",
            "value": {
                "bookmarks": {"inventory": {"last_updated": "2024-01-15T11:30:00Z"}}
            },
        }
        try:
            target.handle_state_message(state_message)
            logger.info("State processed successfully")
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ):
            logger.exception("State processing failed")
        cleanup_result = target.cleanup()
        if not cleanup_result.is_success:
            logger.error(f"Target cleanup failed: {cleanup_result.error}")
        else:
            logger.info("Target finalized successfully")
    except (
        ValueError,
        TypeError,
        KeyError,
        AttributeError,
        OSError,
        RuntimeError,
        ImportError,
    ):
        logger.exception("Example execution failed")
        raise
    finally:
        cleanup_result = target.cleanup()
        if not cleanup_result.is_success:
            logger.error(f"Target cleanup failed: {cleanup_result.error}")
        else:
            logger.info("Target cleanup completed")


def run_from_singer_files() -> None:
    """Run target from Singer JSON files - REAL Singer integration."""
    logger.info("Running target from Singer JSON files")
    config_file = Path("config.json")
    if config_file.exists():
        config = json.loads(config_file.read_text(encoding="utf-8"))
    else:
        config: dict[str, t.ContainerValue] = {
            "base_url": "https://example.wms.oracle.com",
            "username": "demo_user",
            "password": "demo_password",
            "batch_size": 500,
            "table_prefix": "SINGER_",
            "schema_name": "WMS_SINGER",
        }
    target = SingerTargetOracleWMS(config)
    singer_messages = [
        '{"type": "SCHEMA", "stream": "products", "schema": {"type": "object", "properties": {"id": {"type": "string"}, "name": {"type": "string"}}}, "key_properties": ["id"]}',
        '{"type": "RECORD", "stream": "products", "record": {"id": "P001", "name": "Product 1"}, "time_extracted": "2024-01-15T12:00:00Z"}',
        '{"type": "RECORD", "stream": "products", "record": {"id": "P002", "name": "Product 2"}, "time_extracted": "2024-01-15T12:01:00Z"}',
        '{"type": "STATE", "value": {"bookmarks": {"products": {"id": "P002"}}}}',
    ]
    try:
        for message_line in singer_messages:
            message = json.loads(message_line)
            if message["type"] == "SCHEMA":
                try:
                    target.handle_schema_message(message)
                    result = None
                except (
                    ValueError,
                    TypeError,
                    KeyError,
                    AttributeError,
                    OSError,
                    RuntimeError,
                    ImportError,
                ):
                    logger.exception("Schema processing failed")
                    continue
            elif message["type"] == "RECORD":
                try:
                    target.handle_record_message(message)
                    result = None
                except (
                    ValueError,
                    TypeError,
                    KeyError,
                    AttributeError,
                    OSError,
                    RuntimeError,
                    ImportError,
                ):
                    logger.exception("Record processing failed")
                    continue
            elif message["type"] == "STATE":
                try:
                    target.handle_state_message(message)
                    result = None
                except (
                    ValueError,
                    TypeError,
                    KeyError,
                    AttributeError,
                    OSError,
                    RuntimeError,
                    ImportError,
                ):
                    logger.exception("State processing failed")
                    continue
            else:
                logger.warning(f"Unknown message type: {message['type']}")
                continue
            if result is not None:
                logger.error("Message processing failed: %s", result)
            else:
                logger.debug(f"Processed {message['type']} message successfully")
    except (
        ValueError,
        TypeError,
        KeyError,
        AttributeError,
        OSError,
        RuntimeError,
        ImportError,
    ):
        logger.exception("Singer file processing failed")
        raise
    finally:
        target.cleanup()


if __name__ == "__main__":
    "Run the basic usage example."
    run_basic_example()
    run_from_singer_files()
