# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext Target Oracle WMS - Oracle WMS Target Client for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

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

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_meltano import d, e, h, r, s, x

    from flext_target_oracle_wms import (
        _utilities,
        cli,
        constants,
        factory,
        models,
        protocols,
        target_config,
        typings,
        utilities,
    )
    from flext_target_oracle_wms._utilities import (
        CatalogManager,
        StreamProcessor,
        Target,
        Validation,
        WMSDataTransformer,
        WMSSchemaMapper,
        WMSTableManager,
        WMSTypeConverter,
        client,
        create_record_message,
        create_schema_message,
        create_state_message,
        helpers,
    )
    from flext_target_oracle_wms.cli import (
        MIN_CONFIG_ARG_COUNT,
        FlextTargetOracleWmsCli,
        main,
    )
    from flext_target_oracle_wms.constants import (
        FlextTargetOracleWmsConstants,
        FlextTargetOracleWmsConstants as c,
    )
    from flext_target_oracle_wms.factory import (
        FlextTargetFactory,
        FlextTargetMonitoringFactory,
        create_monitored_oracle_wms_target,
        create_oracle_wms_target,
    )
    from flext_target_oracle_wms.models import (
        FlextTargetOracleWmsModels,
        FlextTargetOracleWmsModels as m,
    )
    from flext_target_oracle_wms.protocols import (
        FlextTargetOracleWmsProtocols,
        FlextTargetOracleWmsProtocols as p,
    )
    from flext_target_oracle_wms.target_config import FlextTargetOracleWmsSettings
    from flext_target_oracle_wms.typings import (
        FlextTargetOracleWmsTypes,
        FlextTargetOracleWmsTypes as t,
    )
    from flext_target_oracle_wms.utilities import (
        FlextTargetOracleWmsUtilities,
        FlextTargetOracleWmsUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = merge_lazy_imports(
    ("flext_target_oracle_wms._utilities",),
    {
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
        "_utilities": "flext_target_oracle_wms._utilities",
        "c": ("flext_target_oracle_wms.constants", "FlextTargetOracleWmsConstants"),
        "cli": "flext_target_oracle_wms.cli",
        "constants": "flext_target_oracle_wms.constants",
        "create_monitored_oracle_wms_target": "flext_target_oracle_wms.factory",
        "create_oracle_wms_target": "flext_target_oracle_wms.factory",
        "d": "flext_meltano",
        "e": "flext_meltano",
        "factory": "flext_target_oracle_wms.factory",
        "h": "flext_meltano",
        "m": ("flext_target_oracle_wms.models", "FlextTargetOracleWmsModels"),
        "main": "flext_target_oracle_wms.cli",
        "models": "flext_target_oracle_wms.models",
        "p": ("flext_target_oracle_wms.protocols", "FlextTargetOracleWmsProtocols"),
        "protocols": "flext_target_oracle_wms.protocols",
        "r": "flext_meltano",
        "s": "flext_meltano",
        "t": ("flext_target_oracle_wms.typings", "FlextTargetOracleWmsTypes"),
        "target_config": "flext_target_oracle_wms.target_config",
        "typings": "flext_target_oracle_wms.typings",
        "u": ("flext_target_oracle_wms.utilities", "FlextTargetOracleWmsUtilities"),
        "utilities": "flext_target_oracle_wms.utilities",
        "x": "flext_meltano",
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "__author__",
        "__author_email__",
        "__description__",
        "__license__",
        "__title__",
        "__url__",
        "__version__",
        "__version_info__",
    ],
)
