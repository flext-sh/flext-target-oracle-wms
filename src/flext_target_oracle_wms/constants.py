# AUTO-GENERATED FILE — Regenerate with: make gen
"""Constants for the target Oracle WMS package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import c as flext_meltano_c
from flext_oracle_wms import c as flext_oracle_wms_c

from flext_target_oracle_wms._constants import (
    FlextTargetOracleWmsConstantsBase,
    FlextTargetOracleWmsConstantsValues,
)


class FlextTargetOracleWmsConstants(flext_meltano_c, flext_oracle_wms_c):
    """Typed constant namespace used by target Oracle WMS modules."""

    class TargetOracleWms(
        FlextTargetOracleWmsConstantsBase,
        FlextTargetOracleWmsConstantsValues,
    ):
        """Target-specific defaults and limits."""


c = FlextTargetOracleWmsConstants
__all__: list[str] = ["FlextTargetOracleWmsConstants", "c"]
