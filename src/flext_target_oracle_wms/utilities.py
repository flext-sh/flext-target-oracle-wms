"""Utility helpers for target Oracle WMS operations.

Facade composing helpers from _utilities/ submodules into u.TargetOracleWms.* namespace.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_target_oracle_wms/utilities
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoUtilities
from flext_oracle_wms import FlextOracleWmsUtilities

from flext_target_oracle_wms._utilities import (
    FlextTargetOracleWmsServiceRuntime,
    FlextTargetOracleWmsUtilitiesClient,
    FlextTargetOracleWmsUtilitiesHelpers,
)


class FlextTargetOracleWmsUtilities(FlextMeltanoUtilities, FlextOracleWmsUtilities):
    """Namespace exposing Singer-target Client and Helpers under TargetOracleWms.*."""

    class TargetOracleWms(
        FlextTargetOracleWmsServiceRuntime,
        FlextTargetOracleWmsUtilitiesClient,
        FlextTargetOracleWmsUtilitiesHelpers,
    ):
        """Project-local namespace aggregating Client and Helpers public classes."""


u = FlextTargetOracleWmsUtilities

__all__: list[str] = ["FlextTargetOracleWmsUtilities", "u"]
