# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests.unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import c, d, e, h, m, p, r, s, t, td, tf, tk, tm, tv, u, x

    from .test_benchmarks import TestsFlextTargetOracleWmsBenchmarks
    from .test_catalog import TestsFlextTargetOracleWmsCatalog
    from .test_features import TestsFlextTargetOracleWmsFeatures
    from .test_module_governance import TestsFlextTargetOracleWmsModuleGovernance
    from .test_oracle_wms_cli import TestsFlextTargetOracleWmsOracleWmsCli
    from .test_oracle_wms_init import TestsFlextTargetOracleWmsOracleWmsInit
    from .test_quality import TestsFlextTargetOracleWmsQuality
    from .test_sinks import TestsFlextTargetOracleWmsSinks
    from .test_stream import TestsFlextTargetOracleWmsStream
    from .test_structure import TestsFlextTargetOracleWmsStructure
    from .test_target import TestsFlextTargetOracleWmsTarget
    from .test_wms_patterns import TestsFlextTargetOracleWmsWmsPatterns
    from .test_workflow import TestsFlextTargetOracleWmsWorkflow
__all__: tuple[str, ...] = (
    "TestsFlextTargetOracleWmsBenchmarks",
    "TestsFlextTargetOracleWmsCatalog",
    "TestsFlextTargetOracleWmsFeatures",
    "TestsFlextTargetOracleWmsModuleGovernance",
    "TestsFlextTargetOracleWmsOracleWmsCli",
    "TestsFlextTargetOracleWmsOracleWmsInit",
    "TestsFlextTargetOracleWmsQuality",
    "TestsFlextTargetOracleWmsSinks",
    "TestsFlextTargetOracleWmsStream",
    "TestsFlextTargetOracleWmsStructure",
    "TestsFlextTargetOracleWmsTarget",
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
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".test_benchmarks": ("TestsFlextTargetOracleWmsBenchmarks",),
            ".test_catalog": ("TestsFlextTargetOracleWmsCatalog",),
            ".test_features": ("TestsFlextTargetOracleWmsFeatures",),
            ".test_module_governance": ("TestsFlextTargetOracleWmsModuleGovernance",),
            ".test_oracle_wms_cli": ("TestsFlextTargetOracleWmsOracleWmsCli",),
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
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
