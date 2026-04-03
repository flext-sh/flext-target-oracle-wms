# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.decorators import FlextDecorators as d
from flext_core.exceptions import FlextExceptions as e
from flext_core.handlers import FlextHandlers as h
from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_core.mixins import FlextMixins as x
from flext_core.result import FlextResult as r
from flext_core.service import FlextService as s
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
from tests.examples.test_examples import (
    TestExamplesCodeQuality,
    TestExamplesFlextIntegration,
    TestExamplesImportability,
    TestExamplesStructure,
)
from tests.integration.test_oracle import (
    TestMultiStreamIntegration,
    TestTargetLifecycle,
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

if _t.TYPE_CHECKING:
    import tests.conftest as _tests_conftest

    conftest = _tests_conftest
    import tests.constants as _tests_constants

    constants = _tests_constants
    import tests.examples as _tests_examples

    examples = _tests_examples
    import tests.examples.test_examples as _tests_examples_test_examples

    test_examples = _tests_examples_test_examples
    import tests.integration as _tests_integration

    integration = _tests_integration
    import tests.integration.test_oracle as _tests_integration_test_oracle

    test_oracle = _tests_integration_test_oracle
    import tests.models as _tests_models

    models = _tests_models
    import tests.protocols as _tests_protocols

    protocols = _tests_protocols
    import tests.test_benchmarks as _tests_test_benchmarks

    test_benchmarks = _tests_test_benchmarks
    import tests.test_catalog as _tests_test_catalog

    test_catalog = _tests_test_catalog
    import tests.test_features as _tests_test_features

    test_features = _tests_test_features
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

    utilities = _tests_utilities

    _ = (
        FlextTargetOracleWmsTestConstants,
        FlextTargetOracleWmsTestModels,
        FlextTargetOracleWmsTestProtocols,
        FlextTargetOracleWmsTestTypes,
        FlextTargetOracleWmsTestUtilities,
        PERF_ITERATIONS,
        PERF_THRESHOLD_SEC,
        TestCatalogAddStream,
        TestCatalogAndTableIntegration,
        TestCatalogBenchmarks,
        TestCatalogGetStream,
        TestCatalogMultipleStreams,
        TestClassAttributes,
        TestCliWorkflow,
        TestConstantsNamespace,
        TestConvenienceFunctions,
        TestDataTransformerBenchmarks,
        TestErrorWorkflows,
        TestExamplesCodeQuality,
        TestExamplesFlextIntegration,
        TestExamplesImportability,
        TestExamplesStructure,
        TestFactoryBenchmarks,
        TestFlextTargetFactory,
        TestFlextTargetMonitoringFactory,
        TestFullSingerWorkflow,
        TestMain,
        TestModelsNamespace,
        TestModuleInit,
        TestMonitoredTargetCreationRequest,
        TestMultiStreamIntegration,
        TestOracleWMSTargetCliExecute,
        TestOracleWMSTargetCliInit,
        TestOracleWMSTargetCliLoadConfig,
        TestProtocolsNamespace,
        TestSchemaMapperBenchmarks,
        TestStreamProcessorInitialize,
        TestStreamProcessorMultipleStreams,
        TestStreamProcessorRecord,
        TestTableManagerBenchmarks,
        TestTargetComponentWiring,
        TestTargetCreationRequest,
        TestTargetFeatures,
        TestTargetHandleRecordMessage,
        TestTargetHandleSchemaMessage,
        TestTargetHandleStateMessage,
        TestTargetInit,
        TestTargetLifecycle,
        TestTargetProcessLines,
        TestTargetSetupCleanup,
        TestTransformationIntegration,
        TestTransformerFeatures,
        TestTypeConverterBenchmarks,
        TestUtilitiesFeatures,
        TestWMSDataTransformer,
        TestWMSSchemaMapper,
        TestWMSTableManager,
        TestWMSTypeConverter,
        c,
        config,
        conftest,
        constants,
        d,
        e,
        examples,
        h,
        integration,
        m,
        models,
        p,
        protocols,
        r,
        s,
        sample_inventory_records,
        sample_order_records,
        sample_task_records,
        singer_record_message,
        singer_schema,
        singer_schema_message,
        singer_state_message,
        t,
        temp_output_dir,
        test_benchmarks,
        test_catalog,
        test_examples,
        test_features,
        test_import_from_correct_module,
        test_no_dual_structure,
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
        tm,
        typings,
        u,
        utilities,
        x,
    )
_LAZY_IMPORTS = merge_lazy_imports(
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

__all__ = [
    "PERF_ITERATIONS",
    "PERF_THRESHOLD_SEC",
    "FlextTargetOracleWmsTestConstants",
    "FlextTargetOracleWmsTestModels",
    "FlextTargetOracleWmsTestProtocols",
    "FlextTargetOracleWmsTestTypes",
    "FlextTargetOracleWmsTestUtilities",
    "TestCatalogAddStream",
    "TestCatalogAndTableIntegration",
    "TestCatalogBenchmarks",
    "TestCatalogGetStream",
    "TestCatalogMultipleStreams",
    "TestClassAttributes",
    "TestCliWorkflow",
    "TestConstantsNamespace",
    "TestConvenienceFunctions",
    "TestDataTransformerBenchmarks",
    "TestErrorWorkflows",
    "TestExamplesCodeQuality",
    "TestExamplesFlextIntegration",
    "TestExamplesImportability",
    "TestExamplesStructure",
    "TestFactoryBenchmarks",
    "TestFlextTargetFactory",
    "TestFlextTargetMonitoringFactory",
    "TestFullSingerWorkflow",
    "TestMain",
    "TestModelsNamespace",
    "TestModuleInit",
    "TestMonitoredTargetCreationRequest",
    "TestMultiStreamIntegration",
    "TestOracleWMSTargetCliExecute",
    "TestOracleWMSTargetCliInit",
    "TestOracleWMSTargetCliLoadConfig",
    "TestProtocolsNamespace",
    "TestSchemaMapperBenchmarks",
    "TestStreamProcessorInitialize",
    "TestStreamProcessorMultipleStreams",
    "TestStreamProcessorRecord",
    "TestTableManagerBenchmarks",
    "TestTargetComponentWiring",
    "TestTargetCreationRequest",
    "TestTargetFeatures",
    "TestTargetHandleRecordMessage",
    "TestTargetHandleSchemaMessage",
    "TestTargetHandleStateMessage",
    "TestTargetInit",
    "TestTargetLifecycle",
    "TestTargetProcessLines",
    "TestTargetSetupCleanup",
    "TestTransformationIntegration",
    "TestTransformerFeatures",
    "TestTypeConverterBenchmarks",
    "TestUtilitiesFeatures",
    "TestWMSDataTransformer",
    "TestWMSSchemaMapper",
    "TestWMSTableManager",
    "TestWMSTypeConverter",
    "c",
    "config",
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
    "sample_inventory_records",
    "sample_order_records",
    "sample_task_records",
    "singer_record_message",
    "singer_schema",
    "singer_schema_message",
    "singer_state_message",
    "t",
    "temp_output_dir",
    "test_benchmarks",
    "test_catalog",
    "test_examples",
    "test_features",
    "test_import_from_correct_module",
    "test_no_dual_structure",
    "test_oracle",
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
