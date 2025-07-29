"""Singer Target Oracle WMS implementation using flext-core patterns."""

from __future__ import annotations

import json
import sys
from typing import Any

# Import from flext-core for foundational patterns
from flext_core import FlextResult, get_logger

from flext_target_oracle_wms.connection import (
    OracleWMSConnection,
    OracleWMSConnectionConfig,
)
from flext_target_oracle_wms.patterns import WMSDataTransformer, WMSTableManager
from flext_target_oracle_wms.singer.catalog import SingerWMSCatalogManager
from flext_target_oracle_wms.singer.stream import SingerWMSStreamProcessor

logger = get_logger(__name__)


class SingerTargetOracleWMS:
    """Singer Target Oracle WMS implementation using flext-core patterns."""

    def __init__(self, config: dict[str, Any]) -> None:
        """Initialize Singer Target Oracle WMS."""
        self.config = config

        # Initialize Oracle WMS connection
        oracle_config = OracleWMSConnectionConfig(
            host=config.get("host", "localhost"),
            port=config.get("port", 1521),
            service_name=config.get("service_name", "XE"),
            username=config.get("username", "oracle"),
            password=config.get("password", "oracle"),
            schema=config.get("default_target_schema", "WMS_TARGET"),
            max_connections=config.get("max_connections", 10),
            connection_timeout=config.get("connection_timeout", 30),
        )

        self.oracle_connection = OracleWMSConnection(oracle_config)

        # Initialize WMS components
        self.catalog_manager = SingerWMSCatalogManager()
        self.table_manager = WMSTableManager()
        self.data_transformer = WMSDataTransformer()
        self.stream_processor = SingerWMSStreamProcessor(
            self.table_manager,
            self.data_transformer,
        )

        # Configuration options
        self.batch_size = config.get("batch_size", 1000)
        self.load_method = config.get("load_method", "APPEND_ONLY")
        self.table_prefix = config.get("table_prefix", "")

    def setup(self) -> FlextResult[None]:
        """Setup Oracle WMS Target."""
        try:
            # Test Oracle connection
            test_result = self.oracle_connection.test_connection()
            if not test_result.is_success:
                return FlextResult.fail(
                    f"Oracle WMS connection test failed: {test_result.error}",
                )

            logger.info("Singer Target Oracle WMS setup completed successfully")

            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Singer Target Oracle WMS setup failed")
            return FlextResult.fail(f"Setup failed: {e}")

    def process_schema_message(self, message: dict[str, Any]) -> FlextResult[None]:
        """Process Singer SCHEMA message."""
        try:
            if message.get("type") != "SCHEMA":
                return FlextResult.fail("Not a SCHEMA message")

            stream_name = message.get("stream")
            schema = message.get("schema")

            if not stream_name or not schema:
                return FlextResult.fail(
                    "Invalid SCHEMA message: missing stream or schema",
                )

            # Add to catalog
            catalog_result = self.catalog_manager.add_stream(stream_name, schema)
            if not catalog_result.is_success:
                return FlextResult.fail(
                    f"Failed to add stream to catalog: {catalog_result.error}",
                )

            # Initialize stream processing
            init_result = self.stream_processor.initialize_stream(stream_name, schema)
            if not init_result.is_success:
                return FlextResult.fail(
                    f"Stream initialization failed: {init_result.error}",
                )

            # Create/ensure Oracle WMS table exists
            table_name = self.table_manager.generate_table_name(
                stream_name,
                self.table_prefix,
            )
            schema_name = self.oracle_connection.config.schema_name

            create_sql_result = self.table_manager.generate_create_table_sql(
                table_name,
                schema_name,
                schema,
            )
            if not create_sql_result.is_success:
                return FlextResult.fail(
                    f"CREATE SQL generation failed: {create_sql_result.error}",
                )

            # Execute table creation (or check if exists)
            table_result = self._ensure_table_exists(
                table_name,
                schema_name,
                create_sql_result.data,
            )
            if not table_result.is_success:
                return FlextResult.fail(f"Table creation failed: {table_result.error}")

            logger.info(f"Processed SCHEMA message for WMS stream: {stream_name}")

            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("WMS SCHEMA message processing failed")
            return FlextResult.fail(f"SCHEMA processing failed: {e}")

    def process_record_message(self, message: dict[str, Any]) -> FlextResult[None]:
        """Process Singer RECORD message."""
        try:
            if message.get("type") != "RECORD":
                return FlextResult.fail("Not a RECORD message")

            stream_name = message.get("stream")
            record = message.get("record")

            if not stream_name or not record:
                return FlextResult.fail(
                    "Invalid RECORD message: missing stream or record",
                )

            # Process record through stream processor
            process_result = self.stream_processor.process_record(stream_name, record)
            if not process_result.is_success:
                return FlextResult.fail(
                    f"Record processing failed: {process_result.error}",
                )

            transformed_record = process_result.data

            # Insert into Oracle (this could be batched for performance)
            insert_result = self._insert_record(stream_name, transformed_record)
            if not insert_result.is_success:
                return FlextResult.fail(
                    f"Record insertion failed: {insert_result.error}",
                )

            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("WMS RECORD message processing failed")
            return FlextResult.fail(f"RECORD processing failed: {e}")

    def process_state_message(self, message: dict[str, Any]) -> FlextResult[None]:
        """Process Singer STATE message."""
        try:
            if message.get("type") != "STATE":
                return FlextResult.fail("Not a STATE message")

            # Singer targets should output STATE messages to stdout
            # This allows for incremental processing resumption

            state_line = json.dumps(message)
            sys.stdout.write(state_line + "\n")
            sys.stdout.flush()

            logger.debug("Processed WMS STATE message")

            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("WMS STATE message processing failed")
            return FlextResult.fail(f"STATE processing failed: {e}")

    def _ensure_table_exists(
        self,
        table_name: str,
        schema_name: str,
        create_sql: str,
    ) -> FlextResult[None]:
        """Ensure Oracle WMS table exists."""
        try:
            # Check if table exists
            check_sql = """
                SELECT COUNT(*)
                FROM ALL_TABLES
                WHERE OWNER = UPPER(:schema_name)
                AND TABLE_NAME = UPPER(:table_name)
            """

            check_result = self.oracle_connection.execute_query(
                check_sql,
                {"schema_name": schema_name, "table_name": table_name},
            )

            if not check_result.is_success:
                return FlextResult.fail(
                    f"Table existence check failed: {check_result.error}",
                )

            table_exists = check_result.data and check_result.data[0][0] > 0

            if not table_exists:
                # Create table
                create_result = self.oracle_connection.execute_non_query(create_sql)
                if not create_result.is_success:
                    return FlextResult.fail(
                        f"Table creation failed: {create_result.error}",
                    )

                logger.info(f"Created Oracle WMS table: {schema_name}.{table_name}")
            else:
                logger.debug(
                    f"Oracle WMS table already exists: {schema_name}.{table_name}",
                )

            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception(f"WMS table management failed: {table_name}")
            return FlextResult.fail(f"Table management failed: {e}")

    def _insert_record(
        self,
        stream_name: str,
        record: dict[str, Any],
    ) -> FlextResult[None]:
        """Insert single record into Oracle WMS."""
        try:
            table_name = self.table_manager.generate_table_name(
                stream_name,
                self.table_prefix,
            )
            schema_name = self.oracle_connection.config.schema_name

            # Build INSERT SQL safely (schema and table names are controlled)

            columns = list(record.keys())
            quoted_columns = [f'"{col.upper()}"' for col in columns]
            placeholders = [f":{col.lower().lstrip('_')}" for col in columns]

            # Build parametrized INSERT SQL (safe - uses placeholders)
            insert_sql = (
                f'INSERT INTO "{schema_name.upper()}"."{table_name.upper()}" '
                f"({', '.join(quoted_columns)}) "
                f"VALUES ({', '.join(placeholders)})"
            )

            # Prepare parameters
            params = {}
            for col in columns:
                param_name = col.lower().lstrip("_")
                value = record[col]
                params[param_name] = str(value) if value is not None else ""

            # Execute insert
            insert_result = self.oracle_connection.execute_non_query(insert_sql, params)
            if not insert_result.is_success:
                return FlextResult.fail(f"Insert failed: {insert_result.error}")

            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception(f"WMS record insertion failed: {stream_name}")
            return FlextResult.fail(f"Record insertion failed: {e}")

    def finalize(self) -> FlextResult[dict[str, Any]]:
        """Finalize Oracle WMS Target processing."""
        try:
            # Get processing statistics
            stats_result = self.stream_processor.get_all_stats()
            if not stats_result.is_success:
                return FlextResult.fail(
                    f"Failed to get statistics: {stats_result.error}",
                )

            all_stats = stats_result.data

            # Calculate totals
            total_processed = sum(
                stats.records_processed for stats in all_stats.values()
            )
            total_success = sum(stats.records_success for stats in all_stats.values())
            total_failed = sum(stats.records_failed for stats in all_stats.values())

            summary = {
                "total_records_processed": total_processed,
                "total_records_success": total_success,
                "total_records_failed": total_failed,
                "success_rate": (total_success / total_processed * 100.0)
                if total_processed > 0
                else 0.0,
                "streams_processed": len(all_stats),
                "stream_stats": {
                    name: {
                        "processed": stats.records_processed,
                        "success": stats.records_success,
                        "failed": stats.records_failed,
                        "success_rate": stats.success_rate,
                    }
                    for name, stats in all_stats.items()
                },
            }

            logger.info(f"Oracle WMS Target finalized: {summary}")

            return FlextResult.ok(summary)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Oracle WMS Target finalization failed")
            return FlextResult.fail(f"Finalization failed: {e}")

    def cleanup(self) -> FlextResult[None]:
        """Cleanup Oracle WMS Target resources."""
        try:
            # Close Oracle connection
            disconnect_result = self.oracle_connection.disconnect()
            if not disconnect_result.is_success:
                logger.warning(
                    f"Oracle WMS disconnect failed: {disconnect_result.error}",
                )

            logger.info("Oracle WMS Target cleanup completed")

            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Oracle WMS Target cleanup failed")
            return FlextResult.fail(f"Cleanup failed: {e}")
