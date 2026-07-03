"""Runtime settings for flext-target-oracle-wms tests."""

from __future__ import annotations

from flext_tests.settings import FlextTestsSettings

from flext_target_oracle_wms import FlextTargetOracleWmsSettings


class TestsFlextTargetOracleWmsSettings(
    FlextTargetOracleWmsSettings,
    FlextTestsSettings,
):
    """Target Oracle WMS settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextTargetOracleWmsSettings"]
