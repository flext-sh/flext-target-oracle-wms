"""Tests for u.TargetOracleWms.CatalogManager.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from flext_tests import tm
from tests import c, m, u

if TYPE_CHECKING:
    from tests import t


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
        tm.ok(result)
        tm.that(result.value, eq=True)

    def test_add_stream_makes_stream_retrievable(self) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
        mgr.add_stream(_make_schema_message("inventory"))
        result = mgr.get_stream("inventory")
        tm.ok(result)

    def test_add_stream_overwrites_existing(self) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
        schema_v1 = _make_schema_message("s", key_properties=["id"])
        schema_v2 = _make_schema_message("s", key_properties=["id", "name"])
        mgr.add_stream(schema_v1)
        mgr.add_stream(schema_v2)
        result = mgr.get_stream("s")
        tm.ok(result)
        tm.that(result.value, none=False)
        entry = result.value
        tm.that(entry.key_properties, eq=["id", "name"])

    def test_get_nonexistent_stream_fails(self) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
        result = mgr.get_stream("nope")
        tm.fail(result)
        tm.that(result.error, none=False)
        tm.that(result.error, has="nope")

    def test_get_existing_stream_returns_catalog_entry(self) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
        mgr.add_stream(_make_schema_message("orders"))
        result = mgr.get_stream("orders")
        tm.ok(result)
        tm.that(result.value, none=False)
        entry = result.value
        tm.that(entry.stream, eq="orders")
        tm.that(entry.tap_stream_id, eq="orders")

    def test_entry_has_correct_key_properties(self) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
        mgr.add_stream(_make_schema_message("items", key_properties=["item_id", "lot"]))
        stream_result = mgr.get_stream("items")
        tm.ok(stream_result)
        tm.that(stream_result.value, none=False)
        entry = stream_result.value
        tm.that(entry.key_properties, eq=["item_id", "lot"])

    def test_multiple_independent_streams(self) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
        for name in ("alpha", "beta", "gamma"):
            mgr.add_stream(_make_schema_message(name))
        for name in ("alpha", "beta", "gamma"):
            tm.ok(mgr.get_stream(name))

    @pytest.mark.parametrize(
        "stream_name",
        ["simple", "with-dashes", "with_underscores", "CamelCase", "stream.dotted"],
    )
    def test_various_stream_names(self, stream_name: str) -> None:
        mgr = u.TargetOracleWms.CatalogManager()
        mgr.add_stream(_make_schema_message(stream_name))
        tm.ok(mgr.get_stream(stream_name))
