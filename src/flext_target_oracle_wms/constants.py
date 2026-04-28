"""Constants for the target Oracle WMS package."""

from __future__ import annotations

from enum import StrEnum, unique
from typing import Final

from flext_meltano import FlextMeltanoConstants
from flext_oracle_wms import c


class FlextTargetOracleWmsConstants(FlextMeltanoConstants, c):
    """Typed constant namespace used by target Oracle WMS modules."""

    class TargetOracleWms:
        """Target-specific defaults and limits."""

        CLI_MIN_CONFIG_ARG_COUNT: Final[int] = 3

        class Tests:
            """Test fixture constants — patch paths and test-only literals."""

            PATCH_TARGET: Final[str] = (
                "flext_target_oracle_wms.utilities."
                "FlextTargetOracleWmsUtilities.TargetOracleWms.Target"
            )

        class OracleWms:
            """Oracle WMS runtime defaults."""

            DEFAULT_TIMEOUT: Final[int] = (
                FlextMeltanoConstants.Meltano.DEFAULT_TIMEOUT_SECONDS
            )
            DEFAULT_MAX_RETRIES: Final[int] = 3
            DEFAULT_BATCH_SIZE: Final[int] = (
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
                TRUNCATE_INSERT = "TRUNCATE_INSERT"

            VALID_LOAD_METHODS: Final[frozenset[str]] = frozenset(
                member.value for member in Method
            )


c = FlextTargetOracleWmsConstants
__all__: tuple[str, ...] = ("FlextTargetOracleWmsConstants", "c")
