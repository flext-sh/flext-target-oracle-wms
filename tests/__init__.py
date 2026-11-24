# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_wms import e
    from flext_tests import api, d, h, r, td, tf, tk, tm, x

    from flext_target_oracle_wms import (
        FlextTargetOracleWmsCli,
        FlextTargetOracleWmsConfig,
        FlextTargetOracleWmsConstants,
        FlextTargetOracleWmsModels,
        FlextTargetOracleWmsProtocols,
        FlextTargetOracleWmsService,
        FlextTargetOracleWmsSettings,
        FlextTargetOracleWmsTypes,
        FlextTargetOracleWmsUtilities,
        FlextTargetOracleWmsVersion,
        config,
        main,
        settings,
        target_oracle_wms,
    )
    from tests.base import TestsFlextTargetOracleWmsServiceBase, s
    from tests.constants import TestsFlextTargetOracleWmsConstants, c
    from tests.models import TestsFlextTargetOracleWmsModels, m
    from tests.protocols import TestsFlextTargetOracleWmsProtocols, p
    from tests.settings import TestsFlextTargetOracleWmsSettings
    from tests.typings import TestsFlextTargetOracleWmsTypes, t
    from tests.utilities import TestsFlextTargetOracleWmsUtilities, u


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
    "TestsFlextTargetOracleWmsConstants",
    "TestsFlextTargetOracleWmsModels",
    "TestsFlextTargetOracleWmsProtocols",
    "TestsFlextTargetOracleWmsServiceBase",
    "TestsFlextTargetOracleWmsSettings",
    "TestsFlextTargetOracleWmsTypes",
    "TestsFlextTargetOracleWmsUtilities",
    "api",
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
    "td",
    "tf",
    "tk",
    "tm",
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    {
        "FlextTargetOracleWmsCli": "flext_target_oracle_wms",
        "FlextTargetOracleWmsConfig": "flext_target_oracle_wms",
        "FlextTargetOracleWmsConstants": "flext_target_oracle_wms",
        "FlextTargetOracleWmsModels": "flext_target_oracle_wms",
        "FlextTargetOracleWmsProtocols": "flext_target_oracle_wms",
        "FlextTargetOracleWmsService": "flext_target_oracle_wms",
        "FlextTargetOracleWmsSettings": "flext_target_oracle_wms",
        "FlextTargetOracleWmsTypes": "flext_target_oracle_wms",
        "FlextTargetOracleWmsUtilities": "flext_target_oracle_wms",
        "FlextTargetOracleWmsVersion": "flext_target_oracle_wms",
        "TestsFlextTargetOracleWmsConstants": ".constants",
        "TestsFlextTargetOracleWmsModels": ".models",
        "TestsFlextTargetOracleWmsProtocols": ".protocols",
        "TestsFlextTargetOracleWmsServiceBase": ".base",
        "TestsFlextTargetOracleWmsSettings": ".settings",
        "TestsFlextTargetOracleWmsTypes": ".typings",
        "TestsFlextTargetOracleWmsUtilities": ".utilities",
        "api": "flext_tests",
        "c": ".constants",
        "config": "flext_target_oracle_wms",
        "d": "flext_tests",
        "e": "flext_oracle_wms",
        "h": "flext_tests",
        "m": ".models",
        "main": "flext_target_oracle_wms",
        "p": ".protocols",
        "r": "flext_tests",
        "s": ".base",
        "settings": "flext_target_oracle_wms",
        "t": ".typings",
        "target_oracle_wms": "flext_target_oracle_wms",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "x": "flext_tests",
    },
    public_exports=__all__,
)
