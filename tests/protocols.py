"""Test protocol definitions for flext-target-oracle-wms.

Provides TestsFlextTargetOracleWmsProtocols, combining FlextTestsProtocols with
FlextTargetOracleWmsProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests.protocols import FlextTestsProtocols

from flext_target_oracle_wms.protocols import FlextTargetOracleWmsProtocols


class TestsFlextTargetOracleWmsProtocols(
    FlextTestsProtocols,
    FlextTargetOracleWmsProtocols,
):
    """Test protocols combining FlextTestsProtocols and FlextTargetOracleWmsProtocols.

    Provides access to:
    - tp.Tests.Docker.* (from FlextTestsProtocols)
    - tp.Tests.Factory.* (from FlextTestsProtocols)
    - tp.TargetOracleWms.* (from FlextTargetOracleWmsProtocols)
    """

    class Tests:
        """Project-specific test protocols.

        Extends FlextTestsProtocols.Tests with TargetOracleWms-specific protocols.
        """

        class TargetOracleWms:
            """TargetOracleWms-specific test protocols."""


# Runtime aliases
p = TestsFlextTargetOracleWmsProtocols
tp = TestsFlextTargetOracleWmsProtocols

__all__ = ["TestsFlextTargetOracleWmsProtocols", "p", "tp"]
