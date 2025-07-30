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
        self.version = "1.0.0"

    async def execute(self, **kwargs: Any) -> FlextResult[None]:
        """Execute target using REAL implementation - NO DUPLICATION."""
        try:
            config_path = kwargs.get("config")
            config: dict[str, Any] = {}

            if config_path:
                config = self._load_config(config_path)
            else:
                # Default configuration
                config = {
                    "base_url": "https://ta29.wms.ocs.oraclecloud.com",
                    "username": "oracle",
                    "password": "oracle",
                    "environment": "default",
                    "timeout": 30.0,
                    "max_retries": 3,
                }

            # DRY: Use the REAL implementation only
            target = SingerTargetOracleWMS(config)

            # Setup target
            setup_result = await target.setup()
            if not setup_result.is_success:
                return FlextResult.fail(f"Setup failed: {setup_result.error}")

            # Process stdin messages (Singer protocol)
            for raw_line in sys.stdin:
                line = raw_line.strip()
                if not line:
                    continue

                try:
                    message = json.loads(line)
                    message_type = message.get("type")

                    if message_type == "SCHEMA":
                        result = await target.process_schema_message(message)
                    elif message_type == "RECORD":
                        result = await target.process_record_message(message)
                    elif message_type == "STATE":
                        result = target.process_state_message(message)
                    else:
                        continue

                    if not result.is_success:
                        return FlextResult.fail(
                            f"Message processing failed: {result.error}"
                        )

                except json.JSONDecodeError as e:
                    return FlextResult.fail(f"Invalid JSON: {e}")

            # Finalize and cleanup
            finalize_result = target.finalize()
            await target.cleanup()

            if finalize_result.is_success:
                summary = finalize_result.data or {}
                sys.stderr.write(f"Completed: {summary}\n")

            return FlextResult.ok(None)

        except Exception as e:
            return FlextResult.fail(f"CLI execution failed: {e}")

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
