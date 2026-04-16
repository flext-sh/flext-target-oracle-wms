"""FLEXT Target Oracle WMS Types — MRO composition of parent type namespaces.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pydantic import TypeAdapter

from flext_meltano import FlextMeltanoTypes
from flext_oracle_wms import FlextOracleWmsTypes
from flext_target_oracle_wms import m


class FlextTargetOracleWmsTypes(FlextMeltanoTypes, FlextOracleWmsTypes):
    """MRO facade composing Meltano + OracleWms type namespaces."""

    NV_ADAPTER: m.TypeAdapter[FlextMeltanoTypes.NormalizedValue] = TypeAdapter(
        FlextMeltanoTypes.NormalizedValue
    )
    CONTAINER_MAP_ADAPTER: m.TypeAdapter[FlextMeltanoTypes.ContainerMapping] = (
        TypeAdapter(FlextMeltanoTypes.ContainerMapping)
    )


t = FlextTargetOracleWmsTypes
__all__: list[str] = ["FlextTargetOracleWmsTypes", "t"]
