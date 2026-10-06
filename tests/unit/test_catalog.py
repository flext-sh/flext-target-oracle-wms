"""Tests for u.TargetOracleWms.CatalogManager.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import pytest
from flext_tests import tm

from tests import m, u


class TestsFlextTargetOracleWmsCatalog:
    """Tests for u.TargetOracleWms.CatalogManager stream registration."""

    @staticmethod
    def test_add_stream_returns_success() -> None:
        """Test add stream returns success."""
        mgr = u.TargetOracleWms.CatalogManager()
        result = mgr.add_stream(
            m.Meltano.SingerSchemaMessage(
                stream="test_stream",
                schema={"type": "object"},
            ),
        )
        tm.ok(result)
        tm.that(result.value, eq=True)

    @staticmethod
    def test_add_stream_makes_stream_retrievable() -> None:
        """Test add stream makes stream retrievable."""
        mgr = u.TargetOracleWms.CatalogManager()
        mgr.add_stream(
            m.Meltano.SingerSchemaMessage(
                stream="inventory",
                schema={"type": "object"},
            ),
        )
        result = mgr.get_stream("inventory")
        tm.ok(result)

    @staticmethod
    def test_add_stream_overwrites_existing() -> None:
        """Test add stream overwrites existing."""
        mgr = u.TargetOracleWms.CatalogManager()
        schema_v1 = m.Meltano.SingerSchemaMessage(
            stream="s",
            schema={"type": "object"},
            key_properties=("id",),
        )
        schema_v2 = m.Meltano.SingerSchemaMessage(
            stream="s",
            schema={"type": "object"},
            key_properties=("id", "name"),
        )
        mgr.add_stream(schema_v1)
        mgr.add_stream(schema_v2)
        result = mgr.get_stream("s")
        tm.ok(result)
        tm.ok(result)
        entry = result.value
        tm.that(entry.key_properties, eq=("id", "name"))

    @staticmethod
    def test_get_nonexistent_stream_fails() -> None:
        """Test get nonexistent stream fails."""
        mgr = u.TargetOracleWms.CatalogManager()
        result = mgr.get_stream("nope")
        tm.fail(result)
        tm.that(result.error, has="nope")

    @staticmethod
    def test_get_existing_stream_returns_catalog_entry() -> None:
        """Test get existing stream returns catalog entry."""
        mgr = u.TargetOracleWms.CatalogManager()
        mgr.add_stream(
            m.Meltano.SingerSchemaMessage(stream="orders", schema={"type": "object"}),
        )
        result = mgr.get_stream("orders")
        tm.ok(result)
        tm.that(result.value, none=False)
        entry = result.value
        tm.that(entry.stream, eq="orders")
        tm.that(entry.tap_stream_id, eq="orders")

    @staticmethod
    def test_entry_has_correct_key_properties() -> None:
        """Test entry has correct key properties."""
        mgr = u.TargetOracleWms.CatalogManager()
        mgr.add_stream(
            m.Meltano.SingerSchemaMessage(
                stream="items",
                schema={"type": "object"},
                key_properties=("item_id", "lot"),
            ),
        )
        stream_result = mgr.get_stream("items")
        tm.ok(stream_result)
        tm.that(stream_result.value, none=False)
        entry = stream_result.value
        tm.that(entry.key_properties, eq=("item_id", "lot"))

    @staticmethod
    def test_multiple_independent_streams() -> None:
        """Test multiple independent streams."""
        mgr = u.TargetOracleWms.CatalogManager()
        for name in ("alpha", "beta", "gamma"):
            mgr.add_stream(
                m.Meltano.SingerSchemaMessage(stream=name, schema={"type": "object"}),
            )
        for name in ("alpha", "beta", "gamma"):
            tm.ok(mgr.get_stream(name))

    @staticmethod
    @pytest.mark.parametrize(
        "stream_name",
        ["simple", "with-dashes", "with_underscores", "CamelCase", "stream.dotted"],
    )
    def test_various_stream_names(stream_name: str) -> None:
        """Test various stream names."""
        mgr = u.TargetOracleWms.CatalogManager()
        mgr.add_stream(
            m.Meltano.SingerSchemaMessage(
                stream=stream_name,
                schema={"type": "object"},
            ),
        )
        tm.ok(mgr.get_stream(stream_name))
