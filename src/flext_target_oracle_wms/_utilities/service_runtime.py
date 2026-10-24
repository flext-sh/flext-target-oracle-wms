"""Internal runtime adapters for the target-oracle-wms service facade.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path
from typing import override

from flext_meltano import u

from flext_target_oracle_wms import c, m, p, t
from flext_target_oracle_wms._utilities.client import (
    FlextTargetOracleWmsUtilitiesClient,
)


class FlextTargetOracleWmsServiceRuntime:
    """Service-runtime adapters used by the target-oracle-wms facade."""

    class SingerTarget(m.Meltano.SingerTargetBase):
        """Minimal Singer target used by the service facade."""

        name = c.TargetOracleWms.TARGET_NAME

    class Sink(m.Meltano.SingerSinkBase):
        """Singer sink adapter delegating records to the Oracle WMS runtime."""

        name = "target-oracle-wms-sink"
        _runtime_target: FlextTargetOracleWmsUtilitiesClient.Target

        @classmethod
        def create(
            cls,
            *,
            runtime_target: FlextTargetOracleWmsUtilitiesClient.Target,
            target: m.Meltano.SingerTargetBase,
            stream_name: str,
            schema: t.JsonDict,
            key_properties: t.StrSequence,
        ) -> FlextTargetOracleWmsServiceRuntime.Sink:
            """Create an adapter sink and attach the Oracle WMS runtime target.

            Args:
                runtime_target: Oracle WMS runtime target receiving records.
                target: Singer target base instance owning the sink.
                stream_name: Name of the Singer stream the sink receives.
                schema: Normalized Singer schema for the stream.
                key_properties: Stream key properties for record identity.

            Returns:
                The resulting ``FlextTargetOracleWmsServiceRuntime.Sink``.

            """
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
            """Process a single record through the Oracle WMS runtime.

            Args:
                record: Raw record mapping received for the stream.
                context: Singer record context supplied by the target pipeline.

            Raises:
                RuntimeError: If ``result.failure``.

            """
            _ = context
            result = self._runtime_target.handle_record_message(
                m.Meltano.SingerRecordMessage.model_validate({
                    "type": "RECORD",
                    c.ProcessingMode.STREAM: self.stream_name,
                    "record": u.normalize_to_json_mapping(record),
                }),
            )
            if result.failure:
                msg = result.error or "Oracle WMS runtime rejected the record"
                raise RuntimeError(msg)

        @override
        def process_batch(self, context: t.JsonMapping) -> None:
            """Accept a Singer batch without additional processing.

            Args:
                context: Singer batch context supplied by the target pipeline.

            """
            _ = context

    @classmethod
    def create_sink(
        cls,
        *,
        stream_name: str,
        schema: t.JsonMapping,
        target_config: t.JsonMapping,
    ) -> p.Meltano.SingerDrainSink:
        """Create the service-level Singer sink adapter.

        Args:
            stream_name: Name of the Singer stream the sink receives.
            schema: Singer schema describing the stream's record structure.
            target_config: Scalar target configuration applied to the runtime.

        Returns:
            The resulting ``p.Meltano.SingerDrainSink``.

        Raises:
            RuntimeError: If the Oracle WMS runtime rejects the stream schema.

        """
        normalized_target_config = u.normalize_to_json_mapping(target_config)
        runtime_target = FlextTargetOracleWmsUtilitiesClient.Target(
            normalized_target_config
        )
        normalized_schema = cls.normalize_flat_schema(schema)
        schema_message = m.Meltano.SingerSchemaMessage.model_validate({
            "type": "SCHEMA",
            c.ProcessingMode.STREAM: stream_name,
            "schema": normalized_schema,
            "key_properties": [],
        })
        schema_result = runtime_target.handle_schema_message(schema_message)
        if schema_result.failure:
            msg = schema_result.error or "Oracle WMS runtime rejected the schema"
            raise RuntimeError(msg)
        return cls.Sink.create(
            runtime_target=runtime_target,
            target=cls.SingerTarget(
                config=u.json_dict_adapter().validate_python(normalized_target_config),
                validate_config=False,
            ),
            stream_name=stream_name,
            schema=normalized_schema,
            key_properties=[],
        )

    @staticmethod
    def normalize_flat_schema(schema: t.JsonMapping) -> t.JsonDict:
        """Normalize a flat Singer schema to the WMS runtime contract.

        Args:
            schema: Flat Singer schema mapping to normalize.

        Returns:
            The resulting ``t.JsonDict``.

        """
        return {
            key: (str(value) if isinstance(value, Path) else value)
            for key, value in schema.items()
        }


__all__: list[str] = ["FlextTargetOracleWmsServiceRuntime"]
