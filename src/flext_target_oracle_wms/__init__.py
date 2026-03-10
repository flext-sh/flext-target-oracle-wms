"""Flext Target Oracle WMS - Oracle WMS Target Client for FLEXT ecosystem.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_target_oracle_wms.__version__ import __version__, __version_info__
    from flext_target_oracle_wms.cli import OracleWMSTargetCli, main
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
    from flext_target_oracle_wms.target_models import (
        WMSDataTransformer,
        WMSSchemaMapper,
        WMSTableManager,
        WMSTypeConverter,
    )
    from flext_target_oracle_wms.typings import (
        FlextTargetOracleWmsTypes,
        FlextTargetOracleWmsTypes as t,
    )
    from flext_target_oracle_wms.utilities import (
        FlextTargetOracleWmsUtilities,
        FlextTargetOracleWmsUtilities as u,
    )

# Lazy import mapping: export_name -> (module_path, attr_name)
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
    "FlextTargetOracleWmsTypes": (
        "flext_target_oracle_wms.typings",
        "FlextTargetOracleWmsTypes",
    ),
    "FlextTargetOracleWmsUtilities": (
        "flext_target_oracle_wms.utilities",
        "FlextTargetOracleWmsUtilities",
    ),
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
    "WMSDataTransformer": (
        "flext_target_oracle_wms.target_models",
        "WMSDataTransformer",
    ),
    "WMSSchemaMapper": ("flext_target_oracle_wms.target_models", "WMSSchemaMapper"),
    "WMSTableManager": ("flext_target_oracle_wms.target_models", "WMSTableManager"),
    "WMSTypeConverter": ("flext_target_oracle_wms.target_models", "WMSTypeConverter"),
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
    "m": ("flext_target_oracle_wms.models", "FlextTargetOracleWmsModels"),
    "main": ("flext_target_oracle_wms.cli", "main"),
    "p": ("flext_target_oracle_wms.protocols", "FlextTargetOracleWmsProtocols"),
    "t": ("flext_target_oracle_wms.typings", "FlextTargetOracleWmsTypes"),
    "u": ("flext_target_oracle_wms.utilities", "FlextTargetOracleWmsUtilities"),
}

__all__ = [
    "FlextTargetFactory",
    "FlextTargetMonitoringFactory",
    "FlextTargetOracleWmsConstants",
    "FlextTargetOracleWmsModels",
    "FlextTargetOracleWmsProtocols",
    "FlextTargetOracleWmsTypes",
    "FlextTargetOracleWmsUtilities",
    "OracleWMSTargetCli",
    "SingerTargetOracleWMS",
    "SingerWMSCatalogManager",
    "SingerWMSStreamProcessor",
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
    "__version__",
    "__version_info__",
    "c",
    "create_monitored_oracle_wms_target",
    "create_oracle_wms_target",
    "m",
    "main",
    "p",
    "t",
    "u",
]


def __getattr__(
    name: str,
) -> Any:  # JUSTIFIED: Ruff (any-type) with PEP 562 dynamic module exports — https://docs.astral.sh/ruff/rules/any-type/
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
