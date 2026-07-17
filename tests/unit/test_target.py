"""Tests for FlextTargetOracleWms runtime.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from flext_tests import tm

from tests import c, m, u

if TYPE_CHECKING:
    from tests import t


def _valid_config() -> t.JsonMapping:
    return {
        "wms_auth": {
            "base_url": "https://test.wms.example.com",
            "username": "user",
            "password": "pass",
        },
    }


def _schema_line(
    stream: str = "test_stream",
    properties: t.MappingKV[str, t.StrMapping] | None = None,
    key_properties: t.StrSequence | None = None,
) -> str:
    json_line: str = _schema_msg(stream, properties, key_properties).model_dump_json(
        by_alias=True,
    )
    return json_line


def _record_line(
    stream: str = "test_stream",
    record: t.JsonMapping | None = None,
) -> str:
    json_line: str = _record_msg(stream, record).model_dump_json()
    return json_line


def _state_line(state: t.JsonMapping | None = None) -> str:
    json_line: str = _state_msg(state).model_dump_json()
    return json_line


def _schema_msg(
    stream: str = "test_stream",
    properties: t.MappingKV[str, t.StrMapping] | None = None,
    key_properties: t.StrSequence | None = None,
) -> m.Meltano.SingerSchemaMessage:
    _ = properties
    return m.Meltano.SingerSchemaMessage(
        type=c.Meltano.SingerMessageType.SCHEMA,
        stream=stream,
        schema_definition={
            "type": "object",
        },
        key_properties=key_properties or ["id"],
    )


def _record_msg(
    stream: str = "test_stream",
    record: t.JsonMapping | None = None,
) -> m.Meltano.SingerRecordMessage:
    return m.Meltano.SingerRecordMessage(
        type=c.Meltano.SingerMessageType.RECORD,
        stream=stream,
        record=record or {"id": "1"},
    )


def _state_msg(
    state: t.JsonMapping | None = None,
) -> m.Meltano.SingerStateMessage:
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
    """Tests for FlextTargetOracleWms initialization."""

    def test_init_with_valid_config(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        tm.that(target.name, eq="target-oracle-wms")
        tm.that(target.settings, none=False)

    def test_init_with_invalid_config_raises(self) -> None:
        with pytest.raises(Exception):
            u.TargetOracleWms.Target({"bad": "settings"})

    def test_invalid_load_method_rejected(self) -> None:
        # load_method is typed as the LoadMethods.Method enum, so an unknown value
        # is rejected at construction (data-shape validation lives in the model).
        with pytest.raises(c.ValidationError):
            m.TargetOracleWms.WmsTargetConfig.model_validate({
                **_valid_config(),
                "load_method": "BOGUS",
            })

    def test_valid_load_method_accepted(self) -> None:
        config = m.TargetOracleWms.WmsTargetConfig.model_validate({
            **_valid_config(),
            "load_method": c.TargetOracleWms.LoadMethods.Method.UPSERT,
        })
        tm.that(config.load_method, eq=c.TargetOracleWms.LoadMethods.Method.UPSERT)

    def test_has_catalog_manager(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        tm.that(target.catalog_manager, none=False)

    def test_has_stream_processor(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        tm.that(target.stream_processor, none=False)

    def test_setup_returns_success(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        result = target.setup()
        tm.ok(result)
        tm.that(result.value, eq=True)

    def test_cleanup_returns_success(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        result = target.cleanup()
        tm.ok(result)
        tm.that(result.value, eq=True)

    def test_handle_schema_success(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        msg = _schema_msg("orders")
        result = target.handle_schema_message(msg)
        tm.ok(result)

    def test_schema_registered_in_catalog(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        msg = _schema_msg("items")
        target.handle_schema_message(msg)
        tm.ok(target.catalog_manager.get_stream("items"))

    def test_record_without_schema_fails(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        msg = _record_msg("orphan", {"id": "1"})
        result = target.handle_record_message(msg)
        tm.fail(result)
        error = result.error
        assert error is not None
        tm.that(error.lower(), has="schema not registered")

    def test_record_after_schema_succeeds(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        schema = _schema_msg("s")
        target.handle_schema_message(schema)
        record = _record_msg("s", {"id": "1"})
        result = target.handle_record_message(record)
        tm.ok(result)

    def test_state_message_succeeds(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        msg = _state_msg({"bookmarks": {"pos": "42"}})
        result = target.handle_state_message(msg)
        tm.ok(result)

    def test_empty_lines_succeeds(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        result = target.process_lines([])
        tm.ok(result)

    def test_blank_lines_ignored(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        result = target.process_lines(["", "  ", "\n"])
        tm.ok(result)

    def test_invalid_json_fails(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        result = target.process_lines(["not json"])
        tm.fail(result)
        error = result.error
        assert error is not None
        tm.that(error.lower(), has="invalid json")

    def test_schema_then_record_then_state(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        lines = [
            _schema_line(
                "orders",
                {"id": {"type": "string"}, "name": {"type": "string"}},
            ),
            _record_line("orders", {"id": "1", "name": "test"}),
            _state_line({"bookmarks": {"orders": "1"}}),
        ]
        result = target.process_lines(lines)
        tm.ok(result)

    def test_record_before_schema_fails(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        lines = [_record_line("orders", {"id": "1"})]
        result = target.process_lines(lines)
        tm.fail(result)
