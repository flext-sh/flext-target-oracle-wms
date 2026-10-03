"""Utility helpers for target Oracle WMS operations.

Facade composing helpers from _utilities/ submodules into u.TargetOracleWms.* namespace.
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoUtilities
from flext_oracle_wms import FlextOracleWmsUtilities

from ._utilities.client import FlextTargetOracleWmsUtilitiesClient
from ._utilities.helpers import FlextTargetOracleWmsUtilitiesHelpers


class FlextTargetOracleWmsUtilities(FlextMeltanoUtilities, FlextOracleWmsUtilities):
    """Namespace exposing Singer-target Client and Helpers under TargetOracleWms.*."""

    class TargetOracleWms:
        """Project-local namespace aggregating Client and Helpers public classes."""

        Client = FlextTargetOracleWmsUtilitiesClient
        Helpers = FlextTargetOracleWmsUtilitiesHelpers

        # Direct nested-class access for canonical u.TargetOracleWms.<Class> usage
        CatalogManager = FlextTargetOracleWmsUtilitiesClient.CatalogManager
        StreamProcessor = FlextTargetOracleWmsUtilitiesClient.StreamProcessor
        Target = FlextTargetOracleWmsUtilitiesClient.Target
        WMSDataTransformer = FlextTargetOracleWmsUtilitiesHelpers.WMSDataTransformer
        WMSTableManager = FlextTargetOracleWmsUtilitiesHelpers.WMSTableManager
        WMSTypeConverter = FlextTargetOracleWmsUtilitiesHelpers.WMSTypeConverter


__all__: list[str] = ["FlextTargetOracleWmsUtilities", "u"]
u = FlextTargetOracleWmsUtilities
