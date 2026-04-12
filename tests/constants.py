"""Module skeleton for TestsFlextTargetOracleWmsConstants.

Test constants for flext-target-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsConstants

from flext_target_oracle_wms import FlextTargetOracleWmsConstants


class TestsFlextTargetOracleWmsConstants(
    FlextTestsConstants, FlextTargetOracleWmsConstants
):
    """Test constants for flext-target-oracle-wms."""


c = TestsFlextTargetOracleWmsConstants
__all__: list[str] = ["TestsFlextTargetOracleWmsConstants", "c"]
