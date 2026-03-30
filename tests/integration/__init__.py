# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Integration tests for FLEXT Target Oracle WMS.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from tests.integration.test_oracle import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "TestMultiStreamIntegration": "tests.integration.test_oracle",
    "TestTargetLifecycle": "tests.integration.test_oracle",
    "test_oracle": "tests.integration.test_oracle",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
