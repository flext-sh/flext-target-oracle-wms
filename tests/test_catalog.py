"""Tests for SingerWMSCatalogManager.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import pytest

from flext_target_oracle_wms import m
from flext_target_oracle_wms.target_client import SingerWMSCatalogManager
from tests import t


def _make_schema_message(
    stream_name: str = "test_stream",
    schema: dict[str, t.NormalizedValue] | None = None,
    key_properties: list[str] | None = None,
) -> m.Meltano.SingerSchemaMessage:
    """Build a valid SingerSchemaMessage dict."""
    return m.Meltano.SingerSchemaMessage.model_validate({
        "type": "SCHEMA",
        "stream": stream_name,
        "schema": schema
        or {"type": "t.NormalizedValue", "properties": {"id": {"type": "string"}}},
        "key_properties": key_properties or ["id"],
    })


class TestCatalogAddStream:
    """Tests for SingerWMSCatalogManager.add_stream."""

    def test_add_stream_returns_success(self) -> None:
        mgr = SingerWMSCatalogManager()
        result = mgr.add_stream(_make_schema_message())
        assert result.is_success
        assert result.value is True

    def test_add_stream_makes_stream_retrievable(self) -> None:
        mgr = SingerWMSCatalogManager()
        mgr.add_stream(_make_schema_message("inventory"))
        result = mgr.get_stream("inventory")
        assert result.is_success

    def test_add_stream_overwrites_existing(self) -> None:
        mgr = SingerWMSCatalogManager()
        schema_v1 = _make_schema_message("s", key_properties=["id"])
        schema_v2 = _make_schema_message("s", key_properties=["id", "name"])
        mgr.add_stream(schema_v1)
        mgr.add_stream(schema_v2)
        result = mgr.get_stream("s")
        assert result.is_success
        assert result.value is not None
        entry = result.value
        assert entry.key_properties == ["id", "name"]


class TestCatalogGetStream:
    """Tests for SingerWMSCatalogManager.get_stream."""

    def test_get_nonexistent_stream_fails(self) -> None:
        mgr = SingerWMSCatalogManager()
        result = mgr.get_stream("nope")
        assert result.is_failure
        assert result.error is not None
        assert "nope" in result.error

    def test_get_existing_stream_returns_catalog_entry(self) -> None:
        mgr = SingerWMSCatalogManager()
        mgr.add_stream(_make_schema_message("orders"))
        result = mgr.get_stream("orders")
        assert result.is_success
        assert result.value is not None
        entry = result.value
        assert entry.stream == "orders"
        assert entry.tap_stream_id == "orders"

    def test_entry_has_correct_key_properties(self) -> None:
        mgr = SingerWMSCatalogManager()
        mgr.add_stream(_make_schema_message("items", key_properties=["item_id", "lot"]))
        stream_result = mgr.get_stream("items")
        assert stream_result.is_success
        assert stream_result.value is not None
        entry = stream_result.value
        assert entry.key_properties == ["item_id", "lot"]


class TestCatalogMultipleStreams:
    """Tests for managing multiple streams."""

    def test_multiple_independent_streams(self) -> None:
        mgr = SingerWMSCatalogManager()
        for name in ("alpha", "beta", "gamma"):
            mgr.add_stream(_make_schema_message(name))
        for name in ("alpha", "beta", "gamma"):
            assert mgr.get_stream(name).is_success

    @pytest.mark.parametrize(
        "stream_name",
        ["simple", "with-dashes", "with_underscores", "CamelCase", "stream.dotted"],
    )
    def test_various_stream_names(self, stream_name: str) -> None:
        mgr = SingerWMSCatalogManager()
        mgr.add_stream(_make_schema_message(stream_name))
        assert mgr.get_stream(stream_name).is_success
