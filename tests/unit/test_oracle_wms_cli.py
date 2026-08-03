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
from flext_tests import tm
from tests import c

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

    def test_default_attributes(self) -> None:
        cli = FlextTargetOracleWmsCli()
        tm.that(cli.name, eq="target-oracle-wms")
        tm.that(cli.description, eq="Oracle WMS Singer Target")
        tm.that(cli.version, eq=_pkg_version)

    def test_execute_with_config_file(self, tmp_path: Path) -> None:
        cli = FlextTargetOracleWmsCli()
        config_path = _write_config_file(_valid_config_json(), tmp_path)
        result = cli.execute(message_lines=[], settings=config_path)
        tm.ok(result)

    def test_execute_without_config_uses_defaults(self) -> None:
        cli = FlextTargetOracleWmsCli()
        result = cli.execute(message_lines=[])
        tm.ok(result)

    def test_execute_with_nonexistent_config_fails(self) -> None:
        cli = FlextTargetOracleWmsCli()
        with pytest.raises(FileNotFoundError):
            cli.execute(message_lines=[], settings="/nonexistent/settings.json")

    def test_execute_with_non_object_config_fails(self, tmp_path: Path) -> None:
        cli = FlextTargetOracleWmsCli()
        bad_path = _write_config_file("[1, 2, 3]", tmp_path)
        with pytest.raises(c.ValidationError):
            cli.execute(message_lines=[], settings=bad_path)

    def test_main_no_args_succeeds(self) -> None:
        main(argv=["target-oracle-wms"], message_lines=[])

    def test_main_with_config_arg(self, tmp_path: Path) -> None:
        config_path = _write_config_file(_valid_config_json(), tmp_path)
        main(argv=["target-oracle-wms", "--config", config_path], message_lines=[])

    def test_main_with_bad_config_raises(self) -> None:
        with pytest.raises(FileNotFoundError):
            main(
                argv=["target-oracle-wms", "--config", "/bad/path.json"],
                message_lines=[],
            )
