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

from collections.abc import Mapping
from types import MappingProxyType
from typing import TYPE_CHECKING, ClassVar

from examples import m, settings, t, u

if TYPE_CHECKING:
    from examples import p


class FlextTargetOracleWmsExampleFactoryUsage:
    """Target construction from a validated ``WmsTargetConfig``."""

    logger: ClassVar[p.Logger] = u.fetch_logger(__name__)
    TARGET_CONFIG: ClassVar[Mapping[str, str]] = MappingProxyType({
        "base_url": "https://wms.example.oraclecloud.com",
        "username": "wms_target_user",
        "password": settings.TargetOracleWms.password,
    })

    @staticmethod
    def run_target_creation_example() -> t.Scalar:
        """Create an Oracle WMS target via the canonical utilities facade.

        Returns:
            The resulting ``t.Scalar``.

        """
        example = FlextTargetOracleWmsExampleFactoryUsage
        example.logger.info("Starting Oracle WMS target creation example")
        config = m.TargetOracleWms.WmsTargetConfig.model_validate({
            "wms_auth": {
                "base_url": example.TARGET_CONFIG["base_url"],
                "username": example.TARGET_CONFIG["username"],
                "password": example.TARGET_CONFIG["password"],
            },
        })
        target = u.TargetOracleWms.Target(config)
        example.logger.info("Created Oracle WMS target: %s", target.name)
        example.logger.info("Target creation example completed successfully")
        return True

    @staticmethod
    def main() -> t.Scalar:
        """Run the target creation example.

        Returns:
            ``True`` when the example completed.

        """
        return FlextTargetOracleWmsExampleFactoryUsage.run_target_creation_example()


__all__: list[str] = ["FlextTargetOracleWmsExampleFactoryUsage"]

if __name__ == "__main__":
    FlextTargetOracleWmsExampleFactoryUsage.main()
