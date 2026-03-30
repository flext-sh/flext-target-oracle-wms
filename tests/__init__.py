# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import *

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
    from tests.conftest import *
    from tests.constants import *
    from tests.examples import test_examples
    from tests.examples.test_examples import *
    from tests.integration import test_oracle
    from tests.integration.test_oracle import *
    from tests.models import *
    from tests.protocols import *
    from tests.test_benchmarks import *
    from tests.test_catalog import *
    from tests.test_features import *
    from tests.test_oracle_wms_cli import *
    from tests.test_oracle_wms_factory import *
    from tests.test_oracle_wms_init import *
    from tests.test_quality import *
    from tests.test_sinks import *
    from tests.test_stream import *
    from tests.test_structure import *
    from tests.test_target import *
    from tests.test_wms_patterns import *
    from tests.test_workflow import *
    from tests.typings import *
    from tests.utilities import *

from tests.examples import _LAZY_IMPORTS as _EXAMPLES_LAZY
from tests.integration import _LAZY_IMPORTS as _INTEGRATION_LAZY

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    **_EXAMPLES_LAZY,
    **_INTEGRATION_LAZY,
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
    "c": ["tests.constants", "FlextTargetOracleWmsTestConstants"],
    "config": "tests.conftest",
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "d": "flext_tests",
    "e": "flext_tests",
    "examples": "tests.examples",
    "h": "flext_tests",
    "integration": "tests.integration",
    "m": ["tests.models", "FlextTargetOracleWmsTestModels"],
    "models": "tests.models",
    "p": ["tests.protocols", "FlextTargetOracleWmsTestProtocols"],
    "protocols": "tests.protocols",
    "r": "flext_tests",
    "s": "flext_tests",
    "sample_inventory_records": "tests.conftest",
    "sample_order_records": "tests.conftest",
    "sample_task_records": "tests.conftest",
    "singer_record_message": "tests.conftest",
    "singer_schema": "tests.conftest",
    "singer_schema_message": "tests.conftest",
    "singer_state_message": "tests.conftest",
    "t": ["tests.typings", "FlextTargetOracleWmsTestTypes"],
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
    "u": ["tests.utilities", "FlextTargetOracleWmsTestUtilities"],
    "utilities": "tests.utilities",
    "x": "flext_tests",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, sorted(_LAZY_IMPORTS))
