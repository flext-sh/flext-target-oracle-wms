# AUTO-GENERATED FILE — Regenerate with: make gen
"""Utilities package."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".client": (
            "CatalogManager",
            "StreamProcessor",
            "Target",
        ),
        ".helpers": (
            "Validation",
            "WMSDataTransformer",
            "WMSSchemaMapper",
            "WMSTableManager",
            "WMSTypeConverter",
            "create_record_message",
            "create_schema_message",
            "create_state_message",
        ),
        ".service_runtime": ("FlextTargetOracleWmsServiceRuntime",),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
