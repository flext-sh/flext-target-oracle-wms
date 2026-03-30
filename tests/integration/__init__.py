# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Integration tests for FLEXT Target Oracle WMS.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from tests.integration import test_oracle as test_oracle
    from tests.integration.test_oracle import (
        TestMultiStreamIntegration as TestMultiStreamIntegration,
        TestTargetLifecycle as TestTargetLifecycle,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "TestMultiStreamIntegration": [
        "tests.integration.test_oracle",
        "TestMultiStreamIntegration",
    ],
    "TestTargetLifecycle": ["tests.integration.test_oracle", "TestTargetLifecycle"],
    "test_oracle": ["tests.integration.test_oracle", ""],
}

_EXPORTS: Sequence[str] = [
    "TestMultiStreamIntegration",
    "TestTargetLifecycle",
    "test_oracle",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
