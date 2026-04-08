"""Models for flext-target-oracle-wms tests - uses m.Wms.Tests.* namespace pattern.

This module provides test-specific models that extend the main flext-target-oracle-wms models.
Uses the unified namespace pattern m.Wms.Tests.* for test-only objects.
Combines TestsFlextModels functionality with project-specific test models.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from flext_target_oracle_wms import FlextTargetOracleWmsModels


class TestsFlextTargetOracleWmsModels(FlextTestsModels, FlextTargetOracleWmsModels):
    """Test models combining TestsFlextModels and project-specific models."""

    class TargetOracleWms(FlextTargetOracleWmsModels.TargetOracleWms):
        """TargetOracleWms domain models extending project models."""

        class Tests:
            """Internal tests declarations."""


m = TestsFlextTargetOracleWmsModels

__all__ = ["TestsFlextTargetOracleWmsModels", "m"]
