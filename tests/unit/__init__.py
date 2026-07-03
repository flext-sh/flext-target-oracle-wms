# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_target_oracle_wms.tests.unit.test_benchmarks import (
        TestsFlextTargetOracleWmsBenchmarks as TestsFlextTargetOracleWmsBenchmarks,
    )
    from flext_target_oracle_wms.tests.unit.test_catalog import (
        TestsFlextTargetOracleWmsCatalog as TestsFlextTargetOracleWmsCatalog,
    )
    from flext_target_oracle_wms.tests.unit.test_features import (
        TestsFlextTargetOracleWmsFeatures as TestsFlextTargetOracleWmsFeatures,
    )
    from flext_target_oracle_wms.tests.unit.test_module_governance import (
        TestsFlextTargetOracleWmsModuleGovernance as TestsFlextTargetOracleWmsModuleGovernance,
    )
    from flext_target_oracle_wms.tests.unit.test_oracle_wms_cli import (
        TestsFlextTargetOracleWmsOracleWmsCli as TestsFlextTargetOracleWmsOracleWmsCli,
    )
    from flext_target_oracle_wms.tests.unit.test_oracle_wms_factory import (
        TestsFlextTargetOracleWmsOracleWmsFactory as TestsFlextTargetOracleWmsOracleWmsFactory,
    )
    from flext_target_oracle_wms.tests.unit.test_oracle_wms_init import (
        TestsFlextTargetOracleWmsOracleWmsInit as TestsFlextTargetOracleWmsOracleWmsInit,
    )
    from flext_target_oracle_wms.tests.unit.test_quality import (
        TestsFlextTargetOracleWmsQuality as TestsFlextTargetOracleWmsQuality,
    )
    from flext_target_oracle_wms.tests.unit.test_sinks import (
        TestsFlextTargetOracleWmsSinks as TestsFlextTargetOracleWmsSinks,
    )
    from flext_target_oracle_wms.tests.unit.test_stream import (
        TestsFlextTargetOracleWmsStream as TestsFlextTargetOracleWmsStream,
    )
    from flext_target_oracle_wms.tests.unit.test_structure import (
        TestsFlextTargetOracleWmsStructure as TestsFlextTargetOracleWmsStructure,
    )
    from flext_target_oracle_wms.tests.unit.test_target import (
        TestsFlextTargetOracleWmsTarget as TestsFlextTargetOracleWmsTarget,
    )
    from flext_target_oracle_wms.tests.unit.test_wms_patterns import (
        TestsFlextTargetOracleWmsWmsPatterns as TestsFlextTargetOracleWmsWmsPatterns,
    )
    from flext_target_oracle_wms.tests.unit.test_workflow import (
        TestsFlextTargetOracleWmsWorkflow as TestsFlextTargetOracleWmsWorkflow,
    )
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
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
