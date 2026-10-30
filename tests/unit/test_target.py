"""Tests for FlextTargetOracleWms runtime.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import pytest

from tests import c, m, tm, u


class TestsFlextTargetOracleWmsTarget:
    """Tests for FlextTargetOracleWms initialization.

    WMS-specific: targets Oracle WMS singer protocol directly.
    """

    @staticmethod
    def test_init_with_valid_config() -> None:
        """Test init with valid config."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        tm.that(target.name, eq=c.TargetOracleWms.TARGET_NAME)
        tm.that(target.settings, none=False)

    @staticmethod
    def test_init_with_invalid_config_raises() -> None:
        """Test init with invalid config raises."""
        with pytest.raises(c.ValidationError):
            u.TargetOracleWms.Target({"bad": "settings"})

    @staticmethod
    def test_invalid_load_method_rejected() -> None:
        # load_method is typed as the LoadMethods.Method enum, so an unknown value
        # is rejected at construction (data-shape validation lives in the model).
        """Test invalid load method rejected."""
        with pytest.raises(c.ValidationError):
            m.TargetOracleWms.WmsTargetConfig.model_validate({
                **u.TargetOracleWms.Tests.valid_config(),
                "load_method": "BOGUS",
            })

    @staticmethod
    def test_valid_load_method_accepted() -> None:
        """Test valid load method accepted."""
        config = m.TargetOracleWms.WmsTargetConfig.model_validate({
            **u.TargetOracleWms.Tests.valid_config(),
            "load_method": c.TargetOracleWms.LoadMethods.Method.UPSERT,
        })
        tm.that(config.load_method, eq=c.TargetOracleWms.LoadMethods.Method.UPSERT)

    @staticmethod
    def test_setup_returns_success() -> None:
        """Test setup returns success."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        result = target.setup()
        tm.ok(result)
        tm.ok(result.value)

    @staticmethod
    def test_cleanup_returns_success() -> None:
        """Test cleanup returns success."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        result = target.cleanup()
        tm.ok(result)
        tm.ok(result.value)

    @staticmethod
    def test_handle_schema_success() -> None:
        """Test handle schema success."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        msg = u.TargetOracleWms.Tests.schema_msg("orders")
        result = target.handle_schema_message(msg)
        tm.ok(result)

    @staticmethod
    def test_schema_registered_in_catalog() -> None:
        """Test schema registered in catalog."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        msg = u.TargetOracleWms.Tests.schema_msg("items")
        target.handle_schema_message(msg)
        tm.ok(target.catalog_manager.get_stream("items"))

    @staticmethod
    def test_record_without_schema_fails() -> None:
        """Test record without schema fails."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        msg = u.TargetOracleWms.Tests.record_msg(
            "orphan", {"id": c.ParserBooleanToken.ONE}
        )
        result = target.handle_record_message(msg)
        tm.fail(result)
        tm.that((result.error or "").lower(), has="schema not registered")

    @staticmethod
    def test_record_after_schema_succeeds() -> None:
        """Test record after schema succeeds."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        schema = u.TargetOracleWms.Tests.schema_msg("s")
        target.handle_schema_message(schema)
        record = u.TargetOracleWms.Tests.record_msg(
            "s", {"id": c.ParserBooleanToken.ONE}
        )
        result = target.handle_record_message(record)
        tm.ok(result)

    @staticmethod
    def test_state_message_succeeds() -> None:
        """Test state message succeeds."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        msg = u.TargetOracleWms.Tests.state_msg({"bookmarks": {"pos": "42"}})
        result = target.handle_state_message(msg)
        tm.ok(result)

    @staticmethod
    def test_empty_lines_succeeds() -> None:
        """Test empty lines succeeds."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        result = target.process_lines([])
        tm.ok(result)

    @staticmethod
    def test_blank_lines_ignored() -> None:
        """Test blank lines ignored."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        result = target.process_lines(["", "  ", "\n"])
        tm.ok(result)

    @staticmethod
    def test_invalid_json_fails() -> None:
        """Test invalid json fails."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        result = target.process_lines(["not json"])
        tm.fail(result)
        tm.that((result.error or "").lower(), has="invalid json")

    @staticmethod
    def test_schema_then_record_then_state() -> None:
        """Test schema then record then state."""
        tests = u.TargetOracleWms.Tests
        target = u.TargetOracleWms.Target(tests.valid_config())
        lines = [
            tests.schema_msg("orders").model_dump_json(by_alias=True),
            tests.record_msg(
                "orders", {"id": c.ParserBooleanToken.ONE, "name": "test"}
            ).model_dump_json(),
            tests.state_msg({
                "bookmarks": {"orders": c.ParserBooleanToken.ONE}
            }).model_dump_json(),
        ]
        result = target.process_lines(lines)
        tm.ok(result)

    @staticmethod
    def test_record_before_schema_fails() -> None:
        """Test record before schema fails."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        lines = [
            u.TargetOracleWms.Tests.record_msg(
                "orders", {"id": c.ParserBooleanToken.ONE}
            ).model_dump_json(),
        ]
        result = target.process_lines(lines)
        tm.fail(result)
