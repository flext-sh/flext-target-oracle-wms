# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests for examples directory - REAL flext-* API validation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from tests.examples import test_examples as test_examples
    from tests.examples.test_examples import (
        TestExamplesCodeQuality as TestExamplesCodeQuality,
        TestExamplesFlextIntegration as TestExamplesFlextIntegration,
        TestExamplesImportability as TestExamplesImportability,
        TestExamplesStructure as TestExamplesStructure,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "TestExamplesCodeQuality": [
        "tests.examples.test_examples",
        "TestExamplesCodeQuality",
    ],
    "TestExamplesFlextIntegration": [
        "tests.examples.test_examples",
        "TestExamplesFlextIntegration",
    ],
    "TestExamplesImportability": [
        "tests.examples.test_examples",
        "TestExamplesImportability",
    ],
    "TestExamplesStructure": ["tests.examples.test_examples", "TestExamplesStructure"],
    "test_examples": ["tests.examples.test_examples", ""],
}

_EXPORTS: Sequence[str] = [
    "TestExamplesCodeQuality",
    "TestExamplesFlextIntegration",
    "TestExamplesImportability",
    "TestExamplesStructure",
    "test_examples",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
