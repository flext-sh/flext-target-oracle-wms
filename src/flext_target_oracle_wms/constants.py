"""Constants for the target Oracle WMS package."""

from __future__ import annotations

from enum import StrEnum, unique
from typing import TYPE_CHECKING, Final

from flext_meltano.constants import FlextMeltanoConstants as meltano_c
from flext_oracle_wms import c

if TYPE_CHECKING:
    from flext_oracle_wms import t


class FlextTargetOracleWmsConstants(meltano_c, c):
    """Typed constant namespace used by target Oracle WMS modules."""

    class TargetOracleWms:
        """Target-specific defaults and limits."""

        CLI_MIN_CONFIG_ARG_COUNT: Final[int] = 3

        class OracleWms:
            """Oracle WMS runtime defaults."""

            DEFAULT_TIMEOUT: Final[int] = meltano_c.Meltano.DEFAULT_TIMEOUT_SECONDS
            DEFAULT_MAX_RETRIES: Final[int] = 3
            DEFAULT_BATCH_SIZE: Final[int] = (
                meltano_c.Meltano.BATCH_DEFAULT_DEFAULT_BATCH_SIZE
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

            VALID_LOAD_METHODS: Final[frozenset[str]] = frozenset(
                member.value for member in Method
            )


c = FlextTargetOracleWmsConstants
__all__: t.StrSequence = ("FlextTargetOracleWmsConstants", "c")
