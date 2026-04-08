# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Utilities package."""

from __future__ import annotations

from flext_core.lazy import install_lazy_exports

_LAZY_IMPORTS = {
    "CatalogManager": ("flext_target_oracle_wms._utilities.client", "CatalogManager"),
    "FlextTargetOracleWmsServiceRuntime": (
        "flext_target_oracle_wms._utilities.service_runtime",
        "FlextTargetOracleWmsServiceRuntime",
    ),
    "StreamProcessor": ("flext_target_oracle_wms._utilities.client", "StreamProcessor"),
    "Target": ("flext_target_oracle_wms._utilities.client", "Target"),
    "Validation": ("flext_target_oracle_wms._utilities.helpers", "Validation"),
    "WMSDataTransformer": (
        "flext_target_oracle_wms._utilities.helpers",
        "WMSDataTransformer",
    ),
    "WMSSchemaMapper": (
        "flext_target_oracle_wms._utilities.helpers",
        "WMSSchemaMapper",
    ),
    "WMSTableManager": (
        "flext_target_oracle_wms._utilities.helpers",
        "WMSTableManager",
    ),
    "WMSTypeConverter": (
        "flext_target_oracle_wms._utilities.helpers",
        "WMSTypeConverter",
    ),
    "create_record_message": (
        "flext_target_oracle_wms._utilities.helpers",
        "create_record_message",
    ),
    "create_schema_message": (
        "flext_target_oracle_wms._utilities.helpers",
        "create_schema_message",
    ),
    "create_state_message": (
        "flext_target_oracle_wms._utilities.helpers",
        "create_state_message",
    ),
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
