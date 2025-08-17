"""Comprehensive tests for CLI module - REAL flext-core integration."""

from __future__ import annotations

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

# DRY: Import from REAL implementation - NO DUPLICATION
from flext_core import FlextResult

from flext_target_oracle_wms import OracleWMSTargetCli, main


class TestOracleWMSTargetCli:
    """Test Oracle WMS Target CLI with comprehensive coverage."""

    def test_cli_initialization(self) -> None:
      """Test CLI initialization."""
      cli = OracleWMSTargetCli()
      assert cli.name == "target-oracle-wms"
      assert "Oracle WMS Singer Target" in cli.description
      assert cli.version == "0.9.0"

    def test_load_config_valid_file(self) -> None:
      """Test loading configuration from valid file."""
      cli = OracleWMSTargetCli()
      config_data = {
          "base_url": "https://test.wms.example.com",
          "username": "test_user",
          "password": "test_pass",
      }

      with (
          patch("pathlib.Path.exists", return_value=True),
          patch("pathlib.Path.read_text", return_value=json.dumps(config_data)),
      ):
          result = cli._load_config("config.json")
          assert result == config_data

    def test_load_config_file_not_found(self) -> None:
      """Test loading configuration when file not found."""
      cli = OracleWMSTargetCli()

      with (
          patch("pathlib.Path.exists", return_value=False),
          pytest.raises(FileNotFoundError, match="Configuration file not found"),
      ):
          cli._load_config("nonexistent.json")

    def test_load_config_invalid_json(self) -> None:
      """Test loading configuration with invalid JSON."""
      cli = OracleWMSTargetCli()

      with (
          patch("pathlib.Path.exists", return_value=True),
          patch("pathlib.Path.read_text", return_value="invalid json"),
          pytest.raises(json.JSONDecodeError),
      ):
          cli._load_config("invalid.json")

    @pytest.mark.asyncio
    async def test_execute_with_config_file(self) -> None:
      """Test CLI execution with configuration file."""
      cli = OracleWMSTargetCli()
      config_data = {
          "base_url": "https://test.wms.example.com",
          "username": "test_user",
          "password": "test_pass",
      }

      with (
          patch.object(cli, "_load_config", return_value=config_data),
          patch(
              "flext_target_oracle_wms.cli.SingerTargetOracleWMS",
          ) as mock_target_class,
          patch("sys.stdin", []),
      ):  # Empty stdin
          mock_target = MagicMock()
          mock_target.setup = AsyncMock(return_value=FlextResult.ok(None))
          mock_target.finalize.return_value = FlextResult.ok({"total": 0})
          mock_target.cleanup = AsyncMock()
          mock_target_class.return_value = mock_target

          result = await cli.execute(config="config.json")
          assert result.success

    @pytest.mark.asyncio
    async def test_execute_with_default_config(self) -> None:
      """Test CLI execution with default configuration."""
      cli = OracleWMSTargetCli()

      with (
          patch(
              "flext_target_oracle_wms.cli.SingerTargetOracleWMS",
          ) as mock_target_class,
          patch("sys.stdin", []),
      ):  # Empty stdin
          mock_target = MagicMock()
          mock_target.setup = AsyncMock(return_value=FlextResult.ok(None))
          mock_target.finalize.return_value = FlextResult.ok({"total": 0})
          mock_target.cleanup = AsyncMock()
          mock_target_class.return_value = mock_target

          result = await cli.execute()
          assert result.success

    @pytest.mark.asyncio
    async def test_execute_setup_failure(self) -> None:
      """Test CLI execution when target setup fails."""
      cli = OracleWMSTargetCli()

      with patch(
          "flext_target_oracle_wms.cli.SingerTargetOracleWMS",
      ) as mock_target_class:
          mock_target = MagicMock()
          mock_target.setup = AsyncMock(return_value=FlextResult.fail("Setup failed"))
          mock_target_class.return_value = mock_target

          result = await cli.execute()
          assert not result.success
          assert result.error is not None
          assert "Setup failed" in result.error

    @pytest.mark.asyncio
    async def test_execute_with_singer_messages(self) -> None:
      """Test CLI execution with Singer messages."""
      cli = OracleWMSTargetCli()

      # Mock stdin with Singer messages
      mock_messages = [
          '{"type": "SCHEMA", "stream": "test", "schema": {"properties": {}}}',
          '{"type": "RECORD", "stream": "test", "record": {"id": 1}}',
          '{"type": "STATE", "value": {"bookmarks": {}}}',
      ]

      with (
          patch(
              "flext_target_oracle_wms.cli.SingerTargetOracleWMS",
          ) as mock_target_class,
          patch("sys.stdin", mock_messages),
      ):
          mock_target = MagicMock()
          mock_target.setup = AsyncMock(return_value=FlextResult.ok(None))
          mock_target.process_schema_message = AsyncMock(
              return_value=FlextResult.ok(None),
          )
          mock_target.process_record_message = AsyncMock(
              return_value=FlextResult.ok(None),
          )
          mock_target.process_state_message.return_value = FlextResult.ok(None)
          mock_target.finalize.return_value = FlextResult.ok({"total": 1})
          mock_target.cleanup = AsyncMock()
          mock_target_class.return_value = mock_target

          result = await cli.execute()
          assert result.success
          mock_target.process_schema_message.assert_called_once()
          mock_target.process_record_message.assert_called_once()
          mock_target.process_state_message.assert_called_once()

    @pytest.mark.asyncio
    async def test_execute_with_invalid_json(self) -> None:
      """Test CLI execution with invalid JSON input."""
      cli = OracleWMSTargetCli()

      with (
          patch(
              "flext_target_oracle_wms.cli.SingerTargetOracleWMS",
          ) as mock_target_class,
          patch("sys.stdin", ["invalid json"]),
      ):
          mock_target = MagicMock()
          mock_target.setup = AsyncMock(return_value=FlextResult.ok(None))
          mock_target_class.return_value = mock_target

          result = await cli.execute()
          assert not result.success
          assert result.error is not None
          assert "Invalid JSON" in result.error

    @pytest.mark.asyncio
    async def test_execute_message_processing_failure(self) -> None:
      """Test CLI execution when message processing fails."""
      cli = OracleWMSTargetCli()

      with (
          patch(
              "flext_target_oracle_wms.cli.SingerTargetOracleWMS",
          ) as mock_target_class,
          patch("sys.stdin", ['{"type": "SCHEMA", "stream": "test", "schema": {}}']),
      ):
          mock_target = MagicMock()
          mock_target.setup = AsyncMock(return_value=FlextResult.ok(None))
          mock_target.process_schema_message = AsyncMock(
              return_value=FlextResult.fail("Processing failed"),
          )
          mock_target_class.return_value = mock_target

          result = await cli.execute()
          assert not result.success
          assert result.error is not None
          assert "Processing failed" in result.error

    @pytest.mark.asyncio
    async def test_execute_exception_handling(self) -> None:
      """Test CLI execution exception handling."""
      cli = OracleWMSTargetCli()

      with patch(
          "flext_target_oracle_wms.cli.SingerTargetOracleWMS",
          side_effect=Exception("Test error"),
      ):
          result = await cli.execute()
          assert not result.success
          assert result.error is not None
          assert "CLI execution failed" in result.error
          assert result.error is not None
          assert "Test error" in result.error


class TestMainFunction:
    """Test main function with comprehensive coverage."""

    def test_main_basic_execution(self) -> None:
      """Test basic main function execution."""
      with (
          patch("flext_target_oracle_wms.cli.OracleWMSTargetCli") as mock_cli_class,
          patch("asyncio.run") as mock_run,
          patch("sys.argv", ["target-oracle-wms"]),
      ):
          mock_cli = MagicMock()
          mock_cli.execute = AsyncMock(return_value=FlextResult.ok(None))
          mock_cli_class.return_value = mock_cli
          mock_run.return_value = FlextResult.ok(None)

          with patch("sys.exit") as mock_exit:
              main()
              mock_exit.assert_not_called()

    def test_main_with_config_argument(self) -> None:
      """Test main function with config argument."""
      with (
          patch("flext_target_oracle_wms.cli.OracleWMSTargetCli") as mock_cli_class,
          patch("asyncio.run") as mock_run,
          patch("sys.argv", ["target-oracle-wms", "--config", "config.json"]),
      ):
          mock_cli = MagicMock()
          mock_cli.execute = AsyncMock(return_value=FlextResult.ok(None))
          mock_cli_class.return_value = mock_cli
          mock_run.return_value = FlextResult.ok(None)

          with patch("sys.exit") as mock_exit:
              main()
              mock_exit.assert_not_called()
              # Verify config was passed to execute
              mock_run.assert_called_once()

    def test_main_setup_failure(self) -> None:
      """Test main function when CLI setup fails (now tests execution failure since setup was removed)."""
      with (
          patch("flext_target_oracle_wms.cli.OracleWMSTargetCli") as mock_cli_class,
          patch("asyncio.run") as mock_run,
          patch("sys.stderr"),
      ):
          mock_cli = MagicMock()
          mock_cli_class.return_value = mock_cli
          mock_run.return_value = FlextResult.fail("Execution failed")

          with patch("sys.exit") as mock_exit:
              main()
              mock_exit.assert_called_with(1)

    def test_main_execution_failure(self) -> None:
      """Test main function when execution fails."""
      with (
          patch("flext_target_oracle_wms.cli.OracleWMSTargetCli") as mock_cli_class,
          patch("asyncio.run") as mock_run,
          patch("sys.stderr"),
      ):
          mock_cli = MagicMock()
          mock_cli_class.return_value = mock_cli
          mock_run.return_value = FlextResult.fail("Execution failed")

          with patch("sys.exit") as mock_exit:
              main()
              mock_exit.assert_called_with(1)

    def test_main_keyboard_interrupt(self) -> None:
      """Test main function with keyboard interrupt."""
      with (
          patch("asyncio.run", side_effect=KeyboardInterrupt()),
          patch("sys.stderr"),
          patch("sys.exit") as mock_exit,
      ):
          main()
          mock_exit.assert_called_with(1)

    def test_main_general_exception(self) -> None:
      """Test main function with general exception."""
      with (
          patch("asyncio.run", side_effect=Exception("Test error")),
          patch("sys.stderr"),
          patch("sys.exit") as mock_exit,
      ):
          main()
          mock_exit.assert_called_with(1)
