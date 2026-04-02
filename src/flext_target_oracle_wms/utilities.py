"""Utility helpers for target Oracle WMS operations.

Facade composing helpers from _utilities/ submodules into u.TargetOracleWms.* namespace.
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoUtilities
from flext_oracle_wms import FlextOracleWmsUtilities

from flext_target_oracle_wms import (
    Validation,
    WMSDataTransformer,
    WMSSchemaMapper,
    WMSTableManager,
    WMSTypeConverter,
    create_record_message,
    create_schema_message,
    create_state_message,
)


class FlextTargetOracleWmsUtilities(FlextMeltanoUtilities, FlextOracleWmsUtilities):
    """Namespace with Singer-target utility helpers."""

    class TargetOracleWms:
        """Helpers for Singer message shape handling."""

        create_record_message = staticmethod(create_record_message)
        create_schema_message = staticmethod(create_schema_message)
        create_state_message = staticmethod(create_state_message)

        Validation = Validation
        WMSTypeConverter = WMSTypeConverter
        WMSDataTransformer = WMSDataTransformer
        WMSSchemaMapper = WMSSchemaMapper
        WMSTableManager = WMSTableManager


__all__ = [
    "FlextTargetOracleWmsUtilities",
    "u",
]
u = FlextTargetOracleWmsUtilities
