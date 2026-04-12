"""FlextTargetOracleWmsSettings - Configuration for flext-target-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from pydantic_settings import SettingsConfigDict

from flext_core import FlextSettings
from flext_target_oracle_wms import c, r, t


@FlextSettings.auto_register("target-oracle-wms")
class FlextTargetOracleWmsSettings(FlextSettings):
    """Runtime configuration for target Oracle WMS."""

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_prefix="FLEXT_TARGET_ORACLE_WMS_", extra="ignore"
    )

    @classmethod
    def create_settings(
        cls,
        overrides: t.ContainerValueMapping | None = None,
    ) -> r[FlextTargetOracleWmsSettings]:
        """Create settings instance with optional override values."""
        try:
            data: t.ContainerValueMapping = dict(overrides) if overrides else {}
            settings = FlextTargetOracleWmsSettings.model_validate(data)
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as exc:
            return r[FlextTargetOracleWmsSettings].fail(
                f"Invalid settings overrides: {exc}",
            )
        return r[FlextTargetOracleWmsSettings].ok(settings)


__all__ = ["FlextTargetOracleWmsSettings"]
