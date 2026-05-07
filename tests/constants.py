"""Module skeleton for TestsFlextTargetOracleWmsConstants.

Test constants for flext-target-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final

from flext_tests import FlextTestsConstants

from flext_target_oracle_wms import c


class TestsFlextTargetOracleWmsConstants(c, FlextTestsConstants):
    """Test constants for flext-target-oracle-wms."""

    class TargetOracleWms(c.TargetOracleWms):
        """Target Oracle WMS domain test constants namespace."""

        class Tests(
            c.TargetOracleWms.Tests,
            FlextTestsConstants.Tests,
        ):
            """Target Oracle WMS-specific test constants."""

            PROJECT_ROOT_PARENT_DEPTH: Final[int] = 1
            SRC_DIR: Final[str] = "src"
            PACKAGE_DIR: Final[str] = "flext_target_oracle_wms"
            ALLOWED_MODULE_FUNCTIONS: Final[dict[str, frozenset[str]]] = {
                "cli.py": frozenset({"main"}),
            }
            PERF_ITERATIONS: Final[int] = 500
            PERF_THRESHOLD_SEC: Final[float] = 5.0


c = TestsFlextTargetOracleWmsConstants
__all__: list[str] = ["TestsFlextTargetOracleWmsConstants", "c"]
