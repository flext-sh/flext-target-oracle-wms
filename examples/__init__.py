# AUTO-GENERATED FILE — Regenerate with: make gen
"""Examples package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_api import api
    from flext_cli import cli
    from flext_meltano import meltano, s
    from flext_oracle_wms import e, oracle_wms
    from flext_web import web

    from flext_core import (
        core,
        d,
        h,
        lazy,
        lazy_attribute,
        normalize_lazy_imports,
        r,
        x,
    )
    from flext_target_oracle_wms import (
        c,
        config,
        m,
        main,
        p,
        settings,
        t,
        target_oracle_wms,
        u,
    )

    from .constants import ExamplesFlextTargetOracleWmsConstants
    from .models import ExamplesFlextTargetOracleWmsModels
    from .protocols import ExamplesFlextTargetOracleWmsProtocols
    from .typings import ExamplesFlextTargetOracleWmsTypes
    from .utilities import ExamplesFlextTargetOracleWmsUtilities


__all__: tuple[str, ...] = (
    "ExamplesFlextTargetOracleWmsConstants",
    "ExamplesFlextTargetOracleWmsModels",
    "ExamplesFlextTargetOracleWmsProtocols",
    "ExamplesFlextTargetOracleWmsTypes",
    "ExamplesFlextTargetOracleWmsUtilities",
    "api",
    "c",
    "cli",
    "config",
    "core",
    "d",
    "e",
    "h",
    "lazy",
    "lazy_attribute",
    "m",
    "main",
    "meltano",
    "normalize_lazy_imports",
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

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".constants": ("ExamplesFlextTargetOracleWmsConstants",),
            ".models": ("ExamplesFlextTargetOracleWmsModels",),
            ".protocols": ("ExamplesFlextTargetOracleWmsProtocols",),
            ".typings": ("ExamplesFlextTargetOracleWmsTypes",),
            ".utilities": ("ExamplesFlextTargetOracleWmsUtilities",),
            "flext_api": ("api",),
            "flext_cli": ("cli",),
            "flext_core": (
                "core",
                "d",
                "h",
                "lazy",
                "lazy_attribute",
                "normalize_lazy_imports",
                "r",
                "x",
            ),
            "flext_meltano": ("meltano", "s"),
            "flext_oracle_wms": ("e", "oracle_wms"),
            "flext_target_oracle_wms": (
                "c",
                "config",
                "m",
                "main",
                "p",
                "settings",
                "t",
                "target_oracle_wms",
                "u",
            ),
            "flext_web": ("web",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
