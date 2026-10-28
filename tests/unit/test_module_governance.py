"""Governance checks for target-oracle-wms module structure.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/unit/test_module_governance
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from tests import m, tm, u


class TestsFlextTargetOracleWmsModuleGovernance(u.FlextTestsModuleGovernanceMixin):
    """Behavior contract for test_module_governance."""

    _test_file = __file__

    @staticmethod
    def test_namespace_does_not_define_local_singer_message_models() -> None:
        """The namespace does not define local Singer message models."""
        tm.that(hasattr(m.TargetOracleWms, "SingerFieldSchema"))
        tm.that(hasattr(m.TargetOracleWms, "SingerSchemaProperties"))
        tm.that(hasattr(m.TargetOracleWms, "SingerSchemaMessage"), eq=False)
        tm.that(hasattr(m.TargetOracleWms, "SingerRecordMessage"), eq=False)
        tm.that(hasattr(m.TargetOracleWms, "SingerCatalogEntry"), eq=False)
