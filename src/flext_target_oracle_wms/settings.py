"""FlextTargetOracleWmsSettings - Configuration for flext-target-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_core import FlextSettingsBase, r
from flext_target_oracle_wms import c, m, p, t


class FlextTargetOracleWmsSettings(FlextSettingsBase):
    """Runtime configuration for target Oracle WMS."""

    model_config: ClassVar[m.SettingsConfigDict] = m.SettingsConfigDict(
        env_prefix="FLEXT_TARGET_ORACLE_WMS_", extra="ignore"
    )

    @classmethod
    def create_settings(
        cls,
        overrides: t.JsonMapping | None = None,
    ) -> p.Result[FlextTargetOracleWmsSettings]:
        """Create settings instance with optional override values."""
        try:
            settings = FlextTargetOracleWmsSettings.model_validate(overrides or {})
        except c.Meltano.SINGER_SAFE_EXCEPTIONS as exc:
            return r[FlextTargetOracleWmsSettings].fail(
                f"Invalid settings overrides: {exc}",
            )
        return r[FlextTargetOracleWmsSettings].ok(settings)


__all__: list[str] = ["FlextTargetOracleWmsSettings"]
