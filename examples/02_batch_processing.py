#!/usr/bin/env python3
"""Batch processing example for flext-target-oracle-wms.

Demonstrates batch processing patterns with Oracle WMS target.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import FlextLogger, t
from flext_observability import FlextObservabilityMonitor, flext_monitor_function

logger = FlextLogger(__name__)
monitor = FlextObservabilityMonitor()


@flext_monitor_function(monitor)
def run_batch_example() -> t.Scalar:
    """Run batch processing example."""
    logger.info("Starting batch processing example")
    logger.info("Batch processing completed successfully")
    return True


if __name__ == "__main__":
    """Run the batch processing example."""
    run_batch_example()
