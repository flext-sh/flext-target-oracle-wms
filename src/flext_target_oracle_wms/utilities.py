# AUTO-GENERATED FILE — Regenerate with: make gen
"""Utility helpers for target Oracle WMS operations.

Facade composing helpers from _utilities/ submodules into u.TargetOracleWms.* namespace.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import u as flext_meltano_u
from flext_oracle_wms import u

from flext_target_oracle_wms._utilities import (
    FlextTargetOracleWmsServiceRuntime,
    FlextTargetOracleWmsUtilitiesClient,
    FlextTargetOracleWmsUtilitiesHelpers,
)


class FlextTargetOracleWmsUtilities(flext_meltano_u, u):
    """Namespace exposing Singer-target Client and Helpers under TargetOracleWms.*."""

    class TargetOracleWms(
        FlextTargetOracleWmsServiceRuntime,
        FlextTargetOracleWmsUtilitiesClient,
        FlextTargetOracleWmsUtilitiesHelpers,
    ):
        """Project-local namespace inheriting the Client and Helpers public classes."""


u = FlextTargetOracleWmsUtilities
__all__: list[str] = ["FlextTargetOracleWmsUtilities", "u"]
