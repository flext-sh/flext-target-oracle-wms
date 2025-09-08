"""Test basic structure is correct after fixing dual structure.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

import importlib.util

from flext_target_oracle_wms import TargetOracleWMS


def test_import_from_correct_module() -> None:
    """Test that we can import from the correct module."""
    assert TargetOracleWMS is not None
    if TargetOracleWMS.name != "target-oracle-wms":
        msg: str = f"Expected {'target-oracle-wms'}, got {TargetOracleWMS.name}"
        raise AssertionError(msg)


def test_no_dual_structure() -> None:
    """Test that old target_oracle_wms module doesn't exist."""
    try:
        spec = importlib.util.find_spec("target_oracle_wms")
        if spec is not None:
            msg = "target_oracle_wms module should not exist"
            raise AssertionError(msg)
    except ImportError:
        # This is expected
        pass
