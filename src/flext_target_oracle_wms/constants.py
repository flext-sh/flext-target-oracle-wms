"""Constants for the target Oracle WMS package."""

from __future__ import annotations

from enum import StrEnum
from typing import Final

from flext_core import FlextConstants


class FlextTargetOracleWmsConstants(FlextConstants):
    """Typed constant namespace used by target Oracle WMS modules."""

    class TargetOracleWms:
        """Target-specific defaults and limits."""

        class OracleWms:
            """Oracle WMS runtime defaults."""

            DEFAULT_TIMEOUT: Final[int] = 30
            DEFAULT_MAX_RETRIES: Final[int] = 3
            DEFAULT_BATCH_SIZE: Final[int] = 1000
            DEFAULT_CONNECTION_POOL_SIZE: Final[int] = 5
            DEFAULT_CONNECTION_POOL_MAX: Final[int] = 20
            MIN_LOCATION_PARTS: Final[int] = 2
            PROCESSING_TIME_TOLERANCE: Final[float] = 0.1

        class LoadMethods:
            """Allowed load methods."""

            APPEND_ONLY: Final[str] = "APPEND_ONLY"
            UPSERT: Final[str] = "UPSERT"
            REPLACE: Final[str] = "REPLACE"
            MERGE: Final[str] = "MERGE"
            TRUNCATE_INSERT: Final[str] = "TRUNCATE_INSERT"
            VALID_LOAD_METHODS: Final[set[str]] = {
                APPEND_ONLY,
                UPSERT,
                REPLACE,
                MERGE,
                TRUNCATE_INSERT,
            }

    class ErrorType(StrEnum):
        """Project error categories."""

        WMS_CONNECTION = "WMS_CONNECTION"
        WMS_AUTHENTICATION = "WMS_AUTHENTICATION"
        WMS_BUSINESS_RULE = "WMS_BUSINESS_RULE"
        WMS_VALIDATION = "WMS_VALIDATION"
        SINGER_PROTOCOL = "SINGER_PROTOCOL"
        DATA_TRANSFORMATION = "DATA_TRANSFORMATION"
        PERFORMANCE = "PERFORMANCE"
        CONFIGURATION = "CONFIGURATION"


c = FlextTargetOracleWmsConstants

__all__ = ["FlextTargetOracleWmsConstants", "c"]
