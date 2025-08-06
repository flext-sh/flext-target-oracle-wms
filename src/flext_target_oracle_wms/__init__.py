"""Oracle WMS target implementation - DRY PRODUCTION IMPLEMENTATION.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

DRY REFACTORING: Single source of truth using REAL flext-oracle-wms API.
NO DUPLICATION - uses newer, better implementation via SingerTargetOracleWMS.
"""

from __future__ import annotations

# Version info - use standard importlib.metadata
import importlib.metadata

# === FLEXT-MELTANO COMPLETE INTEGRATION ===
# Re-export ALL flext-meltano facilities for full ecosystem integration
from flext_meltano import (
    # Core Singer SDK classes (centralized from flext-meltano)
    Stream,
    Tap,
    Target,
    Sink,
    BatchSink,
    SQLSink,
    
    # Enterprise services from flext-meltano.base
    FlextMeltanoTargetService,
    FlextMeltanoBaseService,
    create_meltano_target_service,
    
    # Configuration and validation
    FlextMeltanoConfig,
    FlextMeltanoEvent,
    
    # Singer typing utilities (centralized)
    singer_typing,
    
    # Bridge integration
    FlextMeltanoBridge,
    
    # Testing utilities
    get_tap_test_class,
    
    # Authentication patterns
    OAuthAuthenticator,
    
    # Typing definitions
    PropertiesList,
    Property,
)

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

__version__ = importlib.metadata.version("flext-target-oracle-wms")

# DRY EXPORTS: Single implementation, multiple access patterns
__all__: list[str] = [
    # === PRIMARY CLASSES ===
    "TargetOracleWMS",
    "SingerTargetOracleWMS",
    "SingerWMSCatalogManager",
    "SingerWMSStreamProcessor",
    
    # === FLEXT-MELTANO COMPLETE RE-EXPORTS ===
    # Singer SDK core classes
    "Stream",
    "Tap",
    "Target",
    "Sink",
    "BatchSink",
    "SQLSink",
    
    # Enterprise services
    "FlextMeltanoTargetService",
    "FlextMeltanoBaseService",
    "create_meltano_target_service",
    
    # Configuration patterns
    "FlextMeltanoConfig",
    "FlextMeltanoEvent",
    
    # Singer typing
    "singer_typing",
    "PropertiesList",
    "Property",
    
    # Bridge integration
    "FlextMeltanoBridge",
    
    # Testing
    "get_tap_test_class",
    
    # Authentication
    "OAuthAuthenticator",
    
    # === FLEXT-CORE RE-EXPORTS ===
    "FlextResult",
    "FlextValueObject",
    
    # === WMS PATTERNS ===
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
    
    # === FACTORY PATTERNS ===
    "FlextTargetFactory",
    "FlextTargetMonitoringFactory",
    "create_monitored_oracle_wms_target",
    "create_oracle_wms_target",
    
    # === METADATA ===
    "__version__",
]
