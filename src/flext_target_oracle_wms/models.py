"""Compatibility re-export for target models.

This module provides a stable import path `flext_target_oracle_wms.models`
by re-exporting all symbols from `target_models`.


Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from .target_models import (
    WMSDataTransformer,
    WMSSchemaMapper,
    WMSTableManager,
    WMSTypeConverter,
    get_oracle_type_mapping,
    get_wms_metadata_columns,
)

__all__ = [
    "WMSDataTransformer",
    "WMSSchemaMapper",
    "WMSTableManager",
    "WMSTypeConverter",
    "get_oracle_type_mapping",
    "get_wms_metadata_columns",
]
