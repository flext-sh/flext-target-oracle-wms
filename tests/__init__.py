# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

if _t.TYPE_CHECKING:
    import tests.conftest as _tests_conftest

    conftest = _tests_conftest
    import tests.constants as _tests_constants

    constants = _tests_constants
    import tests.examples as _tests_examples
    from tests.constants import (
        TestsFlextTargetOracleWmsConstants,
        TestsFlextTargetOracleWmsConstants as c,
    )

    examples = _tests_examples
    import tests.integration as _tests_integration

    integration = _tests_integration
    import tests.models as _tests_models

    models = _tests_models
    import tests.protocols as _tests_protocols
    from tests.models import (
        TestsFlextTargetOracleWmsModels,
        TestsFlextTargetOracleWmsModels as m,
    )

    protocols = _tests_protocols
    import tests.test_benchmarks as _tests_test_benchmarks
    from tests.protocols import (
        TestsFlextTargetOracleWmsProtocols,
        TestsFlextTargetOracleWmsProtocols as p,
    )

    test_benchmarks = _tests_test_benchmarks
    import tests.test_catalog as _tests_test_catalog

    test_catalog = _tests_test_catalog
    import tests.test_features as _tests_test_features

    test_features = _tests_test_features
    import tests.test_module_governance as _tests_test_module_governance

    test_module_governance = _tests_test_module_governance
    import tests.test_oracle_wms_cli as _tests_test_oracle_wms_cli

    test_oracle_wms_cli = _tests_test_oracle_wms_cli
    import tests.test_oracle_wms_factory as _tests_test_oracle_wms_factory

    test_oracle_wms_factory = _tests_test_oracle_wms_factory
    import tests.test_oracle_wms_init as _tests_test_oracle_wms_init

    test_oracle_wms_init = _tests_test_oracle_wms_init
    import tests.test_quality as _tests_test_quality

    test_quality = _tests_test_quality
    import tests.test_sinks as _tests_test_sinks

    test_sinks = _tests_test_sinks
    import tests.test_stream as _tests_test_stream

    test_stream = _tests_test_stream
    import tests.test_structure as _tests_test_structure

    test_structure = _tests_test_structure
    import tests.test_target as _tests_test_target

    test_target = _tests_test_target
    import tests.test_wms_patterns as _tests_test_wms_patterns

    test_wms_patterns = _tests_test_wms_patterns
    import tests.test_workflow as _tests_test_workflow

    test_workflow = _tests_test_workflow
    import tests.typings as _tests_typings

    typings = _tests_typings
    import tests.utilities as _tests_utilities
    from tests.typings import (
        TestsFlextTargetOracleWmsTypes,
        TestsFlextTargetOracleWmsTypes as t,
    )

    utilities = _tests_utilities
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
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
