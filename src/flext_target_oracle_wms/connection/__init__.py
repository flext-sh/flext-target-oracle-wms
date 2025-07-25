"""Oracle WMS connection module using flext-core patterns."""

from __future__ import annotations

# Contextual import suppression for external libraries
import contextlib

# Import from connection module
with contextlib.suppress(ImportError):
    from flext_target_oracle_wms.connection.config import OracleWMSConnectionConfig
    from flext_target_oracle_wms.connection.connection import OracleWMSConnection

__all__ = [
    "OracleWMSConnection",
    "OracleWMSConnectionConfig",
]
