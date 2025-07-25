"""Oracle WMS patterns using flext-core patterns."""

from __future__ import annotations

import json
from typing import Any

# Import from flext-core for foundational patterns
from flext_core import FlextResult, get_logger

logger = get_logger(__name__)


class WMSTypeConverter:
    """Convert data types for Oracle WMS storage using flext-core patterns."""

    def __init__(self) -> None:
        """Initialize WMS type converter."""

    def convert_singer_to_oracle(
        self,
        singer_type: str,
        value: Any,
    ) -> FlextResult[Any]:
        """Convert Singer type to Oracle-compatible type."""
        try:
            if value is None:
                return FlextResult.ok(None)

            if singer_type in {"string", "text"}:
                return FlextResult.ok(str(value))
            if singer_type in {"integer", "number"}:
                return FlextResult.ok(float(value) if "." in str(value) else int(value))
            if singer_type == "boolean":
                return FlextResult.ok(1 if value else 0)
            if singer_type in {"object", "array"}:
                return FlextResult.ok(json.dumps(value))
            return FlextResult.ok(str(value))

        except Exception as e:
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
                    if convert_result.is_success:
                        transformed[oracle_key] = convert_result.data
                    else:
                        transformed[oracle_key] = str(value)
                else:
                    transformed[oracle_key] = value

            return FlextResult.ok(transformed)

        except Exception as e:
            logger.exception("WMS record transformation failed")
            return FlextResult.fail(f"Record transformation failed: {e}")

    def _normalize_wms_column_name(self, name: str) -> str:
        """Normalize column name for Oracle WMS conventions."""
        # WMS-specific naming conventions
        normalized = name.replace(" ", "_").replace("-", "_")
        normalized = normalized.upper()

        # Truncate to Oracle's identifier limit
        if len(normalized) > 30:
            normalized = normalized[:30]

        return normalized

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

        except Exception as e:
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

                if oracle_type_result.is_success:
                    oracle_columns[oracle_name] = oracle_type_result.data
                else:
                    oracle_columns[oracle_name] = "VARCHAR2(4000)"  # Fallback

            return FlextResult.ok(oracle_columns)

        except Exception as e:
            logger.exception("Schema mapping failed")
            return FlextResult.fail(f"Schema mapping failed: {e}")

    def _normalize_column_name(self, name: str) -> str:
        """Normalize column name for Oracle."""
        normalized = name.replace(" ", "_").replace("-", "_")
        normalized = normalized.upper()

        if len(normalized) > 30:
            normalized = normalized[:30]

        return normalized

    def _map_singer_type_to_oracle(self, prop_def: dict[str, Any]) -> FlextResult[str]:
        """Map Singer property definition to Oracle type."""
        try:
            prop_type = prop_def.get("type", "string")
            prop_format = prop_def.get("format")

            if prop_format == "date-time":
                return FlextResult.ok("TIMESTAMP")
            if prop_format == "date":
                return FlextResult.ok("DATE")
            if prop_type in {"integer", "number"}:
                return FlextResult.ok("NUMBER")
            if prop_type == "boolean":
                return FlextResult.ok("NUMBER(1)")
            if prop_type in {"object", "array"}:
                return FlextResult.ok("CLOB")
            return FlextResult.ok("VARCHAR2(4000)")

        except Exception as e:
            logger.warning(f"Type mapping failed: {e}")
            return FlextResult.ok("VARCHAR2(4000)")


class WMSTableManager:
    """Manage Oracle WMS tables using flext-core patterns."""

    def __init__(self) -> None:
        """Initialize WMS table manager."""

    def generate_table_name(self, stream_name: str, prefix: str = "") -> str:
        """Generate Oracle WMS table name from stream name."""
        # WMS-specific table naming
        table_name = stream_name.replace("-", "_").upper()

        if prefix:
            table_name = f"{prefix.upper()}_{table_name}"

        # Truncate to Oracle's identifier limit
        if len(table_name) > 30:
            table_name = table_name[:30]

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

            # Build column definitions
            column_defs = []
            for col_name, col_type in columns.items():
                column_defs.append(f'"{col_name}" {col_type}')

            # Add WMS metadata columns
            column_defs.extend(
                [
                    '"_SDC_EXTRACTED_AT" TIMESTAMP',
                    '"_SDC_BATCHED_AT" TIMESTAMP',
                    '"_SDC_ENTITY" VARCHAR2(255)',
                    '"_SDC_SEQUENCE" NUMBER',
                ],
            )

            create_sql = f"""
                CREATE TABLE "{schema_name.upper()}"."{table_name.upper()}" (
                    {",\n                    ".join(column_defs)}
                )
            """

            return FlextResult.ok(create_sql)

        except Exception as e:
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
            insert_sql = (
                f'INSERT INTO "{schema_name.upper()}"."{table_name.upper()}" '  # noqa: S608
                f"({', '.join(quoted_columns)}) "
                f"VALUES ({', '.join(placeholders)})"
            )

            return FlextResult.ok(insert_sql)

        except Exception as e:
            logger.exception("INSERT SQL generation failed")
            return FlextResult.fail(f"SQL generation failed: {e}")
