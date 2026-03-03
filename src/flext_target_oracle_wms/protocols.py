"""Protocols for target Oracle WMS integration points."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Protocol, runtime_checkable

from flext_core import FlextResult, t
from flext_meltano import FlextMeltanoProtocols
from flext_oracle_wms.protocols import FlextOracleWmsProtocols


class FlextTargetOracleWmsProtocols(FlextMeltanoProtocols, FlextOracleWmsProtocols):
    """Namespace for target Oracle WMS protocol contracts."""

    class TargetOracleWms:
        """Target Oracle WMS protocol namespace."""

        @runtime_checkable
        class WmsDataLoadingProtocol(Protocol):
            """Protocol for loading records into a WMS sink."""

            def load_data(
                self,
                records: list[Mapping[str, t.ContainerValue]],
            ) -> FlextResult[bool]:
                """Load a batch of records."""
                ...

        @runtime_checkable
        class DataTransformationProtocol(Protocol):
            """Protocol for transforming source record payloads."""

            def transform_to_wms(
                self,
                record: Mapping[str, t.ContainerValue],
            ) -> FlextResult[Mapping[str, t.ContainerValue]]:
                """Transform one record to WMS shape."""
                ...


p = FlextTargetOracleWmsProtocols

__all__ = ["FlextTargetOracleWmsProtocols", "p"]
