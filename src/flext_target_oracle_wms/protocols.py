"""Singer Oracle WMS target protocols for FLEXT ecosystem."""

from typing import Protocol, runtime_checkable

from flext_db_oracle.protocols import p_db_oracle
from flext_meltano.protocols import p_meltano


class FlextTargetOracleWmsProtocols(p_meltano, p_db_oracle):
    """Singer Target Oracle WMS protocols extending Oracle and Meltano protocols.

    Extends both FlextDbOracleProtocols and FlextMeltanoProtocols via multiple inheritance
    to inherit all Oracle protocols, Meltano protocols, and foundation protocols.

    Architecture:
    - EXTENDS: FlextDbOracleProtocols (inherits .Database.* protocols)
    - EXTENDS: FlextMeltanoProtocols (inherits .Meltano.* protocols)
    - ADDS: Target Oracle WMS-specific protocols in Target.OracleWms namespace
    - PROVIDES: Root-level alias `p` for convenient access

    Usage:
    from flext_target_oracle_wms.protocols import p

    # Foundation protocols (inherited)
    result: p.Result[str]
    service: p.Service[str]

    # Oracle protocols (inherited)
    connection: p.Database.ConnectionProtocol

    # Meltano protocols (inherited)
    target: p.Meltano.TargetProtocol

    # Target Oracle WMS-specific protocols
    wms_data_loading: p.Target.OracleWms.WmsDataLoadingProtocol
    """

    class Target:
        """Singer Target domain protocols."""

        class OracleWms:
            """Singer Target Oracle WMS domain protocols for Oracle WMS loading.

            Provides protocol definitions for Oracle WMS operations, including data loading,
            warehouse operations, data transformation, API operations, batch processing,
            data validation, performance optimization, and loading monitoring.
            """

            @runtime_checkable
            class WmsDataLoadingProtocol(p_db_oracle.Service[object], Protocol):
                """Protocol for WMS data loading.

                Defines the interface for loading data into Oracle WMS.
                """

                def load_data(
                    self,
                    records: list[dict[str, object]],
                ) -> p_meltano.Result[bool]:
                    """Load records into WMS.

                    Args:
                        records: List of records to load.

                    Returns:
                        Result indicating success or failure of the loading operation.

                    """

            @runtime_checkable
            class WarehouseOperationsProtocol(p_db_oracle.Service[object], Protocol):
                """Protocol for WMS warehouse operations.

                Defines the interface for executing warehouse operations in Oracle WMS.
                """

                def execute_operation(
                    self,
                    operation: dict[str, object],
                ) -> p_meltano.Result[bool]:
                    """Execute warehouse operation.

                    Args:
                        operation: Operation definition to execute.

                    Returns:
                        Result indicating success or failure of the operation.

                    """

            @runtime_checkable
            class DataTransformationProtocol(p_db_oracle.Service[object], Protocol):
                """Protocol for Singer to WMS transformation.

                Defines the interface for transforming Singer records to WMS format.
                """

                def transform_to_wms(
                    self,
                    record: dict[str, object],
                ) -> p_meltano.Result[dict[str, object]]:
                    """Transform record to WMS format.

                    Args:
                        record: Singer record to transform.

                    Returns:
                        Result containing the transformed record in WMS format.

                    """

            @runtime_checkable
            class WmsApiProtocol(p_db_oracle.Service[object], Protocol):
                """Protocol for WMS API operations.

                Defines the interface for invoking Oracle WMS API endpoints.
                """

                def invoke_api(
                    self,
                    endpoint: str,
                    payload: dict[str, object],
                ) -> p_meltano.Result[dict[str, object]]:
                    """Invoke WMS API endpoint.

                    Args:
                        endpoint: API endpoint to invoke.
                        payload: Request payload.

                    Returns:
                        Result containing the API response.

                    """

            @runtime_checkable
            class BatchProcessingProtocol(p_db_oracle.Service[object], Protocol):
                """Protocol for WMS batch processing.

                Defines the interface for processing batches of WMS records.
                """

                def process_batch(
                    self,
                    records: list[dict[str, object]],
                ) -> p_meltano.Result[bool]:
                    """Process batch of WMS records.

                    Args:
                        records: List of records to process.

                    Returns:
                        Result indicating success or failure of the batch processing.

                    """

            @runtime_checkable
            class ValidationProtocol(p_db_oracle.Service[object], Protocol):
                """Protocol for WMS data validation.

                Defines the interface for validating WMS data.
                """

                def validate_wms_data(
                    self,
                    data: dict[str, object],
                ) -> p_meltano.Result[bool]:
                    """Validate WMS data.

                    Args:
                        data: Data to validate.

                    Returns:
                        Result indicating whether the data is valid.

                    """

            @runtime_checkable
            class PerformanceProtocol(p_db_oracle.Service[object], Protocol):
                """Protocol for WMS performance optimization.

                Defines the interface for optimizing WMS loading performance.
                """

                def optimize_loading(
                    self,
                    config: dict[str, object],
                ) -> p_meltano.Result[dict[str, object]]:
                    """Optimize WMS loading configuration.

                    Args:
                        config: Configuration to optimize.

                    Returns:
                        Result containing optimized configuration.

                    """

            @runtime_checkable
            class MonitoringProtocol(p_db_oracle.Service[object], Protocol):
                """Protocol for WMS loading monitoring.

                Defines the interface for monitoring WMS loading progress.
                """

                def track_load_progress(
                    self,
                    entity: str,
                    records: int,
                ) -> p_meltano.Result[bool]:
                    """Track WMS loading progress.

                    Args:
                        entity: Entity being loaded.
                        records: Number of records processed.

                    Returns:
                        Result indicating success or failure of tracking.

                    """


# Runtime alias for simplified usage
p = FlextTargetOracleWmsProtocols

__all__ = [
    "FlextTargetOracleWmsProtocols",
    "p",
]
