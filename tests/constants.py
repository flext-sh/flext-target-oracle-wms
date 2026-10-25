"""Module skeleton for TestsFlextTargetOracleWmsConstants.

Test constants for flext-target-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_tests import FlextTestsConstants

from flext_target_oracle_wms import FlextTargetOracleWmsConstants


class TestsFlextTargetOracleWmsConstants(
    FlextTargetOracleWmsConstants,
    FlextTestsConstants,
):
    """Test constants for flext-target-oracle-wms."""

    class TargetOracleWms(FlextTargetOracleWmsConstants.TargetOracleWms):
        """Target Oracle WMS domain test constants namespace."""

        # NOTE (multi-agent, bead mro-nwc.19): inherit test constants only from
        # FlextTestsConstants.Tests (canonical). The production constants.Tests
        # namespace
        # was removed — it held only a dead PATCH_TARGET test-mock path (test concern
        # leaking into production constants). Matches sibling target projects.
        class Tests(FlextTestsConstants.Tests):
            """Target Oracle WMS-specific test constants."""

            PERF_ITERATIONS: ClassVar[int] = 500
            PERF_THRESHOLD_SEC: ClassVar[float] = 5.0
            MIN_SEMVER_SEPARATOR_COUNT: ClassVar[int] = 2
            # Scenario data for the WMS auth block; the secret is generated per
            # build (``u.TargetOracleWms.Tests.valid_config``), never a literal.
            WMS_BASE_URL: ClassVar[str] = "https://test.wms.example.com"
            WMS_USERNAME: ClassVar[str] = "user"
            WMS_SECRET_BYTES: ClassVar[int] = 16
            DEFAULT_STREAM: ClassVar[str] = "test_stream"
            BENCH_STREAM: ClassVar[str] = "bench"
            CONFIG_FILE_NAME: ClassVar[str] = "settings.json"


c = TestsFlextTargetOracleWmsConstants
__all__: list[str] = ["TestsFlextTargetOracleWmsConstants", "c"]
