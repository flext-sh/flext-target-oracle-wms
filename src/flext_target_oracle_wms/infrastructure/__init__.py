"""Oracle WMS infrastructure module using flext-core patterns."""

from __future__ import annotations

# Contextual import suppression for external libraries
import contextlib

# Import from infrastructure module
with contextlib.suppress(ImportError):
    from flext_target_oracle_wms.infrastructure.di_container import (
        TargetOracleWMSContainer,
        get_target_oracle_wms_container,
    )

__all__ = [
    "TargetOracleWMSContainer",
    "get_target_oracle_wms_container",
]
