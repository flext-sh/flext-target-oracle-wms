# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests for examples directory - REAL flext-* API validation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from tests.examples import test_examples
    from tests.examples.test_examples import (
        TestExamplesCodeQuality,
        TestExamplesFlextIntegration,
        TestExamplesImportability,
        TestExamplesStructure,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "TestExamplesCodeQuality": "tests.examples.test_examples",
    "TestExamplesFlextIntegration": "tests.examples.test_examples",
    "TestExamplesImportability": "tests.examples.test_examples",
    "TestExamplesStructure": "tests.examples.test_examples",
    "test_examples": "tests.examples.test_examples",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
