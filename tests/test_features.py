"""Feature verification tests for target Oracle WMS.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import math
from collections.abc import Mapping, Sequence

from flext_target_oracle_wms import (
    FlextTargetOracleWmsUtilities,
    FlextTargetOracleWms,
    m,
    u,
)
from tests import t


def _valid_config() -> Mapping[str, t.ContainerValue]:
    return {
        "wms_auth": {
            "base_url": "https://test.wms.example.com",
            "username": "user",
            "password": "pass",
        }
    }


class TestTargetFeatures:
    """Verify core target features."""

    def test_target_initialization(self) -> None:
        target = FlextTargetOracleWms(_valid_config())
        assert target.name == "target-oracle-wms"

    def test_target_setup_cleanup_lifecycle(self) -> None:
        target = FlextTargetOracleWms(_valid_config())
        assert target.setup().is_success
        assert target.cleanup().is_success

    def test_target_process_empty_lines(self) -> None:
        target = FlextTargetOracleWms(_valid_config())
        assert target.process_lines([]).is_success


class TestTransformerFeatures:
    """Verify data transformation features."""

    def test_type_converter_handles_all_types(self) -> None:
        converter = u.TargetOracleWms.WMSTypeConverter()
        types_and_values: Sequence[tuple[str, bool | float | str]] = [
            ("string", "hello"),
            ("integer", 42),
            ("number", math.pi),
            ("boolean", True),
            ("object", '{"key": "val"}'),
            ("array", "[1, 2]"),
        ]
        for singer_type, value in types_and_values:
            result = converter.convert_singer_to_oracle(singer_type, value)
            assert result.is_success, f"Failed for type={singer_type}"

    def test_type_converter_null_handling(self) -> None:
        converter = u.TargetOracleWms.WMSTypeConverter()
        result = converter.convert_singer_to_oracle("string", "")
        assert result.is_success
        assert result.value == ""

    def test_transformer_uppercases_keys(self) -> None:
        transformer = u.TargetOracleWms.WMSDataTransformer()
        record = m.Meltano.SingerRecordMessage.model_validate({
            "type": "RECORD",
            "stream": "s",
            "record": {"name": "test"},
        })
        schema = m.Meltano.SingerSchemaMessage.model_validate({
            "type": "SCHEMA",
            "stream": "s",
            "schema": {
                "type": "object",
            },
            "key_properties": ["name"],
        })
        result = transformer.transform_record(record, schema)
        assert result.is_success
        assert result.value is not None
        assert "NAME" in result.value.record


class TestUtilitiesFeatures:
    """Verify utility helper features."""

    def test_create_schema_message(self) -> None:
        msg = FlextTargetOracleWmsUtilities.TargetOracleWms.create_schema_message(
            "test", {"type": "object"}
        )
        assert msg["type"] == "SCHEMA"
        assert msg["stream"] == "test"

    def test_create_record_message(self) -> None:
        msg = FlextTargetOracleWmsUtilities.TargetOracleWms.create_record_message(
            "test", {"id": "1"}
        )
        assert msg["type"] == "RECORD"
        assert msg["stream"] == "test"

    def test_create_state_message(self) -> None:
        msg = FlextTargetOracleWmsUtilities.TargetOracleWms.create_state_message({
            "pos": 42
        })
        assert msg["type"] == "STATE"
        assert msg["value"] == {"pos": 42}

    def test_validate_config_success(self) -> None:
        result = FlextTargetOracleWmsUtilities.TargetOracleWms.Validation.validate_wms_target_config({
            "base_url": "https://x",
            "username": "u",
            "password": "p",
        })
        assert result.is_success

    def test_validate_config_missing_fields(self) -> None:
        result = FlextTargetOracleWmsUtilities.TargetOracleWms.Validation.validate_wms_target_config({})
        assert result.is_failure
