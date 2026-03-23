# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Flext Target Oracle WMS - Oracle WMS Target Client for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_meltano import d, e, h, r, s, x

    from flext_target_oracle_wms.__version__ import (
        __all__,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
    )
    from flext_target_oracle_wms.cli import (
        MIN_CONFIG_ARG_COUNT,
        OracleWMSTargetCli,
        main,
    )
    from flext_target_oracle_wms.constants import (
        FlextTargetOracleWmsConstants,
        FlextTargetOracleWmsConstants as c,
    )
    from flext_target_oracle_wms.factory import (
        FlextTargetFactory,
        FlextTargetMonitoringFactory,
        create_monitored_oracle_wms_target,
        create_oracle_wms_target,
    )
    from flext_target_oracle_wms.models import (
        FlextTargetOracleWmsModels,
        FlextTargetOracleWmsModels as m,
    )
    from flext_target_oracle_wms.protocols import (
        FlextTargetOracleWmsProtocols,
        FlextTargetOracleWmsProtocols as p,
    )
    from flext_target_oracle_wms.target_client import (
        SingerTargetOracleWMS,
        SingerWMSCatalogManager,
        SingerWMSStreamProcessor,
    )
    from flext_target_oracle_wms.target_config import FlextTargetOracleWmsSettings
    from flext_target_oracle_wms.typings import (
        FlextTargetOracleWmsTypes,
        FlextTargetOracleWmsTypes as t,
    )
    from flext_target_oracle_wms.utilities import (
        FlextTargetOracleWmsUtilities,
        FlextTargetOracleWmsUtilities as u,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextTargetFactory": ("flext_target_oracle_wms.factory", "FlextTargetFactory"),
    "FlextTargetMonitoringFactory": (
        "flext_target_oracle_wms.factory",
        "FlextTargetMonitoringFactory",
    ),
    "FlextTargetOracleWmsConstants": (
        "flext_target_oracle_wms.constants",
        "FlextTargetOracleWmsConstants",
    ),
    "FlextTargetOracleWmsModels": (
        "flext_target_oracle_wms.models",
        "FlextTargetOracleWmsModels",
    ),
    "FlextTargetOracleWmsProtocols": (
        "flext_target_oracle_wms.protocols",
        "FlextTargetOracleWmsProtocols",
    ),
    "FlextTargetOracleWmsSettings": (
        "flext_target_oracle_wms.target_config",
        "FlextTargetOracleWmsSettings",
    ),
    "FlextTargetOracleWmsTypes": (
        "flext_target_oracle_wms.typings",
        "FlextTargetOracleWmsTypes",
    ),
    "FlextTargetOracleWmsUtilities": (
        "flext_target_oracle_wms.utilities",
        "FlextTargetOracleWmsUtilities",
    ),
    "MIN_CONFIG_ARG_COUNT": ("flext_target_oracle_wms.cli", "MIN_CONFIG_ARG_COUNT"),
    "OracleWMSTargetCli": ("flext_target_oracle_wms.cli", "OracleWMSTargetCli"),
    "SingerTargetOracleWMS": (
        "flext_target_oracle_wms.target_client",
        "SingerTargetOracleWMS",
    ),
    "SingerWMSCatalogManager": (
        "flext_target_oracle_wms.target_client",
        "SingerWMSCatalogManager",
    ),
    "SingerWMSStreamProcessor": (
        "flext_target_oracle_wms.target_client",
        "SingerWMSStreamProcessor",
    ),
    "__all__": ("flext_target_oracle_wms.__version__", "__all__"),
    "__author__": ("flext_target_oracle_wms.__version__", "__author__"),
    "__author_email__": ("flext_target_oracle_wms.__version__", "__author_email__"),
    "__description__": ("flext_target_oracle_wms.__version__", "__description__"),
    "__license__": ("flext_target_oracle_wms.__version__", "__license__"),
    "__title__": ("flext_target_oracle_wms.__version__", "__title__"),
    "__url__": ("flext_target_oracle_wms.__version__", "__url__"),
    "__version__": ("flext_target_oracle_wms.__version__", "__version__"),
    "__version_info__": ("flext_target_oracle_wms.__version__", "__version_info__"),
    "c": ("flext_target_oracle_wms.constants", "FlextTargetOracleWmsConstants"),
    "create_monitored_oracle_wms_target": (
        "flext_target_oracle_wms.factory",
        "create_monitored_oracle_wms_target",
    ),
    "create_oracle_wms_target": (
        "flext_target_oracle_wms.factory",
        "create_oracle_wms_target",
    ),
    "d": ("flext_meltano", "d"),
    "e": ("flext_meltano", "e"),
    "h": ("flext_meltano", "h"),
    "m": ("flext_target_oracle_wms.models", "FlextTargetOracleWmsModels"),
    "main": ("flext_target_oracle_wms.cli", "main"),
    "p": ("flext_target_oracle_wms.protocols", "FlextTargetOracleWmsProtocols"),
    "r": ("flext_meltano", "r"),
    "s": ("flext_meltano", "s"),
    "t": ("flext_target_oracle_wms.typings", "FlextTargetOracleWmsTypes"),
    "u": ("flext_target_oracle_wms.utilities", "FlextTargetOracleWmsUtilities"),
    "x": ("flext_meltano", "x"),
}

__all__ = [
    "MIN_CONFIG_ARG_COUNT",
    "FlextTargetFactory",
    "FlextTargetMonitoringFactory",
    "FlextTargetOracleWmsConstants",
    "FlextTargetOracleWmsModels",
    "FlextTargetOracleWmsProtocols",
    "FlextTargetOracleWmsSettings",
    "FlextTargetOracleWmsTypes",
    "FlextTargetOracleWmsUtilities",
    "OracleWMSTargetCli",
    "SingerTargetOracleWMS",
    "SingerWMSCatalogManager",
    "SingerWMSStreamProcessor",
    "__all__",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "create_monitored_oracle_wms_target",
    "create_oracle_wms_target",
    "d",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]


_LAZY_CACHE: dict[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
