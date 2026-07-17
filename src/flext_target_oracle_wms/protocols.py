"""Protocols for target Oracle WMS integration points."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols
from flext_oracle_wms import p

if TYPE_CHECKING:
    from flext_target_oracle_wms import t


class FlextTargetOracleWmsProtocols(FlextMeltanoProtocols, p):
    """Namespace for target Oracle WMS protocol contracts."""

    class TargetOracleWms:
        """Target Oracle WMS protocol namespace."""

        @runtime_checkable
        class WmsDataLoading(Protocol):
            """Protocol for loading records into a WMS sink."""

            def load_data(
                self,
                records: t.SequenceOf[t.JsonMapping],
            ) -> FlextMeltanoProtocols.Result[bool]:
                """Load a batch of records."""
                ...

        @runtime_checkable
        class DataTransformation(Protocol):
            """Protocol for transforming source record payloads."""

            def transform_to_wms(
                self,
                record: t.JsonMapping,
            ) -> FlextMeltanoProtocols.Result[t.JsonMapping]:
                """Transform one record to WMS shape."""
                ...


p = FlextTargetOracleWmsProtocols
__all__: list[str] = ["FlextTargetOracleWmsProtocols", "p"]
