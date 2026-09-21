"""Constants for the target Oracle WMS package."""

from __future__ import annotations

from typing import TYPE_CHECKING, Final

from flext_meltano import FlextMeltanoConstants as meltano_c
from flext_oracle_wms import c

from ._constants.base import FlextTargetOracleWmsConstantsBase
from ._constants.values import FlextTargetOracleWmsConstantsValues

if TYPE_CHECKING:
    from flext_oracle_wms import t


class FlextTargetOracleWmsConstants(meltano_c, c):
    """Typed constant namespace used by target Oracle WMS modules."""

    class TargetOracleWms(
        FlextTargetOracleWmsConstantsBase,
        FlextTargetOracleWmsConstantsValues.TargetOracleWms,
    ):
        """Target-specific defaults and limits."""

        class OracleWms(FlextTargetOracleWmsConstantsValues.TargetOracleWms.OracleWms):
            """Oracle WMS runtime defaults."""

            DEFAULT_BATCH_SIZE: Final[int] = (
                meltano_c.Meltano.BATCH_DEFAULT_DEFAULT_BATCH_SIZE
            )


c = FlextTargetOracleWmsConstants
__all__: t.StrSequence = ("FlextTargetOracleWmsConstants", "c")
