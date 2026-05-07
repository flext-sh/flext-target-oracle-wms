"""Module skeleton for TestsFlextTargetOracleWmsTypes.

Test type aliases for flext-target-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_target_oracle_wms import t


class TestsFlextTargetOracleWmsTypes(FlextTestsTypes, t):
    """Test type aliases for flext-target-oracle-wms."""


t = TestsFlextTargetOracleWmsTypes
__all__: list[str] = ["TestsFlextTargetOracleWmsTypes", "t"]
