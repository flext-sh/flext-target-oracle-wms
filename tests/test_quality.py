"""Production Quality Tests for flext-target-oracle-wms.

Validates production-ready implementation using real flext-oracle-wms API
without requiring actual Oracle WMS credentials.
"""

from __future__ import annotations

import json
import sys
import traceback

from flext_core import FlextTypes as t
from flext_oracle_wms import FlextOracleWmsSettings

from flext_target_oracle_wms.target_client import (
    SingerTargetOracleWMS,
    SingerWMSCatalogManager,
)
from flext_target_oracle_wms.target_models import (
    WMSDataTransformer,
    WMSTableManager,
    WMSTypeConverter,
)


def test_configuration_validation() -> bool | None:
    """Test configuration validation with production patterns."""
    try:
        # Test valid configuration
        valid_config = FlextOracleWmsSettings(
            base_url="https://invalid.wms.ocs.oraclecloud.com/company_unknow",
            username="test_user",
            password="test_pass",
            api_version="LGF_V10",
            timeout=30,
            retry_attempts=3,
            enable_ssl_verification=True,
        )

        # Test validation
        validation_result = valid_config.validate_config()
        if not validation_result.is_success:
            return False

        # Test invalid configurations (simplified)
        try:
            # Test empty base_url
            FlextOracleWmsSettings(base_url="")
            return False  # Should have failed
        except ValueError:
            pass

        try:
            # Test invalid timeout
            FlextOracleWmsSettings(timeout=0)
            return False  # Should have failed
        except ValueError:
            pass

        return True

    except Exception:
        return False


def test_singer_target_interfaces() -> bool | None:
    """Test Singer Target interfaces and error handling."""
    try:
        # Create target with test configuration

        config: dict[str, t.GeneralValueType] = {
            "base_url": "https://test.example.com/wms",
            "username": "test_user",
            "password": "test_pass",
            "environment": "test",
            "timeout": 30.0,
            "max_retries": 3,
        }

        target = SingerTargetOracleWMS(config)

        # Test that target can be created with valid config
        if not hasattr(target, "name") or not isinstance(target.name, str):
            return False

        return target.name == "target-oracle-wms"

    except Exception:
        return False


def test_data_transformation() -> bool | None:
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
            if not result.is_success:
                return False

            converted = result.data
            if singer_type == "object":
                # JSON string comparison
                if isinstance(converted, str) and json.loads(converted) != input_value:
                    return False
            elif converted != expected:
                return False

        # Test data transformer
        transformer = WMSDataTransformer()

        transform_result = transformer.transform_record({"id": 1, "name": "test"})
        if not transform_result.is_success:
            return False

        transformed = transform_result.data

        # Verify transformations
        expected_keys = ["USER_ID", "USER_NAME", "IS_ACTIVE", "SCORE", "METADATA"]
        return all(key in transformed for key in expected_keys)

    except Exception:
        return False


def test_table_management() -> bool | None:
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

        sql_result = manager.generate_create_table_sql(
            "TEST_TABLE",
            "TEST_SCHEMA",
            {"properties": {"id": {"type": "string"}}},
        )
        if not sql_result.is_success:
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
        if not insert_result.is_success:
            return False

        insert_sql = insert_result.data
        return bool(
            insert_sql and isinstance(insert_sql, str) and "INSERT" in insert_sql,
        )

    except Exception:
        return False


def test_catalog_management() -> bool | None:
    """Test catalog management patterns."""
    try:
        manager = SingerWMSCatalogManager()

        # Test adding streams

        # Test that catalog manager can be created and has required methods
        return hasattr(manager, "add_stream")

    except Exception:
        return False


def main() -> bool:
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
            result = test_func()
            if result:
                passed += 1
        except Exception:
            traceback.print_exc()

    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
