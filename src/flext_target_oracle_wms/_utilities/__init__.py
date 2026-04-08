# AUTO-GENERATED FILE — Regenerate with: make gen
from __future__ import annotations

from flext_core.lazy import install_lazy_exports

_LAZY_IMPORTS = {
    "CatalogManager": ".client",
    "FlextTargetOracleWmsServiceRuntime": ".service_runtime",
    "StreamProcessor": ".client",
    "Target": ".client",
    "Validation": ".helpers",
    "WMSDataTransformer": ".helpers",
    "WMSSchemaMapper": ".helpers",
    "WMSTableManager": ".helpers",
    "WMSTypeConverter": ".helpers",
    "create_record_message": ".helpers",
    "create_schema_message": ".helpers",
    "create_state_message": ".helpers",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
