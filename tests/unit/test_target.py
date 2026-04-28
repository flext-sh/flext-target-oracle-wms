"""Tests for FlextTargetOracleWms runtime.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import (
    Mapping,
)

import pytest

from tests import c, m, t, u


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
    properties: Mapping[str, t.StrMapping] | None = None,
    key_properties: t.StrSequence | None = None,
) -> str:
    return str(
        _schema_msg(stream, properties, key_properties).model_dump_json(
            by_alias=True,
        ),
    )


def _record_line(
    stream: str = "test_stream",
    record: t.JsonMapping | None = None,
) -> str:
    return str(_record_msg(stream, record).model_dump_json())


def _state_line(state: t.JsonMapping | None = None) -> str:
    return str(_state_msg(state).model_dump_json())


def _schema_msg(
    stream: str = "test_stream",
    properties: Mapping[str, t.StrMapping] | None = None,
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
        assert target.name == "target-oracle-wms"
        assert target.settings is not None

    def test_init_with_invalid_config_raises(self) -> None:
        with pytest.raises(Exception):
            u.TargetOracleWms.Target({"bad": "settings"})

    def test_has_catalog_manager(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        assert target.catalog_manager is not None

    def test_has_stream_processor(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        assert target.stream_processor is not None

    def test_setup_returns_success(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        result = target.setup()
        assert result.success
        assert result.value is True

    def test_cleanup_returns_success(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        result = target.cleanup()
        assert result.success
        assert result.value is True

    def test_handle_schema_success(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        msg = _schema_msg("orders")
        result = target.handle_schema_message(msg)
        assert result.success

    def test_schema_registered_in_catalog(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        msg = _schema_msg("items")
        target.handle_schema_message(msg)
        assert target.catalog_manager.get_stream("items").success

    def test_record_without_schema_fails(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        msg = _record_msg("orphan", {"id": "1"})
        result = target.handle_record_message(msg)
        assert result.failure
        assert result.error is not None
        assert "schema not registered" in result.error.lower()

    def test_record_after_schema_succeeds(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        schema = _schema_msg("s")
        target.handle_schema_message(schema)
        record = _record_msg("s", {"id": "1"})
        result = target.handle_record_message(record)
        assert result.success

    def test_state_message_succeeds(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        msg = _state_msg({"bookmarks": {"pos": "42"}})
        result = target.handle_state_message(msg)
        assert result.success

    def test_empty_lines_succeeds(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        result = target.process_lines([])
        assert result.success

    def test_blank_lines_ignored(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        result = target.process_lines(["", "  ", "\n"])
        assert result.success

    def test_invalid_json_fails(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        result = target.process_lines(["not json"])
        assert result.failure
        assert result.error is not None
        assert "invalid json" in result.error.lower()

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
        assert result.success

    def test_record_before_schema_fails(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        lines = [_record_line("orders", {"id": "1"})]
        result = target.process_lines(lines)
        assert result.failure
