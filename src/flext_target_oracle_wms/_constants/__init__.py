# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Wms. Constants package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_target_oracle_wms._constants.base import (
        FlextTargetOracleWmsConstantsBase,
    )
    from flext_target_oracle_wms._constants.values import (
        FlextTargetOracleWmsConstantsValues,
    )


__all__: tuple[str, ...] = (
    "FlextTargetOracleWmsConstantsBase",
    "FlextTargetOracleWmsConstantsValues",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextTargetOracleWmsConstantsBase": ".base",
        "FlextTargetOracleWmsConstantsValues": ".values",
    }),
    public_exports=__all__,
)
