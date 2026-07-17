#!/usr/bin/env python3
"""Target creation example for flext-target-oracle-wms - PRODUCTION REAL IMPLEMENTATION.

Demonstrates the canonical way to build and construct an Oracle WMS Singer target
in production: validate a WmsTargetConfig model and construct the target through
the ``u.TargetOracleWms`` utilities facade. The library delivers target creation
through its canonical service/utilities surface — there is no separate factory
module (a parallel creation branch was removed in favour of the MRO facade).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING, Final

from flext_observability.services.monitoring import (
    FlextObservabilityMonitor,
    flext_monitor_function,
)
from flext_target_oracle_wms import (
    m,
    t,
    u,
)

if TYPE_CHECKING:
    from collections.abc import Mapping

_ = u  # Anchor flext_core import for example validation.

logger = u.fetch_logger(__name__)
monitor = FlextObservabilityMonitor()

TARGET_CONFIG: Final[Mapping[str, str]] = MappingProxyType({
    "base_url": "https://wms.example.oraclecloud.com",
    "username": "wms_target_user",
    "password": "wms_target_pass",
})


@flext_monitor_function(monitor)
def run_target_creation_example() -> t.Scalar:
    """Create an Oracle WMS target via the canonical utilities facade."""
    logger.info("Starting Oracle WMS target creation example")
    config = m.TargetOracleWms.WmsTargetConfig.model_validate({
        "wms_auth": {
            "base_url": TARGET_CONFIG["base_url"],
            "username": TARGET_CONFIG["username"],
            "password": TARGET_CONFIG["password"],
        },
    })
    target = u.TargetOracleWms.Target(config)
    logger.info("Created Oracle WMS target: %s", target.name)
    logger.info("Target creation example completed successfully")
    return True


if __name__ == "__main__":
    """Run the target creation example."""
    run_target_creation_example()
