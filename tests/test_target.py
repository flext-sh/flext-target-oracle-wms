"""Tests for SingerTargetOracleWMS runtime.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence

import pytest
from flext_core import t

from flext_target_oracle_wms import m
from flext_target_oracle_wms.target_client import SingerTargetOracleWMS


def _valid_config() -> Mapping[str, t.ContainerValue]:
    return {
        "wms_auth": {
            "base_url": "https://test.wms.example.com",
            "username": "user",
            "password": "pass",
        }
    }


def _schema_line(
    stream: str = "test_stream",
    properties: Mapping[str, Mapping[str, str]] | None = None,
    key_properties: Sequence[str] | None = None,
) -> str:
    return _schema_msg(stream, properties, key_properties).model_dump_json(
        by_alias=True
    )


def _record_line(
    stream: str = "test_stream", record: Mapping[str, t.NormalizedValue] | None = None
) -> str:
    return _record_msg(stream, record).model_dump_json()


def _state_line(state: Mapping[str, t.NormalizedValue] | None = None) -> str:
    return _state_msg(state).model_dump_json()


def _schema_msg(
    stream: str = "test_stream",
    properties: Mapping[str, Mapping[str, str]] | None = None,
    key_properties: Sequence[str] | None = None,
) -> m.Meltano.SingerSchemaMessage:
    return m.Meltano.SingerSchemaMessage.model_validate({
        "type": "SCHEMA",
        "stream": stream,
        "schema": {
            "type": "object",
        },
        "key_properties": key_properties or ["id"],
    })


def _record_msg(
    stream: str = "test_stream", record: Mapping[str, t.NormalizedValue] | None = None
) -> m.Meltano.SingerRecordMessage:
    return m.Meltano.SingerRecordMessage.model_validate({
        "type": "RECORD",
        "stream": stream,
        "record": record or {"id": "1"},
    })


def _state_msg(
    state: Mapping[str, t.NormalizedValue] | None = None,
) -> m.Meltano.SingerStateMessage:
    return m.Meltano.SingerStateMessage.model_validate({
        "type": "STATE",
        "value": state or {"bookmarks": {}},
    })


class TestTargetInit:
    """Tests for SingerTargetOracleWMS initialization."""

    def test_init_with_valid_config(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        assert target.name == "target-oracle-wms"
        assert target.config is not None

    def test_init_with_invalid_config_raises(self) -> None:
        with pytest.raises(Exception):
            SingerTargetOracleWMS({"bad": "config"})

    def test_has_catalog_manager(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        assert target.catalog_manager is not None

    def test_has_stream_processor(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        assert target.stream_processor is not None


class TestTargetSetupCleanup:
    """Tests for setup/cleanup lifecycle."""

    def test_setup_returns_success(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        result = target.setup()
        assert result.is_success
        assert result.value is True

    def test_cleanup_returns_success(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        result = target.cleanup()
        assert result.is_success
        assert result.value is True


class TestTargetHandleSchemaMessage:
    """Tests for handle_schema_message."""

    def test_handle_schema_success(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        msg = _schema_msg("orders")
        result = target.handle_schema_message(msg)
        assert result.is_success

    def test_schema_registered_in_catalog(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        msg = _schema_msg("items")
        target.handle_schema_message(msg)
        assert target.catalog_manager.get_stream("items").is_success


class TestTargetHandleRecordMessage:
    """Tests for handle_record_message."""

    def test_record_without_schema_fails(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        msg = _record_msg("orphan", {"id": "1"})
        result = target.handle_record_message(msg)
        assert result.is_failure
        assert result.error is not None
        assert "schema not registered" in result.error.lower()

    def test_record_after_schema_succeeds(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        schema = _schema_msg("s")
        target.handle_schema_message(schema)
        record = _record_msg("s", {"id": "1"})
        result = target.handle_record_message(record)
        assert result.is_success


class TestTargetHandleStateMessage:
    """Tests for handle_state_message."""

    def test_state_message_succeeds(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        msg = _state_msg({"bookmarks": {"pos": "42"}})
        result = target.handle_state_message(msg)
        assert result.is_success


class TestTargetProcessLines:
    """Tests for process_lines."""

    def test_empty_lines_succeeds(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        result = target.process_lines([])
        assert result.is_success

    def test_blank_lines_ignored(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        result = target.process_lines(["", "  ", "\n"])
        assert result.is_success

    def test_invalid_json_fails(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        result = target.process_lines(["not json"])
        assert result.is_failure
        assert result.error is not None
        assert "invalid json" in result.error.lower()

    def test_schema_then_record_then_state(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        lines = [
            _schema_line(
                "orders", {"id": {"type": "string"}, "name": {"type": "string"}}
            ),
            _record_line("orders", {"id": "1", "name": "test"}),
            _state_line({"bookmarks": {"orders": "1"}}),
        ]
        result = target.process_lines(lines)
        assert result.is_success

    def test_record_before_schema_fails(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        lines = [_record_line("orders", {"id": "1"})]
        result = target.process_lines(lines)
        assert result.is_failure
