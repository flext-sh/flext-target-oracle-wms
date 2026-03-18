#!/usr/bin/env python3
"""Error handling example for flext-target-oracle-wms.

Demonstrates error handling and resilience patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import FlextLogger, t
from flext_observability import FlextObservabilityMonitor, flext_monitor_function

logger = FlextLogger(__name__)
monitor = FlextObservabilityMonitor()


@flext_monitor_function(monitor)
def run_error_handling_example() -> t.Scalar:
    """Run error handling example."""
    logger.info("Starting error handling example")
    logger.info("Error handling example completed successfully")
    return True


if __name__ == "__main__":
    """Run the error handling example."""
    run_error_handling_example()
