# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if _t.TYPE_CHECKING:
    from flext_tests import td, tf, tk, tm, tv

    from flext_target_oracle_wms import d, e, h, r, s, x
    from tests.constants import TestsFlextTargetOracleWmsConstants, c
    from tests.models import TestsFlextTargetOracleWmsModels, m
    from tests.protocols import TestsFlextTargetOracleWmsProtocols, p
    from tests.typings import TestsFlextTargetOracleWmsTypes, t
    from tests.utilities import TestsFlextTargetOracleWmsUtilities, u
_LAZY_IMPORTS = merge_lazy_imports(
    (
        ".examples",
        ".integration",
        ".unit",
    ),
    build_lazy_import_map(
        {
            ".constants": (
                "TestsFlextTargetOracleWmsConstants",
                "c",
            ),
            ".models": (
                "TestsFlextTargetOracleWmsModels",
                "m",
            ),
            ".protocols": (
                "TestsFlextTargetOracleWmsProtocols",
                "p",
            ),
            ".typings": (
                "TestsFlextTargetOracleWmsTypes",
                "t",
            ),
            ".utilities": (
                "TestsFlextTargetOracleWmsUtilities",
                "u",
            ),
            "flext_target_oracle_wms": (
                "d",
                "e",
                "h",
                "r",
                "s",
                "x",
            ),
            "flext_tests": (
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
            ),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
    ),
    module_name=__name__,
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__ = [
    "TestsFlextTargetOracleWmsConstants",
    "TestsFlextTargetOracleWmsModels",
    "TestsFlextTargetOracleWmsProtocols",
    "TestsFlextTargetOracleWmsTypes",
    "TestsFlextTargetOracleWmsUtilities",
    "c",
    "d",
    "e",
    "h",
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
    "x",
]
