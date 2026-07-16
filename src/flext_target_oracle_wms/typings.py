"""FLEXT Target Oracle WMS Types — MRO composition of parent type namespaces.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_meltano import t as meltano_t
from flext_oracle_wms import p, t


class FlextTargetOracleWmsTypes(meltano_t, t):
    """MRO facade composing Meltano + OracleWms type namespaces."""

    json_value_adapter: p.TypeAdapter[t.JsonValue] = t.json_value_adapter()
    CONTAINER_MAP_ADAPTER: p.TypeAdapter[t.JsonMapping] = t.json_mapping_adapter()


t = FlextTargetOracleWmsTypes
__all__: list[str] = ["FlextTargetOracleWmsTypes", "t"]
