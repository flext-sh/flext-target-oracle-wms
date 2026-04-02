"""Internal runtime adapters for the target-oracle-wms service facade."""

from __future__ import annotations

from pathlib import Path
from typing import override

from flext_meltano import (
    FlextMeltanoSingerSinkBase,
    FlextMeltanoSingerTargetBase,
)
from flext_target_oracle_wms import (
    Target as FlextTargetOracleWmsTarget,
    m,
    t,
    u,
)


class FlextTargetOracleWmsServiceRuntime:
    """Service-runtime adapters used by the target-oracle-wms facade."""

    class Target(FlextMeltanoSingerTargetBase):
        """Minimal Singer target used by the service facade."""

        name = "target-oracle-wms"

    class Sink(FlextMeltanoSingerSinkBase):
        """Singer sink adapter delegating records to the Oracle WMS runtime."""

        name = "target-oracle-wms-sink"

        def __init__(
            self,
            *,
            runtime_target: FlextTargetOracleWmsTarget,
            target: FlextMeltanoSingerTargetBase,
            stream_name: str,
            schema: dict[str, t.ContainerValue],
            key_properties: t.StrSequence,
        ) -> None:
            """Initialize the adapter and keep the Oracle WMS runtime target."""
            super().__init__(
                target=target,
                stream_name=stream_name,
                schema=schema,
                key_properties=key_properties,
            )
            self._runtime_target = runtime_target

        @override
        def process_record(
            self,
            record: t.ContainerMapping,
            context: t.ContainerMapping,
        ) -> None:
            """Process a single record through the Oracle WMS runtime."""
            _ = context
            result = self._runtime_target.handle_record_message(
                m.Meltano.SingerRecordMessage.model_validate({
                    "type": "RECORD",
                    "stream": self.stream_name,
                    "record": FlextTargetOracleWmsServiceRuntime.normalize_singer_mapping(
                        record,
                    ),
                }),
            )
            if result.is_failure:
                msg = result.error or "Oracle WMS runtime rejected the record"
                raise RuntimeError(msg)

        @override
        def process_batch(
            self,
            context: t.ContainerMapping,
        ) -> None:
            """Process a batch through the service adapter."""
            _ = context

    @classmethod
    def create_sink(
        cls,
        *,
        stream_name: str,
        schema: t.FlatContainerMapping,
        target_config: t.ContainerMapping,
    ) -> FlextMeltanoSingerSinkBase:
        """Create the service-level Singer sink adapter."""
        normalized_target_config = cls.normalize_singer_mapping(target_config)
        runtime_target = FlextTargetOracleWmsTarget(normalized_target_config)
        normalized_schema = cls.normalize_flat_schema(schema)
        schema_message = m.Meltano.SingerSchemaMessage.model_validate({
            "type": "SCHEMA",
            "stream": stream_name,
            "schema": normalized_schema,
            "key_properties": [],
        })
        schema_result = runtime_target.handle_schema_message(schema_message)
        if schema_result.is_failure:
            msg = schema_result.error or "Oracle WMS runtime rejected the schema"
            raise RuntimeError(msg)
        return cls.Sink(
            runtime_target=runtime_target,
            target=cls.Target(config=normalized_target_config, validate_config=False),
            stream_name=stream_name,
            schema=normalized_schema,
            key_properties=[],
        )

    @classmethod
    def normalize_singer_mapping(
        cls,
        source: t.ContainerMapping,
    ) -> dict[str, t.ContainerValue]:
        """Normalize a Singer payload mapping to the WMS runtime contract."""
        normalized: dict[str, t.ContainerValue] = {}
        for key, value in source.items():
            normalized_value = cls.normalize_singer_value(value)
            if normalized_value is not None:
                normalized[str(key)] = normalized_value
        return normalized

    @classmethod
    def normalize_singer_value(
        cls,
        value: t.NormalizedValue,
    ) -> t.ContainerValue | None:
        """Normalize a Singer payload value to the WMS runtime contract."""
        if value is None:
            return None
        if isinstance(value, Path):
            return str(value)
        if u.is_scalar(value):
            return value
        if u.is_mapping(value):
            return cls.normalize_singer_mapping(value)
        normalized_sequence: list[t.ContainerValue] = []
        for item in value:
            normalized_item = cls.normalize_singer_value(item)
            if normalized_item is not None:
                normalized_sequence.append(normalized_item)
        return normalized_sequence

    @staticmethod
    def normalize_flat_schema(
        schema: t.FlatContainerMapping,
    ) -> dict[str, t.ContainerValue]:
        """Normalize a flat Singer schema to the WMS runtime contract."""
        return {
            key: (str(value) if isinstance(value, Path) else value)
            for key, value in schema.items()
        }


__all__ = ["FlextTargetOracleWmsServiceRuntime"]
