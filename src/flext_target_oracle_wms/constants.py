"""Constants for the target Oracle WMS package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_target_oracle_wms/constants
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_meltano import FlextMeltanoConstants
from flext_oracle_wms import FlextOracleWmsConstants

from flext_target_oracle_wms._constants.base import FlextTargetOracleWmsConstantsBase
from flext_target_oracle_wms._constants.values import (
    FlextTargetOracleWmsConstantsValues,
)

if TYPE_CHECKING:
    from flext_oracle_wms import t


class FlextTargetOracleWmsConstants(FlextMeltanoConstants, FlextOracleWmsConstants):
    """Typed constant namespace used by target Oracle WMS modules."""

    class TargetOracleWms(
        FlextTargetOracleWmsConstantsBase,
        FlextTargetOracleWmsConstantsValues.TargetOracleWms,
    ):
        """Target-specific defaults and limits."""


c = FlextTargetOracleWmsConstants
__all__: t.StrSequence = ("FlextTargetOracleWmsConstants", "c")
