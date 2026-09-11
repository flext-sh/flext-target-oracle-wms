"""Governance checks for target-oracle-wms module structure."""

from __future__ import annotations

from flext_tests.utilities import ModuleGovernanceMixin

from tests import c, m


class TestsFlextTargetOracleWmsModuleGovernance(ModuleGovernanceMixin):
    """Behavior contract for test_module_governance."""

    _test_file = __file__
    _tests_config = c.TargetOracleWms.Tests

    def test_target_oracle_wms_namespace_does_not_define_local_singer_message_models(
        self,
    ) -> None:
        assert hasattr(m.TargetOracleWms, "SingerFieldSchema")
        assert hasattr(m.TargetOracleWms, "SingerSchemaProperties")
        assert not hasattr(m.TargetOracleWms, "SingerSchemaMessage")
        assert not hasattr(m.TargetOracleWms, "SingerRecordMessage")
        assert not hasattr(m.TargetOracleWms, "SingerCatalogEntry")


__all__: list[str] = ["TestsFlextTargetOracleWmsModuleGovernance"]
