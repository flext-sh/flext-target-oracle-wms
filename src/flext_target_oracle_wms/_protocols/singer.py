# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_target_oracle_wms/_protocols/singer
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols


class FlextTargetOracleWmsProtocolsSinger:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class SingerFieldSchema(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def type(self) -> str:
            """JSON schema type descriptor for the field."""
            ...


__all__: list[str] = [
    "FlextTargetOracleWmsProtocolsSinger",
]
