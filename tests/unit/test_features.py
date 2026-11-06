"""Feature verification tests for target Oracle WMS.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import math
from collections.abc import Sequence

from tests import c, tm, u


class TestsFlextTargetOracleWmsFeatures:
    """Verify core target features.

    Feature coverage: init, lifecycle, type conversion, record transformation.
    """

    @staticmethod
    def test_target_initialization() -> None:
        """Test target initialization."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        tm.that(target.name, eq=c.TargetOracleWms.TARGET_NAME)

    @staticmethod
    def test_target_setup_cleanup_lifecycle() -> None:
        """Test target setup cleanup lifecycle."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        tm.ok(target.setup())
        tm.ok(target.cleanup())

    @staticmethod
    def test_target_process_empty_lines() -> None:
        """Test target process empty lines."""
        target = u.TargetOracleWms.Target(u.TargetOracleWms.Tests.valid_config())
        tm.ok(target.process_lines([]))

    @staticmethod
    def test_type_converter_handles_all_types() -> None:
        """Test type converter handles all types."""
        converter = u.TargetOracleWms.WMSTypeConverter()
        types_and_values: Sequence[tuple[str, bool | float | str]] = [
            ("string", "hello"),
            ("integer", 42),
            ("number", math.pi),
            ("boolean", True),
            ("object", '{"key": "val"}'),
            ("array", "[1, 2]"),
        ]
        for singer_type, value in types_and_values:
            result = converter.convert_singer_to_oracle(singer_type, value)
            tm.ok(result)

    @staticmethod
    def test_type_converter_null_handling() -> None:
        """Test type converter null handling."""
        converter = u.TargetOracleWms.WMSTypeConverter()
        result = converter.convert_singer_to_oracle("string", "")
        tm.ok(result, eq="")
