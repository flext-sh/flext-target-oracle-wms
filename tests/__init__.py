# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

if _t.TYPE_CHECKING:
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests import (
        conftest,
        constants,
        examples,
        integration,
        models,
        protocols,
        test_benchmarks,
        test_catalog,
        test_features,
        test_module_governance,
        test_oracle_wms_cli,
        test_oracle_wms_factory,
        test_oracle_wms_init,
        test_quality,
        test_sinks,
        test_stream,
        test_structure,
        test_target,
        test_wms_patterns,
        test_workflow,
        typings,
        utilities,
    )
    from tests.constants import (
        TestsFlextTargetOracleWmsConstants,
        TestsFlextTargetOracleWmsConstants as c,
    )
    from tests.models import (
        TestsFlextTargetOracleWmsModels,
        TestsFlextTargetOracleWmsModels as m,
    )
    from tests.protocols import (
        TestsFlextTargetOracleWmsProtocols,
        TestsFlextTargetOracleWmsProtocols as p,
    )
    from tests.typings import (
        TestsFlextTargetOracleWmsTypes,
        TestsFlextTargetOracleWmsTypes as t,
    )
    from tests.utilities import (
        TestsFlextTargetOracleWmsUtilities,
        TestsFlextTargetOracleWmsUtilities as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    (
        "tests.examples",
        "tests.integration",
    ),
    {
        "TestsFlextTargetOracleWmsConstants": (
            "tests.constants",
            "TestsFlextTargetOracleWmsConstants",
        ),
        "TestsFlextTargetOracleWmsModels": (
            "tests.models",
            "TestsFlextTargetOracleWmsModels",
        ),
        "TestsFlextTargetOracleWmsProtocols": (
            "tests.protocols",
            "TestsFlextTargetOracleWmsProtocols",
        ),
        "TestsFlextTargetOracleWmsTypes": (
            "tests.typings",
            "TestsFlextTargetOracleWmsTypes",
        ),
        "TestsFlextTargetOracleWmsUtilities": (
            "tests.utilities",
            "TestsFlextTargetOracleWmsUtilities",
        ),
        "c": ("tests.constants", "TestsFlextTargetOracleWmsConstants"),
        "conftest": "tests.conftest",
        "constants": "tests.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "examples": "tests.examples",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "integration": "tests.integration",
        "m": ("tests.models", "TestsFlextTargetOracleWmsModels"),
        "models": "tests.models",
        "p": ("tests.protocols", "TestsFlextTargetOracleWmsProtocols"),
        "protocols": "tests.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "t": ("tests.typings", "TestsFlextTargetOracleWmsTypes"),
        "test_benchmarks": "tests.test_benchmarks",
        "test_catalog": "tests.test_catalog",
        "test_features": "tests.test_features",
        "test_module_governance": "tests.test_module_governance",
        "test_oracle_wms_cli": "tests.test_oracle_wms_cli",
        "test_oracle_wms_factory": "tests.test_oracle_wms_factory",
        "test_oracle_wms_init": "tests.test_oracle_wms_init",
        "test_quality": "tests.test_quality",
        "test_sinks": "tests.test_sinks",
        "test_stream": "tests.test_stream",
        "test_structure": "tests.test_structure",
        "test_target": "tests.test_target",
        "test_wms_patterns": "tests.test_wms_patterns",
        "test_workflow": "tests.test_workflow",
        "typings": "tests.typings",
        "u": ("tests.utilities", "TestsFlextTargetOracleWmsUtilities"),
        "utilities": "tests.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)
_ = _LAZY_IMPORTS.pop("cleanup_submodule_namespace", None)
_ = _LAZY_IMPORTS.pop("install_lazy_exports", None)
_ = _LAZY_IMPORTS.pop("lazy_getattr", None)
_ = _LAZY_IMPORTS.pop("logger", None)
_ = _LAZY_IMPORTS.pop("merge_lazy_imports", None)
_ = _LAZY_IMPORTS.pop("output", None)
_ = _LAZY_IMPORTS.pop("output_reporting", None)

__all__ = [
    "TestsFlextTargetOracleWmsConstants",
    "TestsFlextTargetOracleWmsModels",
    "TestsFlextTargetOracleWmsProtocols",
    "TestsFlextTargetOracleWmsTypes",
    "TestsFlextTargetOracleWmsUtilities",
    "c",
    "conftest",
    "constants",
    "d",
    "e",
    "examples",
    "h",
    "integration",
    "m",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "t",
    "test_benchmarks",
    "test_catalog",
    "test_features",
    "test_module_governance",
    "test_oracle_wms_cli",
    "test_oracle_wms_factory",
    "test_oracle_wms_init",
    "test_quality",
    "test_sinks",
    "test_stream",
    "test_structure",
    "test_target",
    "test_wms_patterns",
    "test_workflow",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
