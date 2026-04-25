# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if _t.TYPE_CHECKING:
    from flext_tests import td, tf, tk, tm, tv

    from flext_target_oracle_wms import d, e, h, r, s, x
    from tests.constants import TestsFlextTargetOracleWmsConstants, c
    from tests.examples.test_examples import TestsFlextTargetOracleWmsExamples
    from tests.integration.test_oracle import TestsFlextTargetOracleWmsOracle
    from tests.models import TestsFlextTargetOracleWmsModels, m
    from tests.protocols import TestsFlextTargetOracleWmsProtocols, p
    from tests.typings import TestsFlextTargetOracleWmsTypes, t
    from tests.unit.test_benchmarks import TestsFlextTargetOracleWmsBenchmarks
    from tests.unit.test_catalog import TestsFlextTargetOracleWmsCatalog
    from tests.unit.test_features import TestsFlextTargetOracleWmsFeatures
    from tests.unit.test_module_governance import (
        TestsFlextTargetOracleWmsModuleGovernance,
    )
    from tests.unit.test_oracle_wms_cli import TestsFlextTargetOracleWmsOracleWmsCli
    from tests.unit.test_oracle_wms_factory import (
        TestsFlextTargetOracleWmsOracleWmsFactory,
    )
    from tests.unit.test_oracle_wms_init import TestsFlextTargetOracleWmsOracleWmsInit
    from tests.unit.test_quality import TestsFlextTargetOracleWmsQuality
    from tests.unit.test_sinks import TestsFlextTargetOracleWmsSinks
    from tests.unit.test_stream import TestsFlextTargetOracleWmsStream
    from tests.unit.test_structure import TestsFlextTargetOracleWmsStructure
    from tests.unit.test_target import TestsFlextTargetOracleWmsTarget
    from tests.unit.test_wms_patterns import TestsFlextTargetOracleWmsWmsPatterns
    from tests.unit.test_workflow import TestsFlextTargetOracleWmsWorkflow
    from tests.utilities import TestsFlextTargetOracleWmsUtilities, u
_LAZY_IMPORTS = merge_lazy_imports(
    (
        ".examples",
        ".integration",
        ".unit",
    ),
    build_lazy_import_map(
        {
            ".constants": (
                "TestsFlextTargetOracleWmsConstants",
                "c",
            ),
            ".examples.test_examples": ("TestsFlextTargetOracleWmsExamples",),
            ".integration.test_oracle": ("TestsFlextTargetOracleWmsOracle",),
            ".models": (
                "TestsFlextTargetOracleWmsModels",
                "m",
            ),
            ".protocols": (
                "TestsFlextTargetOracleWmsProtocols",
                "p",
            ),
            ".typings": (
                "TestsFlextTargetOracleWmsTypes",
                "t",
            ),
            ".unit.test_benchmarks": ("TestsFlextTargetOracleWmsBenchmarks",),
            ".unit.test_catalog": ("TestsFlextTargetOracleWmsCatalog",),
            ".unit.test_features": ("TestsFlextTargetOracleWmsFeatures",),
            ".unit.test_module_governance": (
                "TestsFlextTargetOracleWmsModuleGovernance",
            ),
            ".unit.test_oracle_wms_cli": ("TestsFlextTargetOracleWmsOracleWmsCli",),
            ".unit.test_oracle_wms_factory": (
                "TestsFlextTargetOracleWmsOracleWmsFactory",
            ),
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
            "flext_target_oracle_wms": (
                "d",
                "e",
                "h",
                "r",
                "s",
                "x",
            ),
            "flext_tests": (
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
            ),
        },
    ),
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
    module_name=__name__,
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "TestsFlextTargetOracleWmsBenchmarks",
    "TestsFlextTargetOracleWmsCatalog",
    "TestsFlextTargetOracleWmsConstants",
    "TestsFlextTargetOracleWmsExamples",
    "TestsFlextTargetOracleWmsFeatures",
    "TestsFlextTargetOracleWmsModels",
    "TestsFlextTargetOracleWmsModuleGovernance",
    "TestsFlextTargetOracleWmsOracle",
    "TestsFlextTargetOracleWmsOracleWmsCli",
    "TestsFlextTargetOracleWmsOracleWmsFactory",
    "TestsFlextTargetOracleWmsOracleWmsInit",
    "TestsFlextTargetOracleWmsProtocols",
    "TestsFlextTargetOracleWmsQuality",
    "TestsFlextTargetOracleWmsSinks",
    "TestsFlextTargetOracleWmsStream",
    "TestsFlextTargetOracleWmsStructure",
    "TestsFlextTargetOracleWmsTarget",
    "TestsFlextTargetOracleWmsTypes",
    "TestsFlextTargetOracleWmsUtilities",
    "TestsFlextTargetOracleWmsWmsPatterns",
    "TestsFlextTargetOracleWmsWorkflow",
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
]
