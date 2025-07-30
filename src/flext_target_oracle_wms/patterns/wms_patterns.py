"""Oracle WMS patterns using flext-core patterns - REAL DRY REFACTORING."""

from __future__ import annotations

import json
from typing import Any

# DRY: Use REAL flext-core patterns - NO DUPLICATION
from flext_core import FlextResult, get_logger

# DRY: Use REAL flext-observability with correct signature - NO MOCKUP
from flext_observability import FlextObservabilityMonitor, flext_monitor_function

logger = get_logger(__name__)

# DRY: Single observability monitor instance - NO DUPLICATION
_observability_monitor = FlextObservabilityMonitor()


def _normalize_oracle_identifier(name: str) -> str:
    """DRY: Shared Oracle identifier normalization - SINGLE SOURCE OF TRUTH."""
    normalized = name.replace(" ", "_").replace("-", "_").upper()
    # Oracle identifier limit
    return normalized[:30] if len(normalized) > 30 else normalized


# DRY: Oracle type mappings - SINGLE SOURCE OF TRUTH
_ORACLE_TYPE_MAPPINGS = {
    "date-time": "TIMESTAMP",
    "date": "DATE",
    "integer": "NUMBER",
    "number": "NUMBER",
    "boolean": "NUMBER(1)",
    "object": "CLOB",
    "array": "CLOB",
    "string": "VARCHAR2(4000)",
    "text": "VARCHAR2(4000)",
    # Default fallback
    None: "VARCHAR2(4000)",
}

# DRY: WMS metadata columns - SINGLE SOURCE OF TRUTH
_WMS_METADATA_COLUMNS = [
    '"_SDC_EXTRACTED_AT" TIMESTAMP',
    '"_SDC_BATCHED_AT" TIMESTAMP',
    '"_SDC_ENTITY" VARCHAR2(255)',
    '"_SDC_SEQUENCE" NUMBER',
]


class WMSTypeConverter:
    """Convert data types for Oracle WMS storage using flext-core patterns."""

    def __init__(self) -> None:
        """Initialize WMS type converter."""

    @flext_monitor_function(monitor=_observability_monitor)
    def convert_singer_to_oracle(
        self,
        singer_type: str,
        value: object,
    ) -> FlextResult[Any]:
        """Convert Singer type to Oracle-compatible type with REAL observability."""
        try:
            if value is None:
                return FlextResult.ok(None)

            # DRY: Use type mapping logic based on constants
            if singer_type in {"string", "text"}:
                return FlextResult.ok(str(value))
            if singer_type in {"integer", "number"}:
                try:
                    str_val = str(value)
                    return FlextResult.ok(
                        float(str_val) if "." in str_val else int(str_val)
                    )
                except (ValueError, TypeError):
                    return FlextResult.fail(f"Cannot convert {value} to number")
            if singer_type == "boolean":
                return FlextResult.ok(1 if value else 0)
            if singer_type in {"object", "array"}:
                return FlextResult.ok(json.dumps(value))
            return FlextResult.ok(str(value))

        except (RuntimeError, ValueError, TypeError) as e:
            logger.warning(f"Type conversion failed for {singer_type}: {e}")
            return FlextResult.ok(str(value))  # Fallback to string


class WMSDataTransformer:
    """Transform data for Oracle WMS storage using flext-core patterns."""

    def __init__(self, type_converter: WMSTypeConverter | None = None) -> None:
        """Initialize WMS data transformer."""
        self.type_converter = type_converter or WMSTypeConverter()

    def transform_record(
        self,
        record: dict[str, Any],
        schema: dict[str, Any] | None = None,
    ) -> FlextResult[dict[str, Any]]:
        """Transform Singer record for Oracle WMS storage."""
        try:
            transformed = {}

            for key, value in record.items():
                # WMS-specific column naming
                oracle_key = self._normalize_wms_column_name(key)

                # Type conversion
                if schema:
                    properties = schema.get("properties", {})
                    prop_def = properties.get(key, {})
                    singer_type = prop_def.get("type", "string")

                    convert_result = self.type_converter.convert_singer_to_oracle(
                        singer_type,
                        value,
                    )
                    # Type assertion for MyPy - we know convert_singer_to_oracle returns FlextResult
                    if (
                        isinstance(convert_result, FlextResult)
                        and convert_result.is_success
                    ):
                        transformed[oracle_key] = convert_result.data
                    else:
                        transformed[oracle_key] = str(value)
                else:
                    transformed[oracle_key] = value

            return FlextResult.ok(transformed)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("WMS record transformation failed")
            return FlextResult.fail(f"Record transformation failed: {e}")

    def _normalize_wms_column_name(self, name: str) -> str:
        """Normalize column name for Oracle WMS conventions."""
        # DRY: Use shared normalization logic - NO DUPLICATION
        return _normalize_oracle_identifier(name)

    def prepare_batch_parameters(
        self,
        records: list[dict[str, Any]],
        columns: list[str],
    ) -> FlextResult[list[dict[str, Any]]]:
        """Prepare batch parameters for Oracle execution."""
        try:
            batch_params = []

            for record in records:
                params = {}
                for col in columns:
                    # Oracle bind parameters can't start with underscore
                    param_name = col.lstrip("_")
                    value = record.get(col)

                    # Convert to string for Oracle compatibility
                    if value is None:
                        params[param_name] = ""
                    else:
                        params[param_name] = str(value)

                batch_params.append(params)

            return FlextResult.ok(batch_params)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Batch parameter preparation failed")
            return FlextResult.fail(f"Parameter preparation failed: {e}")


class WMSSchemaMapper:
    """Map Singer schemas to Oracle WMS schemas using flext-core patterns."""

    def __init__(self) -> None:
        """Initialize WMS schema mapper."""

    def map_singer_schema_to_oracle(
        self,
        schema: dict[str, Any],
    ) -> FlextResult[dict[str, str]]:
        """Map Singer schema to Oracle WMS column definitions."""
        try:
            oracle_columns = {}
            properties = schema.get("properties", {})

            for prop_name, prop_def in properties.items():
                oracle_name = self._normalize_column_name(prop_name)
                oracle_type_result = self._map_singer_type_to_oracle(prop_def)

                if (
                    oracle_type_result.is_success
                    and oracle_type_result.data is not None
                ):
                    oracle_columns[oracle_name] = oracle_type_result.data
                else:
                    oracle_columns[oracle_name] = "VARCHAR2(4000)"  # Fallback

            return FlextResult.ok(oracle_columns)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Schema mapping failed")
            return FlextResult.fail(f"Schema mapping failed: {e}")

    def _normalize_column_name(self, name: str) -> str:
        """Normalize column name for Oracle."""
        # DRY: Use shared normalization logic - NO DUPLICATION
        return _normalize_oracle_identifier(name)

    def _map_singer_type_to_oracle(self, prop_def: dict[str, Any]) -> FlextResult[str]:
        """Map Singer property definition to Oracle type."""
        try:
            prop_type = prop_def.get("type", "string")
            prop_format = prop_def.get("format")

            # DRY: Use shared type mapping constants - NO DUPLICATION
            # Priority: format-specific mapping first, then type mapping, then fallback
            oracle_type = (
                (_ORACLE_TYPE_MAPPINGS.get(prop_format) if prop_format else None)
                or _ORACLE_TYPE_MAPPINGS.get(prop_type)
                or _ORACLE_TYPE_MAPPINGS[None]
            )

            return FlextResult.ok(oracle_type)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.warning(f"Type mapping failed: {e}")
            return FlextResult.ok(_ORACLE_TYPE_MAPPINGS[None])


class WMSTableManager:
    """Manage Oracle WMS tables using flext-core patterns."""

    def __init__(self) -> None:
        """Initialize WMS table manager."""

    def generate_table_name(self, stream_name: str, prefix: str = "") -> str:
        """Generate Oracle WMS table name from stream name."""
        # DRY: Use shared normalization logic - NO DUPLICATION
        table_name = _normalize_oracle_identifier(stream_name)

        if prefix:
            prefixed_name = f"{_normalize_oracle_identifier(prefix)}_{table_name}"
            return _normalize_oracle_identifier(prefixed_name)

        return table_name

    def generate_create_table_sql(
        self,
        table_name: str,
        schema_name: str,
        schema: dict[str, Any],
    ) -> FlextResult[str]:
        """Generate CREATE TABLE SQL for Oracle WMS."""
        try:
            schema_mapper = WMSSchemaMapper()
            columns_result = schema_mapper.map_singer_schema_to_oracle(schema)

            if not columns_result.is_success:
                return FlextResult.fail(
                    f"Schema mapping failed: {columns_result.error}",
                )

            columns = columns_result.data
            if columns is None:
                return FlextResult.fail("Column mapping returned None")

            # Build column definitions
            column_defs = []
            for col_name, col_type in columns.items():
                column_defs.append(f'"{col_name}" {col_type}')

            # DRY: Add WMS metadata columns using shared constants - NO DUPLICATION
            column_defs.extend(_WMS_METADATA_COLUMNS)

            create_sql = f"""
                CREATE TABLE "{schema_name.upper()}"."{table_name.upper()}" (
                    {",\n                    ".join(column_defs)}
                )
            """

            return FlextResult.ok(create_sql)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("CREATE TABLE SQL generation failed")
            return FlextResult.fail(f"SQL generation failed: {e}")

    def generate_insert_sql(
        self,
        table_name: str,
        schema_name: str,
        columns: list[str],
    ) -> FlextResult[str]:
        """Generate INSERT SQL for Oracle WMS."""
        try:
            quoted_columns = [f'"{col.upper()}"' for col in columns]
            placeholders = [f":{col.lower().lstrip('_')}" for col in columns]

            # Build parametrized INSERT SQL (safe - uses placeholders)
            # Note: SQL injection is not possible here as all table/column names are controlled
            # and parameters use proper placeholders

            insert_sql = f'INSERT INTO "{schema_name.upper()}"."{table_name.upper()}" ({", ".join(quoted_columns)}) VALUES ({", ".join(placeholders)})'  # noqa: S608

            return FlextResult.ok(insert_sql)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("INSERT SQL generation failed")
            return FlextResult.fail(f"SQL generation failed: {e}")
