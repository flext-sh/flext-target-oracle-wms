# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_benchmarks": ("test_benchmarks",),
        ".test_catalog": ("test_catalog",),
        ".test_features": ("test_features",),
        ".test_module_governance": ("test_module_governance",),
        ".test_oracle_wms_cli": ("test_oracle_wms_cli",),
        ".test_oracle_wms_factory": ("test_oracle_wms_factory",),
        ".test_oracle_wms_init": ("test_oracle_wms_init",),
        ".test_quality": ("test_quality",),
        ".test_sinks": ("test_sinks",),
        ".test_stream": ("test_stream",),
        ".test_structure": ("test_structure",),
        ".test_target": ("test_target",),
        ".test_wms_patterns": ("test_wms_patterns",),
        ".test_workflow": ("test_workflow",),
        "flext_target_oracle_wms": (
            "c",
            "d",
            "e",
            "h",
            "m",
            "p",
            "r",
            "s",
            "t",
            "u",
            "x",
        ),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
