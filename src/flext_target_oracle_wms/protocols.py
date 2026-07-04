"""Protocols for target Oracle WMS integration points."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano.protocols import FlextMeltanoProtocols as meltano_p
from flext_oracle_wms.protocols import p

if TYPE_CHECKING:
    from flext_target_oracle_wms.typings import t


class FlextTargetOracleWmsProtocols(meltano_p, p):
    """Namespace for target Oracle WMS protocol contracts."""

    class TargetOracleWms:
        """Target Oracle WMS protocol namespace."""

        @runtime_checkable
        class WmsDataLoading(Protocol):
            """Protocol for loading records into a WMS sink."""

            def load_data(
                self,
                records: t.SequenceOf[t.JsonMapping],
            ) -> meltano_p.Result[bool]:
                """Load a batch of records."""
                ...

        @runtime_checkable
        class DataTransformation(Protocol):
            """Protocol for transforming source record payloads."""

            def transform_to_wms(
                self,
                record: t.JsonMapping,
            ) -> meltano_p.Result[t.JsonMapping]:
                """Transform one record to WMS shape."""
                ...


p = FlextTargetOracleWmsProtocols
__all__: list[str] = ["FlextTargetOracleWmsProtocols", "p"]
