"""End-to-end workflow tests for target Oracle WMS.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_target_oracle_wms import FlextTargetOracleWmsCli
from tests import c, tm, u


class TestsFlextTargetOracleWmsWorkflow:
    """End-to-end Singer SCHEMA → RECORD → STATE workflow."""

    @staticmethod
    def test_single_stream_workflow() -> None:
        """Test single stream workflow."""
        tests = u.TargetOracleWms.Tests
        target = u.TargetOracleWms.Target(tests.valid_config())
        lines = [
            tests.schema_msg("inventory").model_dump_json(by_alias=True),
            tests.record_msg(
                "inventory", {"id": "ITEM001", "qty": 100}
            ).model_dump_json(),
            tests.record_msg(
                "inventory", {"id": "ITEM002", "qty": 50}
            ).model_dump_json(),
            tests.state_msg({"bookmarks": {"inventory": "2"}}).model_dump_json(),
        ]
        result = target.process_lines(lines)
        tm.ok(result)

    @staticmethod
    def test_schema_update_mid_stream() -> None:
        """Test schema update mid stream."""
        tests = u.TargetOracleWms.Tests
        target = u.TargetOracleWms.Target(tests.valid_config())
        lines = [
            tests.schema_msg("s").model_dump_json(by_alias=True),
            tests.record_msg("s", {"id": c.ParserBooleanToken.ONE}).model_dump_json(),
            tests.schema_msg("s").model_dump_json(by_alias=True),
            tests.record_msg("s", {"id": "2", "name": "updated"}).model_dump_json(),
        ]
        result = target.process_lines(lines)
        tm.ok(result)

    @staticmethod
    def test_state_only_workflow() -> None:
        """Test state only workflow."""
        tests = u.TargetOracleWms.Tests
        target = u.TargetOracleWms.Target(tests.valid_config())
        result = target.process_lines([tests.state_msg().model_dump_json()])
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
        tests = u.TargetOracleWms.Tests
        lines = [
            tests.schema_msg("test").model_dump_json(by_alias=True),
            tests.record_msg(
                "test", {"id": c.ParserBooleanToken.ONE}
            ).model_dump_json(),
            tests.state_msg().model_dump_json(),
        ]
        cli = FlextTargetOracleWmsCli()
        result = cli.execute(message_lines=lines)
        tm.ok(result)

    @staticmethod
    def test_malformed_json_stops_processing() -> None:
        """Test malformed json stops processing."""
        tests = u.TargetOracleWms.Tests
        target = u.TargetOracleWms.Target(tests.valid_config())
        lines = [
            tests.schema_msg("s").model_dump_json(by_alias=True),
            "NOT VALID JSON",
        ]
        result = target.process_lines(lines)
        tm.fail(result)

    @staticmethod
    def test_record_for_unknown_stream_fails() -> None:
        """Test record for unknown stream fails."""
        tests = u.TargetOracleWms.Tests
        target = u.TargetOracleWms.Target(tests.valid_config())
        lines = [
            tests.record_msg(
                "unknown_stream", {"id": c.ParserBooleanToken.ONE}
            ).model_dump_json(),
        ]
        result = target.process_lines(lines)
        tm.fail(result)
