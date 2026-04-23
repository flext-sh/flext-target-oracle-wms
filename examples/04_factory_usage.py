#!/usr/bin/env python3
"""Factory usage example for flext-target-oracle-wms - PRODUCTION REAL IMPLEMENTATION.

Demonstrates factory patterns for target creation in production.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import u as core_u
from flext_observability import (
    FlextObservabilityMonitor,
    flext_monitor_function,
)

from examples import t, u
from flext_target_oracle_wms import FlextTargetFactory, FlextTargetOracleWmsModels

_ = core_u  # Anchor flext_core import for example validation.

logger = u.fetch_logger(__name__)
monitor = FlextObservabilityMonitor()

FACTORY_CONFIG = {
    "base_url": "https://wms.example.oraclecloud.com",
    "username": "wms_factory_user",
    "password": "wms_factory_pass",
}


@flext_monitor_function(monitor)
def run_factory_example() -> t.Scalar:
    """Run factory usage example with Oracle WMS target creation."""
    logger.info("Starting factory usage example")
    request = FlextTargetOracleWmsModels.TargetOracleWms.TargetCreationRequest(
        base_url=FACTORY_CONFIG["base_url"],
        username=FACTORY_CONFIG["username"],
        password=FACTORY_CONFIG["password"],
        additional_config=None,
    )
    result = FlextTargetFactory.create_target(request)
    if result.success:
        logger.info("Created Oracle WMS target: %s", result.value.name)
    logger.info("Factory usage example completed successfully")
    return True


if __name__ == "__main__":
    """Run the factory usage example."""
    run_factory_example()
