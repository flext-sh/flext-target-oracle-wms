"""Settings for flext-target-oracle-wms — layer-0 strict.

Imports only stdlib + pydantic-settings + the tier base (``FlextMeltanoSettings``).
All runtime fields are inherited from the base by MRO; this class only scopes the
env prefix. No ``c/t/p/m/u/r`` imports, no project imports, no accessor/factory
methods — construction goes through ``fetch_global`` / ``model_validate``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pydantic_settings import SettingsConfigDict

from flext_meltano import FlextMeltanoSettings


class FlextTargetOracleWmsSettings(FlextMeltanoSettings):
    """Runtime configuration for target Oracle WMS (fields inherited from base)."""

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_TARGET_ORACLE_WMS_",
        extra="ignore",
    )


settings: FlextTargetOracleWmsSettings = FlextTargetOracleWmsSettings.fetch_global()
"""Pre-instantiated project settings singleton — ``from flext_target_oracle_wms import settings``."""

__all__: list[str] = ["FlextTargetOracleWmsSettings", "settings"]
