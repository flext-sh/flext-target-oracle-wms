# AUTO-GENERATED FILE — Regenerate with: make gen
"""Examples package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_meltano import (
        cli,
        core,
        d,
        h,
        lazy_attribute,
        meltano,
        r,
        s,
        services,
        x,
    )
    from flext_oracle_wms import api, e, oracle_wms, web

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
    "lazy_attribute",
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
            "flext_meltano": (
                "cli",
                "core",
                "d",
                "h",
                "lazy_attribute",
                "meltano",
                "r",
                "s",
                "services",
                "x",
            ),
            "flext_oracle_wms": ("api", "e", "oracle_wms", "web"),
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
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
