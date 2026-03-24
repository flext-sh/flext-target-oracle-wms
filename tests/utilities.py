"""Module skeleton for FlextTargetOracleWmsTestUtilities.

Test utilities for flext-target-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsUtilities

from flext_target_oracle_wms.utilities import FlextTargetOracleWmsUtilities


class FlextTargetOracleWmsTestUtilities(
    FlextTestsUtilities,
    FlextTargetOracleWmsUtilities,
):
    """Test utilities for flext-target-oracle-wms."""


u = FlextTargetOracleWmsTestUtilities
__all__ = ["FlextTargetOracleWmsTestUtilities", "u"]
