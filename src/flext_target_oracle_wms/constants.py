"""Constants for the target Oracle WMS package."""

from __future__ import annotations

from enum import StrEnum, unique
from typing import Final

from flext_meltano import c as meltano_c
from flext_oracle_wms import c


class FlextTargetOracleWmsConstants(meltano_c, c):
    """Typed constant namespace used by target Oracle WMS modules."""

    class TargetOracleWms:
        """Target-specific defaults and limits."""

        CLI_MIN_CONFIG_ARG_COUNT: Final[int] = 3

        class OracleWms:
            """Oracle WMS runtime defaults."""

            DEFAULT_TIMEOUT: Final[int] = meltano_c.DEFAULT_TIMEOUT_SECONDS
            DEFAULT_MAX_RETRIES: Final[int] = meltano_c.DEFAULT_MAX_RETRY_ATTEMPTS
            DEFAULT_BATCH_SIZE: Final[int] = meltano_c.DEFAULT_BATCH_SIZE

        class LoadMethods:
            """Allowed load methods."""

            @unique
            class Method(StrEnum):
                """Allowed target load methods."""

                APPEND_ONLY = "APPEND_ONLY"
                UPSERT = "UPSERT"
                REPLACE = "REPLACE"
                MERGE = "MERGE"
                TRUNCATE_INSERT = "TRUNCATE_INSERT"

            VALID_LOAD_METHODS: Final[frozenset[str]] = frozenset(
                member.value for member in Method
            )


meltano_c = FlextTargetOracleWmsConstants
__all__: list[str] = ["FlextTargetOracleWmsConstants", "meltano_c"]
