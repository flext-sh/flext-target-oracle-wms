"""Models for flext-target-oracle-wms tests - uses m.Wms.Tests.* namespace pattern.

This module provides test-specific models that extend the main flext-target-oracle-wms models.
Uses the unified namespace pattern m.Wms.Tests.* for test-only objects.
Combines m functionality with project-specific test models.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tests import m

from flext_target_oracle_wms import FlextTargetOracleWmsModels


class TestsFlextTargetOracleWmsModels(m, FlextTargetOracleWmsModels):
    """Test models combining m and project-specific models."""

    class Wms(FlextTargetOracleWmsModels):
        """Wms domain models extending project models."""

        class Tests:
            """Internal tests declarations."""


tm = TestsFlextTargetOracleWmsModels
m = TestsFlextTargetOracleWmsModels

__all__ = ["TestsFlextTargetOracleWmsModels", "m", "tm"]
