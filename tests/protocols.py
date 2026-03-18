"""Protocols for flext-target-oracle-wms tests - uses p.Wms.Tests.* namespace pattern.

This module provides test-specific protocols that extend the main flext-target-oracle-wms protocols.
Uses the unified namespace pattern p.Wms.Tests.* for test-only objects.
Combines p functionality with project-specific test protocols.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tests import p

from flext_target_oracle_wms.models import FlextTargetOracleWmsModels


class TestsFlextTargetOracleWmsProtocols(p):
    """Test protocols combining p and project-specific protocols."""

    class Wms(FlextTargetOracleWmsModels):
        """Wms domain protocols extending project protocols."""

        class Tests:
            """Internal tests declarations."""


p = TestsFlextTargetOracleWmsProtocols
__all__ = ["TestsFlextTargetOracleWmsProtocols", "p"]
