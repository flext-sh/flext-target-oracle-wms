"""Integration tests for target Oracle WMS lifecycle.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import pytest

from tests import c, tm, u


@pytest.mark.integration
class TestsFlextTargetOracleWmsOracle:
    """Integration tests for full target lifecycle.

    WMS-oracle integration: tests end-to-end target process_lines flow.
    """

    @staticmethod
    def test_setup_process_cleanup() -> None:
        """Test setup process cleanup."""
        tests = u.TargetOracleWms.Tests
        target = u.TargetOracleWms.Target(tests.valid_config())
        tm.ok(target.setup())
        lines = [
            tests.schema_msg("items").model_dump_json(by_alias=True),
            tests.record_msg(
                "items", {"id": c.ParserBooleanToken.ONE, "name": "Widget"}
            ).model_dump_json(),
            tests.state_msg({
                "bookmarks": {"items": c.ParserBooleanToken.ONE}
            }).model_dump_json(),
        ]
        tm.ok(target.process_lines(lines))
        tm.ok(target.cleanup())

    @staticmethod
    def test_multiple_batches() -> None:
        """Test multiple batches."""
        tests = u.TargetOracleWms.Tests
        target = u.TargetOracleWms.Target(tests.valid_config())
        target.setup()
        batch1 = [
            tests.schema_msg("orders", ["order_id"]).model_dump_json(by_alias=True),
            tests.record_msg("orders", {"order_id": "ORD001"}).model_dump_json(),
            tests.record_msg("orders", {"order_id": "ORD002"}).model_dump_json(),
        ]
        tm.ok(target.process_lines(batch1))
        batch2 = [
            tests.record_msg("orders", {"order_id": "ORD003"}).model_dump_json(),
            tests.state_msg({"bookmarks": {"orders": "3"}}).model_dump_json(),
        ]
        tm.ok(target.process_lines(batch2))
        tm.ok(target.cleanup())

    """Integration tests for multi-stream scenarios."""

    @staticmethod
    def test_three_streams_interleaved() -> None:
        """Test three streams interleaved."""
        tests = u.TargetOracleWms.Tests
        target = u.TargetOracleWms.Target(tests.valid_config())
        target.setup()
        streams = ("orders", "items", "tasks")
        lines = [
            *(tests.schema_msg(s).model_dump_json(by_alias=True) for s in streams),
            tests.record_msg("orders", {"id": "O1"}).model_dump_json(),
            tests.record_msg("items", {"id": "I1"}).model_dump_json(),
            tests.record_msg("tasks", {"id": "T1"}).model_dump_json(),
            tests.record_msg("orders", {"id": "O2"}).model_dump_json(),
            tests.state_msg().model_dump_json(),
        ]
        tm.ok(target.process_lines(lines))
        tm.ok(target.cleanup())
