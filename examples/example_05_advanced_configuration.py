#!/usr/bin/env python3
"""Advanced configuration example for flext-target-oracle-wms (real).

Demonstrates advanced configuration and custom business logic for production use.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from examples import c, t, u

if TYPE_CHECKING:
    from examples import p


class FlextTargetOracleWmsExampleAdvancedConfiguration:
    """Advanced configuration read from the Oracle WMS constants."""

    logger: ClassVar[p.Logger] = u.fetch_logger(__name__)
    LOAD_METHOD: ClassVar[str] = c.TargetOracleWms.LoadMethods.Method.UPSERT
    DEFAULT_BATCH: ClassVar[int] = c.TargetOracleWms.OracleWms.DEFAULT_BATCH_SIZE

    @staticmethod
    def run_advanced_example() -> t.Scalar:
        """Run advanced configuration example with Oracle WMS constants.

        Returns:
            The resulting ``t.Scalar``.

        """
        example = FlextTargetOracleWmsExampleAdvancedConfiguration
        example.logger.info("Starting advanced configuration example")
        example.logger.info(
            "Load method: %s, base_url: wms.example.oraclecloud.com",
            example.LOAD_METHOD,
        )
        example.logger.info(
            "Default batch size: %d, password protected", example.DEFAULT_BATCH
        )
        example.logger.info("Advanced configuration example completed successfully")
        return True

    @staticmethod
    def main() -> t.Scalar:
        """Run the advanced configuration example.

        Returns:
            ``True`` when the example completed.

        """
        return FlextTargetOracleWmsExampleAdvancedConfiguration.run_advanced_example()


__all__: list[str] = ["FlextTargetOracleWmsExampleAdvancedConfiguration"]

if __name__ == "__main__":
    FlextTargetOracleWmsExampleAdvancedConfiguration.main()
