"""Flext Target Oracle WMS - Oracle WMS Target Client for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

import importlib.metadata
import sys as _sys
import types as _types

from flext_core import FlextModels, FlextResult, FlextTypes
from flext_meltano import (
    FlextMeltanoBridge,
    FlextMeltanoConfig,
    FlextMeltanoTargetService,
)
from flext_target_oracle_wms.cli import OracleWMSTargetCli, main
from flext_target_oracle_wms.factory import (
    FlextTargetFactory,
    FlextTargetMonitoringFactory,
    create_monitored_oracle_wms_target,
    create_oracle_wms_target,
)
from flext_target_oracle_wms.target_client import (
    SingerTargetOracleWMS,
    SingerWMSCatalogManager,
    SingerWMSStreamProcessor,
)
from flext_target_oracle_wms.target_models import (
    WMSDataTransformer,
    WMSSchemaMapper,
    WMSTableManager,
    WMSTypeConverter,
)

_legacy_mod_name = "flext_target_oracle_wms.singer.target"
_legacy_mod = _types.ModuleType(_legacy_mod_name)
setattr(_legacy_mod, "SingerTargetOracleWMS", SingerTargetOracleWMS)
_sys.modules[_legacy_mod_name] = _legacy_mod

# BACKWARD COMPATIBILITY: Alias to prevent API breakage
# Uses the newer, better code path without changing the interface
TargetOracleWMS = SingerTargetOracleWMS

__version__ = importlib.metadata.version("flext-target-oracle-wms")
__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())

# DRY EXPORTS: Single implementation, multiple access patterns
__all__: FlextTypes.Core.StringList = [
    "BatchSink",
    "FlextMeltanoBaseService",
    # Bridge integration
    "FlextMeltanoBridge",
    # Configuration patterns
    "FlextMeltanoConfig",
    "FlextMeltanoEvent",
    # Enterprise services
    "FlextMeltanoTargetService",
    "FlextModels",
    # === FLEXT-CORE RE-EXPORTS ===
    "FlextResult",
    # === FACTORY PATTERNS ===
    "FlextTargetFactory",
    "FlextTargetMonitoringFactory",
    # Authentication
    "OAuthAuthenticator",
    # === CLI ===
    "OracleWMSTargetCli",
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
    "main",
    # Singer typing
    "singer_typing",
]
