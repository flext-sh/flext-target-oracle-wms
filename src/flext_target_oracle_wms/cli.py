"""Re-export shim — canonical implementation lives in _utilities.cli."""

from __future__ import annotations

from flext_target_oracle_wms._utilities.cli import (
    MIN_CONFIG_ARG_COUNT,
    FlextTargetOracleWmsCli,
    main,
)

__all__ = ["MIN_CONFIG_ARG_COUNT", "FlextTargetOracleWmsCli", "main"]
