# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_target_oracle_wms/_protocols/auth
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols

if TYPE_CHECKING:
    from flext_target_oracle_wms import t


class FlextTargetOracleWmsProtocolsAuth:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class WmsAuthenticationConfig(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        base_url: str
        auth_method: Literal["oauth2", "basic", "api_key"]
        username: str | None
        password: t.SecretStr | None
        api_key: t.SecretStr | None
        company_code: str
        facility_code: str


__all__: list[str] = [
    "FlextTargetOracleWmsProtocolsAuth",
]
