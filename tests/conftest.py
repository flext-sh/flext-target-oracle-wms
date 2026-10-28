"""Pytest configuration for target-oracle-wms tests.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

import pytest


@pytest.fixture(scope="class")
def examples_dir() -> Path:
    """Get examples directory path.

    Returns:
        The resulting ``Path``.

    """
    project_root = Path(__file__).parents[1]
    return project_root / "examples"


@pytest.fixture(scope="class")
def example_files(examples_dir: Path) -> Sequence[Path]:
    """Get all Python example files (excluding __init__.py).

    Returns:
        The resulting ``Sequence[Path]``.

    """
    return [f for f in examples_dir.glob("*.py") if f.name != "__init__.py"]
