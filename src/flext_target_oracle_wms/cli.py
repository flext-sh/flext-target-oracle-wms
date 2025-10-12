"""CLI entry point - REAL implementation using available flext-cli patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import override

from flext_core import FlextCore

from flext_target_oracle_wms.target_client import SingerTargetOracleWMS


class OracleWMSTargetCli:
    """Oracle WMS Target CLI using REAL flext-cli patterns."""

    @override
    def __init__(self: object) -> None:
        """Initialize CLI with real flext-cli patterns."""
        self.name = "target-oracle-wms"
        self.description = "Oracle WMS Singer Target - Production Ready using REAL flext-oracle-wms API"
        self.version = "0.9.0"

    @override
    def execute(self, **kwargs: object) -> FlextCore.Result[None]:
        """Execute target using REAL implementation.

        SOLID REFACTORING: Reduced multiple returns (count=6) to single exit point
        using Railway-Oriented Programming pattern.
        """
        result: FlextCore.Result[None] = FlextCore.Result[None].ok(None)

        try:
            # Load configuration
            config_path: FlextCore.Types.Dict = kwargs.get("config")
            config_path_str: FlextCore.Types.Dict = (
                str(config_path) if config_path is not None else None
            )
            config_result: FlextCore.Result[object] = self._prepare_config(
                config_path_str
            )
            if not config_result.success:
                result = FlextCore.Result[None].fail(
                    config_result.error or "Configuration failed",
                )
            else:
                config: FlextCore.Types.Dict = config_result.data
                if config is None:
                    result: FlextCore.Result[object] = FlextCore.Result[None].fail(
                        "Configuration data is None"
                    )
                else:
                    # Continue with target setup and processing
                    result: FlextCore.Result[object] = self._execute_target_pipeline(
                        config
                    )

        except Exception as e:
            result: FlextCore.Result[object] = FlextCore.Result[None].fail(
                f"CLI execution failed: {e}"
            )

        return result

    def _execute_target_pipeline(
        self,
        config: FlextCore.Types.Dict,
    ) -> FlextCore.Result[None]:
        """Execute the target pipeline with railway-oriented programming.

        SOLID REFACTORING: Extract target pipeline execution to reduce complexity.
        """
        target = SingerTargetOracleWMS(config)

        # Setup target
        setup_result: FlextCore.Result[object] = target.setup()
        if not setup_result.success:
            return FlextCore.Result[None].fail(f"Setup failed: {setup_result.error}")

        # Process messages
        process_result: FlextCore.Result[object] = self._process_stdin_messages(target)
        if not process_result.success:
            return process_result

        # Finalize and cleanup
        return self._finalize_target(target)

    def _prepare_config(
        self,
        config_path: str | None,
    ) -> FlextCore.Result[FlextCore.Types.Dict]:
        """Prepare configuration from path or defaults."""
        try:
            if config_path:
                return FlextCore.Result[FlextCore.Types.Dict].ok(
                    self._load_config(config_path),
                )

            # Default configuration
            config: FlextCore.Types.Dict = {
                "base_url": "https://invalid.wms.ocs.oraclecloud.com",
                "username": "oracle",
                "password": "oracle",
                "environment": "default",
                "timeout": 30.0,
                "max_retries": 3,
            }
            return FlextCore.Result[FlextCore.Types.Dict].ok(config)
        except Exception as e:
            return FlextCore.Result[FlextCore.Types.Dict].fail(
                f"Configuration preparation failed: {e}",
            )

    def _process_stdin_messages(
        self,
        target: SingerTargetOracleWMS,
    ) -> FlextCore.Result[None]:
        """Process stdin messages following Singer protocol."""
        try:
            for raw_line in sys.stdin:
                line = raw_line.strip()
                if not line:
                    continue

                result: FlextCore.Result[object] = self._process_single_message(
                    target, line
                )
                if not result.success:
                    return result

            return FlextCore.Result[None].ok(None)
        except Exception as e:
            return FlextCore.Result[None].fail(f"Message processing failed: {e}")

    def _process_single_message(
        self,
        target: SingerTargetOracleWMS,
        line: str,
    ) -> FlextCore.Result[None]:
        """Process a single Singer message."""
        try:
            message = json.loads(line)
            message_type = message.get("type")

            if message_type == "SCHEMA":
                target.handle_schema_message(message)
                return FlextCore.Result[None].ok(None)
            if message_type == "RECORD":
                target.handle_record_message(message)
                return FlextCore.Result[None].ok(None)
            if message_type == "STATE":
                target.handle_state_message(message)
                return FlextCore.Result[None].ok(None)

            # Skip unknown message types
            return FlextCore.Result[None].ok(None)

        except json.JSONDecodeError as e:
            return FlextCore.Result[None].fail(f"Invalid JSON: {e}")

    def _finalize_target(
        self,
        target: SingerTargetOracleWMS,
    ) -> FlextCore.Result[None]:
        """Finalize target processing and cleanup."""
        try:
            target.cleanup()
            return FlextCore.Result[None].ok(None)
        except Exception as e:
            return FlextCore.Result[None].fail(f"Finalization failed: {e}")

    def _load_config(self, config_path: str) -> FlextCore.Types.Dict:
        """Load configuration from file path."""
        config_file: FlextCore.Types.Dict = Path(config_path)
        if not config_file.exists():
            msg: str = f"Configuration file not found: {config_path}"
            raise FileNotFoundError(msg)

        config_text: FlextCore.Types.Dict = config_file.read_text(encoding="utf-8")
        return dict(json.loads(config_text))


def main() -> None:
    """Provide CLI entry point without complex CLI setup."""
    try:
        # DRY: Direct approach without FlextCliSettings that causes env var conflicts
        # Create and run CLI instance directly
        cli_instance = OracleWMSTargetCli()

        # Parse command line arguments manually - simple and reliable
        config_path = None
        min_cli_args = 2  # Command itself + --config flag requires 2+ args
        if len(sys.argv) > min_cli_args and sys.argv[1] == "--config":
            config_path = sys.argv[2]

        # Execute CLI with parsed arguments
        result: FlextCore.Result[object] = cli_instance.execute(config=config_path)

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
