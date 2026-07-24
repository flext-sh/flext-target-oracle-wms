"""Integration tests for target Oracle WMS lifecycle.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import json as _stdlib_json
from typing import TYPE_CHECKING

import pytest

from flext_tests import tm
from tests import u

if TYPE_CHECKING:
    from tests import t


def _valid_config() -> t.JsonMapping:
    return {
        "wms_auth": {
            "base_url": "https://test.wms.example.com",
            "username": "user",
            "password": "pass",
        }
    }


def _schema_line(
    stream: str, props: t.MappingKV[str, t.StrMapping], keys: t.StrSequence
) -> str:
    return _stdlib_json.dumps({
        "type": "SCHEMA",
        "stream": stream,
        "schema": {"type": "object", "properties": dict(props)},
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


@pytest.mark.integration
class TestsFlextTargetOracleWmsOracle:
    """Integration tests for full target lifecycle."""

    def test_setup_process_cleanup(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        tm.ok(target.setup())
        lines = [
            _schema_line(
                "items", {"id": {"type": "string"}, "name": {"type": "string"}}, ["id"]
            ),
            _record_line("items", {"id": "1", "name": "Widget"}),
            _state_line({"bookmarks": {"items": "1"}}),
        ]
        tm.ok(target.process_lines(lines))
        tm.ok(target.cleanup())

    def test_multiple_batches(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        target.setup()
        batch1 = [
            _schema_line("orders", {"order_id": {"type": "string"}}, ["order_id"]),
            _record_line("orders", {"order_id": "ORD001"}),
            _record_line("orders", {"order_id": "ORD002"}),
        ]
        tm.ok(target.process_lines(batch1))
        batch2 = [
            _record_line("orders", {"order_id": "ORD003"}),
            _state_line({"bookmarks": {"orders": "3"}}),
        ]
        tm.ok(target.process_lines(batch2))
        tm.ok(target.cleanup())

    """Integration tests for multi-stream scenarios."""

    def test_three_streams_interleaved(self) -> None:
        target = u.TargetOracleWms.Target(_valid_config())
        target.setup()
        lines = [
            _schema_line("orders", {"id": {"type": "string"}}, ["id"]),
            _schema_line("items", {"id": {"type": "string"}}, ["id"]),
            _schema_line("tasks", {"id": {"type": "string"}}, ["id"]),
            _record_line("orders", {"id": "O1"}),
            _record_line("items", {"id": "I1"}),
            _record_line("tasks", {"id": "T1"}),
            _record_line("orders", {"id": "O2"}),
            _state_line({"bookmarks": {}}),
        ]
        tm.ok(target.process_lines(lines))
        tm.ok(target.cleanup())
