"""End-to-end workflow tests for target Oracle WMS.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from flext_core.typings import t
from pydantic import TypeAdapter

from flext_target_oracle_wms.cli import OracleWMSTargetCli
from flext_target_oracle_wms.target_client import SingerTargetOracleWMS


def _valid_config() -> dict[str, t.ContainerValue]:
    return {
        "wms_auth": {
            "base_url": "https://test.wms.example.com",
            "username": "user",
            "password": "pass",
        }
    }


def _schema_line(stream: str, props: dict[str, dict[str, str]], keys: list[str]) -> str:
    return (
        TypeAdapter(t.NormalizedValue)
        .dump_json({
            "type": "SCHEMA",
            "stream": stream,
            "schema": {"type": "t.NormalizedValue", "properties": props},
            "key_properties": keys,
        })
        .decode("utf-8")
    )


def _record_line(stream: str, record: dict[str, t.NormalizedValue]) -> str:
    return (
        TypeAdapter(t.NormalizedValue)
        .dump_json({"type": "RECORD", "stream": stream, "record": record})
        .decode("utf-8")
    )


def _state_line(value: dict[str, t.NormalizedValue]) -> str:
    return (
        TypeAdapter(t.NormalizedValue)
        .dump_json({"type": "STATE", "value": value})
        .decode("utf-8")
    )


class TestFullSingerWorkflow:
    """End-to-end Singer SCHEMA → RECORD → STATE workflow."""

    def test_single_stream_workflow(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        lines = [
            _schema_line(
                "inventory",
                {"id": {"type": "string"}, "qty": {"type": "integer"}},
                ["id"],
            ),
            _record_line("inventory", {"id": "ITEM001", "qty": 100}),
            _record_line("inventory", {"id": "ITEM002", "qty": 50}),
            _state_line({"bookmarks": {"inventory": "2"}}),
        ]
        result = target.process_lines(lines)
        assert result.is_success

    def test_multiple_stream_workflow(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        lines = [
            _schema_line("orders", {"order_id": {"type": "string"}}, ["order_id"]),
            _schema_line("items", {"item_id": {"type": "string"}}, ["item_id"]),
            _record_line("orders", {"order_id": "ORD001"}),
            _record_line("items", {"item_id": "ITEM001"}),
            _state_line({"bookmarks": {}}),
        ]
        result = target.process_lines(lines)
        assert result.is_success

    def test_schema_update_mid_stream(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        lines = [
            _schema_line("s", {"id": {"type": "string"}}, ["id"]),
            _record_line("s", {"id": "1"}),
            _schema_line(
                "s", {"id": {"type": "string"}, "name": {"type": "string"}}, ["id"]
            ),
            _record_line("s", {"id": "2", "name": "updated"}),
        ]
        result = target.process_lines(lines)
        assert result.is_success

    def test_state_only_workflow(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        lines = [_state_line({"bookmarks": {}})]
        result = target.process_lines(lines)
        assert result.is_success


class TestCliWorkflow:
    """End-to-end CLI execution workflow."""

    @patch("flext_target_oracle_wms.cli.sys.stdin", [])
    def test_cli_execute_empty_stdin(self) -> None:
        cli = OracleWMSTargetCli()
        result = cli.execute()
        assert result.is_success

    @patch("flext_target_oracle_wms.cli.sys.stdin")
    def test_cli_execute_with_messages(self, mock_stdin: MagicMock) -> None:
        lines = [
            _schema_line("test", {"id": {"type": "string"}}, ["id"]) + "\n",
            _record_line("test", {"id": "1"}) + "\n",
            _state_line({"bookmarks": {}}) + "\n",
        ]
        mock_stdin.__iter__ = MagicMock(return_value=iter(lines))
        mock_stdin.__next__ = MagicMock(side_effect=lines)
        cli = OracleWMSTargetCli()
        result = cli.execute()
        assert result.is_success


class TestErrorWorkflows:
    """Tests for error handling in workflows."""

    def test_malformed_json_stops_processing(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        lines = [
            _schema_line("s", {"id": {"type": "string"}}, ["id"]),
            "NOT VALID JSON",
        ]
        result = target.process_lines(lines)
        assert result.is_failure

    def test_record_for_unknown_stream_fails(self) -> None:
        target = SingerTargetOracleWMS(_valid_config())
        lines = [_record_line("unknown_stream", {"id": "1"})]
        result = target.process_lines(lines)
        assert result.is_failure
