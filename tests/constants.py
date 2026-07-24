"""Module skeleton for TestsFlextTargetOracleWmsConstants.

Test constants for flext-target-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final

from flext_target_oracle_wms import c
from flext_tests import FlextTestsConstants


class TestsFlextTargetOracleWmsConstants(c, FlextTestsConstants):
    """Test constants for flext-target-oracle-wms."""

    class TargetOracleWms(c.TargetOracleWms):
        """Target Oracle WMS domain test constants namespace."""

        # NOTE (multi-agent, bead mro-nwc.19): inherit test constants only from
        # FlextTestsConstants.Tests (canonical). The production constants.Tests namespace
        # was removed — it held only a dead PATCH_TARGET test-mock path (test concern
        # leaking into production constants). Matches sibling target projects.
        class Tests(FlextTestsConstants.Tests):
            """Target Oracle WMS-specific test constants."""

            PROJECT_ROOT_PARENT_DEPTH: Final[int] = 1
            SRC_DIR: Final[str] = "src"
            PACKAGE_DIR: Final[str] = "flext_target_oracle_wms"
            ALLOWED_MODULE_FUNCTIONS: Final[dict[str, frozenset[str]]] = {
                "cli.py": frozenset({"main"})
            }
            PERF_ITERATIONS: Final[int] = 500
            PERF_THRESHOLD_SEC: Final[float] = 5.0
            MIN_EXAMPLE_FILE_COUNT: Final[int] = 4
            MIN_MODULE_DOCSTRING_LENGTH: Final[int] = 50
            MIN_FUNCTION_DOCSTRING_LENGTH: Final[int] = 10
            MIN_DOCUMENTED_FUNCTION_RATIO: Final[float] = 0.8
            MIN_README_LENGTH: Final[int] = 1000
            MIN_EXAMPLE_STEM_LENGTH: Final[int] = 5
            MIN_SEMVER_SEPARATOR_COUNT: Final[int] = 2


c = TestsFlextTargetOracleWmsConstants
__all__: list[str] = ["TestsFlextTargetOracleWmsConstants", "c"]
