"""CLI entry point for target Oracle WMS."""

from __future__ import annotations

import sys
from pathlib import Path

from flext_target_oracle_wms import Target as FlextTargetOracleWms, c, m, p, r, t


class FlextTargetOracleWmsCli:
    """Minimal CLI wrapper for Singer target execution."""

    def __init__(self) -> None:
        """Initialize CLI metadata."""
        self.name = "target-oracle-wms"
        self.description = "Oracle WMS Singer Target"
        self.version = "0.9.0"

    def execute(self, **kwargs: t.Scalar) -> p.Result[bool]:
        """Execute target run using optional settings path."""
        config_arg = kwargs.get("settings")
        config_path = str(config_arg) if config_arg is not None else None
        return (
            self
            ._prepare_config(config_path)
            .map_error(lambda e: e or "Configuration failed")
            .flat_map(self._execute_target_pipeline)
        )

    def _execute_target_pipeline(
        self,
        settings: m.TargetOracleWms.WmsTargetConfig,
    ) -> p.Result[bool]:
        """Setup, process stdin, and cleanup target runtime."""
        target = FlextTargetOracleWms(settings)
        setup_result = target.setup().map_error(lambda e: e or "Setup failed")
        if setup_result.failure:
            return setup_result
        process_result = self._process_stdin_messages(target)
        if process_result.failure:
            return process_result
        return self._finalize_target(target)

    def _finalize_target(self, target: FlextTargetOracleWms) -> p.Result[bool]:
        """Finalize target processing."""
        return target.cleanup()

    def _load_config(self, config_path: str) -> str:
        """Read JSON configuration file."""
        config_file = Path(config_path)
        if not config_file.exists():
            msg = f"Configuration file not found: {config_path}"
            raise FileNotFoundError(msg)
        return config_file.read_text(encoding="utf-8")

    def _prepare_config(
        self,
        config_path: str | None,
    ) -> p.Result[m.TargetOracleWms.WmsTargetConfig]:
        """Load settings from file or build defaults."""
        if config_path is not None:
            return r[m.TargetOracleWms.WmsTargetConfig].ok(
                m.TargetOracleWms.WmsTargetConfig.model_validate_json(
                    self._load_config(config_path),
                ),
            )
        return r[m.TargetOracleWms.WmsTargetConfig].ok(
            m.TargetOracleWms.WmsTargetConfig.model_validate({
                "wms_auth": {
                    "base_url": "https://invalid.wms.ocs.oraclecloud.com",
                    "username": "oracle",
                    "password": "oracle",
                },
            }),
        )

    def _process_stdin_messages(self, target: FlextTargetOracleWms) -> p.Result[bool]:
        """Read and process stdin message lines."""
        return target.process_lines(list(sys.stdin))


def main() -> None:
    """Run CLI command from process arguments."""
    cli_instance = FlextTargetOracleWmsCli()
    config_path: str | None = None
    if (
        len(sys.argv) >= c.TargetOracleWms.CLI_MIN_CONFIG_ARG_COUNT
        and sys.argv[1] == "--config"
    ):
        config_path = sys.argv[2]
    result = (
        cli_instance.execute(settings=config_path)
        if config_path is not None
        else cli_instance.execute()
    )
    if result.failure:
        msg = result.error or "Execution failed"
        raise RuntimeError(msg)


if __name__ == "__main__":
    main()
