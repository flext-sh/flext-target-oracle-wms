# AUTO-GENERATED FILE — Regenerate with: make gen
"""Examples package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if _t.TYPE_CHECKING:
    from examples.test_examples import (
        TestExamplesCodeQuality,
        TestExamplesFlextIntegration,
        TestExamplesImportability,
        TestExamplesStructure,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_examples": (
            "TestExamplesCodeQuality",
            "TestExamplesFlextIntegration",
            "TestExamplesImportability",
            "TestExamplesStructure",
        ),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "TestExamplesCodeQuality",
    "TestExamplesFlextIntegration",
    "TestExamplesImportability",
    "TestExamplesStructure",
]
