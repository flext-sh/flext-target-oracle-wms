"""Utility helpers for target Oracle WMS operations.

Facade composing helpers from _utilities/ submodules into u.TargetOracleWms.* namespace.
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoUtilities
from flext_oracle_wms import u

from flext_target_oracle_wms._utilities.client import (
    FlextTargetOracleWmsUtilitiesClient,
)
from flext_target_oracle_wms._utilities.helpers import (
    FlextTargetOracleWmsUtilitiesHelpers,
)
from flext_target_oracle_wms.typings import t


class FlextTargetOracleWmsUtilities(FlextMeltanoUtilities, u):
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

        @staticmethod
        def create_record_message(
            stream_name: str,
            record: t.JsonMapping,
        ) -> t.JsonMapping:
            """Create a Singer RECORD message payload."""
            return t.Cli.JSON_MAPPING_ADAPTER.validate_python(
                FlextTargetOracleWmsUtilitiesHelpers.create_record_message(
                    stream_name, record
                ),
            )

        @staticmethod
        def create_schema_message(
            stream_name: str,
            schema: t.JsonMapping,
            key_properties: t.StrSequence | None = None,
        ) -> t.JsonMapping:
            """Create a Singer SCHEMA message payload."""
            return t.Cli.JSON_MAPPING_ADAPTER.validate_python(
                FlextTargetOracleWmsUtilitiesHelpers.create_schema_message(
                    stream_name, schema, key_properties
                ),
            )

        @staticmethod
        def create_state_message(
            state: t.JsonMapping,
        ) -> t.JsonMapping:
            """Create a Singer STATE message payload."""
            return t.Cli.JSON_MAPPING_ADAPTER.validate_python(
                FlextTargetOracleWmsUtilitiesHelpers.create_state_message(state),
            )


__all__: list[str] = [
    "FlextTargetOracleWmsUtilities",
    "u",
]
u = FlextTargetOracleWmsUtilities
