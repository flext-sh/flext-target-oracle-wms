"""Advanced configuration example - PRODUCTION REAL implementation with flext-* patterns.

This example shows advanced configuration options, custom patterns, and
real-world scenarios using REAL flext-* APIs.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import os
from collections.abc import Mapping
from datetime import UTC, datetime

from flext_core import FlextLogger, FlextResult, t
from flext_observability import FlextObservabilityMonitor, flext_monitor_function

from flext_target_oracle_wms import (
    SingerTargetOracleWMS,
    WMSDataTransformer,
    WMSSchemaMapper,
    WMSTableManager,
    WMSTypeConverter,
)

logger = FlextLogger(__name__)
monitor = FlextObservabilityMonitor()


class CustomWMSTypeConverter(WMSTypeConverter):
    """Custom type converter with business-specific transformations."""

    def convert_singer_to_oracle(
        self, singer_type: str, value: object
    ) -> FlextResult[object]:
        """Custom conversion with business rules."""
        if singer_type == "business_date":
            if isinstance(value, str) and value:
                try:
                    dt = datetime.strptime(value, "%Y-%m-%d").replace(tzinfo=UTC)
                    oracle_date = dt.strftime("%d-%b-%Y").upper()
                    return FlextResult[bool].ok(oracle_date)
                except ValueError:
                    return FlextResult[bool].fail(
                        f"Invalid business date format: {value}"
                    )
        elif singer_type == "business_currency":
            if isinstance(value, (int, float)) and value is not None:
                return FlextResult[bool].ok(round(float(value), 2))
        elif singer_type == "wms_status" and isinstance(value, str):
            status_mapping = {
                "active": "A",
                "inactive": "I",
                "pending": "P",
                "suspended": "S",
                "archived": "Z",
            }
            mapped_status = status_mapping.get(value.lower(), value)
            return FlextResult[bool].ok(mapped_status)
        parent_result: FlextResult[object] = super().convert_singer_to_oracle(
            singer_type, value
        )
        return parent_result


class CustomWMSDataTransformer(WMSDataTransformer):
    """Custom data transformer with business-specific logic."""

    def __init__(self) -> None:
        """Initialize with custom type converter."""
        super().__init__(CustomWMSTypeConverter())

    def transform_record(
        self,
        record_message: Mapping[str, t.ContainerValue],
        schema_message: Mapping[str, t.ContainerValue] | None = None,
    ) -> FlextResult[object]:
        """Transform record with business validations."""
        base_result = super().transform_record(record_message, schema_message)
        if not base_result.is_success:
            return base_result
        transformed = base_result.data
        if transformed is None:
            return FlextResult[bool].fail("Base transformation returned None")
        try:
            transformed["_PROCESSED_AT"] = "SYSTIMESTAMP"
            transformed["_PROCESSED_BY"] = "FLEXT_TARGET"
            item_id_min_length = 9
            item_prefix_length = 3
            item_number_end = 9
            if "ITEM_ID" in transformed:
                item_id = str(transformed["ITEM_ID"]).upper().strip()
                if (
                    len(item_id) >= item_id_min_length
                    and item_id[:item_prefix_length].isalpha()
                    and item_id[item_prefix_length:item_number_end].isdigit()
                ):
                    transformed["ITEM_ID"] = item_id[:9]
            required_fields = ["ITEM_ID", "LOCATION_ID"]
            for field in required_fields:
                if field not in transformed or not transformed[field]:
                    return FlextResult[bool].fail(
                        f"Missing required business field: {field}"
                    )
            return FlextResult[bool].ok(transformed)
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            return FlextResult[bool].fail(f"Business transformation failed: {e}")


@flext_monitor_function(monitor)
def run_advanced_configuration_example() -> None:
    """Demonstrate advanced configuration with custom components."""
    logger.info("Starting advanced configuration example")
    config = {
        "base_url": os.getenv("WMS_BASE_URL", "https://advanced.wms.oracle.com"),
        "username": os.getenv("WMS_USERNAME", "advanced_user"),
        "password": os.getenv("WMS_PASSWORD", "secure_password"),
        "environment": os.getenv("WMS_ENV", "production"),
        "batch_size": 2000,
        "connection_timeout": 30,
        "request_timeout": 120,
        "max_retries": 3,
        "retry_delay": 5,
        "table_prefix": "ADV_",
        "schema_name": "WMS_ADVANCED",
        "create_schema": True,
        "drop_existing_tables": False,
        "null_value_handling": "empty_string",
        "date_format": "YYYY-MM-DD HH24:MI:SS",
        "numeric_precision": 10,
        "numeric_scale": 2,
        "enable_compression": True,
        "enable_encryption": True,
        "audit_trail": True,
        "conflict_resolution": "last_write_wins",
        "custom_type_mappings": {
            "business_date": "DATE",
            "business_currency": "NUMBER(10,2)",
            "wms_status": "VARCHAR2(1)",
        },
    }
    target = SingerTargetOracleWMS(config)
    target.data_transformer = CustomWMSDataTransformer()
    try:
        setup_result = target.setup()
        if not setup_result.is_success:
            logger.error(f"Advanced setup failed: {setup_result.error}")
            return
        logger.info("Advanced target setup completed")
        advanced_schema = {
            "type": "SCHEMA",
            "stream": "advanced_inventory",
            "schema": {
                "type": "object",
                "properties": {
                    "item_id": {"type": "string"},
                    "item_name": {"type": "string"},
                    "location_id": {"type": "string"},
                    "effective_date": {"type": "business_date"},
                    "unit_cost": {"type": "business_currency"},
                    "status": {"type": "wms_status"},
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
        schema_result = target.process_schema_message(advanced_schema)
        if not schema_result.is_success:
            logger.error(f"Advanced schema failed: {schema_result.error}")
            return
        logger.info("Advanced schema processed")
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
                    "dimensions": {"length": 10.0, "width": 5.0, "height": 3.0},
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
                "unit_cost": 45.0,
                "status": "pending",
                "attributes": {
                    "weight": 0.8,
                    "dimensions": {"length": 5.0, "width": 3.0, "height": 1.0},
                    "tags": ["standard", "bulk"],
                },
                "created_by": "import_batch",
                "created_at": "2024-01-16T09:15:00Z",
                "modified_by": "import_batch",
                "modified_at": "2024-01-16T09:15:00Z",
                "version": 1,
            },
        ]
        for record_data in complex_records:
            record_message = {
                "type": "RECORD",
                "stream": "advanced_inventory",
                "record": record_data,
                "time_extracted": "2024-01-16T12:00:00Z",
            }
            record_result = target.process_record_message(record_message)
            if not record_result.is_success:
                logger.error(f"Complex record failed: {record_result.error}")
                continue
            logger.info(f"Processed complex record: {record_data['item_id']}")
        invalid_record = {
            "type": "RECORD",
            "stream": "advanced_inventory",
            "record": {
                "item_id": "",
                "item_name": "Invalid Item",
                "effective_date": "invalid-date",
                "status": "unknown_status",
            },
        }
        invalid_result = target.process_record_message(invalid_record)
        if not invalid_result.is_success:
            logger.info(f"Invalid record correctly rejected: {invalid_result.error}")
        else:
            logger.warning("Invalid record was unexpectedly accepted")
        final_result = target.finalize()
        if final_result.is_success and final_result.data:
            stats = final_result.data
            logger.info(
                f"Processing completed - Records: {stats.get('total_records', 0)}, Errors: {stats.get('total_errors', 0)}"
            )
    except (
        ValueError,
        TypeError,
        KeyError,
        AttributeError,
        OSError,
        RuntimeError,
        ImportError,
    ):
        logger.exception("Advanced configuration example failed")
        raise
    finally:
        target.cleanup()


@flext_monitor_function(monitor)
def demonstrate_custom_components() -> None:
    """Demonstrate usage of custom WMS components."""
    logger.info("Demonstrating custom WMS components")
    custom_converter = CustomWMSTypeConverter()
    date_result = custom_converter.convert_singer_to_oracle(
        "business_date", "2024-01-15"
    )
    logger.info(f"Business date conversion: {date_result.data}")
    currency_result = custom_converter.convert_singer_to_oracle(
        "business_currency", 123.456789
    )
    logger.info(f"Currency conversion: {currency_result.data}")
    status_result = custom_converter.convert_singer_to_oracle("wms_status", "active")
    logger.info(f"Status mapping: {status_result.data}")
    table_manager = WMSTableManager()
    table_name = table_manager.generate_table_name("inventory", "CUSTOM")
    logger.info("Generated table name: %s", table_name)
    schema_mapper = WMSSchemaMapper()
    test_schema: dict[str, t.ContainerValue] = {
        "properties": {
            "business_date": {"type": "business_date"},
            "amount": {"type": "business_currency"},
            "status": {"type": "wms_status"},
        }
    }
    mapping_result = schema_mapper.map_singer_schema_to_oracle(test_schema)
    if mapping_result.is_success:
        logger.info(f"Schema mapping: {mapping_result.data}")


if __name__ == "__main__":
    "Run advanced configuration examples."
    run_advanced_configuration_example()
    demonstrate_custom_components()
