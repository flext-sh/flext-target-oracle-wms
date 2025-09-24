"""FLEXT Target Oracle WMS Constants - Oracle WMS target loading constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

from flext_core import FlextConstants


class FlextTargetOracleWmsConstants(FlextConstants):
    """Oracle WMS target loading-specific constants following flext-core patterns."""

    # Oracle WMS Connection Configuration
    DEFAULT_WMS_TIMEOUT = 30
    DEFAULT_MAX_RETRIES = 3

    # Singer Target Configuration
    DEFAULT_BATCH_SIZE = 1000
    MAX_BATCH_SIZE = 10000

    # WMS Load Methods
    LOAD_METHODS: ClassVar[list[str]] = ["BULK_INSERT", "INCREMENTAL", "UPSERT"]


__all__ = ["FlextTargetOracleWmsConstants"]
