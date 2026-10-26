# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Wms package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_meltano import cli, d, h, meltano, r, s, x
    from flext_oracle_wms import api, e, oracle_wms, web

    from flext_target_oracle_wms.__version__ import (
        FlextTargetOracleWmsVersion,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
    )
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
    "FlextTargetOracleWmsVersion",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "api",
    "c",
    "cli",
    "config",
    "d",
    "e",
    "h",
    "m",
    "main",
    "meltano",
    "oracle_wms",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "target_oracle_wms",
    "u",
    "web",
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
        "FlextTargetOracleWmsVersion": ".__version__",
        "__author__": ".__version__",
        "__author_email__": ".__version__",
        "__description__": ".__version__",
        "__license__": ".__version__",
        "__title__": ".__version__",
        "__url__": ".__version__",
        "__version_info__": ".__version__",
        "api": "flext_oracle_wms",
        "c": ".constants",
        "cli": "flext_meltano",
        "config": "._config",
        "d": "flext_meltano",
        "e": "flext_oracle_wms",
        "h": "flext_meltano",
        "m": ".models",
        "main": ".cli",
        "meltano": "flext_meltano",
        "oracle_wms": "flext_oracle_wms",
        "p": ".protocols",
        "r": "flext_meltano",
        "s": "flext_meltano",
        "settings": "._settings",
        "t": ".typings",
        "target_oracle_wms": ".api",
        "u": ".utilities",
        "web": "flext_oracle_wms",
        "x": "flext_meltano",
    }),
    public_exports=__all__,
)

if not TYPE_CHECKING:
    from flext_target_oracle_wms.__version__ import __version__
