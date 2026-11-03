# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_target_oracle_wms/_protocols/target
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols

from flext_target_oracle_wms import t

if TYPE_CHECKING:
    from flext_target_oracle_wms._constants import FlextTargetOracleWmsConstantsValues
    from flext_target_oracle_wms._protocols import (
        FlextTargetOracleWmsProtocolsAuth,
        FlextTargetOracleWmsProtocolsSinger,
    )


class FlextTargetOracleWmsProtocolsTarget:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class WmsTargetConfig(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def wms_auth(self) -> FlextTargetOracleWmsProtocolsAuth.WmsAuthenticationConfig:
            """WMS authentication and endpoint settings."""
            ...

        @property
        def stream_maps(self) -> MutableMapping[str, Mapping[str, str]]:
            """Singer stream map configurations."""
            ...

        @property
        def batch_size(self) -> t.BatchSize:
            """Number of records per batch write."""
            ...

        @property
        def load_method(self) -> FlextTargetOracleWmsConstantsValues.LoadMethods.Method:
            """Load strategy for writing records to WMS."""
            ...

        @property
        def validate_records(self) -> bool:
            """Whether to validate records before writing."""
            ...

    @runtime_checkable
    class SingerSchemaProperties(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def properties(
            self,
        ) -> Mapping[str, FlextTargetOracleWmsProtocolsSinger.SingerFieldSchema]:
            """Singer schema field property definitions."""
            ...


__all__: list[str] = [
    "FlextTargetOracleWmsProtocolsTarget",
]
