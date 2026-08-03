"""CLI entry point for target Oracle WMS."""

from __future__ import annotations

import sys
from pathlib import Path

from flext_core import r
from flext_target_oracle_wms import c, m, p, t, u
from flext_target_oracle_wms.__version__ import __version__
from flext_target_oracle_wms._utilities.client import (
    FlextTargetOracleWmsUtilitiesClient,
)


class FlextTargetOracleWmsCli:
    """Minimal CLI wrapper for Singer target execution."""

    def __init__(self) -> None:
        """Initialize CLI metadata."""
        self.name = "target-oracle-wms"
        self.description = "Oracle WMS Singer Target"
        # NOTE (multi-agent, bead mro-nwc.19): derive from __version__ SSOT; the prior
        # hardcoded "0.9.0" was stale (real version is 0.12.0.dev0) — a silent version bug.
        self.version = __version__

    def execute(
        self, message_lines: t.StrSequence | None = None, settings: str | None = None
    ) -> p.Result[bool]:
        """Execute target run.

        Args:
            message_lines: Singer message lines to process. When ``None`` the lines
                are read from ``sys.stdin`` (dependency injection seam so callers and
                tests supply input directly instead of patching stdin).
            settings: optional path to a Singer settings JSON file. When ``None`` a
                default configuration is used.

        """
        lines: t.StrSequence = (
            message_lines if message_lines is not None else list(sys.stdin)
        )
        return (
            self
            ._prepare_config(settings)
            .map_error(lambda e: e or "Configuration failed")
            .flat_map(lambda config: self._execute_target_pipeline(config, lines))
        )

    def _execute_target_pipeline(
        self, settings: m.TargetOracleWms.WmsTargetConfig, message_lines: t.StrSequence
    ) -> p.Result[bool]:
        """Set up, process the message lines, and clean up the target runtime."""
        target = FlextTargetOracleWmsUtilitiesClient.Target(settings)
        setup_result = target.setup().map_error(lambda e: e or "Setup failed")
        if setup_result.failure:
            return setup_result
        process_result = target.process_lines(message_lines)
        if process_result.failure:
            return process_result
        return self._finalize_target(target)

    def _finalize_target(
        self, target: FlextTargetOracleWmsUtilitiesClient.Target
    ) -> p.Result[bool]:
        """Finalize target processing."""
        return target.cleanup()

    def _load_config(self, config_path: str) -> str:
        """Read JSON configuration file."""
        config_file = Path(config_path)
        if not config_file.exists():
            msg = f"Configuration file not found: {config_path}"
            raise FileNotFoundError(msg)
        content: str = u.Cli.files_read_text(config_file).unwrap()
        return content

    def _prepare_config(
        self, config_path: str | None
    ) -> p.Result[m.TargetOracleWms.WmsTargetConfig]:
        """Load settings from file or build defaults."""
        if config_path is not None:
            return r[m.TargetOracleWms.WmsTargetConfig].ok(
                m.TargetOracleWms.WmsTargetConfig.model_validate_json(
                    self._load_config(config_path)
                )
            )
        return r[m.TargetOracleWms.WmsTargetConfig].ok(
            m.TargetOracleWms.WmsTargetConfig.model_validate({
                "wms_auth": {
                    "base_url": "https://invalid.wms.ocs.oraclecloud.com",
                    "username": "oracle",
                    "password": "oracle",
                }
            })
        )


def main(
    argv: t.StrSequence | None = None, message_lines: t.StrSequence | None = None
) -> None:
    """Run CLI command from process arguments.

    Args:
        argv: process arguments (excluding the program name is NOT assumed — mirrors
            ``sys.argv``). Defaults to ``sys.argv`` when ``None`` (DI seam for tests).
        message_lines: Singer message lines; forwarded to ``execute`` (reads stdin
            when ``None``).

    """
    args: t.StrSequence = argv if argv is not None else sys.argv
    cli_instance = FlextTargetOracleWmsCli()
    config_path: str | None = None
    if (
        len(args) >= c.TargetOracleWms.CLI_MIN_CONFIG_ARG_COUNT
        and args[1] == "--config"
    ):
        config_path = args[2]
    result = cli_instance.execute(message_lines=message_lines, settings=config_path)
    if result.failure:
        msg = result.error or "Execution failed"
        raise RuntimeError(msg)


if __name__ == "__main__":
    main()
