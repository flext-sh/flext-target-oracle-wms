"""Test basic structure is correct after fixing dual structure.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import importlib.util

from flext_tests import tm

from tests import c, u


class TestsFlextTargetOracleWmsStructure:
    """Behavior contract for test_structure."""

    @staticmethod
    def test_import_from_correct_module() -> None:
        """Test that we can import from the correct module."""
        tm.that(u.TargetOracleWms.Target, none=False)
        tm.that(u.TargetOracleWms.Target.name, eq=c.TargetOracleWms.TARGET_NAME)

    @staticmethod
    def test_no_dual_structure() -> None:
        """Test that flext_target_oracle_wms module exists correctly."""
        spec = importlib.util.find_spec("flext_target_oracle_wms")
        tm.that(spec, none=False)
