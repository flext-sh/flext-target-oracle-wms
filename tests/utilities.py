"""Module skeleton for TestsFlextTargetOracleWmsUtilities.

Test utilities for flext-target-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsUtilities

from flext_target_oracle_wms import u


class TestsFlextTargetOracleWmsUtilities(
    FlextTestsUtilities,
    u,
):
    """Test utilities for flext-target-oracle-wms."""


u = TestsFlextTargetOracleWmsUtilities
__all__: list[str] = ["TestsFlextTargetOracleWmsUtilities", "u"]
