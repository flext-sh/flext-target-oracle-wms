# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Wms. Models package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_target_oracle_wms._models.config import FlextTargetOracleWmsModelsConfig


__all__: tuple[str, ...] = ("FlextTargetOracleWmsModelsConfig",)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({"FlextTargetOracleWmsModelsConfig": ".config"}),
    public_exports=__all__,
)
