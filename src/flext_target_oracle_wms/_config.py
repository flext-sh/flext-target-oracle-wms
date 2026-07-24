"""FlextTargetOracleWmsConfig — frozen config singleton for flext-target-oracle-wms (ADR-005 §7).

Model-less: business rules live in ``config/*.yaml`` under the ``TargetOracleWms:`` key and
are exposed through the open ``config.TargetOracleWms`` namespace (``extra="allow"``), with
no per-domain model. Access is ``config.TargetOracleWms.<domain>[<key>...]``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from flext_meltano import FlextMeltanoConfig


class _TargetOracleWmsNamespace(BaseModel):
    """Open, frozen namespace exposing every ``config/*.yaml`` domain model-less."""

    model_config = ConfigDict(extra="allow", frozen=True)


class FlextTargetOracleWmsConfig(FlextMeltanoConfig):
    """TargetOracleWms config auto-loaded model-less from ``config/*.yaml``."""

    TargetOracleWms: _TargetOracleWmsNamespace = _TargetOracleWmsNamespace()


config: FlextTargetOracleWmsConfig = FlextTargetOracleWmsConfig.fetch_global()
"""Pre-instantiated frozen config singleton — ``from flext_target_oracle_wms import config``."""

__all__: list[str] = ["FlextTargetOracleWmsConfig", "config"]
