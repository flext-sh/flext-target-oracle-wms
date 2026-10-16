"""Domain models for target Oracle WMS.

Inherits from the canonical Meltano models facade and m.
Defines local TargetOracleWms namespace for target-specific models.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoModels
from flext_oracle_wms import FlextOracleWmsModels

from flext_target_oracle_wms._models.config import FlextTargetOracleWmsModelsConfig
from flext_target_oracle_wms._models.target import FlextTargetOracleWmsModelsTarget


class FlextTargetOracleWmsModels(FlextMeltanoModels, FlextOracleWmsModels):
    """Pydantic model namespace for target Oracle WMS.

    Inherited namespaces:
        m.Meltano.*    — Singer message types (overridden with Container support)
        m.OracleWms.*  — WMS entity/API types (from m)

    Local namespace:
        m.TargetOracleWms.* — target-specific settings and schema helpers
    """

    class TargetOracleWms(
        FlextTargetOracleWmsModelsConfig,
        FlextTargetOracleWmsModelsTarget,
    ):
        """Target Oracle WMS model namespace — m.TargetOracleWms.*."""

        WmsAuthenticationConfig = (
            FlextTargetOracleWmsModelsTarget.WmsAuthenticationConfig
        )
        WmsTargetConfig = FlextTargetOracleWmsModelsTarget.WmsTargetConfig
        SingerFieldSchema = FlextTargetOracleWmsModelsTarget.SingerFieldSchema
        SingerSchemaProperties = FlextTargetOracleWmsModelsTarget.SingerSchemaProperties


m = FlextTargetOracleWmsModels

__all__: list[str] = ["FlextTargetOracleWmsModels", "m"]
