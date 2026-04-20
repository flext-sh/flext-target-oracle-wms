"""Protocols for target Oracle WMS integration points."""

from __future__ import annotations

from collections.abc import (
    Sequence,
)
from typing import Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols
from flext_oracle_wms import FlextOracleWmsProtocols
from flext_target_oracle_wms import t


class FlextTargetOracleWmsProtocols(FlextMeltanoProtocols, FlextOracleWmsProtocols):
    """Namespace for target Oracle WMS protocol contracts."""

    class TargetOracleWms:
        """Target Oracle WMS protocol namespace."""

        @runtime_checkable
        class WmsDataLoading(Protocol):
            """Protocol for loading records into a WMS sink."""

            def load_data(
                self,
                records: Sequence[t.ContainerValueMapping],
            ) -> p.Result[bool]:
                """Load a batch of records."""
                ...

        @runtime_checkable
        class DataTransformation(Protocol):
            """Protocol for transforming source record payloads."""

            def transform_to_wms(
                self,
                record: t.ContainerValueMapping,
            ) -> p.Result[t.ContainerValueMapping]:
                """Transform one record to WMS shape."""
                ...


p = FlextTargetOracleWmsProtocols
__all__: list[str] = ["FlextTargetOracleWmsProtocols", "p"]
