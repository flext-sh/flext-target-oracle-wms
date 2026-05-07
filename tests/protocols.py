"""Protocols for flext-target-oracle-wms tests - uses p.Wms.Tests.* namespace pattern.

This module provides test-specific protocols that extend the main flext-target-oracle-wms protocols.
Uses the unified namespace pattern p.Wms.Tests.* for test-only objects.
Combines TestsFlextProtocols functionality with project-specific test protocols.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_target_oracle_wms import p


class TestsFlextTargetOracleWmsProtocols(
    FlextTestsProtocols,
    p,
):
    """Test protocols combining TestsFlextProtocols and project-specific protocols."""

    class TargetOracleWms(p.TargetOracleWms):
        """TargetOracleWms domain protocols extending project protocols."""

        class Tests:
            """Internal tests declarations."""


p = TestsFlextTargetOracleWmsProtocols
__all__: list[str] = ["TestsFlextTargetOracleWmsProtocols", "p"]
