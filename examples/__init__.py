# AUTO-GENERATED FILE — Regenerate with: make gen
"""Examples package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_core import (
        FlextTargetOracleWmsConstants,
        FlextTargetOracleWmsConstants as c,
        d,
        e,
        h,
        m,
        p,
        r,
        s,
        t,
        u,
        x,
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
    "FlextTargetOracleWmsConstants",
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "u",
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
            "flext_core": (
                "FlextTargetOracleWmsConstants",
                "c",
                "d",
                "e",
                "h",
                "m",
                "p",
                "r",
                "s",
                "t",
                "u",
                "x",
            ),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
