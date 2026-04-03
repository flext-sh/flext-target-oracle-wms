# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Utilities package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_target_oracle_wms import client, helpers, service_runtime
    from flext_target_oracle_wms.client import (
        CatalogManager,
        StreamProcessor,
        Target,
        logger,
    )
    from flext_target_oracle_wms.helpers import (
        Validation,
        WMSDataTransformer,
        WMSSchemaMapper,
        WMSTableManager,
        WMSTypeConverter,
        create_record_message,
        create_schema_message,
        create_state_message,
    )
    from flext_target_oracle_wms.service_runtime import (
        FlextTargetOracleWmsServiceRuntime,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "CatalogManager": "flext_target_oracle_wms.client",
    "FlextTargetOracleWmsServiceRuntime": "flext_target_oracle_wms.service_runtime",
    "StreamProcessor": "flext_target_oracle_wms.client",
    "Target": "flext_target_oracle_wms.client",
    "Validation": "flext_target_oracle_wms.helpers",
    "WMSDataTransformer": "flext_target_oracle_wms.helpers",
    "WMSSchemaMapper": "flext_target_oracle_wms.helpers",
    "WMSTableManager": "flext_target_oracle_wms.helpers",
    "WMSTypeConverter": "flext_target_oracle_wms.helpers",
    "client": "flext_target_oracle_wms.client",
    "create_record_message": "flext_target_oracle_wms.helpers",
    "create_schema_message": "flext_target_oracle_wms.helpers",
    "create_state_message": "flext_target_oracle_wms.helpers",
    "helpers": "flext_target_oracle_wms.helpers",
    "logger": "flext_target_oracle_wms.client",
    "service_runtime": "flext_target_oracle_wms.service_runtime",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
