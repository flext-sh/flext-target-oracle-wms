"""Oracle WMS target implementation - DRY PRODUCTION IMPLEMENTATION.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

DRY REFACTORING: Single source of truth using REAL flext-oracle-wms API.
NO DUPLICATION - uses newer, better implementation via SingerTargetOracleWMS.
"""

from __future__ import annotations

# Version info - use standard importlib.metadata
import importlib.metadata

# Provide legacy module path alias: flext_target_oracle_wms.singer.target
# to satisfy tests importing from that location
import sys as _sys
import types as _types

# RE-EXPORT real flext-core types - NO DUPLICATION
from flext_core import FlextResult, FlextValueObject

# === FLEXT-MELTANO COMPLETE INTEGRATION ===
# Re-export ALL flext-meltano facilities for full ecosystem integration
from flext_meltano import (
    BatchSink,
    FlextMeltanoBaseService,
    # Bridge integration
    FlextMeltanoBridge,
    # Configuration and validation
    FlextMeltanoConfig,
    FlextMeltanoEvent,
    # Enterprise services from flext-meltano.base
    FlextMeltanoTargetService,
    # Authentication patterns
    OAuthAuthenticator,
    # Typing definitions
    PropertiesList,
    Property,
    Sink,
    SQLSink,
    # Core Singer SDK classes (centralized from flext-meltano)
    Stream,
    Tap,
    Target,
    create_meltano_target_service,
    # Testing utilities
    get_tap_test_class,
    # Singer typing utilities (centralized)
    singer_typing,
)

# Factory patterns for easier library usage - SOLID principles
from flext_target_oracle_wms.factory import (
    FlextTargetFactory,
    FlextTargetMonitoringFactory,
    create_monitored_oracle_wms_target,
    create_oracle_wms_target,
)
from flext_target_oracle_wms.target_client import (
    # Main target implementation
    SingerTargetOracleWMS,
    SingerWMSCatalogManager,
    SingerWMSStreamProcessor,
)

# Import consolidated models and client classes
from flext_target_oracle_wms.target_models import (
    WMSDataTransformer,
    WMSSchemaMapper,
    WMSTableManager,
    WMSTypeConverter,
)

_legacy_mod_name = "flext_target_oracle_wms.singer.target"
_legacy_mod = _types.ModuleType(_legacy_mod_name)
_legacy_mod.SingerTargetOracleWMS = SingerTargetOracleWMS  # type: ignore[attr-defined]
_sys.modules[_legacy_mod_name] = _legacy_mod

# BACKWARD COMPATIBILITY: Alias to prevent API breakage
# Uses the newer, better code path without changing the interface
TargetOracleWMS = SingerTargetOracleWMS

__version__ = importlib.metadata.version("flext-target-oracle-wms")
__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())

# DRY EXPORTS: Single implementation, multiple access patterns
__all__: list[str] = [
    "BatchSink",
    "FlextMeltanoBaseService",
    # Bridge integration
    "FlextMeltanoBridge",
    # Configuration patterns
    "FlextMeltanoConfig",
    "FlextMeltanoEvent",
    # Enterprise services
    "FlextMeltanoTargetService",
    # === FLEXT-CORE RE-EXPORTS ===
    "FlextResult",
    # === FACTORY PATTERNS ===
    "FlextTargetFactory",
    "FlextTargetMonitoringFactory",
    "FlextValueObject",
    # Authentication
    "OAuthAuthenticator",
    "PropertiesList",
    "Property",
    "SQLSink",
    "SingerTargetOracleWMS",
    "SingerWMSCatalogManager",
    "SingerWMSStreamProcessor",
    "Sink",
    # === FLEXT-MELTANO COMPLETE RE-EXPORTS ===
    # Singer SDK core classes
    "Stream",
    "Tap",
    "Target",
    # === PRIMARY CLASSES ===
    "TargetOracleWMS",
    # === WMS PATTERNS ===
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
    # === METADATA ===
    "__version__",
    "__version_info__",
    "create_meltano_target_service",
    "create_monitored_oracle_wms_target",
    "create_oracle_wms_target",
    # Testing
    "get_tap_test_class",
    # Singer typing
    "singer_typing",
]
