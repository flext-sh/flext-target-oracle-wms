"""FlextTargetOracleWmsSettings - Configuration for flext-target-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from pydantic_settings import SettingsConfigDict

from flext_core import FlextSettings


@FlextSettings.auto_register("target-oracle-wms")
class FlextTargetOracleWmsSettings(FlextSettings):
    """Runtime configuration for target Oracle WMS."""

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_prefix="FLEXT_TARGET_ORACLE_WMS_",
        extra="ignore",
    )


__all__ = ["FlextTargetOracleWmsSettings"]
