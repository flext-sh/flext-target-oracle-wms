"""FLEXT Target Oracle WMS Types — MRO composition of parent type namespaces.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_meltano import FlextMeltanoTypes, m, t
from flext_oracle_wms import FlextOracleWmsTypes


class FlextTargetOracleWmsTypes(FlextMeltanoTypes, FlextOracleWmsTypes):
    """MRO facade composing Meltano + OracleWms type namespaces."""

    NV_ADAPTER: m.TypeAdapter[t.Container] = m.TypeAdapter(t.Container)
    CONTAINER_MAP_ADAPTER: m.TypeAdapter[Mapping[str, t.Container]] = m.TypeAdapter(
        Mapping[str, t.Container]
    )


t = FlextTargetOracleWmsTypes
__all__: list[str] = ["FlextTargetOracleWmsTypes", "t"]
