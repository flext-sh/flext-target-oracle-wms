"""Target Oracle WMS target configuration models.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping
from typing import Annotated

from flext_meltano import m

from flext_target_oracle_wms import c, t
from flext_target_oracle_wms._models import (
    FlextTargetOracleWmsModelsAuth,
    FlextTargetOracleWmsModelsSinger,
)


class FlextTargetOracleWmsModelsTarget:
    """Target-specific WMS configuration models composed into ``m.TargetOracleWms``."""

    class WmsTargetConfig(m.ArbitraryTypesModel):
        """Top-level target configuration model."""

        wms_auth: Annotated[
            FlextTargetOracleWmsModelsAuth.WmsAuthenticationConfig,
            m.Field(description="WMS authentication and endpoint settings."),
        ]
        stream_maps: Annotated[
            MutableMapping[str, Mapping[str, str]],
            m.Field(
                default_factory=dict,
                description="Singer stream map configurations.",
            ),
        ]
        batch_size: Annotated[
            t.BatchSize,
            m.Field(description="Number of records per batch write."),
        ] = c.TargetOracleWms.OracleWms.DEFAULT_BATCH_SIZE
        load_method: Annotated[
            c.TargetOracleWms.LoadMethods.Method,
            m.Field(description="Load strategy for writing records to WMS."),
        ] = c.TargetOracleWms.LoadMethods.Method.APPEND_ONLY
        validate_records: Annotated[
            bool,
            m.Field(description="Whether to validate records before writing."),
        ] = True

    class SingerSchemaProperties(m.FlexibleModel):
        """Typed Singer schema properties block for target-side schema parsing."""

        properties: Annotated[
            MutableMapping[
                str,
                FlextTargetOracleWmsModelsSinger.SingerFieldSchema,
            ],
            m.Field(
                default_factory=dict,
                description="Singer schema field property definitions.",
            ),
        ]


__all__: list[str] = ["FlextTargetOracleWmsModelsTarget"]
