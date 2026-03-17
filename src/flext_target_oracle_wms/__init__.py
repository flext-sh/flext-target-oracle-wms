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
    from flext_core.typings import FlextTypes

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
    from flext_target_oracle_wms.constants import FlextTargetOracleWmsConstants, c
    from flext_target_oracle_wms.factory import (
        FlextTargetFactory,
        FlextTargetMonitoringFactory,
        MonitoredTargetCreationRequest,
        TargetCreationRequest,
        create_monitored_oracle_wms_target,
        create_oracle_wms_target,
    )
    from flext_target_oracle_wms.models import FlextTargetOracleWmsModels, m
    from flext_target_oracle_wms.protocols import FlextTargetOracleWmsProtocols, p
    from flext_target_oracle_wms.target_client import (
        SingerTargetOracleWMS,
        SingerWMSCatalogManager,
        SingerWMSStreamProcessor,
    )
    from flext_target_oracle_wms.target_config import (
        FlextTargetOracleWmsSettings,
        create_settings,
    )
    from flext_target_oracle_wms.target_models import (
        WMSDataTransformer,
        WMSSchemaMapper,
        WMSTableManager,
        WMSTypeConverter,
    )
    from flext_target_oracle_wms.typings import FlextTargetOracleWmsTypes, t
    from flext_target_oracle_wms.utilities import FlextTargetOracleWmsUtilities, u

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextTargetFactory": ("flext_target_oracle_wms.factory", "FlextTargetFactory"),
    "FlextTargetMonitoringFactory": ("flext_target_oracle_wms.factory", "FlextTargetMonitoringFactory"),
    "FlextTargetOracleWmsConstants": ("flext_target_oracle_wms.constants", "FlextTargetOracleWmsConstants"),
    "FlextTargetOracleWmsModels": ("flext_target_oracle_wms.models", "FlextTargetOracleWmsModels"),
    "FlextTargetOracleWmsProtocols": ("flext_target_oracle_wms.protocols", "FlextTargetOracleWmsProtocols"),
    "FlextTargetOracleWmsSettings": ("flext_target_oracle_wms.target_config", "FlextTargetOracleWmsSettings"),
    "FlextTargetOracleWmsTypes": ("flext_target_oracle_wms.typings", "FlextTargetOracleWmsTypes"),
    "FlextTargetOracleWmsUtilities": ("flext_target_oracle_wms.utilities", "FlextTargetOracleWmsUtilities"),
    "MIN_CONFIG_ARG_COUNT": ("flext_target_oracle_wms.cli", "MIN_CONFIG_ARG_COUNT"),
    "MonitoredTargetCreationRequest": ("flext_target_oracle_wms.factory", "MonitoredTargetCreationRequest"),
    "OracleWMSTargetCli": ("flext_target_oracle_wms.cli", "OracleWMSTargetCli"),
    "SingerTargetOracleWMS": ("flext_target_oracle_wms.target_client", "SingerTargetOracleWMS"),
    "SingerWMSCatalogManager": ("flext_target_oracle_wms.target_client", "SingerWMSCatalogManager"),
    "SingerWMSStreamProcessor": ("flext_target_oracle_wms.target_client", "SingerWMSStreamProcessor"),
    "TargetCreationRequest": ("flext_target_oracle_wms.factory", "TargetCreationRequest"),
    "WMSDataTransformer": ("flext_target_oracle_wms.target_models", "WMSDataTransformer"),
    "WMSSchemaMapper": ("flext_target_oracle_wms.target_models", "WMSSchemaMapper"),
    "WMSTableManager": ("flext_target_oracle_wms.target_models", "WMSTableManager"),
    "WMSTypeConverter": ("flext_target_oracle_wms.target_models", "WMSTypeConverter"),
    "__all__": ("flext_target_oracle_wms.__version__", "__all__"),
    "__author__": ("flext_target_oracle_wms.__version__", "__author__"),
    "__author_email__": ("flext_target_oracle_wms.__version__", "__author_email__"),
    "__description__": ("flext_target_oracle_wms.__version__", "__description__"),
    "__license__": ("flext_target_oracle_wms.__version__", "__license__"),
    "__title__": ("flext_target_oracle_wms.__version__", "__title__"),
    "__url__": ("flext_target_oracle_wms.__version__", "__url__"),
    "__version__": ("flext_target_oracle_wms.__version__", "__version__"),
    "__version_info__": ("flext_target_oracle_wms.__version__", "__version_info__"),
    "c": ("flext_target_oracle_wms.constants", "c"),
    "create_monitored_oracle_wms_target": ("flext_target_oracle_wms.factory", "create_monitored_oracle_wms_target"),
    "create_oracle_wms_target": ("flext_target_oracle_wms.factory", "create_oracle_wms_target"),
    "create_settings": ("flext_target_oracle_wms.target_config", "create_settings"),
    "m": ("flext_target_oracle_wms.models", "m"),
    "main": ("flext_target_oracle_wms.cli", "main"),
    "p": ("flext_target_oracle_wms.protocols", "p"),
    "t": ("flext_target_oracle_wms.typings", "t"),
    "u": ("flext_target_oracle_wms.utilities", "u"),
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
    "MonitoredTargetCreationRequest",
    "OracleWMSTargetCli",
    "SingerTargetOracleWMS",
    "SingerWMSCatalogManager",
    "SingerWMSStreamProcessor",
    "TargetCreationRequest",
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
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
    "create_settings",
    "m",
    "main",
    "p",
    "t",
    "u",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
