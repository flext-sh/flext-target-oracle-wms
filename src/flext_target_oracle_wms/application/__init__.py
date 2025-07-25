"""Oracle WMS application module using flext-core patterns."""

from __future__ import annotations

# Contextual import suppression for external libraries
import contextlib

# Import from application module
with contextlib.suppress(ImportError):
    from flext_target_oracle_wms.application.orchestrator import (
        OracleWMSTargetOrchestrator,
    )

__all__ = [
    "OracleWMSTargetOrchestrator",
]
