"""Test models for flext-target-oracle-wms tests.

Provides TestsFlextTargetOracleWmsModels, extending FlextTestsModels with
flext-target-oracle-wms-specific models using COMPOSITION INHERITANCE.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests.models import FlextTestsModels

from flext_target_oracle_wms.models import FlextTargetOracleWmsModels


class TestsFlextTargetOracleWmsModels(FlextTestsModels, FlextTargetOracleWmsModels):
    """Models for flext-target-oracle-wms tests using COMPOSITION INHERITANCE.

    MANDATORY: Inherits from BOTH:
    1. FlextTestsModels - for test infrastructure (.Tests.*)
    2. FlextTargetOracleWmsModels - for domain models

    Access patterns:
    - tm.Tests.* (generic test models from FlextTestsModels)
    - tm.* (Target Oracle WMS domain models)
    - m.* (production models via alternative alias)
    """

    class Tests:
        """Project-specific test fixtures namespace."""

        class TargetOracleWms:
            """Target Oracle WMS-specific test fixtures."""


# Short aliases per FLEXT convention
tm = TestsFlextTargetOracleWmsModels
m = TestsFlextTargetOracleWmsModels

__all__ = [
    "TestsFlextTargetOracleWmsModels",
    "m",
    "tm",
]
