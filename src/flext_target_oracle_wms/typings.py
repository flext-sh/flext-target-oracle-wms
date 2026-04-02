"""FLEXT Target Oracle WMS Types — MRO composition of parent type namespaces.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_meltano import FlextMeltanoTypes
from flext_oracle_wms import FlextOracleWmsTypes


class FlextTargetOracleWmsTypes(FlextMeltanoTypes, FlextOracleWmsTypes):
    """MRO facade composing Meltano + OracleWms type namespaces."""


t = FlextTargetOracleWmsTypes
__all__ = ["FlextTargetOracleWmsTypes", "t"]
