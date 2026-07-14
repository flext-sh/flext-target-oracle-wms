# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Wms package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports
from flext_target_oracle_wms.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if TYPE_CHECKING:
    from flext_meltano import d, e, h, r, s, x

    from ._settings import FlextTargetOracleWmsSettings, settings
    from .api import FlextTargetOracleWmsService, target_oracle_wms
    from .cli import FlextTargetOracleWmsCli, main
    from .constants import (
        FlextTargetOracleWmsConstants,
        FlextTargetOracleWmsConstants as c,
    )
    from .models import FlextTargetOracleWmsModels, FlextTargetOracleWmsModels as m
    from .protocols import (
        FlextTargetOracleWmsProtocols,
        FlextTargetOracleWmsProtocols as p,
    )
    from .typings import FlextTargetOracleWmsTypes, FlextTargetOracleWmsTypes as t
    from .utilities import (
        FlextTargetOracleWmsUtilities,
        FlextTargetOracleWmsUtilities as u,
    )

    _ = (
        c,
        FlextTargetOracleWmsConstants,
        t,
        FlextTargetOracleWmsTypes,
        p,
        FlextTargetOracleWmsProtocols,
        m,
        FlextTargetOracleWmsModels,
        u,
        FlextTargetOracleWmsUtilities,
        d,
        e,
        h,
        r,
        s,
        x,
        main,
        FlextTargetOracleWmsCli,
        FlextTargetOracleWmsSettings,
        settings,
        FlextTargetOracleWmsService,
        target_oracle_wms,
    )


_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    "._settings": (
        "FlextTargetOracleWmsSettings",
        "settings",
    ),
    ".api": (
        "FlextTargetOracleWmsService",
        "target_oracle_wms",
    ),
    ".cli": (
        "FlextTargetOracleWmsCli",
        "main",
    ),
    ".constants": (
        "FlextTargetOracleWmsConstants",
        "c",
    ),
    ".models": (
        "FlextTargetOracleWmsModels",
        "m",
    ),
    ".protocols": (
        "FlextTargetOracleWmsProtocols",
        "p",
    ),
    ".typings": (
        "FlextTargetOracleWmsTypes",
        "t",
    ),
    ".utilities": (
        "FlextTargetOracleWmsUtilities",
        "u",
    ),
    "flext_meltano": (
        "d",
        "e",
        "h",
        "r",
        "s",
        "x",
    ),
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES,
    alias_groups=_LAZY_ALIAS_GROUPS,
    sort_keys=False,
)

_DIRECT_IMPORTS: tuple[str, ...] = (
    "FlextTargetOracleWmsCli",
    "FlextTargetOracleWmsConstants",
    "FlextTargetOracleWmsModels",
    "FlextTargetOracleWmsProtocols",
    "FlextTargetOracleWmsService",
    "FlextTargetOracleWmsSettings",
    "FlextTargetOracleWmsTypes",
    "FlextTargetOracleWmsUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "build_lazy_import_map",
    "c",
    "d",
    "e",
    "h",
    "install_lazy_exports",
    "m",
    "main",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "target_oracle_wms",
    "u",
    "x",
)

__all__: tuple[str, ...] = (
    "FlextTargetOracleWmsCli",
    "FlextTargetOracleWmsConstants",
    "FlextTargetOracleWmsModels",
    "FlextTargetOracleWmsProtocols",
    "FlextTargetOracleWmsService",
    "FlextTargetOracleWmsSettings",
    "FlextTargetOracleWmsTypes",
    "FlextTargetOracleWmsUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
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
    "u",
    "x",
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    public_exports=__all__,
)
