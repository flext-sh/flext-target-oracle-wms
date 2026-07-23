"""Test module __init__.py import and version handling - DRY REAL approach.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import flext_target_oracle_wms
from flext_tests import tm
from tests import c


class TestsFlextTargetOracleWmsOracleWmsInit:
    """Test module initialization and version handling."""

    def test_version_import_success(self) -> None:
        """Test successful version import from importlib.metadata."""
        tm.that(flext_target_oracle_wms.__version__, is_=str)
        assert flext_target_oracle_wms.__version__

    def test_version_import_fallback(self) -> None:
        """Test fallback version logic - simplified approach."""
        tm.that(flext_target_oracle_wms.__version__, is_=str)
        version = flext_target_oracle_wms.__version__
        assert version
        assert version.count(".") >= c.TargetOracleWms.Tests.MIN_SEMVER_SEPARATOR_COUNT

    def test_module_exports(self) -> None:
        """Test that module exports are properly defined."""
        tm.that(flext_target_oracle_wms.__all__, is_=(list, tuple))
        # NOTE (multi-agent, bead mro-nwc.19): canonical package surface only. The
        # non-canonical FlextTargetFactory (parallel creation branch) was removed —
        # creation is delivered by FlextTargetOracleWmsService (api.py) via MRO.
        expected_exports = [
            "FlextTargetOracleWmsUtilities",
            "FlextTargetOracleWmsService",
            "u",
        ]
        for export in expected_exports:
            tm.that(flext_target_oracle_wms.__all__, has=export)
        tm.that(
            flext_target_oracle_wms.u.TargetOracleWms.Client.__name__,
            eq=("FlextTargetOracleWmsUtilitiesClient"),
        )
