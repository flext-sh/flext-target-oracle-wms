# AUTO-GENERATED FILE — Regenerate with: make gen
"""Lazy export registry."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, merge_lazy_imports

_LOCAL_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".base": (
            "TestsFlextTargetOracleWmsServiceBase",
            "s",
        ),
        ".conftest": ("conftest",),
        ".constants": (
            "TestsFlextTargetOracleWmsConstants",
            "c",
        ),
        ".examples": ("examples",),
        ".examples.test_examples": ("TestsFlextTargetOracleWmsExamples",),
        ".integration": ("integration",),
        ".integration.test_oracle": ("TestsFlextTargetOracleWmsOracle",),
        ".models": (
            "TestsFlextTargetOracleWmsModels",
            "m",
        ),
        ".protocols": (
            "TestsFlextTargetOracleWmsProtocols",
            "p",
        ),
        ".settings": ("TestsFlextTargetOracleWmsSettings",),
        ".typings": (
            "TestsFlextTargetOracleWmsTypes",
            "t",
        ),
        ".unit": ("unit",),
        ".unit.test_benchmarks": ("TestsFlextTargetOracleWmsBenchmarks",),
        ".unit.test_catalog": ("TestsFlextTargetOracleWmsCatalog",),
        ".unit.test_features": ("TestsFlextTargetOracleWmsFeatures",),
        ".unit.test_module_governance": ("TestsFlextTargetOracleWmsModuleGovernance",),
        ".unit.test_oracle_wms_cli": ("TestsFlextTargetOracleWmsOracleWmsCli",),
        ".unit.test_oracle_wms_factory": ("TestsFlextTargetOracleWmsOracleWmsFactory",),
        ".unit.test_oracle_wms_init": ("TestsFlextTargetOracleWmsOracleWmsInit",),
        ".unit.test_quality": ("TestsFlextTargetOracleWmsQuality",),
        ".unit.test_sinks": ("TestsFlextTargetOracleWmsSinks",),
        ".unit.test_stream": ("TestsFlextTargetOracleWmsStream",),
        ".unit.test_structure": ("TestsFlextTargetOracleWmsStructure",),
        ".unit.test_target": ("TestsFlextTargetOracleWmsTarget",),
        ".unit.test_wms_patterns": ("TestsFlextTargetOracleWmsWmsPatterns",),
        ".unit.test_workflow": ("TestsFlextTargetOracleWmsWorkflow",),
        ".utilities": (
            "TestsFlextTargetOracleWmsUtilities",
            "u",
        ),
        "flext_tests": (
            "d",
            "e",
            "h",
            "r",
            "td",
            "tf",
            "tk",
            "tm",
            "tv",
            "x",
        ),
    },
)

TESTS_FLEXT_TARGET_ORACLE_WMS_LAZY_IMPORTS = merge_lazy_imports(
    (
        ".examples",
        ".integration",
        ".unit",
    ),
    _LOCAL_LAZY_IMPORTS,
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
        "pytest_addoption",
        "pytest_collect_file",
        "pytest_collection_modifyitems",
        "pytest_configure",
        "pytest_runtest_setup",
        "pytest_runtest_teardown",
        "pytest_sessionfinish",
        "pytest_sessionstart",
        "pytest_terminal_summary",
        "pytest_warning_recorded",
    ),
    module_name="tests",
)

__all__: list[str] = ["TESTS_FLEXT_TARGET_ORACLE_WMS_LAZY_IMPORTS"]
