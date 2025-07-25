"""Oracle WMS patterns module using flext-core patterns."""

from __future__ import annotations

# Contextual import suppression for external libraries
import contextlib

# Import from patterns module
with contextlib.suppress(ImportError):
    from flext_target_oracle_wms.patterns.wms_patterns import (
        WMSDataTransformer,
        WMSSchemaMapper,
        WMSTableManager,
        WMSTypeConverter,
    )

__all__ = [
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
]
