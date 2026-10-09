"""Governance checks for target-oracle-wms module structure.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/unit/test_module_governance
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import u

from tests import m


class TestsFlextTargetOracleWmsModuleGovernance(u.FlextTestsModuleGovernanceMixin):
    """Behavior contract for test_module_governance."""

    _test_file = __file__

    @staticmethod
    def test_namespace_does_not_define_local_singer_message_models() -> None:
        """The namespace does not define local Singer message models."""
        assert hasattr(m.TargetOracleWms, "SingerFieldSchema")
        assert hasattr(m.TargetOracleWms, "SingerSchemaProperties")
        assert not hasattr(m.TargetOracleWms, "SingerSchemaMessage")
        assert not hasattr(m.TargetOracleWms, "SingerRecordMessage")
        assert not hasattr(m.TargetOracleWms, "SingerCatalogEntry")
