# AUTO-GENERATED FILE — Regenerate with: make gen
"""Examples package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_target_oracle_wms.tests.examples.test_examples import (
        TestsFlextTargetOracleWmsExamples as TestsFlextTargetOracleWmsExamples,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_examples": ("TestsFlextTargetOracleWmsExamples",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
