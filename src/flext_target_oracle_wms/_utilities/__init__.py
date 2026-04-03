# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Utilities package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import flext_target_oracle_wms._utilities.client as _flext_target_oracle_wms__utilities_client

    client = _flext_target_oracle_wms__utilities_client
    import flext_target_oracle_wms._utilities.helpers as _flext_target_oracle_wms__utilities_helpers
    from flext_target_oracle_wms._utilities.client import (
        CatalogManager,
        StreamProcessor,
        Target,
    )

    helpers = _flext_target_oracle_wms__utilities_helpers
    import flext_target_oracle_wms._utilities.service_runtime as _flext_target_oracle_wms__utilities_service_runtime
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

    service_runtime = _flext_target_oracle_wms__utilities_service_runtime
    from flext_target_oracle_wms._utilities.service_runtime import (
        FlextTargetOracleWmsServiceRuntime,
    )
_LAZY_IMPORTS = {
    "CatalogManager": "flext_target_oracle_wms._utilities.client",
    "FlextTargetOracleWmsServiceRuntime": "flext_target_oracle_wms._utilities.service_runtime",
    "StreamProcessor": "flext_target_oracle_wms._utilities.client",
    "Target": "flext_target_oracle_wms._utilities.client",
    "Validation": "flext_target_oracle_wms._utilities.helpers",
    "WMSDataTransformer": "flext_target_oracle_wms._utilities.helpers",
    "WMSSchemaMapper": "flext_target_oracle_wms._utilities.helpers",
    "WMSTableManager": "flext_target_oracle_wms._utilities.helpers",
    "WMSTypeConverter": "flext_target_oracle_wms._utilities.helpers",
    "client": "flext_target_oracle_wms._utilities.client",
    "create_record_message": "flext_target_oracle_wms._utilities.helpers",
    "create_schema_message": "flext_target_oracle_wms._utilities.helpers",
    "create_state_message": "flext_target_oracle_wms._utilities.helpers",
    "helpers": "flext_target_oracle_wms._utilities.helpers",
    "service_runtime": "flext_target_oracle_wms._utilities.service_runtime",
}

__all__ = [
    "CatalogManager",
    "FlextTargetOracleWmsServiceRuntime",
    "StreamProcessor",
    "Target",
    "Validation",
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
    "client",
    "create_record_message",
    "create_schema_message",
    "create_state_message",
    "helpers",
    "service_runtime",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
