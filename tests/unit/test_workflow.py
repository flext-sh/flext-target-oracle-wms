"""End-to-end workflow tests for target Oracle WMS.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import json as _stdlib_json
from typing import TYPE_CHECKING

from flext_tests import tm

from flext_target_oracle_wms.cli import FlextTargetOracleWmsCli
from tests import u
from tests._helpers import _valid_config

if TYPE_CHECKING:
    from tests import t


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

    @staticmethod
    def test_single_stream_workflow() -> None:
        """Test single stream workflow."""
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

    @staticmethod
    def test_multiple_stream_workflow() -> None:
        """Test multiple stream workflow."""
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

    @staticmethod
    def test_schema_update_mid_stream() -> None:
        """Test schema update mid stream."""
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

    @staticmethod
    def test_state_only_workflow() -> None:
        """Test state only workflow."""
        target = u.TargetOracleWms.Target(_valid_config())
        lines = [_state_line({"bookmarks": {}})]
        result = target.process_lines(lines)
        tm.ok(result)

    @staticmethod
    def test_cli_execute_empty_stdin() -> None:
        # NOTE (multi-agent, bead mro-nwc.19): inject empty message lines via the CLI's
        # public DI seam instead of patching sys.stdin (real behavior, no mock).
        """Test cli execute empty stdin."""
        cli = FlextTargetOracleWmsCli()
        result = cli.execute(message_lines=[])
        tm.ok(result)

    @staticmethod
    def test_cli_execute_with_messages() -> None:
        """Test cli execute with messages."""
        lines = [
            _schema_line("test", {"id": {"type": "string"}}, ["id"]),
            _record_line("test", {"id": "1"}),
            _state_line({"bookmarks": {}}),
        ]
        cli = FlextTargetOracleWmsCli()
        result = cli.execute(message_lines=lines)
        tm.ok(result)

    @staticmethod
    def test_malformed_json_stops_processing() -> None:
        """Test malformed json stops processing."""
        target = u.TargetOracleWms.Target(_valid_config())
        lines = [
            _schema_line("s", {"id": {"type": "string"}}, ["id"]),
            "NOT VALID JSON",
        ]
        result = target.process_lines(lines)
        tm.fail(result)

    @staticmethod
    def test_record_for_unknown_stream_fails() -> None:
        """Test record for unknown stream fails."""
        target = u.TargetOracleWms.Target(_valid_config())
        lines = [_record_line("unknown_stream", {"id": "1"})]
        result = target.process_lines(lines)
        tm.fail(result)
