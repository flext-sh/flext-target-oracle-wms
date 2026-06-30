# AUTO-GENERATED FILE — Regenerate with: make gen
"""Lazy export map part."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map

FLEXT_TARGET_ORACLE_WMS_LAZY_IMPORTS_PART_01 = build_lazy_import_map(
    {
        "._utilities.client": ("FlextTargetOracleWmsUtilitiesClient",),
        "._utilities.helpers": ("FlextTargetOracleWmsUtilitiesHelpers",),
        "._utilities.service_runtime": ("FlextTargetOracleWmsServiceRuntime",),
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
    },
)

__all__: list[str] = ["FLEXT_TARGET_ORACLE_WMS_LAZY_IMPORTS_PART_01"]
