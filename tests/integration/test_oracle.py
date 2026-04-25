"""Integration tests for target Oracle WMS lifecycle.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import (
    Mapping,
)

import orjson
import pytest

from flext_target_oracle_wms import Target as FlextTargetOracleWms
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
    stream: str,
    props: Mapping[str, t.StrMapping],
    keys: t.StrSequence,
) -> str:
    return orjson.dumps({
        "type": "SCHEMA",
        "stream": stream,
        "schema": {"type": "object", "properties": props},
        "key_properties": keys,
    }).decode("utf-8")


def _record_line(stream: str, record: t.JsonMapping) -> str:
    return orjson.dumps({"type": "RECORD", "stream": stream, "record": record}).decode(
        "utf-8",
    )


def _state_line(value: t.JsonMapping) -> str:
    return orjson.dumps({"type": "STATE", "value": value}).decode("utf-8")


@pytest.mark.integration
class TestsFlextTargetOracleWmsOracle:
    """Integration tests for full target lifecycle."""

    def test_setup_process_cleanup(self) -> None:
        target = FlextTargetOracleWms(_valid_config())
        assert target.setup().success
        lines = [
            _schema_line(
                "items",
                {"id": {"type": "string"}, "name": {"type": "string"}},
                ["id"],
            ),
            _record_line("items", {"id": "1", "name": "Widget"}),
            _state_line({"bookmarks": {"items": "1"}}),
        ]
        assert target.process_lines(lines).success
        assert target.cleanup().success

    def test_multiple_batches(self) -> None:
        target = FlextTargetOracleWms(_valid_config())
        target.setup()
        batch1 = [
            _schema_line("orders", {"order_id": {"type": "string"}}, ["order_id"]),
            _record_line("orders", {"order_id": "ORD001"}),
            _record_line("orders", {"order_id": "ORD002"}),
        ]
        assert target.process_lines(batch1).success
        batch2 = [
            _record_line("orders", {"order_id": "ORD003"}),
            _state_line({"bookmarks": {"orders": "3"}}),
        ]
        assert target.process_lines(batch2).success
        assert target.cleanup().success

    """Integration tests for multi-stream scenarios."""

    def test_three_streams_interleaved(self) -> None:
        target = FlextTargetOracleWms(_valid_config())
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
        assert target.process_lines(lines).success
        assert target.cleanup().success
