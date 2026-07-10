"""Service base for flext-target-oracle-wms tests."""

from __future__ import annotations

from typing import override

from flext_tests import s as tests_s

from flext_target_oracle_wms import m
from tests.settings import TestsFlextTargetOracleWmsSettings


class TestsFlextTargetOracleWmsServiceBase(tests_s):
    """Target Oracle WMS test service base with source and test settings namespaces."""

    @classmethod
    @override
    def fetch_settings(cls) -> TestsFlextTargetOracleWmsSettings:
        """Return the typed Target Oracle WMS+Tests settings singleton."""

    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(
            settings_type=TestsFlextTargetOracleWmsSettings,
        )


s = TestsFlextTargetOracleWmsServiceBase

__all__: list[str] = ["TestsFlextTargetOracleWmsServiceBase", "s"]
