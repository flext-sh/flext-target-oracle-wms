"""Utility helpers for target Oracle WMS operations."""

from __future__ import annotations

from collections.abc import Mapping

from flext_core import r
from flext_meltano import FlextMeltanoUtilities
from flext_oracle_wms import FlextOracleWmsUtilities

from flext_target_oracle_wms import t

from .constants import c


class FlextTargetOracleWmsUtilities(FlextMeltanoUtilities, FlextOracleWmsUtilities):
    """Namespace with Singer-target utility helpers."""

    class TargetOracleWms:
        """Helpers for Singer message shape handling."""

        @staticmethod
        def create_record_message(
            stream_name: str,
            record: Mapping[str, t.ContainerValue],
        ) -> Mapping[str, t.ContainerValue | Mapping[str, t.ContainerValue]]:
            """Create a Singer RECORD message payload."""
            return {"type": "RECORD", "stream": stream_name, "record": record}

        @staticmethod
        def create_schema_message(
            stream_name: str,
            schema: Mapping[str, t.ContainerValue],
            key_properties: list[str] | None = None,
        ) -> Mapping[
            str,
            t.ContainerValue | Mapping[str, t.ContainerValue] | list[str],
        ]:
            """Create a Singer SCHEMA message payload."""
            return {
                "type": "SCHEMA",
                "stream": stream_name,
                "schema": schema,
                "key_properties": key_properties or [],
            }

        @staticmethod
        def create_state_message(
            state: Mapping[str, t.ContainerValue],
        ) -> Mapping[str, t.ContainerValue | Mapping[str, t.ContainerValue]]:
            """Create a Singer STATE message payload."""
            return {"type": "STATE", "value": state}

    class Validation:
        """Validation helpers for runtime target configuration."""

        @staticmethod
        def validate_wms_target_config(
            config: Mapping[str, t.ContainerValue],
        ) -> r[bool]:
            """Validate minimal required target configuration fields."""
            required = {"base_url", "username", "password"}
            missing = sorted(key for key in required if key not in config)
            if missing:
                return r[bool].fail(f"Missing required configuration fields: {missing}")
            load_method = config.get(
                "load_method", c.TargetOracleWms.LoadMethods.APPEND_ONLY
            )
            if load_method not in c.TargetOracleWms.LoadMethods.VALID_LOAD_METHODS:
                return r[bool].fail("Invalid load_method")
            return r[bool].ok(value=True)


__all__ = ["FlextTargetOracleWmsUtilities", "u"]
u = FlextTargetOracleWmsUtilities
