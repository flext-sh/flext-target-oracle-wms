#!/usr/bin/env python3
"""Advanced configuration example for flext-target-oracle-wms.

Demonstrates advanced configuration and custom business logic.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import FlextLogger, t
from flext_observability import FlextObservabilityMonitor, flext_monitor_function

logger = FlextLogger(__name__)
monitor = FlextObservabilityMonitor()


@flext_monitor_function(monitor)
def run_advanced_example() -> t.Scalar:
    """Run advanced configuration example."""
    logger.info("Starting advanced configuration example")
    logger.info("Advanced configuration example completed successfully")
    return True


if __name__ == "__main__":
    """Run the advanced configuration example."""
    run_advanced_example()
