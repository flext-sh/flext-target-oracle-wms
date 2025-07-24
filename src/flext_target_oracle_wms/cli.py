"""CLI entry point for FLEXT Target Oracle WMS."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import click

from flext_target_oracle_wms.target import TargetOracleWMS


@click.command()
@click.option(
    "--config",
    "-c",
    help="Configuration file path or JSON string",
    type=str,
)
@click.option(
    "--format",
    "output_format",
    help="Output format (default: singer)",
    type=click.Choice(["singer", "json"], case_sensitive=False),
    default="singer",
)
@click.version_option(version="0.7.0", prog_name="target-oracle-wms")
def main(
    config: str | None = None,
    output_format: str = "singer",
) -> None:
    """FLEXT Target Oracle WMS - Singer target for Oracle WMS data loading.

    This target reads Singer-formatted data from stdin and loads it into Oracle WMS.

    Examples:
        target-oracle-wms --config config.json
        cat data.jsonl | target-oracle-wms --config config.json

    """
    target = TargetOracleWMS(
        config=_load_config(config) if config else None,
        parse_env_config=True,
    )

    target.listen()


def _load_config(config_path: str) -> dict[str, Any]:
    """Load configuration from file path."""
    config_file = Path(config_path)
    if not config_file.exists():
        msg = f"Configuration file not found: {config_path}"
        raise FileNotFoundError(msg)

    config_data: dict[str, Any] = json.loads(config_file.read_text(encoding="utf-8"))
    return config_data


if __name__ == "__main__":
    main()
