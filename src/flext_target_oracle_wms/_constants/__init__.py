# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Target Oracle Wms. Constants package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from .base import FlextTargetOracleWmsConstantsBase
    from .values import FlextTargetOracleWmsConstantsValues
__all__: tuple[str, ...] = (
    "FlextTargetOracleWmsConstantsBase", "FlextTargetOracleWmsConstantsValues",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("FlextTargetOracleWmsConstantsBase",),
            ".values": ("FlextTargetOracleWmsConstantsValues",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
