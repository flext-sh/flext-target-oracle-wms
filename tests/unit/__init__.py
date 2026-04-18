# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_benchmarks": (
            "TestCatalogBenchmarks",
            "TestDataTransformerBenchmarks",
            "TestFactoryBenchmarks",
            "TestSchemaMapperBenchmarks",
            "TestTableManagerBenchmarks",
            "TestTypeConverterBenchmarks",
        ),
        ".test_catalog": (
            "TestCatalogAddStream",
            "TestCatalogGetStream",
            "TestCatalogMultipleStreams",
        ),
        ".test_features": (
            "TestTargetFeatures",
            "TestTransformerFeatures",
            "TestUtilitiesFeatures",
        ),
        ".test_module_governance": ("test_module_governance",),
        ".test_oracle_wms_cli": (
            "TestMain",
            "TestOracleWMSTargetCliExecute",
            "TestOracleWMSTargetCliInit",
            "TestOracleWMSTargetCliLoadConfig",
        ),
        ".test_oracle_wms_factory": (
            "TestFactoryConvenienceMethods",
            "TestFlextTargetFactory",
            "TestFlextTargetMonitoringFactory",
            "TestMonitoredTargetCreationRequest",
            "TestTargetCreationRequest",
        ),
        ".test_oracle_wms_init": ("TestModuleInit",),
        ".test_quality": (
            "TestClassAttributes",
            "TestConstantsNamespace",
            "TestModelsNamespace",
            "TestProtocolsNamespace",
        ),
        ".test_sinks": (
            "TestCatalogAndTableIntegration",
            "TestTargetComponentWiring",
            "TestTransformationIntegration",
        ),
        ".test_stream": (
            "TestStreamProcessorInitialize",
            "TestStreamProcessorMultipleStreams",
            "TestStreamProcessorRecord",
        ),
        ".test_structure": ("test_structure",),
        ".test_target": (
            "TestTargetHandleRecordMessage",
            "TestTargetHandleSchemaMessage",
            "TestTargetHandleStateMessage",
            "TestTargetInit",
            "TestTargetProcessLines",
            "TestTargetSetupCleanup",
        ),
        ".test_wms_patterns": (
            "TestWMSDataTransformer",
            "TestWMSSchemaMapper",
            "TestWMSTableManager",
            "TestWMSTypeConverter",
        ),
        ".test_workflow": (
            "TestCliWorkflow",
            "TestErrorWorkflows",
            "TestFullSingerWorkflow",
        ),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
