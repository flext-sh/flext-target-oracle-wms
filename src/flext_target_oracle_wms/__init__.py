# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Wms package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports
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
    from flext_meltano import d, h, r, s, x
    from flext_oracle_wms import e

    from flext_target_oracle_wms._config import FlextTargetOracleWmsConfig, config
    from flext_target_oracle_wms._settings import FlextTargetOracleWmsSettings, settings
    from flext_target_oracle_wms.api import (
        FlextTargetOracleWmsService,
        target_oracle_wms,
    )
    from flext_target_oracle_wms.cli import FlextTargetOracleWmsCli, main
    from flext_target_oracle_wms.constants import FlextTargetOracleWmsConstants, c
    from flext_target_oracle_wms.models import FlextTargetOracleWmsModels, m
    from flext_target_oracle_wms.protocols import FlextTargetOracleWmsProtocols, p
    from flext_target_oracle_wms.typings import FlextTargetOracleWmsTypes, t
    from flext_target_oracle_wms.utilities import FlextTargetOracleWmsUtilities, u


__all__: tuple[str, ...] = (
    "FlextTargetOracleWmsCli",
    "FlextTargetOracleWmsConfig",
    "FlextTargetOracleWmsConstants",
    "FlextTargetOracleWmsModels",
    "FlextTargetOracleWmsProtocols",
    "FlextTargetOracleWmsService",
    "FlextTargetOracleWmsSettings",
    "FlextTargetOracleWmsTypes",
    "FlextTargetOracleWmsUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "config",
    "d",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "target_oracle_wms",
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextTargetOracleWmsCli": ".cli",
        "FlextTargetOracleWmsConfig": "._config",
        "FlextTargetOracleWmsConstants": ".constants",
        "FlextTargetOracleWmsModels": ".models",
        "FlextTargetOracleWmsProtocols": ".protocols",
        "FlextTargetOracleWmsService": ".api",
        "FlextTargetOracleWmsSettings": "._settings",
        "FlextTargetOracleWmsTypes": ".typings",
        "FlextTargetOracleWmsUtilities": ".utilities",
        "c": ".constants",
        "config": "._config",
        "d": "flext_meltano",
        "e": "flext_oracle_wms",
        "h": "flext_meltano",
        "m": ".models",
        "main": ".cli",
        "p": ".protocols",
        "r": "flext_meltano",
        "s": "flext_meltano",
        "settings": "._settings",
        "t": ".typings",
        "target_oracle_wms": ".api",
        "u": ".utilities",
        "x": "flext_meltano",
    }),
    public_exports=__all__,
)
