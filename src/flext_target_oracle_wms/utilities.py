"""Utility helpers for target Oracle WMS operations.

Facade composing helpers from _utilities/ submodules into u.TargetOracleWms.* namespace.
"""

from __future__ import annotations

from collections.abc import (
    Mapping,
)

from flext_meltano import FlextMeltanoUtilities
from flext_oracle_wms import FlextOracleWmsUtilities
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


class FlextTargetOracleWmsUtilities(FlextMeltanoUtilities, FlextOracleWmsUtilities):
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
            record: t.ContainerValueMapping,
        ) -> Mapping[str, t.Container | t.ContainerValueMapping]:
            """Create a Singer RECORD message payload."""
            return create_record_message(stream_name, record)

        @staticmethod
        def create_schema_message(
            stream_name: str,
            schema: t.ContainerValueMapping,
            key_properties: t.StrSequence | None = None,
        ) -> Mapping[str, t.Container | t.ContainerValueMapping | t.StrSequence]:
            """Create a Singer SCHEMA message payload."""
            return create_schema_message(stream_name, schema, key_properties)

        @staticmethod
        def create_state_message(
            state: t.ContainerValueMapping,
        ) -> Mapping[str, t.Container | t.ContainerValueMapping]:
            """Create a Singer STATE message payload."""
            return create_state_message(state)


__all__: list[str] = [
    "FlextTargetOracleWmsUtilities",
    "u",
]
u = FlextTargetOracleWmsUtilities
