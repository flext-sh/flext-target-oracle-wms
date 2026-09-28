"""FLEXT Target Oracle WMS Types — MRO composition of parent type namespaces.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_meltano import FlextMeltanoTypes
from flext_oracle_wms import FlextOracleWmsTypes

if TYPE_CHECKING:
    from flext_meltano import m


class FlextTargetOracleWmsTypes(FlextMeltanoTypes, FlextOracleWmsTypes):
    """MRO facade composing Meltano + OracleWms type namespaces."""

    CONTAINER_MAP_ADAPTER: m.TypeAdapter[FlextOracleWmsTypes.JsonMapping] = (
        FlextOracleWmsTypes.json_mapping_adapter()
    )


t = FlextTargetOracleWmsTypes
__all__: list[str] = ["FlextTargetOracleWmsTypes", "t"]
