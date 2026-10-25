"""FLEXT service orchestrator for target-oracle-wms.

Thin facade over ``meltano.Target`` — all infrastructure from the base via MRO.
The sink factory is declared, never overridden.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, ClassVar

from flext_meltano import FlextMeltanoTargetServiceBase

from flext_target_oracle_wms import c, m, p, t, u


class FlextTargetOracleWmsService(FlextMeltanoTargetServiceBase):
    """Orchestrator for target-oracle-wms. All behavior from base via MRO."""

    target_name: Annotated[
        t.NonEmptyStr,
        m.Field(description="Canonical Singer target identifier."),
    ] = c.TargetOracleWms.TARGET_NAME

    sink_factory: ClassVar[p.Meltano.SinkFactory] = u.TargetOracleWms.create_sink


_service: FlextTargetOracleWmsService = FlextTargetOracleWmsService.fetch_global()

target_oracle_wms: FlextTargetOracleWmsService = _service
"""Shared FlextTargetOracleWmsService facade instance."""

__all__: list[str] = ["FlextTargetOracleWmsService", "target_oracle_wms"]
