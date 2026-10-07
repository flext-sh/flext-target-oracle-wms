"""Governance checks for target-oracle-wms module structure.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/unit/test_module_governance
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModuleGovernanceMixin

from tests import c, m


class TestsFlextTargetOracleWmsModuleGovernance(FlextTestsModuleGovernanceMixin):
    """Behavior contract for test_module_governance."""

    _test_file = __file__
    _tests_config = c.TargetOracleWms.Tests

    @staticmethod
    def test_target_oracle_wms_namespace_does_not_define_local_singer_message_models() -> (
        None
    ):
        """Test target oracle wms namespace does not define local singer message models."""
        assert hasattr(m.TargetOracleWms, "SingerFieldSchema")
        assert hasattr(m.TargetOracleWms, "SingerSchemaProperties")
        assert not hasattr(m.TargetOracleWms, "SingerSchemaMessage")
        assert not hasattr(m.TargetOracleWms, "SingerRecordMessage")
        assert not hasattr(m.TargetOracleWms, "SingerCatalogEntry")
