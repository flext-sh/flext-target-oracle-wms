# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import api, td, tf, tk, tm, tv

    from flext_target_oracle_wms import d, e, h, r, x

    from . import examples, integration, unit
    from .base import (
        TestsFlextTargetOracleWmsServiceBase,
        TestsFlextTargetOracleWmsServiceBase as s,
    )
    from .constants import TestsFlextTargetOracleWmsConstants, c
    from .models import TestsFlextTargetOracleWmsModels, m
    from .protocols import TestsFlextTargetOracleWmsProtocols, p
    from .settings import TestsFlextTargetOracleWmsSettings
    from .typings import TestsFlextTargetOracleWmsTypes, t
    from .utilities import TestsFlextTargetOracleWmsUtilities, u


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
    "tv",
    "u",
    "unit",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("TestsFlextTargetOracleWmsServiceBase", "s"),
            ".constants": ("TestsFlextTargetOracleWmsConstants", "c"),
            ".examples": ("examples",),
            ".integration": ("integration",),
            ".models": ("TestsFlextTargetOracleWmsModels", "m"),
            ".protocols": ("TestsFlextTargetOracleWmsProtocols", "p"),
            ".settings": ("TestsFlextTargetOracleWmsSettings",),
            ".typings": ("TestsFlextTargetOracleWmsTypes", "t"),
            ".unit": ("unit",),
            ".utilities": ("TestsFlextTargetOracleWmsUtilities", "u"),
            "flext_target_oracle_wms": ("d", "e", "h", "r", "x"),
            "flext_tests": ("api", "td", "tf", "tk", "tm", "tv"),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
