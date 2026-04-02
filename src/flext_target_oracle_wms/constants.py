"""Constants for the target Oracle WMS package."""

from __future__ import annotations

from typing import Final

from flext_meltano import FlextMeltanoConstants
from flext_oracle_wms import FlextOracleWmsConstants


class FlextTargetOracleWmsConstants(FlextMeltanoConstants, FlextOracleWmsConstants):
    """Typed constant namespace used by target Oracle WMS modules."""

    class TargetOracleWms:
        """Target-specific defaults and limits."""

        CLI_MIN_CONFIG_ARG_COUNT: Final[int] = 3

        class OracleWms:
            """Oracle WMS runtime defaults."""

            DEFAULT_TIMEOUT: Final[int] = FlextMeltanoConstants.DEFAULT_TIMEOUT_SECONDS
            DEFAULT_MAX_RETRIES: Final[int] = (
                FlextMeltanoConstants.DEFAULT_MAX_RETRY_ATTEMPTS
            )
            DEFAULT_BATCH_SIZE: Final[int] = FlextMeltanoConstants.DEFAULT_BATCH_SIZE

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


c = FlextTargetOracleWmsConstants
__all__ = ["FlextTargetOracleWmsConstants", "c"]
