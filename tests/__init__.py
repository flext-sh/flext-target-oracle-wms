# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

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
        TestsFlextTargetOracleWmsConstants,
        TestsFlextTargetOracleWmsConstants as c,
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
    from tests.models import TestsFlextTargetOracleWmsModels, m, tm
    from tests.protocols import TestsFlextTargetOracleWmsProtocols, p
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
        TestsFlextTargetOracleWmsTypes,
        TestsFlextTargetOracleWmsTypes as t,
    )
    from tests.utilities import (
        TestsFlextTargetOracleWmsUtilities,
        TestsFlextTargetOracleWmsUtilities as u,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "PERF_ITERATIONS": ("tests.test_benchmarks", "PERF_ITERATIONS"),
    "PERF_THRESHOLD_SEC": ("tests.test_benchmarks", "PERF_THRESHOLD_SEC"),
    "TestCatalogAddStream": ("tests.test_catalog", "TestCatalogAddStream"),
    "TestCatalogAndTableIntegration": (
        "tests.test_sinks",
        "TestCatalogAndTableIntegration",
    ),
    "TestCatalogBenchmarks": ("tests.test_benchmarks", "TestCatalogBenchmarks"),
    "TestCatalogGetStream": ("tests.test_catalog", "TestCatalogGetStream"),
    "TestCatalogMultipleStreams": ("tests.test_catalog", "TestCatalogMultipleStreams"),
    "TestClassAttributes": ("tests.test_quality", "TestClassAttributes"),
    "TestCliWorkflow": ("tests.test_workflow", "TestCliWorkflow"),
    "TestConstantsNamespace": ("tests.test_quality", "TestConstantsNamespace"),
    "TestConvenienceFunctions": (
        "tests.test_oracle_wms_factory",
        "TestConvenienceFunctions",
    ),
    "TestDataTransformerBenchmarks": (
        "tests.test_benchmarks",
        "TestDataTransformerBenchmarks",
    ),
    "TestErrorWorkflows": ("tests.test_workflow", "TestErrorWorkflows"),
    "TestExamplesCodeQuality": (
        "tests.examples.test_examples",
        "TestExamplesCodeQuality",
    ),
    "TestExamplesFlextIntegration": (
        "tests.examples.test_examples",
        "TestExamplesFlextIntegration",
    ),
    "TestExamplesImportability": (
        "tests.examples.test_examples",
        "TestExamplesImportability",
    ),
    "TestExamplesStructure": ("tests.examples.test_examples", "TestExamplesStructure"),
    "TestFactoryBenchmarks": ("tests.test_benchmarks", "TestFactoryBenchmarks"),
    "TestFlextTargetFactory": (
        "tests.test_oracle_wms_factory",
        "TestFlextTargetFactory",
    ),
    "TestFlextTargetMonitoringFactory": (
        "tests.test_oracle_wms_factory",
        "TestFlextTargetMonitoringFactory",
    ),
    "TestFullSingerWorkflow": ("tests.test_workflow", "TestFullSingerWorkflow"),
    "TestMain": ("tests.test_oracle_wms_cli", "TestMain"),
    "TestModelsNamespace": ("tests.test_quality", "TestModelsNamespace"),
    "TestModuleInit": ("tests.test_oracle_wms_init", "TestModuleInit"),
    "TestMonitoredTargetCreationRequest": (
        "tests.test_oracle_wms_factory",
        "TestMonitoredTargetCreationRequest",
    ),
    "TestMultiStreamIntegration": (
        "tests.integration.test_oracle",
        "TestMultiStreamIntegration",
    ),
    "TestOracleWMSTargetCliExecute": (
        "tests.test_oracle_wms_cli",
        "TestOracleWMSTargetCliExecute",
    ),
    "TestOracleWMSTargetCliInit": (
        "tests.test_oracle_wms_cli",
        "TestOracleWMSTargetCliInit",
    ),
    "TestOracleWMSTargetCliLoadConfig": (
        "tests.test_oracle_wms_cli",
        "TestOracleWMSTargetCliLoadConfig",
    ),
    "TestProtocolsNamespace": ("tests.test_quality", "TestProtocolsNamespace"),
    "TestSchemaMapperBenchmarks": (
        "tests.test_benchmarks",
        "TestSchemaMapperBenchmarks",
    ),
    "TestStreamProcessorInitialize": (
        "tests.test_stream",
        "TestStreamProcessorInitialize",
    ),
    "TestStreamProcessorMultipleStreams": (
        "tests.test_stream",
        "TestStreamProcessorMultipleStreams",
    ),
    "TestStreamProcessorRecord": ("tests.test_stream", "TestStreamProcessorRecord"),
    "TestTableManagerBenchmarks": (
        "tests.test_benchmarks",
        "TestTableManagerBenchmarks",
    ),
    "TestTargetComponentWiring": ("tests.test_sinks", "TestTargetComponentWiring"),
    "TestTargetCreationRequest": (
        "tests.test_oracle_wms_factory",
        "TestTargetCreationRequest",
    ),
    "TestTargetFeatures": ("tests.test_features", "TestTargetFeatures"),
    "TestTargetHandleRecordMessage": (
        "tests.test_target",
        "TestTargetHandleRecordMessage",
    ),
    "TestTargetHandleSchemaMessage": (
        "tests.test_target",
        "TestTargetHandleSchemaMessage",
    ),
    "TestTargetHandleStateMessage": (
        "tests.test_target",
        "TestTargetHandleStateMessage",
    ),
    "TestTargetInit": ("tests.test_target", "TestTargetInit"),
    "TestTargetLifecycle": ("tests.integration.test_oracle", "TestTargetLifecycle"),
    "TestTargetProcessLines": ("tests.test_target", "TestTargetProcessLines"),
    "TestTargetSetupCleanup": ("tests.test_target", "TestTargetSetupCleanup"),
    "TestTransformationIntegration": (
        "tests.test_sinks",
        "TestTransformationIntegration",
    ),
    "TestTransformerFeatures": ("tests.test_features", "TestTransformerFeatures"),
    "TestTypeConverterBenchmarks": (
        "tests.test_benchmarks",
        "TestTypeConverterBenchmarks",
    ),
    "TestUtilitiesFeatures": ("tests.test_features", "TestUtilitiesFeatures"),
    "TestWMSDataTransformer": ("tests.test_wms_patterns", "TestWMSDataTransformer"),
    "TestWMSSchemaMapper": ("tests.test_wms_patterns", "TestWMSSchemaMapper"),
    "TestWMSTableManager": ("tests.test_wms_patterns", "TestWMSTableManager"),
    "TestWMSTypeConverter": ("tests.test_wms_patterns", "TestWMSTypeConverter"),
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
    "config": ("tests.conftest", "config"),
    "m": ("tests.models", "m"),
    "p": ("tests.protocols", "p"),
    "sample_inventory_records": ("tests.conftest", "sample_inventory_records"),
    "sample_order_records": ("tests.conftest", "sample_order_records"),
    "sample_task_records": ("tests.conftest", "sample_task_records"),
    "singer_record_message": ("tests.conftest", "singer_record_message"),
    "singer_schema": ("tests.conftest", "singer_schema"),
    "singer_schema_message": ("tests.conftest", "singer_schema_message"),
    "singer_state_message": ("tests.conftest", "singer_state_message"),
    "t": ("tests.typings", "TestsFlextTargetOracleWmsTypes"),
    "temp_output_dir": ("tests.conftest", "temp_output_dir"),
    "test_import_from_correct_module": (
        "tests.test_structure",
        "test_import_from_correct_module",
    ),
    "test_no_dual_structure": ("tests.test_structure", "test_no_dual_structure"),
    "tm": ("tests.models", "tm"),
    "u": ("tests.utilities", "TestsFlextTargetOracleWmsUtilities"),
}

__all__ = [
    "PERF_ITERATIONS",
    "PERF_THRESHOLD_SEC",
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
    "TestsFlextTargetOracleWmsConstants",
    "TestsFlextTargetOracleWmsModels",
    "TestsFlextTargetOracleWmsProtocols",
    "TestsFlextTargetOracleWmsTypes",
    "TestsFlextTargetOracleWmsUtilities",
    "c",
    "config",
    "m",
    "p",
    "sample_inventory_records",
    "sample_order_records",
    "sample_task_records",
    "singer_record_message",
    "singer_schema",
    "singer_schema_message",
    "singer_state_message",
    "t",
    "temp_output_dir",
    "test_import_from_correct_module",
    "test_no_dual_structure",
    "tm",
    "u",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
