"""Utility helpers for target Oracle WMS operations.

Facade composing helpers from _utilities/ submodules into u.TargetOracleWms.* namespace.
"""

from __future__ import annotations

from flext_meltano.utilities import FlextMeltanoUtilities as meltano_u
from flext_oracle_wms.utilities import u
from flext_target_oracle_wms._utilities.client import (
    FlextTargetOracleWmsUtilitiesClient,
)
from flext_target_oracle_wms._utilities.helpers import (
    FlextTargetOracleWmsUtilitiesHelpers,
)


class FlextTargetOracleWmsUtilities(meltano_u, u):
    """Namespace exposing Singer-target Client and Helpers under TargetOracleWms.*."""

    class TargetOracleWms:
        """Project-local namespace aggregating Client and Helpers public classes."""

        Client = FlextTargetOracleWmsUtilitiesClient
        Helpers = FlextTargetOracleWmsUtilitiesHelpers

        # Direct nested-class access for canonical u.TargetOracleWms.<Class> usage
        CatalogManager = FlextTargetOracleWmsUtilitiesClient.CatalogManager
        StreamProcessor = FlextTargetOracleWmsUtilitiesClient.StreamProcessor
        Target = FlextTargetOracleWmsUtilitiesClient.Target
        Validation = FlextTargetOracleWmsUtilitiesHelpers.Validation
        WMSDataTransformer = FlextTargetOracleWmsUtilitiesHelpers.WMSDataTransformer
        WMSSchemaMapper = FlextTargetOracleWmsUtilitiesHelpers.WMSSchemaMapper
        WMSTableManager = FlextTargetOracleWmsUtilitiesHelpers.WMSTableManager
        WMSTypeConverter = FlextTargetOracleWmsUtilitiesHelpers.WMSTypeConverter
        create_record_message = staticmethod(
            FlextTargetOracleWmsUtilitiesHelpers.create_record_message,
        )
        create_schema_message = staticmethod(
            FlextTargetOracleWmsUtilitiesHelpers.create_schema_message,
        )
        create_state_message = staticmethod(
            FlextTargetOracleWmsUtilitiesHelpers.create_state_message,
        )


__all__: list[str] = [
    "FlextTargetOracleWmsUtilities",
    "u",
]
u = FlextTargetOracleWmsUtilities
