# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_oracle_wms import e
    from flext_tests import api, td, tf, tk, tm

    from flext_target_oracle_wms import d, h, r, x
    from tests import examples, integration, unit
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
    "d",
    "e",
    "examples",
    "h",
    "integration",
    "m",
    "p",
    "r",
    "s",
    "t",
    "td",
    "tf",
    "tk",
    "tm",
    "u",
    "unit",
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
        "d": "flext_target_oracle_wms",
        "e": "flext_oracle_wms",
        "examples": ".examples",
        "h": "flext_target_oracle_wms",
        "integration": ".integration",
        "m": ".models",
        "p": ".protocols",
        "r": "flext_target_oracle_wms",
        "s": ".base",
        "t": ".typings",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "unit": ".unit",
        "x": "flext_target_oracle_wms",
    }),
    public_exports=__all__,
)
