"""Performance benchmarks for target Oracle WMS components.

Uses time.time() for measurement (pytest-benchmark is unavailable).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import time

from tests import c, tm, u


class TestsFlextTargetOracleWmsBenchmarks:
    """Performance tests for WMSTypeConverter."""

    @staticmethod
    def test_convert_string_performance() -> None:
        """Test convert string performance."""
        converter = u.TargetOracleWms.WMSTypeConverter()
        start = time.time()
        for _ in range(c.TargetOracleWms.Tests.PERF_ITERATIONS):
            converter.convert_singer_to_oracle("string", "hello")
        elapsed = time.time() - start
        tm.that(elapsed, lt=c.TargetOracleWms.Tests.PERF_THRESHOLD_SEC)

    @staticmethod
    def test_convert_integer_performance() -> None:
        """Test convert integer performance."""
        converter = u.TargetOracleWms.WMSTypeConverter()
        start = time.time()
        for _ in range(c.TargetOracleWms.Tests.PERF_ITERATIONS):
            converter.convert_singer_to_oracle("integer", 42)
        elapsed = time.time() - start
        tm.that(elapsed, lt=c.TargetOracleWms.Tests.PERF_THRESHOLD_SEC)

    @staticmethod
    def test_register_and_lookup_performance() -> None:
        """Test register and lookup performance."""
        manager = u.TargetOracleWms.WMSTableManager()
        start = time.time()
        for i in range(c.TargetOracleWms.Tests.PERF_ITERATIONS):
            name = f"stream_{i}"
            manager.register_stream(name)
            manager.get_table_name(name)
        elapsed = time.time() - start
        tm.that(elapsed, lt=c.TargetOracleWms.Tests.PERF_THRESHOLD_SEC)

    @staticmethod
    def test_add_and_get_stream_performance() -> None:
        """Test add and get stream performance."""
        mgr = u.TargetOracleWms.CatalogManager()
        start = time.time()
        for i in range(c.TargetOracleWms.Tests.PERF_ITERATIONS):
            name = f"stream_{i}"
            mgr.add_stream(u.TargetOracleWms.Tests.schema_msg(name))
            mgr.get_stream(name)
        elapsed = time.time() - start
        tm.that(elapsed, lt=c.TargetOracleWms.Tests.PERF_THRESHOLD_SEC)

    @staticmethod
    def test_transform_record_performance() -> None:
        """Test transform record performance."""
        transformer = u.TargetOracleWms.WMSDataTransformer()
        bench = c.TargetOracleWms.Tests.BENCH_STREAM
        rec = u.TargetOracleWms.Tests.record_msg(
            bench, {"id": c.ParserBooleanToken.ONE, "qty": 100}
        )
        schema = u.TargetOracleWms.Tests.schema_msg(bench)
        start = time.time()
        for _ in range(c.TargetOracleWms.Tests.PERF_ITERATIONS):
            transformer.transform_record(rec, schema)
        elapsed = time.time() - start
        tm.that(elapsed, lt=c.TargetOracleWms.Tests.PERF_THRESHOLD_SEC)
