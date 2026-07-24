"""Internal runtime adapters for the target-oracle-wms service facade."""

from __future__ import annotations

from pathlib import Path
from typing import override

from flext_target_oracle_wms import m, p, t, u


class FlextTargetOracleWmsServiceRuntime:
    """Service-runtime adapters used by the target-oracle-wms facade."""

    class Target(m.Meltano.SingerTargetBase):
        """Minimal Singer target used by the service facade."""

        name = "target-oracle-wms"

    class Sink(m.Meltano.SingerSinkBase):
        """Singer sink adapter delegating records to the Oracle WMS runtime."""

        name = "target-oracle-wms-sink"
        _runtime_target: u.TargetOracleWms.Target

        @classmethod
        def create(
            cls,
            *,
            runtime_target: u.TargetOracleWms.Target,
            target: p.Meltano.SingerTargetBase,
            stream_name: str,
            schema: t.JsonDict,
            key_properties: t.StrSequence,
        ) -> FlextTargetOracleWmsServiceRuntime.Sink:
            """Create an adapter sink and attach the Oracle WMS runtime target."""
            service_sink = cls(
                target=target,
                stream_name=stream_name,
                schema=schema,
                key_properties=key_properties,
            )
            service_sink._runtime_target = runtime_target
            return service_sink

        @override
        def process_record(self, record: t.JsonMapping, context: t.JsonMapping) -> None:
            """Process a single record through the Oracle WMS runtime."""
            _ = context
            result = self._runtime_target.handle_record_message(
                m.Meltano.SingerRecordMessage.model_validate({
                    "type": "RECORD",
                    "stream": self.stream_name,
                    "record": u.normalize_to_json_mapping(record),
                })
            )
            if result.failure:
                msg = result.error or "Oracle WMS runtime rejected the record"
                raise RuntimeError(msg)

        @override
        def process_batch(self, context: t.JsonMapping) -> None:
            """Process a batch through the service adapter."""
            _ = context

    @classmethod
    def create_sink(
        cls, *, stream_name: str, schema: t.JsonMapping, target_config: t.ScalarMapping
    ) -> p.Meltano.SingerDrainSink:
        """Create the service-level Singer sink adapter."""
        normalized_target_config = u.normalize_to_json_mapping(target_config)
        runtime_target = u.TargetOracleWms.Target(normalized_target_config)
        normalized_schema = cls.normalize_flat_schema(schema)
        schema_message = m.Meltano.SingerSchemaMessage.model_validate({
            "type": "SCHEMA",
            "stream": stream_name,
            "schema": normalized_schema,
            "key_properties": [],
        })
        schema_result = runtime_target.handle_schema_message(schema_message)
        if schema_result.failure:
            msg = schema_result.error or "Oracle WMS runtime rejected the schema"
            raise RuntimeError(msg)
        return cls.Sink.create(
            runtime_target=runtime_target,
            target=cls.Target(
                config=t.json_dict_adapter().validate_python(normalized_target_config),
                validate_config=False,
            ),
            stream_name=stream_name,
            schema=normalized_schema,
            key_properties=[],
        )

    @staticmethod
    def normalize_flat_schema(schema: t.JsonMapping) -> t.JsonDict:
        """Normalize a flat Singer schema to the WMS runtime contract."""
        return {
            key: (str(value) if isinstance(value, Path) else value)
            for key, value in schema.items()
        }


__all__: list[str] = ["FlextTargetOracleWmsServiceRuntime"]
