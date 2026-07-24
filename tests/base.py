"""Service base for flext-target-oracle-wms tests."""

from __future__ import annotations

from typing import override

from flext_target_oracle_wms import m
from flext_tests import s as tests_s
from tests.settings import TestsFlextTargetOracleWmsSettings


class TestsFlextTargetOracleWmsServiceBase(tests_s):
    """Target Oracle WMS test service base with source and test settings namespaces."""

    # NOTE (multi-agent, bead mro-nwc.19): fetch_settings is delivered by the flext_tests
    # base via MRO (resolves test_settings_type() from _runtime_bootstrap_options below).
    # The prior empty override shadowed it and returned None (silent bug, pyrefly bad-return).
    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(
            settings_type=TestsFlextTargetOracleWmsSettings
        )


s = TestsFlextTargetOracleWmsServiceBase

__all__: list[str] = ["TestsFlextTargetOracleWmsServiceBase", "s"]
