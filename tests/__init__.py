# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import tests.conftest as _tests_conftest

    conftest = _tests_conftest
    import tests.constants as _tests_constants
    from tests.conftest import pytest_plugins

    constants = _tests_constants
    import tests.models as _tests_models
    from tests.constants import (
        FlextTargetOracleWmsTestConstants,
        FlextTargetOracleWmsTestConstants as c,
    )

    models = _tests_models
    import tests.protocols as _tests_protocols
    from tests.models import (
        FlextTargetOracleWmsTestModels,
        FlextTargetOracleWmsTestModels as m,
        tm,
    )

    protocols = _tests_protocols
    import tests.test_benchmarks as _tests_test_benchmarks
    from tests.protocols import (
        FlextTargetOracleWmsTestProtocols,
        FlextTargetOracleWmsTestProtocols as p,
    )

    test_benchmarks = _tests_test_benchmarks
    import tests.test_catalog as _tests_test_catalog
    from tests.test_benchmarks import PERF_ITERATIONS, PERF_THRESHOLD_SEC

    test_catalog = _tests_test_catalog
    import tests.test_features as _tests_test_features

    test_features = _tests_test_features
    import tests.test_module_governance as _tests_test_module_governance

    test_module_governance = _tests_test_module_governance
    import tests.test_oracle_wms_cli as _tests_test_oracle_wms_cli
    from tests.test_module_governance import ALLOWED_MODULE_FUNCTIONS, PACKAGE_ROOT

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
        FlextTargetOracleWmsTestTypes,
        FlextTargetOracleWmsTestTypes as t,
    )

    utilities = _tests_utilities
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests.utilities import (
        FlextTargetOracleWmsTestUtilities,
        FlextTargetOracleWmsTestUtilities as u,
    )
_LAZY_IMPORTS = {
    "ALLOWED_MODULE_FUNCTIONS": (
        "tests.test_module_governance",
        "ALLOWED_MODULE_FUNCTIONS",
    ),
    "FlextTargetOracleWmsTestConstants": (
        "tests.constants",
        "FlextTargetOracleWmsTestConstants",
    ),
    "FlextTargetOracleWmsTestModels": (
        "tests.models",
        "FlextTargetOracleWmsTestModels",
    ),
    "FlextTargetOracleWmsTestProtocols": (
        "tests.protocols",
        "FlextTargetOracleWmsTestProtocols",
    ),
    "FlextTargetOracleWmsTestTypes": ("tests.typings", "FlextTargetOracleWmsTestTypes"),
    "FlextTargetOracleWmsTestUtilities": (
        "tests.utilities",
        "FlextTargetOracleWmsTestUtilities",
    ),
    "PACKAGE_ROOT": ("tests.test_module_governance", "PACKAGE_ROOT"),
    "PERF_ITERATIONS": ("tests.test_benchmarks", "PERF_ITERATIONS"),
    "PERF_THRESHOLD_SEC": ("tests.test_benchmarks", "PERF_THRESHOLD_SEC"),
    "c": ("tests.constants", "FlextTargetOracleWmsTestConstants"),
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("tests.models", "FlextTargetOracleWmsTestModels"),
    "models": "tests.models",
    "p": ("tests.protocols", "FlextTargetOracleWmsTestProtocols"),
    "protocols": "tests.protocols",
    "pytest_plugins": ("tests.conftest", "pytest_plugins"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "t": ("tests.typings", "FlextTargetOracleWmsTestTypes"),
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
    "tm": ("tests.models", "tm"),
    "typings": "tests.typings",
    "u": ("tests.utilities", "FlextTargetOracleWmsTestUtilities"),
    "utilities": "tests.utilities",
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "ALLOWED_MODULE_FUNCTIONS",
    "PACKAGE_ROOT",
    "PERF_ITERATIONS",
    "PERF_THRESHOLD_SEC",
    "FlextTargetOracleWmsTestConstants",
    "FlextTargetOracleWmsTestModels",
    "FlextTargetOracleWmsTestProtocols",
    "FlextTargetOracleWmsTestTypes",
    "FlextTargetOracleWmsTestUtilities",
    "c",
    "conftest",
    "constants",
    "d",
    "e",
    "h",
    "m",
    "models",
    "p",
    "protocols",
    "pytest_plugins",
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
    "tm",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
