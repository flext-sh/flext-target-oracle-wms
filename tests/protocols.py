"""Protocols for flext-target-oracle-wms tests - uses p.Wms.Tests.* namespace pattern.

This module provides test-specific protocols that extend the main flext-target-oracle-wms protocols.
Uses the unified namespace pattern p.Wms.Tests.* for test-only objects.
Combines FlextTestsProtocols functionality with project-specific test protocols.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_target_oracle_wms.models import FlextTargetOracleWmsModels


class TestsFlextTargetOracleWmsProtocols(FlextTestsProtocols):
    """Test protocols combining FlextTestsProtocols and project-specific protocols."""

    class Wms(FlextTargetOracleWmsModels):
        """Wms domain protocols extending project protocols."""

        class Tests:
            """Internal tests declarations."""


p = TestsFlextTargetOracleWmsProtocols
__all__ = ["TestsFlextTargetOracleWmsProtocols", "p"]
