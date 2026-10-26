# AUTO-GENERATED FILE — Regenerate with: make gen
"""Constants for the target Oracle WMS package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoConstants
from flext_oracle_wms import c

from flext_target_oracle_wms._constants import (
    FlextTargetOracleWmsConstantsBase,
    FlextTargetOracleWmsConstantsValues,
)


class FlextTargetOracleWmsConstants(FlextMeltanoConstants, c):
    """Typed constant namespace used by target Oracle WMS modules."""

    class TargetOracleWms(
        FlextTargetOracleWmsConstantsBase,
        FlextTargetOracleWmsConstantsValues,
    ):
        """Target-specific defaults and limits."""


c = FlextTargetOracleWmsConstants
__all__: list[str] = ["FlextTargetOracleWmsConstants", "c"]
