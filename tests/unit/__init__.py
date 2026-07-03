# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_benchmarks": ("TestsFlextTargetOracleWmsBenchmarks",),
        ".test_catalog": ("TestsFlextTargetOracleWmsCatalog",),
        ".test_features": ("TestsFlextTargetOracleWmsFeatures",),
        ".test_module_governance": ("TestsFlextTargetOracleWmsModuleGovernance",),
        ".test_oracle_wms_cli": ("TestsFlextTargetOracleWmsOracleWmsCli",),
        ".test_oracle_wms_factory": ("TestsFlextTargetOracleWmsOracleWmsFactory",),
        ".test_oracle_wms_init": ("TestsFlextTargetOracleWmsOracleWmsInit",),
        ".test_quality": ("TestsFlextTargetOracleWmsQuality",),
        ".test_sinks": ("TestsFlextTargetOracleWmsSinks",),
        ".test_stream": ("TestsFlextTargetOracleWmsStream",),
        ".test_structure": ("TestsFlextTargetOracleWmsStructure",),
        ".test_target": ("TestsFlextTargetOracleWmsTarget",),
        ".test_wms_patterns": ("TestsFlextTargetOracleWmsWmsPatterns",),
        ".test_workflow": ("TestsFlextTargetOracleWmsWorkflow",),
        "flext_tests": (
            "c",
            "d",
            "e",
            "h",
            "m",
            "p",
            "r",
            "s",
            "t",
            "td",
            "tf",
            "tk",
            "tm",
            "tv",
            "u",
            "x",
        ),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
