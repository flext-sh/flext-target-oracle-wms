"""Runtime settings for flext-target-oracle-wms tests.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/settings
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsSettings

from flext_target_oracle_wms import FlextTargetOracleWmsSettings


class TestsFlextTargetOracleWmsSettings(
    FlextTargetOracleWmsSettings,
    FlextTestsSettings,
):
    """Target Oracle WMS settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextTargetOracleWmsSettings"]
