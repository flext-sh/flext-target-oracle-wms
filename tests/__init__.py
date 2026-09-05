# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from . import examples as examples
    from . import integration as integration
    from . import unit as unit
    from flext_tests import FlextTestsConstants, d, e, h, r, td, tf, tk, tm, tv, x
    from typing import Final

    from .base import (
        TestsFlextTargetOracleWmsServiceBase,
        TestsFlextTargetOracleWmsServiceBase as s,
    )
    from .constants import (
        TestsFlextTargetOracleWmsConstants,
        TestsFlextTargetOracleWmsConstants as c,
    )
    from .models import (
        TestsFlextTargetOracleWmsModels,
        TestsFlextTargetOracleWmsModels as m,
    )
    from .protocols import (
        TestsFlextTargetOracleWmsProtocols,
        TestsFlextTargetOracleWmsProtocols as p,
    )
    from .settings import TestsFlextTargetOracleWmsSettings
    from .typings import (
        TestsFlextTargetOracleWmsTypes,
        TestsFlextTargetOracleWmsTypes as t,
    )
    from .utilities import (
        TestsFlextTargetOracleWmsUtilities,
        TestsFlextTargetOracleWmsUtilities as u,
    )
__all__: tuple[str, ...] = (
    "Final",
    "FlextTestsConstants",
    "TestsFlextTargetOracleWmsConstants",
    "TestsFlextTargetOracleWmsModels",
    "TestsFlextTargetOracleWmsProtocols",
    "TestsFlextTargetOracleWmsServiceBase",
    "TestsFlextTargetOracleWmsSettings",
    "TestsFlextTargetOracleWmsTypes",
    "TestsFlextTargetOracleWmsUtilities",
    "c",
    "d",
    "e",
    "examples",
    "h",
    "integration",
    "m",
    "p",
    "r",
    "s",
    "t",
    "td",
    "tf",
    "tk",
    "tm",
    "tv",
    "u",
    "unit",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("TestsFlextTargetOracleWmsServiceBase", "s"),
            ".constants": ("TestsFlextTargetOracleWmsConstants", "c"),
            ".examples": ("examples",),
            ".integration": ("integration",),
            ".models": ("TestsFlextTargetOracleWmsModels", "m"),
            ".protocols": ("TestsFlextTargetOracleWmsProtocols", "p"),
            ".settings": ("TestsFlextTargetOracleWmsSettings",),
            ".typings": ("TestsFlextTargetOracleWmsTypes", "t"),
            ".unit": ("unit",),
            ".utilities": ("TestsFlextTargetOracleWmsUtilities", "u"),
            "flext_tests": (
                "FlextTestsConstants",
                "d",
                "e",
                "h",
                "r",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "x",
            ),
            "typing": ("Final",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
