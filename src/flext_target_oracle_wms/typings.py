"""FLEXT Target Oracle WMS Types — MRO composition of parent type namespaces.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_meltano.models import m
from flext_meltano.typings import t as meltano_t
from flext_oracle_wms.typings import t


class FlextTargetOracleWmsTypes(meltano_t, t):
    """MRO facade composing Meltano + OracleWms type namespaces."""

    json_value_adapter: m.TypeAdapter[t.JsonValue] = t.json_value_adapter()
    CONTAINER_MAP_ADAPTER: m.TypeAdapter[t.JsonMapping] = t.json_mapping_adapter()


t = FlextTargetOracleWmsTypes
__all__: list[str] = ["FlextTargetOracleWmsTypes", "t"]
