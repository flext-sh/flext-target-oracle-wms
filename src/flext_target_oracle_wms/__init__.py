"""Oracle WMS target implementation - DRY PRODUCTION IMPLEMENTATION.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

DRY REFACTORING: Single source of truth using REAL flext-oracle-wms API.
NO DUPLICATION - uses newer, better implementation via SingerTargetOracleWMS.
"""

from __future__ import annotations

# RE-EXPORT real flext-core types - NO DUPLICATION
from flext_core import FlextResult, FlextValueObject

# Factory patterns for easier library usage - SOLID principles
from flext_target_oracle_wms.factory import (
    FlextTargetFactory,
    FlextTargetMonitoringFactory,
    create_monitored_oracle_wms_target,
    create_oracle_wms_target,
)

# Import patterns and singer modules
from flext_target_oracle_wms.patterns import (
    WMSDataTransformer,
    WMSSchemaMapper,
    WMSTableManager,
    WMSTypeConverter,
)
from flext_target_oracle_wms.singer.catalog import SingerWMSCatalogManager
from flext_target_oracle_wms.singer.stream import SingerWMSStreamProcessor

# DRY PRINCIPLE: Use ONLY the production-ready implementation
# This eliminates ALL duplication and uses REAL flext-oracle-wms API
from flext_target_oracle_wms.singer.target import SingerTargetOracleWMS

# BACKWARD COMPATIBILITY: Alias to prevent API breakage
# Uses the newer, better code path without changing the interface
TargetOracleWMS = SingerTargetOracleWMS

# Version info
try:
    import importlib.metadata

    __version__ = importlib.metadata.version("flext-target-oracle-wms")
except ImportError:
    __version__ = "1.0.0"

# DRY EXPORTS: Single implementation, multiple access patterns
__all__ = [
    # Sorted alphabetically as required by RUF022
    "FlextResult",
    "FlextTargetFactory",
    "FlextTargetMonitoringFactory",
    "FlextValueObject",
    "SingerTargetOracleWMS",
    "SingerWMSCatalogManager",
    "SingerWMSStreamProcessor",
    "TargetOracleWMS",
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
    "__version__",
    "create_monitored_oracle_wms_target",
    "create_oracle_wms_target",
]
