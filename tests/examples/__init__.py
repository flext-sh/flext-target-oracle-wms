# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Tests for examples directory - REAL flext-* API validation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

    from tests.examples.test_examples import (
        TestExamplesCodeQuality,
        TestExamplesFlextIntegration,
        TestExamplesImportability,
        TestExamplesStructure,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "TestExamplesCodeQuality": (
        "tests.examples.test_examples",
        "TestExamplesCodeQuality",
    ),
    "TestExamplesFlextIntegration": (
        "tests.examples.test_examples",
        "TestExamplesFlextIntegration",
    ),
    "TestExamplesImportability": (
        "tests.examples.test_examples",
        "TestExamplesImportability",
    ),
    "TestExamplesStructure": ("tests.examples.test_examples", "TestExamplesStructure"),
}

__all__ = [
    "TestExamplesCodeQuality",
    "TestExamplesFlextIntegration",
    "TestExamplesImportability",
    "TestExamplesStructure",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
