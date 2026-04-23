"""Utility helpers for target Oracle WMS operations.

Facade composing helpers from _utilities/ submodules into u.TargetOracleWms.* namespace.
"""

from __future__ import annotations

from flext_meltano import u as meltano_u
from flext_oracle_wms import u

from flext_target_oracle_wms import (
    CatalogManager,
    StreamProcessor,
    Target,
    Validation,
    WMSDataTransformer,
    WMSSchemaMapper,
    WMSTableManager,
    WMSTypeConverter,
    create_record_message,
    create_schema_message,
    create_state_message,
    t,
)


class FlextTargetOracleWmsUtilities(meltano_u, u):
    """Namespace with Singer-target utility helpers."""

    class TargetOracleWms:
        """Helpers for Singer message shape handling."""

        # Nested class bindings — private _utilities classes exposed through the facade
        CatalogManager = CatalogManager
        StreamProcessor = StreamProcessor
        Target = Target
        Validation = Validation
        WMSDataTransformer = WMSDataTransformer
        WMSSchemaMapper = WMSSchemaMapper
        WMSTableManager = WMSTableManager
        WMSTypeConverter = WMSTypeConverter

        @staticmethod
        def create_record_message(
            stream_name: str,
            record: t.JsonMapping,
        ) -> t.JsonMapping:
            """Create a Singer RECORD message payload."""
            return t.Cli.JSON_MAPPING_ADAPTER.validate_python(
                create_record_message(stream_name, record),
            )

        @staticmethod
        def create_schema_message(
            stream_name: str,
            schema: t.JsonMapping,
            key_properties: t.StrSequence | None = None,
        ) -> t.JsonMapping:
            """Create a Singer SCHEMA message payload."""
            return t.Cli.JSON_MAPPING_ADAPTER.validate_python(
                create_schema_message(stream_name, schema, key_properties),
            )

        @staticmethod
        def create_state_message(
            state: t.JsonMapping,
        ) -> t.JsonMapping:
            """Create a Singer STATE message payload."""
            return t.Cli.JSON_MAPPING_ADAPTER.validate_python(
                create_state_message(state),
            )


__all__: list[str] = [
    "FlextTargetOracleWmsUtilities",
    "u",
]
u = FlextTargetOracleWmsUtilities
