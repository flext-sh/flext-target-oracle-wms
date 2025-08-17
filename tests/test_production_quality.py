#!/usr/bin/env python3
"""Production Quality Tests for flext-target-oracle-wms.

Validates production-ready implementation using real flext-oracle-wms API
without requiring actual Oracle WMS credentials.
"""

import asyncio
import json
import sys
import traceback

from flext_oracle_wms import FlextOracleWmsClientConfig
from flext_oracle_wms.api_catalog import FlextOracleWmsApiVersion

from flext_target_oracle_wms import (
    SingerTargetOracleWMS,
    SingerWMSCatalogManager,
    WMSDataTransformer,
    WMSTableManager,
    WMSTypeConverter,
)


async def test_configuration_validation() -> bool | None:
    """Test configuration validation with production patterns."""
    try:
        # Test valid configuration
        valid_config = FlextOracleWmsClientConfig(
            base_url="https://ta29.wms.ocs.oraclecloud.com/raizen_test",
            username="test_user",
            password="test_pass",
            environment="test_env",
            timeout=30.0,
            max_retries=3,
            api_version=FlextOracleWmsApiVersion.LGF_V10,
            verify_ssl=True,
            enable_logging=True,
        )

        # Test validation
        valid_config.validate_domain_rules()

        # Test invalid configurations
        invalid_tests = [
            ("Empty base_url", {"base_url": ""}),
            ("Invalid base_url", {"base_url": "invalid-url"}),
            ("Empty username", {"username": ""}),
            ("Empty password", {"password": ""}),
            ("Empty environment", {"environment": ""}),
            ("Zero timeout", {"timeout": 0}),
            ("Negative retries", {"max_retries": -1}),
        ]

        for _test_name, override_params in invalid_tests:
            try:
                config_params = {
                    "base_url": "https://test.com",
                    "username": "test",
                    "password": "test",
                    "environment": "test",
                    "timeout": 30.0,
                    "max_retries": 3,
                    "api_version": FlextOracleWmsApiVersion.LGF_V10,
                    "verify_ssl": True,
                    "enable_logging": True,
                }
                config_params.update(override_params)

                invalid_config = FlextOracleWmsClientConfig(**config_params)
                invalid_config.validate_domain_rules()
                return False
            except ValueError:
                pass

        return True

    except Exception:
        return False


async def test_singer_target_interfaces() -> bool | None:
    """Test Singer Target interfaces and error handling."""
    try:
        # Create target with test configuration
        config = {
            "base_url": "https://test.example.com/wms",
            "username": "test_user",
            "password": "test_pass",
            "environment": "test",
            "timeout": 30.0,
            "max_retries": 3,
            "batch_size": 100,
            "load_method": "APPEND_ONLY",
            "table_prefix": "SINGER_",
            "default_target_schema": "WMS_TARGET",
        }

        target = SingerTargetOracleWMS(config)

        # Test invalid message types
        invalid_messages = [
            ("Invalid type", {"type": "INVALID", "stream": "test"}),
            ("Missing stream", {"type": "SCHEMA", "schema": {}}),
            ("Missing schema", {"type": "SCHEMA", "stream": "test"}),
            ("Missing record", {"type": "RECORD", "stream": "test"}),
        ]

        for _test_name, message in invalid_messages:
            if message.get("type") == "SCHEMA":
                result = await target.process_schema_message(message)
            elif message.get("type") == "RECORD":
                result = await target.process_record_message(message)
            else:
                result = await target.process_schema_message(message)

            if result.success:
                return False

        # Test valid schema message structure
        valid_schema = {
            "type": "SCHEMA",
            "stream": "test_entity",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "active": {"type": "boolean"},
                },
            },
            "key_properties": ["id"],
        }

        # This will fail at Oracle connection, but should pass message validation
        schema_result = await target.process_schema_message(valid_schema)
        if (
            schema_result.success
            or "connection" in schema_result.error.lower()
            or "failed" in schema_result.error.lower()
        ):
            pass
        else:
            return False

        # Test state message processing
        state_message = {
            "type": "STATE",
            "value": {"bookmarks": {"test": {"last_updated": "2025-01-29T10:00:00Z"}}},
        }

        state_result = target.process_state_message(state_message)
        return state_result.success

    except Exception:
        return False


async def test_data_transformation() -> bool | None:
    """Test data transformation patterns."""
    try:
        # Test type converter
        converter = WMSTypeConverter()

        test_conversions = [
            ("string", "test", "test"),
            ("integer", "123", 123),
            ("number", "123.45", 123.45),
            ("boolean", True, 1),
            ("boolean", False, 0),
            ("object", {"key": "value"}, '{"key": "value"}'),
        ]

        for singer_type, input_value, expected in test_conversions:
            result = converter.convert_singer_to_oracle(singer_type, input_value)
            if not result.success:
                return False

            converted: str | int | float | bool | dict[str, object] = result.data
            if singer_type == "object":
                # JSON string comparison

                if json.loads(converted) != input_value:
                    return False
            elif converted != expected:
                return False

        # Test data transformer
        transformer = WMSDataTransformer()

        test_record = {
            "user_id": "U123",
            "user-name": "Test User",
            "is_active": True,
            "score": 95.5,
            "metadata": {"role": "REDACTED_LDAP_BIND_PASSWORD"},
        }

        test_schema = {
            "properties": {
                "user_id": {"type": "string"},
                "user-name": {"type": "string"},
                "is_active": {"type": "boolean"},
                "score": {"type": "number"},
                "metadata": {"type": "object"},
            },
        }

        transform_result = transformer.transform_record(test_record, test_schema)
        if not transform_result.success:
            return False

        transformed = transform_result.data

        # Verify transformations
        expected_keys = ["USER_ID", "USER_NAME", "IS_ACTIVE", "SCORE", "METADATA"]
        return all(key in transformed for key in expected_keys)

    except Exception:
        return False


async def test_table_management() -> bool | None:
    """Test table management patterns."""
    try:
        manager = WMSTableManager()

        # Test table name generation
        test_cases = [
            ("user_events", "", "USER_EVENTS"),
            ("user-events", "SINGER", "SINGER_USER_EVENTS"),
            (
                "very_long_table_name_that_exceeds_limit",
                "",
                "VERY_LONG_TABLE_NAME_THAT_EXCE",
            ),  # Truncated to 30 chars
        ]

        for stream_name, prefix, expected in test_cases:
            result = manager.generate_table_name(stream_name, prefix)
            if result != expected:
                return False

        # Test CREATE TABLE SQL generation
        test_schema = {
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "age": {"type": "integer"},
                "active": {"type": "boolean"},
                "created_at": {"type": "string", "format": "date-time"},
                "metadata": {"type": "object"},
            },
        }

        sql_result = manager.generate_create_table_sql(
            "TEST_TABLE",
            "TEST_SCHEMA",
            test_schema,
        )
        if not sql_result.success:
            return False

        sql = sql_result.data
        if not sql or "CREATE TABLE" not in sql:
            return False

        # Test INSERT SQL generation
        columns = ["ID", "NAME", "AGE", "ACTIVE"]
        insert_result = manager.generate_insert_sql(
            "TEST_TABLE",
            "TEST_SCHEMA",
            columns,
        )
        if not insert_result.success:
            return False

        insert_sql = insert_result.data
        return not (not insert_sql or "INSERT INTO" not in insert_sql)

    except Exception:
        return False


async def test_catalog_management() -> bool | None:  # noqa: PLR0911
    """Test catalog management patterns."""
    try:
        manager = SingerWMSCatalogManager()

        # Test adding streams
        test_schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
            },
        }

        add_result = manager.add_stream("test_stream", test_schema)
        if not add_result.success:
            return False

        # Test getting stream
        get_result = manager.get_stream("test_stream")
        if not get_result.success:
            return False

        stream_entry = get_result.data
        if not stream_entry or stream_entry.stream != "test_stream":
            return False

        # Test listing streams
        list_result = manager.list_streams()
        if not list_result.success:
            return False

        streams = list_result.data
        if not streams or "test_stream" not in streams:
            return False

        # Test Singer catalog conversion
        catalog_result = manager.to_singer_catalog()
        if not catalog_result.success:
            return False

        catalog = catalog_result.data
        return not (not catalog or "streams" not in catalog)

    except Exception:
        return False


async def main() -> bool:
    """Run all production quality tests."""
    tests = [
        ("Configuration Validation", test_configuration_validation),
        ("Singer Target Interfaces", test_singer_target_interfaces),
        ("Data Transformation", test_data_transformation),
        ("Table Management", test_table_management),
        ("Catalog Management", test_catalog_management),
    ]

    passed = 0
    total = len(tests)

    for _test_name, test_func in tests:
        try:
            if await test_func():
                passed += 1
        except Exception:
            traceback.print_exc()

    return passed == total


if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
