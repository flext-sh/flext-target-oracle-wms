# AUTO-GENERATED FILE — Regenerate with: make gen
"""Examples package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_meltano import s
    from flext_oracle_wms import e

    from examples.constants import ExamplesFlextTargetOracleWmsConstants
    from examples.models import ExamplesFlextTargetOracleWmsModels
    from examples.protocols import ExamplesFlextTargetOracleWmsProtocols
    from examples.typings import ExamplesFlextTargetOracleWmsTypes
    from examples.utilities import ExamplesFlextTargetOracleWmsUtilities
    from flext_target_oracle_wms import c, d, h, m, p, r, t, u, x


__all__: tuple[str, ...] = (
    "ExamplesFlextTargetOracleWmsConstants",
    "ExamplesFlextTargetOracleWmsModels",
    "ExamplesFlextTargetOracleWmsProtocols",
    "ExamplesFlextTargetOracleWmsTypes",
    "ExamplesFlextTargetOracleWmsUtilities",
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "ExamplesFlextTargetOracleWmsConstants": ".constants",
        "ExamplesFlextTargetOracleWmsModels": ".models",
        "ExamplesFlextTargetOracleWmsProtocols": ".protocols",
        "ExamplesFlextTargetOracleWmsTypes": ".typings",
        "ExamplesFlextTargetOracleWmsUtilities": ".utilities",
        "c": "flext_target_oracle_wms",
        "d": "flext_target_oracle_wms",
        "e": "flext_oracle_wms",
        "h": "flext_target_oracle_wms",
        "m": "flext_target_oracle_wms",
        "p": "flext_target_oracle_wms",
        "r": "flext_target_oracle_wms",
        "s": "flext_meltano",
        "t": "flext_target_oracle_wms",
        "u": "flext_target_oracle_wms",
        "x": "flext_target_oracle_wms",
    }),
    public_exports=__all__,
)
