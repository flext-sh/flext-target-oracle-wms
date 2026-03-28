"""Performance benchmarks for target Oracle WMS components.

Uses time.time() for measurement (pytest-benchmark is unavailable).

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import time
from unittest.mock import MagicMock, patch

from flext_target_oracle_wms import m, u
from flext_target_oracle_wms._utilities.client import (
    CatalogManager as FlextTargetOracleWmsCatalogManager,
)
from flext_target_oracle_wms.factory import FlextTargetFactory, create_oracle_wms_target

PERF_ITERATIONS = 500
PERF_THRESHOLD_SEC = 5.0


def _schema_msg(stream: str = "bench") -> m.Meltano.SingerSchemaMessage:
    return m.Meltano.SingerSchemaMessage.model_validate({
        "type": "SCHEMA",
        "stream": stream,
        "schema": {
            "type": "object",
        },
        "key_properties": ["id"],
    })


def _record_msg(stream: str = "bench") -> m.Meltano.SingerRecordMessage:
    return m.Meltano.SingerRecordMessage.model_validate({
        "type": "RECORD",
        "stream": stream,
        "record": {"id": "1", "qty": 100},
    })


class TestTypeConverterBenchmarks:
    """Performance tests for WMSTypeConverter."""

    def test_convert_string_performance(self) -> None:
        converter = u.TargetOracleWms.WMSTypeConverter()
        start = time.time()
        for _ in range(PERF_ITERATIONS):
            converter.convert_singer_to_oracle("string", "hello")
        elapsed = time.time() - start
        assert elapsed < PERF_THRESHOLD_SEC

    def test_convert_integer_performance(self) -> None:
        converter = u.TargetOracleWms.WMSTypeConverter()
        start = time.time()
        for _ in range(PERF_ITERATIONS):
            converter.convert_singer_to_oracle("integer", 42)
        elapsed = time.time() - start
        assert elapsed < PERF_THRESHOLD_SEC


class TestTableManagerBenchmarks:
    """Performance tests for WMSTableManager."""

    def test_register_and_lookup_performance(self) -> None:
        tm = u.TargetOracleWms.WMSTableManager()
        start = time.time()
        for i in range(PERF_ITERATIONS):
            name = f"stream_{i}"
            tm.register_stream(name)
            tm.get_table_name(name)
        elapsed = time.time() - start
        assert elapsed < PERF_THRESHOLD_SEC


class TestSchemaMapperBenchmarks:
    """Performance tests for WMSSchemaMapper."""

    def test_map_stream_schema_performance(self) -> None:
        mapper = u.TargetOracleWms.WMSSchemaMapper()
        msg = _schema_msg()
        start = time.time()
        for _ in range(PERF_ITERATIONS):
            mapper.map_stream_schema(msg)
        elapsed = time.time() - start
        assert elapsed < PERF_THRESHOLD_SEC


class TestCatalogBenchmarks:
    """Performance tests for FlextTargetOracleWmsCatalogManager."""

    def test_add_and_get_stream_performance(self) -> None:
        mgr = FlextTargetOracleWmsCatalogManager()
        start = time.time()
        for i in range(PERF_ITERATIONS):
            name = f"stream_{i}"
            mgr.add_stream(_schema_msg(name))
            mgr.get_stream(name)
        elapsed = time.time() - start
        assert elapsed < PERF_THRESHOLD_SEC


class TestFactoryBenchmarks:
    """Performance tests for FlextTargetFactory."""

    @patch("flext_target_oracle_wms.factory.FlextTargetOracleWms")
    def test_create_target_performance(self, mock_target: MagicMock) -> None:
        start = time.time()
        for _ in range(PERF_ITERATIONS):
            req = m.TargetOracleWms.TargetCreationRequest(
                base_url="https://bench.example.com",
                username="u",
                password="p",
                additional_config=None,
            )
            FlextTargetFactory.create_target(req)
        elapsed = time.time() - start
        assert elapsed < PERF_THRESHOLD_SEC

    @patch("flext_target_oracle_wms.factory.FlextTargetOracleWms")
    def test_convenience_function_performance(self, mock_target: MagicMock) -> None:
        start = time.time()
        for _ in range(PERF_ITERATIONS):
            create_oracle_wms_target(
                base_url="https://bench.example.com",
                username="u",
                password="p",
            )
        elapsed = time.time() - start
        assert elapsed < PERF_THRESHOLD_SEC


class TestDataTransformerBenchmarks:
    """Performance tests for WMSDataTransformer."""

    def test_transform_record_performance(self) -> None:
        transformer = u.TargetOracleWms.WMSDataTransformer()
        rec = _record_msg()
        schema = _schema_msg()
        start = time.time()
        for _ in range(PERF_ITERATIONS):
            transformer.transform_record(rec, schema)
        elapsed = time.time() - start
        assert elapsed < PERF_THRESHOLD_SEC
