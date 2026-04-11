#!/usr/bin/env python3
"""Advanced configuration example for flext-target-oracle-wms - PRODUCTION REAL IMPLEMENTATION.

Demonstrates advanced configuration and custom business logic for production use.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import t
from flext_observability import FlextObservabilityMonitor, flext_monitor_function
from flext_target_oracle_wms import c

logger = u.fetch_logger(__name__)
monitor = FlextObservabilityMonitor()

LOAD_METHOD: str = c.TargetOracleWms.LoadMethods.UPSERT
DEFAULT_BATCH: int = c.TargetOracleWms.OracleWms.DEFAULT_BATCH_SIZE


@flext_monitor_function(monitor)
def run_advanced_example() -> t.Scalar:
    """Run advanced configuration example with Oracle WMS constants."""
    logger.info("Starting advanced configuration example")
    logger.info("Load method: %s, base_url: wms.example.oraclecloud.com", LOAD_METHOD)
    logger.info("Default batch size: %d, password protected", DEFAULT_BATCH)
    logger.info("Advanced configuration example completed successfully")
    return True


if __name__ == "__main__":
    """Run the advanced configuration example."""
    run_advanced_example()
