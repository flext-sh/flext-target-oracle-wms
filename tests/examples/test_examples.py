"""Runtime behavior tests for the flext-target-oracle-wms examples.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import runpy
from collections.abc import Sequence
from typing import TYPE_CHECKING

from tests import tm

if TYPE_CHECKING:
    from pathlib import Path


class TestsFlextTargetOracleWmsExamples:
    """Every runnable example executes its public entry to completion."""

    @staticmethod
    def test_examples_run_to_completion(example_files: Sequence[Path]) -> None:
        """Load each example by file path and run its facade's ``main`` entry."""
        runnable = [path for path in example_files if path.name.startswith("example_")]
        tm.that(len(runnable), gt=0, msg="No runnable example found")
        for path in runnable:
            namespace = runpy.run_path(str(path))
            for name in namespace["__all__"]:
                entry = namespace[name]
                tm.that(entry.main(), eq=True, msg=f"{path.name} {name}.main failed")
