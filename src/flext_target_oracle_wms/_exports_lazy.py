# AUTO-GENERATED FILE — Regenerate with: make gen
"""Lazy export registry."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, merge_lazy_imports

_LOCAL_LAZY_IMPORTS = build_lazy_import_map(
    {
        "._constants": ("_constants",),
        "._utilities": ("_utilities",),
        ".api": (
            "FlextTargetOracleWmsService",
            "target_oracle_wms",
        ),
        ".cli": (
            "FlextTargetOracleWmsCli",
            "main",
        ),
        ".constants": (
            "FlextTargetOracleWmsConstants",
            "c",
        ),
        ".factory": (
            "FlextTargetFactory",
            "FlextTargetMonitoringFactory",
        ),
        ".models": (
            "FlextTargetOracleWmsModels",
            "m",
        ),
        ".protocols": (
            "FlextTargetOracleWmsProtocols",
            "p",
        ),
        ".settings": ("FlextTargetOracleWmsSettings",),
        ".typings": (
            "FlextTargetOracleWmsTypes",
            "t",
        ),
        ".utilities": (
            "FlextTargetOracleWmsUtilities",
            "u",
        ),
    },
)

FLEXT_TARGET_ORACLE_WMS_LAZY_IMPORTS = merge_lazy_imports(
    (),
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
    module_name="flext_target_oracle_wms",
)

__all__: list[str] = ["FLEXT_TARGET_ORACLE_WMS_LAZY_IMPORTS"]
