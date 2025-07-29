"""Oracle WMS connection management - REFACTORED to eliminate code duplication.

Uses FlextOracleWmsClient from flext-oracle-wms library instead of reimplementing.
This eliminates 168 lines of duplicated WMS connection functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_core import get_logger
from flext_oracle_wms import FlextOracleWmsClient

logger = get_logger(__name__)

# Use library client instead of reimplementing connection
FlextOracleOracleWMSConnection = FlextOracleWmsClient

# Alias for backward compatibility
OracleWMSConnection = FlextOracleWmsClient

__all__ = ["FlextOracleOracleWMSConnection", "OracleWMSConnection"]
