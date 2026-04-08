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
    from tests.conftest import (
        config,
        pytest_plugins,
        sample_inventory_records,
        sample_order_records,
        sample_task_records,
        singer_record_message,
        singer_schema,
        singer_schema_message,
        singer_state_message,
        temp_output_dir,
    )

    constants = _tests_constants
    import tests.examples as _tests_examples
    from tests.constants import (
        FlextTargetOracleWmsTestConstants,
        FlextTargetOracleWmsTestConstants as c,
    )

    examples = _tests_examples
    import tests.integration as _tests_integration
    from tests.examples import (
        TestExamplesCodeQuality,
        TestExamplesFlextIntegration,
        TestExamplesImportability,
        TestExamplesStructure,
        test_examples,
    )

    integration = _tests_integration
    import tests.models as _tests_models
    from tests.integration import (
        TestMultiStreamIntegration,
        TestTargetLifecycle,
        test_oracle,
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

    test_catalog = _tests_test_catalog
    import tests.test_features as _tests_test_features
    from tests.test_catalog import (
        TestCatalogAddStream,
        TestCatalogGetStream,
        TestCatalogMultipleStreams,
    )

    test_features = _tests_test_features
    import tests.test_module_governance as _tests_test_module_governance
    from tests.test_features import (
        TestTargetFeatures,
        TestTransformerFeatures,
        TestUtilitiesFeatures,
    )

    test_module_governance = _tests_test_module_governance
    import tests.test_oracle_wms_cli as _tests_test_oracle_wms_cli
    from tests.test_module_governance import (
        ALLOWED_MODULE_FUNCTIONS,
        PACKAGE_ROOT,
        test_package_modules_do_not_define_module_level_loggers,
        test_package_modules_do_not_define_unapproved_top_level_functions,
    )

    test_oracle_wms_cli = _tests_test_oracle_wms_cli
    import tests.test_oracle_wms_factory as _tests_test_oracle_wms_factory
    from tests.test_oracle_wms_cli import (
        TestMain,
        TestOracleWMSTargetCliExecute,
        TestOracleWMSTargetCliInit,
        TestOracleWMSTargetCliLoadConfig,
    )

    test_oracle_wms_factory = _tests_test_oracle_wms_factory
    import tests.test_oracle_wms_init as _tests_test_oracle_wms_init
    from tests.test_oracle_wms_factory import (
        TestFactoryConvenienceMethods,
        TestFlextTargetFactory,
        TestFlextTargetMonitoringFactory,
        TestMonitoredTargetCreationRequest,
        TestTargetCreationRequest,
    )

    test_oracle_wms_init = _tests_test_oracle_wms_init
    import tests.test_quality as _tests_test_quality
    from tests.test_oracle_wms_init import TestModuleInit

    test_quality = _tests_test_quality
    import tests.test_sinks as _tests_test_sinks
    from tests.test_quality import (
        TestClassAttributes,
        TestConstantsNamespace,
        TestModelsNamespace,
        TestProtocolsNamespace,
    )

    test_sinks = _tests_test_sinks
    import tests.test_stream as _tests_test_stream
    from tests.test_sinks import (
        TestCatalogAndTableIntegration,
        TestTargetComponentWiring,
        TestTransformationIntegration,
    )

    test_stream = _tests_test_stream
    import tests.test_structure as _tests_test_structure
    from tests.test_stream import (
        TestStreamProcessorInitialize,
        TestStreamProcessorMultipleStreams,
        TestStreamProcessorRecord,
    )

    test_structure = _tests_test_structure
    import tests.test_target as _tests_test_target
    from tests.test_structure import (
        test_import_from_correct_module,
        test_no_dual_structure,
    )

    test_target = _tests_test_target
    import tests.test_wms_patterns as _tests_test_wms_patterns
    from tests.test_target import (
        TestTargetHandleRecordMessage,
        TestTargetHandleSchemaMessage,
        TestTargetHandleStateMessage,
        TestTargetInit,
        TestTargetProcessLines,
        TestTargetSetupCleanup,
    )

    test_wms_patterns = _tests_test_wms_patterns
    import tests.test_workflow as _tests_test_workflow
    from tests.test_wms_patterns import (
        TestWMSDataTransformer,
        TestWMSSchemaMapper,
        TestWMSTableManager,
        TestWMSTypeConverter,
    )

    test_workflow = _tests_test_workflow
    import tests.typings as _tests_typings
    from tests.test_workflow import (
        TestCliWorkflow,
        TestErrorWorkflows,
        TestFullSingerWorkflow,
    )

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
_LAZY_IMPORTS = merge_lazy_imports(
    (
        "tests.examples",
        "tests.integration",
    ),
    {
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
        "FlextTargetOracleWmsTestTypes": (
            "tests.typings",
            "FlextTargetOracleWmsTestTypes",
        ),
        "FlextTargetOracleWmsTestUtilities": (
            "tests.utilities",
            "FlextTargetOracleWmsTestUtilities",
        ),
        "PACKAGE_ROOT": ("tests.test_module_governance", "PACKAGE_ROOT"),
        "PERF_ITERATIONS": ("tests.test_benchmarks", "PERF_ITERATIONS"),
        "PERF_THRESHOLD_SEC": ("tests.test_benchmarks", "PERF_THRESHOLD_SEC"),
        "TestCatalogAddStream": ("tests.test_catalog", "TestCatalogAddStream"),
        "TestCatalogAndTableIntegration": (
            "tests.test_sinks",
            "TestCatalogAndTableIntegration",
        ),
        "TestCatalogBenchmarks": ("tests.test_benchmarks", "TestCatalogBenchmarks"),
        "TestCatalogGetStream": ("tests.test_catalog", "TestCatalogGetStream"),
        "TestCatalogMultipleStreams": (
            "tests.test_catalog",
            "TestCatalogMultipleStreams",
        ),
        "TestClassAttributes": ("tests.test_quality", "TestClassAttributes"),
        "TestCliWorkflow": ("tests.test_workflow", "TestCliWorkflow"),
        "TestConstantsNamespace": ("tests.test_quality", "TestConstantsNamespace"),
        "TestDataTransformerBenchmarks": (
            "tests.test_benchmarks",
            "TestDataTransformerBenchmarks",
        ),
        "TestErrorWorkflows": ("tests.test_workflow", "TestErrorWorkflows"),
        "TestFactoryBenchmarks": ("tests.test_benchmarks", "TestFactoryBenchmarks"),
        "TestFactoryConvenienceMethods": (
            "tests.test_oracle_wms_factory",
            "TestFactoryConvenienceMethods",
        ),
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
        "c": ("tests.constants", "FlextTargetOracleWmsTestConstants"),
        "config": ("tests.conftest", "config"),
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
        "pytest_plugins": ("tests.conftest", "pytest_plugins"),
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "sample_inventory_records": ("tests.conftest", "sample_inventory_records"),
        "sample_order_records": ("tests.conftest", "sample_order_records"),
        "sample_task_records": ("tests.conftest", "sample_task_records"),
        "singer_record_message": ("tests.conftest", "singer_record_message"),
        "singer_schema": ("tests.conftest", "singer_schema"),
        "singer_schema_message": ("tests.conftest", "singer_schema_message"),
        "singer_state_message": ("tests.conftest", "singer_state_message"),
        "t": ("tests.typings", "FlextTargetOracleWmsTestTypes"),
        "temp_output_dir": ("tests.conftest", "temp_output_dir"),
        "test_benchmarks": "tests.test_benchmarks",
        "test_catalog": "tests.test_catalog",
        "test_features": "tests.test_features",
        "test_import_from_correct_module": (
            "tests.test_structure",
            "test_import_from_correct_module",
        ),
        "test_module_governance": "tests.test_module_governance",
        "test_no_dual_structure": ("tests.test_structure", "test_no_dual_structure"),
        "test_oracle_wms_cli": "tests.test_oracle_wms_cli",
        "test_oracle_wms_factory": "tests.test_oracle_wms_factory",
        "test_oracle_wms_init": "tests.test_oracle_wms_init",
        "test_package_modules_do_not_define_module_level_loggers": (
            "tests.test_module_governance",
            "test_package_modules_do_not_define_module_level_loggers",
        ),
        "test_package_modules_do_not_define_unapproved_top_level_functions": (
            "tests.test_module_governance",
            "test_package_modules_do_not_define_unapproved_top_level_functions",
        ),
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
    },
)
_ = _LAZY_IMPORTS.pop("cleanup_submodule_namespace", None)
_ = _LAZY_IMPORTS.pop("install_lazy_exports", None)
_ = _LAZY_IMPORTS.pop("lazy_getattr", None)
_ = _LAZY_IMPORTS.pop("merge_lazy_imports", None)
_ = _LAZY_IMPORTS.pop("output", None)
_ = _LAZY_IMPORTS.pop("output_reporting", None)

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
    "pytest_plugins",
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
    "test_module_governance",
    "test_no_dual_structure",
    "test_oracle",
    "test_oracle_wms_cli",
    "test_oracle_wms_factory",
    "test_oracle_wms_init",
    "test_package_modules_do_not_define_module_level_loggers",
    "test_package_modules_do_not_define_unapproved_top_level_functions",
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
