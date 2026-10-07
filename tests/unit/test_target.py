"""Tests for FlextTargetOracleWms runtime.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from flext_tests import tm

from tests import c, m, u
from tests._helpers import _record_msg, _schema_msg, _valid_config

if TYPE_CHECKING:
    from tests import t


def _schema_line(
    stream: str,
    props: t.MappingKV[str, t.StrMapping],
    keys: t.StrSequence,
) -> str:
    message: m.Meltano.SingerSchemaMessage = (
        m.Meltano.SingerSchemaMessage.model_validate({
            "type": c.Meltano.SingerMessageType.SCHEMA,
            "stream": stream,
            "schema": {"type": "object", "properties": props},
            "key_properties": keys,
        })
    )
    return message.model_dump_json(by_alias=True)


def _record_line(
    stream: str = "test_stream",
    record: t.JsonMapping | None = None,
) -> str:
    json_line: str = _record_msg(stream, record).model_dump_json()
    return json_line


def _state_line(state: t.JsonMapping | None = None) -> str:
    json_line: str = _state_msg(state).model_dump_json()
    return json_line


def _state_msg(state: t.JsonMapping | None = None) -> m.Meltano.SingerStateMessage:
    empty_bookmarks: dict[str, t.JsonValue] = {}
    default_state: dict[str, t.JsonValue] = {"bookmarks": empty_bookmarks}
    resolved_state: dict[str, t.JsonValue] = (
        dict(state) if state is not None else default_state
    )
    state_message: m.Meltano.SingerStateMessage = (
        m.Meltano.SingerStateMessage.model_validate({
            "type": c.Meltano.SingerMessageType.STATE,
            "value": resolved_state,
        })
    )
    return state_message


class TestsFlextTargetOracleWmsTarget:
    """Tests for FlextTargetOracleWms initialization.

    WMS-specific: targets Oracle WMS singer protocol directly.
    """

    @staticmethod
    def test_init_with_valid_config() -> None:
        """Test init with valid config."""
        target = u.TargetOracleWms.Target(_valid_config())
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
                **_valid_config(),
                "load_method": "BOGUS",
            })

    @staticmethod
    def test_valid_load_method_accepted() -> None:
        """Test valid load method accepted."""
        config = m.TargetOracleWms.WmsTargetConfig.model_validate({
            **_valid_config(),
            "load_method": c.TargetOracleWms.LoadMethods.Method.UPSERT,
        })
        tm.that(config.load_method, eq=c.TargetOracleWms.LoadMethods.Method.UPSERT)

    @staticmethod
    def test_setup_returns_success() -> None:
        """Test setup returns success."""
        target = u.TargetOracleWms.Target(_valid_config())
        result = target.setup()
        tm.ok(result)
        tm.that(result.value, eq=True)

    @staticmethod
    def test_cleanup_returns_success() -> None:
        """Test cleanup returns success."""
        target = u.TargetOracleWms.Target(_valid_config())
        result = target.cleanup()
        tm.ok(result)
        tm.that(result.value, eq=True)

    @staticmethod
    def test_handle_schema_success() -> None:
        """Test handle schema success."""
        target = u.TargetOracleWms.Target(_valid_config())
        msg = _schema_msg("orders")
        result = target.handle_schema_message(msg)
        tm.ok(result)

    @staticmethod
    def test_schema_registered_in_catalog() -> None:
        """Test schema registered in catalog."""
        target = u.TargetOracleWms.Target(_valid_config())
        msg = _schema_msg("items")
        target.handle_schema_message(msg)
        tm.ok(target.catalog_manager.get_stream("items"))

    @staticmethod
    def test_record_without_schema_fails() -> None:
        """Test record without schema fails."""
        target = u.TargetOracleWms.Target(_valid_config())
        msg = _record_msg("orphan", {"id": "1"})
        result = target.handle_record_message(msg)
        tm.fail(result)
        tm.that((result.error or "").lower(), has="schema not registered")

    @staticmethod
    def test_record_after_schema_succeeds() -> None:
        """Test record after schema succeeds."""
        target = u.TargetOracleWms.Target(_valid_config())
        schema = _schema_msg("s")
        target.handle_schema_message(schema)
        record = _record_msg("s", {"id": "1"})
        result = target.handle_record_message(record)
        tm.ok(result)

    @staticmethod
    def test_state_message_succeeds() -> None:
        """Test state message succeeds."""
        target = u.TargetOracleWms.Target(_valid_config())
        msg = _state_msg({"bookmarks": {"pos": "42"}})
        result = target.handle_state_message(msg)
        tm.ok(result)

    @staticmethod
    def test_empty_lines_succeeds() -> None:
        """Test empty lines succeeds."""
        target = u.TargetOracleWms.Target(_valid_config())
        result = target.process_lines([])
        tm.ok(result)

    @staticmethod
    def test_blank_lines_ignored() -> None:
        """Test blank lines ignored."""
        target = u.TargetOracleWms.Target(_valid_config())
        result = target.process_lines(["", "  ", "\n"])
        tm.ok(result)

    @staticmethod
    def test_invalid_json_fails() -> None:
        """Test invalid json fails."""
        target = u.TargetOracleWms.Target(_valid_config())
        result = target.process_lines(["not json"])
        tm.fail(result)
        tm.that((result.error or "").lower(), has="invalid json")

    @staticmethod
    def test_schema_then_record_then_state() -> None:
        """Test schema then record then state."""
        target = u.TargetOracleWms.Target(_valid_config())
        lines = [
            _schema_line(
                "orders",
                {"id": {"type": "string"}, "name": {"type": "string"}},
                ["id"],
            ),
            _record_line("orders", {"id": "1", "name": "test"}),
            _state_line({"bookmarks": {"orders": "1"}}),
        ]
        result = target.process_lines(lines)
        tm.ok(result)

    @staticmethod
    def test_record_before_schema_fails() -> None:
        """Test record before schema fails."""
        target = u.TargetOracleWms.Target(_valid_config())
        lines = [_record_line("orders", {"id": "1"})]
        result = target.process_lines(lines)
        tm.fail(result)
