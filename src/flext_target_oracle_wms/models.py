"""Domain models for target Oracle WMS.

Inherits from the canonical Meltano models facade and m.
Defines local TargetOracleWms namespace for target-specific models.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_target_oracle_wms/models
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import MutableMapping
from typing import Annotated, Literal

from flext_meltano import FlextMeltanoModels
from flext_oracle_wms import FlextOracleWmsModels

from flext_target_oracle_wms import c, t, u

# NOTE (multi-agent, bead mro-nwc.19): t / MutableMapping MUST stay RUNTIME imports.
# `from __future__ import annotations` makes pydantic v2 resolve these field annotation
# types lazily at model-build time; hiding them under TYPE_CHECKING left WmsTargetConfig /
# SingerSchemaProperties "not fully defined". Do NOT move them under TYPE_CHECKING.


class FlextTargetOracleWmsModels(FlextMeltanoModels, FlextOracleWmsModels):
    """Pydantic model namespace for target Oracle WMS.

    Inherited namespaces:
        m.Meltano.*    — Singer message types (overridden with Container support)
        m.OracleWms.*  — WMS entity/API types (from m)

    Local namespace:
        m.TargetOracleWms.* — target-specific settings and schema helpers
    """

    class TargetOracleWms:
        """Target Oracle WMS model namespace — m.TargetOracleWms.*."""

        class WmsAuthenticationConfig(FlextMeltanoModels.ArbitraryTypesModel):
            """Authentication and endpoint settings."""

            base_url: Annotated[
                str,
                u.Field(description="Oracle WMS REST API base URL."),
            ]
            auth_method: Annotated[
                Literal["oauth2", "basic", "api_key"],
                u.Field(description="WMS authentication method."),
            ] = "oauth2"
            username: Annotated[
                str | None,
                u.Field(description="Optional authentication username."),
            ] = None
            password: Annotated[
                t.SecretStr | None,
                u.Field(description="Optional authentication password."),
            ] = None
            api_key: Annotated[
                t.SecretStr | None,
                u.Field(description="Optional API key for the selected auth method."),
            ] = None
            company_code: Annotated[str, u.Field(description="WMS company code.")] = (
                "DEFAULT"
            )
            facility_code: Annotated[str, u.Field(description="WMS facility code.")] = (
                "MAIN"
            )

        class WmsTargetConfig(FlextMeltanoModels.ArbitraryTypesModel):
            """Top-level target configuration model."""

            wms_auth: Annotated[
                FlextTargetOracleWmsModels.TargetOracleWms.WmsAuthenticationConfig,
                u.Field(description="WMS authentication and endpoint settings."),
            ]
            stream_maps: Annotated[
                MutableMapping[str, t.StrMapping],
                u.Field(
                    default_factory=dict,
                    description="Singer stream map configurations.",
                ),
            ]
            batch_size: Annotated[
                t.BatchSize,
                u.Field(description="Number of records per batch write."),
            ] = c.TargetOracleWms.OracleWms.DEFAULT_BATCH_SIZE
            load_method: Annotated[
                c.TargetOracleWms.LoadMethods.Method,
                u.Field(description="Load strategy for writing records to WMS."),
            ] = c.TargetOracleWms.LoadMethods.Method.APPEND_ONLY
            validate_records: Annotated[
                bool,
                u.Field(description="Whether to validate records before writing."),
            ] = True

        class SingerFieldSchema(FlextMeltanoModels.FlexibleModel):
            """Typed Singer field schema entry for target-side schema parsing."""

            type: Annotated[
                str,
                u.Field(description="JSON schema type descriptor for the field."),
            ] = "string"

        class SingerSchemaProperties(FlextMeltanoModels.FlexibleModel):
            """Typed Singer schema properties block for target-side schema parsing."""

            properties: Annotated[
                MutableMapping[
                    str,
                    FlextTargetOracleWmsModels.TargetOracleWms.SingerFieldSchema,
                ],
                u.Field(
                    default_factory=dict,
                    description="Singer schema field property definitions.",
                ),
            ]


m = FlextTargetOracleWmsModels

__all__: list[str] = ["FlextTargetOracleWmsModels", "m"]
