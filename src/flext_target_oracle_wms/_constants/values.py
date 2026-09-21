"""Scalar constants for flext-target-oracle-wms.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from enum import StrEnum, unique
from typing import Final

from flext_meltano import FlextMeltanoConstants as meltano_c


class FlextTargetOracleWmsConstantsValues:
    """Scalar constants mixed into ``c.TargetOracleWms``."""

    class TargetOracleWms:
        """Target-specific scalar constants."""

        CLI_MIN_CONFIG_ARG_COUNT: Final[int] = 3
        CLI_PLACEHOLDER_BASE_URL: Final[str] = "https://invalid.wms.ocs.oraclecloud.com"

        class OracleWms:
            """Oracle WMS runtime scalar defaults."""

            DEFAULT_TIMEOUT: Final[int] = meltano_c.Meltano.DEFAULT_TIMEOUT_SECONDS
            DEFAULT_MAX_RETRIES: Final[int] = 3

        class LoadMethods:
            """Allowed load methods."""

            @unique
            class Method(StrEnum):
                """Allowed target load methods."""

                APPEND_ONLY = "APPEND_ONLY"
                UPSERT = "UPSERT"
                REPLACE = "REPLACE"
                MERGE = "MERGE"

            VALID_LOAD_METHODS: Final[frozenset[str]] = frozenset(
                member.value for member in Method
            )


__all__: list[str] = ["FlextTargetOracleWmsConstantsValues"]
