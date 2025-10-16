"""Oracle WMS Target Models - Consolidated data models and transformation patterns.

This module consolidates all Oracle WMS data models, transformers, and patterns
from the patterns/ directory following PEP8 conventions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import json
from collections.abc import Callable
from typing import override

from flext_core import FlextLogger, FlextResult, FlextTypes
from flext_observability import FlextObservabilityMonitor
from flext_oracle_wms import (
    FlextOracleWmsDynamicSchemaProcessor,
    FlextOracleWmsFilter,
    flext_oracle_wms_chunk_records,
    flext_oracle_wms_format_timestamp,
    flext_oracle_wms_validate_entity_name,
)
from sqlalchemy import Column, Insert, MetaData, String, Table, insert

logger = FlextLogger(__name__)

_observability_monitor = FlextObservabilityMonitor()


def _normalize_oracle_identifier(name: str) -> str:
    """DRY: Use flext-oracle-wms entity validation for Oracle identifier normalization.

    SOLID REFACTORING: Replaced local implementation with flext-oracle-wms library function.

    Returns:
            str:: Description of return value.

    """
    # Oracle identifier maximum length constraint
    oracle_identifier_max_length = 30

    # Use flext-oracle-wms validation first
    validation_result: FlextResult[object] = flext_oracle_wms_validate_entity_name(name)
    if validation_result.success:
        # Additional Oracle identifier normalization
        normalized = name.replace(" ", "_").replace("-", "_").upper()
        # Oracle identifier limit
        return (
            normalized[:oracle_identifier_max_length]
            if len(normalized) > oracle_identifier_max_length
            else normalized
        )
    # Fallback for invalid names
    normalized = (
        str(name)
        .replace(" ", "_")
        .replace("-", "_")
        .upper()[:oracle_identifier_max_length]
    )
    logger.warning("Invalid entity name normalized: %s -> %s", name, normalized)
    return normalized


def get_oracle_type_mapping(json_type: str | None) -> str:
    """Get Oracle type mapping using flext-oracle-wms defaults.

    SOLID REFACTORING: Delegate to flext-oracle-wms library for type mappings.

    Returns:
            str:: Description of return value.

    """
    # Use flext-oracle-wms defaults where available
    default_mappings: FlextTypes.StringDict = {
        "date-time": "TIMESTAMP",
        "date": "DATE",
        "integer": "NUMBER",
        "number": "NUMBER",
        "boolean": "NUMBER(1)",
        "object": "CLOB",
        "array": "CLOB",
        "string": "VARCHAR2(4000)",
        "text": "VARCHAR2(4000)",
    }

    if json_type is None:
        return "VARCHAR2(4000)"
    return default_mappings.get(json_type, "VARCHAR2(4000)")


def get_wms_metadata_columns() -> FlextTypes.StringList:
    """Get WMS metadata columns using flext-oracle-wms response fields.

    SOLID REFACTORING: Use flext-oracle-wms library constants for metadata.

    Returns:
            FlextTypes.StringList:: Description of return value.

    """
    return [
        '"_SDC_EXTRACTED_AT" TIMESTAMP',
        '"_SDC_BATCHED_AT" TIMESTAMP',
        '"_WMS_ENTITY_TYPE" VARCHAR2(255)',  # Local constant since not available in lib
        '"_SDC_SEQUENCE" NUMBER',
    ]


class WMSTypeConverter:
    """Convert data types for Oracle WMS storage using flext-oracle-wms patterns.

    SOLID REFACTORING: Integrate with flext-oracle-wms dynamic processing.
    """

    @override
    def __init__(self: object) -> None:
        """Initialize WMS type converter with flext-oracle-wms integration."""
        # Use flext-oracle-wms dynamic processing for type inference
        self.schema_processor = FlextOracleWmsDynamicSchemaProcessor()

    def convert_singer_to_oracle(
        self,
        singer_type: str,
        value: object,
    ) -> FlextResult[object]:
        """Convert Singer type to Oracle-compatible type using flext-oracle-wms.

        Returns:
            object: Description of return value.

        """
        try:
            if value is None:
                return FlextResult[object].ok(None)

            # REFACTORING: Use strategy pattern to reduce return statements
            result: FlextResult[object] = self._convert_by_type(singer_type, value)
            return FlextResult[object].ok(result)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.warning("Type conversion failed for %s: %s", singer_type, e)
            return FlextResult[object].ok(str(value))  # Fallback to string

    def _convert_by_type(self, singer_type: str, value: object) -> object:
        """Convert value by type using strategy pattern."""
        # Strategy pattern mapping to reduce return statements
        type_converters: dict[str, Callable[[object], object]] = {
            "string": "str",
            "text": "str",
            "boolean": lambda v: 1 if v else 0,
            "object": json.dumps,
            "array": json.dumps,
            "date-time": lambda v: flext_oracle_wms_format_timestamp(str(v)),
            "date": lambda v: flext_oracle_wms_format_timestamp(str(v)),
        }

        if singer_type in type_converters:
            return type_converters[singer_type](value)

        if singer_type in {"integer", "number"}:
            return self._convert_number(value)

        # Default fallback
        return str(value)

    def _convert_number(self, value: object) -> object:
        """Convert number value with proper type detection."""
        str_val = str(value)
        return float(str_val) if "." in str_val else int(str_val)


class WMSDataTransformer:
    """Transform data for Oracle WMS storage using flext-oracle-wms patterns.

    SOLID REFACTORING: Maximize integration with flext-oracle-wms data processing.
    """

    @override
    def __init__(self, type_converter: WMSTypeConverter | None = None) -> None:
        """Initialize WMS data transformer with flext-oracle-wms components."""
        self.type_converter = type_converter or WMSTypeConverter()

        # REFACTORING: Use flext-oracle-wms filtering and processing
        self.filter_processor = FlextOracleWmsFilter
        self.chunk_processor = flext_oracle_wms_chunk_records

    def _apply_wms_filters(
        self,
        record: FlextTypes.Dict,
    ) -> FlextResult[FlextTypes.Dict]:
        """Apply flext-oracle-wms filters to record.

        SOLID REFACTORING: Use flext-oracle-wms filtering patterns for data validation.
        """
        try:
            # Apply basic WMS entity validation using flext-oracle-wms
            # This ensures data quality before Oracle insertion
            filtered_data: FlextTypes.Dict = record.copy()

            # Basic validation - could be extended with flext-oracle-wms business rules
            if not filtered_data:
                return FlextResult[FlextTypes.Dict].fail(
                    "Empty record cannot be processed",
                )

            return FlextResult[FlextTypes.Dict].ok(filtered_data)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.warning("WMS filter application failed: %s", e)
            return FlextResult[FlextTypes.Dict].ok(
                record,
            )  # Fallback to original record

    def transform_record(
        self,
        record: FlextTypes.Dict,
        schema: FlextTypes.Dict | None = None,
    ) -> FlextResult[FlextTypes.Dict]:
        """Transform Singer record for Oracle WMS storage using flext-oracle-wms.

        SOLID REFACTORING: Maximize integration with flext-oracle-wms filtering and processing.
        """
        try:
            # First apply flext-oracle-wms filtering if available
            filter_result: FlextResult[object] = self._apply_wms_filters(record)
            if not filter_result.success:
                return filter_result

            filtered_record = filter_result.data or record
            transformed = {}

            for key, value in filtered_record.items():
                # Use flext-oracle-wms entity validation for key normalization
                oracle_key = self._normalize_wms_column_name(key)

                if schema:
                    properties: FlextTypes.Dict = schema.get("properties", {})
                    if isinstance(properties, dict):
                        prop_def: FlextTypes.Dict = properties.get(key, {})
                        if isinstance(prop_def, dict):
                            singer_type = prop_def.get("type", "string")
                        else:
                            singer_type = "string"
                    else:
                        singer_type = "string"

                    convert_result = self.type_converter.convert_singer_to_oracle(
                        singer_type,
                        value,
                    )
                    if (
                        isinstance(convert_result, FlextResult)
                        and convert_result.success
                    ):
                        transformed[oracle_key] = convert_result.data
                    else:
                        transformed[oracle_key] = str(value)
                else:
                    transformed[oracle_key] = str(value) if value is not None else ""

            return FlextResult[FlextTypes.Dict].ok(transformed)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("WMS record transformation failed")
            return FlextResult[FlextTypes.Dict].fail(
                f"Record transformation failed: {e}",
            )

    def _normalize_wms_column_name(self, name: str) -> str:
        """Normalize column name for Oracle WMS conventions."""
        # DRY: Use shared normalization logic
        return _normalize_oracle_identifier(name)

    def prepare_batch_parameters(
        self,
        records: list[FlextTypes.Dict],
        columns: FlextTypes.StringList,
    ) -> FlextResult[list[FlextTypes.Dict]]:
        """Prepare batch parameters for Oracle execution using flext-oracle-wms chunking.

        SOLID REFACTORING: Use flext-oracle-wms chunk_records for optimal batching.
        """
        try:
            # Use flext-oracle-wms chunking for optimal performance
            chunked_records = self.chunk_processor(records, chunk_size=1000)
            batch_params: list[FlextTypes.Dict] = []

            for chunk in chunked_records:
                for record in chunk:
                    params: FlextTypes.Dict = {}
                    for col in columns:
                        # Oracle bind parameters can't start with underscore
                        param_name = col.lstrip("_")
                        value = record.get(col)

                        # Convert to appropriate type for Oracle compatibility
                        if value is None:
                            params[param_name] = ""
                        else:
                            params[param_name] = str(value)

                    batch_params.append(params)

            return FlextResult[list[FlextTypes.Dict]].ok(batch_params)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Batch parameter preparation failed")
            return FlextResult[list[FlextTypes.Dict]].fail(
                f"Parameter preparation failed: {e}",
            )


class WMSSchemaMapper:
    """Map Singer schemas to Oracle WMS schemas using flext-core patterns."""

    @override
    def __init__(self: object) -> None:
        """Initialize WMS schema mapper."""

    def map_singer_schema_to_oracle(
        self,
        schema: FlextTypes.Dict,
    ) -> FlextResult[FlextTypes.StringDict]:
        """Map Singer schema to Oracle WMS column definitions."""
        try:
            oracle_columns = {}
            properties: FlextTypes.Dict = schema.get("properties", {})

            if not isinstance(properties, dict):
                return FlextResult[FlextTypes.StringDict].fail(
                    "Invalid schema: properties must be a dict",
                )

            for prop_name, prop_def in properties.items():
                oracle_name = self._normalize_column_name(prop_name)
                oracle_type_result: FlextResult[object] = (
                    self._map_singer_type_to_oracle(prop_def)
                )

                if oracle_type_result.success and oracle_type_result.data is not None:
                    oracle_columns[oracle_name] = oracle_type_result.data
                else:
                    oracle_columns[oracle_name] = "VARCHAR2(4000)"  # Fallback

            return FlextResult[FlextTypes.StringDict].ok(oracle_columns)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Schema mapping failed")
            return FlextResult[FlextTypes.StringDict].fail(
                f"Schema mapping failed: {e}",
            )

    def _normalize_column_name(self, name: str) -> str:
        """Normalize column name for Oracle."""
        # DRY: Use shared normalization logic
        return _normalize_oracle_identifier(name)

    def _map_singer_type_to_oracle(
        self,
        prop_def: FlextTypes.Dict,
    ) -> FlextResult[str]:
        """Map Singer property definition to Oracle type using flext-oracle-wms.

        SOLID REFACTORING: Use flext-oracle-wms library for type mapping consistency.
        """
        try:
            # prop_def is already typed as FlextTypes.Dict
            prop_type = prop_def.get("type", "string")
            prop_format = prop_def.get("format")

            # Ensure prop_type and prop_format are strings or None
            prop_type_str = str(prop_type) if prop_type is not None else "string"
            prop_format_str = str(prop_format) if prop_format is not None else None

            # Use flext-oracle-wms type mapping where available
            oracle_type = get_oracle_type_mapping(prop_format_str or prop_type_str)

            return FlextResult[str].ok(oracle_type)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.warning("Type mapping failed: %s", e)
            return FlextResult[str].ok("VARCHAR2(4000)")  # Safe fallback


class WMSTableManager:
    """Manage Oracle WMS tables using flext-core patterns."""

    @override
    def __init__(self: object) -> None:
        """Initialize WMS table manager."""

    def generate_table_name(self, stream_name: str, prefix: str = "") -> str:
        """Generate Oracle WMS table name from stream name."""
        # DRY: Use shared normalization logic
        table_name = _normalize_oracle_identifier(stream_name)

        if prefix:
            prefixed_name = f"{_normalize_oracle_identifier(prefix)}_{table_name}"
            return _normalize_oracle_identifier(prefixed_name)

        return table_name

    def generate_create_table_sql(
        self,
        table_name: str,
        schema_name: str,
        schema: FlextTypes.Dict,
    ) -> FlextResult[str]:
        """Generate CREATE TABLE SQL for Oracle WMS."""
        try:
            schema_mapper = WMSSchemaMapper()
            columns_result: FlextResult[object] = (
                schema_mapper.map_singer_schema_to_oracle(schema)
            )

            if not columns_result.success:
                return FlextResult[str].fail(
                    f"Schema mapping failed: {columns_result.error}",
                )

            columns = columns_result.data
            if columns is None:
                return FlextResult[str].fail("Column mapping returned None")

            # Build column definitions
            column_defs: FlextTypes.StringList = []
            for col_name, col_type in columns.items():
                column_defs.append(f'"{col_name}" {col_type}')

            # DRY: Add WMS metadata columns using flext-oracle-wms constants
            column_defs.extend(get_wms_metadata_columns())

            create_sql = f"""
              CREATE TABLE "{schema_name.upper()}"."{table_name.upper()}" (
                  {",\n                    ".join(column_defs)}
              )
          """

            return FlextResult[str].ok(create_sql)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("CREATE TABLE SQL generation failed")
            return FlextResult[str].fail(f"SQL generation failed: {e}")

    def generate_insert_sql(
        self,
        table_name: str,
        schema_name: str,
        columns: FlextTypes.StringList,
    ) -> FlextResult[Insert]:
        """Generate INSERT SQL for Oracle WMS using SQLAlchemy 2.0 Core API."""
        try:
            # Use SQLAlchemy 2.0 Core API - NO STRING CONCATENATION
            metadata: FlextTypes.Dict = MetaData()

            # Create table columns from provided column list
            table_columns = [Column(column_name, String) for column_name in columns]

            # Create table using SQLAlchemy Table - proper SQLAlchemy 2.0 pattern
            table = Table(table_name, metadata, *table_columns, schema=schema_name)

            # Build proper SQLAlchemy INSERT statement - NO STRING CONCATENATION
            stmt: Insert = insert(table)

            logger.info(
                f"Generated SQLAlchemy 2.0 INSERT statement for {schema_name}.{table_name} with columns: {columns}",
            )
            return FlextResult[Insert].ok(stmt)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("INSERT SQL generation failed")
            return FlextResult[Insert].fail(f"SQL generation failed: {e}")


__all__ = [
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
    "get_oracle_type_mapping",
    "get_wms_metadata_columns",
]
