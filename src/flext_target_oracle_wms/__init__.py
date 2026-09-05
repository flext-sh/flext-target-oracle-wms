# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Wms package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

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
    from enum import StrEnum, unique
    from flext_meltano import FlextMeltanoConstants as meltano_c, d, e, h, r, s, x
    from typing import Final, TYPE_CHECKING

    from ._config import FlextTargetOracleWmsConfig, config
    from ._settings import FlextTargetOracleWmsSettings, settings
    from .api import FlextTargetOracleWmsService, target_oracle_wms
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
__all__: tuple[str, ...] = (
    "TYPE_CHECKING",
    "Final",
    "FlextTargetOracleWmsConfig",
    "FlextTargetOracleWmsConstants",
    "FlextTargetOracleWmsModels",
    "FlextTargetOracleWmsProtocols",
    "FlextTargetOracleWmsService",
    "FlextTargetOracleWmsSettings",
    "FlextTargetOracleWmsTypes",
    "FlextTargetOracleWmsUtilities",
    "StrEnum",
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
    "meltano_c",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "target_oracle_wms",
    "u",
    "unique",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            "._config": ("FlextTargetOracleWmsConfig", "config"),
            "._settings": ("FlextTargetOracleWmsSettings", "settings"),
            ".api": ("FlextTargetOracleWmsService", "target_oracle_wms"),
            ".constants": ("FlextTargetOracleWmsConstants", "c"),
            ".models": ("FlextTargetOracleWmsModels", "m"),
            ".protocols": ("FlextTargetOracleWmsProtocols", "p"),
            ".typings": ("FlextTargetOracleWmsTypes", "t"),
            ".utilities": ("FlextTargetOracleWmsUtilities", "u"),
            "enum": ("StrEnum", "unique"),
            "flext_meltano": ("d", "e", "h", "r", "s", "x"),
            "typing": ("Final", "TYPE_CHECKING"),
        }),
        alias_groups=MappingProxyType({
            "flext_meltano": (("meltano_c", "FlextMeltanoConstants"),)
        }),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
