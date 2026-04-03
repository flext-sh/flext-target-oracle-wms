# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_target_oracle_wms import (
        conftest,
        constants,
        examples,
        integration,
        models,
        protocols,
        test_benchmarks,
        test_catalog,
        test_examples,
        test_features,
        test_oracle,
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
    from flext_target_oracle_wms.conftest import (
        config,
        sample_inventory_records,
        sample_order_records,
        sample_task_records,
        singer_record_message,
        singer_schema,
        singer_schema_message,
        singer_state_message,
        temp_output_dir,
    )
    from flext_target_oracle_wms.constants import (
        FlextTargetOracleWmsTestConstants,
        FlextTargetOracleWmsTestConstants as c,
    )
    from flext_target_oracle_wms.examples import TestExamplesCodeQuality
    from flext_target_oracle_wms.integration import (
        TestMultiStreamIntegration,
        TestTargetLifecycle,
    )
    from flext_target_oracle_wms.models import (
        FlextTargetOracleWmsTestModels,
        FlextTargetOracleWmsTestModels as m,
        tm,
    )
    from flext_target_oracle_wms.protocols import (
        FlextTargetOracleWmsTestProtocols,
        FlextTargetOracleWmsTestProtocols as p,
    )
    from flext_target_oracle_wms.test_benchmarks import (
        PERF_ITERATIONS,
        PERF_THRESHOLD_SEC,
    )
    from flext_target_oracle_wms.test_catalog import TestCatalogAddStream
    from flext_target_oracle_wms.test_oracle_wms_factory import (
        TestTargetCreationRequest,
    )
    from flext_target_oracle_wms.test_oracle_wms_init import TestModuleInit
    from flext_target_oracle_wms.test_quality import TestModelsNamespace
    from flext_target_oracle_wms.test_sinks import TestTargetComponentWiring
    from flext_target_oracle_wms.test_stream import TestStreamProcessorInitialize
    from flext_target_oracle_wms.test_structure import test_import_from_correct_module
    from flext_target_oracle_wms.test_target import TestTargetInit, by_alias
    from flext_target_oracle_wms.test_wms_patterns import TestWMSTypeConverter
    from flext_target_oracle_wms.typings import (
        FlextTargetOracleWmsTestTypes,
        FlextTargetOracleWmsTestTypes as t,
    )
    from flext_target_oracle_wms.utilities import (
        FlextTargetOracleWmsTestUtilities,
        FlextTargetOracleWmsTestUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
    (
        "flext_target_oracle_wms.examples",
        "flext_target_oracle_wms.integration",
    ),
    {
        "FlextTargetOracleWmsTestConstants": "flext_target_oracle_wms.constants",
        "FlextTargetOracleWmsTestModels": "flext_target_oracle_wms.models",
        "FlextTargetOracleWmsTestProtocols": "flext_target_oracle_wms.protocols",
        "FlextTargetOracleWmsTestTypes": "flext_target_oracle_wms.typings",
        "FlextTargetOracleWmsTestUtilities": "flext_target_oracle_wms.utilities",
        "PERF_ITERATIONS": "flext_target_oracle_wms.test_benchmarks",
        "PERF_THRESHOLD_SEC": "flext_target_oracle_wms.test_benchmarks",
        "TestCatalogAddStream": "flext_target_oracle_wms.test_catalog",
        "TestModelsNamespace": "flext_target_oracle_wms.test_quality",
        "TestModuleInit": "flext_target_oracle_wms.test_oracle_wms_init",
        "TestStreamProcessorInitialize": "flext_target_oracle_wms.test_stream",
        "TestTargetComponentWiring": "flext_target_oracle_wms.test_sinks",
        "TestTargetCreationRequest": "flext_target_oracle_wms.test_oracle_wms_factory",
        "TestTargetInit": "flext_target_oracle_wms.test_target",
        "TestWMSTypeConverter": "flext_target_oracle_wms.test_wms_patterns",
        "by_alias": "flext_target_oracle_wms.test_target",
        "c": ("flext_target_oracle_wms.constants", "FlextTargetOracleWmsTestConstants"),
        "config": "flext_target_oracle_wms.conftest",
        "conftest": "flext_target_oracle_wms.conftest",
        "constants": "flext_target_oracle_wms.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "examples": "flext_target_oracle_wms.examples",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "integration": "flext_target_oracle_wms.integration",
        "m": ("flext_target_oracle_wms.models", "FlextTargetOracleWmsTestModels"),
        "models": "flext_target_oracle_wms.models",
        "p": ("flext_target_oracle_wms.protocols", "FlextTargetOracleWmsTestProtocols"),
        "protocols": "flext_target_oracle_wms.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "sample_inventory_records": "flext_target_oracle_wms.conftest",
        "sample_order_records": "flext_target_oracle_wms.conftest",
        "sample_task_records": "flext_target_oracle_wms.conftest",
        "singer_record_message": "flext_target_oracle_wms.conftest",
        "singer_schema": "flext_target_oracle_wms.conftest",
        "singer_schema_message": "flext_target_oracle_wms.conftest",
        "singer_state_message": "flext_target_oracle_wms.conftest",
        "t": ("flext_target_oracle_wms.typings", "FlextTargetOracleWmsTestTypes"),
        "temp_output_dir": "flext_target_oracle_wms.conftest",
        "test_benchmarks": "flext_target_oracle_wms.test_benchmarks",
        "test_catalog": "flext_target_oracle_wms.test_catalog",
        "test_examples": "flext_target_oracle_wms.test_examples",
        "test_features": "flext_target_oracle_wms.test_features",
        "test_import_from_correct_module": "flext_target_oracle_wms.test_structure",
        "test_oracle": "flext_target_oracle_wms.test_oracle",
        "test_oracle_wms_cli": "flext_target_oracle_wms.test_oracle_wms_cli",
        "test_oracle_wms_factory": "flext_target_oracle_wms.test_oracle_wms_factory",
        "test_oracle_wms_init": "flext_target_oracle_wms.test_oracle_wms_init",
        "test_quality": "flext_target_oracle_wms.test_quality",
        "test_sinks": "flext_target_oracle_wms.test_sinks",
        "test_stream": "flext_target_oracle_wms.test_stream",
        "test_structure": "flext_target_oracle_wms.test_structure",
        "test_target": "flext_target_oracle_wms.test_target",
        "test_wms_patterns": "flext_target_oracle_wms.test_wms_patterns",
        "test_workflow": "flext_target_oracle_wms.test_workflow",
        "tm": "flext_target_oracle_wms.models",
        "typings": "flext_target_oracle_wms.typings",
        "u": ("flext_target_oracle_wms.utilities", "FlextTargetOracleWmsTestUtilities"),
        "utilities": "flext_target_oracle_wms.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
