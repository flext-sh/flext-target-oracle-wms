"""Scalar constants for flext-target-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from enum import StrEnum, unique
from typing import ClassVar

from flext_meltano import FlextMeltanoConstants


class FlextTargetOracleWmsConstantsValues:
    """Scalar constants mixed into ``c.TargetOracleWms``."""

    TARGET_NAME: ClassVar[str] = "target-oracle-wms"
    CLI_MIN_CONFIG_ARG_COUNT: ClassVar[int] = 3
    CLI_PLACEHOLDER_BASE_URL: ClassVar[str] = "https://invalid.wms.ocs.oraclecloud.com"

    class OracleWms:
        """Oracle WMS runtime scalar defaults."""

        DEFAULT_BATCH_SIZE: ClassVar[int] = (
            FlextMeltanoConstants.Meltano.BATCH_DEFAULT_DEFAULT_BATCH_SIZE
        )

    class LoadMethods:
        """Allowed load methods."""

        @unique
        class Method(StrEnum):
            """Allowed target load methods."""

            APPEND_ONLY = "APPEND_ONLY"
            UPSERT = "UPSERT"
            REPLACE = "REPLACE"
            MERGE = "MERGE"


__all__: list[str] = ["FlextTargetOracleWmsConstantsValues"]
