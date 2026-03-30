"""Module skeleton for FlextTargetOracleWmsTestTypes.

Test type aliases for flext-target-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_target_oracle_wms import FlextTargetOracleWmsTypes


class FlextTargetOracleWmsTestTypes(FlextTestsTypes, FlextTargetOracleWmsTypes):
    """Test type aliases for flext-target-oracle-wms."""


t = FlextTargetOracleWmsTestTypes
__all__ = ["FlextTargetOracleWmsTestTypes", "t"]
