"""Protocols for target Oracle WMS integration points."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_core import FlextResult, FlextTypes as t


class FlextTargetOracleWmsProtocols:
    """Namespace for target Oracle WMS protocol contracts."""

    class TargetOracleWms:
        """Target Oracle WMS protocol namespace."""

        @runtime_checkable
        class WmsDataLoadingProtocol(Protocol):
            """Protocol for loading records into a WMS sink."""

            def load_data(
                self,
                records: list[dict[str, t.GeneralValueType]],
            ) -> FlextResult[bool]:
                """Load a batch of records."""
                ...

        @runtime_checkable
        class DataTransformationProtocol(Protocol):
            """Protocol for transforming source record payloads."""

            def transform_to_wms(
                self,
                record: dict[str, t.GeneralValueType],
            ) -> FlextResult[dict[str, t.GeneralValueType]]:
                """Transform one record to WMS shape."""
                ...


p = FlextTargetOracleWmsProtocols

__all__ = ["FlextTargetOracleWmsProtocols", "p"]
