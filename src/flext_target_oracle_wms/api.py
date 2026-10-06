"""FLEXT service orchestrator for target-oracle-wms.

Thin facade over ``meltano.Target`` — all infrastructure from the base via MRO.
Only domain-specific sink creation defined here.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, override

from flext_meltano import meltano

from flext_target_oracle_wms import c, p, t, u
from flext_target_oracle_wms._utilities.service_runtime import (
    FlextTargetOracleWmsServiceRuntime,
)


class FlextTargetOracleWmsService(meltano.Target):
    """Orchestrator for target-oracle-wms. All behavior from base via MRO."""

    target_name: Annotated[
        t.NonEmptyStr,
        u.Field(description="Canonical Singer target identifier."),
    ] = c.TargetOracleWms.TARGET_NAME

    @override
    def create_sink(
        self,
        stream_name: str,
        schema: t.JsonMapping,
    ) -> p.Meltano.SingerDrainSink:
        """Create an Oracle WMS sink for a stream.

        Returns:
            The resulting ``p.Meltano.SingerDrainSink``.
        """
        target_config: t.ScalarMapping = (
            self.settings_overrides if self.settings_overrides is not None else {}
        )
        return FlextTargetOracleWmsServiceRuntime.create_sink(
            stream_name=stream_name,
            schema=schema,
            target_config=target_config,
        )


target_oracle_wms: FlextTargetOracleWmsService = (
    FlextTargetOracleWmsService.fetch_global()
)
"""Shared FlextTargetOracleWmsService facade instance."""

__all__: list[str] = ["FlextTargetOracleWmsService", "target_oracle_wms"]
