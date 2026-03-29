# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Internal utility submodules for target Oracle WMS."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes

    from flext_target_oracle_wms._utilities.client import (
        CatalogManager,
        StreamProcessor,
        Target,
    )
    from flext_target_oracle_wms._utilities.helpers import (
        Validation,
        WMSDataTransformer,
        WMSSchemaMapper,
        WMSTableManager,
        WMSTypeConverter,
        create_record_message,
        create_schema_message,
        create_state_message,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "CatalogManager": ["flext_target_oracle_wms._utilities.client", "CatalogManager"],
    "StreamProcessor": ["flext_target_oracle_wms._utilities.client", "StreamProcessor"],
    "Target": ["flext_target_oracle_wms._utilities.client", "Target"],
    "Validation": ["flext_target_oracle_wms._utilities.helpers", "Validation"],
    "WMSDataTransformer": ["flext_target_oracle_wms._utilities.helpers", "WMSDataTransformer"],
    "WMSSchemaMapper": ["flext_target_oracle_wms._utilities.helpers", "WMSSchemaMapper"],
    "WMSTableManager": ["flext_target_oracle_wms._utilities.helpers", "WMSTableManager"],
    "WMSTypeConverter": ["flext_target_oracle_wms._utilities.helpers", "WMSTypeConverter"],
    "create_record_message": ["flext_target_oracle_wms._utilities.helpers", "create_record_message"],
    "create_schema_message": ["flext_target_oracle_wms._utilities.helpers", "create_schema_message"],
    "create_state_message": ["flext_target_oracle_wms._utilities.helpers", "create_state_message"],
}

__all__ = [
    "CatalogManager",
    "StreamProcessor",
    "Target",
    "Validation",
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
    "create_record_message",
    "create_schema_message",
    "create_state_message",
]


_LAZY_CACHE: MutableMapping[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> Sequence[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
