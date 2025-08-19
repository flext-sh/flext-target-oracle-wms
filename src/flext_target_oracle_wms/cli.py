"""CLI entry point - REAL implementation using available flext-cli patterns."""

from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

# Removed Any import - using specific types from flext-core
# DRY: Use only essential imports - avoid CLISettings env var conflicts
from flext_core import FlextResult

# DRY: Use ONLY the production-ready implementation
from flext_target_oracle_wms.target_client import SingerTargetOracleWMS


class OracleWMSTargetCli:
    """Oracle WMS Target CLI using REAL flext-cli patterns - NO DUPLICATION."""

    def __init__(self) -> None:
        """Initialize CLI with real flext-cli patterns."""
        self.name = "target-oracle-wms"
        self.description = "Oracle WMS Singer Target - Production Ready using REAL flext-oracle-wms API"
        self.version = "0.9.0"

    async def execute(self, **kwargs: object) -> FlextResult[None]:
        """Execute target using REAL implementation - NO DUPLICATION.

        SOLID REFACTORING: Reduced multiple returns (count=6) to single exit point
        using Railway-Oriented Programming pattern.
        """
        result: FlextResult[None] = FlextResult[None].ok(None)

        try:
            # Load configuration
            config_path = kwargs.get("config")
            config_path_str = str(config_path) if config_path is not None else None
            config_result = self._prepare_config(config_path_str)
            if not config_result.success:
                result = FlextResult[None].fail(config_result.error or "Configuration failed")
            else:
                config = config_result.data
                if config is None:
                    result = FlextResult[None].fail("Configuration data is None")
                else:
                    # Continue with target setup and processing
                    result = await self._execute_target_pipeline(config)

        except Exception as e:
            result = FlextResult[None].fail(f"CLI execution failed: {e}")

        return result

    async def _execute_target_pipeline(
        self,
        config: dict[str, object],
    ) -> FlextResult[None]:
        """Execute the target pipeline with railway-oriented programming.

        SOLID REFACTORING: Extract target pipeline execution to reduce complexity.
        """
        target = SingerTargetOracleWMS(config)

        # Setup target
        setup_result = await target.setup()
        if not setup_result.success:
            return FlextResult[None].fail(f"Setup failed: {setup_result.error}")

        # Process messages
        process_result = await self._process_stdin_messages(target)
        if not process_result.success:
            return process_result

        # Finalize and cleanup
        return await self._finalize_target(target)

    def _prepare_config(
        self,
        config_path: str | None,
    ) -> FlextResult[dict[str, object]]:
        """Prepare configuration from path or defaults."""
        try:
            if config_path:
                return FlextResult[None].ok(self._load_config(config_path))

            # Default configuration
            config = {
                "base_url": "https://ta29.wms.ocs.oraclecloud.com",
                "username": "oracle",
                "password": "oracle",
                "environment": "default",
                "timeout": 30.0,
                "max_retries": 3,
            }
            return FlextResult[None].ok(config)
        except Exception as e:
            return FlextResult[None].fail(f"Configuration preparation failed: {e}")

    async def _process_stdin_messages(
        self,
        target: SingerTargetOracleWMS,
    ) -> FlextResult[None]:
        """Process stdin messages following Singer protocol."""
        try:
            for raw_line in sys.stdin:
                line = raw_line.strip()
                if not line:
                    continue

                result = await self._process_single_message(target, line)
                if not result.success:
                    return result

            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Message processing failed: {e}")

    async def _process_single_message(
        self,
        target: SingerTargetOracleWMS,
        line: str,
    ) -> FlextResult[None]:
        """Process a single Singer message."""
        try:
            message = json.loads(line)
            message_type = message.get("type")

            if message_type == "SCHEMA":
                target._handle_schema_message(message)
                return FlextResult[None].ok(None)
            if message_type == "RECORD":
                target._handle_record_message(message)
                return FlextResult[None].ok(None)
            if message_type == "STATE":
                target._handle_state_message(message)
                return FlextResult[None].ok(None)

            # Skip unknown message types
            return FlextResult[None].ok(None)

        except json.JSONDecodeError as e:
            return FlextResult[None].fail(f"Invalid JSON: {e}")

    async def _finalize_target(
        self,
        target: SingerTargetOracleWMS,
    ) -> FlextResult[None]:
        """Finalize target processing and cleanup."""
        try:
            await target.cleanup()
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Finalization failed: {e}")

    def _load_config(self, config_path: str) -> dict[str, object]:
        """Load configuration from file path - NO DUPLICATION."""
        config_file = Path(config_path)
        if not config_file.exists():
            msg: str = f"Configuration file not found: {config_path}"
            raise FileNotFoundError(msg)

        config_text = config_file.read_text(encoding="utf-8")
        return dict(json.loads(config_text))


def main() -> None:
    """Provide CLI entry point without complex CLI setup."""
    try:
        # DRY: Direct approach without CLISettings that causes env var conflicts
        # Create and run CLI instance directly
        cli_instance = OracleWMSTargetCli()

        # Parse command line arguments manually - simple and reliable
        config_path = None
        min_cli_args = 2  # Command itself + --config flag requires 2+ args
        if len(sys.argv) > min_cli_args and sys.argv[1] == "--config":
            config_path = sys.argv[2]

        # Execute CLI with parsed arguments
        result = asyncio.run(cli_instance.execute(config=config_path))

        if not result.success:
            sys.stderr.write(f"Execution failed: {result.error}\n")
            sys.exit(1)

    except KeyboardInterrupt:
        sys.stderr.write("Interrupted by user\n")
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
