# AUTO-GENERATED FILE — Regenerate with: make gen
"""Protocols for target Oracle WMS integration points.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoProtocols
from flext_oracle_wms import FlextOracleWmsProtocols

from flext_target_oracle_wms._protocols import (
    FlextTargetOracleWmsProtocolsAuth,
    FlextTargetOracleWmsProtocolsConfig,
    FlextTargetOracleWmsProtocolsSinger,
    FlextTargetOracleWmsProtocolsTarget,
)


class FlextTargetOracleWmsProtocols(FlextMeltanoProtocols, FlextOracleWmsProtocols):
    """Protocols composed from Meltano and Oracle WMS via MRO."""

    class TargetOracleWms(
        FlextTargetOracleWmsProtocolsAuth,
        FlextTargetOracleWmsProtocolsConfig,
        FlextTargetOracleWmsProtocolsSinger,
        FlextTargetOracleWmsProtocolsTarget,
    ):
        """Target Oracle WMS protocol namespace."""


p = FlextTargetOracleWmsProtocols
__all__: list[str] = ["FlextTargetOracleWmsProtocols", "p"]
