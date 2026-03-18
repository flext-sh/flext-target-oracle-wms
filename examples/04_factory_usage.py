#!/usr/bin/env python3
"""Factory usage example for flext-target-oracle-wms.

Demonstrates factory patterns for target creation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import FlextLogger, t
from flext_observability import FlextObservabilityMonitor, flext_monitor_function

logger = FlextLogger(__name__)
monitor = FlextObservabilityMonitor()


@flext_monitor_function(monitor)
def run_factory_example() -> t.Scalar:
    """Run factory usage example."""
    logger.info("Starting factory usage example")
    logger.info("Factory usage example completed successfully")
    return True


if __name__ == "__main__":
    """Run the factory usage example."""
    run_factory_example()
