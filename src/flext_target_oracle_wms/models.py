# AUTO-GENERATED FILE — Regenerate with: make gen
"""Domain models for target Oracle WMS.

Inherits from the canonical Meltano models facade and m.
Defines local TargetOracleWms namespace for target-specific models.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import m as flext_meltano_m
from flext_oracle_wms import m as flext_oracle_wms_m

from flext_target_oracle_wms._models import (
    FlextTargetOracleWmsModelsAuth,
    FlextTargetOracleWmsModelsConfig,
    FlextTargetOracleWmsModelsSinger,
    FlextTargetOracleWmsModelsTarget,
)


class FlextTargetOracleWmsModels(flext_meltano_m, flext_oracle_wms_m):
    """Pydantic model namespace for target Oracle WMS.

    Inherited namespaces:
        m.Meltano.*    — Singer message types (overridden with Container support)
        m.OracleWms.*  — WMS entity/API types (from m)

    Local namespace:
        m.TargetOracleWms.* — target-specific settings and schema helpers
    """

    class TargetOracleWms(
        FlextTargetOracleWmsModelsAuth,
        FlextTargetOracleWmsModelsConfig,
        FlextTargetOracleWmsModelsSinger,
        FlextTargetOracleWmsModelsTarget,
    ):
        """Target Oracle WMS model namespace — m.TargetOracleWms.*."""


m = FlextTargetOracleWmsModels
__all__: list[str] = ["FlextTargetOracleWmsModels", "m"]
