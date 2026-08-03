# @generated AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Wms. Utilities package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .client import (
        FlextTargetOracleWmsUtilitiesClient as FlextTargetOracleWmsUtilitiesClient,
    )
    from .helpers import (
        FlextTargetOracleWmsUtilitiesHelpers as FlextTargetOracleWmsUtilitiesHelpers,
    )
    from .service_runtime import (
        FlextTargetOracleWmsServiceRuntime as FlextTargetOracleWmsServiceRuntime,
    )

_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    ".client": ("FlextTargetOracleWmsUtilitiesClient",),
    ".helpers": ("FlextTargetOracleWmsUtilitiesHelpers",),
    ".service_runtime": ("FlextTargetOracleWmsServiceRuntime",),
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES, alias_groups=_LAZY_ALIAS_GROUPS, sort_keys=False
)

_PUBLIC_EXPORTS: tuple[str, ...] = (
    "FlextTargetOracleWmsServiceRuntime",
    "FlextTargetOracleWmsUtilitiesClient",
    "FlextTargetOracleWmsUtilitiesHelpers",
)

__all__: tuple[str, ...] = tuple(_PUBLIC_EXPORTS)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
