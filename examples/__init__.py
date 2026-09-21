# AUTO-GENERATED FILE — Regenerate with: make gen
"""Examples package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_core import d, h, r, x
    from flext_meltano import s
    from flext_oracle_wms import e
<<<<<<< HEAD
    from flext_target_oracle_wms import (
        FlextTargetOracleWmsConstants,
        FlextTargetOracleWmsConstants as c,
        m,
        p,
        t,
        u,
    )
=======

    from flext_core import d, h, r, x
    from flext_target_oracle_wms import FlextTargetOracleWmsConstants
>>>>>>> origin/0.12.0-dev

    from .constants import (
        ExamplesFlextTargetOracleWmsConstants,
        ExamplesFlextTargetOracleWmsConstants as c,
    )
    from .models import (
        ExamplesFlextTargetOracleWmsModels,
        ExamplesFlextTargetOracleWmsModels as m,
    )
    from .protocols import (
        ExamplesFlextTargetOracleWmsProtocols,
        ExamplesFlextTargetOracleWmsProtocols as p,
    )
    from .typings import (
        ExamplesFlextTargetOracleWmsTypes,
        ExamplesFlextTargetOracleWmsTypes as t,
    )
    from .utilities import (
        ExamplesFlextTargetOracleWmsUtilities,
        ExamplesFlextTargetOracleWmsUtilities as u,
    )
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
            ".constants": ("ExamplesFlextTargetOracleWmsConstants", "c"),
            ".models": ("ExamplesFlextTargetOracleWmsModels", "m"),
            ".protocols": ("ExamplesFlextTargetOracleWmsProtocols", "p"),
            ".typings": ("ExamplesFlextTargetOracleWmsTypes", "t"),
            ".utilities": ("ExamplesFlextTargetOracleWmsUtilities", "u"),
            "flext_core": ("d", "h", "r", "x"),
            "flext_meltano": ("s",),
            "flext_oracle_wms": ("e",),
            "flext_target_oracle_wms": ("FlextTargetOracleWmsConstants",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
