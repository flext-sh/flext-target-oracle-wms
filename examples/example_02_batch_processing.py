#!/usr/bin/env python3
"""Batch processing example for flext-target-oracle-wms (real implementation).

Demonstrates batch processing patterns with Oracle WMS target for production use.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING, ClassVar

from flext_target_oracle_wms import settings, t, u

if TYPE_CHECKING:
    from flext_target_oracle_wms import p


class FlextTargetOracleWmsExampleBatchProcessing:
    """Batch processing over several Oracle WMS streams."""

    logger: ClassVar[p.Logger] = u.fetch_logger(__name__)
    BATCH_CONFIG: ClassVar[t.JsonMapping] = MappingProxyType({
        "wms_auth": {
            "base_url": "https://wms.example.oraclecloud.com",
            "username": "wms_batch_user",
            "password": settings.TargetOracleWms.password,
        },
        "batch_size": 500,
    })
    STREAMS: ClassVar[tuple[str, ...]] = ("orders", "items", "tasks")

    @staticmethod
    def run_batch_example() -> t.Scalar:
        """Run batch processing example with Oracle WMS table management.

        Returns:
            The resulting ``t.Scalar``.

        """
        example = FlextTargetOracleWmsExampleBatchProcessing
        example.logger.info("Starting batch processing example")
        batch_size = example.BATCH_CONFIG["batch_size"]
        manager = u.TargetOracleWms.WMSTableManager()
        for stream in example.STREAMS:
            result = manager.register_stream(stream)
            if result.success:
                example.logger.info(
                    "Registered stream table %s for batches of %s",
                    result.value,
                    batch_size,
                )
        example.logger.info(
            "Batch processing completed: %d streams", len(example.STREAMS)
        )
        return True

    @staticmethod
    def main() -> t.Scalar:
        """Run the batch processing example.

        Returns:
            ``True`` when the example completed.

        """
        return FlextTargetOracleWmsExampleBatchProcessing.run_batch_example()


__all__: list[str] = ["FlextTargetOracleWmsExampleBatchProcessing"]

if __name__ == "__main__":
    FlextTargetOracleWmsExampleBatchProcessing.main()
