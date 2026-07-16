"""Performance benchmarks for target Oracle WMS components.

Uses time.time() for measurement (pytest-benchmark is unavailable).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import time

from tests import c, m, u


def _schema_msg(stream: str = "bench") -> p.Meltano.SingerSchemaMessage:
    return m.Meltano.SingerSchemaMessage(
        type=c.Meltano.SingerMessageType.SCHEMA,
        stream=stream,
        schema_definition={
            "type": "object",
        },
        key_properties=["id"],
    )


def _record_msg(stream: str = "bench") -> p.Meltano.SingerRecordMessage:
    return m.Meltano.SingerRecordMessage(
        type=c.Meltano.SingerMessageType.RECORD,
        stream=stream,
        record={"id": "1", "qty": 100},
    )


class TestsFlextTargetOracleWmsBenchmarks:
    """Performance tests for WMSTypeConverter."""

    def test_convert_string_performance(self) -> None:
        converter = u.TargetOracleWms.WMSTypeConverter()
        start = time.time()
        for _ in range(c.TargetOracleWms.Tests.PERF_ITERATIONS):
            converter.convert_singer_to_oracle("string", "hello")
        elapsed = time.time() - start
        assert elapsed < c.TargetOracleWms.Tests.PERF_THRESHOLD_SEC

    def test_convert_integer_performance(self) -> None:
        converter = u.TargetOracleWms.WMSTypeConverter()
        start = time.time()
        for _ in range(c.TargetOracleWms.Tests.PERF_ITERATIONS):
            converter.convert_singer_to_oracle("integer", 42)
        elapsed = time.time() - start
        assert elapsed < c.TargetOracleWms.Tests.PERF_THRESHOLD_SEC

    def test_register_and_lookup_performance(self) -> None:
        tm = u.TargetOracleWms.WMSTableManager()
        start = time.time()
        for i in range(c.TargetOracleWms.Tests.PERF_ITERATIONS):
            name = f"stream_{i}"
            tm.register_stream(name)
            tm.get_table_name(name)
        elapsed = time.time() - start
        assert elapsed < c.TargetOracleWms.Tests.PERF_THRESHOLD_SEC

    def test_map_stream_schema_performance(self) -> None:
        mapper = u.TargetOracleWms.WMSSchemaMapper()
        msg = _schema_msg()
        start = time.time()
        for _ in range(c.TargetOracleWms.Tests.PERF_ITERATIONS):
            mapper.map_stream_schema(msg)
        elapsed = time.time() - start
        assert elapsed < c.TargetOracleWms.Tests.PERF_THRESHOLD_SEC

    def test_add_and_get_stream_performance(self) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
        start = time.time()
        for i in range(c.TargetOracleWms.Tests.PERF_ITERATIONS):
            name = f"stream_{i}"
            mgr.add_stream(_schema_msg(name))
            mgr.get_stream(name)
        elapsed = time.time() - start
        assert elapsed < c.TargetOracleWms.Tests.PERF_THRESHOLD_SEC

    def test_transform_record_performance(self) -> None:
        transformer = u.TargetOracleWms.WMSDataTransformer()
        rec = _record_msg()
        schema = _schema_msg()
        start = time.time()
        for _ in range(c.TargetOracleWms.Tests.PERF_ITERATIONS):
            transformer.transform_record(rec, schema)
        elapsed = time.time() - start
        assert elapsed < c.TargetOracleWms.Tests.PERF_THRESHOLD_SEC
