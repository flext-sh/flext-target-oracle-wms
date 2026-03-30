# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Internal utility submodules for target Oracle WMS."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_target_oracle_wms._utilities import client as client, helpers as helpers
    from flext_target_oracle_wms._utilities.client import (
        CatalogManager as CatalogManager,
        StreamProcessor as StreamProcessor,
        Target as Target,
    )
    from flext_target_oracle_wms._utilities.helpers import (
        Validation as Validation,
        WMSDataTransformer as WMSDataTransformer,
        WMSSchemaMapper as WMSSchemaMapper,
        WMSTableManager as WMSTableManager,
        WMSTypeConverter as WMSTypeConverter,
        create_record_message as create_record_message,
        create_schema_message as create_schema_message,
        create_state_message as create_state_message,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "CatalogManager": ["flext_target_oracle_wms._utilities.client", "CatalogManager"],
    "StreamProcessor": ["flext_target_oracle_wms._utilities.client", "StreamProcessor"],
    "Target": ["flext_target_oracle_wms._utilities.client", "Target"],
    "Validation": ["flext_target_oracle_wms._utilities.helpers", "Validation"],
    "WMSDataTransformer": [
        "flext_target_oracle_wms._utilities.helpers",
        "WMSDataTransformer",
    ],
    "WMSSchemaMapper": [
        "flext_target_oracle_wms._utilities.helpers",
        "WMSSchemaMapper",
    ],
    "WMSTableManager": [
        "flext_target_oracle_wms._utilities.helpers",
        "WMSTableManager",
    ],
    "WMSTypeConverter": [
        "flext_target_oracle_wms._utilities.helpers",
        "WMSTypeConverter",
    ],
    "client": ["flext_target_oracle_wms._utilities.client", ""],
    "create_record_message": [
        "flext_target_oracle_wms._utilities.helpers",
        "create_record_message",
    ],
    "create_schema_message": [
        "flext_target_oracle_wms._utilities.helpers",
        "create_schema_message",
    ],
    "create_state_message": [
        "flext_target_oracle_wms._utilities.helpers",
        "create_state_message",
    ],
    "helpers": ["flext_target_oracle_wms._utilities.helpers", ""],
}

_EXPORTS: Sequence[str] = [
    "CatalogManager",
    "StreamProcessor",
    "Target",
    "Validation",
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
    "client",
    "create_record_message",
    "create_schema_message",
    "create_state_message",
    "helpers",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
