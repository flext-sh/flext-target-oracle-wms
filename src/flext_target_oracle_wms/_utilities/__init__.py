# AUTO-GENERATED FILE — Regenerate with: make gen
"""Utilities package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_target_oracle_wms._utilities.client import (
        FlextTargetOracleWmsUtilitiesClient as FlextTargetOracleWmsUtilitiesClient,
    )
    from flext_target_oracle_wms._utilities.helpers import (
        FlextTargetOracleWmsUtilitiesHelpers as FlextTargetOracleWmsUtilitiesHelpers,
    )
    from flext_target_oracle_wms._utilities.service_runtime import (
        FlextTargetOracleWmsServiceRuntime as FlextTargetOracleWmsServiceRuntime,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".client": ("FlextTargetOracleWmsUtilitiesClient",),
        ".helpers": ("FlextTargetOracleWmsUtilitiesHelpers",),
        ".service_runtime": ("FlextTargetOracleWmsServiceRuntime",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
