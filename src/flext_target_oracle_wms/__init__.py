# @generated AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Wms package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import __author__ as __author__
from .__version__ import __author_email__ as __author_email__
from .__version__ import __description__ as __description__
from .__version__ import __license__ as __license__
from .__version__ import __title__ as __title__
from .__version__ import __url__ as __url__
from .__version__ import __version__ as __version__
from .__version__ import __version_info__ as __version_info__

if TYPE_CHECKING:
    from flext_meltano import d as d
    from flext_meltano import e as e
    from flext_meltano import h as h
    from flext_meltano import r as r
    from flext_meltano import s as s
    from flext_meltano import x as x

    from ._config import FlextTargetOracleWmsConfig as FlextTargetOracleWmsConfig
    from ._config import config as config
    from ._settings import FlextTargetOracleWmsSettings as FlextTargetOracleWmsSettings
    from ._settings import settings as settings
    from .api import FlextTargetOracleWmsService as FlextTargetOracleWmsService
    from .api import target_oracle_wms as target_oracle_wms
    from .cli import FlextTargetOracleWmsCli as FlextTargetOracleWmsCli
    from .cli import main as main
    from .constants import (
        FlextTargetOracleWmsConstants as FlextTargetOracleWmsConstants,
    )

    c: type[FlextTargetOracleWmsConstants]
    from .models import FlextTargetOracleWmsModels as FlextTargetOracleWmsModels

    m: type[FlextTargetOracleWmsModels]
    from .protocols import (
        FlextTargetOracleWmsProtocols as FlextTargetOracleWmsProtocols,
    )

    p: type[FlextTargetOracleWmsProtocols]
    from .typings import FlextTargetOracleWmsTypes as FlextTargetOracleWmsTypes

    t: type[FlextTargetOracleWmsTypes]
    from .utilities import (
        FlextTargetOracleWmsUtilities as FlextTargetOracleWmsUtilities,
    )

    u: type[FlextTargetOracleWmsUtilities]

_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    "._config": ("FlextTargetOracleWmsConfig", "config"),
    "._settings": ("FlextTargetOracleWmsSettings", "settings"),
    ".api": ("FlextTargetOracleWmsService", "target_oracle_wms"),
    ".cli": ("FlextTargetOracleWmsCli", "main"),
    ".constants": ("FlextTargetOracleWmsConstants", "c"),
    ".models": ("FlextTargetOracleWmsModels", "m"),
    ".protocols": ("FlextTargetOracleWmsProtocols", "p"),
    ".typings": ("FlextTargetOracleWmsTypes", "t"),
    ".utilities": ("FlextTargetOracleWmsUtilities", "u"),
    "flext_meltano": ("d", "e", "h", "r", "s", "x"),
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES, alias_groups=_LAZY_ALIAS_GROUPS, sort_keys=False
)

_PUBLIC_EXPORTS: tuple[str, ...] = (
    "FlextTargetOracleWmsCli",
    "FlextTargetOracleWmsConfig",
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
    "u",
    "x",
)

__all__: tuple[str, ...] = tuple(_PUBLIC_EXPORTS)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
