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

if TYPE_CHECKING:
    from flext_target_oracle_wms import c, t
    from flext_target_oracle_wms._protocols import (
        FlextTargetOracleWmsProtocolsAuth,
        FlextTargetOracleWmsProtocolsSinger,
    )


class FlextTargetOracleWmsProtocolsTarget:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class WmsTargetConfig(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def wms_auth(self) -> FlextTargetOracleWmsProtocolsAuth.WmsAuthenticationConfig:
            """WMS authentication and endpoint settings."""
            ...

        stream_maps: MutableMapping[str, Mapping[str, str]]
        batch_size: t.BatchSize
        load_method: c.TargetOracleWms.LoadMethods.Method
        validate_records: bool

    @runtime_checkable
    class SingerSchemaProperties(FlextMeltanoProtocols.BaseModel, Protocol):
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
