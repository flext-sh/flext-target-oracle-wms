# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Wms package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)
from flext_target_oracle_wms.__version__ import *

if _t.TYPE_CHECKING:
    from flext_oracle_wms import d, e, h, r, s, x
    from flext_target_oracle_wms._utilities.client import (
        CatalogManager,
        StreamProcessor,
        Target,
    )
    from flext_target_oracle_wms._utilities.helpers import (
        Validation,
        WMSDataTransformer,
        WMSSchemaMapper,
        WMSTableManager,
        WMSTypeConverter,
        create_record_message,
        create_schema_message,
        create_state_message,
    )
    from flext_target_oracle_wms._utilities.service_runtime import (
        FlextTargetOracleWmsServiceRuntime,
    )
    from flext_target_oracle_wms.api import (
        FlextTargetOracleWmsService,
        target_oracle_wms,
    )
    from flext_target_oracle_wms.cli import FlextTargetOracleWmsCli, main
    from flext_target_oracle_wms.constants import FlextTargetOracleWmsConstants, c
    from flext_target_oracle_wms.factory import (
        FlextTargetFactory,
        FlextTargetMonitoringFactory,
    )
    from flext_target_oracle_wms.models import FlextTargetOracleWmsModels, m
    from flext_target_oracle_wms.protocols import FlextTargetOracleWmsProtocols, p
    from flext_target_oracle_wms.settings import FlextTargetOracleWmsSettings
    from flext_target_oracle_wms.target_config import FlextTargetOracleWmsTargetConfig
    from flext_target_oracle_wms.typings import FlextTargetOracleWmsTypes, t
    from flext_target_oracle_wms.utilities import FlextTargetOracleWmsUtilities, u
_LAZY_IMPORTS = merge_lazy_imports(
    ("._utilities",),
    build_lazy_import_map(
        {
            ".__version__": (
                "__author__",
                "__author_email__",
                "__description__",
                "__license__",
                "__title__",
                "__url__",
                "__version__",
                "__version_info__",
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
            ".target_config": ("FlextTargetOracleWmsTargetConfig",),
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
    ),
    exclude_names=(
        "FlextDispatcher",
        "FlextLogger",
        "FlextRegistry",
        "FlextRuntime",
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
    ),
    module_name=__name__,
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "CatalogManager",
    "FlextTargetFactory",
    "FlextTargetMonitoringFactory",
    "FlextTargetOracleWmsCli",
    "FlextTargetOracleWmsConstants",
    "FlextTargetOracleWmsModels",
    "FlextTargetOracleWmsProtocols",
    "FlextTargetOracleWmsService",
    "FlextTargetOracleWmsServiceRuntime",
    "FlextTargetOracleWmsSettings",
    "FlextTargetOracleWmsTargetConfig",
    "FlextTargetOracleWmsTypes",
    "FlextTargetOracleWmsUtilities",
    "StreamProcessor",
    "Target",
    "Validation",
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "create_record_message",
    "create_schema_message",
    "create_state_message",
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
]
