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
    __author__ as __author__,
    __author_email__ as __author_email__,
    __description__ as __description__,
    __license__ as __license__,
    __title__ as __title__,
    __url__ as __url__,
    __version__ as __version__,
    __version_info__ as __version_info__,
)

if TYPE_CHECKING:
    from flext_meltano import d, e, h, r, s, x

    from flext_target_oracle_wms import (
        _utilities as _utilities,
        cli as cli,
        constants as constants,
        factory as factory,
        models as models,
        protocols as protocols,
        target_config as target_config,
        typings as typings,
        utilities as utilities,
    )
    from flext_target_oracle_wms._utilities import client as client, helpers as helpers
    from flext_target_oracle_wms._utilities.client import (
        CatalogManager as CatalogManager,
        StreamProcessor as StreamProcessor,
        Target as Target,
    )
    from flext_target_oracle_wms._utilities.helpers import (
        Validation as Validation,
        WMSDataTransformer as WMSDataTransformer,
        WMSSchemaMapper as WMSSchemaMapper,
        WMSTableManager as WMSTableManager,
        WMSTypeConverter as WMSTypeConverter,
        create_record_message as create_record_message,
        create_schema_message as create_schema_message,
        create_state_message as create_state_message,
    )
    from flext_target_oracle_wms.cli import (
        MIN_CONFIG_ARG_COUNT as MIN_CONFIG_ARG_COUNT,
        FlextTargetOracleWmsCli as FlextTargetOracleWmsCli,
        main as main,
    )
    from flext_target_oracle_wms.constants import (
        FlextTargetOracleWmsConstants as FlextTargetOracleWmsConstants,
        FlextTargetOracleWmsConstants as c,
    )
    from flext_target_oracle_wms.factory import (
        FlextTargetFactory as FlextTargetFactory,
        FlextTargetMonitoringFactory as FlextTargetMonitoringFactory,
        create_monitored_oracle_wms_target as create_monitored_oracle_wms_target,
        create_oracle_wms_target as create_oracle_wms_target,
    )
    from flext_target_oracle_wms.models import (
        FlextTargetOracleWmsModels as FlextTargetOracleWmsModels,
        FlextTargetOracleWmsModels as m,
    )
    from flext_target_oracle_wms.protocols import (
        FlextTargetOracleWmsProtocols as FlextTargetOracleWmsProtocols,
        FlextTargetOracleWmsProtocols as p,
    )
    from flext_target_oracle_wms.target_config import (
        FlextTargetOracleWmsSettings as FlextTargetOracleWmsSettings,
    )
    from flext_target_oracle_wms.typings import (
        FlextTargetOracleWmsTypes as FlextTargetOracleWmsTypes,
        FlextTargetOracleWmsTypes as t,
    )
    from flext_target_oracle_wms.utilities import (
        FlextTargetOracleWmsUtilities as FlextTargetOracleWmsUtilities,
        FlextTargetOracleWmsUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "CatalogManager": ["flext_target_oracle_wms._utilities.client", "CatalogManager"],
    "FlextTargetFactory": ["flext_target_oracle_wms.factory", "FlextTargetFactory"],
    "FlextTargetMonitoringFactory": ["flext_target_oracle_wms.factory", "FlextTargetMonitoringFactory"],
    "FlextTargetOracleWmsCli": ["flext_target_oracle_wms.cli", "FlextTargetOracleWmsCli"],
    "FlextTargetOracleWmsConstants": ["flext_target_oracle_wms.constants", "FlextTargetOracleWmsConstants"],
    "FlextTargetOracleWmsModels": ["flext_target_oracle_wms.models", "FlextTargetOracleWmsModels"],
    "FlextTargetOracleWmsProtocols": ["flext_target_oracle_wms.protocols", "FlextTargetOracleWmsProtocols"],
    "FlextTargetOracleWmsSettings": ["flext_target_oracle_wms.target_config", "FlextTargetOracleWmsSettings"],
    "FlextTargetOracleWmsTypes": ["flext_target_oracle_wms.typings", "FlextTargetOracleWmsTypes"],
    "FlextTargetOracleWmsUtilities": ["flext_target_oracle_wms.utilities", "FlextTargetOracleWmsUtilities"],
    "MIN_CONFIG_ARG_COUNT": ["flext_target_oracle_wms.cli", "MIN_CONFIG_ARG_COUNT"],
    "StreamProcessor": ["flext_target_oracle_wms._utilities.client", "StreamProcessor"],
    "Target": ["flext_target_oracle_wms._utilities.client", "Target"],
    "Validation": ["flext_target_oracle_wms._utilities.helpers", "Validation"],
    "WMSDataTransformer": ["flext_target_oracle_wms._utilities.helpers", "WMSDataTransformer"],
    "WMSSchemaMapper": ["flext_target_oracle_wms._utilities.helpers", "WMSSchemaMapper"],
    "WMSTableManager": ["flext_target_oracle_wms._utilities.helpers", "WMSTableManager"],
    "WMSTypeConverter": ["flext_target_oracle_wms._utilities.helpers", "WMSTypeConverter"],
    "_utilities": ["flext_target_oracle_wms._utilities", ""],
    "c": ["flext_target_oracle_wms.constants", "FlextTargetOracleWmsConstants"],
    "cli": ["flext_target_oracle_wms.cli", ""],
    "client": ["flext_target_oracle_wms._utilities.client", ""],
    "constants": ["flext_target_oracle_wms.constants", ""],
    "create_monitored_oracle_wms_target": ["flext_target_oracle_wms.factory", "create_monitored_oracle_wms_target"],
    "create_oracle_wms_target": ["flext_target_oracle_wms.factory", "create_oracle_wms_target"],
    "create_record_message": ["flext_target_oracle_wms._utilities.helpers", "create_record_message"],
    "create_schema_message": ["flext_target_oracle_wms._utilities.helpers", "create_schema_message"],
    "create_state_message": ["flext_target_oracle_wms._utilities.helpers", "create_state_message"],
    "d": ["flext_meltano", "d"],
    "e": ["flext_meltano", "e"],
    "factory": ["flext_target_oracle_wms.factory", ""],
    "h": ["flext_meltano", "h"],
    "helpers": ["flext_target_oracle_wms._utilities.helpers", ""],
    "m": ["flext_target_oracle_wms.models", "FlextTargetOracleWmsModels"],
    "main": ["flext_target_oracle_wms.cli", "main"],
    "models": ["flext_target_oracle_wms.models", ""],
    "p": ["flext_target_oracle_wms.protocols", "FlextTargetOracleWmsProtocols"],
    "protocols": ["flext_target_oracle_wms.protocols", ""],
    "r": ["flext_meltano", "r"],
    "s": ["flext_meltano", "s"],
    "t": ["flext_target_oracle_wms.typings", "FlextTargetOracleWmsTypes"],
    "target_config": ["flext_target_oracle_wms.target_config", ""],
    "typings": ["flext_target_oracle_wms.typings", ""],
    "u": ["flext_target_oracle_wms.utilities", "FlextTargetOracleWmsUtilities"],
    "utilities": ["flext_target_oracle_wms.utilities", ""],
    "x": ["flext_meltano", "x"],
}

_EXPORTS: Sequence[str] = [
    "CatalogManager",
    "FlextTargetFactory",
    "FlextTargetMonitoringFactory",
    "FlextTargetOracleWmsCli",
    "FlextTargetOracleWmsConstants",
    "FlextTargetOracleWmsModels",
    "FlextTargetOracleWmsProtocols",
    "FlextTargetOracleWmsSettings",
    "FlextTargetOracleWmsTypes",
    "FlextTargetOracleWmsUtilities",
    "MIN_CONFIG_ARG_COUNT",
    "StreamProcessor",
    "Target",
    "Validation",
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "_utilities",
    "c",
    "cli",
    "client",
    "constants",
    "create_monitored_oracle_wms_target",
    "create_oracle_wms_target",
    "create_record_message",
    "create_schema_message",
    "create_state_message",
    "d",
    "e",
    "factory",
    "h",
    "helpers",
    "m",
    "main",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "t",
    "target_config",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
