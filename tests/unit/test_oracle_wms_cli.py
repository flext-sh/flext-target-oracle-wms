"""Tests for FlextTargetOracleWmsCli and main().

Behavior-only: exercises the public CLI surface (``execute`` / ``main``) through
its dependency-injection seams (``message_lines`` / ``argv``). No mocking, no
patching, no private-method probing — real functionality on public interfaces.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from flext_target_oracle_wms import main
from flext_target_oracle_wms.__version__ import __version__ as _pkg_version
from flext_target_oracle_wms.cli import FlextTargetOracleWmsCli
from tests import c, tm

if TYPE_CHECKING:
    from pathlib import Path


def _valid_config_json() -> str:
    return (
        '{"wms_auth": {"base_url": "https://test.wms.example.com", '
        '"username": "user", "password": "pass"}}'
    )


def _write_config_file(config_json: str, tmp_path: Path) -> str:
    config_file = tmp_path / "settings.json"
    config_file.write_text(config_json, encoding="utf-8")
    return str(config_file)


class TestsFlextTargetOracleWmsOracleWmsCli:
    """Behavior contract for the target-oracle-wms CLI public surface."""

    @staticmethod
    def test_default_attributes() -> None:
        """Test default attributes."""
        cli = FlextTargetOracleWmsCli()
        tm.that(cli.name, eq="target-oracle-wms")
        tm.that(cli.description, eq="Oracle WMS Singer Target")
        tm.that(cli.version, eq=_pkg_version)

    @staticmethod
    def test_execute_with_config_file(tmp_path: Path) -> None:
        """Test execute with config file."""
        cli = FlextTargetOracleWmsCli()
        config_path = _write_config_file(_valid_config_json(), tmp_path)
        result = cli.execute(message_lines=[], settings=config_path)
        tm.ok(result)

    @staticmethod
    def test_execute_without_config_uses_defaults() -> None:
        """Test execute without config uses defaults."""
        cli = FlextTargetOracleWmsCli()
        result = cli.execute(message_lines=[])
        tm.ok(result)

    @staticmethod
    def test_execute_with_nonexistent_config_fails() -> None:
        """Test execute with nonexistent config fails."""
        cli = FlextTargetOracleWmsCli()
        with pytest.raises(FileNotFoundError):
            cli.execute(message_lines=[], settings="/nonexistent/settings.json")

    @staticmethod
    def test_execute_with_non_object_config_fails(tmp_path: Path) -> None:
        """Test execute with non object config fails."""
        cli = FlextTargetOracleWmsCli()
        bad_path = _write_config_file("[1, 2, 3]", tmp_path)
        with pytest.raises(c.ValidationError):
            cli.execute(message_lines=[], settings=bad_path)

    @staticmethod
    def test_main_no_args_succeeds() -> None:
        """Test main no args succeeds."""
        main(argv=["target-oracle-wms"], message_lines=[])

    @staticmethod
    def test_main_with_config_arg(tmp_path: Path) -> None:
        """Test main with config arg."""
        config_path = _write_config_file(_valid_config_json(), tmp_path)
        main(argv=["target-oracle-wms", "--config", config_path], message_lines=[])

    @staticmethod
    def test_main_with_bad_config_raises() -> None:
        """Test main with bad config raises."""
        with pytest.raises(FileNotFoundError):
            main(
                argv=["target-oracle-wms", "--config", "/bad/path.json"],
                message_lines=[],
            )
