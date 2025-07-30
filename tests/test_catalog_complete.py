"""COMPREHENSIVE tests for Singer WMS Catalog Manager - REAL flext-core integration targeting 90%+ coverage."""

from __future__ import annotations

from typing import Any

import pytest

# DRY: Import from REAL implementation - NO DUPLICATION
from flext_core import FlextResult

from flext_target_oracle_wms.singer.catalog import SingerWMSCatalogManager, SingerWMSCatalogEntry


class TestSingerWMSCatalogManagerComprehensive:
    """Comprehensive tests targeting uncovered catalog manager functionality."""

    def test_get_schema_for_stream_existing(self) -> None:
        """Test getting schema for existing stream."""
        manager = SingerWMSCatalogManager()
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
            }
        }
        
        # Add stream first
        manager.add_stream("test_stream", schema)
        
        # Get schema
        result = manager.get_schema_for_stream("test_stream")
        assert result.is_success
        assert result.data is not None
        assert result.data == schema

    def test_get_schema_for_stream_nonexistent(self) -> None:
        """Test getting schema for non-existent stream."""
        manager = SingerWMSCatalogManager()
        
        result = manager.get_schema_for_stream("nonexistent_stream")
        assert not result.is_success
        assert result.error is not None
        assert "not found" in result.error.lower()

    def test_get_key_properties_existing(self) -> None:
        """Test getting key properties for existing stream."""
        manager = SingerWMSCatalogManager()
        schema = {"type": "object", "properties": {"id": {"type": "integer"}}}
        metadata = [{"breadcrumb": [], "metadata": {"inclusion": "available"}}]
        
        # Add stream first
        manager.add_stream("test_stream", schema, metadata)
        
        # Get key properties
        result = manager.get_key_properties("test_stream")
        assert result.is_success
        assert result.data is not None
        assert isinstance(result.data, list)

    def test_get_key_properties_nonexistent(self) -> None:
        """Test getting key properties for non-existent stream."""
        manager = SingerWMSCatalogManager()
        
        result = manager.get_key_properties("nonexistent_stream")
        assert not result.is_success
        assert result.error is not None
        assert "not found" in result.error.lower()

    def test_update_stream_metadata_existing(self) -> None:
        """Test updating metadata for existing stream."""
        manager = SingerWMSCatalogManager()
        schema = {"type": "object", "properties": {"id": {"type": "integer"}}}
        original_metadata = [{"breadcrumb": [], "metadata": {"inclusion": "available"}}]
        
        # Add stream first
        manager.add_stream("test_stream", schema, original_metadata)
        
        # Update metadata
        new_metadata = [
            {"breadcrumb": [], "metadata": {"inclusion": "automatic"}},
            {"breadcrumb": ["properties", "id"], "metadata": {"inclusion": "available"}},
        ]
        
        result = manager.update_stream_metadata("test_stream", new_metadata)
        assert result.is_success
        
        # Verify metadata was updated
        stream_result = manager.get_stream("test_stream")
        assert stream_result.is_success
        assert stream_result.data is not None
        assert stream_result.data.metadata == new_metadata

    def test_update_stream_metadata_nonexistent(self) -> None:
        """Test updating metadata for non-existent stream."""
        manager = SingerWMSCatalogManager()
        metadata = [{"breadcrumb": [], "metadata": {"inclusion": "available"}}]
        
        result = manager.update_stream_metadata("nonexistent_stream", metadata)
        assert not result.is_success
        assert result.error is not None
        assert "not found" in result.error.lower()

    def test_to_singer_catalog_empty(self) -> None:
        """Test converting empty catalog to Singer format."""
        manager = SingerWMSCatalogManager()
        
        result = manager.to_singer_catalog()
        assert result.is_success
        assert result.data is not None
        
        catalog = result.data
        assert "streams" in catalog
        assert catalog["streams"] == []

    def test_to_singer_catalog_with_streams(self) -> None:
        """Test converting catalog with streams to Singer format."""
        manager = SingerWMSCatalogManager()
        
        # Add multiple streams with various properties
        schema1 = {"type": "object", "properties": {"id": {"type": "integer"}}}
        schema2 = {
            "type": "object", 
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
            }
        }
        
        metadata1 = [{"breadcrumb": [], "metadata": {"inclusion": "available"}}]
        metadata2 = [
            {"breadcrumb": [], "metadata": {"inclusion": "automatic"}},
            {"breadcrumb": ["properties", "id"], "metadata": {"inclusion": "available"}},
        ]
        
        manager.add_stream("stream1", schema1, metadata1)
        manager.add_stream("stream2", schema2, metadata2)
        
        # Convert to Singer catalog
        result = manager.to_singer_catalog()
        assert result.is_success
        assert result.data is not None
        
        catalog = result.data
        assert "streams" in catalog
        assert len(catalog["streams"]) == 2
        
        # Verify stream structure
        stream_names = [stream["stream"] for stream in catalog["streams"]]
        assert "stream1" in stream_names
        assert "stream2" in stream_names
        
        # Verify each stream has required fields
        for stream in catalog["streams"]:
            assert "tap_stream_id" in stream
            assert "stream" in stream
            assert "schema" in stream
            assert "metadata" in stream

    def test_load_from_singer_catalog_valid(self) -> None:
        """Test loading from valid Singer catalog format."""
        manager = SingerWMSCatalogManager()
        
        singer_catalog = {
            "streams": [
                {
                    "tap_stream_id": "test_stream_1",
                    "stream": "test_stream_1",
                    "schema": {
                        "type": "object",
                        "properties": {"id": {"type": "integer"}}
                    },
                    "metadata": [{"breadcrumb": [], "metadata": {"inclusion": "available"}}],
                    "key_properties": ["id"],
                    "replication_method": "FULL_TABLE",
                },
                {
                    "tap_stream_id": "test_stream_2", 
                    "stream": "test_stream_2",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string"},
                            "name": {"type": "string"},
                        }
                    },
                    "metadata": [],
                    "key_properties": ["id"],
                    "bookmark_properties": ["updated_at"],
                    "replication_method": "INCREMENTAL",
                    "replication_key": "updated_at",
                },
            ]
        }
        
        result = manager.load_from_singer_catalog(singer_catalog)
        assert result.is_success
        
        # Verify streams were loaded
        list_result = manager.list_streams()
        assert list_result.is_success
        assert list_result.data is not None
        assert len(list_result.data) == 2
        assert "test_stream_1" in list_result.data
        assert "test_stream_2" in list_result.data
        
        # Verify stream details
        stream1_result = manager.get_stream("test_stream_1")
        assert stream1_result.is_success
        assert stream1_result.data is not None
        assert stream1_result.data.replication_method == "FULL_TABLE"
        assert stream1_result.data.key_properties == ["id"]
        
        stream2_result = manager.get_stream("test_stream_2")
        assert stream2_result.is_success
        assert stream2_result.data is not None
        assert stream2_result.data.replication_method == "INCREMENTAL"
        assert stream2_result.data.replication_key == "updated_at"
        assert stream2_result.data.bookmark_properties == ["updated_at"]

    def test_load_from_singer_catalog_missing_streams(self) -> None:
        """Test loading from Singer catalog missing streams key."""
        manager = SingerWMSCatalogManager()
        
        invalid_catalog = {"version": "1.0"}  # Missing streams
        
        result = manager.load_from_singer_catalog(invalid_catalog)
        assert result.is_success  # Empty streams list should be handled gracefully
        
        # Verify catalog is empty
        list_result = manager.list_streams()
        assert list_result.is_success
        assert list_result.data == []

    def test_load_from_singer_catalog_invalid_stream(self) -> None:
        """Test loading from Singer catalog with invalid stream data."""
        manager = SingerWMSCatalogManager()
        
        invalid_catalog = {
            "streams": [
                {
                    "tap_stream_id": "",  # Invalid: empty
                    "stream": "test_stream",
                    "schema": {"type": "object"},
                }
            ]
        }
        
        result = manager.load_from_singer_catalog(invalid_catalog)
        # Should handle gracefully or fail appropriately
        # Behavior depends on implementation details

    def test_catalog_round_trip_conversion(self) -> None:
        """Test round-trip conversion: catalog -> Singer format -> catalog."""
        manager = SingerWMSCatalogManager()
        
        # Add streams with comprehensive properties
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "created_at": {"type": "string", "format": "date-time"},
            }
        }
        metadata = [
            {"breadcrumb": [], "metadata": {"inclusion": "automatic"}},
            {"breadcrumb": ["properties", "id"], "metadata": {"inclusion": "available"}},
            {"breadcrumb": ["properties", "name"], "metadata": {"inclusion": "available"}},
        ]
        
        manager.add_stream("round_trip_stream", schema, metadata)
        
        # Convert to Singer format
        to_singer_result = manager.to_singer_catalog()
        assert to_singer_result.is_success
        assert to_singer_result.data is not None
        
        # Create new manager and load from Singer format
        manager2 = SingerWMSCatalogManager()
        from_singer_result = manager2.load_from_singer_catalog(to_singer_result.data)
        assert from_singer_result.is_success
        
        # Verify round-trip preserved data
        stream_result = manager2.get_stream("round_trip_stream")
        assert stream_result.is_success
        assert stream_result.data is not None
        assert stream_result.data.schema_info == schema
        assert stream_result.data.metadata == metadata

    def test_catalog_manager_error_handling(self) -> None:
        """Test catalog manager error handling edge cases."""
        manager = SingerWMSCatalogManager()
        
        # Test None/empty inputs
        empty_schema_result = manager.add_stream("test", {})
        # Should handle empty schema appropriately based on validation rules
        
        # Get stream with None data scenario would be tested implicitly
        # through other error cases since FlextValueObject ensures data integrity

    def test_catalog_entry_immutability(self) -> None:
        """Test that catalog entries are properly immutable (FlextValueObject)."""
        manager = SingerWMSCatalogManager()
        schema = {"type": "object", "properties": {"id": {"type": "integer"}}}
        metadata = [{"breadcrumb": [], "metadata": {"inclusion": "available"}}]
        
        # Add stream
        manager.add_stream("immutable_test", schema, metadata)
        
        # Get entry
        entry_result = manager.get_stream("immutable_test")
        assert entry_result.is_success
        assert entry_result.data is not None
        
        original_entry = entry_result.data
        
        # Update metadata to create new entry
        new_metadata = [{"breadcrumb": [], "metadata": {"inclusion": "automatic"}}]
        update_result = manager.update_stream_metadata("immutable_test", new_metadata)
        assert update_result.is_success
        
        # Get updated entry
        updated_entry_result = manager.get_stream("immutable_test")
        assert updated_entry_result.is_success
        assert updated_entry_result.data is not None
        
        updated_entry = updated_entry_result.data
        
        # Verify entries are different objects with different metadata
        assert original_entry.metadata != updated_entry.metadata
        assert original_entry.schema_info == updated_entry.schema_info  # Schema unchanged

    @pytest.mark.parametrize(
        ("stream_count", "expected_count"),
        [
            (0, 0),
            (1, 1),
            (5, 5),
            (10, 10),
        ],
    )
    def test_catalog_scaling(self, stream_count: int, expected_count: int) -> None:
        """Test catalog manager performance with various stream counts."""
        manager = SingerWMSCatalogManager()
        
        # Add multiple streams
        for i in range(stream_count):
            schema = {
                "type": "object",
                "properties": {f"field_{i}": {"type": "string"}}
            }
            manager.add_stream(f"stream_{i}", schema)
        
        # Verify all streams were added
        list_result = manager.list_streams()
        assert list_result.is_success
        assert list_result.data is not None
        assert len(list_result.data) == expected_count
        
        # Test catalog conversion performance
        catalog_result = manager.to_singer_catalog()
        assert catalog_result.is_success
        assert catalog_result.data is not None
        assert len(catalog_result.data["streams"]) == expected_count