"""CLI entry point - REAL implementation using available flext-cli patterns."""

from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path
from typing import Any

# DRY: Use only essential imports - avoid CLISettings env var conflicts
from flext_core import FlextResult

# DRY: Use ONLY the production-ready implementation
from flext_target_oracle_wms.singer.target import SingerTargetOracleWMS


class OracleWMSTargetCli:
    """Oracle WMS Target CLI using REAL flext-cli patterns - NO DUPLICATION."""

    def __init__(self) -> None:
        """Initialize CLI with real flext-cli patterns."""
        self.name = "target-oracle-wms"
        self.description = "Oracle WMS Singer Target - Production Ready using REAL flext-oracle-wms API"
        self.version = "0.9.0"

    async def execute(self, **kwargs: Any) -> FlextResult[None]:
        """Execute target using REAL implementation - NO DUPLICATION."""
        try:
            # Load configuration
            config_result = self._prepare_config(kwargs.get("config"))
            if not config_result.is_success:
                return FlextResult.fail(config_result.error or "Configuration failed")

            config = config_result.data
            if config is None:
                return FlextResult.fail("Configuration data is None")
            target = SingerTargetOracleWMS(config)

            # Setup target
            setup_result = await target.setup()
            if not setup_result.is_success:
                return FlextResult.fail(f"Setup failed: {setup_result.error}")

            # Process messages
            process_result = await self._process_stdin_messages(target)
            if not process_result.is_success:
                return process_result

            # Finalize and cleanup
            return await self._finalize_target(target)

        except Exception as e:
            return FlextResult.fail(f"CLI execution failed: {e}")

    def _prepare_config(self, config_path: str | None) -> FlextResult[dict[str, Any]]:
        """Prepare configuration from path or defaults."""
        try:
            if config_path:
                return FlextResult.ok(self._load_config(config_path))

            # Default configuration
            config = {
                "base_url": "https://ta29.wms.ocs.oraclecloud.com",
                "username": "oracle",
                "password": "oracle",
                "environment": "default",
                "timeout": 30.0,
                "max_retries": 3,
            }
            return FlextResult.ok(config)
        except Exception as e:
            return FlextResult.fail(f"Configuration preparation failed: {e}")

    async def _process_stdin_messages(
        self, target: SingerTargetOracleWMS,
    ) -> FlextResult[None]:
        """Process stdin messages following Singer protocol."""
        try:
            for raw_line in sys.stdin:
                line = raw_line.strip()
                if not line:
                    continue

                result = await self._process_single_message(target, line)
                if not result.is_success:
                    return result

            return FlextResult.ok(None)
        except Exception as e:
            return FlextResult.fail(f"Message processing failed: {e}")

    async def _process_single_message(
        self, target: SingerTargetOracleWMS, line: str,
    ) -> FlextResult[None]:
        """Process a single Singer message."""
        try:
            message = json.loads(line)
            message_type = message.get("type")

            if message_type == "SCHEMA":
                return await target.process_schema_message(message)
            if message_type == "RECORD":
                return await target.process_record_message(message)
            if message_type == "STATE":
                return target.process_state_message(message)

            # Skip unknown message types
            return FlextResult.ok(None)

        except json.JSONDecodeError as e:
            return FlextResult.fail(f"Invalid JSON: {e}")

    async def _finalize_target(
        self, target: SingerTargetOracleWMS,
    ) -> FlextResult[None]:
        """Finalize target processing and cleanup."""
        try:
            finalize_result = target.finalize()
            await target.cleanup()

            if finalize_result.is_success:
                summary = finalize_result.data or {}
                sys.stderr.write(f"Completed: {summary}\n")

            return FlextResult.ok(None)
        except Exception as e:
            return FlextResult.fail(f"Finalization failed: {e}")

    def _load_config(self, config_path: str) -> dict[str, Any]:
        """Load configuration from file path - NO DUPLICATION."""
        config_file = Path(config_path)
        if not config_file.exists():
            msg = f"Configuration file not found: {config_path}"
            raise FileNotFoundError(msg)

        config_text = config_file.read_text(encoding="utf-8")
        return dict(json.loads(config_text))


def main() -> None:
    """Main CLI entry point - DRY approach without complex CLI setup."""
    try:
        # DRY: Direct approach without CLISettings that causes env var conflicts
        # Create and run CLI instance directly
        cli_instance = OracleWMSTargetCli()

        # Parse command line arguments manually - simple and reliable
        config_path = None
        if len(sys.argv) > 2 and sys.argv[1] == "--config":
            config_path = sys.argv[2]

        # Execute CLI with parsed arguments
        result = asyncio.run(cli_instance.execute(config=config_path))

        if not result.is_success:
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
