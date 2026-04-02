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
    from tests.conftest import (
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
    from tests.constants import (
        FlextTargetOracleWmsTestConstants,
        FlextTargetOracleWmsTestConstants as c,
    )
    from tests.examples import (
        TestExamplesCodeQuality,
        TestExamplesFlextIntegration,
        TestExamplesImportability,
        TestExamplesStructure,
        test_examples,
    )
    from tests.integration import (
        TestMultiStreamIntegration,
        TestTargetLifecycle,
        test_oracle,
    )
    from tests.models import (
        FlextTargetOracleWmsTestModels,
        FlextTargetOracleWmsTestModels as m,
        tm,
    )
    from tests.protocols import (
        FlextTargetOracleWmsTestProtocols,
        FlextTargetOracleWmsTestProtocols as p,
    )
    from tests.test_benchmarks import (
        PERF_ITERATIONS,
        PERF_THRESHOLD_SEC,
        TestCatalogBenchmarks,
        TestDataTransformerBenchmarks,
        TestFactoryBenchmarks,
        TestSchemaMapperBenchmarks,
        TestTableManagerBenchmarks,
        TestTypeConverterBenchmarks,
    )
    from tests.test_catalog import (
        TestCatalogAddStream,
        TestCatalogGetStream,
        TestCatalogMultipleStreams,
    )
    from tests.test_features import (
        TestTargetFeatures,
        TestTransformerFeatures,
        TestUtilitiesFeatures,
    )
    from tests.test_oracle_wms_cli import (
        TestMain,
        TestOracleWMSTargetCliExecute,
        TestOracleWMSTargetCliInit,
        TestOracleWMSTargetCliLoadConfig,
    )
    from tests.test_oracle_wms_factory import (
        TestConvenienceFunctions,
        TestFlextTargetFactory,
        TestFlextTargetMonitoringFactory,
        TestMonitoredTargetCreationRequest,
        TestTargetCreationRequest,
    )
    from tests.test_oracle_wms_init import TestModuleInit
    from tests.test_quality import (
        TestClassAttributes,
        TestConstantsNamespace,
        TestModelsNamespace,
        TestProtocolsNamespace,
    )
    from tests.test_sinks import (
        TestCatalogAndTableIntegration,
        TestTargetComponentWiring,
        TestTransformationIntegration,
    )
    from tests.test_stream import (
        TestStreamProcessorInitialize,
        TestStreamProcessorMultipleStreams,
        TestStreamProcessorRecord,
    )
    from tests.test_structure import (
        test_import_from_correct_module,
        test_no_dual_structure,
    )
    from tests.test_target import (
        TestTargetHandleRecordMessage,
        TestTargetHandleSchemaMessage,
        TestTargetHandleStateMessage,
        TestTargetInit,
        TestTargetProcessLines,
        TestTargetSetupCleanup,
    )
    from tests.test_wms_patterns import (
        TestWMSDataTransformer,
        TestWMSSchemaMapper,
        TestWMSTableManager,
        TestWMSTypeConverter,
    )
    from tests.test_workflow import (
        TestCliWorkflow,
        TestErrorWorkflows,
        TestFullSingerWorkflow,
    )
    from tests.typings import (
        FlextTargetOracleWmsTestTypes,
        FlextTargetOracleWmsTestTypes as t,
    )
    from tests.utilities import (
        FlextTargetOracleWmsTestUtilities,
        FlextTargetOracleWmsTestUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
    (
        "tests.examples",
        "tests.integration",
    ),
    {
        "FlextTargetOracleWmsTestConstants": "tests.constants",
        "FlextTargetOracleWmsTestModels": "tests.models",
        "FlextTargetOracleWmsTestProtocols": "tests.protocols",
        "FlextTargetOracleWmsTestTypes": "tests.typings",
        "FlextTargetOracleWmsTestUtilities": "tests.utilities",
        "PERF_ITERATIONS": "tests.test_benchmarks",
        "PERF_THRESHOLD_SEC": "tests.test_benchmarks",
        "TestCatalogAddStream": "tests.test_catalog",
        "TestCatalogAndTableIntegration": "tests.test_sinks",
        "TestCatalogBenchmarks": "tests.test_benchmarks",
        "TestCatalogGetStream": "tests.test_catalog",
        "TestCatalogMultipleStreams": "tests.test_catalog",
        "TestClassAttributes": "tests.test_quality",
        "TestCliWorkflow": "tests.test_workflow",
        "TestConstantsNamespace": "tests.test_quality",
        "TestConvenienceFunctions": "tests.test_oracle_wms_factory",
        "TestDataTransformerBenchmarks": "tests.test_benchmarks",
        "TestErrorWorkflows": "tests.test_workflow",
        "TestFactoryBenchmarks": "tests.test_benchmarks",
        "TestFlextTargetFactory": "tests.test_oracle_wms_factory",
        "TestFlextTargetMonitoringFactory": "tests.test_oracle_wms_factory",
        "TestFullSingerWorkflow": "tests.test_workflow",
        "TestMain": "tests.test_oracle_wms_cli",
        "TestModelsNamespace": "tests.test_quality",
        "TestModuleInit": "tests.test_oracle_wms_init",
        "TestMonitoredTargetCreationRequest": "tests.test_oracle_wms_factory",
        "TestOracleWMSTargetCliExecute": "tests.test_oracle_wms_cli",
        "TestOracleWMSTargetCliInit": "tests.test_oracle_wms_cli",
        "TestOracleWMSTargetCliLoadConfig": "tests.test_oracle_wms_cli",
        "TestProtocolsNamespace": "tests.test_quality",
        "TestSchemaMapperBenchmarks": "tests.test_benchmarks",
        "TestStreamProcessorInitialize": "tests.test_stream",
        "TestStreamProcessorMultipleStreams": "tests.test_stream",
        "TestStreamProcessorRecord": "tests.test_stream",
        "TestTableManagerBenchmarks": "tests.test_benchmarks",
        "TestTargetComponentWiring": "tests.test_sinks",
        "TestTargetCreationRequest": "tests.test_oracle_wms_factory",
        "TestTargetFeatures": "tests.test_features",
        "TestTargetHandleRecordMessage": "tests.test_target",
        "TestTargetHandleSchemaMessage": "tests.test_target",
        "TestTargetHandleStateMessage": "tests.test_target",
        "TestTargetInit": "tests.test_target",
        "TestTargetProcessLines": "tests.test_target",
        "TestTargetSetupCleanup": "tests.test_target",
        "TestTransformationIntegration": "tests.test_sinks",
        "TestTransformerFeatures": "tests.test_features",
        "TestTypeConverterBenchmarks": "tests.test_benchmarks",
        "TestUtilitiesFeatures": "tests.test_features",
        "TestWMSDataTransformer": "tests.test_wms_patterns",
        "TestWMSSchemaMapper": "tests.test_wms_patterns",
        "TestWMSTableManager": "tests.test_wms_patterns",
        "TestWMSTypeConverter": "tests.test_wms_patterns",
        "c": ("tests.constants", "FlextTargetOracleWmsTestConstants"),
        "config": "tests.conftest",
        "conftest": "tests.conftest",
        "constants": "tests.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "examples": "tests.examples",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "integration": "tests.integration",
        "m": ("tests.models", "FlextTargetOracleWmsTestModels"),
        "models": "tests.models",
        "p": ("tests.protocols", "FlextTargetOracleWmsTestProtocols"),
        "protocols": "tests.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "sample_inventory_records": "tests.conftest",
        "sample_order_records": "tests.conftest",
        "sample_task_records": "tests.conftest",
        "singer_record_message": "tests.conftest",
        "singer_schema": "tests.conftest",
        "singer_schema_message": "tests.conftest",
        "singer_state_message": "tests.conftest",
        "t": ("tests.typings", "FlextTargetOracleWmsTestTypes"),
        "temp_output_dir": "tests.conftest",
        "test_benchmarks": "tests.test_benchmarks",
        "test_catalog": "tests.test_catalog",
        "test_features": "tests.test_features",
        "test_import_from_correct_module": "tests.test_structure",
        "test_no_dual_structure": "tests.test_structure",
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
        "tm": "tests.models",
        "typings": "tests.typings",
        "u": ("tests.utilities", "FlextTargetOracleWmsTestUtilities"),
        "utilities": "tests.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
