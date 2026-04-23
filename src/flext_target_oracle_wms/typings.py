"""FLEXT Target Oracle WMS Types — MRO composition of parent type namespaces.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_meltano import m, t as meltano_t
from flext_oracle_wms import t


class FlextTargetOracleWmsTypes(meltano_t, t):
    """MRO facade composing Meltano + OracleWms type namespaces."""

    NV_ADAPTER: m.TypeAdapter[t.JsonValue] = m.TypeAdapter(t.JsonValue)
    CONTAINER_MAP_ADAPTER: m.TypeAdapter[t.JsonMapping] = m.TypeAdapter(t.JsonMapping)


t = FlextTargetOracleWmsTypes
__all__: list[str] = ["FlextTargetOracleWmsTypes", "t"]
