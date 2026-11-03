# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_target_oracle_wms/_protocols/auth
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Literal, Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols

from flext_target_oracle_wms import t


class FlextTargetOracleWmsProtocolsAuth:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class WmsAuthenticationConfig(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def base_url(self) -> str:
            """Oracle WMS REST API base URL."""
            ...

        @property
        def auth_method(self) -> Literal["oauth2", "basic", "api_key"]:
            """WMS authentication method."""
            ...

        @property
        def username(self) -> str | None:
            """Optional authentication username."""
            ...

        @property
        def password(self) -> t.SecretStr | None:
            """Optional authentication password."""
            ...

        @property
        def api_key(self) -> t.SecretStr | None:
            """Optional API key for the selected auth method."""
            ...

        @property
        def company_code(self) -> str:
            """WMS company code."""
            ...

        @property
        def facility_code(self) -> str:
            """WMS facility code."""
            ...


__all__: list[str] = [
    "FlextTargetOracleWmsProtocolsAuth",
]
