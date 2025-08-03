"""Comprehensive tests for Singer WMS Catalog Manager - REAL flext-core integration."""

from __future__ import annotations

import pytest

# DRY: Import from REAL implementation - NO DUPLICATION
from flext_core import FlextResult

from flext_target_oracle_wms.singer.catalog import (
    SingerWMSCatalogEntry,
    SingerWMSCatalogManager,
)


class TestSingerWMSCatalogEntry:
    """Test Singer WMS Catalog Entry validation and domain rules."""

    def test_catalog_entry_valid_creation(self) -> None:
        """Test creating a valid catalog entry."""
        entry = SingerWMSCatalogEntry(
            tap_stream_id="test_stream",
            stream="test_stream",
            schema_info={"type": "object", "properties": {"id": {"type": "string"}}},
            metadata=[{"breadcrumb": [], "metadata": {"inclusion": "available"}}],
            key_properties=["id"],
        )

        validation_result = entry.validate_domain_rules()
        assert validation_result.is_success
        assert validation_result.error is None

    def test_catalog_entry_empty_tap_stream_id(self) -> None:
        """Test catalog entry validation with empty tap_stream_id."""
        entry = SingerWMSCatalogEntry(
            tap_stream_id="",  # Empty
            stream="test_stream",
            schema_info={"type": "object"},
        )

        validation_result = entry.validate_domain_rules()
        assert not validation_result.is_success
        assert validation_result.error is not None
        assert "tap_stream_id cannot be empty" in validation_result.error

    def test_catalog_entry_whitespace_tap_stream_id(self) -> None:
        """Test catalog entry validation with whitespace-only tap_stream_id."""
        entry = SingerWMSCatalogEntry(
            tap_stream_id="   ",  # Whitespace only
            stream="test_stream",
            schema_info={"type": "object"},
        )

        validation_result = entry.validate_domain_rules()
        assert not validation_result.is_success
        assert validation_result.error is not None
        assert "tap_stream_id cannot be empty" in validation_result.error

    def test_catalog_entry_empty_stream(self) -> None:
        """Test catalog entry validation with empty stream."""
        entry = SingerWMSCatalogEntry(
            tap_stream_id="test_stream",
            stream="",  # Empty
            schema_info={"type": "object"},
        )

        validation_result = entry.validate_domain_rules()
        assert not validation_result.is_success
        assert validation_result.error is not None
        assert "stream cannot be empty" in validation_result.error

    def test_catalog_entry_empty_schema_info(self) -> None:
        """Test catalog entry validation with empty schema_info."""
        entry = SingerWMSCatalogEntry(
            tap_stream_id="test_stream",
            stream="test_stream",
            schema_info={},  # Empty dict
        )

        validation_result = entry.validate_domain_rules()
        assert not validation_result.is_success
        assert validation_result.error is not None
        assert "schema_info cannot be empty" in validation_result.error

    def test_catalog_entry_default_values(self) -> None:
        """Test catalog entry uses correct default values."""
        entry = SingerWMSCatalogEntry(
            tap_stream_id="test_stream",
            stream="test_stream",
            schema_info={"type": "object"},
        )

        # Test default values
        assert entry.metadata == []
        assert entry.key_properties == []
        assert entry.bookmark_properties == []
        assert entry.replication_method == "FULL_TABLE"
        assert entry.replication_key is None

        # Should still validate successfully
        validation_result = entry.validate_domain_rules()
        assert validation_result.is_success


class TestSingerWMSCatalogManager:
    """Test Singer WMS Catalog Manager with comprehensive coverage."""

    def test_catalog_manager_initialization(self) -> None:
        """Test Singer WMS catalog manager initialization."""
        manager = SingerWMSCatalogManager()
        assert manager is not None

    def test_add_stream_basic(self) -> None:
        """Test adding a basic stream to catalog."""
        manager = SingerWMSCatalogManager()
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
            },
        }

        result = manager.add_stream("test_stream", schema)
        assert result.is_success
        assert result.error is None

    def test_add_stream_with_complex_schema(self) -> None:
        """Test adding stream with complex schema."""
        manager = SingerWMSCatalogManager()
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "created_at": {"type": "string", "format": "date-time"},
                "is_active": {"type": "boolean"},
                "metadata": {"type": "object"},
                "tags": {"type": "array"},
                "price": {"type": "number"},
            },
        }

        result = manager.add_stream("complex_stream", schema)
        assert result.is_success
        assert result.error is None

    def test_add_duplicate_stream(self) -> None:
        """Test adding duplicate stream overwrites existing."""
        manager = SingerWMSCatalogManager()
        schema1 = {"type": "object", "properties": {"id": {"type": "integer"}}}
        schema2 = {"type": "object", "properties": {"id": {"type": "string"}}}

        # Add first stream
        result1 = manager.add_stream("duplicate_stream", schema1)
        assert result1.is_success

        # Add same stream with different schema (should overwrite)
        result2 = manager.add_stream("duplicate_stream", schema2)
        assert result2.is_success

        # Verify the schema was updated
        get_result = manager.get_stream("duplicate_stream")
        assert get_result.is_success
        entry = get_result.data
        assert entry is not None
        assert entry.schema_info == schema2

    def test_get_stream_existing(self) -> None:
        """Test getting existing stream from catalog."""
        manager = SingerWMSCatalogManager()
        schema = {"type": "object", "properties": {"id": {"type": "integer"}}}

        # Add stream first
        manager.add_stream("test_stream", schema)

        # Get stream
        result = manager.get_stream("test_stream")
        assert result.is_success

        entry = result.data
        assert entry is not None
        assert entry.stream == "test_stream"
        assert entry.schema_info == schema

    def test_get_stream_nonexistent(self) -> None:
        """Test getting non-existent stream returns error."""
        manager = SingerWMSCatalogManager()

        result = manager.get_stream("nonexistent_stream")
        assert not result.is_success
        assert result.error is not None
        assert "not found" in result.error.lower()

    def test_list_streams_empty(self) -> None:
        """Test listing streams when catalog is empty."""
        manager = SingerWMSCatalogManager()

        result = manager.list_streams()
        assert result.is_success
        streams = result.data
        assert streams is not None
        assert len(streams) == 0

    def test_list_streams_with_streams(self) -> None:
        """Test listing streams when catalog has streams."""
        manager = SingerWMSCatalogManager()
        schema = {"type": "object", "properties": {"id": {"type": "integer"}}}

        # Add multiple streams
        stream_names = ["stream1", "stream2", "stream3"]
        for stream_name in stream_names:
            manager.add_stream(stream_name, schema)

        # List streams
        result = manager.list_streams()
        assert result.is_success

        streams = result.data
        assert streams is not None
        assert len(streams) == 3
        assert set(streams) == set(stream_names)

    def test_remove_stream_existing(self) -> None:
        """Test removing existing stream from catalog."""
        manager = SingerWMSCatalogManager()
        schema = {"type": "object", "properties": {"id": {"type": "integer"}}}

        # Add stream first
        manager.add_stream("test_stream", schema)

        # Verify stream exists
        get_result = manager.get_stream("test_stream")
        assert get_result.is_success

        # Remove stream
        remove_result = manager.remove_stream("test_stream")
        assert remove_result.is_success

        # Verify stream is gone
        get_result_after = manager.get_stream("test_stream")
        assert not get_result_after.is_success

    def test_remove_stream_nonexistent(self) -> None:
        """Test removing non-existent stream succeeds (idempotent)."""
        manager = SingerWMSCatalogManager()

        result = manager.remove_stream("nonexistent_stream")
        assert result.is_success  # Should succeed even if stream doesn't exist

    def test_catalog_entry_properties(self) -> None:
        """Test catalog entry properties are correctly set."""
        manager = SingerWMSCatalogManager()
        schema = {
            "type": "object",
            "properties": {"id": {"type": "integer"}, "name": {"type": "string"}},
        }
        metadata = [{"breadcrumb": [], "metadata": {"inclusion": "available"}}]

        # Add stream with metadata
        result = manager.add_stream("property_test", schema, metadata)
        assert result.is_success

        # Get stream and verify properties
        get_result = manager.get_stream("property_test")
        assert get_result.is_success

        entry = get_result.data
        assert entry is not None
        assert entry.tap_stream_id == "property_test"
        assert entry.stream == "property_test"
        assert entry.schema_info == schema
        assert entry.metadata == metadata
        assert entry.replication_method == "FULL_TABLE"  # Default value
        assert entry.replication_key is None  # Default value

    def test_multiple_operations_workflow(self) -> None:
        """Test complete workflow with multiple operations."""
        manager = SingerWMSCatalogManager()

        # Add multiple streams
        for i in range(3):
            schema = {
                "type": "object",
                "properties": {f"field_{i}": {"type": "string"}},
            }
            result = manager.add_stream(f"stream_{i}", schema)
            assert result.is_success

        # List all streams
        list_result = manager.list_streams()
        assert list_result.is_success
        assert len(list_result.data or []) == 3

        # Remove one stream
        remove_result = manager.remove_stream("stream_1")
        assert remove_result.is_success

        # Verify count decreased
        list_result_after = manager.list_streams()
        assert list_result_after.is_success
        assert len(list_result_after.data or []) == 2

        # Verify removed stream is gone
        get_result = manager.get_stream("stream_1")
        assert not get_result.is_success

        # Verify other streams still exist
        get_result_0 = manager.get_stream("stream_0")
        assert get_result_0.is_success

        get_result_2 = manager.get_stream("stream_2")
        assert get_result_2.is_success

    def test_catalog_manager_isolation(self) -> None:
        """Test that different catalog manager instances are isolated."""
        manager1 = SingerWMSCatalogManager()
        manager2 = SingerWMSCatalogManager()

        schema = {"type": "object", "properties": {"id": {"type": "integer"}}}

        # Add stream to first manager
        manager1.add_stream("isolated_stream", schema)

        # Verify stream doesn't exist in second manager
        result1 = manager1.get_stream("isolated_stream")
        assert result1.is_success

        result2 = manager2.get_stream("isolated_stream")
        assert not result2.is_success

    def test_catalog_entry_validation_with_edge_cases(self) -> None:
        """Test catalog entry validation with edge cases."""
        # Test entry with very long strings to potentially trigger edge cases
        entry = SingerWMSCatalogEntry(
            tap_stream_id="test_stream",
            stream="test_stream",
            schema_info={"type": "object", "properties": {}},
        )

        validation_result = entry.validate_domain_rules()
        assert validation_result.is_success  # Should pass with valid data

    def test_add_stream_exception_handling(self) -> None:
        """Test add_stream exception handling."""
        from unittest.mock import patch

        manager = SingerWMSCatalogManager()

        # Use proper mock to simulate catalog entry creation failure - SOLID DRY pattern
        with patch(
            "flext_target_oracle_wms.singer.catalog.SingerWMSCatalogEntry",
        ) as mock_entry:
            mock_entry.side_effect = RuntimeError("Catalog entry creation failed")
            result = manager.add_stream("test_stream", {"type": "object"})

        assert not result.is_success
        assert result.error is not None
        assert "Stream addition failed" in result.error

    def test_list_streams_exception_handling(self) -> None:
        """Test list_streams exception handling."""
        from unittest.mock import patch

        manager = SingerWMSCatalogManager()

        # Use proper mock to simulate catalog entries access failure - SOLID pattern
        with patch.object(manager, "_catalog_entries") as mock_entries:
            mock_entries.keys.side_effect = RuntimeError("keys() failed")
            result = manager.list_streams()

        assert not result.is_success
        assert result.error is not None
        assert "Stream listing failed" in result.error

    def test_remove_stream_exception_handling(self) -> None:
        """Test remove_stream exception handling."""
        from unittest.mock import MagicMock, patch

        manager = SingerWMSCatalogManager()

        # Use proper mock to simulate dict deletion failure - SOLID pattern
        mock_entries = MagicMock()
        mock_entries.__contains__.return_value = True
        mock_entries.__delitem__.side_effect = RuntimeError("__delitem__ failed")

        with patch.object(manager, "_catalog_entries", mock_entries):
            result = manager.remove_stream("test_stream")

        assert not result.is_success
        assert result.error is not None
        assert "Stream removal failed" in result.error

    def test_get_schema_for_stream_functionality(self) -> None:
        """Test get_schema_for_stream functionality."""
        manager = SingerWMSCatalogManager()
        schema = {
            "type": "object",
            "properties": {"id": {"type": "integer"}, "name": {"type": "string"}},
        }

        # Add stream first
        manager.add_stream("test_stream", schema)

        # Test successful retrieval (lines 107-114)
        result = manager.get_schema_for_stream("test_stream")
        assert result.is_success
        assert result.data == schema

        # Test non-existent stream
        result = manager.get_schema_for_stream("nonexistent_stream")
        assert not result.is_success
        assert result.error is not None
        assert "not found" in result.error.lower()

    def test_get_schema_for_stream_none_entry(self) -> None:
        """Test get_schema_for_stream when stream entry is None."""
        manager = SingerWMSCatalogManager()

        # Use pytest.MonkeyPatch instead of direct assignment - DRY REAL
        import pytest

        def mock_get_stream(
            stream_name: str,
        ) -> FlextResult[SingerWMSCatalogEntry | None]:
            return FlextResult.ok(None)

        # Use monkeypatch for proper type safety - REAL DRY approach
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr(manager, "get_stream", mock_get_stream)

            result = manager.get_schema_for_stream("test_stream")
            assert not result.is_success
            assert result.error is not None
            assert "Stream entry is None" in result.error

    def test_get_key_properties_functionality(self) -> None:
        """Test get_key_properties functionality."""
        manager = SingerWMSCatalogManager()
        schema = {"type": "object", "properties": {"id": {"type": "integer"}}}
        metadata = [{"breadcrumb": [], "metadata": {"inclusion": "available"}}]

        # Add stream with key properties (lines 118-125)
        add_result = manager.add_stream("test_stream", schema, metadata)
        assert add_result.is_success

        # Test successful retrieval
        result = manager.get_key_properties("test_stream")
        assert result.is_success
        assert isinstance(result.data, list)

        # Test non-existent stream
        result = manager.get_key_properties("nonexistent_stream")
        assert not result.is_success
        assert result.error is not None
        assert "not found" in result.error.lower()

    def test_get_key_properties_none_entry(self) -> None:
        """Test get_key_properties when stream entry is None."""
        manager = SingerWMSCatalogManager()

        # Use pytest.MonkeyPatch for proper typing - REAL DRY
        def mock_get_stream(
            stream_name: str,
        ) -> FlextResult[SingerWMSCatalogEntry | None]:
            return FlextResult.ok(None)

        # Use monkeypatch for proper type safety - REAL DRY approach
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr(manager, "get_stream", mock_get_stream)

            result = manager.get_key_properties("test_stream")
            assert not result.is_success
            assert result.error is not None
            assert "Stream entry is None" in result.error

    def test_update_stream_metadata_functionality(self) -> None:
        """Test update_stream_metadata functionality."""
        manager = SingerWMSCatalogManager()
        schema = {"type": "object", "properties": {"id": {"type": "integer"}}}

        # Add stream first
        manager.add_stream("test_stream", schema)

        # Test successful metadata update (lines 133-156)
        new_metadata = [{"breadcrumb": [], "metadata": {"inclusion": "automatic"}}]
        result = manager.update_stream_metadata("test_stream", new_metadata)
        assert result.is_success

        # Verify metadata was updated
        get_result = manager.get_stream("test_stream")
        assert get_result.is_success
        entry = get_result.data
        assert entry is not None
        assert entry.metadata == new_metadata

        # Test non-existent stream
        result = manager.update_stream_metadata("nonexistent_stream", new_metadata)
        assert not result.is_success
        assert result.error is not None
        assert "not found" in result.error.lower()

    def test_update_stream_metadata_exception_handling(self) -> None:
        """Test update_stream_metadata exception handling."""
        from unittest.mock import patch

        manager = SingerWMSCatalogManager()

        # Add a stream first so it exists
        schema = {"type": "object", "properties": {"id": {"type": "integer"}}}
        manager.add_stream("test_stream", schema)

        # Use proper mock to simulate metadata processing failure - SOLID pattern
        with patch.object(manager, "_validate_metadata") as mock_validate:
            mock_validate.side_effect = RuntimeError("Metadata validation failed")
            result = manager.update_stream_metadata(
                "test_stream",
                [{"metadata": "test"}],
            )

        assert not result.is_success
        assert result.error is not None
        assert "Metadata update failed" in result.error

    def test_to_singer_catalog_functionality(self) -> None:
        """Test to_singer_catalog functionality."""
        manager = SingerWMSCatalogManager()

        # Test empty catalog (lines 160-191)
        result = manager.to_singer_catalog()
        assert result.is_success
        assert result.data is not None
        catalog = result.data
        assert "streams" in catalog
        assert catalog["streams"] == []

        # Add streams and test conversion
        schema1 = {"type": "object", "properties": {"id": {"type": "integer"}}}
        schema2 = {"type": "object", "properties": {"name": {"type": "string"}}}

        manager.add_stream("stream1", schema1)
        manager.add_stream("stream2", schema2)

        result = manager.to_singer_catalog()
        assert result.is_success
        assert result.data is not None
        catalog = result.data
        assert len(catalog["streams"]) == 2

        # Verify stream structures
        stream_names = [s["stream"] for s in catalog["streams"]]
        assert "stream1" in stream_names
        assert "stream2" in stream_names

    def test_to_singer_catalog_exception_handling(self) -> None:
        """Test to_singer_catalog exception handling."""
        from unittest.mock import patch

        manager = SingerWMSCatalogManager()

        # Use proper mock to simulate catalog entries access failure - SOLID pattern
        with patch.object(manager, "_catalog_entries") as mock_entries:
            mock_entries.values.side_effect = RuntimeError("values() failed")
            result = manager.to_singer_catalog()

        assert not result.is_success
        assert result.error is not None
        assert "Catalog conversion failed" in result.error

    def test_load_from_singer_catalog_functionality(self) -> None:
        """Test load_from_singer_catalog functionality."""
        manager = SingerWMSCatalogManager()

        # Test loading valid catalog (lines 195-224)
        catalog = {
            "streams": [
                {
                    "tap_stream_id": "test_stream1",
                    "stream": "test_stream1",
                    "schema": {
                        "type": "object",
                        "properties": {"id": {"type": "integer"}},
                    },
                    "metadata": [
                        {"breadcrumb": [], "metadata": {"inclusion": "available"}},
                    ],
                    "key_properties": ["id"],
                    "bookmark_properties": ["updated_at"],
                    "replication_method": "INCREMENTAL",
                    "replication_key": "updated_at",
                },
                {
                    "tap_stream_id": "test_stream2",
                    "stream": "test_stream2",
                    "schema": {
                        "type": "object",
                        "properties": {"name": {"type": "string"}},
                    },
                    # Missing optional fields to test defaults
                },
            ],
        }

        result = manager.load_from_singer_catalog(catalog)
        assert result.is_success

        # Verify streams were loaded
        list_result = manager.list_streams()
        assert list_result.is_success
        streams = list_result.data
        assert streams is not None
        assert len(streams) == 2
        assert "test_stream1" in streams
        assert "test_stream2" in streams

        # Verify stream1 properties
        get_result = manager.get_stream("test_stream1")
        assert get_result.is_success
        entry1 = get_result.data
        assert entry1 is not None
        assert entry1.replication_method == "INCREMENTAL"
        assert entry1.replication_key == "updated_at"
        assert entry1.key_properties == ["id"]

        # Verify stream2 defaults
        get_result = manager.get_stream("test_stream2")
        assert get_result.is_success
        entry2 = get_result.data
        assert entry2 is not None
        assert entry2.replication_method == "FULL_TABLE"  # Default
        assert entry2.replication_key is None  # Default
        assert entry2.key_properties == []  # Default

    def test_load_from_singer_catalog_exception_handling(self) -> None:
        """Test load_from_singer_catalog exception handling."""
        from unittest.mock import MagicMock

        manager = SingerWMSCatalogManager()

        # Use proper mock to simulate catalog access failure - SOLID pattern
        bad_catalog = MagicMock()
        bad_catalog.get.side_effect = RuntimeError("get() failed")

        result = manager.load_from_singer_catalog(bad_catalog)
        assert not result.is_success
        assert result.error is not None
        assert "Catalog loading failed" in result.error

    def test_load_from_singer_catalog_missing_streams(self) -> None:
        """Test load_from_singer_catalog with missing streams key."""
        manager = SingerWMSCatalogManager()

        # Test catalog without streams key
        catalog: dict[str, object] = {}
        result = manager.load_from_singer_catalog(catalog)
        assert result.is_success  # Should succeed with empty streams

        # Verify no streams were loaded
        list_result = manager.list_streams()
        assert list_result.is_success
        streams = list_result.data
        assert streams is not None
        assert len(streams) == 0
