"""CLI entry point for target Oracle WMS."""

from __future__ import annotations

import sys
from pathlib import Path

from flext_core import r, t, u

from .models import m
from .target_client import SingerTargetOracleWMS

MIN_CONFIG_ARG_COUNT = 3


class OracleWMSTargetCli:
    """Minimal CLI wrapper for Singer target execution."""

    def __init__(self) -> None:
        """Initialize CLI metadata."""
        self.name = "target-oracle-wms"
        self.description = "Oracle WMS Singer Target"
        self.version = "0.9.0"

    def execute(self, **kwargs: t.Scalar) -> r[bool]:
        """Execute target run using optional config path."""
        config_arg = kwargs.get("config")
        config_path = str(config_arg) if config_arg is not None else None
        return (
            self
            ._prepare_config(config_path)
            .map_error(lambda e: e or "Configuration failed")
            .flat_map(self._execute_target_pipeline)
        )

    def _execute_target_pipeline(
        self, config: m.TargetOracleWms.WmsTargetConfig
    ) -> r[bool]:
        """Setup, process stdin, and cleanup target runtime."""
        target = SingerTargetOracleWMS(config)
        setup_result = target.setup().map_error(lambda e: e or "Setup failed")
        return u.flow_result(
            setup_result,
            lambda _: self._process_stdin_messages(target),
            lambda _: self._finalize_target(target),
        )

    def _finalize_target(self, target: SingerTargetOracleWMS) -> r[bool]:
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
        self, config_path: str | None
    ) -> r[m.TargetOracleWms.WmsTargetConfig]:
        """Load config from file or build defaults."""
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

    def _process_stdin_messages(self, target: SingerTargetOracleWMS) -> r[bool]:
        """Read and process stdin message lines."""
        return target.process_lines(list(sys.stdin))


def main() -> None:
    """Run CLI command from process arguments."""
    cli_instance = OracleWMSTargetCli()
    config_path: str | None = None
    if len(sys.argv) >= MIN_CONFIG_ARG_COUNT and sys.argv[1] == "--config":
        config_path = sys.argv[2]
    result = cli_instance.execute(config=config_path)
    if result.is_failure:
        msg = result.error or "Execution failed"
        raise RuntimeError(msg)


if __name__ == "__main__":
    main()
