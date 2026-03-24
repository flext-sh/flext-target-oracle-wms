"""Test basic structure is correct after fixing dual structure.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import importlib.util

from flext_target_oracle_wms import FlextTargetOracleWms


def test_import_from_correct_module() -> None:
    """Test that we can import from the correct module."""
    assert FlextTargetOracleWms is not None
    if FlextTargetOracleWms.name != "target-oracle-wms":
        msg: str = f"Expected {'target-oracle-wms'}, got {FlextTargetOracleWms.name}"
        raise AssertionError(msg)


def test_no_dual_structure() -> None:
    """Test that flext_target_oracle_wms module exists correctly."""
    spec = importlib.util.find_spec("flext_target_oracle_wms")
    assert spec is not None, "flext_target_oracle_wms module should exist"
