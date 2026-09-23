# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_meltano import meltano
    from flext_oracle_wms import e, oracle_wms, web
    from flext_tests import (
        api,
        cli,
        core,
        d,
        h,
        install_local_packages,
        lazy_attribute,
        load_infra_report,
        r,
        services,
        td,
        tf,
        tk,
        tm,
        tv,
        x,
    )

    from flext_target_oracle_wms import config, main, settings, target_oracle_wms

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
    "cli",
    "config",
    "core",
    "d",
    "e",
    "examples",
    "h",
    "install_local_packages",
    "integration",
    "lazy_attribute",
    "load_infra_report",
    "m",
    "main",
    "meltano",
    "oracle_wms",
    "p",
    "r",
    "s",
    "services",
    "settings",
    "t",
    "target_oracle_wms",
    "td",
    "tf",
    "tk",
    "tm",
    "tv",
    "u",
    "unit",
    "web",
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
            "flext_meltano": ("meltano",),
            "flext_oracle_wms": ("e", "oracle_wms", "web"),
            "flext_target_oracle_wms": (
                "config",
                "main",
                "settings",
                "target_oracle_wms",
            ),
            "flext_tests": (
                "api",
                "cli",
                "core",
                "d",
                "h",
                "install_local_packages",
                "lazy_attribute",
                "load_infra_report",
                "r",
                "services",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "x",
            ),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
