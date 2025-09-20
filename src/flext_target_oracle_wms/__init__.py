"""Flext Target Oracle WMS - Oracle WMS Target Client for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from .cli import OracleWMSTargetCli, main
from .factory import (
    FlextTargetFactory,
    FlextTargetMonitoringFactory,
    create_monitored_oracle_wms_target,
    create_oracle_wms_target,
)
from .target_client import (
    SingerTargetOracleWMS,
    SingerWMSCatalogManager,
    SingerWMSStreamProcessor,
)
from .target_models import (
    WMSDataTransformer,
    WMSSchemaMapper,
    WMSTableManager,
    WMSTypeConverter,
)

__all__: list[str] = [
    "FlextTargetFactory",
    "FlextTargetMonitoringFactory",
    "OracleWMSTargetCli",
    "SingerTargetOracleWMS",
    "SingerWMSCatalogManager",
    "SingerWMSStreamProcessor",
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
    "create_monitored_oracle_wms_target",
    "create_oracle_wms_target",
    "main",
]
