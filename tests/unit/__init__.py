# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests.unit package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from tests.unit.test_module_governance import (
        TestsFlextTargetOracleWmsModuleGovernance,
    )


__all__: tuple[str, ...] = ("TestsFlextTargetOracleWmsModuleGovernance",)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "TestsFlextTargetOracleWmsModuleGovernance": ".test_module_governance",
    }),
    public_exports=__all__,
)
