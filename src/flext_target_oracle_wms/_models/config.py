"""Pure config namespace declarations for flext-target-oracle-wms.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_cli import m


class FlextTargetOracleWmsModelsConfig:
    """Field-only Pydantic declarations for the TargetOracleWms config singleton."""

    class TargetOracleWmsNamespace(m.BaseModel):
        """Open, frozen namespace exposing every ``config/*.yaml`` domain model-less."""

        model_config = m.ConfigDict(extra="allow", frozen=True)


__all__: tuple[str, ...] = ("FlextTargetOracleWmsModelsConfig",)
