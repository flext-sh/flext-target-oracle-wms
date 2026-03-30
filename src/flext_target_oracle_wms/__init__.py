# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext Target Oracle WMS - Oracle WMS Target Client for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

from flext_target_oracle_wms.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if TYPE_CHECKING:
    from flext_meltano import *

    from flext_target_oracle_wms import (
        cli,
        constants,
        factory,
        models,
        protocols,
        target_config,
        typings,
        utilities,
    )
    from flext_target_oracle_wms._utilities import *
    from flext_target_oracle_wms.cli import *
    from flext_target_oracle_wms.constants import *
    from flext_target_oracle_wms.factory import *
    from flext_target_oracle_wms.models import *
    from flext_target_oracle_wms.protocols import *
    from flext_target_oracle_wms.target_config import *
    from flext_target_oracle_wms.typings import *
    from flext_target_oracle_wms.utilities import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "CatalogManager": "flext_target_oracle_wms._utilities.client",
    "FlextTargetFactory": "flext_target_oracle_wms.factory",
    "FlextTargetMonitoringFactory": "flext_target_oracle_wms.factory",
    "FlextTargetOracleWmsCli": "flext_target_oracle_wms.cli",
    "FlextTargetOracleWmsConstants": "flext_target_oracle_wms.constants",
    "FlextTargetOracleWmsModels": "flext_target_oracle_wms.models",
    "FlextTargetOracleWmsProtocols": "flext_target_oracle_wms.protocols",
    "FlextTargetOracleWmsSettings": "flext_target_oracle_wms.target_config",
    "FlextTargetOracleWmsTypes": "flext_target_oracle_wms.typings",
    "FlextTargetOracleWmsUtilities": "flext_target_oracle_wms.utilities",
    "MIN_CONFIG_ARG_COUNT": "flext_target_oracle_wms.cli",
    "StreamProcessor": "flext_target_oracle_wms._utilities.client",
    "Target": "flext_target_oracle_wms._utilities.client",
    "Validation": "flext_target_oracle_wms._utilities.helpers",
    "WMSDataTransformer": "flext_target_oracle_wms._utilities.helpers",
    "WMSSchemaMapper": "flext_target_oracle_wms._utilities.helpers",
    "WMSTableManager": "flext_target_oracle_wms._utilities.helpers",
    "WMSTypeConverter": "flext_target_oracle_wms._utilities.helpers",
    "_utilities": "flext_target_oracle_wms._utilities",
    "c": ["flext_target_oracle_wms.constants", "FlextTargetOracleWmsConstants"],
    "cli": "flext_target_oracle_wms.cli",
    "client": "flext_target_oracle_wms._utilities.client",
    "constants": "flext_target_oracle_wms.constants",
    "create_monitored_oracle_wms_target": "flext_target_oracle_wms.factory",
    "create_oracle_wms_target": "flext_target_oracle_wms.factory",
    "create_record_message": "flext_target_oracle_wms._utilities.helpers",
    "create_schema_message": "flext_target_oracle_wms._utilities.helpers",
    "create_state_message": "flext_target_oracle_wms._utilities.helpers",
    "d": "flext_meltano",
    "e": "flext_meltano",
    "factory": "flext_target_oracle_wms.factory",
    "h": "flext_meltano",
    "helpers": "flext_target_oracle_wms._utilities.helpers",
    "m": ["flext_target_oracle_wms.models", "FlextTargetOracleWmsModels"],
    "main": "flext_target_oracle_wms.cli",
    "models": "flext_target_oracle_wms.models",
    "p": ["flext_target_oracle_wms.protocols", "FlextTargetOracleWmsProtocols"],
    "protocols": "flext_target_oracle_wms.protocols",
    "r": "flext_meltano",
    "s": "flext_meltano",
    "t": ["flext_target_oracle_wms.typings", "FlextTargetOracleWmsTypes"],
    "target_config": "flext_target_oracle_wms.target_config",
    "typings": "flext_target_oracle_wms.typings",
    "u": ["flext_target_oracle_wms.utilities", "FlextTargetOracleWmsUtilities"],
    "utilities": "flext_target_oracle_wms.utilities",
    "x": "flext_meltano",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, sorted(_LAZY_IMPORTS))
