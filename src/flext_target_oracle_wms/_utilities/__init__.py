# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Internal utility submodules for target Oracle WMS."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_target_oracle_wms._utilities import client, helpers
    from flext_target_oracle_wms._utilities.client import *
    from flext_target_oracle_wms._utilities.helpers import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "CatalogManager": "flext_target_oracle_wms._utilities.client",
    "StreamProcessor": "flext_target_oracle_wms._utilities.client",
    "Target": "flext_target_oracle_wms._utilities.client",
    "Validation": "flext_target_oracle_wms._utilities.helpers",
    "WMSDataTransformer": "flext_target_oracle_wms._utilities.helpers",
    "WMSSchemaMapper": "flext_target_oracle_wms._utilities.helpers",
    "WMSTableManager": "flext_target_oracle_wms._utilities.helpers",
    "WMSTypeConverter": "flext_target_oracle_wms._utilities.helpers",
    "client": "flext_target_oracle_wms._utilities.client",
    "create_record_message": "flext_target_oracle_wms._utilities.helpers",
    "create_schema_message": "flext_target_oracle_wms._utilities.helpers",
    "create_state_message": "flext_target_oracle_wms._utilities.helpers",
    "helpers": "flext_target_oracle_wms._utilities.helpers",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, sorted(_LAZY_IMPORTS))
