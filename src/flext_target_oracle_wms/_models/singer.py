"""Target Oracle WMS Singer schema field models.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated

from flext_meltano import m


class FlextTargetOracleWmsModelsSinger:
    """Singer schema field models composed into ``m.TargetOracleWms``."""

    class SingerFieldSchema(m.FlexibleModel):
        """Typed Singer field schema entry for target-side schema parsing."""

        type: Annotated[
            str,
            m.Field(description="JSON schema type descriptor for the field."),
        ] = "string"


__all__: list[str] = ["FlextTargetOracleWmsModelsSinger"]
