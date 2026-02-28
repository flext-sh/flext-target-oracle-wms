"""Flext Target Oracle WMS - Oracle WMS Target Client for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from flext_target_oracle_wms.__version__ import __version__, __version_info__
from flext_target_oracle_wms.cli import OracleWMSTargetCli, main
from flext_target_oracle_wms.constants import FlextTargetOracleWmsConstants, c
from flext_target_oracle_wms.factory import (
    FlextTargetFactory,
    FlextTargetMonitoringFactory,
    create_monitored_oracle_wms_target,
    create_oracle_wms_target,
)
from flext_target_oracle_wms.models import FlextTargetOracleWmsModels, m
from flext_target_oracle_wms.protocols import FlextTargetOracleWmsProtocols
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
from flext_target_oracle_wms.utilities import FlextTargetOracleWmsUtilities

__all__: list[str] = [
    "FlextTargetFactory",
    "FlextTargetMonitoringFactory",
    "FlextTargetOracleWmsConstants",
    "FlextTargetOracleWmsModels",
    "FlextTargetOracleWmsProtocols",
    "FlextTargetOracleWmsUtilities",
    "OracleWMSTargetCli",
    "SingerTargetOracleWMS",
    "SingerWMSCatalogManager",
    "SingerWMSStreamProcessor",
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
    "__version__",
    "__version_info__",
    "c",
    "create_monitored_oracle_wms_target",
    "create_oracle_wms_target",
    "m",
    "main",
]
