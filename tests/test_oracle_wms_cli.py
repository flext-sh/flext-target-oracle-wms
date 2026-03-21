"""Tests for OracleWMSTargetCli and main().

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest
from pydantic import TypeAdapter, ValidationError

from flext_target_oracle_wms.cli import OracleWMSTargetCli, main


def _write_config_file(config: dict[str, dict[str, str]], tmp_path: Path) -> str:
    config_file = tmp_path / "config.json"
    config_file.write_text(
        TypeAdapter(dict[str, dict[str, str]]).dump_json(config).decode("utf-8"),
        encoding="utf-8",
    )
    return str(config_file)


def _valid_config_dict() -> dict[str, dict[str, str]]:
    return {
        "wms_auth": {
            "base_url": "https://test.wms.example.com",
            "username": "user",
            "password": "pass",
        }
    }


class TestOracleWMSTargetCliInit:
    """Tests for CLI initialization."""

    def test_default_attributes(self) -> None:
        cli = OracleWMSTargetCli()
        assert cli.name == "target-oracle-wms"
        assert cli.description == "Oracle WMS Singer Target"
        assert cli.version == "0.9.0"


class TestOracleWMSTargetCliLoadConfig:
    """Tests for _load_config."""

    def test_load_valid_config(self, tmp_path: Path) -> None:
        cli = OracleWMSTargetCli()
        config_path = _write_config_file(_valid_config_dict(), tmp_path)
        loaded = cli._load_config(config_path)
        assert "wms_auth" in loaded

    def test_load_nonexistent_file_raises(self) -> None:
        cli = OracleWMSTargetCli()
        with pytest.raises(FileNotFoundError):
            cli._load_config("/nonexistent/path/config.json")

    def test_load_non_object_json_raises(self, tmp_path: Path) -> None:
        cli = OracleWMSTargetCli()
        bad_file = tmp_path / "bad.json"
        bad_file.write_text(
            TypeAdapter(list[int]).dump_json([1, 2, 3]).decode("utf-8"),
            encoding="utf-8",
        )
        with pytest.raises(ValidationError):
            cli._prepare_config(str(bad_file))


class TestOracleWMSTargetCliExecute:
    """Tests for execute method."""

    @patch("flext_target_oracle_wms.cli.sys.stdin", [])
    def test_execute_with_config_file(self, tmp_path: Path) -> None:
        cli = OracleWMSTargetCli()
        config_path = _write_config_file(_valid_config_dict(), tmp_path)
        result = cli.execute(config=config_path)
        assert result.is_success

    @patch("flext_target_oracle_wms.cli.sys.stdin", [])
    def test_execute_without_config_uses_defaults(self) -> None:
        cli = OracleWMSTargetCli()
        result = cli.execute()
        assert result.is_success

    @patch("flext_target_oracle_wms.cli.sys.stdin", [])
    def test_execute_with_none_config(self) -> None:
        cli = OracleWMSTargetCli()
        result = cli.execute()
        assert result.is_success


class TestMain:
    """Tests for main() entry point."""

    @patch("flext_target_oracle_wms.cli.sys.stdin", [])
    @patch("flext_target_oracle_wms.cli.sys.argv", ["target-oracle-wms"])
    def test_main_no_args_succeeds(self) -> None:
        main()

    @patch("flext_target_oracle_wms.cli.sys.stdin", [])
    def test_main_with_config_arg(self, tmp_path: Path) -> None:
        config_path = _write_config_file(_valid_config_dict(), tmp_path)
        with patch(
            "flext_target_oracle_wms.cli.sys.argv",
            ["target-oracle-wms", "--config", config_path],
        ):
            main()

    @patch("flext_target_oracle_wms.cli.sys.stdin", [])
    @patch(
        "flext_target_oracle_wms.cli.sys.argv",
        ["target-oracle-wms", "--config", "/bad/path.json"],
    )
    def test_main_with_bad_config_raises(self) -> None:
        with pytest.raises(FileNotFoundError):
            main()
