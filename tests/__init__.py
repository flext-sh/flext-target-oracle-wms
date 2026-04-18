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

    from examples.test_examples import (
        TestExamplesCodeQuality,
        TestExamplesFlextIntegration,
        TestExamplesImportability,
        TestExamplesStructure,
    )
    from flext_target_oracle_wms import d, e, h, r, s, x
    from tests.constants import TestsFlextTargetOracleWmsConstants, c
    from tests.integration.test_oracle import (
        TestMultiStreamIntegration,
        TestTargetLifecycle,
    )
    from tests.models import TestsFlextTargetOracleWmsModels, m
    from tests.protocols import TestsFlextTargetOracleWmsProtocols, p
    from tests.typings import TestsFlextTargetOracleWmsTypes, t
    from tests.unit.test_benchmarks import (
        TestCatalogBenchmarks,
        TestDataTransformerBenchmarks,
        TestFactoryBenchmarks,
        TestSchemaMapperBenchmarks,
        TestTableManagerBenchmarks,
        TestTypeConverterBenchmarks,
    )
    from tests.unit.test_catalog import (
        TestCatalogAddStream,
        TestCatalogGetStream,
        TestCatalogMultipleStreams,
    )
    from tests.unit.test_features import (
        TestTargetFeatures,
        TestTransformerFeatures,
        TestUtilitiesFeatures,
    )
    from tests.unit.test_oracle_wms_cli import (
        TestMain,
        TestOracleWMSTargetCliExecute,
        TestOracleWMSTargetCliInit,
        TestOracleWMSTargetCliLoadConfig,
    )
    from tests.unit.test_oracle_wms_factory import (
        TestFactoryConvenienceMethods,
        TestFlextTargetFactory,
        TestFlextTargetMonitoringFactory,
        TestMonitoredTargetCreationRequest,
        TestTargetCreationRequest,
    )
    from tests.unit.test_oracle_wms_init import TestModuleInit
    from tests.unit.test_quality import (
        TestClassAttributes,
        TestConstantsNamespace,
        TestModelsNamespace,
        TestProtocolsNamespace,
    )
    from tests.unit.test_sinks import (
        TestCatalogAndTableIntegration,
        TestTargetComponentWiring,
        TestTransformationIntegration,
    )
    from tests.unit.test_stream import (
        TestStreamProcessorInitialize,
        TestStreamProcessorMultipleStreams,
        TestStreamProcessorRecord,
    )
    from tests.unit.test_target import (
        TestTargetHandleRecordMessage,
        TestTargetHandleSchemaMessage,
        TestTargetHandleStateMessage,
        TestTargetInit,
        TestTargetProcessLines,
        TestTargetSetupCleanup,
    )
    from tests.unit.test_wms_patterns import (
        TestWMSDataTransformer,
        TestWMSSchemaMapper,
        TestWMSTableManager,
        TestWMSTypeConverter,
    )
    from tests.unit.test_workflow import (
        TestCliWorkflow,
        TestErrorWorkflows,
        TestFullSingerWorkflow,
    )
    from tests.utilities import TestsFlextTargetOracleWmsUtilities, u
_LAZY_IMPORTS = merge_lazy_imports(
    (
        "examples",
        ".integration",
        ".unit",
    ),
    build_lazy_import_map(
        {
            ".constants": (
                "TestsFlextTargetOracleWmsConstants",
                "c",
            ),
            ".integration.test_oracle": (
                "TestMultiStreamIntegration",
                "TestTargetLifecycle",
            ),
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
            ".unit.test_benchmarks": (
                "TestCatalogBenchmarks",
                "TestDataTransformerBenchmarks",
                "TestFactoryBenchmarks",
                "TestSchemaMapperBenchmarks",
                "TestTableManagerBenchmarks",
                "TestTypeConverterBenchmarks",
            ),
            ".unit.test_catalog": (
                "TestCatalogAddStream",
                "TestCatalogGetStream",
                "TestCatalogMultipleStreams",
            ),
            ".unit.test_features": (
                "TestTargetFeatures",
                "TestTransformerFeatures",
                "TestUtilitiesFeatures",
            ),
            ".unit.test_oracle_wms_cli": (
                "TestMain",
                "TestOracleWMSTargetCliExecute",
                "TestOracleWMSTargetCliInit",
                "TestOracleWMSTargetCliLoadConfig",
            ),
            ".unit.test_oracle_wms_factory": (
                "TestFactoryConvenienceMethods",
                "TestFlextTargetFactory",
                "TestFlextTargetMonitoringFactory",
                "TestMonitoredTargetCreationRequest",
                "TestTargetCreationRequest",
            ),
            ".unit.test_oracle_wms_init": ("TestModuleInit",),
            ".unit.test_quality": (
                "TestClassAttributes",
                "TestConstantsNamespace",
                "TestModelsNamespace",
                "TestProtocolsNamespace",
            ),
            ".unit.test_sinks": (
                "TestCatalogAndTableIntegration",
                "TestTargetComponentWiring",
                "TestTransformationIntegration",
            ),
            ".unit.test_stream": (
                "TestStreamProcessorInitialize",
                "TestStreamProcessorMultipleStreams",
                "TestStreamProcessorRecord",
            ),
            ".unit.test_target": (
                "TestTargetHandleRecordMessage",
                "TestTargetHandleSchemaMessage",
                "TestTargetHandleStateMessage",
                "TestTargetInit",
                "TestTargetProcessLines",
                "TestTargetSetupCleanup",
            ),
            ".unit.test_wms_patterns": (
                "TestWMSDataTransformer",
                "TestWMSSchemaMapper",
                "TestWMSTableManager",
                "TestWMSTypeConverter",
            ),
            ".unit.test_workflow": (
                "TestCliWorkflow",
                "TestErrorWorkflows",
                "TestFullSingerWorkflow",
            ),
            ".utilities": (
                "TestsFlextTargetOracleWmsUtilities",
                "u",
            ),
            "examples.test_examples": (
                "TestExamplesCodeQuality",
                "TestExamplesFlextIntegration",
                "TestExamplesImportability",
                "TestExamplesStructure",
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
    ),
    module_name=__name__,
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "TestCatalogAddStream",
    "TestCatalogAndTableIntegration",
    "TestCatalogBenchmarks",
    "TestCatalogGetStream",
    "TestCatalogMultipleStreams",
    "TestClassAttributes",
    "TestCliWorkflow",
    "TestConstantsNamespace",
    "TestDataTransformerBenchmarks",
    "TestErrorWorkflows",
    "TestExamplesCodeQuality",
    "TestExamplesFlextIntegration",
    "TestExamplesImportability",
    "TestExamplesStructure",
    "TestFactoryBenchmarks",
    "TestFactoryConvenienceMethods",
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
