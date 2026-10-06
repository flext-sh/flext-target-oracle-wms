"""Protocols for target Oracle WMS integration points.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_target_oracle_wms/protocols
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoProtocols
from flext_oracle_wms import FlextOracleWmsProtocols


class FlextTargetOracleWmsProtocols(FlextMeltanoProtocols, FlextOracleWmsProtocols):
    """Protocols composed from Meltano and Oracle WMS via MRO."""


p = FlextTargetOracleWmsProtocols
__all__: list[str] = ["FlextTargetOracleWmsProtocols", "p"]
