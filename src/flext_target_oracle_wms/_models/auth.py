"""Target Oracle WMS authentication models.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated, Literal

from flext_meltano import m

from flext_target_oracle_wms import t


class FlextTargetOracleWmsModelsAuth:
    """WMS authentication models composed into ``m.TargetOracleWms``."""

    class WmsAuthenticationConfig(m.ArbitraryTypesModel):
        """Authentication and endpoint settings."""

        base_url: Annotated[
            str,
            m.Field(description="Oracle WMS REST API base URL."),
        ]
        auth_method: Annotated[
            Literal["oauth2", "basic", "api_key"],
            m.Field(description="WMS authentication method."),
        ] = "oauth2"
        username: Annotated[
            str | None,
            m.Field(description="Optional authentication username."),
        ] = None
        password: Annotated[
            t.SecretStr | None,
            m.Field(description="Optional authentication password."),
        ] = None
        api_key: Annotated[
            t.SecretStr | None,
            m.Field(description="Optional API key for the selected auth method."),
        ] = None
        company_code: Annotated[str, m.Field(description="WMS company code.")] = (
            "DEFAULT"
        )
        facility_code: Annotated[str, m.Field(description="WMS facility code.")] = (
            "MAIN"
        )


__all__: list[str] = ["FlextTargetOracleWmsModelsAuth"]
