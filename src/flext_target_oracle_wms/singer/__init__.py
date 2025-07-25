"""Singer WMS module using flext-core patterns."""

from __future__ import annotations

# Contextual import suppression for external libraries
import contextlib

# Import from singer module
with contextlib.suppress(ImportError):
    from flext_target_oracle_wms.singer.catalog import SingerWMSCatalogManager
    from flext_target_oracle_wms.singer.stream import SingerWMSStreamProcessor
    from flext_target_oracle_wms.singer.target import SingerTargetOracleWMS

__all__ = [
    "SingerTargetOracleWMS",
    "SingerWMSCatalogManager",
    "SingerWMSStreamProcessor",
]
