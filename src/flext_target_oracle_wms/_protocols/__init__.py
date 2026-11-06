# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Wms. Protocols package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_target_oracle_wms._protocols.auth import (
        FlextTargetOracleWmsProtocolsAuth,
    )
    from flext_target_oracle_wms._protocols.config import (
        FlextTargetOracleWmsProtocolsConfig,
    )
    from flext_target_oracle_wms._protocols.singer import (
        FlextTargetOracleWmsProtocolsSinger,
    )
    from flext_target_oracle_wms._protocols.target import (
        FlextTargetOracleWmsProtocolsTarget,
    )


__all__: tuple[str, ...] = (
    "FlextTargetOracleWmsProtocolsAuth",
    "FlextTargetOracleWmsProtocolsConfig",
    "FlextTargetOracleWmsProtocolsSinger",
    "FlextTargetOracleWmsProtocolsTarget",
)

install_lazy_exports(
    __name__,
    globals(),
    {
        "FlextTargetOracleWmsProtocolsAuth": ".auth",
        "FlextTargetOracleWmsProtocolsConfig": ".config",
        "FlextTargetOracleWmsProtocolsSinger": ".singer",
        "FlextTargetOracleWmsProtocolsTarget": ".target",
    },
    public_exports=__all__,
)
