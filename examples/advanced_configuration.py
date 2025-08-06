#!/usr/bin/env python3
"""Advanced configuration example - PRODUCTION REAL implementation with flext-* patterns.

This example shows advanced configuration options, custom patterns, and
real-world scenarios using REAL flext-* APIs.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import asyncio
import os
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any, cast

from flext_core import FlextResult, get_logger
from flext_observability import FlextObservabilityMonitor, flext_monitor_function

from flext_target_oracle_wms import (
    SingerTargetOracleWMS,
    WMSDataTransformer,
    WMSSchemaMapper,
    WMSTableManager,
    WMSTypeConverter,
)

if TYPE_CHECKING:
    from collections.abc import Coroutine

logger = get_logger(__name__)
monitor = FlextObservabilityMonitor()


class CustomWMSTypeConverter(WMSTypeConverter):
    """Custom type converter with business-specific transformations."""

    def convert_singer_to_oracle(
        self,
        singer_type: str,
        value: object,
    ) -> FlextResult[Any]:
        """Custom conversion with business rules."""
        # Handle custom business types
        if singer_type == "business_date":
            # Convert business date format to Oracle format
            if isinstance(value, str) and value:
                # Business logic: convert YYYY-MM-DD to DD-MON-YYYY
                try:
                    dt = datetime.strptime(value, "%Y-%m-%d").replace(tzinfo=UTC)
                    oracle_date = dt.strftime("%d-%b-%Y").upper()
                    return FlextResult.ok(oracle_date)
                except ValueError:
                    return FlextResult.fail(f"Invalid business date format: {value}")

        # Handle custom currency with precision
        elif singer_type == "business_currency":
            if isinstance(value, (int, float)) and value is not None:
                # Round to 2 decimal places for currency
                return FlextResult.ok(round(float(value), 2))

        # Handle custom status enums
        elif singer_type == "wms_status" and isinstance(value, str):
            # Map business status to WMS codes
            status_mapping = {
                "active": "A",
                "inactive": "I",
                "pending": "P",
                "suspended": "S",
                "archived": "Z",
            }
            mapped_status = status_mapping.get(value.lower(), value)
            return FlextResult.ok(mapped_status)

        # Delegate to parent for standard types - ensure proper typing
        parent_result = super().convert_singer_to_oracle(singer_type, value)
        # Type cast to ensure MyPy understands this returns FlextResult[Any]

        return cast("FlextResult[Any]", parent_result)


class CustomWMSDataTransformer(WMSDataTransformer):
    """Custom data transformer with business-specific logic."""

    def __init__(self) -> None:
        """Initialize with custom type converter."""
        super().__init__(CustomWMSTypeConverter())

    def transform_record(
        self,
        record: dict[str, object],
        schema: dict[str, object] | None = None,
    ) -> FlextResult[dict[str, object]]:
        """Transform record with business validations."""
        # Apply standard transformation first
        base_result = super().transform_record(record, schema)
        if not base_result.success:
            return base_result

        transformed = base_result.data
        if transformed is None:
            return FlextResult.fail("Base transformation returned None")

        # Apply business-specific transformations
        try:
            # Add audit fields
            transformed["_PROCESSED_AT"] = "SYSTIMESTAMP"
            transformed["_PROCESSED_BY"] = "FLEXT_TARGET"

            # Apply business key formatting
            if "ITEM_ID" in transformed:
                item_id = str(transformed["ITEM_ID"]).upper().strip()
                # Ensure item ID follows business format (3 letters + 6 digits)
                if (
                    len(item_id) >= 9
                    and item_id[:3].isalpha()
                    and item_id[3:9].isdigit()
                ):
                    transformed["ITEM_ID"] = item_id[:9]  # Truncate to standard length

            # Validate required business fields
            required_fields = ["ITEM_ID", "LOCATION_ID"]
            for field in required_fields:
                if field not in transformed or not transformed[field]:
                    return FlextResult.fail(f"Missing required business field: {field}")

            return FlextResult.ok(transformed)

        except Exception as e:
            return FlextResult.fail(f"Business transformation failed: {e}")


@flext_monitor_function(monitor)
async def run_advanced_configuration_example() -> None:
    """Demonstrate advanced configuration with custom components."""
    logger.info("Starting advanced configuration example")

    # Advanced configuration with all options
    config = {
        # Connection settings
        "base_url": os.getenv("WMS_BASE_URL", "https://advanced.wms.oracle.com"),
        "username": os.getenv("WMS_USERNAME", "advanced_user"),
        "password": os.getenv("WMS_PASSWORD", "secure_password"),
        "environment": os.getenv("WMS_ENV", "production"),
        # Performance tuning
        "batch_size": 2000,
        "connection_timeout": 30,
        "request_timeout": 120,
        "max_retries": 3,
        "retry_delay": 5,
        # Schema configuration
        "table_prefix": "ADV_",
        "schema_name": "WMS_ADVANCED",
        "create_schema": True,
        "drop_existing_tables": False,
        # Data handling
        "null_value_handling": "empty_string",
        "date_format": "YYYY-MM-DD HH24:MI:SS",
        "numeric_precision": 10,
        "numeric_scale": 2,
        # Advanced features
        "enable_compression": True,
        "enable_encryption": True,
        "audit_trail": True,
        "conflict_resolution": "last_write_wins",
        # Custom transformations
        "custom_type_mappings": {
            "business_date": "DATE",
            "business_currency": "NUMBER(10,2)",
            "wms_status": "VARCHAR2(1)",
        },
    }

    # Create target with custom transformer
    target = SingerTargetOracleWMS(config)

    # Replace default transformer with custom one
    target.data_transformer = CustomWMSDataTransformer()

    try:
        # Setup with advanced configuration
        setup_result = await target.setup()
        if not setup_result.success:
            logger.error(f"Advanced setup failed: {setup_result.error}")
            return

        logger.info("Advanced target setup completed")

        # Process complex schema with custom types
        advanced_schema = {
            "type": "SCHEMA",
            "stream": "advanced_inventory",
            "schema": {
                "type": "object",
                "properties": {
                    # Standard fields
                    "item_id": {"type": "string"},
                    "item_name": {"type": "string"},
                    "location_id": {"type": "string"},
                    # Business-specific types
                    "effective_date": {"type": "business_date"},
                    "unit_cost": {"type": "business_currency"},
                    "status": {"type": "wms_status"},
                    # Complex nested data
                    "attributes": {
                        "type": "object",
                        "properties": {
                            "weight": {"type": "number"},
                            "dimensions": {
                                "type": "object",
                                "properties": {
                                    "length": {"type": "number"},
                                    "width": {"type": "number"},
                                    "height": {"type": "number"},
                                },
                            },
                            "tags": {"type": "array"},
                        },
                    },
                    # Audit fields
                    "created_by": {"type": "string"},
                    "created_at": {"type": "string", "format": "date-time"},
                    "modified_by": {"type": "string"},
                    "modified_at": {"type": "string", "format": "date-time"},
                    "version": {"type": "integer"},
                },
            },
            "key_properties": ["item_id", "location_id"],
            "bookmark_properties": ["modified_at"],
        }

        schema_result = await target.process_schema_message(advanced_schema)
        if not schema_result.success:
            logger.error(f"Advanced schema failed: {schema_result.error}")
            return

        logger.info("Advanced schema processed")

        # Process complex records
        complex_records = [
            {
                "item_id": "ABC123456",
                "item_name": "Advanced Widget Pro",
                "location_id": "ZONE_A_001",
                "effective_date": "2024-01-15",
                "unit_cost": 125.99,
                "status": "active",
                "attributes": {
                    "weight": 2.5,
                    "dimensions": {
                        "length": 10.0,
                        "width": 5.0,
                        "height": 3.0,
                    },
                    "tags": ["electronic", "fragile", "high-value"],
                },
                "created_by": "system",
                "created_at": "2024-01-15T08:00:00Z",
                "modified_by": "user123",
                "modified_at": "2024-01-15T10:30:00Z",
                "version": 1,
            },
            {
                "item_id": "DEF789012",
                "item_name": "Standard Component",
                "location_id": "ZONE_B_002",
                "effective_date": "2024-01-16",
                "unit_cost": 45.00,
                "status": "pending",
                "attributes": {
                    "weight": 0.8,
                    "dimensions": {
                        "length": 5.0,
                        "width": 3.0,
                        "height": 1.0,
                    },
                    "tags": ["standard", "bulk"],
                },
                "created_by": "import_batch",
                "created_at": "2024-01-16T09:15:00Z",
                "modified_by": "import_batch",
                "modified_at": "2024-01-16T09:15:00Z",
                "version": 1,
            },
        ]

        # Process with custom transformations
        for record_data in complex_records:
            record_message = {
                "type": "RECORD",
                "stream": "advanced_inventory",
                "record": record_data,
                "time_extracted": "2024-01-16T12:00:00Z",
            }

            record_result = await target.process_record_message(record_message)
            if not record_result.success:
                logger.error(f"Complex record failed: {record_result.error}")
                continue

            logger.info(f"Processed complex record: {record_data['item_id']}")

        # Demonstrate error handling with invalid data
        invalid_record = {
            "type": "RECORD",
            "stream": "advanced_inventory",
            "record": {
                "item_id": "",  # Invalid: empty
                "item_name": "Invalid Item",
                "effective_date": "invalid-date",  # Invalid format
                "status": "unknown_status",  # Invalid status
            },
        }

        invalid_result = await target.process_record_message(invalid_record)
        if not invalid_result.success:
            logger.info(f"Invalid record correctly rejected: {invalid_result.error}")
        else:
            logger.warning("Invalid record was unexpectedly accepted")

        # Finalize with statistics
        final_result = target.finalize()
        if final_result.success and final_result.data:
            stats = final_result.data
            logger.info(
                f"Processing completed - Records: {stats.get('total_records', 0)}, "
                f"Errors: {stats.get('total_errors', 0)}",
            )

    except Exception:
        logger.exception("Advanced configuration example failed")
        raise
    finally:
        await target.cleanup()


@flext_monitor_function(monitor)
async def demonstrate_custom_components() -> None:
    """Demonstrate usage of custom WMS components."""
    logger.info("Demonstrating custom WMS components")

    # Custom type converter usage
    custom_converter = CustomWMSTypeConverter()

    # Test business date conversion
    date_result = custom_converter.convert_singer_to_oracle(
        "business_date",
        "2024-01-15",
    )
    logger.info(f"Business date conversion: {date_result.data}")

    # Test currency conversion
    currency_result = custom_converter.convert_singer_to_oracle(
        "business_currency",
        123.456789,
    )
    logger.info(f"Currency conversion: {currency_result.data}")

    # Test status mapping
    status_result = custom_converter.convert_singer_to_oracle("wms_status", "active")
    logger.info(f"Status mapping: {status_result.data}")

    # Custom table manager
    table_manager = WMSTableManager()

    # Generate table with custom prefix
    table_name = table_manager.generate_table_name("inventory", "CUSTOM")
    logger.info(f"Generated table name: {table_name}")

    # Custom schema mapper
    schema_mapper = WMSSchemaMapper()

    test_schema: dict[str, object] = {
        "properties": {
            "business_date": {"type": "business_date"},
            "amount": {"type": "business_currency"},
            "status": {"type": "wms_status"},
        },
    }

    mapping_result = schema_mapper.map_singer_schema_to_oracle(test_schema)
    if mapping_result.success:
        logger.info(f"Schema mapping: {mapping_result.data}")


if __name__ == "__main__":
    """Run advanced configuration examples."""

    asyncio.run(cast("Coroutine[Any, Any, None]", run_advanced_configuration_example()))
    asyncio.run(cast("Coroutine[Any, Any, None]", demonstrate_custom_components()))
