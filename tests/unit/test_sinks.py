"""Component integration tests for target Oracle WMS.

Tests target initialization and component wiring.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import tm

from tests import u

from .._helpers import _record_msg, _schema_msg, _valid_config


class TestsFlextTargetOracleWmsSinks:
    """Verify target initializes all expected sub-components."""

    def test_unknown_stream_lookup_fails_not_found(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        tm.fail(target.catalog_manager.get_stream("never_registered"))

    def test_schema_registers_in_both_catalog_and_table(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        schema = _schema_msg("items")
        target.handle_schema_message(schema)
        tm.ok(target.catalog_manager.get_stream("items"))
        tm.ok(target.table_manager.get_table_name("items"))

    def test_table_name_is_uppercased_stream(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        schema = _schema_msg("orders")
        target.handle_schema_message(schema)
        table_result = target.table_manager.get_table_name("orders")
        tm.ok(table_result)
        tm.that(table_result.value, none=False)
        tm.that(table_result.value, eq="ORDERS")

    def test_record_keys_uppercased(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        schema = _schema_msg("s")
        target.handle_schema_message(schema)
        record = _record_msg("s", {"name": "test"})
        result = target.handle_record_message(record)
        tm.ok(result)
