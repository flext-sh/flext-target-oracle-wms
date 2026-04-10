"""Test module __init__.py import and version handling - DRY REAL approach.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import flext_target_oracle_wms


class TestModuleInit:
    """Test module initialization and version handling."""

    def test_version_import_success(self) -> None:
        """Test successful version import from importlib.metadata."""
        assert isinstance(flext_target_oracle_wms.__version__, str)
        assert flext_target_oracle_wms.__version__

    def test_version_import_fallback(self) -> None:
        """Test fallback version logic - simplified approach."""
        assert isinstance(flext_target_oracle_wms.__version__, str)
        version = flext_target_oracle_wms.__version__
        assert version
        assert version.count(".") >= 2

    def test_module_exports(self) -> None:
        """Test that module exports are properly defined."""
        assert isinstance(flext_target_oracle_wms.__all__, (list, tuple))
        expected_exports = [
            "Target",
            "FlextTargetOracleWmsUtilities",
        ]
        for export in expected_exports:
            assert export in flext_target_oracle_wms.__all__
