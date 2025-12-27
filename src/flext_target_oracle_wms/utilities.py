"""FlextTargetOracleWmsUtilities - Singer target utilities for Oracle Warehouse Management System operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import ClassVar

from flext_core import FlextResult, FlextTypes as t
from flext_core.utilities import FlextUtilities as u_core

from flext_target_oracle_wms.constants import c


class FlextTargetOracleWmsUtilities(u_core):
    """Single unified utilities class for Singer target Oracle WMS operations.

    This class provides complete Oracle WMS target functionality for Singer protocol
    integration, including warehouse operations, inventory management, business rule
    validation, and high-performance data loading for enterprise warehouse systems.

    Oracle WMS Domain Specialization:
    - Enterprise Oracle WMS connectivity with business rule validation
    - Warehouse operations management (inventory, shipments, receipts, labor)
    - High-performance bulk WMS operations with transaction management
    - Singer protocol compliance with stream-to-WMS-entity mapping
    - WMS-specific error handling with complete business rule enforcement
    - Enterprise security with WMS authentication and authorization patterns
    - WMS performance monitoring and optimization patterns

    Attributes:
        WMS_DEFAULT_BATCH_SIZE: Default batch size for WMS bulk operations (1000)
        WMS_DEFAULT_CONNECTION_TIMEOUT: Default WMS connection timeout (120 seconds)
        WMS_DEFAULT_PARALLEL_DEGREE: Default parallel processing degree (8)
        MAX_WMS_RETRIES: Maximum WMS operation retry attempts (5)
        DEFAULT_FACILITY_CODE: Default WMS facility code ("MAIN_DC")

    """

    WMS_DEFAULT_BATCH_SIZE: ClassVar[int] = 1000
    WMS_DEFAULT_CONNECTION_TIMEOUT: ClassVar[int] = 120
    WMS_DEFAULT_PARALLEL_DEGREE: ClassVar[int] = 8
    MAX_WMS_RETRIES: ClassVar[int] = 5
    DEFAULT_FACILITY_CODE: ClassVar[str] = "MAIN_DC"
    WMS_MAX_BULK_SIZE: ClassVar[int] = 10000
    DEFAULT_REQUEST_TIMEOUT: ClassVar[int] = 300

    class SingerUtilities:
        """Singer protocol utilities for Oracle WMS target operations."""

        @staticmethod
        def create_schema_message(
            stream_name: str,
            schema: dict[str, t.GeneralValueType],
            key_properties: list[str] | None = None,
        ) -> dict[str, t.GeneralValueType]:
            """Create Singer SCHEMA message for WMS entity definition.

            Args:
            stream_name: Name of the Singer stream
            schema: JSON schema definition for the stream
            key_properties: List of key property names

            Returns:
            Singer SCHEMA message dictionary

            """
            return {
                "type": "SCHEMA",
                "stream": stream_name,
                "schema": schema,
                "key_properties": key_properties or [],
                "bookmark_properties": [],
            }

        @staticmethod
        def create_record_message(
            stream_name: str,
            record: dict[str, t.GeneralValueType],
            time_extracted: str | None = None,
        ) -> dict[str, t.GeneralValueType]:
            """Create Singer RECORD message for WMS data loading.

            Args:
            stream_name: Name of the Singer stream
            record: WMS record data to load
            time_extracted: Optional extraction timestamp

            Returns:
            Singer RECORD message dictionary

            """
            message = {
                "type": "RECORD",
                "stream": stream_name,
                "record": record,
            }
            if time_extracted:
                message["time_extracted"] = time_extracted
            return message

        @staticmethod
        def create_state_message(
            state: dict[str, t.GeneralValueType],
        ) -> dict[str, t.GeneralValueType]:
            """Create Singer STATE message for WMS target checkpointing.

            Args:
            state: State data for checkpointing

            Returns:
            Singer STATE message dictionary

            """
            return {"type": "STATE", "value": state}

        @staticmethod
        def validate_singer_message(
            message: dict[str, t.GeneralValueType],
        ) -> FlextResult[dict[str, t.GeneralValueType]]:
            """Validate Singer message format and required fields.

            Args:
            message: Singer message to validate

            Returns:
            FlextResult containing validated message or error

            """
            if not isinstance(message, dict):
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    "Singer message must be a dictionary",
                )

            message_type = message.get("type")
            if message_type not in {"SCHEMA", "RECORD", "STATE"}:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    f"Invalid Singer message type: {message_type}",
                )

            if message_type == "SCHEMA":
                required_fields = ["stream", "schema"]
                for field in required_fields:
                    if field not in message:
                        return FlextResult[dict[str, t.GeneralValueType]].fail(
                            f"Missing required field for SCHEMA: {field}",
                        )

            elif message_type == "RECORD":
                required_fields = ["stream", "record"]
                for field in required_fields:
                    if field not in message:
                        return FlextResult[dict[str, t.GeneralValueType]].fail(
                            f"Missing required field for RECORD: {field}",
                        )

            elif message_type == "STATE":
                if "value" not in message:
                    return FlextResult[dict[str, t.GeneralValueType]].fail(
                        "Missing required field for STATE: value",
                    )

            return FlextResult[dict[str, t.GeneralValueType]].ok(message)

    class WmsEntityProcessing:
        """Oracle WMS entity-specific processing utilities."""

        @staticmethod
        def map_singer_stream_to_wms_entity(
            stream_name: str,
            schema: dict[str, t.GeneralValueType],
            wms_config: dict[str, t.GeneralValueType],
        ) -> FlextResult[dict[str, t.GeneralValueType]]:
            """Map Singer stream to Oracle WMS entity configuration.

            Args:
            stream_name: Name of the Singer stream
            schema: Singer stream schema
            wms_config: WMS-specific configuration

            Returns:
            FlextResult containing WMS entity mapping or error

            """
            try:
                # Map common WMS entities
                wms_entity_mapping = {
                    "inventory": "WMS_INVENTORY",
                    "inventory_transactions": "WMS_INV_TRANSACTIONS",
                    "shipments": "WMS_SHIPMENTS",
                    "receipts": "WMS_RECEIPTS",
                    "labor": "WMS_LABOR",
                    "item_master": "WMS_ITEM_MASTER",
                    "locations": "WMS_LOCATIONS",
                    "orders": "WMS_ORDERS",
                    "picks": "WMS_PICKS",
                    "putaways": "WMS_PUTAWAYS",
                }

                wms_table = wms_entity_mapping.get(stream_name.lower())
                if not wms_table:
                    # Use stream name as table name if not in standard mapping
                    wms_table = f"WMS_{stream_name.upper()}"

                entity_mapping = {
                    "stream_name": stream_name,
                    "wms_table_name": wms_table,
                    "wms_entity_type": stream_name.lower(),
                    "schema": schema,
                    "wms_configuration": wms_config,
                    "facility_code": wms_config.get(
                        "facility_code",
                        FlextTargetOracleWmsUtilities.DEFAULT_FACILITY_CODE,
                    ),
                    "company_code": wms_config.get("company_code", "DEFAULT"),
                    "load_method": wms_config.get("load_method", "BATCH_INSERT"),
                    "validation_rules": wms_config.get("validation_rules", []),
                    "business_rules": wms_config.get("business_rules", []),
                }

                return FlextResult[dict[str, t.GeneralValueType]].ok(entity_mapping)

            except Exception as e:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    f"Failed to map Singer stream to WMS entity: {e}",
                )

        @staticmethod
        def validate_wms_business_rules(
            entity_type: str,
            record: dict[str, t.GeneralValueType],
            business_rules: list[str],
        ) -> FlextResult[dict[str, t.GeneralValueType]]:
            """Validate Oracle WMS business rules for entity record.

            Args:
            entity_type: Type of WMS entity (inventory, shipment, etc.)
            record: WMS entity record data
            business_rules: List of business rules to validate

            Returns:
            FlextResult containing validated record or error

            """
            try:
                validation_results = []

                for rule in business_rules:
                    if rule == "item_code_exists" and entity_type in {
                        "inventory",
                        "inventory_transactions",
                    }:
                        if not record.get("item_code"):
                            return FlextResult[dict[str, t.GeneralValueType]].fail(
                                "Item code is required for inventory entities",
                            )

                    elif rule == "location_code_exists" and entity_type in {
                        "inventory",
                        "picks",
                        "putaways",
                    }:
                        if not record.get("location_code"):
                            return FlextResult[dict[str, t.GeneralValueType]].fail(
                                "Location code is required for location-based entities",
                            )

                    elif rule == "quantity_positive" and entity_type in {
                        "inventory",
                        "inventory_transactions",
                    }:
                        quantity = record.get("quantity", 0)
                        if not isinstance(quantity, (int, float)) or quantity < 0:
                            return FlextResult[dict[str, t.GeneralValueType]].fail(
                                "Quantity must be a positive number",
                            )

                    elif rule == "order_reference_exists" and entity_type in {
                        "shipments",
                        "picks",
                    }:
                        if not record.get("order_id") and not record.get(
                            "order_number",
                        ):
                            return FlextResult[dict[str, t.GeneralValueType]].fail(
                                "Order reference is required for order-based entities",
                            )

                    elif rule == "facility_code_valid":
                        facility_code = record.get("facility_code")
                        if not facility_code or not isinstance(facility_code, str):
                            return FlextResult[dict[str, t.GeneralValueType]].fail(
                                "Valid facility code is required",
                            )

                    validation_results.append(f"{rule}: PASSED")

                validated_record = record.copy()
                validated_record["_validation_results"] = validation_results

                return FlextResult[dict[str, t.GeneralValueType]].ok(validated_record)

            except Exception as e:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    f"Failed to validate WMS business rules: {e}",
                )

        @staticmethod
        def transform_record_for_wms(
            record: dict[str, t.GeneralValueType],
            entity_mapping: dict[str, t.GeneralValueType],
        ) -> FlextResult[dict[str, t.GeneralValueType]]:
            """Transform Singer record for Oracle WMS entity loading.

            Args:
            record: Singer record data
            entity_mapping: WMS entity mapping configuration

            Returns:
            FlextResult containing transformed record or error

            """
            try:
                entity_type = entity_mapping.get("wms_entity_type", "")
                facility_code = entity_mapping.get("facility_code")
                company_code = entity_mapping.get("company_code")

                transformed = record.copy()

                # Add mandatory WMS fields
                if facility_code:
                    transformed["facility_code"] = facility_code
                if company_code:
                    transformed["company_code"] = company_code

                # Add WMS audit fields
                current_time = datetime.now(UTC).isoformat()
                transformed["load_timestamp"] = current_time
                transformed["load_source"] = "SINGER_TARGET"

                # Entity-specific transformations
                if entity_type == "inventory":
                    # Ensure required inventory fields
                    if "unit_of_measure" not in transformed:
                        transformed["unit_of_measure"] = "EA"  # Default to Each
                    if "status" not in transformed:
                        transformed["status"] = "AVAILABLE"

                elif entity_type == "inventory_transactions":
                    # Ensure transaction type
                    if "transaction_type" not in transformed:
                        # Determine transaction type based on quantity
                        quantity = transformed.get("quantity", 0)
                        transformed["transaction_type"] = (
                            "RECEIPT" if quantity > 0 else "ISSUE"
                        )

                elif entity_type == "shipments":
                    # Ensure shipment status
                    if "shipment_status" not in transformed:
                        transformed["shipment_status"] = "PLANNED"

                # Convert field names to WMS conventions (uppercase)
                wms_record = {}
                for key, value in transformed.items():
                    wms_key = key.upper()
                    wms_record[wms_key] = value

                return FlextResult[dict[str, t.GeneralValueType]].ok(wms_record)

            except Exception as e:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    f"Failed to transform record for WMS: {e}",
                )

    class WmsOperationUtilities:
        """Oracle WMS operation utilities for bulk processing."""

        @staticmethod
        def prepare_wms_bulk_operation(
            records: list[dict[str, t.GeneralValueType]],
            operation_config: dict[str, t.GeneralValueType],
        ) -> FlextResult[dict[str, t.GeneralValueType]]:
            """Prepare Oracle WMS bulk operation configuration.

            Args:
            records: List of WMS records for bulk operation
            operation_config: WMS operation configuration

            Returns:
            FlextResult containing bulk operation setup or error

            """
            try:
                entity_type = operation_config.get("entity_type", "")
                batch_size = operation_config.get(
                    "batch_size",
                    FlextTargetOracleWmsUtilities.WMS_DEFAULT_BATCH_SIZE,
                )
                parallel_degree = operation_config.get(
                    "parallel_degree",
                    FlextTargetOracleWmsUtilities.WMS_DEFAULT_PARALLEL_DEGREE,
                )

                # Validate batch size
                batch_size = min(
                    batch_size,
                    FlextTargetOracleWmsUtilities.WMS_MAX_BULK_SIZE,
                )

                # Split records into batches
                batches = []
                for i in range(0, len(records), batch_size):
                    batch = records[i : i + batch_size]
                    batches.append(batch)

                bulk_operation = {
                    "entity_type": entity_type,
                    "total_records": len(records),
                    "batch_count": len(batches),
                    "batch_size": batch_size,
                    "parallel_degree": parallel_degree,
                    "batches": batches,
                    "operation_metadata": {
                        "load_method": operation_config.get(
                            "load_method",
                            "BATCH_INSERT",
                        ),
                        "enable_parallel": operation_config.get(
                            "enable_parallel",
                            True,
                        ),
                        "validate_records": operation_config.get(
                            "validate_records",
                            True,
                        ),
                        "enable_wms_hints": operation_config.get(
                            "enable_wms_hints",
                            True,
                        ),
                    },
                }

                return FlextResult[dict[str, t.GeneralValueType]].ok(bulk_operation)

            except Exception as e:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    f"Failed to prepare WMS bulk operation: {e}",
                )

        @staticmethod
        def calculate_wms_performance_hints(
            entity_type: str,
            record_count: int,
            operation_type: str = "INSERT",
        ) -> FlextResult[dict[str, str]]:
            """Calculate Oracle WMS performance hints for operations.

            Args:
            entity_type: Type of WMS entity
            record_count: Number of records in operation
            operation_type: Type of operation (INSERT, UPDATE, DELETE)

            Returns:
            FlextResult containing WMS performance hints or error

            """
            try:
                hints = {}

                # Base hints for WMS operations
                if (
                    operation_type.upper() == "INSERT"
                    and record_count
                    > c.TargetOracleWms.OracleWms.PARALLEL_OPERATION_THRESHOLD
                ):
                    hints["bulk_collect"] = "FORALL"
                    hints["append_hint"] = "APPEND"
                    if record_count > c.TargetOracleWms.OracleWms.HIGH_VOLUME_THRESHOLD:
                        hints["parallel_hint"] = (
                            f"PARALLEL({FlextTargetOracleWmsUtilities.WMS_DEFAULT_PARALLEL_DEGREE})"
                        )
                        hints["nologging"] = "NOLOGGING"

                # Entity-specific hints
                if entity_type == "inventory":
                    hints["index_hint"] = "INDEX(inv, WMS_INV_ITEM_LOC_IDX)"
                elif entity_type == "inventory_transactions":
                    hints["index_hint"] = "INDEX(txn, WMS_TXN_TIMESTAMP_IDX)"
                elif entity_type in {"shipments", "orders"}:
                    hints["index_hint"] = "INDEX(ord, WMS_ORDER_STATUS_IDX)"

                # Performance optimization hints
                if record_count > c.TargetOracleWms.OracleWms.HIGH_VOLUME_THRESHOLD:
                    hints["memory_hint"] = "USE_HASH(a,b)"
                    hints["temp_tablespace"] = "TEMP"

                return FlextResult[dict[str, str]].ok(hints)

            except Exception as e:
                return FlextResult[dict[str, str]].fail(
                    f"Failed to calculate WMS performance hints: {e}",
                )

    class StreamUtilities:
        """Singer stream processing utilities for Oracle WMS target."""

        @staticmethod
        def process_schema_stream(
            stream_name: str,
            schema_message: dict[str, t.GeneralValueType],
            wms_config: dict[str, t.GeneralValueType],
        ) -> FlextResult[dict[str, t.GeneralValueType]]:
            """Process Singer schema stream for WMS entity configuration.

            Args:
            stream_name: Name of the Singer stream
            schema_message: Singer SCHEMA message
            wms_config: WMS-specific configuration

            Returns:
            FlextResult containing processed schema information or error

            """
            try:
                schema = schema_message.get("schema", {})
                key_properties = schema_message.get("key_properties", [])

                # Map to WMS entity
                entity_result = FlextTargetOracleWmsUtilities.WmsEntityProcessing.map_singer_stream_to_wms_entity(
                    stream_name,
                    schema,
                    wms_config,
                )
                if entity_result.is_failure:
                    return FlextResult[dict[str, t.GeneralValueType]].fail(
                        f"WMS entity mapping failed: {entity_result.error}",
                    )

                processed_schema = {
                    "stream_name": stream_name,
                    "wms_entity_config": entity_result.value,
                    "key_properties": key_properties,
                    "properties": schema.get("properties", {}),
                    "wms_metadata": {
                        "entity_type": stream_name.lower(),
                        "load_strategy": wms_config.get("load_strategy", "bulk"),
                        "validation_level": wms_config.get(
                            "validation_level",
                            "strict",
                        ),
                    },
                }

                return FlextResult[dict[str, t.GeneralValueType]].ok(processed_schema)

            except Exception as e:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    f"Failed to process schema stream: {e}",
                )

        @staticmethod
        def batch_records_for_wms_loading(
            records: list[dict[str, t.GeneralValueType]],
            batch_size: int | None = None,
        ) -> FlextResult[list[list[dict[str, t.GeneralValueType]]]]:
            """Batch Singer records for efficient WMS loading operations.

            Args:
            records: List of Singer records
            batch_size: Size of each batch (default: WMS_DEFAULT_BATCH_SIZE)

            Returns:
            FlextResult containing list of batches or error

            """
            actual_batch_size = (
                batch_size or FlextTargetOracleWmsUtilities.WMS_DEFAULT_BATCH_SIZE
            )

            if actual_batch_size <= 0:
                return FlextResult[list[list[dict[str, t.GeneralValueType]]]].fail(
                    "Batch size must be positive",
                )

            try:
                batches = []
                for i in range(0, len(records), actual_batch_size):
                    batch = records[i : i + actual_batch_size]
                    batches.append(batch)

                return FlextResult[list[list[dict[str, t.GeneralValueType]]]].ok(
                    batches
                )

            except Exception as e:
                return FlextResult[list[list[dict[str, t.GeneralValueType]]]].fail(
                    f"Failed to batch records: {e}",
                )

    class ConfigValidation:
        """Configuration validation utilities for Oracle WMS target."""

        @staticmethod
        def validate_wms_connection_config(
            config: dict[str, t.GeneralValueType],
        ) -> FlextResult[dict[str, t.GeneralValueType]]:
            """Validate Oracle WMS connection configuration.

            Args:
            config: WMS connection configuration

            Returns:
            FlextResult containing validated config or error

            """
            required_fields = ["base_url", "company_code", "facility_code"]
            for field in required_fields:
                if field not in config or not config[field]:
                    return FlextResult[dict[str, t.GeneralValueType]].fail(
                        f"Missing required WMS config field: {field}",
                    )

            # Validate authentication method
            auth_method = config.get("auth_method", "oauth2")
            if auth_method == "oauth2":
                oauth_fields = [
                    "oauth_client_id",
                    "oauth_client_secret",
                    "oauth_token_url",
                ]
                for field in oauth_fields:
                    if field not in config or not config[field]:
                        return FlextResult[dict[str, t.GeneralValueType]].fail(
                            f"Missing required OAuth2 field: {field}",
                        )

            # Validate base URL
            base_url = config["base_url"]
            if not base_url.startswith(("https://", "http://")):
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    "WMS base URL must be a valid HTTP/HTTPS URL",
                )

            return FlextResult[dict[str, t.GeneralValueType]].ok(config)

        @staticmethod
        def validate_wms_target_config(
            config: dict[str, t.GeneralValueType],
        ) -> FlextResult[dict[str, t.GeneralValueType]]:
            """Validate Oracle WMS target-specific configuration.

            Args:
            config: WMS target configuration

            Returns:
            FlextResult containing validated config or error

            """
            # Validate batch size
            batch_size = config.get(
                "batch_size",
                FlextTargetOracleWmsUtilities.WMS_DEFAULT_BATCH_SIZE,
            )
            if (
                batch_size <= 0
                or batch_size > FlextTargetOracleWmsUtilities.WMS_MAX_BULK_SIZE
            ):
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    f"Batch size must be between 1 and {FlextTargetOracleWmsUtilities.WMS_MAX_BULK_SIZE}",
                )

            # Validate parallel degree
            parallel_degree = config.get(
                "parallel_degree",
                FlextTargetOracleWmsUtilities.WMS_DEFAULT_PARALLEL_DEGREE,
            )
            if (
                parallel_degree <= 0
                or parallel_degree > c.TargetOracleWms.OracleWms.MAX_PARALLEL_DEGREE
            ):
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    f"Parallel degree must be between 1 and {c.TargetOracleWms.OracleWms.MAX_PARALLEL_DEGREE}",
                )

            # Validate timeout
            timeout = config.get(
                "connection_timeout",
                FlextTargetOracleWmsUtilities.WMS_DEFAULT_CONNECTION_TIMEOUT,
            )
            if (
                timeout <= 0
                or timeout > c.TargetOracleWms.OracleWms.MAX_CONNECTION_TIMEOUT
            ):
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    f"Connection timeout must be between 1 and {c.TargetOracleWms.OracleWms.MAX_CONNECTION_TIMEOUT} seconds",
                )

            return FlextResult[dict[str, t.GeneralValueType]].ok(config)

    class StateManagement:
        """Singer state management utilities for Oracle WMS target."""

        @staticmethod
        def create_wms_target_state(
            entity_states: dict[str, t.GeneralValueType],
            target_metadata: dict[str, t.GeneralValueType] | None = None,
        ) -> FlextResult[dict[str, t.GeneralValueType]]:
            """Create Oracle WMS target state for Singer checkpointing.

            Args:
            entity_states: Dictionary of WMS entity states
            target_metadata: Optional target-specific metadata

            Returns:
            FlextResult containing WMS target state or error

            """
            try:
                state = {
                    "entities": entity_states,
                    "target_type": "oracle_wms",
                    "last_updated": datetime.now(UTC).isoformat(),
                }

                if target_metadata:
                    state["target_metadata"] = target_metadata

                return FlextResult[dict[str, t.GeneralValueType]].ok(state)

            except Exception as e:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    f"Failed to create WMS target state: {e}",
                )

        @staticmethod
        def update_entity_state(
            current_state: dict[str, t.GeneralValueType],
            entity_type: str,
            loading_result: dict[str, t.GeneralValueType],
        ) -> FlextResult[dict[str, t.GeneralValueType]]:
            """Update state for a specific WMS entity.

            Args:
            current_state: Current Singer state
            entity_type: Type of WMS entity
            loading_result: WMS loading result data

            Returns:
            FlextResult containing updated state or error

            """
            try:
                updated_state = current_state.copy()

                if "entities" not in updated_state:
                    updated_state["entities"] = {}

                updated_state["entities"][entity_type] = {
                    "loading_result": loading_result,
                    "last_updated": datetime.now(UTC).isoformat(),
                    "records_processed": loading_result.get("records_processed", 0),
                    "loading_status": loading_result.get("status", "unknown"),
                }

                return FlextResult[dict[str, t.GeneralValueType]].ok(updated_state)

            except Exception as e:
                return FlextResult[dict[str, t.GeneralValueType]].fail(
                    f"Failed to update entity state: {e}",
                )

    class PerformanceUtilities:
        """Oracle WMS performance optimization utilities."""

        @staticmethod
        def calculate_optimal_wms_batch_size(
            entity_type: str,
            record_size_bytes: int,
            available_memory_mb: int = 100,
        ) -> FlextResult[int]:
            """Calculate optimal batch size for WMS operations.

            Args:
            entity_type: Type of WMS entity
            record_size_bytes: Average size of record in bytes
            available_memory_mb: Available memory for batching in MB

            Returns:
            FlextResult containing optimal batch size or error

            """
            try:
                if record_size_bytes <= 0:
                    return FlextResult[int].fail("Record size must be positive")

                if available_memory_mb <= 0:
                    return FlextResult[int].fail("Available memory must be positive")

                available_memory_bytes = available_memory_mb * 1024 * 1024
                max_batch_size = available_memory_bytes // record_size_bytes

                # Entity-specific optimizations
                if entity_type == "inventory_transactions":
                    # Higher batch size for transaction-heavy operations
                    preferred_batch_size = min(max_batch_size, 5000)
                elif entity_type in {"shipments", "orders"}:
                    # Moderate batch size for complex entities
                    preferred_batch_size = min(max_batch_size, 1000)
                else:
                    # Default batch size
                    preferred_batch_size = min(
                        max_batch_size,
                        FlextTargetOracleWmsUtilities.WMS_DEFAULT_BATCH_SIZE,
                    )

                # Ensure minimum batch size
                optimal_batch_size = max(1, preferred_batch_size)

                return FlextResult[int].ok(optimal_batch_size)

            except Exception as e:
                return FlextResult[int].fail(
                    f"Failed to calculate optimal batch size: {e}",
                )

        @staticmethod
        def estimate_wms_operation_time(
            entity_type: str,
            record_count: int,
            batch_size: int,
            parallel_degree: int = 1,
        ) -> FlextResult[float]:
            """Estimate Oracle WMS operation completion time.

            Args:
            entity_type: Type of WMS entity
            record_count: Number of records to process
            batch_size: Batch size for processing
            parallel_degree: Degree of parallelism

            Returns:
            FlextResult containing estimated time in seconds or error

            """
            try:
                if record_count <= 0 or batch_size <= 0 or parallel_degree <= 0:
                    return FlextResult[float].fail("All parameters must be positive")

                # Base processing rates (records per second) by entity type
                processing_rates = {
                    "inventory": 500,
                    "inventory_transactions": 1000,
                    "shipments": 200,
                    "receipts": 300,
                    "orders": 150,
                    "picks": 400,
                    "putaways": 350,
                    "labor": 800,
                    "default": 300,
                }

                base_rate = processing_rates.get(
                    entity_type,
                    processing_rates["default"],
                )

                # Calculate effective rate with parallelism
                effective_rate = base_rate * parallel_degree

                # Add batch overhead (approximately 10% overhead per batch)
                num_batches = (record_count + batch_size - 1) // batch_size
                batch_overhead = num_batches * 0.1

                # Calculate estimated time
                processing_time = record_count / effective_rate
                total_time = processing_time + batch_overhead

                return FlextResult[float].ok(total_time)

            except Exception as e:
                return FlextResult[float].fail(
                    f"Failed to estimate WMS operation time: {e}",
                )

    # Proxy methods for backward compatibility (minimal)
    def validate_singer_message(
        self,
        message: dict[str, t.GeneralValueType],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Proxy to SingerUtilities.validate_singer_message."""
        return self.SingerUtilities.validate_singer_message(message)

    def validate_wms_business_rules(
        self,
        entity_type: str,
        record: dict[str, t.GeneralValueType],
        business_rules: list[str],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Proxy to WmsEntityProcessing.validate_wms_business_rules."""
        return self.WmsEntityProcessing.validate_wms_business_rules(
            entity_type,
            record,
            business_rules,
        )

    def validate_wms_connection_config(
        self,
        config: dict[str, t.GeneralValueType],
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Proxy to ConfigValidation.validate_wms_connection_config."""
        return self.ConfigValidation.validate_wms_connection_config(config)


__all__ = [
    "FlextTargetOracleWmsUtilities",
]
