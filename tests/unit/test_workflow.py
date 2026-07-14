"""End-to-end workflow tests for target Oracle WMS.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import json as _stdlib_json

from flext_tests import tm

from flext_target_oracle_wms.cli import FlextTargetOracleWmsCli
from tests import t, u


def _valid_config() -> t.JsonMapping:
    return {
        "wms_auth": {
            "base_url": "https://test.wms.example.com",
            "username": "user",
            "password": "pass",
        },
    }


def _schema_line(
    stream: str,
    props: t.MappingKV[str, t.StrMapping],
    keys: t.StrSequence,
) -> str:
    _ = props
    return _stdlib_json.dumps({
        "type": "SCHEMA",
        "stream": stream,
        "schema": {"type": "object"},
        "key_properties": list(keys),
    })


def _record_line(stream: str, record: t.JsonMapping) -> str:
    return _stdlib_json.dumps({
        "type": "RECORD",
        "stream": stream,
        "record": dict(record),
    })


def _state_line(value: t.JsonMapping) -> str:
    return _stdlib_json.dumps({"type": "STATE", "value": dict(value)})


class TestsFlextTargetOracleWmsWorkflow:
    """End-to-end Singer SCHEMA → RECORD → STATE workflow."""

    def test_single_stream_workflow(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
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
        tm.ok(result)

    def test_multiple_stream_workflow(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        lines = [
            _schema_line("orders", {"order_id": {"type": "string"}}, ["order_id"]),
            _schema_line("items", {"item_id": {"type": "string"}}, ["item_id"]),
            _record_line("orders", {"order_id": "ORD001"}),
            _record_line("items", {"item_id": "ITEM001"}),
            _state_line({"bookmarks": {}}),
        ]
        result = target.process_lines(lines)
        tm.ok(result)

    def test_schema_update_mid_stream(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        lines = [
            _schema_line("s", {"id": {"type": "string"}}, ["id"]),
            _record_line("s", {"id": "1"}),
            _schema_line(
                "s",
                {"id": {"type": "string"}, "name": {"type": "string"}},
                ["id"],
            ),
            _record_line("s", {"id": "2", "name": "updated"}),
        ]
        result = target.process_lines(lines)
        tm.ok(result)

    def test_state_only_workflow(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        lines = [_state_line({"bookmarks": {}})]
        result = target.process_lines(lines)
        tm.ok(result)

    def test_cli_execute_empty_stdin(self) -> None:
        # NOTE (multi-agent, bead mro-nwc.19): inject empty message lines via the CLI's
        # public DI seam instead of patching sys.stdin (real behavior, no mock).
        cli = FlextTargetOracleWmsCli()
        result = cli.execute(message_lines=[])
        tm.ok(result)

    def test_cli_execute_with_messages(self) -> None:
        lines = [
            _schema_line("test", {"id": {"type": "string"}}, ["id"]),
            _record_line("test", {"id": "1"}),
            _state_line({"bookmarks": {}}),
        ]
        cli = FlextTargetOracleWmsCli()
        result = cli.execute(message_lines=lines)
        tm.ok(result)

    def test_malformed_json_stops_processing(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        lines = [
            _schema_line("s", {"id": {"type": "string"}}, ["id"]),
            "NOT VALID JSON",
        ]
        result = target.process_lines(lines)
        tm.fail(result)

    def test_record_for_unknown_stream_fails(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        lines = [_record_line("unknown_stream", {"id": "1"})]
        result = target.process_lines(lines)
        tm.fail(result)
