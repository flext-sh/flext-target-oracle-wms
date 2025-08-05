"""Singer WMS catalog management using flext-core patterns."""

from __future__ import annotations

# Import from flext-core for foundational patterns
from flext_core import (
    FlextResult,
    FlextValueObject as FlextDomainBaseModel,
    get_logger,
)
from pydantic import Field

logger = get_logger(__name__)


class SingerWMSCatalogEntry(FlextDomainBaseModel):
    """Singer WMS catalog entry using flext-core patterns."""

    tap_stream_id: str
    stream: str
    schema_info: dict[str, object]
    metadata: list[dict[str, object]] = Field(default_factory=list)
    key_properties: list[str] = Field(default_factory=list)
    bookmark_properties: list[str] = Field(default_factory=list)
    replication_method: str = "FULL_TABLE"
    replication_key: str | None = None

    def validate_domain_rules(self) -> FlextResult[None]:
        """Validate catalog entry domain rules."""
        try:
            if not self.tap_stream_id.strip():
                return FlextResult.fail("tap_stream_id cannot be empty")
            if not self.stream.strip():
                return FlextResult.fail("stream cannot be empty")
            if not self.schema_info:
                return FlextResult.fail("schema_info cannot be empty")
            return FlextResult.ok(None)
        except Exception as e:
            return FlextResult.fail(f"Catalog entry validation failed: {e}")


class SingerWMSCatalogManager:
    """Manage Singer WMS catalog operations using flext-core patterns."""

    def __init__(self) -> None:
        """Initialize Singer WMS catalog manager."""
        self._catalog_entries: dict[str, SingerWMSCatalogEntry] = {}

    def add_stream(
        self,
        stream_name: str,
        schema: dict[str, object],
        metadata: list[dict[str, object]] | None = None,
    ) -> FlextResult[None]:
        """Add WMS stream to catalog."""
        try:
            entry = SingerWMSCatalogEntry(
                tap_stream_id=stream_name,
                stream=stream_name,
                schema_info=schema,
                metadata=metadata or [],
            )

            self._catalog_entries[stream_name] = entry
            logger.info(f"Added WMS stream to catalog: {stream_name}")

            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception(f"Failed to add WMS stream to catalog: {stream_name}")
            return FlextResult.fail(f"Stream addition failed: {e}")

    def get_stream(self, stream_name: str) -> FlextResult[SingerWMSCatalogEntry]:
        """Get WMS stream from catalog."""
        if stream_name not in self._catalog_entries:
            return FlextResult.fail(f"WMS stream not found: {stream_name}")

        return FlextResult.ok(self._catalog_entries[stream_name])

    def list_streams(self) -> FlextResult[list[str]]:
        """List all WMS streams in catalog."""
        try:
            streams = list(self._catalog_entries.keys())
            return FlextResult.ok(streams)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Failed to list WMS streams")
            return FlextResult.fail(f"Stream listing failed: {e}")

    def remove_stream(self, stream_name: str) -> FlextResult[None]:
        """Remove WMS stream from catalog."""
        try:
            if stream_name in self._catalog_entries:
                del self._catalog_entries[stream_name]
                logger.info(f"Removed WMS stream from catalog: {stream_name}")

            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception(f"Failed to remove WMS stream: {stream_name}")
            return FlextResult.fail(f"Stream removal failed: {e}")

    def get_schema_for_stream(self, stream_name: str) -> FlextResult[dict[str, object]]:
        """Get schema for specific WMS stream."""
        stream_result = self.get_stream(stream_name)
        if not stream_result.success:
            return FlextResult.fail(stream_result.error or "Stream not found")

        stream_entry = stream_result.data
        if stream_entry is None:
            return FlextResult.fail("Stream entry is None")
        return FlextResult.ok(stream_entry.schema_info)

    def get_key_properties(self, stream_name: str) -> FlextResult[list[str]]:
        """Get key properties for WMS stream."""
        stream_result = self.get_stream(stream_name)
        if not stream_result.success:
            return FlextResult.fail(stream_result.error or "Stream not found")

        stream_entry = stream_result.data
        if stream_entry is None:
            return FlextResult.fail("Stream entry is None")
        return FlextResult.ok(stream_entry.key_properties)

    def update_stream_metadata(
        self,
        stream_name: str,
        metadata: list[dict[str, object]],
    ) -> FlextResult[None]:
        """Update metadata for WMS stream."""
        try:
            if stream_name not in self._catalog_entries:
                return FlextResult.fail(f"WMS stream not found: {stream_name}")

            # Create updated entry with new metadata (FlextValueObject is immutable)
            current_entry = self._catalog_entries[stream_name]
            updated_entry = SingerWMSCatalogEntry(
                tap_stream_id=current_entry.tap_stream_id,
                stream=current_entry.stream,
                schema_info=current_entry.schema_info,
                metadata=metadata,
                key_properties=current_entry.key_properties,
                bookmark_properties=current_entry.bookmark_properties,
                replication_method=current_entry.replication_method,
                replication_key=current_entry.replication_key,
            )
            self._catalog_entries[stream_name] = updated_entry
            logger.info(f"Updated metadata for WMS stream: {stream_name}")

            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception(f"Failed to update WMS stream metadata: {stream_name}")
            return FlextResult.fail(f"Metadata update failed: {e}")

    def to_singer_catalog(self) -> FlextResult[dict[str, object]]:
        """Convert to Singer catalog format."""
        try:
            streams = []

            for entry in self._catalog_entries.values():
                stream_dict = {
                    "tap_stream_id": entry.tap_stream_id,
                    "stream": entry.stream,
                    "schema": entry.schema_info,
                    "metadata": entry.metadata,
                }

                if entry.key_properties:
                    stream_dict["key_properties"] = entry.key_properties

                if entry.bookmark_properties:
                    stream_dict["bookmark_properties"] = entry.bookmark_properties

                if entry.replication_method:
                    stream_dict["replication_method"] = entry.replication_method

                if entry.replication_key:
                    stream_dict["replication_key"] = entry.replication_key

                streams.append(stream_dict)

            catalog: dict[str, object] = {"streams": streams}

            return FlextResult.ok(catalog)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Failed to convert to Singer WMS catalog")
            return FlextResult.fail(f"Catalog conversion failed: {e}")

    def load_from_singer_catalog(self, catalog: dict[str, object]) -> FlextResult[None]:
        """Load from Singer catalog format."""
        try:
            self._catalog_entries.clear()

            streams = catalog.get("streams", [])
            if not isinstance(streams, list):
                return FlextResult.fail(
                    "Invalid catalog format: streams must be a list",
                )

            for stream_dict in streams:
                if not isinstance(stream_dict, dict):
                    continue
                stream_name = stream_dict.get("stream")

                # Validate stream_name is a string
                if not isinstance(stream_name, str):
                    continue

                entry = SingerWMSCatalogEntry(
                    tap_stream_id=stream_dict.get("tap_stream_id", stream_name),
                    stream=stream_name,
                    schema_info=stream_dict["schema"],
                    metadata=stream_dict.get("metadata", []),
                    key_properties=stream_dict.get("key_properties", []),
                    bookmark_properties=stream_dict.get("bookmark_properties", []),
                    replication_method=stream_dict.get(
                        "replication_method",
                        "FULL_TABLE",
                    ),
                    replication_key=stream_dict.get("replication_key"),
                )

                self._catalog_entries[stream_name] = entry

            logger.info(
                f"Loaded {len(self._catalog_entries)} WMS streams from Singer catalog",
            )

            return FlextResult.ok(None)

        except (RuntimeError, ValueError, TypeError) as e:
            logger.exception("Failed to load Singer WMS catalog")
            return FlextResult.fail(f"Catalog loading failed: {e}")
