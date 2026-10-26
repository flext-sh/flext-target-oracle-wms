# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_wms import e
    from flext_tests import api, install_local_packages, td, tf, tk, tm

    from flext_target_oracle_wms import (
        cli,
        config,
        d,
        h,
        main,
        meltano,
        oracle_wms,
        r,
        settings,
        target_oracle_wms,
        web,
        x,
    )
    from tests.base import TestsFlextTargetOracleWmsServiceBase, s
    from tests.constants import TestsFlextTargetOracleWmsConstants, c
    from tests.models import TestsFlextTargetOracleWmsModels, m
    from tests.protocols import TestsFlextTargetOracleWmsProtocols, p
    from tests.settings import TestsFlextTargetOracleWmsSettings
    from tests.typings import TestsFlextTargetOracleWmsTypes, t
    from tests.utilities import TestsFlextTargetOracleWmsUtilities, u


__all__: tuple[str, ...] = (
    "TestsFlextTargetOracleWmsConstants",
    "TestsFlextTargetOracleWmsModels",
    "TestsFlextTargetOracleWmsProtocols",
    "TestsFlextTargetOracleWmsServiceBase",
    "TestsFlextTargetOracleWmsSettings",
    "TestsFlextTargetOracleWmsTypes",
    "TestsFlextTargetOracleWmsUtilities",
    "api",
    "c",
    "cli",
    "config",
    "d",
    "e",
    "h",
    "install_local_packages",
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
    "td",
    "tf",
    "tk",
    "tm",
    "u",
    "web",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "TestsFlextTargetOracleWmsConstants": ".constants",
        "TestsFlextTargetOracleWmsModels": ".models",
        "TestsFlextTargetOracleWmsProtocols": ".protocols",
        "TestsFlextTargetOracleWmsServiceBase": ".base",
        "TestsFlextTargetOracleWmsSettings": ".settings",
        "TestsFlextTargetOracleWmsTypes": ".typings",
        "TestsFlextTargetOracleWmsUtilities": ".utilities",
        "api": "flext_tests",
        "c": ".constants",
        "cli": "flext_target_oracle_wms",
        "config": "flext_target_oracle_wms",
        "d": "flext_target_oracle_wms",
        "e": "flext_oracle_wms",
        "h": "flext_target_oracle_wms",
        "install_local_packages": "flext_tests",
        "m": ".models",
        "main": "flext_target_oracle_wms",
        "meltano": "flext_target_oracle_wms",
        "oracle_wms": "flext_target_oracle_wms",
        "p": ".protocols",
        "r": "flext_target_oracle_wms",
        "s": ".base",
        "settings": "flext_target_oracle_wms",
        "t": ".typings",
        "target_oracle_wms": "flext_target_oracle_wms",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "web": "flext_target_oracle_wms",
        "x": "flext_target_oracle_wms",
    }),
    public_exports=__all__,
)
