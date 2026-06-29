"""Tests for u.TargetOracleWms.CatalogManager.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import pytest

from tests.constants import c
from tests.models import m
from tests.typings import t
from tests.utilities import u


def _make_schema_message(
    stream_name: str = "test_stream",
    schema: t.JsonMapping | None = None,
    key_properties: t.StrSequence | None = None,
) -> m.Meltano.SingerSchemaMessage:
    """Build a valid SingerSchemaMessage dict."""
    return m.Meltano.SingerSchemaMessage(
        type=c.Meltano.SingerMessageType.SCHEMA,
        stream=stream_name,
        schema_definition=schema or {"type": "object"},
        key_properties=key_properties or ["id"],
    )


class TestsFlextTargetOracleWmsCatalog:
    def test_add_stream_returns_success(self) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
        result = mgr.add_stream(_make_schema_message())
        assert result.success
        assert result.value is True

    def test_add_stream_makes_stream_retrievable(self) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
        mgr.add_stream(_make_schema_message("inventory"))
        result = mgr.get_stream("inventory")
        assert result.success

    def test_add_stream_overwrites_existing(self) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
        schema_v1 = _make_schema_message("s", key_properties=["id"])
        schema_v2 = _make_schema_message("s", key_properties=["id", "name"])
        mgr.add_stream(schema_v1)
        mgr.add_stream(schema_v2)
        result = mgr.get_stream("s")
        assert result.success
        assert result.value is not None
        entry = result.value
        assert entry.key_properties == ["id", "name"]

    def test_get_nonexistent_stream_fails(self) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
        result = mgr.get_stream("nope")
        assert result.failure
        assert result.error is not None
        assert "nope" in result.error

    def test_get_existing_stream_returns_catalog_entry(self) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
        mgr.add_stream(_make_schema_message("orders"))
        result = mgr.get_stream("orders")
        assert result.success
        assert result.value is not None
        entry = result.value
        assert entry.stream == "orders"
        assert entry.tap_stream_id == "orders"

    def test_entry_has_correct_key_properties(self) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
        mgr.add_stream(_make_schema_message("items", key_properties=["item_id", "lot"]))
        stream_result = mgr.get_stream("items")
        assert stream_result.success
        assert stream_result.value is not None
        entry = stream_result.value
        assert entry.key_properties == ["item_id", "lot"]

    def test_multiple_independent_streams(self) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
        for name in ("alpha", "beta", "gamma"):
            mgr.add_stream(_make_schema_message(name))
        for name in ("alpha", "beta", "gamma"):
            assert mgr.get_stream(name).success

    @pytest.mark.parametrize(
        "stream_name",
        ["simple", "with-dashes", "with_underscores", "CamelCase", "stream.dotted"],
    )
    def test_various_stream_names(self, stream_name: str) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
        mgr.add_stream(_make_schema_message(stream_name))
        assert mgr.get_stream(stream_name).success
