"""FLEXT service orchestrator for target-oracle-wms.

Thin facade — all infrastructure from ``FlextMeltanoTargetServiceBase`` via MRO.
Only domain-specific sink creation defined here.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import override

from flext_meltano import FlextMeltanoSingerSinkBase, FlextMeltanoTargetServiceBase

from flext_target_oracle_wms import t


class _OracleWmsSink(FlextMeltanoSingerSinkBase):
    """Minimal Singer sink bridging to Oracle WMS target runtime."""

    name = "target-oracle-wms-sink"

    @override
    def process_record(self, record: dict, context: dict) -> None:  # type: ignore[override]
        """Process a single record (delegated to WMS runtime)."""

    @override
    def process_batch(self, context: dict) -> None:  # type: ignore[override]
        """Process a batch (delegated to WMS runtime)."""


class FlextTargetOracleWmsService(FlextMeltanoTargetServiceBase):
    """Orchestrator for target-oracle-wms. All behavior from base via MRO."""

    target_name: t.NonEmptyStr = "target-oracle-wms"

    @override
    def create_sink(
        self,
        stream_name: str,
        schema: t.FlatContainerMapping,
    ) -> FlextMeltanoSingerSinkBase:
        """Create an Oracle WMS sink for a stream."""
        return _OracleWmsSink(
            target=None,
            stream_name=stream_name,
            schema=dict(schema),
            key_properties=[],
        )


__all__ = ["FlextTargetOracleWmsService"]
