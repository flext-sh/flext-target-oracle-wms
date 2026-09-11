"""Shared test helpers for flext-target-oracle-wms test packages.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from tests import c, m

if TYPE_CHECKING:
    from tests import t


def _valid_config() -> t.JsonMapping:
    return {
        "wms_auth": {
            "base_url": "https://test.wms.example.com",
            "username": "user",
            "password": "pass",
        }
    }


def _schema_msg(
    stream: str = "test_stream", key_properties: t.StrSequence | None = None
) -> m.Meltano.SingerSchemaMessage:
    message: m.Meltano.SingerSchemaMessage = (
        m.Meltano.SingerSchemaMessage.model_validate({
            "type": c.Meltano.SingerMessageType.SCHEMA,
            "stream": stream,
            "schema": {"type": "object"},
            "key_properties": key_properties or ["id"],
        })
    )
    return message


def _record_msg(
    stream: str = "test_stream", record: t.JsonMapping | None = None
) -> m.Meltano.SingerRecordMessage:
    return m.Meltano.SingerRecordMessage(
        type=c.Meltano.SingerMessageType.RECORD,
        stream=stream,
        record=record or {"id": "1"},
    )


__all__: list[str] = ["_record_msg", "_schema_msg", "_valid_config"]
