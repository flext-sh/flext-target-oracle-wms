# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Wms. Models package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_target_oracle_wms._models.auth import FlextTargetOracleWmsModelsAuth
    from flext_target_oracle_wms._models.config import FlextTargetOracleWmsModelsConfig
    from flext_target_oracle_wms._models.singer import FlextTargetOracleWmsModelsSinger
    from flext_target_oracle_wms._models.target import FlextTargetOracleWmsModelsTarget


__all__: tuple[str, ...] = (
    "FlextTargetOracleWmsModelsAuth",
    "FlextTargetOracleWmsModelsConfig",
    "FlextTargetOracleWmsModelsSinger",
    "FlextTargetOracleWmsModelsTarget",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextTargetOracleWmsModelsAuth": ".auth",
        "FlextTargetOracleWmsModelsConfig": ".config",
        "FlextTargetOracleWmsModelsSinger": ".singer",
        "FlextTargetOracleWmsModelsTarget": ".target",
    }),
    public_exports=__all__,
)
