"""FLEXT service orchestrator for target-oracle-wms.

from flext_target_oracle_wms.utilities import u
Thin facade — all infrastructure from ``FlextMeltanoTargetServiceBase`` via MRO.
Only domain-specific sink creation defined here.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, override

from flext_meltano.services.consumer_bases.target_service_base import (
    FlextMeltanoTargetServiceBase,
)
from flext_target_oracle_wms import p, t, u
from flext_target_oracle_wms._utilities.service_runtime import (
    FlextTargetOracleWmsServiceRuntime,
)


class FlextTargetOracleWmsService(FlextMeltanoTargetServiceBase):
    """Orchestrator for target-oracle-wms. All behavior from base via MRO."""

    target_name: Annotated[
        t.NonEmptyStr,
        u.Field(description="Canonical Singer target identifier."),
    ] = "target-oracle-wms"

    @override
    def create_sink(
        self,
        stream_name: str,
        schema: t.JsonMapping,
    ) -> p.Meltano.SingerDrainSink:
        """Create an Oracle WMS sink for a stream."""
        target_config: t.JsonMapping = (
            self.settings_overrides if self.settings_overrides is not None else {}
        )
        return FlextTargetOracleWmsServiceRuntime.create_sink(
            stream_name=stream_name,
            schema=schema,
            target_config=target_config,
        )


target_oracle_wms = FlextTargetOracleWmsService

__all__: list[str] = ["FlextTargetOracleWmsService", "target_oracle_wms"]
