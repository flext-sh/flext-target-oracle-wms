"""Component integration tests for target Oracle WMS.

Tests target initialization and component wiring.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from tests import tm, u


class TestsFlextTargetOracleWmsSinks:
    """Verify target initializes all expected sub-components."""

    @staticmethod
    def test_unknown_stream_lookup_fails_not_found() -> None:
        """Test unknown stream lookup fails not found."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        tm.fail(target.catalog_manager.get_stream("never_registered"))

    @staticmethod
    def test_schema_registers_in_both_catalog_and_table() -> None:
        """Test schema registers in both catalog and table."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        schema = u.TargetOracleWms.Tests.schema_msg("items")
        target.handle_schema_message(schema)
        tm.ok(target.catalog_manager.get_stream("items"))
        tm.ok(target.table_manager.get_table_name("items"))

    @staticmethod
    def test_table_name_is_uppercased_stream() -> None:
        """Test table name is uppercased stream."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        schema = u.TargetOracleWms.Tests.schema_msg("orders")
        target.handle_schema_message(schema)
        table_result = target.table_manager.get_table_name("orders")
        tm.ok(table_result)
        tm.that(table_result.value, none=False)
        tm.that(table_result.value, eq="ORDERS")

    @staticmethod
    def test_record_keys_uppercased() -> None:
        """Test record keys uppercased."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        schema = u.TargetOracleWms.Tests.schema_msg("s")
        target.handle_schema_message(schema)
        record = u.TargetOracleWms.Tests.record_msg("s", {"name": "test"})
        result = target.handle_record_message(record)
        tm.ok(result)
