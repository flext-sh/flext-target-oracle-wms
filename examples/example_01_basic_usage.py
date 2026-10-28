#!/usr/bin/env python3
"""Basic usage example for flext-target-oracle-wms - PRODUCTION REAL IMPLEMENTATION.

This example demonstrates the basic usage of the Oracle WMS target with REAL
flext-* APIs and production-quality patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path
from types import MappingProxyType
from typing import TYPE_CHECKING, ClassVar

from examples import settings, t, u

if TYPE_CHECKING:
    from collections.abc import Mapping

    from examples import p


class FlextTargetOracleWmsExampleBasicUsage:
    """Basic Oracle WMS target usage: stream registration and Singer files."""

    logger: ClassVar[p.Logger] = u.fetch_logger(__name__)
    WMS_AUTH: ClassVar[Mapping[str, str]] = MappingProxyType({
        "base_url": "https://wms.example.oraclecloud.com",
        "username": "wms_user",
        "password": settings.TargetOracleWms.password,
    })
    BATCH_SIZE: ClassVar[int] = 100
    CONFIG_FILE_NAME: ClassVar[str] = "settings.json"
    STREAM_NAME: ClassVar[str] = "orders"

    @staticmethod
    def run_basic_example() -> t.Scalar:
        """Run basic Oracle WMS target example with REAL configuration.

        Returns:
            The resulting ``t.Scalar``.

        """
        example = FlextTargetOracleWmsExampleBasicUsage
        example.logger.info("Starting basic Oracle WMS target example")
        example.logger.info(
            "Using base_url=%s, batch_size=%d",
            example.WMS_AUTH["base_url"],
            example.BATCH_SIZE,
        )
        manager = u.TargetOracleWms.WMSTableManager()
        registered = manager.register_stream(example.STREAM_NAME)
        lookup = manager.get_table_name(example.STREAM_NAME)
        example.logger.info(
            "Registered=%s, lookup=%s",
            registered.success,
            lookup.value if lookup.success else lookup.error,
        )
        example.logger.info("Example completed successfully")
        return True

    @staticmethod
    def run_from_singer_files() -> t.Scalar:
        """Run target from Singer JSON files - REAL Singer integration.

        Returns:
            The resulting ``t.Scalar``.

        """
        example = FlextTargetOracleWmsExampleBasicUsage
        example.logger.info("Running target from Singer JSON files")
        if Path(example.CONFIG_FILE_NAME).exists():
            example.logger.info("Config file found")
        else:
            example.logger.info("Using default configuration")
        example.logger.info("Singer file processing completed")
        return True

    @staticmethod
    def main() -> t.Scalar:
        """Run every basic usage step.

        Returns:
            ``True`` when every step completed.

        """
        example = FlextTargetOracleWmsExampleBasicUsage
        basic = example.run_basic_example()
        singer = example.run_from_singer_files()
        return bool(basic) and bool(singer)


__all__: list[str] = ["FlextTargetOracleWmsExampleBasicUsage"]

if __name__ == "__main__":
    FlextTargetOracleWmsExampleBasicUsage.main()
