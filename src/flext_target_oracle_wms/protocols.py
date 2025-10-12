"""Singer Oracle WMS target protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_core import FlextCore


class FlextTargetOracleWmsProtocols:
    """Singer Target Oracle WMS protocols with explicit re-exports from FlextCore.Protocols foundation.

    Domain Extension Pattern (Phase 3):
    - Explicit re-export of foundation protocols (not inheritance)
    - Domain-specific protocols organized in TargetOracleWms namespace
    - 100% backward compatibility through aliases
    """

    # ============================================================================
    # RE-EXPORT FOUNDATION PROTOCOLS (EXPLICIT PATTERN)
    # ============================================================================

    Foundation = FlextCore.Protocols.Foundation
    Domain = FlextCore.Protocols.Domain
    Application = FlextCore.Protocols.Application
    Infrastructure = FlextCore.Protocols.Infrastructure
    Extensions = FlextCore.Protocols.Extensions
    Commands = FlextCore.Protocols.Commands

    # ============================================================================
    # SINGER TARGET ORACLE WMS-SPECIFIC PROTOCOLS (DOMAIN NAMESPACE)
    # ============================================================================

    class TargetOracleWms:
        """Singer Target Oracle WMS domain protocols for Oracle WMS loading."""

        @runtime_checkable
        class WmsDataLoadingProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for WMS data loading."""

            def load_data(
                self, records: list[FlextCore.Types.Dict]
            ) -> FlextCore.Result[None]: ...

        @runtime_checkable
        class WarehouseOperationsProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for WMS warehouse operations."""

            def execute_operation(
                self, operation: FlextCore.Types.Dict
            ) -> FlextCore.Result[None]: ...

        @runtime_checkable
        class DataTransformationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for Singer to WMS transformation."""

            def transform_to_wms(
                self, record: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]: ...

        @runtime_checkable
        class WmsApiProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for WMS API operations."""

            def invoke_api(
                self, endpoint: str, payload: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]: ...

        @runtime_checkable
        class BatchProcessingProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for WMS batch processing."""

            def process_batch(
                self, records: list[FlextCore.Types.Dict]
            ) -> FlextCore.Result[None]: ...

        @runtime_checkable
        class ValidationProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for WMS data validation."""

            def validate_wms_data(
                self, data: FlextCore.Types.Dict
            ) -> FlextCore.Result[bool]: ...

        @runtime_checkable
        class PerformanceProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for WMS performance optimization."""

            def optimize_loading(
                self, config: FlextCore.Types.Dict
            ) -> FlextCore.Result[FlextCore.Types.Dict]: ...

        @runtime_checkable
        class MonitoringProtocol(FlextCore.Protocols.Domain.Service, Protocol):
            """Protocol for WMS loading monitoring."""

            def track_load_progress(
                self, entity: str, records: int
            ) -> FlextCore.Result[None]: ...

    # ============================================================================
    # BACKWARD COMPATIBILITY ALIASES (100% COMPATIBILITY)
    # ============================================================================

    WmsDataLoadingProtocol = TargetOracleWms.WmsDataLoadingProtocol
    WarehouseOperationsProtocol = TargetOracleWms.WarehouseOperationsProtocol
    DataTransformationProtocol = TargetOracleWms.DataTransformationProtocol
    WmsApiProtocol = TargetOracleWms.WmsApiProtocol
    BatchProcessingProtocol = TargetOracleWms.BatchProcessingProtocol
    ValidationProtocol = TargetOracleWms.ValidationProtocol
    PerformanceProtocol = TargetOracleWms.PerformanceProtocol
    MonitoringProtocol = TargetOracleWms.MonitoringProtocol

    TargetOracleWmsDataLoadingProtocol = TargetOracleWms.WmsDataLoadingProtocol
    TargetOracleWmsWarehouseOperationsProtocol = (
        TargetOracleWms.WarehouseOperationsProtocol
    )
    TargetOracleWmsDataTransformationProtocol = (
        TargetOracleWms.DataTransformationProtocol
    )
    TargetOracleWmsApiProtocol = TargetOracleWms.WmsApiProtocol
    TargetOracleWmsBatchProcessingProtocol = TargetOracleWms.BatchProcessingProtocol
    TargetOracleWmsValidationProtocol = TargetOracleWms.ValidationProtocol
    TargetOracleWmsPerformanceProtocol = TargetOracleWms.PerformanceProtocol
    TargetOracleWmsMonitoringProtocol = TargetOracleWms.MonitoringProtocol


__all__ = [
    "FlextTargetOracleWmsProtocols",
]
