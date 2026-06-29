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
    from flext_oracle_wms import d as d, e as e, h as h, r as r, s as s, x as x
    from flext_target_oracle_wms.api import (
        FlextTargetOracleWmsService as FlextTargetOracleWmsService,
        target_oracle_wms as target_oracle_wms,
    )
    from flext_target_oracle_wms.cli import (
        FlextTargetOracleWmsCli as FlextTargetOracleWmsCli,
        main as main,
    )
    from flext_target_oracle_wms.constants import (
        FlextTargetOracleWmsConstants as FlextTargetOracleWmsConstants,
        c as c,
    )
    from flext_target_oracle_wms.factory import (
        FlextTargetFactory as FlextTargetFactory,
        FlextTargetMonitoringFactory as FlextTargetMonitoringFactory,
    )
    from flext_target_oracle_wms.models import (
        FlextTargetOracleWmsModels as FlextTargetOracleWmsModels,
        m as m,
    )
    from flext_target_oracle_wms.protocols import (
        FlextTargetOracleWmsProtocols as FlextTargetOracleWmsProtocols,
        p as p,
    )
    from flext_target_oracle_wms.settings import (
        FlextTargetOracleWmsSettings as FlextTargetOracleWmsSettings,
    )
    from flext_target_oracle_wms.typings import (
        FlextTargetOracleWmsTypes as FlextTargetOracleWmsTypes,
        t as t,
    )
    from flext_target_oracle_wms.utilities import (
        FlextTargetOracleWmsUtilities as FlextTargetOracleWmsUtilities,
        u as u,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
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
        ".factory": (
            "FlextTargetFactory",
            "FlextTargetMonitoringFactory",
        ),
        ".models": (
            "FlextTargetOracleWmsModels",
            "m",
        ),
        ".protocols": (
            "FlextTargetOracleWmsProtocols",
            "p",
        ),
        ".settings": ("FlextTargetOracleWmsSettings",),
        ".typings": (
            "FlextTargetOracleWmsTypes",
            "t",
        ),
        ".utilities": (
            "FlextTargetOracleWmsUtilities",
            "u",
        ),
        "flext_oracle_wms": (
            "d",
            "e",
            "h",
            "r",
            "s",
            "x",
        ),
    },
)


__all__: tuple[str, ...] = (
    "FlextTargetFactory",
    "FlextTargetMonitoringFactory",
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
