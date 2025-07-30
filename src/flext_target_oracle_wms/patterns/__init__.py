"""Oracle WMS patterns module using flext-core patterns."""

from __future__ import annotations

# DRY: REAL imports - NO FALLBACKS, NO SUPPRESS
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
